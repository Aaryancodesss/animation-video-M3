"""
perfect_render.py
-----------------
Uses the embedded FFmpeg binary from imageio-ffmpeg to concatenate all 8 scenes
and mux the master voiceover audio track into a broadcast-quality MP4 that is
100% compatible with QuickTime Player, macOS Quick Look, browsers, and VLC.
"""

import subprocess
from pathlib import Path
import imageio_ffmpeg

FFMPEG_BIN = imageio_ffmpeg.get_ffmpeg_exe()
BASE_DIR = Path(__file__).resolve().parent.parent
SCENE_DIR = BASE_DIR / "media" / "videos" / "1080p30"
AUDIO_FILE = BASE_DIR / "media" / "master_voiceover.wav"
FINAL_VIDEO = BASE_DIR / "_Video.mp4"
FINAL_VOICEOVER_VIDEO = BASE_DIR / "_Video_with_Voiceover.mp4"

SCENES = [
    "TitleScene",
    "HookScene",
    "ConceptIntroScene",
    "VisualIntuitionScene",
    "WorkedExampleScene",
    "InterpretationScene",
    "SummaryScene",
    "ClosingScene"
]

def main():
    print("=" * 65)
    print("PRODUCING 100% QUICKTIME-COMPATIBLE VIDEO WITH VOICE-OVER")
    print("=" * 65)
    
    # 1. Create ffmpeg concat list file
    concat_list_path = BASE_DIR / "media" / "concat_list.txt"
    with open(concat_list_path, "w") as f:
        for s in SCENES:
            scene_path = SCENE_DIR / f"{s}.mp4"
            if not scene_path.exists():
                raise FileNotFoundError(f"Missing scene: {scene_path}")
            f.write(f"file '{scene_path}'\n")
            
    print(f"Created concat list with {len(SCENES)} scenes.")
    
    # 2. Run FFmpeg to concatenate video and mux audio
    # -safe 0 -f concat -i concat_list.txt
    # -i master_voiceover.wav
    # -c:v libx264 -pix_fmt yuv420p -profile:v high -level 4.0 -preset fast -crf 18
    # -c:a aac -b:a 192k -ar 44100
    # -movflags +faststart
    cmd = [
        FFMPEG_BIN,
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list_path),
        "-i", str(AUDIO_FILE),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-profile:v", "high",
        "-level", "4.0",
        "-preset", "medium",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar", "44100",
        "-movflags", "+faststart",
        str(FINAL_VIDEO)
    ]
    
    print("\nExecuting FFmpeg assembly...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("FFmpeg Error:\n", res.stderr)
        raise RuntimeError("FFmpeg concatenation failed!")
        
    print(f"\nFinal video successfully written to:\n{FINAL_VIDEO}")
    
    # Copy to _Video_with_Voiceover.mp4 as well
    import shutil
    shutil.copy2(FINAL_VIDEO, FINAL_VOICEOVER_VIDEO)
    print(f"Also saved copy to:\n{FINAL_VOICEOVER_VIDEO}")
    
    # Inspect final file metrics
    probe_cmd = [
        FFMPEG_BIN,
        "-i", str(FINAL_VIDEO)
    ]
    probe = subprocess.run(probe_cmd, capture_output=True, text=True)
    print("\n" + "=" * 65)
    print("FINAL MEDIA INSPECTION")
    print("=" * 65)
    for line in probe.stderr.splitlines():
        if "Duration" in line or "Stream #" in line:
            print("  ", line.strip())
    print("=" * 65)

if __name__ == "__main__":
    main()
