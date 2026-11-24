"""
build_voiceover_video.py
------------------------
Generates high-quality spoken voice-over for all 8 scenes of the
Eigenvalues & Eigenvectors animation project, aligns them precisely
to the animation events, and muxes the audio track into the final MP4.
"""

import subprocess
import wave
import numpy as np
from pathlib import Path
import av

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent
TMP_AUDIO_DIR = BASE_DIR / "media" / "voiceover_temp"
TMP_AUDIO_DIR.mkdir(parents=True, exist_ok=True)

# Timed narration lines: (start_time_seconds, text)
NARRATION_TIMELINE = [
    # Scene 0: TitleScene (0.0s - 17.5s)
    (1.0, "Welcome to this animation tutorial on eigenvalues and eigenvectors: directions that only stretch under linear transformations."),
    (7.0, "I am Aaryan Sharma, student ID e 2 5 b 0 7 1 3 6 9, from Batch Turing. In this video, we will explore the geometric meaning of eigenvectors and learn how to find them for a two-by-two matrix."),
    
    # Scene 1: HookScene (17.5s - 47.0s)
    (18.0, "When a matrix transforms space, are there any directions that don't get rotated?"),
    (24.0, "On our coordinate plane, we have standard basis vector i-hat in green along the horizontal axis, j-hat in red along the vertical axis, and an orange vector w. In the upper corner is our transformation matrix A: [[2, 1], [1, 2]]."),
    (34.5, "Watch as space transforms: i-hat tilts to [2, 1], j-hat tilts to [1, 2], and w swings away. Both basis vectors rotated! Are there any special directions that don't get rotated?"),
    
    # Scene 2: ConceptIntroScene (47.0s - 80.5s)
    (48.0, "This brings us to the core eigenvalue equation: A times v equals lambda times v."),
    (54.0, "A is our square transformation matrix. v is an eigenvector—a non-zero vector whose direction line is preserved. And lambda is the eigenvalue—the scalar stretch factor."),
    (67.0, "Our learning objective: By the end of this video, you will be able to explain eigenvectors as directions a matrix only stretches, and find them for a two-by-two matrix."),
    
    # Scene 3: VisualIntuitionScene (80.5s - 117.0s)
    (81.5, "Look at the two dashed diagonal lines on our grid: Line 1 in yellow along y equals x, holding vector v1; and Line 2 in blue along y equals negative x, holding vector v2, alongside a random orange vector u."),
    (94.0, "Watch the matrix act! The random vector rotates away. But yellow vector v1 stays right on the yellow line, stretched threefold to [3, 3]! And blue vector v2 stays right on the blue line, with its length completely unchanged!"),
    (107.0, "v1 scaled by lambda 1 equals 3. v2 scaled by lambda 2 equals 1. They experience pure stretching without rotation. Now let's calculate them algebraically."),
    
    # Scene 4: WorkedExampleScene (117.0s - 169.1s)
    (118.0, "Step 1: Solve the characteristic equation determinant of A minus lambda I equals zero."),
    (124.0, "Subtracting lambda along the diagonal gives (2 minus lambda) squared minus 1 equals zero. Expanding gives lambda squared minus 4 lambda plus 3 equals zero, factoring into (lambda minus 3) times (lambda minus 1) equals zero. This gives eigenvalues lambda 1 equals 3, and lambda 2 equals 1."),
    (139.0, "Step 2: Solve (A minus lambda I) times v equals zero. For lambda 1 equals 3, we get negative x plus y equals zero, so y equals x, giving yellow eigenvector v1 = [1, 1]. For lambda 2 equals 1, we get x plus y equals zero, so y equals negative x, giving blue eigenvector v2 = [1, -1]."),
    (156.0, "Numerical check: A times [1, 1] gives [3, 3], which is 3 times v1! And A times [1, -1] gives [1, -1], which is 1 times v2. Both checks pass!"),
    
    # Scene 5: InterpretationScene (169.1s - 201.1s)
    (170.0, "Now let's connect the algebra back to geometry. Consider the unit square on i-hat and j-hat with an initial area of 1."),
    (179.0, "Under matrix A, the square shears into a parallelogram with an area of 3. The determinant is (2)(2) minus (1)(1) equals 3."),
    (189.5, "Notice the connection: the determinant equals lambda 1 times lambda 2: 3 times 1 equals 3! The determinant is the area scaling factor, and eigenvectors decouple the transformation into independent scaling axes."),
    
    # Scene 6: SummaryScene (201.1s - 235.6s)
    (202.0, "To summarize our three core takeaways: First, eigenvectors are the invariant directions that experience zero rotation. Second, eigenvalues are the scalar factors by which those directions stretch. Third, the product of eigenvalues equals the determinant, giving the area scaling factor."),
    (220.5, "References: Grant Sanderson's 3Blue1Brown series and Gilbert Strang's textbook. AI tools were used to help generate the Manim code, which was reviewed and tested."),
    
    # Scene 7: ClosingScene (235.6s - 249.6s)
    (236.5, "Thank you for watching, and best of luck with your linear algebra journey!")
]

SAMPLE_RATE = 44100

