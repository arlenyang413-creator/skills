#!/usr/bin/env python3
"""
Graduation Memory Video — Piano Music Generator

Two modes:
  --method suno  : Call Suno API for professional AI-generated piano solo
  --method wave  : Generate simple piano melody using Python wave module (fallback)

Usage:
  python3 generate_music.py --method suno --style "warm piano solo" --duration 18 --output piano.mp3
  python3 generate_music.py --method wave --duration 18 --output piano.wav
"""

import argparse
import json
import os
import struct
import sys
import time
import urllib.request
import urllib.error
import wave as wave_module


# ─── Suno API Mode ───────────────────────────────────────────────────────────

def generate_suno(style: str, duration: int, output: str) -> None:
    """Generate piano music via Suno API."""
    api_key = os.environ.get("SUNO_API_KEY")
    if not api_key:
        print("ERROR: SUNO_API_KEY not set. Falling back to wave mode.")
        generate_wave(duration, output.replace(".mp3", ".wav"))
        return

    # Suno API endpoint (adjust if using a different Suno API provider)
    suno_base = os.environ.get("SUNO_API_BASE", "https://api.suno.ai/v1")

    prompt = f"{style}, {duration} seconds duration, gentle sentimental melody, no vocals"

    payload = json.dumps({
        "prompt": prompt,
        "duration": duration,
        "output_format": "mp3",
    }).encode("utf-8")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    print(f"Requesting Suno API: {prompt}")

    try:
        req = urllib.request.Request(
            f"{suno_base}/generate",
            data=payload,
            headers=headers,
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))

        # Suno returns a URL or task ID; polling for completion
        if "url" in result:
            download_url = result["url"]
            print(f"Downloading generated music from: {download_url}")
            urllib.request.urlretrieve(download_url, output)
            print(f"Saved: {output}")
        elif "id" in result:
            # Poll for task completion
            task_id = result["id"]
            print(f"Task ID: {task_id}, polling for completion...")
            for attempt in range(30):
                time.sleep(5)
                poll_req = urllib.request.Request(
                    f"{suno_base}/tasks/{task_id}",
                    headers=headers,
                    method="GET",
                )
                with urllib.request.urlopen(poll_req, timeout=30) as poll_resp:
                    poll_result = json.loads(poll_resp.read().decode("utf-8"))
                status = poll_result.get("status", "unknown")
                print(f"  Poll {attempt+1}: status={status}")
                if status == "completed" and "url" in poll_result:
                    urllib.request.urlretrieve(poll_result["url"], output)
                    print(f"Saved: {output}")
                    return
                if status == "failed":
                    print(f"ERROR: Suno task failed: {poll_result.get('error', 'unknown')}")
                    print("Falling back to wave mode.")
                    generate_wave(duration, output.replace(".mp3", ".wav"))
                    return
            print("ERROR: Suno task timed out. Falling back to wave mode.")
            generate_wave(duration, output.replace(".mp3", ".wav"))
        else:
            print(f"ERROR: Unexpected Suno response: {result}")
            print("Falling back to wave mode.")
            generate_wave(duration, output.replace(".mp3", ".wav"))

    except urllib.error.URLError as e:
        print(f"ERROR: Suno API request failed: {e}")
        print("Falling back to wave mode.")
        generate_wave(duration, output.replace(".mp3", ".wav"))
    except Exception as e:
        print(f"ERROR: Unexpected error with Suno: {e}")
        print("Falling back to wave mode.")
        generate_wave(duration, output.replace(".mp3", ".wav"))


# ─── Wave Fallback Mode ──────────────────────────────────────────────────────

# Note frequencies (C3 through E5)
NOTES = {
    "C3": 130.81, "C#3": 138.59, "D3": 146.83, "D#3": 155.56, "E3": 164.81,
    "F3": 174.61, "F#3": 185.00, "G3": 196.00, "G#3": 207.65, "A3": 220.00,
    "A#3": 233.08, "B3": 246.94,
    "C4": 261.63, "C#4": 277.18, "D4": 293.66, "D#4": 311.13, "E4": 329.63,
    "F4": 349.23, "F#4": 369.99, "G4": 392.00, "G#4": 415.30, "A4": 440.00,
    "A#4": 466.16, "B4": 493.88,
    "C5": 523.25, "D5": 587.33, "E5": 659.25,
}

