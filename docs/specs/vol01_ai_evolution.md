# Vol.01 AI 编年史 / AI Evolution Timeline

- Source image: `0.AI编年史.png` (1024×1536)
- Declared volume number in header: **Volume 01** ("AI Technology Bible · Volume 01")
- Filename number: 0 — filename uses a 0-based index while the header declares Volume 01. Header-declared number wins. **Note: `1.人工智能基础脉络.png` also declares "Vol.01" — see vol01b spec; k2 must reconcile this series-numbering collision.**
- Aspect: portrait 2:3 (1024×1536 reference)

## 1. Header

- Title (zh): **AI 编年史 (1950-2026)** — white bold, with yellow subtitle **人工智能发展全景图** to the right of the title
- Series line (below title, yellow/white): `AI Technology Bible · Volume 01  |  AI Evolution Timeline`
- Top-right quote (white, beside a portrait photo of Alan Turing):
  > "人工智能是人类有史以来最伟大的创造，也是我们面临的最深刻的变革。" —— 图灵
- Dark navy/black header band.

## 2. Legend row

Located directly under the header, label `图例:` on the left. Five chips (icon + zh label), dark background:

| Chip | Color (approx) | zh label | Meaning |
|------|----------------|----------|---------|
| ◎ circle icon | blue | 里程碑事件 | milestone events |
| gear icon | green | 关键技术突破 | key technology breakthroughs |
| atom icon | orange/red | 代表性模型/算法 | representative models/algorithms |
| book icon | dark blue | 重要论文 | important papers |
| factory icon | purple/brown | 工业落地/应用 | industry adoption/applications |

## 3. Sections (top-to-bottom)

The poster is a stack of **6 numbered era bands**; each band = left column `时代特征` bullet list + 6 event cards (each with year chip, zh/en title, mini image/diagram, 2-line zh description, optional 论文 citation line) + right column panel. Band headers show a numbered circle, zh era name, year range, and zh subtitle.

### Section 1 — AI 萌芽时代 1950-1989 | 从思想到符号主义 (blue accent)

- 时代特征 (left column):
  - 以符号推理为主
  - 依赖人工设计规则
  - 缺乏学习能力
  - 计算资源极度有限
- Cards:
  1. **1950 图灵测试 / Alan Turing** — 提出"机器能思考吗？" 论文: Computing Machinery and Intelligence (1950). Mini image: chessboard.
  2. **1956 达特茅斯会议 / Dartmouth Conference** — AI 正式诞生 / 标志: 人工智能这个学科的诞生 [verbatim wording slightly garbled on poster]. Mini image: B&W group photo.
  3. **1966 ELIZA / 聊天机器人** — 第一个聊天机器人程序 / 开创人机对话研究. Mini image: terminal screen.
  4. **1970s 专家系统 / Expert Systems** — 符号主义达到巅峰 / 广泛应用于工业、医疗. Mini-diagram: `IF … THEN …` and `规则库 → 推理机` flow.
  5. **1980s AI Winter / 第一次AI寒冬** — 期望过高，投入减少 / 研究进入低谷. Mini image: declining red curve + snowflake.
  6. **1989 Backprop / 反向传播算法** — 推动神经网络重新崛起 / 为深度学习奠基. Mini-diagram: small neural-net graph.
- Right panel **为什么失败?**:
  - 规则难以穷尽
  - 缺乏学习能力
  - 无法处理不确定性
  - 计算能力不足
  - 数据稀缺

### Section 2 — 机器学习时代 1990-2011 | 从统计学习到特征学习 (green accent)

- 时代特征:
  - 数据驱动思想兴起
  - 统计学习方法主导
  - 特征工程依赖人工
  - 模型泛化能力提升
- Cards:
  1. **1990 统计学习 / Statistical Learning** — 机器学习理论基础建立 / VC理论、结构风险最小化. Mini image: scatter + regression line.
  2. **1995 SVM 支持向量机 / Vapnik** — 小样本学习方法突破 / 高维空间有效分类. Mini image: margin/hyperplane diagram.
  3. **1998 CNN / LeCun** — 卷积神经网络提出 / 用于手写数字识别. Mini image: LeCun photo + MNIST digits.
  4. **2001 LSTM / Hochreiter & Schmidhuber** — 解决RNN长序列依赖问题. Mini-diagram: LSTM cell.
  5. **2008 深度学习复兴 / Deep Learning Revival** — 大数据 + GPU 驱动 / 深度学习再次兴起. Mini-diagram: deep MLP stack.
  6. **2011 Google Brain / 深度神经网络** — 大规模神经网络 / 开启产业化应用. Mini image: Google Brain logo.
