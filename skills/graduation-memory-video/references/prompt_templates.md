# 毕业纪念视频 — 图片与转场 Prompt 模板

本文件包含两个预设脚本的完整 prompt 模板：
- **脚本A**：毕业纪念视频（6分镜，默认选项）
- **脚本B**：校草给你递毕业证（4分镜，浪漫互动）

---

# ═══════════════════════════════════════
# 脚本A：毕业纪念视频（6分镜）
# ═══════════════════════════════════════

以下为6张毕业场景图片的完整 prompt 模板。使用时将 `[人物描述]` 替换为从用户提供的参考照片中提取的人物特征描述（外貌、发型、气质等），确保6张图片的人物一致性。

**⚠️ 人物一致性关键提醒**：每个 prompt 中的人物描述必须极其详细且统一。在6张 prompt 中使用**完全相同**的人物特征描述（复制粘贴，不要缩略或改写），这是保持一致性的唯一手段。

**视觉风格统一要求**：6张图片应呈现统一的视觉风格——温暖电影感色调（golden hour / warm cinematic grading）、纪实感但略微唯美化、9:16竖版构图。色调从明亮温暖逐步过渡到柔和昏黄，呼应情感递进。

---

## 图片1：高中毕业照

```
A realistic cinematic portrait photo of [人物描述], wearing a Chinese high school uniform (蓝白配色运动校服), standing in a bright school corridor with large windows letting in warm natural morning light, smiling warmly with youthful energy and optimism, soft golden hour color tones with warm highlights, cinematic film grain texture, shallow depth of field with blurred background, documentary photography style with slight cinematic elevation, 9:16 vertical aspect ratio, gentle and nostalgic atmosphere, the light creates a warm halo effect around the subject
```

**要点**: 校服应为典型的中国高中蓝白配色校服，走廊光线明亮温暖（golden hour），人物微笑阳光。浅景深让人物突出，电影胶片质感。

---

## 图片2：本科毕业照

```
A realistic cinematic portrait photo of [人物描述], wearing a Chinese bachelor's degree graduation gown (黑色学士服 with 粉色领饰/粉垂 indicating arts/humanities), standing confidently on a tree-lined campus path with dappled warm sunlight filtering through green leaves, background shows the university library building in soft focus, warm spring golden hour lighting creating gentle shadows, cinematic film grain texture, shallow depth of field, documentary photography style with cinematic elevation, 9:16 vertical aspect ratio, scholarly and proud atmosphere, warm color palette with rich golden tones
```

**要点**: 学位服为中国大学标准学士学位服（黑色袍+粉色领饰），背景需有图书馆建筑（浅景深模糊），林荫道光影效果，金色暖调。

---

## 图片3：硕士毕业照

```
A realistic cinematic portrait photo of [人物描述], wearing a Chinese master's degree graduation gown (蓝色硕士服 with 藏蓝色/深蓝领饰), standing on a beautiful ginkgo tree-lined path with golden autumn leaves creating a warm amber canopy, background shows the graduate school entrance gate with signage in soft focus, warm autumn golden tones with amber and burnt sienna highlights, cinematic film grain texture, shallow depth of field, the golden ginkgo leaves frame the subject naturally, documentary photography style with cinematic elevation, 9:16 vertical aspect ratio, mature and accomplished atmosphere, warm rich color palette
```

**要点**: 硕士学位服为蓝色袍+深蓝领饰（中国标准），银杏小路秋季金叶（暖琥珀色调），背景研究生院门口（浅景深），整体色调比前两张更暖更深。

---

## 图片4：博士毕业照

```
A realistic cinematic portrait photo of [人物描述], wearing a Chinese doctoral degree graduation gown (红色博士服 with 红色领饰 and black trim), standing proudly in front of a traditional Chinese-style ancient building with a visible plaque that reads "学术报告厅" (Academic Lecture Hall) in clear Chinese characters, surrounded by blooming peach blossom trees (桃花) creating a soft pink-red frame, warm spring sunlight with gentle golden highlights, cinematic film grain texture, shallow depth of field with the ancient building softly blurred behind, documentary photography style with cinematic elevation, 9:16 vertical aspect ratio, dignified and scholarly atmosphere with a sense of culmination, warm and slightly more saturated color palette than previous scenes
```

