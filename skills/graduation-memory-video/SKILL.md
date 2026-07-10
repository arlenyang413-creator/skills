---
name: graduation-memory-video
description: "Cinematic graduation tribute video creator. Given one portrait photo, generates 6 graduation scene images (high school through doctoral + diploma + memorial book cover), then creates smooth first-last-frame transition videos using Kling, assembles into a 15-18s cinematic video with warm piano accompaniment. Use this when user asks for graduation memory video, graduation tribute, graduation photo video, or similar creative video from a single portrait."
version: "1.1.0"
author: theo-lovart
license: Apache-2.0

metadata:
  hermes:
    tags:
      - creative-design
      - content-creation
      - video
      - graduation
      - workflow
      - cinematic
      - ai-generation
    related_skills: []
    requires_tools:
      - image_generate
      - video_generate
      - terminal
    fallback_for_toolsets: []
    fallback_for_tools: []
    config:
      - key: image_gen.provider
        description: "Image generation provider (openai for gpt-image-2)"
        default: "openai"
      - key: video_gen.provider
        description: "Video generation provider (fal for Kling v3)"
        default: "fal"
      - key: video_gen.fal.model
        description: "FAL video model (kling-v3 for Kling first-last frame mode)"
        default: "kling-v3"

required_environment_variables:
  - name: OPENAI_API_KEY
    prompt: "OpenAI API key for gpt-image-2"
    help: "Get from https://platform.openai.com/api-keys"
    required_for: "Image generation (Step 1)"
  - name: FAL_KEY
    prompt: "FAL API key for Kling v3 video generation"
    help: "Get from https://fal.ai/dashboard/keys"
    required_for: "Video generation (Step 2)"
  - name: SUNO_API_KEY
    prompt: "Suno API key for piano music generation (optional — falls back to wave synthesis)"
    help: "Get from https://suno.com/api — if unavailable, the skill uses Python wave module for placeholder piano music"
    required_for: "Music accompaniment (Step 4)"
---

# Graduation Memory Video Creator

Create a cinematic graduation tribute video from a single portrait photo. The complete workflow: 6 graduation scene images → Kling first-last-frame transition videos → 15-18s assembled video → warm piano accompaniment.

**Core design philosophy**: The video uses **cinematic variable-duration pacing** — not uniform 3s/clip, but emotional rhythm where key moments (doctoral graduation, memorial book ending) get more screen time, and transitions are shorter, creating natural breathing space. Based on real Lovart成品 analysis.

## When to Use

Trigger this skill when the user:
- Provides a portrait photo and asks for a graduation memory/tribute video
- Wants to create a video spanning their academic journey (high school → bachelor's → master's → doctoral)
- Asks for "毕业纪念视频", "毕业回忆视频", "graduation memory video", "graduation tribute"
- Wants AI-generated graduation scenes assembled into a short video

## Quick Reference

| Step | Tool | Key Parameters |
|------|------|----------------|
| 1. Generate 6 images | `image_generate` | `aspect_ratio="portrait"`, `model="gpt-image-2"` (high quality) |
| 2. Create 6 transition videos | `video_generate` | `model="kling-v3"`, `aspect_ratio="9:16"`, `image_url` + `reference_image_urls` for first-last frame |
| 3. Assemble video | `terminal` | `ffmpeg` or moviepy crossfade montage |
| 4. Add piano music | `terminal` | Suno API (preferred) or Python wave fallback via `${HERMES_SKILL_DIR}/scripts/generate_music.py` |

## Step 1: Generate 6 Graduation Scene Images

Use `image_generate` (provider: openai, model: gpt-image-2) to create 6 9:16 vertical images. Each prompt must include extremely detailed person description for consistency across all 6 images.

**⚠️ Critical: Person Consistency**

Since `image_generate` is text-to-image only (no image-to-image mode in current Hermes plugin architecture), maintaining face consistency is the biggest challenge. Strategies:
1. **Extract person features** from the provided photo first — describe hair, skin tone, facial features, build in extreme detail
2. **Copy-paste the EXACT same person description** across all 6 prompts (consistency > brevity)
3. **After generating all 6 images**, show them to the user for consistency review before proceeding to Step 2

### Generation Order (strict)

Generate images in order 1→6, confirming each image's quality before proceeding:

1. **High School**: Student in Chinese high school uniform, bright school corridor, warm morning light
2. **Bachelor's**: Black gown with pink trim, tree-lined campus path, library background
3. **Master's**: Blue gown with deep blue trim, golden ginkgo autumn path, graduate school entrance
4. **Doctoral**: Red gown with red trim + black border, traditional Chinese ancient building with peach blossoms
5. **Diploma**: Close-up doctoral diploma on sunlit wooden desk, golden light rays
6. **Memorial Book Cover**: Closed book with "毕业纪念册" typography, warm sunset ambient light

### Color Tone Progression