- Right panel **关键推动力**:
  - 算法理论发展
  - 计算能力提升
  - 数据规模增长
  - 特征学习能力增强

### Section 3 — 深度学习革命 2012-2016 | 从感知智能到端到端学习 (orange/red accent)

- 时代特征:
  - 深度网络性能突破
  - 端到端学习兴起
  - 感知任务全面领先
  - Attention 机制诞生
- Cards:
  1. **2012 AlexNet / Krizhevsky** — ImageNet冠军 / 深度学习里程碑. 论文: ImageNet Classification with Deep Convolutional Neural Networks (NIPS 2012). Mini-diagram: CNN stack.
  2. **2013 Word2Vec / Mikolov** — 词向量革命 / 让文字拥有语义空间. 论文: Efficient Estimation of Word Representations in Vector Space (ICLR 2013). Mini-diagram: CBOW/skip-gram.
  3. **2014 Seq2Seq / Sutskever** — 序列到序列模型 / 机器翻译重大突破. 论文: Sequence to Sequence Learning with Neural Networks (NIPS 2014). Mini-diagram: encoder-decoder.
  4. **2015 ResNet / He et al.** — 残差网络提出 / 突破超深网络极限. 论文: Deep Residual Learning for Image Recognition (CVPR 2016). Mini-diagram: residual block.
  5. **2015 Attention / Bahdanau** — 注意力机制提出 / 解决长距离依赖. 论文: Neural Machine Translation by Jointly Learning to Align and Translate (ICLR 2015). Mini-diagram: attention alignment.
  6. **2016 AlphaGo / DeepMind** — 深度学习 + 强化学习 / 战胜人类顶尖棋手. Mini image: Go board.
- Right panel **革命意义**:
  - 感知任务超越人类
  - 端到端学习成为主流
  - Attention 打开新时代
  - 为 Transformer 铺路

### Section 4 — Transformer时代 2017-2020 | 统一架构，开启大模型时代 (blue accent)

- 时代特征:
  - 注意力机制为核心
  - 并行计算能力强
  - 可扩展性极佳
  - 大模型时代开启
- Cards:
  1. **2017 Transformer / Vaswani et al.** — Attention Is All You Need / 奠定基石架构. 论文: Attention Is All You Need (NeurIPS 2017). Mini-diagram: encoder-decoder Transformer.
  2. **2018 BERT / Google** — 双向预训练 / NLP 范式革命. 论文: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (NAACL 2019).
  3. **2019 GPT-2 / OpenAI** — 大规模无监督预训练 / 生成能力惊人. 论文: Language Models are Unsupervised Multitask Learners (2019).
  4. **2019 T5 / Google** — 统一文本到文本框架 / 支持多种任务. 论文: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (JMLR 2020).
  5. **2020 GPT-3 / OpenAI** — 1750亿参数 / Scaling Law 惊现. 论文: Language Models are Few-Shot Learners (NeurIPS 2020). Mini image: OpenAI logo.
  6. **2020 Vision Transformer (ViT) / Google** — 将Transformer扩展到图像 / 打破CNN垄断 [last word partially unclear, "垄断" best reading]. 论文: An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (ICLR 2021). Mini-diagram: patch grid.
- Right panel **核心突破**:
  - 统一架构
  - 预训练 + 微调范式
  - Scaling Law出现
  - 多模态融合开始

### Section 5 — Foundation Model时代 2021-2023 | 大模型爆发，能力涌现 (purple accent)

- 时代特征:
  - 模型规模指数级增长
  - 涌现能力出现
  - 多模态模型涌现
  - 应用生态爆发
- Cards:
  1. **2021 InstructGPT / OpenAI** — 指令微调 / 模型更可用. 论文: Training language models to follow instructions with human feedback (2022).
  2. **2022 RLHF / OpenAI** — 人类反馈强化学习 / 对齐人类价值. 论文: Deep Reinforcement Learning from Human Preferences (NeurIPS 2017) (应用于大模型对齐). [poster verbatim; note the poster itself cross-cites the 2017 paper]
  3. **2022 ChatGPT / OpenAI** — 对话式AI爆发 / 全球用户破亿. 产品: ChatGPT (2022.11发布).
  4. **2023 GPT-4 / OpenAI** — 多模态能力增强 / 更强推理能力. 论文/产品: GPT-4 (2023.3发布).
  5. **2023 Stable Diffusion / Stability AI** — 开源文生图模型 / AIGC 爆发. 产品: Stable Diffusion (2022.8发布).
  6. **2023 SAM / DINOv2 — Meta / Meta** — 分割 + 一切 / 视觉表征革命 / CV 大模型诞生. 论文: SAM (2023) DINOv2 (CVPR 2023).
