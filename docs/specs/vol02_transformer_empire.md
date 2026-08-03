# Vol.02 Transformer 帝国 / Transformer Empire

- Source image: `2.Transformer帝国.png` (1024×1536), redesigned in this implementation as a horizontal knowledge map.
- Delivered series label in header: **Modern AI Atlas Vol.02**
- Filename number: 2 — matches header. No discrepancy.
- Aspect: 16:9 landscape knowledge map (`3520×1980` canvas).
- Note: the current implementation preserves the reference poster's narrative density while redesigning it as a landscape story map. The reading order is causal: **sequential bottleneck → attention breakthrough → scalable pretraining → architecture branches → domain expansion → training and deployment lifecycle → physical-world loop**.

## 1. Header

- Series line: `Modern AI Atlas` + yellow chip `Vol.02`
- Title (en): **Transformer Empire** (huge white); below it (zh, yellow): **Transformer 帝国**
- Era chip: **2017 - NOW**
- Header route: **Attention → Foundation Models → Multimodal → Physical AI**
- Tagline: **From Sequential Bottlenecks to a Universal AI Engine · 从序列瓶颈到通用智能引擎**
- Right-side quote:
  > "它先让机器并行阅读，再让文字、图像、声音和行动共享同一种计算语言。" — The AI Architect

The body uses neutral cool-gray surfaces and borders. Domain colors are reserved for meaning: restrained blue for language/core architecture, green for vision, purple for multimodal, orange for generation, and teal for world models/physical AI.

Four source-attributed figures anchor the domain branches in concrete
architectures: the original Transformer encoder-decoder, ViT patch
tokenization, CLIP contrastive alignment, and DiT conditioning blocks. They
are embedded as supporting raster figures inside the SVG; all explanatory
poster copy remains editable vector text.

## 2. Legend row

Full-width reading legend below the header. Categories occupy the left half and relation semantics the right half so neither group can overflow or collide.

| Color | zh label | Meaning |
|-------|----------|---------|
| blue | NLP (语言) | language models |
| green | CV (视觉) | vision models |
| purple | 多模态 | multimodal |
| orange | 生成模型 | generative models |
| teal | 世界模型 / 具身 | world models / embodied |
| gray | 其他领域 | other domains |

Edge styles:

| Style | zh label |
|-------|----------|
| solid arrow | 直接继承 |
| dashed arrow | 改进/优化 |
| dotted arrow | 并行/独立发展 |
| double-line | 组合/融合 |
| dash-dot arrow | 影响/启发 |

(These map to the project relations: 直接继承=inherits solid, 趋同=converges dashed, 组合=composes dotted; the poster splits 趋同 into 改进/优化 + 并行/独立发展 and adds 影响/启发.)

## 3. Sections (top-to-bottom)

### 3.1 十年四幕

The top timeline is a causal story rather than a model inventory:

- Act 1, 2017: attention replaces recurrent computation as the main sequence-modeling path.
- Act 2, 2018-2020: encoder, decoder, and encoder-decoder pretraining mature; scaling and vision transfer emerge.
- Act 3, 2021-2022: aligned representations connect language, vision, and generation.
- Act 4, 2023-2026: open models, reasoning models, native multimodality, agents, VLA, and world models move toward action.

### 3.2 Core row: 瓶颈如何被击穿 | 标准架构 | 信息如何穿过模型

**Problem / breakthrough / scaling flywheel**:
- RNN sequential computation creates long dependency paths and low hardware parallelism.
- Self-attention lets arbitrary tokens exchange information directly.
- Parallel training makes much larger data/model/compute regimes practical.
- Pretraining, transfer, scaling, and emergent capabilities reinforce one another.

Summary:
**The breakthrough is the combined algorithm-data-hardware flywheel, not attention in isolation.**

**Transformer 标准架构**:
Input → Embedding → Positional Encoding → Multi-Head Attention → Add & Norm → Feed Forward → Add & Norm → Output

**One input's journey**:
- Tokenize: split text, images, audio, state, or action into computable units.
- Embed: convert tokens to vectors and add order, spatial, or temporal position.
- Attend: use Q/K relevance weights to route information carried by V.
- Transform: stack attention, FFN, residual connections, and normalization.
- Decode: produce a representation, prediction, generated token, tool call, or action.

