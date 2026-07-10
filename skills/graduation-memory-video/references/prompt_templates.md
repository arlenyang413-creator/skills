# Prompt Templates for Graduation Memory Video

## Image Generation Prompt Templates

Use `image_generate` tool with `aspect_ratio="portrait"` and `model="gpt-image-2"`.

**⚠️ Person Description Template**

Replace `[PERSON_DESCRIPTION]` in each prompt with the EXACT SAME detailed person description extracted from the user's photo. Copy-paste identical text across all 6 prompts — consistency is more important than brevity.

Example person description format:
```
a young Chinese person, [age], [gender], with [hair style and color], [skin tone], [facial features: eye shape, nose, jawline], [build: height estimate, body type], wearing [any visible clothing/accessories from the photo]
```

**⚠️ Color Tone Reminder**: Each prompt includes a color tone directive. Follow the progression: Bright warm → Warm amber → Deep amber → Rich saturated → Soft muted → Warmest sunset.

---

### Image 1: High School Graduation (Bright warm golden tones)

```
cinematic portrait, film grain, shallow depth of field, golden hour lighting — [PERSON_DESCRIPTION], wearing a Chinese high school uniform (white shirt, dark blue trousers, red school badge on chest), standing in a bright school corridor with large windows letting in warm morning light, sunlight streaming through creating soft shadows, gentle smile, youthful expression, school bulletin board and trophy shelf visible in soft-focus background, warm nostalgic golden color grading, bright warm golden tones, 9:16 vertical composition, cinematic film still quality, NO text overlay, NO watermark
```

### Image 2: Bachelor's Graduation (Warm spring amber tones)

```
cinematic portrait, film grain, shallow depth of field, golden hour lighting — [PERSON_DESCRIPTION], wearing a black bachelor's graduation gown (学士服) with pink collar trim following Chinese university convention, holding a rolled-up diploma, standing on a tree-lined campus path with the university library in soft-focus background, spring green leaves and dappled sunlight, gentle confident smile, warm spring amber color grading, slightly deeper warm tones than the previous scene, 9:16 vertical composition, cinematic film still quality, NO text overlay, NO watermark
```

### Image 3: Master's Graduation (Warm autumn amber tones, slightly deeper)

```
cinematic portrait, film grain, shallow depth of field, golden hour lighting — [PERSON_DESCRIPTION], wearing a blue master's graduation gown (硕士服) with deep blue collar trim following Chinese university convention, standing on a golden ginkgo-lined autumn path with the graduate school entrance gate visible in background, fallen golden leaves on the path, warm autumn amber color grading with slightly increased saturation and depth, expression showing mature confidence and scholarly poise, 9:16 vertical composition, cinematic film still quality, NO text overlay, NO watermark
```

### Image 4: Doctoral Graduation (Rich warm tones, slightly more saturated)

```
cinematic portrait, film grain, shallow depth of field, golden hour lighting — [PERSON_DESCRIPTION], wearing a red doctoral graduation gown (博士服) with red collar trim and black border following Chinese university convention, standing proudly in front of a traditional Chinese ancient building with elegant architectural details and peach blossoms blooming around the entrance, a visible plaque reading "学术报告厅" on the building, warm rich tones with slightly increased saturation marking the academic pinnacle, dignified and accomplished expression, 9:16 vertical composition, cinematic film still quality, NO text overlay, NO watermark
```

### Image 5: Doctoral Diploma Certificate (Soft muted warm golden tones)

```
cinematic close-up, film grain, shallow depth of field, golden hour lighting — A doctoral diploma certificate resting on a sunlit wooden desk, warm golden light rays crossing the desk surface, the certificate features the graduate's portrait photo [PERSON_DESCRIPTION face only] in a small inset, ornate border design, text reading "博士学位证书" in elegant Chinese typography, university seal impression visible, soft muted warm golden color grading marking a shift from celebration to quiet reflection, 9:16 vertical composition, cinematic film still quality, NO real university names, NO text overlay obscuring the diploma, NO watermark
```

### Image 6: Graduation Memorial Book Cover (Warmest soft sunset amber tones)

```
cinematic close-up, film grain, shallow depth of field, warm sunset ambient lighting — A closed elegant book resting on a warm surface, the book cover reads "毕业纪念册" in elegant Chinese calligraphy typography with subtle decorative floral border, warm sunset-like ambient lighting casting soft shadows, the warmest and softest color palette of the entire sequence — sunset amber tones suggesting fond memory and closure, sentimental nostalgic atmosphere, 9:16 vertical composition, cinematic film still quality, NO text overlay other than the book title, NO watermark
```

---

## Chinese Academic Gown Color Standards

| Degree | Chinese Name | Gown Color | Collar Trim Color | Additional Detail | Visual Meaning |
|--------|-------------|-----------|-------------------|-------------------|---------------|
| Bachelor's | 学士 | Black | Pink | — | Fresh start, youthful hope |
| Master's | 硕士 | Blue | Deep Blue | — | Scholarly depth, academic growth |
| Doctoral | 博士 | Red | Red | Black border on trim | Academic pinnacle, supreme achievement |

---

## Video Transition Prompt Templates

Each transition video uses `video_generate` with Kling first-last frame mode via FAL provider.

**⚠️ How to Use First-Last Frame Mode**

For Videos 1-5:
- `image_url` = start frame image (the image being transitioned FROM)
- `reference_image_urls` = [end frame image] (the image being transitioned TO)
- `prompt` = transition description

For Video 6:
- `image_url` = Image 6 (memorial book cover)
- `reference_image_urls` = [] (no end frame)
- `prompt` = ending hold description

