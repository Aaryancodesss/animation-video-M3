"""
render_and_combine.py
---------------------
Orchestrates rendering all 8 scenes of the Eigenvalues & Eigenvectors
animation project at full 1080p (1920x1080, 30fps), concatenates them
into a single final MP4, and verifies total duration and quality.
"""

import sys
import time
from pathlib import Path
import av
from manim import config

# Set global quality to 1080p @ 30fps
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.media_dir = str(Path(__file__).resolve().parent.parent / "media")

# Import the scene classes
from scenes import (
    TitleScene,
    HookScene,
    ConceptIntroScene,
    VisualIntuitionScene,
    WorkedExampleScene,
    InterpretationScene,
    SummaryScene,
    ClosingScene
)

SCENE_CLASSES = [
    TitleScene,
    HookScene,
    ConceptIntroScene,
    VisualIntuitionScene,
    WorkedExampleScene,
    InterpretationScene,
    SummaryScene,
    ClosingScene
]

def render_scenes():
    print("=" * 65)
    print("STEP 1: RENDERING ALL 8 SCENES (1080p @ 30 FPS)")
    print("=" * 65)
    
    rendered_files = []
    video_dir = Path(config.media_dir) / "videos" / "scenes" / "1080p30"
    
    for idx, scene_cls in enumerate(SCENE_CLASSES, 1):
        name = scene_cls.__name__
        print(f"\n[{idx}/8] Rendering {name}...")
        t0 = time.time()
        scene = scene_cls()
        scene.render()
        elapsed = time.time() - t0
        
        expected_path = Path(scene.renderer.file_writer.movie_file_path)
        if not expected_path.exists():
            raise FileNotFoundError(f"Expected output video not found: {expected_path}")
            
        with av.open(str(expected_path)) as c:
            st = c.streams.video[0]
            dur = float(st.duration * st.time_base) if st.duration else float(c.duration / av.time_base)
            print(f"       -> Done in {elapsed:.1f}s | Duration: {dur:.2f}s ({int(dur//60)}m {int(dur%60)}s)")
            
        rendered_files.append(expected_path)
        
    return rendered_files

def concatenate_videos(input_files, output_path):
    print("\n" + "=" * 65)
    print("STEP 2: CONCATENATING SCENES INTO FINAL MP4")
    print("=" * 65)
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Setup output container
    output_container = av.open(str(output_path), mode="w", format="mp4")
    out_stream = output_container.add_stream("libx264", rate=30)
    out_stream.width = 1920
    out_stream.height = 1080
    out_stream.pix_fmt = "yuv420p"
    out_stream.options = {"preset": "fast", "crf": "18"}
    
    total_pts = 0
    total_frames = 0
    
    for in_idx, in_file in enumerate(input_files, 1):
        print(f"Merging [{in_idx}/8]: {in_file.name}...")
        with av.open(str(in_file)) as in_container:
            in_stream = in_container.streams.video[0]
            for packet in in_container.demux(in_stream):
                for frame in packet.decode():
                    new_frame = av.VideoFrame.from_ndarray(frame.to_ndarray(format="rgb24"), format="rgb24")
                    new_frame.pts = total_pts
                    total_pts += 1
                    total_frames += 1
                    for out_packet in out_stream.encode(new_frame):
                        output_container.mux(out_packet)
                        
    # Flush output stream
    for out_packet in out_stream.encode():
        output_container.mux(out_packet)
        
    output_container.close()
    print(f"\nFinal concatenated MP4 successfully written to:\n{output_path}")

def verify_final_video(video_path):
    print("\n" + "=" * 65)
    print("STEP 3: FINAL VIDEO METRICS & AUDIT")
    print("=" * 65)
    
    with av.open(str(video_path)) as c:
        st = c.streams.video[0]
        dur = float(st.duration * st.time_base) if st.duration else float(c.duration / av.time_base)
        fps = float(st.average_rate)
        width = st.width
        height = st.height
        size_mb = video_path.stat().st_size / (1024 * 1024)
        
    minutes = int(dur // 60)
    seconds = int(dur % 60)
    
    print(f"File Path    : {video_path}")
    print(f"File Size    : {size_mb:.2f} MB")
    print(f"Resolution   : {width} x {height} (16:9)")
    print(f"Frame Rate   : {fps:.1f} fps")
    print(f"Duration     : {dur:.2f} seconds ({minutes} min {seconds} sec)")
    
    assert width == 1920 and height == 1080, f"Expected 1920x1080, got {width}x{height}"
    assert fps >= 30, f"Expected >= 30 fps, got {fps}"
    assert 180 <= dur <= 420, f"Duration {dur}s outside expected 3-7 minute range!"
    
    print("\nALL VIDEO SPECIFICATIONS CONFIRMED!")
    print("=" * 65)

if __name__ == "__main__":
    rendered = render_scenes()
    final_output = Path(__file__).resolve().parent.parent / "_Video.mp4"
    concatenate_videos(rendered, final_output)
    verify_final_video(final_output)
