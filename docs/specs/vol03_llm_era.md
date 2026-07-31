# Vol.03 大语言模型时代 / The LLM Era

- Source image: `3.大语言模型时代.png` (1536×1024)
- Declared volume number in header: **Vol.03** (badge on "Modern AI Atlas" logo block)
- Filename number: 3 — matches header. No discrepancy.
- Aspect: **landscape 3:2 (1536×1024)** — ⚠ this poster is landscape, unlike the portrait 2:3 of vols 01/02. k2 must decide whether to re-layout to portrait or support a landscape variant.
- Theme: light/white background with dark navy + blue/purple accents (same visual language as vol01b, not the dark vol01/vol02 posters).

## 1. Header

- Top-left badge: atom logo + `Modern AI Atlas` + `Vol.03` (dark navy rounded block)
- Title (zh): **大语言模型时代** / subtitle (en): **The LLM Era**
- Tagline (zh): **从规模扩展到智能涌现：理解、生成与对齐的新时代**
- Tagline (en): From Scaling to Emergence: Understanding, Generation and Alignment
- Top-right callout box:
  > 大语言模型不仅改变了NLP，它正在重塑所有软件与知识工作的底层范式。
- Atom logo at far right of header.

## 2. Legend row

No dedicated legend row on this poster. The Model Family Tree panel uses **row color coding** instead:
- blue left rail: 闭源模型 (Proprietary)
- green left rail: 开源模型 (Open Source)
- purple left rail: API / 云服务 (Platforms)

## 3. Sections (top-to-bottom)

### 3.1 大语言模型发展时间线 (里程碑)

Horizontal timeline with 11 milestone cards (year chip + title + 2-line zh description), rocket at the right end:

1. **2017 Transformer** — Attention Is All You Need
2. **2018 GPT-1** — 预训练+微调范式 / 117M参数
3. **2019 GPT-2** — 无监督预训练 / 15亿参数
4. **2020 GPT-3** — 涌现能力初现 / 1750亿参数
5. **2021 Codex** — 代码生成 / 12B参数
6. **2021 InstructGPT** — RLHF对齐 / 人类反馈强化学习
7. **2022 ChatGPT** — 对话交互 / 现象级应用
8. **2023 GPT-4 / PaLM 2 / Claude 2** — 更强理解与推理 / 多模态初步融合
9. **2023 Llama 2** — 开源浪潮 / 70B参数
10. **2024 GPT-4o / Claude 3 / Gemini 1.5** — 多模态原生 / 长上下文突破
11. **2024+ 迈向AGI** — 更强推理、记忆与行动 / 系统级能力涌现

### 3.2 大语言模型生态图谱 (Model Family Tree)

Grid: org logo rows × year columns (2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024+), model chips connected by arrows.

**闭源模型 (Proprietary)** — blue rail:
- **OpenAI**: GPT-1 → GPT-2 → GPT-3 → Codex → InstructGPT → ChatGPT / GPT-3.5 → GPT-4 → GPT-4o / GPT-5?
- **Google**: BERT → T5 → PaLM → PaLM 2 → PaLM 2-Codey → Gemini 1.0 → Gemini 1.5 / Gemini 2.0
- **Anthropic**: Claude 1 → Claude 2 → Claude 3 / Claude 3.5

**开源模型 (Open Source)** — green rail:
- **Meta (Llama)**: Llama 1 (7B/13B/33B/65B) → Llama 2 (7B/13B/70B) → Llama 3 (8B/70B) → Llama 3.1 (8B/70B/405B) → Llama 3.2 (多模态)
- **Mistral AI**: Mistral 7B → Mistral 8x7B → Mistral 8x22B → Mistral Large
- **其他开源**: Bloom → GPT-NeoX → Falcon → Yi / Qwen / Baichuan / InternLM / DeepSeek → 持续演进

**API / 云服务 (Platforms)** — purple rail:
- OpenAI API / Azure OpenAI / Google Vertex AI / AWS Bedrock / Anthropic API / 其他平台

### 3.3 大语言模型核心架构 (core architecture panel)

**Transformer 解码器结构 (Decoder-Only)** — vertical flow diagram:
输入 Tokens → Token & Position Embedding → [ RMSNorm → Masked Multi-Head Self-Attention → (⊕ residual) → RMSNorm → Feed Forward (MLP) → (⊕ residual) ] × N Layers → RMSNorm → Linear → 输出概率 (Next Token)

**预训练目标** — 下一词预测 (Next Token Prediction) token table:
- Row `Tokens`: The | cat | sat | on | the | mat
- Row `预测`: (shifted) The | cat | sat | on | the | mat | `<eos>`

**对齐技术演进** — 3-step flow:
SFT 监督微调 → Reward Model 奖励模型 → RLHF / DPO / PPO 强化学习优化