**Critical Prompt Requirement**: Every prompt must emphasize **the transition should be smooth, natural, and aesthetically beautiful — NO stiff or mechanical morphing, NO abrupt cuts**.

**Tool call example (Video 1):**
```
video_generate(
    prompt="Kling first-last frame transition...",
    image_url="<image_1_url>",
    reference_image_urls=["<image_2_url>"],
    model="kling-v3",
    aspect_ratio="9:16",
    duration=2.5,
    negative_prompt="stiff, mechanical, morphing, abrupt, harsh, jerky"
)
```

---

### Video 1: High School → Bachelor's (image_url=Image1, reference_image_urls=[Image2], 2-2.5s)

```
Kling first-last frame transition video. Start frame: a young student in Chinese high school uniform standing in a bright school corridor with warm morning light. End frame: the same person wearing a black bachelor's graduation gown with pink trim on a tree-lined campus path with library in soft-focus background. The transition should be smooth, natural, and aesthetically beautiful — the scene gently evolves from the school corridor to the campus path with the person's attire naturally morphing from school uniform to graduation gown, warm nostalgic golden color grading maintained throughout, gentle camera drift right, NO stiff or mechanical morphing, NO abrupt cuts, 2.5 seconds duration
```

### Video 2: Bachelor's → Master's (image_url=Image2, reference_image_urls=[Image3], 2-2.5s)

```
Kling first-last frame transition video. Start frame: a graduate in black bachelor's gown on a campus tree-lined path with library background. End frame: the same person wearing a blue master's graduation gown on a golden ginkgo-lined autumn path with graduate school entrance in background. The transition should be smooth, natural, and aesthetically beautiful — the scene gently evolves from spring campus path to autumn ginkgo path with the gown color naturally shifting from black to blue, warm autumn amber tones gradually intensifying, gentle camera movement, NO stiff or mechanical morphing, NO abrupt cuts, 2.5 seconds duration
```

### Video 3: Master's → Doctoral (image_url=Image3, reference_image_urls=[Image4], 3-3.5s)

```
Kling first-last frame transition video. Start frame: a graduate in blue master's gown on a ginkgo-lined autumn path with graduate school gate. End frame: the same person wearing a red doctoral gown in front of a traditional Chinese ancient building with peach blossoms and visible "学术报告厅" plaque. The transition should be smooth, natural, and aesthetically beautiful — the scene slowly and gracefully evolves from autumn ginkgo path to spring ancient building with peach blossoms, the gown naturally shifts from blue to red, warm tones becoming richer and more saturated, gentle camera pull-in with slight zoom, NO stiff or mechanical morphing, NO abrupt cuts, this key moment deserves more screen time with a dignified and deliberate pace, 3.5 seconds duration
```

### Video 4: Doctoral → Diploma (image_url=Image4, reference_image_urls=[Image5], 2.5-3s)

```
Kling first-last frame transition video. Start frame: a doctoral graduate in red gown standing proudly before an ancient building with peach blossoms. End frame: a close-up of a doctoral diploma certificate resting on a sunlit wooden desk with the graduate's portrait visible and university name obscured. The transition should be smooth, natural, and aesthetically beautiful — the camera gently pulls back and shifts perspective from the person in graduation scene to the diploma on the desk, warm golden light rays gradually appear across the desk surface, tones becoming softer and more muted, NO stiff or mechanical morphing, NO abrupt cuts, this transition shifts emotional tone from celebration to quiet reflection, 3 seconds duration
```

### Video 5: Diploma → Memorial Book (image_url=Image5, reference_image_urls=[Image6], 2.5-3s)

```
Kling first-last frame transition video. Start frame: a doctoral diploma on a sunlit desk with golden light rays. End frame: a closed book with cover reading "毕业纪念册" in elegant Chinese typography resting on a warm surface with sunset-like ambient lighting. The transition should be smooth, natural, and aesthetically beautiful — the scene gently evolves from the desk with diploma to the warm surface with the memorial book, the warmest and softest color palette of the entire sequence gradually emerging, soft camera movement, nostalgic and sentimental atmosphere intensifying, NO stiff or mechanical morphing, NO abrupt cuts, transition from reflection to closure, 3 seconds duration
```

### Video 6: Memorial Book Ending Hold (image_url=Image6, NO reference images, 3-4s)

```
Kling first-frame-only video. Start frame: the closed "毕业纪念册" book cover in warm sunset-like ambient light. NO end frame provided — this is a final hold sequence. Slow gentle camera hold with very subtle breathing movement, the warmest muted golden tones suggesting fond memory and closure, sentimental atmosphere, slow fade to slightly darker/warmer in the final second, emotional ending that gives the viewer time to absorb, 4 seconds duration. The transition style should be natural and gentle — no abrupt changes, just a peaceful, lingering final moment
```

---

## Color Tone Progression Reference

| Image # | Scene | Primary Tone | Emotional Purpose | Key Words |
|---------|-------|-------------|-------------------|-----------|
| 1 | High School | Bright warm golden | Youthful innocence | morning light, bright, nostalgic |
| 2 | Bachelor's | Warm spring amber | Growth & hope | dappled sunlight, spring green |
| 3 | Master's | Warm autumn amber (deeper) | Maturation | ginkgo gold, deeper saturation |
| 4 | Doctoral | Rich warm (more saturated) | Achievement peak | rich, saturated, pinnacle |
| 5 | Diploma | Soft muted warm golden | Quiet reflection | sunlit, muted, soft rays |
| 6 | Memorial Book | Warmest soft sunset amber | Fond closure | sunset, warmest, sentimental |