| Image | Color Tone | Emotional Purpose |
|-------|-----------|-------------------|
| 1 (High School) | Bright warm golden | Youthful innocence |
| 2 (Bachelor's) | Warm spring amber | Growth & hope |
| 3 (Master's) | Warm autumn amber (slightly deeper) | Maturation |
| 4 (Doctoral) | Rich warm + slightly more saturated | Achievement peak |
| 5 (Diploma) | Soft warm muted golden | Quiet reflection |
| 6 (Memorial Book) | Warmest soft sunset amber | Fond closure |

### Chinese Academic Gown Standards

| Degree | Gown Color | Trim Color | Trim Border |
|--------|-----------|-----------|-------------|
| Bachelor's (学士) | Black | Pink | — |
| Master's (硕士) | Blue | Deep Blue | — |
| Doctoral (博士) | Red | Red | Black border on trim |

### Tool Call Format

```
image_generate(
    prompt="<full prompt from references/prompt_templates.md>",
    aspect_ratio="portrait",
    model="gpt-image-2"
)
```

For high-quality output, use the "high" quality tier of gpt-image-2 (if provider supports quality tiers).

Complete prompt templates in `references/prompt_templates.md`.

## Step 2: Create Transition Videos with Kling First-Last Frame Mode

Use `video_generate` (provider: fal, model: kling-v3) with Kling's **first-last frame mode** to create smooth transition videos.

### ⚠️ Strict Generation Order

1. **Complete Step 1 first**: Generate all 6 images in order (1→6), confirming each before continuing
2. **Then generate videos**: Only start Step 2 after all 6 images are done
3. **Generate videos in order**: Videos 1→5 sequentially, Video 6 separately

### First-Last Frame Mode Details

Kling's first-last frame mode takes a **start frame** and an **end frame** as input, and AI-generates the smooth transition animation between them. In Hermes, this is achieved through `video_generate` parameters:

- **`image_url`**: The primary reference image → use as the **start frame** (first frame of the transition)
- **`reference_image_urls`**: Additional reference images → use for the **end frame** (last frame of the transition)
- **`prompt`**: Text description of the transition, must emphasize smooth natural aesthetics

**⚠️ Provider-specific behavior**: The `reference_image_urls` parameter's exact behavior with Kling/FAL depends on the provider implementation. If `reference_image_urls` does not correctly pass the end frame to Kling's first-last frame mode, you may need to:
1. Use `image_url` as the start frame and describe the end frame content in the prompt
2. Or check if the FAL Kling API supports `end_frame_url` as a separate parameter through kwargs

### Generation Rules

- **Videos 1-5**: First-last frame mode. `image_url` = start frame image, `reference_image_urls` = [end frame image]
- **Video 6**: First-frame-only mode. `image_url` = Image 6, no reference images needed

| Video # | `image_url` (Start Frame) | `reference_image_urls` (End Frame) | Transition Description | Suggested Duration | Emotional Role |
|---------|---------------------------|------------------------------------|----------------------|--------------------|----------------|
| 1 | Image 1 (High School) | [Image 2 (Bachelor's)] | School corridor → campus path | 2-2.5s | Youthful beginning |
| 2 | Image 2 (Bachelor's) | [Image 3 (Master's)] | Library path → ginkgo path | 2-2.5s | Growth acceleration |
| 3 | Image 3 (Master's) | [Image 4 (Doctoral)] | Graduate school → ancient building | 3-3.5s | Academic peak |
| 4 | Image 4 (Doctoral) | [Image 5 (Diploma)] | Peach blossoms → sunlit desk | 2.5-3s | Celebration → reflection |
| 5 | Image 5 (Diploma) | [Image 6 (Memorial Book)] | Diploma → memorial book | 2.5-3s | Reflection → closure |
| 6 | Image 6 (Memorial Book) | **None** (no end frame) | Memorial book static hold | 3-4s | Warm closure |

### Video 6 Special Handling

Video 6 only has a start frame (Image 6) — no end frame or reference images. Kling generates a slow static hold with gradual fade-out (3-4 seconds), giving viewers time to absorb the emotional conclusion.

### Transition Prompt Requirements

Every prompt must include these 4 elements:
1. **Start and end frame content** (e.g., "starting from school corridor, naturally transitioning to campus path")
2. **Transition style**: **smooth, natural, aesthetically beautiful — NO stiff mechanical morphing, NO abrupt cuts**
3. **Emotional atmosphere** matching the transition's role
4. **Color tone continuity** — maintain warm progression, no sudden color shifts

### Tool Call Format

**Videos 1-5 (first-last frame mode):**
```
video_generate(
    prompt="<transition prompt from references/prompt_templates.md>",
    image_url="<start_frame_image_url_or_path>",
    reference_image_urls=["<end_frame_image_url_or_path>"],
    model="kling-v3",
    aspect_ratio="9:16",
    duration=<suggested_duration>,
    negative_prompt="stiff, mechanical, morphing, abrupt, harsh, jerky"
)
```

**Video 6 (first-frame-only mode):**
```
video_generate(
    prompt="<ending hold prompt>",
    image_url="<image_6_url_or_path>",
    model="kling-v3",
    aspect_ratio="9:16",
    duration=4
)
```

### Cinematic Pacing Strategy

**Do NOT use equal-duration clips.** Variable pacing based on emotional rhythm:

| Segment | Content | Duration | Emotional Role |
|---------|---------|----------|----------------|
| Opening | High school → Bachelor's | 4-5s | Let viewers enter the emotion |
| Middle 1 | Bachelor's → Master's | 2.5-3s | Growth acceleration, compact |
| Middle 2 | Master's → Doctoral | 4-5s | Academic peak, more time here |
| Closing | Doctoral → Diploma → Memorial book | 5-6s | Reflective ending, unhurried |

Total: ~15-18 seconds.

### If video_generate or Kling is Not Available

Use moviepy crossfade montage as fallback via `terminal`:
```bash
python3 ${HERMES_SKILL_DIR}/scripts/assemble_video.py --images <img1>,<img2>,...,<img6> --durations 2.5,2.5,3.5,3,3,4 --crossfade 0.6 --output graduation_memory.mp4
```

## Step 3: Assemble Final Video

After all 6 transition videos are generated, assemble them into the final 15-18s video.

### Using ffmpeg (preferred)
```bash
ffmpeg -i video1.mp4 -i video2.mp4 ... -i video6.mp4 \
  -filter_complex "[0:v][1:v]xfade=transition=fade:duration=0.6:offset=2.0[v01]; ..." \
  -c:v libx264 -preset medium -crf 23 graduation_memory.mp4
```

### Using moviepy (fallback)
If ffmpeg is not available, use the bundled script:
```bash
python3 ${HERMES_SKILL_DIR}/scripts/assemble_video.py \
  --videos <v1>,<v2>,...,<v6> \
  --crossfade 0.6 \
  --fade_out 1.5 \
  --output graduation_memory.mp4
```

### Parameters
- **Crossfade overlap**: 0.6-0.8 seconds between clips
- **Fade-out at end**: 1.5 seconds (last 1.5s of video fade to black/warm)
- **Resolution**: 720×1280 (9:16 mobile vertical)
- **FPS**: 30

## Step 4: Add Piano Accompaniment

### Option A: Suno API (preferred)

If `SUNO_API_KEY` is available, generate warm piano solo music via Suno:
```bash
python3 ${HERMES_SKILL_DIR}/scripts/generate_music.py --method suno \
  --style "warm sentimental piano solo, graduation tribute, gentle melody" \
  --duration 18 \
  --output piano_accompaniment.mp3
```

Then combine video + audio:
```bash
ffmpeg -i graduation_memory.mp4 -i piano_accompaniment.mp3 \
  -c:v copy -c:a aac -shortest graduation_memory_final.mp4
```

### Option B: Python Wave Fallback

If no Suno API key or ffmpeg audio encoding, generate simple piano melody using Python wave module:
```bash
python3 ${HERMES_SKILL_DIR}/scripts/generate_music.py --method wave \
  --duration 18 \
  --output piano_accompaniment.wav
```

Then combine with moviepy:
```bash
python3 ${HERMES_SKILL_DIR}/scripts/combine_video_audio.py \
  --video graduation_memory.mp4 \
  --audio piano_accompaniment.wav \
  --output graduation_memory_final.mp4
```

### Music Guidelines
- **Style**: Warm sentimental piano solo
- **Volume**: 30-40% of total audio mix (music should support, not overpower)
- **Ending**: Fade out synchronized with video fade-out (last 1.5-2s)
- **Duration**: Match video length exactly (15-18s)

## Important Notes

1. **Person consistency is the #1 challenge** — text-to-image tools produce different faces each time. Always copy-paste identical person descriptions across all 6 prompts.
2. **Generation order matters** — complete all 6 images before starting any video generation.
3. **Kling first-last frame mode** — the `reference_image_urls` parameter maps to Kling's end frame. If this doesn't work correctly with the FAL Kling provider, describe the end frame content in the prompt text and use `image_url` alone.
4. **Variable pacing** — never use uniform durations. Follow the cinematic pacing strategy table.
5. **Transition quality** — every prompt must explicitly demand smooth natural transitions: "NO stiff mechanical morphing, NO abrupt cuts".
6. **Fallbacks** — if any tool (image_generate, video_generate) is unavailable, inform the user and suggest alternatives. The skill is designed with multiple fallback paths.

## Verification

After completing all steps, verify:
1. **6 images generated** — check each exists and person appearance is reasonably consistent
2. **6 videos generated** — check transitions are smooth and not jarring
3. **Final video assembled** — duration is 15-18s, resolution is 720×1280, transitions flow naturally
4. **Music added** — piano solo is audible at 30-40% volume, fades out at end
5. **Show result** — present the final video to the user for review, using `[[as_document]]` for high-quality delivery

## Lovart成品 Reference

Real production video analysis (Theo's Lovart成品):
- Duration: 18.1s, Resolution: 720×1280, FPS: 30
- 4 main scene segments (~5s → ~6s → ~6.6s), NOT uniform 6×3s
- Scene transitions at t≈2.0s, t≈5.0-5.5s, t≈11.0-11.5s
- Audio: piano accompaniment at 44100Hz
- Key insight: variable-duration cinematic pacing produces superior emotional impact vs. uniform timing