**要点**: 博士学位服为红色袍+红色领饰（中国标准），古建筑牌匾必须显示"学术报告厅"四个字（清晰可见），桃花树环绕（粉红色框架），庄重学术氛围。色调饱和度略高于前几张，呼应"巅峰"感。

---

## 图片5：博士毕业证书

```
A realistic cinematic close-up photo of a Chinese doctoral diploma/graduation certificate placed on a polished wooden desk, warm golden sunlight slanting across the desk surface creating dramatic light rays and warm shadows, the certificate features [人物描述]'s portrait photo in the upper corner, the certificate has ornate borders with traditional Chinese academic design elements in red and gold, the university name area is intentionally blurred or obscured (不显示校名), warm nostalgic lighting with slightly softer and more muted tones than previous scenes, cinematic film grain texture, shallow depth of field focused on the certificate, documentary photography style with cinematic elevation, 9:16 vertical aspect ratio, the overall mood transitions from bright celebration to quiet reflection
```

**要点**: 毕业证书放在书桌上，阳光斜射效果（金色光线条），证书上有人物头像，校名必须隐藏/模糊处理。色调开始变柔和昏黄，情感从"庆祝"转向"感慨回顾"。

---

## 图片6：毕业纪念册封面

```
A realistic cinematic photo of a closed book resting on a warm surface, the book cover (书皮) clearly displays the title "毕业纪念册" (Graduation Memorial Book) in elegant Chinese typography with a warm nostalgic design, the cover features soft pastel colors with subtle decorative elements like small graduation cap motifs and delicate flower illustrations, warm ambient lighting with soft shadows and the gentle glow of sunset-like illumination, cinematic film grain texture, the book is positioned at a slight angle creating visual interest, shallow depth of field with surface texture visible, documentary photography style with cinematic elevation, 9:16 vertical aspect ratio, gentle and sentimental atmosphere, the overall color palette is the warmest and softest of all six scenes — muted golden tones suggesting closure and fond memory
```

**要点**: 书本合上状态，书皮上"毕业纪念册"文字必须清晰可见，设计温馨怀旧。色调是6张中最温暖最柔和的——昏黄夕阳色调，暗示"回忆收束"。

---

## 脚本A — 转场视频 Prompt 模板

每个转场视频使用 Kling 的**首尾帧模式**（First-Last Frame mode）生成。

**Prompt 核心要求**：每个 prompt 必须强调 **transition should be smooth, natural, and aesthetically beautiful — no stiff or mechanical morphing, no abrupt cuts**。

### 视频1: 高中→本科（首帧=图片1，尾帧=图片2，2-2.5秒）

```
Kling first-last frame transition video. Start frame: a young student in Chinese high school uniform standing in a bright school corridor with warm morning light. End frame: the same person wearing a black bachelor's graduation gown with pink trim on a tree-lined campus path with library in soft-focus background. The transition should be smooth, natural, and aesthetically beautiful — the scene gently evolves from the school corridor to the campus path with the person's attire naturally morphing from school uniform to graduation gown, warm nostalgic golden color grading maintained throughout, gentle camera drift right, NO stiff or mechanical morphing, NO abrupt cuts, 2.5 seconds duration
```

### 视频2: 本科→硕士（首帧=图片2，尾帧=图片3，2-2.5秒）

```
Kling first-last frame transition video. Start frame: a graduate in black bachelor's gown on a campus tree-lined path with library background. End frame: the same person wearing a blue master's graduation gown on a golden ginkgo-lined autumn path with graduate school entrance in background. The transition should be smooth, natural, and aesthetically beautiful — the scene gently evolves from spring campus path to autumn ginkgo path with the gown color naturally shifting from black to blue, warm autumn amber tones gradually intensifying, gentle camera movement, NO stiff or mechanical morphing, NO abrupt cuts, 2.5 seconds duration
```

