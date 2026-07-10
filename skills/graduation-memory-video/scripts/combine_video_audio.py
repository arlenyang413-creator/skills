#!/usr/bin/env python3
"""
Graduation Memory Video — Combine Video + Audio

Merges a video file with an audio file into a final video.
Uses moviepy when ffmpeg is not available.

Usage:
  python3 combine_video_audio.py \
    --video graduation_memory.mp4 \
    --audio piano_accompaniment.wav \
    --output graduation_memory_final.mp4 \
    --volume 0.35
"""

import argparse
import sys


def combine(video_path, audio_path, output, volume, fps):
    """Combine video and audio using moviepy."""
    try:
        from moviepy import VideoFileClip, AudioFileClip
    except ImportError:
        print("ERROR: moviepy not installed. Install with: pip install moviepy")
        sys.exit(1)

    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    # Adjust audio volume
    if volume < 1.0:
        audio = audio.with_volume_set(volume)

    # Trim audio to match video duration
    if audio.duration > video.duration:
        audio = audio.subclipped(0, video.duration)

    # Set audio on video
    final = video.with_audio(audio)

    final.write_videofile(output, fps=fps, codec="libx264", audio_codec="aac")
    print(f"Saved final video: {output}")
    print(f"  Duration: {final.duration:.1f}s")
    print(f"  Resolution: {final.size}")

    video.close()
    audio.close()
    final.close()


def main():
    parser = argparse.ArgumentParser(description="Combine video and audio files")
    parser.add_argument("--video", required=True, help="Video file path")
    parser.add_argument("--audio", required=True, help="Audio file path")
    parser.add_argument("--output", default="graduation_memory_final.mp4",
                        help="Output file path")
    parser.add_argument("--volume", type=float, default=0.35,
                        help="Audio volume (0.0-1.0, default 0.35 for background music)")
    parser.add_argument("--fps", type=int, default=30, help="Video FPS")
    args = parser.parse_args()

    combine(args.video, args.audio, args.output, args.volume, args.fps)


if __name__ == "__main__":
    main()