The reusable mechanism matrix also covers the modern operating path: Q/K/V,
causal masks and cross-attention, RoPE, FFN/MoE, residual normalization,
MQA/GQA, FlashAttention, and KV Cache. These are mechanisms or engineering
optimizations, not separate architecture lineages.

### 3.3 三类核心架构

Three explanatory cards replace the previous flat taxonomy strip:

- Encoder — bidirectional understanding; classification, retrieval, extraction, and embeddings; BERT / RoBERTa / DeBERTa / E5 / BGE.
- Decoder — causal next-token generation; dialogue, writing, code, and tool use; GPT / LLaMA / Qwen / Mistral / DeepSeek.
- Encoder-Decoder — input encoding plus cross-attention-conditioned generation; translation, summarization, and transformation; T5 / BART / mT5 / mBART / PEGASUS / NLLB.

The next section owns domain expansion, so architecture families and application domains are no longer repeated in two competing maps.

### 3.4 Five empire branches

- NLP 帝国: GPT / LLaMA / Qwen; encoder for understanding, decoder for generation, T5 for text-to-text tasks.
- Vision 帝国: ViT turns images into patch sequences; DETR unifies detection; DINO/SAM learn generic visual representations; SigLIP/EVA strengthen visual-language interfaces.
- Diffusion 帝国: early Stable Diffusion uses latent diffusion + U-Net; DiT/MMDiT/SD3/Flux represent the transformer diffusion route.
- 多模态帝国: CLIP aligns image/text; Flamingo/LLaVA connect vision and language; GPT-4o/Gemini move toward native multimodality.
- 物理 AI 帝国: VLM expands to VLA; world models learn environment dynamics; agents close the execution loop.

### 3.5 Cross-domain fusion and worked examples

Fusion band:
Text / Image / Video / Audio / Action / World State → **Token + Attention + Shared Representation** → 理解 / 生成 / 预测 / 规划 / 决策

Three editable SVG worked examples make the mechanism concrete:
- Language: in “小红把书收好，因为她喜欢”, attention links “她” back to “小红” so the token representation incorporates its referent.
- Vision: an image is divided into patch tokens, transformed as a sequence, and aggregated into a recognition result.
- Embodied AI: perception feeds prediction/planning, planning emits an action, and environment feedback closes the loop.

The operating lifecycle closes the gap between an architecture diagram and a
deployed system:
Data → self-supervised pretraining (MLM / Causal LM / Denoising) → SFT →
preference alignment (RLHF / DPO) → inference optimization (KV Cache,
quantization, batching) → tools, memory, planning, and Agent feedback.

### 3.6 当前挑战 + 未来方向 + 理解边界

Challenges:
- 长上下文效率 / KV Cache
- 推理成本与延迟
- 长期记忆与可解释性
- 多模态统一表示
- 世界建模与闭环执行

Future directions:
- Sparse / Linear Attention
- MoE 与动态计算
- Long Context 与外部记忆
- Unified Multimodal Transformer
- World Models + Embodied Foundation Models

Beginner boundary checks:
- A Transformer is not a database; probabilistic generation still needs retrieval and verification.
- Context is not persistent memory; durable experience needs external storage and update mechanisms.
- Next-token prediction is not a complete agent; reliable execution needs tools, planning, feedback, and recovery.
- Fluent language is not a world model; physical causality needs environment data, simulation, or interaction.

The footer bridges directly into Vol.03, the decoder branch and the LLM era.