### 视频3: 硕士→博士（首帧=图片3，尾帧=图片4，3-3.5秒）

```
Kling first-last frame transition video. Start frame: a graduate in blue master's gown on a ginkgo-lined autumn path with graduate school gate. End frame: the same person wearing a red doctoral gown in front of a traditional Chinese ancient building with peach blossoms and visible "学术报告厅" plaque. The transition should be smooth, natural, and aesthetically beautiful — the scene slowly and gracefully evolves from autumn ginkgo path to spring ancient building with peach blossoms, the gown naturally shifts from blue to red, warm tones becoming richer and more saturated, gentle camera pull-in with slight zoom, NO stiff or mechanical morphing, NO abrupt cuts, this key moment deserves more screen time with a dignified and deliberate pace, 3.5 seconds duration
```

### 视频4: 博士→毕业证书（首帧=图片4，尾帧=图片5，2.5-3秒）

```
Kling first-last frame transition video. Start frame: a doctoral graduate in red gown standing proudly before an ancient building with peach blossoms. End frame: a close-up of a doctoral diploma certificate resting on a sunlit wooden desk with the graduate's portrait visible and university name obscured. The transition should be smooth, natural, and aesthetically beautiful — the camera gently pulls back and shifts perspective from the person in graduation scene to the diploma on the desk, warm golden light rays gradually appear across the desk surface, tones becoming softer and more muted, NO stiff or mechanical morphing, NO abrupt cuts, this transition shifts emotional tone from celebration to quiet reflection, 3 seconds duration
```

### 视频5: 毕业证书→纪念册（首帧=图片5，尾帧=图片6，2.5-3秒）

```
Kling first-last frame transition video. Start frame: a doctoral diploma on a sunlit desk with golden light rays. End frame: a closed book with cover reading "毕业纪念册" in elegant Chinese typography resting on a warm surface with sunset-like ambient lighting. The transition should be smooth, natural, and aesthetically beautiful — the scene gently evolves from the desk with diploma to the warm surface with the memorial book, the warmest and softest color palette of the entire sequence gradually emerging, soft camera movement, nostalgic and sentimental atmosphere intensifying, NO stiff or mechanical morphing, NO abrupt cuts, transition from reflection to closure, 3 seconds duration
```

### 视频6: 纪念册定格结尾（首帧=图片6，无尾帧，3-4秒）

```
Kling first-frame-only video. Start frame: the closed "毕业纪念册" book cover in warm sunset-like ambient light. NO end frame provided — this is a final hold sequence. Slow gentle camera hold with very subtle breathing movement, the warmest muted golden tones suggesting fond memory and closure, sentimental atmosphere, slow fade to slightly darker/warmer in the final second, emotional ending that gives the viewer time to absorb, 4 seconds duration. The transition style should be natural and gentle — no abrupt changes, just a peaceful, lingering final moment
```

---

## 脚本A — 色调递进对照表

| 场景 | 色调特征 | 情感映射 | 关键词 |
|------|---------|---------|--------|
| 高中 | 明亮温暖，偏白金 | 青春开始，朝气 | bright warm, golden highlights |
| 本科 | 温暖金调，丰富 | 成长扎实，自信 | rich golden, warm spring |
| 硕士 | 琥珀暖色，偏深 | 深入沉稳，厚重 | amber, burnt sienna |
| 博士 | 略增饱和，庄重红金 | 巅峰荣耀，高光 | richer saturation, red-gold |
| 证书 | 柔和昏黄，收束 | 回顾感慨，安静 | muted golden, softer |
| 纪念册 | 最温暖最柔和 | 收束回忆，尾声 | warmest, softest, sunset-like |

---

## 脚本A — 中国学位服颜色对照