- Right panel **时代意义**:
  - Foundation Model 成为新范式
  - AI 从单点能力走向通用能力
  - 生态与应用爆发

### Section 6 — Foundation AI时代 2024-Now | 走向通用智能与物理世界 (teal/dark accent)

- 时代特征:
  - 多模态深度融合
  - 世界模型兴起
  - 具身智能发展
  - 走向物理世界与AGI
- Cards:
  1. **2024 Qwen / DeepSeek — 通义千问 / 深度求索** — 开源大模型崛起 / 国产模型群崭露头角 [last line partially unclear, "崭露头角" best reading].
  2. **2024 Multimodal Models / 多模态大模型** — 图文音视频融合 / 统一多模态理解.
  3. **2024 World Model / V-JEPA2 / Cosmos** — 预测物理世界 / 从表示到生成.
  4. **2024 VLA / OpenVLA — Qwen-VLA / π0** — 视觉-语言-动作模型 / 连接感知与行动.
  5. **2024 Embodied AI / GROOT / Isaac** — 具身智能突破 / 机器人走向通用. [poster spells "GROOT"; NVIDIA's product is GR00T — keep poster spelling, note for k2]
  6. **2024+ AutoDriving / UniAD / End-to-End** — 端到端自动驾驶 / 迈向完全自动化.
- Right panel **未来趋势**:
  - 通用人工智能 (AGI)
  - 物理世界操作
  - 自主智能体 (Agent)
  - 人机共生未来

## 4. Bottom band(s)

### AI 技术发展主线 (main-line timeline, dark band with 6 glowing nodes + arrows)

`Rule Based AI (规则驱动)` → `Machine Learning (机器学习)` → `Deep Learning (深度学习)` → `Transformer (统一架构)` → `Foundation Model (基础模型)` → `Foundation AI (迈向通用智能)`

- 时间轴 row: `1950s | 1960s | 1970s-1980s | 1990s | 2010s | 2017 | 2020 | 2023 | 2026+`
- 核心驱动力 row (green/blue/purple chips, two lines each):
  1. 计算能力提升 / 从机械计算到电子计算
  2. 算法创新 / 从规则到学习
  3. 数据爆发 / 互联网+移动应用数据
  4. 深度学习突破 / GPU + 大数据
  5. 规模化定律 / Scaling Law
  6. 多模态融合 / 世界模型
  7. 自主智能体 / 物理世界交互

### 历史启示 row (4 chips + closing quote)

1. 智能涌现与突破 [first 1-2 characters uncertain — best reading "智能涌现与突破"]
2. 范式变革智能 [verify — possibly "范式变革智能"]
3. 规模是突破智能的关键
4. 跨领域融合产生新物种

Closing quote (large white text): **未来已来，唯变不变。**

### NEXT teaser (right side, yellow "NEXT" label)

- **Vol.02 Transformer 帝国**
- 技术架构、架构演化与模型家族全图谱
- Glowing blue cube illustration + `>>>` chevrons.

## 5. Graph content (nodes & edges for knowledge graph)

### Nodes

| id | zh label | en label | year | kind |
|----|----------|----------|------|------|
| turing_test | 图灵测试 | Turing Test | 1950 | milestone |
| dartmouth_conference | 达特茅斯会议 | Dartmouth Conference | 1956 | milestone |
| eliza | ELIZA 聊天机器人 | ELIZA | 1966 | model |
| expert_systems | 专家系统 | Expert Systems | 1970 | model |
| ai_winter | 第一次AI寒冬 | AI Winter | 1980 | industry |
| backprop | 反向传播算法 | Backpropagation | 1989 | paper |
| statistical_learning | 统计学习 | Statistical Learning | 1990 | concept |
| svm | 支持向量机 | SVM | 1995 | model |
| cnn_lenet | 卷积神经网络 (LeCun) | CNN / LeNet | 1998 | model |
| lstm | 长短期记忆网络 | LSTM | 2001 | model |
| dl_revival | 深度学习复兴 | Deep Learning Revival | 2008 | milestone |
| google_brain | Google Brain 深度神经网络 | Google Brain | 2011 | industry |
| alexnet | AlexNet | AlexNet | 2012 | model |
| word2vec | Word2Vec | Word2Vec | 2013 | model |
| seq2seq | 序列到序列模型 | Seq2Seq | 2014 | model |
| resnet | 残差网络 | ResNet | 2015 | model |
| attention_bahdanau | 注意力机制 | Attention (Bahdanau) | 2015 | paper |
| alphago | AlphaGo | AlphaGo | 2016 | milestone |
| transformer | Transformer | Transformer | 2017 | paper |
| bert | BERT | BERT | 2018 | model |
| gpt2 | GPT-2 | GPT-2 | 2019 | model |
| t5 | T5 | T5 | 2019 | model |
| gpt3 | GPT-3 | GPT-3 | 2020 | model |
| vit | Vision Transformer | ViT | 2020 | model |
| instructgpt | InstructGPT | InstructGPT | 2021 | model |
| rlhf | 人类反馈强化学习 | RLHF | 2022 | concept |
| chatgpt | ChatGPT | ChatGPT | 2022 | industry |
| gpt4 | GPT-4 | GPT-4 | 2023 | model |
| stable_diffusion | Stable Diffusion | Stable Diffusion | 2023 | model |
| sam | 分割一切模型 | SAM | 2023 | model |
| dinov2 | DINOv2 | DINOv2 | 2023 | model |
| qwen | 通义千问 | Qwen | 2024 | model |
| deepseek | 深度求索 DeepSeek | DeepSeek | 2024 | model |
| multimodal_models | 多模态大模型 | Multimodal Models | 2024 | concept |
| world_model | 世界模型 (V-JEPA2 / Cosmos) | World Model | 2024 | concept |
| vla_openvla | 视觉-语言-动作模型 | VLA / OpenVLA | 2024 | model |
| embodied_ai | 具身智能 (GROOT / Isaac) | Embodied AI | 2024 | concept |
| autodriving_uniad | 端到端自动驾驶 | UniAD / End-to-End | 2024 | industry |

### Edges (relation semantics per docs/AI圣经_修订版.md)

- backprop → cnn_lenet (inherits) ; backprop → lstm (inherits)
- statistical_learning → svm (inherits)
- cnn_lenet → alexnet (inherits) ; lstm → seq2seq (inherits)
- seq2seq → attention_bahdanau (inherits) ; attention_bahdanau → transformer (inherits)
- cnn_lenet → resnet (inherits) ; alexnet → resnet (inherits)
- word2vec → transformer (converges) [both feed representation learning; not a direct descendant]
- transformer → bert (inherits) ; transformer → gpt2 (inherits) ; transformer → t5 (inherits) ; transformer → vit (inherits)
- gpt2 → gpt3 (inherits) ; gpt3 → instructgpt (inherits) ; instructgpt → chatgpt (inherits) ; chatgpt → gpt4 (inherits) [poster implies the GPT lineage]
- gpt3 → rlhf (composes) [RLHF applied on top of LLM for alignment]
- rlhf → instructgpt (composes)
- bert ↔ roberta-style 趋同 not present on this poster (no RoBERTa card); skip
- resnet + transformer → stable_diffusion (composes) [latent diffusion uses U-Net conv + attention; poster places SD in the same era band]
- vit → sam (inherits) ; vit → dinov2 (converges) [DINO line is self-supervised ViT, parallel development]
- transformer → qwen (inherits) ; transformer → deepseek (inherits) [decoder-only LLM line]
- gpt4 → multimodal_models (inherits)
- transformer → vla_openvla (composes) [VLA = vision encoder + LLM + action head]
- multimodal_models → world_model (converges) ; world_model → embodied_ai (converges) ; vla_openvla → embodied_ai (composes)
- transformer → autodriving_uniad (composes) [end-to-end driving stacks use transformer backbones]
- Era main-line chain (bottom band, "inherits"-like solid arrows): Rule Based AI → Machine Learning → Deep Learning → Transformer → Foundation Model → Foundation AI

## 6. Style notes

- Background: very dark navy/near-black; era bands are alternating deep-tinted panels (blue / green / orange-red / blue / purple / teal) with a colored number chip and a colored era title.
- Cards: dark panels with a light "polaroid" image area (white-framed mini photo/diagram), colored year text, bold zh title + smaller en subtitle, 2 lines of zh description, and a small 论文: citation line.
- Left column 时代特征 and right column panels (为什么失败? / 关键推动力 / 革命意义 / 核心突破 / 时代意义 / 未来趋势) are bullet lists with small colored dot markers.
- Typography: heavy bold zh sans for titles; era titles colored per band; year chips colored; description text small (~10-12 px at 1024 width) in light gray/white.
- Bottom band: neon-glow nodes (blue/green/purple gradients) connected by arrows on a dark band; 时间轴 / 核心驱动力 rows as small pill chips; final quote 未来已来，唯变不变。 in large white text; NEXT teaser box with yellow "NEXT" label, yellow Vol.02 title, and a glowing cube illustration.
- Overall look: "AI Technology Bible" series chrome — same dark theme as vol02/vol03 posters, but each era band has its own accent color.