## 4. Technical verification sources

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- Dao et al., [FlashAttention](https://arxiv.org/abs/2205.14135)
- Ainslie et al., [GQA: Training Generalized Multi-Query Transformer Models](https://aclanthology.org/2023.emnlp-main.298/)
- DeepSeek-AI, [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)
- DeepSeek-AI, [DeepSeek-R1](https://arxiv.org/abs/2501.12948)
- Qwen Team, [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)
- OpenAI, [Introducing GPT-4.1 in the API](https://openai.com/index/gpt-4-1/)
- Google DeepMind, [Gemini 2.5](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-thinking-updates-march-2025/)
- Kim et al., [OpenVLA](https://arxiv.org/abs/2406.09246)
- NVIDIA, [Cosmos World Foundation Model Platform](https://developer.nvidia.com/blog/advancing-physical-ai-with-nvidia-cosmos-world-foundation-model-platform/)
- NVIDIA, [Cosmos 3](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/)

## 5. Legacy detail retained below

The following detail records the previous portrait implementation and model inventory. It remains useful for content provenance, but the active poster layout is the landscape map described above.

### 4.1 Previous top row: 为什么是 Transformer? | hero panel | 关键奠基论文

**Left panel — 为什么是 Transformer?** (5 icon bullets):
- 并行计算 — 全局注意力，打破 RNN 的顺序依赖，极大提升训练效率
- 长距离依赖 — 任何位置之间可直接建模，捕捉长距离信息
- 可扩展性 — 参数规模、数据规模、计算规模三维度 Scaling
- 通用性 — 文本、图像、语音、视频、多模态、甚至策略学习
- 能力涌现 — Scale 带来 In-context Learning、工具使用与复杂推理等新能力

**Center hero panel — Transformer (2017) / Attention Is All You Need**:
- Google logo; Encoder–Decoder architecture diagram (the classic Vaswani figure)
- Caption: 提出 Multi-Head Attention 机制，完全基于注意力的序列建模架构，奠定现代 AI 基础

**Right panel — 关键奠基论文 Key Papers** (portrait photo + year + citation):
- 2017 Vaswani et al. — Attention Is All You Need (NeurIPS 2017)
- 2018 Devlin et al. — BERT: Pre-training of Deep Bidirectional Transformers (NAACL 2019)
- 2018 Radford et al. — Improving Language Understanding by Generative Pre-Training
- 2020 Dosovitskiy et al. — An Image is Worth 16x16 Words: Transformers for Image Recognition (ICLR 2021)
- 2022 Ramesh et al. — Hierarchical Text-Conditional Image Generation with CLIP Latents

### 3.2 Architecture family panels (4 columns + side panels)

**Encoder 架构 (双向理解)** — blue header; mini architecture diagram; year chips on left edge:
- 2018 **BERT (Google)** — Bidirectional Encoder Representations from Transformers
- 2019 **RoBERTa (Meta)** — A Robustly Optimized BERT Pretraining Approach
- 2020 **DeBERTa (Microsoft)** — Decoding-enhanced BERT with Disentangled Attention
- 2020 **MPNet (Microsoft)** — Masked and Permuted Pre-training
- 2023 **E5 / GTE / BGE** — Embedding Models (BAAI, Microsoft, etc.)
- 2024 **ModernBERT (Answer.AI / LightOn)** — modern encoder recipe with long context and efficient training
- Footer: 应用: 搜索、推荐、问答、理解 / 代表产品: Google Search, Bing, 等

**Decoder 架构 (自回归生成)** — blue header:
- 2018 **GPT-1 (OpenAI)** — Generative Pre-trained Transformer
- 2019 **GPT-2 (OpenAI)** — Scaling Laws Start Emerging
- 2020 **GPT-3 (OpenAI)** — 175B Parameters Few-shot Learning
- 2023 **GPT-4 (OpenAI)** — Stronger Reasoning, Multimodal
- 2023+ **LLaMA (Meta) / Qwen (阿里) / DeepSeek (深度求索) / Mistral** — Open-source LLMs
- Footer: 应用: 对话、写作、编程、通用智能 / 代表产品: ChatGPT, Copilot, Claude, 通义千问, 等

**Encoder-Decoder 架构 (序列到序列)** — purple header:
- 2019 **T5 (Google)** — Text-to-Text Transfer Transformer
- 2019 **BART (Meta)** — Denoising Sequence-to-Sequence Pre-training
- 2022 **UL2 (Google)** — Unified Language Learner
- 2022 **FLAN-T5 (Google)** — Instruction Tuning
- 2020–2022 **mT5 / mBART / PEGASUS / NLLB** — multilingual, denoising and summarization-oriented seq2seq models
- Footer: 应用: 翻译、摘要、重写、生成 / 代表产品: Google Translate, 文心一言等

**Attention 通用模块 (核心机制)** — dark navy header:
- Multi-Head Attention — 并行关注不同子空间
- MQA / GQA — 共享或分组 KV 头，降低推理缓存成本
- FlashAttention — IO-aware 精确注意力，显著提升训练与推理效率
- MLA — 低秩潜变量 KV 表示，面向高效长上下文推理
- Scaled Dot-Product Attention — 稳定梯度，提升训练效果
- Positional Encoding — 注入序列位置信息
- RoPE — 旋转位置编码，支撑外推与长上下文扩展
- Feed Forward Network — 非线性变换能力
- Layer Normalization — 稳定深层训练
- Residual Connection — 缓解梯度消失
- Footer: 被所有分支继承和使用 / Transformer 的 DNA

**其他变体架构 (稀疏设计)** — gray header, bullet list:
- Reformer (2020) / Performer (2020) / Linformer (2020) / Longformer (2020) / BigBird (2020) / RWKV (2021) / Mamba (2023)

**Vision Transformer 家族 (CV)** — green header, year chips on left:
- 2020 **ViT (Google)** — Vision Transformer
- 2021 **Swin Transformer (Microsoft)** — Hierarchical Vision Transformer
- 2021 **MAE (Meta)** — Masked Autoencoders
- 2021 **DeiT (Facebook)** — Data-efficient ViT
- 2022 **DINO (Meta)** — Self-Distillation
- 2022 **BEVFormer (Horizon / Shanghai AI Lab)** — spatiotemporal BEV perception for autonomous driving
- 2023 **SAM (Meta)** — promptable foundation model for segmentation
- 2023 **DINOv2 (Meta)** — Stronger Visual Features
- Footer: 应用: 图像分类、检测、分割、3D 等 / 代表产品: SAM, Florence-2, 等

**生成模型家族 (Diffusion / DiT)** — orange header:
- 2022 **Stable Diffusion (Stability AI)** — Latent Diffusion (U-Net)
- 2023 **DiT (Peebles & Xie)** — Diffusion Transformer [poster year chip reads 2023; paper is 2022/ICCV 2023]
- 2023–2024 **PixArt / SD3 / MMDiT** — PixArt 系列与 Stable Diffusion 3 的 transformer diffusion 路线
- 2024 **Flux (Black Forest Labs)**
- Footer: 应用: 文生图、视频生成、3D生成等

**多模态融合家族** — purple header:
- 2021 **CLIP (OpenAI)** — Contrastive Language-Image Pre-training
- 2022 **Flamingo (DeepMind)** — Few-shot Multimodal
- 2023 **LLaVA (UW–Madison & Microsoft)** — Visual Instruction Tuning
- 2023–2024 **Qwen-VL / Qwen2-VL (阿里)** — 视觉-语言理解与多模态对话
- Footer: 应用: 多模态理解、视觉对话、VLM等

### 3.3 跨领域融合: Transformer 的无限可能 (fusion band)

Dark band: six modality chips with icons — 文本 (Text) / 图像 (Image) / 视频 (Video) / 语音 (Audio) / 3D / 点云 (3D / Point Cloud) / 时间序列 (Time Series) — arrows converging into a glowing core labeled **统一的 Transformer 表示空间**, then fanning out to five capability chips: **理解 / 生成 / 预测 / 规划 / 决策**.

### 3.4 关键技术创新时间线 (innovation timeline)

Horizontal timeline, 8 nodes (year + zh title + 2-line zh description):
- 2017 Transformer — 提出统一架构
- 2018 预训练范式 (BERT, GPT) — 引爆预训练浪潮
- 2019 大规模预训练 — 参数规模突破10亿级
- 2020 Scaling Laws — 损失与能力随规模呈可预测提升
- 2021 RoPE / 多模态预训练 (CLIP, ALIGN) — 长上下文位置编码 / 打通视觉-语言
- 2022 FlashAttention + 指令微调 / RLHF — 高效注意力与对齐训练范式成型
- 2023 GQA / MoE / 开源大模型爆发 — LLaMA, Qwen, Mixtral 等 / 生态繁荣
- 2024+ MLA + 长上下文 — 效率、推理、多模态增强，进入系统智能前夜

### 3.5 Bottom row: 产业影响 | 如何改变AI世界 | 未来演进方向

**产业影响 Industry Impact** (3 sub-columns):
- 科技巨头: Google / OpenAI / Meta / Microsoft / Baidu 百度 / 阿里巴巴 Alibaba (logos)
- 开源生态: Hugging Face / PyTorch / TensorFlow / vLLM / Transformers (logos)
- 应用落地: 搜索推荐 / 智能客服 / 内容生成 / 编程助手 / 自动驾驶 / 机器人 (icon list)

**Transformer 如何改变 AI 世界?** (5 checkmark items + summary):
- 从任务特定 → 通用基础模型
- 从手工特征 → 自学习表示
- 从小数据 → 大数据驱动
- 从单模态 → 多模态融合
- 从理解 → 生成 + 推理 + 决策
- Summary: **Transformer = 新的计算范式 (Paradigm Shift)**

**未来演进方向 Future Directions** (6 icon items, right side has a glowing cube/brain illustration):
- 更长上下文 (百万级 Token)
- 更高效率 (稀疏注意力 / 线性复杂度)
- 更强推理 (思维链 / 自我反思)
- 更强具身能力 (与物理世界交互)
- 更强多模态 (全模态融合) [parenthetical partially unclear, "全模态融合" best reading]
- 走向 AGI (通用智能)

## 4. Bottom band(s)

- Footer quote (centered, white):
  > "Transformer 不是终点，而是起点。未来的所有智能，都将建立在它的肩膀上。"
- NEXT teaser (bottom-right): **NEXT Vol.03 / LLM Era (语言大模型时代)** + `>>>` chevrons.

## 5. Graph content (nodes & edges for knowledge graph)

### Nodes

| id | zh label | en label | year | kind |
|----|----------|----------|------|------|
| transformer | Transformer | Transformer (Attention Is All You Need) | 2017 | paper |
| bert | BERT | BERT | 2018 | model |
| roberta | RoBERTa | RoBERTa | 2019 | model |
| deberta | DeBERTa | DeBERTa | 2020 | model |
| mpnet | MPNet | MPNet | 2020 | model |
| e5_gte_bge | E5 / GTE / BGE 嵌入模型 | E5 / GTE / BGE Embedding Models | 2023 | model |
| modernbert | ModernBERT | ModernBERT | 2024 | model |
| gpt1 | GPT-1 | GPT-1 | 2018 | model |
| gpt2 | GPT-2 | GPT-2 | 2019 | model |
| gpt3 | GPT-3 | GPT-3 | 2020 | model |
| gpt4 | GPT-4 | GPT-4 | 2023 | model |
| llama | LLaMA | LLaMA | 2023 | model |
| qwen | 通义千问 | Qwen | 2023 | model |
| deepseek | DeepSeek | DeepSeek | 2023 | model |
| mistral | Mistral | Mistral | 2023 | model |
| t5 | T5 | T5 | 2019 | model |
| bart | BART | BART | 2019 | model |
| ul2 | UL2 | UL2 | 2022 | model |
| flan_t5 | FLAN-T5 | FLAN-T5 | 2022 | model |
| mt5 | mT5 | mT5 | 2020 | model |
| mbart | mBART | mBART | 2020 | model |
| pegasus | PEGASUS | PEGASUS | 2020 | model |
| nllb | NLLB | NLLB | 2022 | model |
| multi_head_attention | 多头注意力 | Multi-Head Attention | 2017 | concept |
| mqa | 多查询注意力 | Multi-Query Attention | 2019 | concept |
| gqa | 分组查询注意力 | Grouped-Query Attention | 2023 | concept |
| flash_attention | FlashAttention | FlashAttention | 2022 | concept |
| mla | 多头潜在注意力 | Multi-head Latent Attention | 2024 | concept |
| scaled_dot_product | 缩放点积注意力 | Scaled Dot-Product Attention | 2017 | concept |
| positional_encoding | 位置编码 | Positional Encoding | 2017 | concept |
| rope | 旋转位置编码 | Rotary Position Embedding | 2021 | concept |
| ffn | 前馈网络 | Feed Forward Network | 2017 | concept |
| layernorm | 层归一化 | Layer Normalization | 2017 | concept |
| residual | 残差连接 | Residual Connection | 2017 | concept |
| reformer | Reformer | Reformer | 2020 | model |
| performer | Performer | Performer | 2020 | model |
| linformer | Linformer | Linformer | 2020 | model |
| longformer | Longformer | Longformer | 2020 | model |
| bigbird | BigBird | BigBird | 2020 | model |
| rwkv | RWKV | RWKV | 2021 | model |
| mamba | Mamba | Mamba | 2023 | model |
| vit | Vision Transformer | ViT | 2020 | model |
| swin | Swin Transformer | Swin Transformer | 2021 | model |
| mae | MAE | Masked Autoencoders | 2021 | model |
| deit | DeiT | Data-efficient ViT | 2021 | model |
| dino | DINO | DINO | 2022 | model |
| bevformer | BEVFormer | BEVFormer | 2022 | model |
| sam | SAM | Segment Anything Model | 2023 | model |
| dinov2 | DINOv2 | DINOv2 | 2023 | model |
| stable_diffusion | Stable Diffusion | Stable Diffusion (Latent Diffusion U-Net) | 2022 | model |
| dit | DiT | Diffusion Transformer | 2023 | model |
| pixart_sd3_mmdit | PixArt / SD3 / MMDiT | PixArt / SD3 / MMDiT | 2024 | model |
| flux | Flux | Flux (Black Forest Labs) | 2024 | model |
| clip | CLIP | CLIP | 2021 | model |
| flamingo | Flamingo | Flamingo | 2022 | model |
| llava | LLaVA | LLaVA | 2023 | model |
| qwen_vl | Qwen-VL / Qwen2-VL | Qwen-VL / Qwen2-VL | 2023 | model |

### Edges (relation semantics per docs/AI圣经_修订版.md)

- transformer → bert / gpt1 / t5 (inherits) — three architecture branches
- bert → roberta (converges) [per plan: BERT ↔ RoBERTa is 趋同/竞争, NOT inheritance]
- bert → deberta (converges) ; bert → mpnet (converges)
- bert → e5_gte_bge (inherits) ; bert → modernbert (inherits) [modern encoder and embedding models derived from the encoder line]
- gpt1 → gpt2 → gpt3 → gpt4 (inherits)
- gpt3 → llama (converges) ; llama → qwen / deepseek / mistral (converges) [open-source LLMs, parallel development]
- t5 → ul2 (inherits) ; t5 → flan_t5 (inherits)
- bart ↔ t5 (converges) [contemporary seq2seq pretraining, different teams]
- t5 → mt5 (inherits) ; bart → mbart (inherits) ; t5 → pegasus (converges) ; mbart → nllb (converges)
- transformer → multi_head_attention / scaled_dot_product / positional_encoding / ffn / layernorm / residual (composes) [component modules; footer "被所有分支继承和使用 Transformer 的 DNA"]
- multi_head_attention → mqa / gqa / flash_attention (converges); gqa → mla (converges); positional_encoding → rope (converges)
- transformer → reformer / performer / linformer / longformer / bigbird (converges) [efficiency variants, parallel designs]
- transformer → rwkv (converges) ; transformer → mamba (converges) [alternative sequence models competing with attention]
- transformer → vit (inherits)
- vit → swin (converges) [per plan: Swin 不是 ViT 的直接后代]
- vit → mae (inherits) [MAE trains ViT via masked autoencoding]
- vit → deit (converges) ; deit → dino (converges) ; dino → dinov2 (inherits)
- vit → bevformer / sam (composes) [Transformer vision encoders composed into autonomous-driving perception and segmentation foundation models]
- stable_diffusion → dit (converges) [DiT replaces U-Net with transformer — 组合 of transformer into diffusion; could also model as transformer → dit (composes)]
- transformer → dit (composes) ; dit → pixart_sd3_mmdit (inherits) ; dit → flux (converges)
- clip → flamingo (converges) ; clip → llava (composes) [LLaVA = CLIP visual encoder + LLM] ; llava → qwen_vl (converges)
- clip = vit + transformer text encoder (composes) — per plan: CLIP = ViT ＋ GPT 组合, draw vit → clip (composes) and transformer → clip (composes)
- Fusion band: transformer → {text/image/video/audio/3d/time_series} unified representation space (composes)

## 6. Style notes

- Background: near-black deep navy; big white English title + yellow zh title; yellow Vol.02 chip.
- Family panels: rounded white/very-light cards with **colored header bands** (blue ×2 for encoder/decoder, purple for enc-dec + multimodal, dark navy for attention modules, gray for variants, green for ViT family, orange for diffusion); year chips are small colored pills on the left edge; model rows show bold model name + (org) + 1-2 line description.
- Side footers inside each family panel: `应用:` / `代表产品:` lines in small gray text.
- Fusion band: dark panel with neon-blue glow, modality chips with icons, central glowing "统一的 Transformer 表示空间" core, capability chips (理解/生成/预测/规划/决策).
- Innovation timeline: small triangular year markers on a horizontal line, zh title + 2-line description under each.
- Industry impact: logo grid (real company/product logos); 应用落地 as icon list.
- Future directions: dark panel with glowing cyan cube/brain illustration on the right.
- Typography: heavy bold for titles; model names bold dark; descriptions ~10-11 px gray; zh+en mixed throughout.