| 学位级别 | 袍颜色 | 领饰颜色 | 视觉寓意 |
|---------|--------|---------|---------|
| 学士    | 黑色    | 粉色领饰（文科）| 基础扎实，温暖起步 |
| 硕士    | 蓝色    | 藏蓝领饰 | 深入钻研，沉稳厚重 |
| 博士    | 红色    | 红色领饰+黑色边饰 | 学术巅峰，庄重荣耀 |

---

# ═══════════════════════════════════════
# 脚本B：校草给你递毕业证（4分镜）
# ═══════════════════════════════════════

以下为"校草给你递毕业证"4帧场景图片的完整 prompt 模板。

**双人物模板**：
- `[校草描述]`：穿学士服的年轻英俊亚裔男子——在帧1-4中完全相同复制粘贴
- `[用户描述]`：用户本人——从用户提供的照片提取面容特征，在帧3-4中完全相同复制粘贴

**⚠️ 双人物一致性是此脚本的最大挑战**：帧3和帧4同时出现两个不同人物。如果环境支持图生图（GPT image2），优先使用。在纯文本生图模式下，两个人物描述都需要极其详细。

---

## 图片1：桃花校道·背影

```
A realistic cinematic photo of [校草描述], wearing a Chinese bachelor's degree graduation gown (黑色学士服 with 粉色领饰), standing on a beautiful campus path lined with blooming peach blossom trees (桃花盛开), the person is facing AWAY from the camera — back view only, the graduation gown flows gently in a soft breeze, warm pink-golden spring sunlight filtering through peach blossom petals creating a dreamy and romantic atmosphere, cinematic film grain texture, shallow depth of field with soft-focus peach blossoms framing the silhouette, a sense of mystery and anticipation — who is this person?, documentary photography style with cinematic elevation, 9:16 vertical aspect ratio, warm golden-pink color grading with soft peach blossom highlights, the scene evokes a feeling of approaching someone special on a beautiful spring day
```

**要点**：背影构图是此帧的核心——制造悬念感。桃花盛开的校道（粉金暖调），学士服随微风轻摆。色调偏粉金（柔美浪漫），与脚本A的明亮白金不同。必须强调 "facing AWAY from the camera — back view only"。

---

## 图片2：转脸·惊喜面庞

```
A realistic cinematic portrait photo of [校草描述], wearing a Chinese bachelor's degree graduation gown (黑色学士服 with 粉色领饰), now facing the camera directly with a surprised and delighted expression — eyes wide open with a sparkle of joyful recognition, a slightly open mouth showing a gasp of pleasant surprise, youthful handsome face with a bashful and fresh quality (青涩感), standing on the same peach blossom-lined campus path, warm bright golden sunlight illuminating his face beautifully, cinematic film grain texture, shallow depth of field with peach blossoms softly blurred behind, documentary photography style with cinematic elevation, 9:16 vertical aspect ratio, warm golden lighting creating a flattering glow on the face, the expression captures the exact moment of unexpectedly seeing someone dear — surprise mixed with genuine joy and a touch of boyish shyness, bright warm color grading slightly more vivid than the previous back-view scene
```

**要点**：此帧的关键是**表情**——又惊又喜（surprised AND delighted）+ 青涩感（bashful/fresh）。不是成熟从容的微笑，而是像意外遇到心上人时的那种惊喜+害羞。面部光线明亮温暖（给他好看的光），色调比帧1更明亮鲜艳——"他看到你了"的光感。

---

## 图片3：递合照·阳光笑容

