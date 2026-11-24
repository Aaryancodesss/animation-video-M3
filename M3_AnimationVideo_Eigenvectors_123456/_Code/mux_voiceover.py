"""
mux_voiceover.py
----------------
Multiplexes an audio track with _Video.mp4 to produce a final MP4
containing both video and high-fidelity synchronized audio.
"""

import sys
from pathlib import Path
import av

def mux(video_path: Path, audio_path: Path, output_path: Path):
    print("=" * 65)
    print("MUXING VIDEO & AUDIO WITH PyAV")
    print("=" * 65)
    print(f"Video input  : {video_path}")
    print(f"Audio input  : {audio_path}")
    print(f"Output file  : {output_path}")
    
    v_in = av.open(str(video_path))
    a_in = av.open(str(audio_path))
    
    v_stream = v_in.streams.video[0]
    a_stream = a_in.streams.audio[0]
    
    output_container = av.open(str(output_path), mode="w", format="mp4")
    
    # Configure video stream (copy parameters)
    out_v = output_container.add_stream("h264", rate=30)
    out_v.width = v_stream.width
    out_v.height = v_stream.height
    out_v.pix_fmt = "yuv420p"
    
    # Configure audio stream
    out_a = output_container.add_stream("aac", rate=44100)
    out_a.layout = "mono"
    
    print("\nMultiplexing video packets...")
    v_packets = 0
    for packet in v_in.demux(v_stream):
        if packet.dts is None:
            continue
        packet.stream = out_v
        output_container.mux(packet)
        v_packets += 1
        
    print(f"Muxed {v_packets} video packets.")
    
    print("Encoding and multiplexing audio frames...")
    a_packets = 0
    for frame in a_in.decode(a_stream):
        for packet in out_a.encode(frame):
            output_container.mux(packet)
            a_packets += 1
            
    for packet in out_a.encode():
        output_container.mux(packet)
        a_packets += 1
        
    print(f"Muxed {a_packets} audio packets.")
    
    output_container.close()
    v_in.close()
    a_in.close()
    
    print("\nAudit of output file:")
    with av.open(str(output_path)) as c:
        vs = c.streams.video[0]
        as_ = c.streams.audio[0]
        v_dur = float(vs.duration * vs.time_base) if vs.duration else float(c.duration / av.time_base)
        a_dur = float(as_.duration * as_.time_base) if as_.duration else float(c.duration / av.time_base)
        print(f"Video: {vs.width}x{vs.height} @ {float(vs.average_rate):.1f} fps, Duration: {v_dur:.2f}s")
        print(f"Audio: {as_.channels} ch, {as_.rate} Hz {as_.codec_context.name}, Duration: {a_dur:.2f}s")
        print(f"Size : {output_path.stat().st_size / (1024*1024):.2f} MB")
        
    print("=" * 65)
    print("MUXING COMPLETED SUCCESSFULLY!")

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    v_file = base_dir / "_Video.mp4"
    
    if len(sys.argv) > 1:
        a_file = Path(sys.argv[1]).resolve()
    else:
        a_file = base_dir / "media" / "master_voiceover.wav"
        
    out_file = base_dir / "_Video_with_Voiceover.mp4"
    mux(v_file, a_file, out_file)
