#!/usr/bin/env python3
"""
Graduation Memory Video — Video Assembler

Assembles transition videos or images into a crossfade montage.
Supports variable-duration clips for cinematic pacing.

Usage (from videos):
  python3 assemble_video.py --videos v1.mp4,v2.mp4,...,v6.mp4 \
    --crossfade 0.6 --fade_out 1.5 --output graduation_memory.mp4

Usage (from images — moviepy fallback when no Kling available):
  python3 assemble_video.py --images img1.png,img2.png,...,img6.png \
    --durations 2.5,2.5,3.5,3,3,4 --crossfade 0.6 --fade_out 1.5 \
    --output graduation_memory.mp4
"""

import argparse
import os
import sys


def assemble_from_videos(video_paths, crossfade, fade_out, output, resolution, fps):
    """Assemble pre-generated transition videos with crossfade."""
    try:
        from moviepy import VideoFileClip, concatenate_videoclips
    except ImportError:
        print("ERROR: moviepy not installed. Install with: pip install moviepy")
        sys.exit(1)

    clips = []
    for path in video_paths:
        clip = VideoFileClip(path)
        # Resize to target resolution if needed
        if clip.size != resolution:
            clip = clip.resized(resolution)
        clips.append(clip)

    # Concatenate with crossfade method
    # moviepy v2.x: use concatenate_videoclips with method="compose"
    final = concatenate_videoclips(clips, method="compose")

    # Add fade-out at end
    if fade_out > 0:
        final = final.with_effects([final.fadeout(fade_out)])

    final.write_videofile(output, fps=fps, codec="libx264", audio=False)
    print(f"Saved: {output}")


def assemble_from_images(image_paths, durations, crossfade, fade_out, output, resolution, fps):
    """Assemble images into a crossfade montage with variable durations."""
    try:
        from moviepy import ImageClip, concatenate_videoclips
    except ImportError:
        print("ERROR: moviepy not installed. Install with: pip install moviepy")
        sys.exit(1)

    clips = []
    for i, (path, dur) in enumerate(zip(image_paths, durations)):
        clip = ImageClip(path).with_duration(dur).resized(resolution)
        # Add crossfade transition
        if crossfade > 0:
            clip = clip.with_effects([clip.crossfadein(crossfade)])
        clips.append(clip)

    # Concatenate with crossfade
    final = concatenate_videoclips(clips, method="compose")

    # Add fade-out at end
    if fade_out > 0:
        final = final.with_effects([final.fadeout(fade_out)])

    final.write_videofile(output, fps=fps, codec="libx264", audio=False)
    print(f"Saved: {output}")


def main():
    parser = argparse.ArgumentParser(description="Assemble graduation memory video")
    parser.add_argument("--videos", default=None,
                        help="Comma-separated video file paths")
    parser.add_argument("--images", default=None,
                        help="Comma-separated image file paths (fallback mode)")
    parser.add_argument("--durations", default="2.5,2.5,3.5,3,3,4",
                        help="Comma-separated clip durations in seconds (for image mode)")
    parser.add_argument("--crossfade", type=float, default=0.6,
                        help="Crossfade overlap duration in seconds")
    parser.add_argument("--fade_out", type=float, default=1.5,
                        help="Fade-out duration at video end in seconds")
    parser.add_argument("--output", default="graduation_memory.mp4",
                        help="Output video file path")
    parser.add_argument("--resolution", default="720x1280",
                        help="Target resolution (width x height)")
    parser.add_argument("--fps", type=int, default=30,
                        help="Frames per second")
    args = parser.parse_args()

    # Parse resolution
    w, h = args.resolution.split("x")
    resolution = (int(w), int(h))

    if args.videos:
        video_paths = args.videos.split(",")
        assemble_from_videos(video_paths, args.crossfade, args.fade_out,
                             args.output, resolution, args.fps)
    elif args.images:
        image_paths = args.images.split(",")
        durations = [float(d) for d in args.durations.split(",")]
        if len(image_paths) != len(durations):
            print(f"ERROR: {len(image_paths)} images but {len(durations)} durations")
            sys.exit(1)
        assemble_from_images(image_paths, durations, args.crossfade, args.fade_out,
                             args.output, resolution, args.fps)
    else:
        print("ERROR: Provide --videos or --images")
        sys.exit(1)


if __name__ == "__main__":
    main()