# Simple sentimental piano melody (note, duration_in_beats)
# Beat = 0.4s at tempo 150 BPM equivalent
MELODY = [
    # Opening — gentle, nostalgic
    ("E4", 2), ("G4", 1), ("A4", 2), ("G4", 1),
    ("E4", 2), ("D4", 1), ("E4", 3),
    # Building — hope and growth
    ("G4", 2), ("A4", 1), ("B4", 2), ("A4", 1),
    ("G4", 2), ("E4", 1), ("G4", 3),
    # Peak — achievement
    ("C5", 2), ("B4", 1), ("A4", 2), ("G4", 1),
    ("A4", 2), ("B4", 1), ("C5", 3),
    # Reflection — soft, warm
    ("E4", 2), ("G4", 1), ("A4", 2), ("G4", 1),
    ("E4", 3), ("D4", 2), ("C4", 4),
]


def generate_wave(duration: int, output: str) -> None:
    """Generate a simple piano melody using Python wave module."""
    sample_rate = 44100
    beat_duration = 0.4  # seconds per beat unit
    fade_out_seconds = 2.0

    total_samples = int(sample_rate * duration)
    audio_data = bytearray(total_samples * 2)  # 16-bit mono

    current_sample = 0
    for note_name, beats in MELODY:
        freq = NOTES.get(note_name, 261.63)
        note_samples = int(sample_rate * beat_duration * beats)

        for i in range(note_samples):
            if current_sample + i >= total_samples:
                break
            t = i / sample_rate

            # ADSR envelope
            attack = 0.02
            decay = 0.1
            sustain_level = 0.6
            release_start = note_samples * 0.7 / sample_rate

            if t < attack:
                env = t / attack
            elif t < attack + decay:
                env = 1.0 - (1.0 - sustain_level) * (t - attack) / decay
            elif t < release_start:
                env = sustain_level
            else:
                env = sustain_level * (1.0 - (t - release_start) / (beat_duration * beats - release_start))

            # Piano-like tone: fundamental + harmonics with decay
            fundamental = 0.6 * env * (2 * freq * t % 2 - 1)  # sawtooth-ish
            harmonic2 = 0.2 * env * (2 * (2 * freq) * t % 2 - 1)
            harmonic3 = 0.1 * env * (2 * (3 * freq) * t % 2 - 1)
            value = fundamental + harmonic2 + harmonic3

            # Clamp
            sample = max(-1.0, min(1.0, value))
            int_sample = int(sample * 32767)
            struct.pack_into("<h", audio_data, (current_sample + i) * 2, int_sample)

        current_sample += note_samples

    # Fill remaining with silence (or extend last note)
    # Apply global fade-out at end
    fade_start = total_samples - int(sample_rate * fade_out_seconds)
    for i in range(fade_start, total_samples):
        if i < current_sample:
            continue  # already written by melody
        fade_ratio = 1.0 - (i - fade_start) / (total_samples - fade_start)
        # Fade existing samples
        existing = struct.unpack_from("<h", audio_data, i * 2)[0]
        faded = int(existing * fade_ratio)
        struct.pack_into("<h", audio_data, i * 2, faded)

    # Apply fade-out to all samples in the fade zone
    for i in range(max(fade_start, 0), total_samples):
        fade_ratio = 1.0 - (i - fade_start) / (total_samples - fade_start)
        existing = struct.unpack_from("<h", audio_data, i * 2)[0]
        faded = int(existing * fade_ratio)
        struct.pack_into("<h", audio_data, i * 2, faded)

    # Write WAV file
    with wave_module.open(output, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(bytes(audio_data))

    print(f"Saved WAV: {output} ({duration}s, {sample_rate}Hz mono)")
    print("NOTE: This is a simple synthesized piano melody — for professional quality, use Suno API mode.")


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate piano accompaniment for graduation memory video")
    parser.add_argument("--method", choices=["suno", "wave"], default="wave",
                        help="Generation method: 'suno' (Suno API) or 'wave' (Python fallback)")
    parser.add_argument("--style", default="warm sentimental piano solo, graduation tribute, gentle melody",
                        help="Music style description (for Suno mode)")
    parser.add_argument("--duration", type=int, default=18,
                        help="Duration in seconds")
    parser.add_argument("--output", default="piano_accompaniment.wav",
                        help="Output file path")
    args = parser.parse_args()

    if args.method == "suno":
        generate_suno(args.style, args.duration, args.output)
    else:
        generate_wave(args.duration, args.output)


if __name__ == "__main__":
    main()