```
A realistic cinematic photo of [校草描述], wearing a Chinese bachelor's degree graduation gown (黑色学士服 with 粉色领饰), holding and presenting (递过) a printed photograph toward the camera/viewer (POV perspective — as if handing the photo to YOU), the photo in his hand shows TWO people wearing bachelor's graduation gowns standing together at a university campus entrance gate with architectural details visible — one person is [校草描述] with a bright sunny smile (阳光俊朗的笑容), the other person is [用户描述] also in bachelor's gown with a warm happy smile, both people in the photo look joyful and radiant, the young man holding the photo has a bright sunshine smile on his own face (青春阳光俊朗), warm golden ambient lighting, cinematic film grain texture, the held photo is clearly visible and recognizable as a portrait of two graduates, shallow depth of field with the man's hand and the photo in focus while background is softly blurred, documentary photography style with cinematic elevation, 9:16 vertical aspect ratio, warm golden color palette, sweet and touching atmosphere of someone sharing a precious memory with you
```

**要点**：此帧最复杂——同时出现两个层次：①递合照的男子（前景，阳光笑容）②合照里的两个人（照片内容，一个人是校草另一个人是用户）。prompt 必须同时描述两个人物。合照背景是学院门口（与帧1-2的桃花校道不同）。递照片的手势是"向镜头递"（POV视角）。色调温暖金调+照片亮色。

---

## 图片4：聚焦合照·双人笑容

```
A realistic cinematic close-up photo focusing entirely on a printed photograph resting on a warm surface (or held in gentle hands at the bottom of frame), the photograph shows [校草描述] and [用户描述] standing side by side at a university campus entrance gate with beautiful architectural details, both wearing Chinese bachelor's degree graduation gowns (黑色学士服 with 粉色领饰), both with bright sunny smiles — the kind of genuine joyful smile that comes from a truly happy shared moment, warm golden sunlight falling on the photograph, cinematic film grain texture, shallow depth of field with the photograph in sharp focus while everything else is softly blurred, documentary photography style with cinematic elevation, 9:16 vertical aspect ratio, the warmest and most intimate color palette of this sequence — soft warm golden tones suggesting the preciousness of this shared memory, sentimental and tender atmosphere, the photo captures two people at the happiest moment of their academic journey together
```

**要点**：此帧的构图核心是**聚焦到合照本身**——照片是画面主体，其他一切虚化。两个人的笑容必须阳光灿烂（sunny smile）。色调是最温暖最柔和的——"我们毕业了"的温馨定格。背景完全虚化，只保留照片的清晰细节。

---

## 脚本B — 转场视频 Prompt 模板

### 视频1: 背影→转脸（首帧=图片1，尾帧=图片2，3-3.5秒）

```
Kling first-last frame transition video. Start frame: a young handsome Asian man in black bachelor's graduation gown standing on a peach blossom-lined campus path, facing AWAY from the camera — back view, mysterious silhouette. End frame: the same man now turning to face the camera directly, revealing a surprised and delighted youthful handsome face with bashful joyful expression, warm bright golden sunlight illuminating his face beautifully on the same peach blossom path. The transition should be smooth, natural, and aesthetically beautiful — the person slowly and gracefully turns around from back view to face the camera, the expression gradually shifts from hidden mystery to open surprise and delight, warm golden-pink color grading becoming slightly brighter and more vivid as the face appears, gentle camera movement following the turn, NO stiff or mechanical morphing, NO abrupt cuts, this reveal deserves a slightly longer duration with deliberate pacing, 3.5 seconds duration
```

### 视频2: 惊喜面庞→递合照（首帧=图片2，尾帧=图片3，3-3.5秒）

```
Kling first-last frame transition video. Start frame: a young handsome Asian man in bachelor's gown on a peach blossom path, facing the camera with a surprised and delighted expression, warm bright golden light on his face. End frame: the same man now holding and presenting a printed photograph toward the camera (POV), the photo shows two people in bachelor's gowns at a campus entrance — himself and the viewer, with bright sunny smiles, his own face now shows a sunshine smile. The transition should be smooth, natural, and aesthetically beautiful — the scene gently evolves from the surprised face moment to him reaching out and presenting the shared photo, the expression naturally shifts from surprise to warm sunshine smile, the photo gradually appears in his hands as a precious shared memory, warm golden color palette maintained throughout, gentle camera pull-in following the hand movement, NO stiff or mechanical morphing, NO abrupt cuts, sweet and touching transition from surprise to shared joy, 3.5 seconds duration
```

