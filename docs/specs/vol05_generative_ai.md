# Vol.05 生成式 AI / Generative AI

- Source image: `assets/reference/volumes/5.生成式AI.png`
- Declared volume number in header: **Vol.05** (matches filename number 5 — no discrepancy)
- Aspect: portrait 2:3 (1024×1536 reference)
- Theme note: light background like Vol.04 (see §6).

## 1. Header

- Left badge: dark navy rounded square `Modern AI Atlas` + pill `Vol.05`.
- Title (zh): **生成式 AI**
- Subtitle (en): **Generative AI** (indigo)
- Tagline (zh): **让机器创造内容，开启人机共创新时代**
- Top-right quote box:
  > 生成式 AI 不仅重塑世界，更能创造世界。
  > — Sam Altman
- Far-right header illustration: human-head silhouette filled with a glowing neural network (blue/orange).

## 2. Legend row

No top legend row. Bottom-left **图例 (Legend)** panel contains 9 chips (icon + zh + en):

文本 (Text) · 图像 (Image) · 音频 (Audio) · 视频 (Video) · 3D (3D) · 代码 (Code) · 模型 (Model) · 工具 (Tools) · 应用 (Application)

## 3. Sections (in top-to-bottom order)

Sections unnumbered; dark-navy zh title + en in parentheses.

### 3.1 生成式 AI 发展时间线 (Timeline)

6 era columns above a navy axis; decorative sketch icons under each era (terminal window with `> hello world / hello AI / AI is future / future ...`, graph sketch, VAE-style `x → W → x'` diagram, GPT-3 network sketch labeled `GPT-3 / 175B 参数`, OpenAI swirl logo, painter palette, brain, robot head, globe).

| Era | Years | Summary | Bullets / 代表 |
|-----|-------|---------|----------------|
| 早期萌芽阶段 | 1950s–1990s | 使用规则与统计方法生成简单内容 | Markov 链、文法系统等早期尝试 |
| 概率图模型阶段 | 2000s–2010s | 概率图模型发展 | 代表: HMM, CRF, RBM, DBN |
| 深度生成模型阶段 | 2014–2017 | 深度学习推动生成模型突破 | 代表: VAE, GAN |
| 预训练大模型阶段 | 2018–2020 | 大规模预训练模型涌现 | 代表: GPT-1/2/3, BERT, T5 |
| 大模型生成突破阶段 | 2021–2022 | 多模态与指令微调兴起 | 代表: DALL-E, Stable Diffusion, ChatGPT |
| 通用生成智能阶段 | 2023–至今 | 更强大、更可控、更安全 | 多模态、智能体与工具融合；迈向通用人工智能 (AGI) |

### 3.2 生成式 AI 核心概念 (Core Concepts)

Left vertical list (icon + title + desc):

- 生成 (Generation) — 从随机分布中学习，生成新的内容
- 条件生成 (Conditional Generation) — 在给定条件（文本/图像等）下生成内容
- 潜在表示学习 (Representation Learning) — 学习数据的潜在分布与特征表示
- 创造与多样性 (Creativity & Diversity) — 生成新颖、多样、富有创意的内容
- 可控性 (Controllability) — 通过提示、参数等方式控制生成结果
- 对齐与安全 (Evaluation & Alignment) — 评估生成质量，确保安全、对齐人类价值

### 3.3 主流生成式模型类型 (Main Generative Model Types)

6 cards in 3×2 grid (icon graphic + zh/en title + capability line + 示例):

- 语言大模型 (LLMs) — 生成文本、对话、代码等 — 示例: GPT-4, Llama 3, Claude 3, PaLM 2
- 图像生成模型 — 生成图像、插画、设计等 — 示例: DALL-E 3, Midjourney, Stable Diffusion
- 音频生成模型 — 生成音乐、语音、音效等 — 示例: MusicLM, ElevenLabs, Suno
- 视频生成模型 — 生成视频、动画、特效等 — 示例: Sora, Pika Labs, Runway Gen-3
- 3D 生成模型 — 生成 3D 物体、场景等 — 示例: DreamFusion, Magic3D, Point-E
- 多模态生成模型 — 跨模态理解与内容生成 — 示例: GPT-4V, Gemini 1.5, Claude 3, Flamingo

### 3.4 生成过程 (The Generative Process)

Right vertical 5-step flow (numbered icons, downward arrows):

1. 需求输入 (Input) — 用户输入提示、条件或数据
2. 理解与建模 (Modeling) — 模型理解输入，建立生成分布
3. 生成 (Generation) — 从分布中采样，生成内容
4. 优化与筛选 (Refinement) — 对结果进行优化、筛选与调整
5. 输出与应用 (Output & Use) — 输出结果并应用于实际场景

### 3.5 技术基础与关键方法 (Technical Foundations)

Left column, each = title + zh desc + 如: examples + a small formula/diagram sketch:

- 自回归模型 (AutoRegressive) — 基于历史生成下一个元素 — 如: GPT 系列 — diagram `x₁ → x₂ → x₃ → … → xₙ`
- 变分自编码器 (VAE) — 学习潜在空间分布进行生成 — 如: VAE, β-VAE — diagram 编码器 q(z|x) → z → 解码器 p(z|a)
- 生成对抗网络 (GAN) — 生成器与判别器对抗训练 — 如: GAN, StyleGAN — diagram 噪声串 z → 生成器 G → 图像 → 判别器 D → 真/假
- 扩散模型 (Diffusion Models) — 通过逐步去噪生成高质量内容 — 如: Stable Diffusion, DALL-E 3 — diagram 噪声 → 去噪步骤 → 图像
- 流匹配模型 (Flow Matching) — 学习连续变换将噪声映射到数据 — 如: Imagen, Flow Matching — diagram 噪声 ⇢ 数据

### 3.6 生成式 AI 典型架构 (Typical Architectures)

4 architecture mini-diagrams:

- Transformer 架构（核心基础）— 自注意力机制，支持长序列建模 — `输入嵌入 → Transformer Block × N → 输出层`
- 编码器-解码器 (Encoder-Decoder) — 用于条件生成、机器翻译等 — `编码器 → 上下文向量 → 解码器`
- 扩散模型架构 (Diffusion U-Net) — U-Net 结构 + 时间步嵌入 — (U-shaped block diagram)
- 多模态融合架构 (Multimodal Fusion) — 跨模态编码 + 融合 + 解码 — `文本 / 音频 → 融合模块 → 生成`

### 3.7 应用场景 (Applications)

9 icon tiles (zh + en subtitle): 内容创作 文章、故事、诗歌等 · 图像设计 插画、海报、Logo 等 · 音乐创作 作曲、编曲、音乐生成 · 视频制作 视频生成、剪辑、特效 · 代码生成 代码编写、注释、调试 · 虚拟人/数字人 数字人生成与驱动 · 游戏开发 场景、角色、剧情生成 · 教育学习 个性化内容生成 · 科学研究 分子、蛋白质、材料生成

Below: 更多领域… row of 6 small icons: 营销广告, 电商, 金融, 医疗健康, 建筑设计, 工业制造

### 3.8 重要数据集 (Key Datasets)

Table, headers: 类型 | 数据集 | 简介

| 类型 | 数据集 | 简介 |
|------|--------|------|
| 文本 | C4 | 大规模清洗文本数据集 |
| 文本 | The Pile | 多领域、多语言文本数据集 |
| 代码 | CodeParrot | GitHub 代码数据集 |
| 图像 | LAION-5B | 大规模图像-文本对数据集 |
| 图像 | COCO | 图像识别与描述数据集 |
| 音频 | LibriTTS | 语音合成数据集 |
| 视频 | WebVid-10M | 大规模视频数据集 |
| 多模态 | CC3M | 图像-文本对数据集 |

### 3.9 评估指标 (Evaluation Metrics)

Four groups:

- 文本生成: Perplexity (PPL); BLEU, ROUGE, METEOR; BERTScore, GPTScore
- 图像生成: FID (Fréchet Inception Distance); IS (Inception Score); CLIP Score
- 音频生成: MOS (Mean Opinion Score); FAD (Fréchet Audio Distance); Mel Cepstral Distortion
- 通用评估: 人类评估（主观质量）; 安全性评估（有害内容、偏见等）; 对齐性评估（价值观对齐）

### 3.10 生成式 AI 生态系统 (Ecosystem)

Four columns with logos:

- 基础模型 (Model Providers): OpenAI, Google, Meta, Anthropic
- 开源社区 (Open Source): Hugging Face, ModelScope, LLaMA, Falcon
- 开发工具 (Tools & Platforms): LangChain, LlamaIndex, Weights & Biases, Ray, Pinecone
- 应用生态 (Applications): ChatGPT, Midjourney, Notion AI, GitHub Copilot

### 3.11 挑战与未来 (Challenges & Future)

**主要挑战 (Challenges)** — 6 red icon items: 数据隐私与安全 · 生成内容真伪难辨 *(transcribed from small text; "真伪难辨" slightly uncertain but contextually consistent)* · 偏见与公平性 · 可控性与可解释性 · 高昂的算力成本 · 法律与伦理问题

**未来趋势 (Future Trends)** — 6 green icon items: 更强大的多模态生成与理解能力 · 更高效的模型（小型化、轻量化、边缘化） · 更可控、可解释、可靠的生成式系统 · AI 智能体与工具使用能力增强 · 与物理世界的深度融合 · 迈向通用人工智能 (AGI)

## 4. Bottom band(s)

- Dark navy gradient banner with glowing brain illustration; bilingual quote:
  > 生成式 AI 正在重塑内容生产的方式，释放人类的创造力，推动社会进入智能共创的新时代。
  > Generative AI is reshaping how we create, enabling human creativity, and driving us into a new era of intelligent co-creation.
- No NEXT Vol.XX teaser, no summary stats row.

## 5. Graph content (for knowledge graph nodes/edges)