**能力涌现 (Emergent Abilities)** — 6 icon chips:
上下文学习 (In-context Learning) / 推理能力 (Reasoning) / 指令遵循 (Instruction Following) / 工具使用 (Tool Use) / 多轮对话 (Multi-turn Dialogue) / 代码生成 (Code Gen)

### 3.4 Scaling 三大维度 + 涌现能力阶梯

**Scaling 三大维度** — 3 cards + caption 三者协同推动性能持续提升:
- 模型规模 (Model Size) — 参数量 ↑
- 数据规模 (Data Scale) — 数据量 ↑
- 计算规模 (Compute Scale) — 算力 ↑

**涌现能力阶梯 (能力随规模呈现非线性增长)** — S-curve chart:
- Axes: x = 模型规模 (参数量) (Model Scale), log ticks 10⁸ → 10⁹ → 10¹⁰ → 10¹¹ → 10¹² → 10¹³⁺; y = 能力 (Ability)
- Stage callouts along the rising curve: 基础能力 (记忆/补全) → 上下文学习 (In-context Learning) → 复杂推理 (Reasoning) → 工具使用 (Tool Use) → 通用智能 (AGI 潜力)

### 3.5 主要应用场景 (application scenarios)

6 cards (icon + zh/en title + 3 bullets):
1. 智能对话 (Conversational AI): 聊天机器人 / 虚拟助手 / 客户服务
2. 内容创作 (Content Generation): 文章写作 / 文案生成 / 创意激发
3. 代码开发 (Code Development): 代码生成 / 代码补全 / 调试助手
4. 知识问答 (Question Answering): 知识检索 / 文档问答 / 教育辅导
5. 办公提效 (Productivity): 总结提炼 / 翻译润色 / 流程自动化
6. 科学研究 (Scientific Research): 文献分析 / 假设生成 / 实验设计

### 3.6 关键技术栈 (key technology stack)

5 labeled rows with pill chips:
- 预训练 Pre-training: 分布式训练 / 大规模数据处理 / 混合精度 / 梯度优化
- 微调 Fine-tuning: SFT / LoRA / QLoRA / Adapter / Prompt Tuning
- 对齐 Alignment: RLHF / DPO / PPO / Reward Model / Constitutional AI
- 推理加速 Inference: 量化 (INT8/4) / KV Cache / TensorRT / vLLM / FlashAttention
- 评估 Evaluation: 基准测试 / 人类评估 / 安全评估 / 红队测试

### 3.7 挑战与风险 (challenges & risks)

6 cards (icon + zh/en title + 2 bullets), pink/red-tinted:
1. 幻觉问题 (Hallucination): 生成不实信息 / 缺乏事实依据
2. 偏见与公平 (Bias & Fairness): 数据偏见 / 歧视与不公平
3. 安全与对齐 (Safety & Alignment): 越狱攻击 / 有害内容生成
4. 隐私与版权 (Privacy & IP): 数据隐私 / 版权争议
5. 成本与能耗 (Cost & Energy): 训练成本高 / 能耗巨大
6. 可解释性 (Interpretability): 黑箱模型 / 难以解释

### 3.8 基础支撑 (foundations)

5 icon items: 硬件算力 (GPU / TPU / NPU) / 数据资源 (高质量语料库) / 开源生态 (PyTorch / TensorFlow / Hugging Face) / 社区协作 (模型共享与创新) / 资金与人才 (持续投入与研究)

## 4. Bottom band(s)

**未来展望 (The Road to AGI)** — 6-step horizontal arrow flow:
更长上下文 (Longer Context) → 多模态统一 (Omni-modal) → 记忆增强 (Memory) → 推理增强 (Reasoning) → 智能体系统 (Agentic AI) → 通用人工智能 (AGI)

Bottom-right illustration: earth/globe over a starry sea with caption **迈向AGI的星辰大海**.

No NEXT-volume teaser on this poster.

## 5. Graph content (nodes & edges for knowledge graph)

### Nodes