### 视频3: 递合照→聚焦合照（首帧=图片3，尾帧=图片4，2.5-3秒）

```
Kling first-last frame transition video. Start frame: a young man in bachelor's gown holding and presenting a photograph of two graduates toward the camera (POV), the photo shows two people with sunny smiles at a campus entrance. End frame: a close-up focused entirely on the photograph itself — two people in bachelor's gowns standing side by side at the campus entrance with bright sunny smiles, warm golden lighting, everything else softly blurred. The transition should be smooth, natural, and aesthetically beautiful — the camera gently zooms in from the man holding the photo to focus entirely on the photograph itself, the warmest and softest color palette of the sequence gradually emerging as the focus narrows, sentimental atmosphere intensifying, NO stiff or mechanical morphing, NO abrupt cuts, transition from interaction to intimate focus on shared memory, 3 seconds duration
```

### 视频4: 合照定格结尾（首帧=图片4，无尾帧，3-4秒）

```
Kling first-frame-only video. Start frame: a close-up focused entirely on a photograph showing two people in bachelor's graduation gowns at a campus entrance with sunny joyful smiles, warm golden ambient light. NO end frame provided — this is a final hold sequence. Slow gentle camera hold with very subtle breathing movement, the warmest soft golden tones suggesting precious shared memory and tender closure, sentimental and intimate atmosphere, slow fade to slightly softer/warmer in the final second, emotional ending that gives the viewer time to absorb the warmth of this shared moment, 4 seconds duration. The transition style should be natural and gentle — no abrupt changes, just a peaceful, lingering final moment of two smiles frozen in time
```

---

## 脚本B — 色调递进对照表

| 场景 | 色调特征 | 情感映射 | 关键词 |
|------|---------|---------|--------|
| 帧1（背影） | 柔美粉金暖调 | 悬念期待 | pink-golden, dreamy, romantic |
| 帧2（转脸） | 明亮暖光更鲜艳 | 惊喜心动 | bright warm golden, vivid |
| 帧3（递合照） | 温暖金调+照片亮色 | 甜蜜互动 | warm golden, bright photo |
| 帧4（聚焦合照） | 柔和温暖定格 | 温馨收束 | warmest softest, intimate |

---

## 人物描述提取指南

### 脚本A（单人物）

从用户提供的参考照片中提取 `[人物描述]`：
- 性别和年龄段
- 面部特征（发型、肤色、五官特点——极其详细）
- 身体特征（身高体型、姿态习惯）
- 整体气质和风格（知性、活泼、温柔等）
- 任何用户特别强调的特征

**关键**：6张 prompt 中的人物描述必须是完全相同的文本（复制粘贴）。一致性优先于简洁性。

示例: `a young Chinese woman in her late 20s, with long black hair flowing past her shoulders, warm brown eyes, gentle smile showing slightly dimpled cheeks, fair skin with warm undertones, slender build with graceful posture, warm and intellectual demeanor`

### 脚本B（双人物）

从用户提供的参考照片中提取 `[用户描述]`（与脚本A相同的方式）。

`[校草描述]` 需额外构建——如果用户提供了校草的参考照片，提取特征；如果用户只描述了概念（如"一个英俊帅气的年轻亚裔男生"），则构建详细描述：

示例: `a young handsome Asian man around 22-25 years old, with short neat black hair, warm bright eyes with a slight sparkle, clean-shaven with a defined jawline, fair skin with warm undertones, athletic lean build, wearing a bright and youthful expression that shifts between bashful shyness and sunny confidence, overall demeanor of a charming campus heartthrob`

**关键**：
- `[校草描述]` 在帧1-4中完全相同（复制粘贴）
- `[用户描述]` 在帧3-4中完全相同（复制粘贴）
- 两个人物的描述之间要有明显差异（不同发型、不同五官特征），避免生成时混淆为同一人