### Nodes

| id | zh label | en label | year | kind |
|----|----------|----------|------|------|
| markov_chain | 马尔可夫链 | Markov Chain | 1950 | concept |
| hmm | 隐马尔可夫模型 | HMM | 1970 | model |
| crf | 条件随机场 | CRF | 2001 | model |
| rbm | 受限玻尔兹曼机 | RBM | 2006 | model |
| dbn | 深度信念网络 | DBN | 2006 | model |
| vae | 变分自编码器 | VAE | 2014 | milestone |
| gan | 生成对抗网络 | GAN | 2014 | milestone |
| stylegan | 风格生成网络 | StyleGAN | 2018 | model |
| gpt_series | GPT 系列 | GPT-1/2/3 | 2018 | milestone |
| bert | 双向编码器 | BERT | 2018 | milestone |
| t5 | 统一文本到文本 | T5 | 2019 | model |
| dall_e | 文本到图像 | DALL-E | 2021 | model |
| stable_diffusion | 潜在扩散模型 | Stable Diffusion | 2022 | milestone |
| chatgpt | 对话生成 | ChatGPT | 2022 | milestone |
| dall_e_3 | 文本到图像 v3 | DALL-E 3 | 2023 | model |
| midjourney | 图像生成服务 | Midjourney | 2022 | industry |
| gpt_4 | 大语言模型 | GPT-4 | 2023 | milestone |
| llama_3 | 开源大模型 | Llama 3 | 2024 | model |
| claude_3 | 大语言模型 | Claude 3 | 2023 | model |
| palm_2 | 大语言模型 | PaLM 2 | 2023 | model |
| musiclm | 音乐生成 | MusicLM | 2023 | model |
| suno | 音乐生成 | Suno | 2023 | industry |
| elevenlabs | 语音合成 | ElevenLabs | 2023 | industry |
| sora | 视频生成 | Sora | 2024 | milestone |
| pika_labs | 视频生成 | Pika Labs | 2023 | industry |
| runway_gen3 | 视频生成 | Runway Gen-3 | 2024 | industry |
| dreamfusion | 文本到 3D | DreamFusion | 2022 | paper |
| magic3d | 文本到 3D | Magic3D | 2022 | paper |
| point_e | 点云生成 | Point-E | 2022 | model |
| gpt_4v | 多模态大模型 | GPT-4V | 2023 | model |
| gemini_1_5 | 多模态大模型 | Gemini 1.5 | 2024 | model |
| flamingo | 少样本多模态 | Flamingo | 2022 | model |
| imagen | 文本到图像 | Imagen | 2022 | model |
| flow_matching | 流匹配 | Flow Matching | 2022 | concept |
| diffusion_models | 扩散模型 | Diffusion Models | 2020 | concept |

### Suggested edges

- `rbm → dbn` — **inherits** (DBN is stacked RBMs)
- `vae → beta_vae` — n/a (β-VAE mentioned as example; optional node)
- `gan → stylegan` — **inherits**
- `vae ↔ gan` — **converges** (parallel 2014 deep generative routes)
- `diffusion_models → stable_diffusion` — **inherits** (latent diffusion lineage)
- `diffusion_models → dall_e_3` — **converges** (per poster: DALL-E 3 listed under diffusion)
- `diffusion_models → imagen` — **inherits** (cascaded diffusion)
- `flow_matching → stable_diffusion` — **converges** (flow-matching training of SD3; poster lists them side by side)
- `gpt_series → chatgpt → gpt_4` — **inherits** (same product line)
- `bert ↔ gpt_series` — **converges** (explicit AI圣经 rule: 2018 fork, GPT is NOT a descendant of BERT)
- `t5 ↔ bert` — **converges**
- `gpt_series → dall_e` — **composes** (DALL-E 1 = GPT-3-style autoregression over image tokens)
- `clip → dall_e_3` — **composes** (cross-volume edge to Vol.04 CLIP; k2 may link volumes)
- `stable_diffusion → sora` — **converges** (DiT route; AI圣经: Sora → Cosmos-type relations are 趋同 not 继承)
- `stable_diffusion ↔ midjourney ↔ pika_labs ↔ runway_gen3` — **converges** (parallel products)
- `dreamfusion ↔ magic3d ↔ point_e` — **converges** (parallel text-to-3D routes)
- `gpt_4 → sora` — **composes** (transformer + diffusion; flag as uncertain)

## 6. Style notes

- Same light theme as Vol.04: off-white lavender background, dark navy titles, indigo section accents, white cards with light borders.
- Model-type cards (3.3) have colored header accents and example chips in gray pills.
- Architecture diagrams (3.6) use small gray/indigo blocks with arrows — simple flat vector sketches.
- Challenges icons red; future-trend icons green; section 3.11 logos printed in brand colors.
- Bottom banner dark navy gradient with a glowing-brain image and bilingual (zh white + en light-blue) quote text.
- Timeline decorations include hand-drawn-style sketches (terminal, network graphs, logos) — these are ornamental, not data.