| id | zh label | en label | year | kind |
|----|----------|----------|------|------|
| transformer | Transformer | Transformer | 2017 | paper |
| gpt1 | GPT-1 | GPT-1 | 2018 | model |
| gpt2 | GPT-2 | GPT-2 | 2019 | model |
| gpt3 | GPT-3 | GPT-3 | 2020 | model |
| codex | Codex | Codex | 2021 | model |
| instructgpt | InstructGPT | InstructGPT | 2021 | model |
| chatgpt | ChatGPT (GPT-3.5) | ChatGPT | 2022 | industry |
| gpt4 | GPT-4 | GPT-4 | 2023 | model |
| gpt4o | GPT-4o | GPT-4o | 2024 | model |
| bert | BERT | BERT | 2018 | model |
| t5 | T5 | T5 | 2019 | model |
| palm | PaLM | PaLM | 2022 | model |
| palm2 | PaLM 2 (含 Codey) | PaLM 2 | 2023 | model |
| gemini1 | Gemini 1.0 | Gemini 1.0 | 2023 | model |
| gemini15 | Gemini 1.5 | Gemini 1.5 | 2024 | model |
| claude1 | Claude 1 | Claude 1 | 2023 | model |
| claude2 | Claude 2 | Claude 2 | 2023 | model |
| claude3 | Claude 3 / 3.5 | Claude 3 | 2024 | model |
| llama1 | Llama 1 | Llama 1 | 2023 | model |
| llama2 | Llama 2 | Llama 2 | 2023 | model |
| llama3 | Llama 3 / 3.1 / 3.2 | Llama 3 | 2024 | model |
| mistral7b | Mistral 7B | Mistral 7B | 2023 | model |
| mixtral | Mistral 8x7B / 8x22B | Mixtral | 2023 | model |
| mistral_large | Mistral Large | Mistral Large | 2024 | model |
| bloom | BLOOM | BLOOM | 2022 | model |
| gpt_neox | GPT-NeoX | GPT-NeoX | 2022 | model |
| falcon | Falcon | Falcon | 2023 | model |
| yi | Yi | Yi | 2023 | model |
| qwen | Qwen | Qwen | 2023 | model |
| baichuan | Baichuan | Baichuan | 2023 | model |
| internlm | InternLM | InternLM | 2023 | model |
| deepseek | DeepSeek | DeepSeek | 2023 | model |
| next_token_prediction | 下一词预测 | Next Token Prediction | — | concept |
| sft | 监督微调 | SFT | — | concept |
| reward_model | 奖励模型 | Reward Model | — | concept |
| rlhf | RLHF | RLHF | — | concept |
| dpo | DPO | DPO | — | concept |
| ppo | PPO | PPO | — | concept |
| lora | LoRA / QLoRA | LoRA | — | concept |
| in_context_learning | 上下文学习 | In-context Learning | — | concept |
| scaling_law | 规模化定律 | Scaling Law | — | concept |
| emergent_abilities | 能力涌现 | Emergent Abilities | — | concept |
| constitutional_ai | Constitutional AI | Constitutional AI | — | concept |
| agentic_ai | 智能体系统 | Agentic AI | 2024 | concept |
| agi | 通用人工智能 | AGI | — | milestone |

### Edges

- transformer → gpt1 (inherits) ; gpt1 → gpt2 → gpt3 (inherits)
- gpt3 → codex (inherits) ; gpt3 → instructgpt (inherits) ; instructgpt → chatgpt (inherits) ; chatgpt → gpt4 (inherits) ; gpt4 → gpt4o (inherits)
- transformer → bert (inherits) ; bert → t5 (converges) ; t5 → palm (converges) ; palm → palm2 (inherits) ; palm2 → gemini1 (inherits) ; gemini1 → gemini15 (inherits)
- gpt3 → claude1 (converges) ; claude1 → claude2 → claude3 (inherits)
- gpt3 → llama1 (converges) ; llama1 → llama2 → llama3 (inherits)
- llama1 → mistral7b (converges) ; mistral7b → mixtral → mistral_large (inherits)
- gpt3 → bloom / gpt_neox (converges) ; bloom → falcon (converges)
- llama2 → yi / qwen / baichuan / internlm / deepseek (converges) [open-source ecosystem, parallel development]
- gpt3 → sft (composes) ; sft → reward_model (composes) ; reward_model → rlhf (composes) [对齐技术演进 chain]
- rlhf ↔ dpo (converges) [alternative alignment methods]; ppo → rlhf (composes) [RLHF uses PPO]
- gpt3 → lora (composes) [parameter-efficient fine-tuning applied to LLMs]
- scaling_law → emergent_abilities (converges) [poster: 能力随规模非线性增长]
- transformer → next_token_prediction (composes)
- claude3 → constitutional_ai (composes) [Anthropic alignment technique]
- gpt4o → agentic_ai (converges) ; agentic_ai → agi (converges) [Road to AGI chain: 更长上下文 → 多模态统一 → 记忆增强 → 推理增强 → 智能体系统 → AGI]

## 6. Style notes

- **Landscape 1536×1024, light theme**: white background; dark navy panel titles with English parentheticals; pastel blue/green/purple/pink card tints.
- Header: dark navy logo block (atom + Modern AI Atlas + Vol.03), big zh title + en subtitle, zh+en taglines, top-right callout box.
- Timeline milestone cards: light beige/cream cards with rounded corners and small icons.
- Model Family Tree: org logo in a left cell per row, colored left rail per category (blue/green/purple), model chips as white pills with thin borders connected by arrows; year column headers on top.
- Architecture diagram: stacked rounded boxes (cream/pink/blue tints) with ×N Layers bracket; token chips colored (blue input / purple output / yellow highlight).
- Emergence curve: thin purple S-curve on white axes with stage callout boxes.
- Risk cards: pink/red tinted headers; tech-stack rows: label chip on left + gray pill chips.
- Road to AGI: 6 chevron-arrow steps; bottom-right starry-sea earth illustration with caption 迈向AGI的星辰大海.