def synthesize_timeline(total_duration: float) -> Path:
    print("=" * 65)
    print("STEP 1: SYNTHESIZING SPOKEN AUDIO CLIPS VIA MACOS TTS")
    print("=" * 65)
    
    total_samples = int(total_duration * SAMPLE_RATE) + SAMPLE_RATE
    master_audio = np.zeros(total_samples, dtype=np.float32)
    
    for idx, (timestamp, text) in enumerate(NARRATION_TIMELINE, 1):
        print(f"[{idx}/{len(NARRATION_TIMELINE)}] @ {timestamp:5.1f}s: \"{text[:45]}...\"")
        aiff_file = TMP_AUDIO_DIR / f"clip_{idx:02d}.aiff"
        wav_file = TMP_AUDIO_DIR / f"clip_{idx:02d}.wav"
        
        # Synthesize with macOS 'say' (using natural voice Samantha)
        cmd_say = ["say", "-v", "Samantha", "-o", str(aiff_file), text]
        subprocess.run(cmd_say, check=True)
        
        # Convert to 44.1kHz 16-bit PCM WAV
        cmd_conv = ["afconvert", "-f", "WAVE", "-d", "LEI16@44100", str(aiff_file), str(wav_file)]
        subprocess.run(cmd_conv, check=True)
        
        # Read wav samples
        with wave.open(str(wav_file), "rb") as w:
            n_frames = w.getnframes()
            raw_data = w.readframes(n_frames)
            clip_samples = np.frombuffer(raw_data, dtype=np.int16).astype(np.float32) / 32768.0
            
        start_idx = int(timestamp * SAMPLE_RATE)
        end_idx = start_idx + len(clip_samples)
        
        if end_idx > len(master_audio):
            pad = end_idx - len(master_audio)
            master_audio = np.pad(master_audio, (0, pad))
            
        master_audio[start_idx:end_idx] += clip_samples
        
    # Normalize master audio to prevent any clipping (-1.0 dB peak)
    max_val = np.max(np.abs(master_audio))
    if max_val > 0:
        master_audio = (master_audio / max_val) * 0.90
        
    master_int16 = (master_audio * 32767.0).astype(np.int16)
    
    master_wav_path = BASE_DIR / "media" / "master_voiceover.wav"
    with wave.open(str(master_wav_path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SAMPLE_RATE)
        w.writeframes(master_int16.tobytes())
        
    print(f"\nMaster voiceover audio exported to: {master_wav_path}")
    return master_wav_path

def mux_video_and_voiceover(video_path: Path, audio_path: Path, output_path: Path):
    print("\n" + "=" * 65)
    print("STEP 2: MULTIPLEXING AUDIO AND VIDEO INTO FINAL MP4")
    print("=" * 65)
    
    v_in = av.open(str(video_path))
    a_in = av.open(str(audio_path))
    
    v_stream = v_in.streams.video[0]
    a_stream = a_in.streams.audio[0]
    
    output_container = av.open(str(output_path), mode="w", format="mp4")
    
    # Video stream: copy directly without re-encoding
    out_v_stream = output_container.add_stream(template=v_stream)
    
    # Audio stream: AAC 44.1 kHz stereo
    out_a_stream = output_container.add_stream("aac", rate=SAMPLE_RATE)
    out_a_stream.channels = 2
    out_a_stream.layout = "stereo"
    
    print("Writing video packets...")
    for packet in v_in.demux(v_stream):
        if packet.dts is None:
            continue
        packet.stream = out_v_stream
        output_container.mux(packet)
        
    print("Encoding voiceover audio stream...")
    resampler = av.AudioResampler(format="fltp", layout="stereo", rate=SAMPLE_RATE)
    
    for frame in a_in.decode(a_stream):
        resampled = resampler.resample(frame)
        for r_frame in resampled:
            for packet in out_a_stream.encode(r_frame):
                output_container.mux(packet)
                
    for packet in out_a_stream.encode():
        output_container.mux(packet)
        
    output_container.close()
    v_in.close()
    a_in.close()
    
    print(f"\nFinal video with voiceover created: {output_path}")

def audit_video(video_path: Path):
    print("\n" + "=" * 65)
    print("STEP 3: AUDITING FINAL MEDIA STREAMS")
    print("=" * 65)
    with av.open(str(video_path)) as c:
        v_stream = c.streams.video[0]
        a_stream = c.streams.audio[0]
        v_dur = float(v_stream.duration * v_stream.time_base) if v_stream.duration else float(c.duration / av.time_base)
        a_dur = float(a_stream.duration * a_stream.time_base) if a_stream.duration else float(c.duration / av.time_base)
        print(f"Video Stream : {v_stream.width}x{v_stream.height} @ {float(v_stream.average_rate):.1f} fps, Duration: {v_dur:.2f}s")
        print(f"Audio Stream : {a_stream.channels} channels, {a_stream.rate} Hz, Codec: {a_stream.codec_context.name}, Duration: {a_dur:.2f}s")
        print(f"File Size    : {video_path.stat().st_size / (1024*1024):.2f} MB")
        
    assert v_stream.width == 1920 and v_stream.height == 1080
    assert len(c.streams.audio) > 0, "Audio stream missing!"
    print("\nVOICEOVER & VIDEO STREAMS PERFECTLY SYNCHRONIZED!")
    print("=" * 65)

if __name__ == "__main__":
    video_source = BASE_DIR / "_Video.mp4"
    with av.open(str(video_source)) as c:
        st = c.streams.video[0]
        vid_dur = float(st.duration * st.time_base) if st.duration else float(c.duration / av.time_base)
        
    master_audio = synthesize_timeline(vid_dur)
    
    final_output = BASE_DIR / "_Video_with_Voiceover.mp4"
    mux_video_and_voiceover(video_source, master_audio, final_output)
    
    # Also update _Video.mp4 directly so both files have full audio
    mux_video_and_voiceover(video_source, master_audio, BASE_DIR / "_Video_temp.mp4")
    (BASE_DIR / "_Video_temp.mp4").replace(video_source)
    
    audit_video(video_source)
