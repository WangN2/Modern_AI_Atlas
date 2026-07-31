# 《AI 技术圣经》修订方案

> **目标不变**：一套能持续使用多年的 AI 知识地图，读完任何论文都能快速定位它在体系中的位置。
> **修订重点**：修正分类层级混乱、继承关系硬伤、路径依赖问题。
> **对齐基准**：与项目实际 14 卷结构（atlas/vol01–vol13 + vol01b）严格一致。

---

## 一、分类体系：四层金字塔（概念框架）

原方案把架构（Diffusion）、训练范式（RL）、应用领域（自动驾驶）、独立学科（SLAM）并列——维度不统一。修正为严格分层：

```
                          ┌─────────────┐
                          │   Layer 4   │  应用与落地
                          │  Auto/RL/   │  自动驾驶·机器人·Agent·AI系统
                          │  Embodied   │
                          └──────┬──────┘
                                 │
                    ┌────────────┴────────────┐
                    │        Layer 3         │  能力层
                    │   World Model · VLA    │  预测、规划、行动
                    │   Planning · Action    │
                    └────────────┬────────────┘
                                 │
              ┌──────────────────┴──────────────────┐
              │              Layer 2                │  多模态融合
              │  CLIP · LLaVA · InternVL · Qwen-VL │  图文音视频统一
              │  Multimodal Foundation Models      │
              └──────────────────┬──────────────────┘
                                 │
    ┌────────────┬───────────────┼───────────────┬────────────┐
    │            │               │               │            │
    ▼            ▼               ▼               ▼            ▼
 NLP           CV           Generation         RL           Audio
 GPT/BERT    ViT/DINO     Diffusion/DiT     PPO/SAC      Whisper
 (Decoder)   (Encoder)    (Encoder)        (Paradigm)   (Encoder-Dec)

                          Layer 1：基础架构
                          Transformer 作为统一的计算范式
```

**关键规则**：下层可以组合成上层。同一层内才有"继承"关系可以比较，跨层不叫继承，叫"组合使用"。

**各卷在四层金字塔中的位置**：

| 卷 | 名称 | 所属层级 | 定位 |
|-----|------|---------|------|
| 01 | AI 编年史 | 全层 | 纵览：从 1950 到 2026，六个时代的全景时间线 |
| 01b | 人工智能基础 | 全层 | 概念底座：核心概念、学科分支、能力层次、关键人物 |
| 02 | Transformer 帝国 | Layer 1 | 基础架构的统治范式：Encoder/Decoder/Enc-Dec 三大分支 |
| 03 | 大语言模型时代 | Layer 1→2 | LLM 的 Scaling、推理、对齐、工具使用全栈 |
| 04 | 多模态 AI | Layer 2 | 图文音视频统一的四种架构范式 |
| 05 | 生成式 AI | Layer 1 | 扩散/Flow/自回归三条生成路线的完整谱系 |
| 06 | 强化学习 | Layer 4 | 从 DQN 到 RLHF 到 GRPO 的训练范式演进 |
| 07 | 计算机视觉 | Layer 1 | CNN→ViT→自监督→密集预测的 CV 全路线 |
| 08 | 具身智能 | Layer 4 | 感知→规划→控制→执行的机器人全栈 |
| 09 | 自动驾驶 | Layer 4 | 最大单一应用领域：感知→预测→规划→控制 |
| 10 | 世界模型 | Layer 3 | 生成式 vs 判别式 vs 混合式的路线之争 |
| 11 | AI Agents | Layer 4 | Memory/Planning/Tool Use/Multi-Agent 四件套 |
| 12 | AI 系统 | Layer 4 | GPU 算力+训练框架+推理优化+分布式系统 |
| 13 | 迈向 AGI | 全层 | 五种 AGI 路线、能力阶梯、十年预测、生态全景 |

---

## 二、卷结构详解（严格按项目实际顺序）

### Vol.01：AI 编年史（1950-2026）

叙事定位：**纵览全貌**。按六个时代组织——从符号主义到 Foundation AI。读者拿到这卷就能建立全局时间感。

```
六个时代：

  1. AI 萌芽时代（1950-1989）
     图灵测试(1950) → 达特茅斯会议(1956) → ELIZA(1966)
     → 专家系统(1970s) → AI Winter(1980s) → Backprop(1989)
     标志：符号主义从兴起到衰落

  2. 机器学习时代（1990-2011）
     SVM → CNN萌芽(LeNet) → Boosting → Random Forest
     → ImageNet(2009) → 统计学习主导
     标志：从规则到数据驱动

  3. 深度学习革命（2012-2016）
     AlexNet(2012) → GAN(2014) → AlphaGo(2016) → ResNet
     标志：GPU 改变一切，深度学习成为主流

  4. Transformer 时代（2017-2019）
     Attention Is All You Need(2017) → BERT(2018) → GPT-1→GPT-2
     标志：NLP 范式统一，预训练成为标配

  5. Foundation Model 时代（2020-2023）
     GPT-3(2020) → ViT(2020) → CLIP(2021) → ChatGPT(2022)
     → Stable Diffusion(2022) → GPT-4(2023) → LLaMA(2023)
     标志：Scaling Law + 涌现能力 + 多模态融合

  6. Foundation AI 时代（2024-2026）
     Sora(2024) → o1→o3(推理增强) → DeepSeek-R1(开源推理)
     → π0(具身VLA) → Gemini 2.5 → Qwen3
     标志：推理、具身、Agent 三线并进
```

---

### Vol.01b：人工智能基础

叙事定位：**概念底座**。不按时间线，按概念结构组织——核心概念轮盘、学科地图、能力金字塔、范式演进、关键人物。

```
六个板块：

  1. AI 思想发展时间线（里程碑 Milestones）
     1956 达特茅斯 → 1960s 搜索推理 → 1970s 知识表示
     → 1980s 机器学习起步 → 1990s 神经网络复兴
     → 2000s 大数据 → 2010s 深度学习突破 → 2020s 大模型时代

  2. AI 核心概念轮盘（Core Concepts Wheel）
     感知(Perception) + 学习(Learning) + 推理(Reasoning)
     + 知识表示(Knowledge) + 行动(Action)
     └─ 外围：Agent 条带（感知环境→理解→推理→行动→反馈）

  3. AI 学科分支地图（Discipline Map，8 学科放射状）
     计算机科学 ⊙ 数学 ⊙ 统计学 ⊙ 神经科学
     ⊙ 认知科学 ⊙ 语言学 ⊙ 哲学 ⊙ 控制论
     └─ 汇聚于中心"人工智能"

  4. AI 能力层次金字塔（Capability Hierarchy）
     底部（基础能力）→ 顶端（高阶能力）：
     感知 → 理解 → 推理 → 决策 → 创造
     └─ 绿色底座 → 橙色/红色顶端

  5. 关键人物（Key Figures）
     Turing, McCarthy, Minsky, Hinton, LeCun, Bengio,
     Schmidhuber, Sutskever, Vaswani, He Kaiming...

  6. 基础理论支撑 + 推动因素
     信息论、计算理论、概率图模型、优化理论
     + 大数据、GPU 算力、开源生态、资本投入
```

---

### Vol.02：Transformer 帝国

叙事定位：**"一切模型皆可 Transformer"**。只画以 Transformer 为骨架的模型分化。

```
                        Transformer (2017, Vaswani et al.)
                        "Attention Is All You Need"
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
    Encoder 架构         Encoder-Decoder      Decoder 架构
    (双向注意力)           (Seq2Seq)          (因果注意力)
          │                   │                   │
    ┌─────┴──────┐      ┌────┴────┐        ┌─────┴──────┐
    BERT        ViT     T5      BART      GPT-1 → GPT-2
    (2018)     (2020)  (2019)  (2019)     → GPT-3 → GPT-4
    │           │       │                   (2020→2023)
    RoBERTa    MAE     Flan-T5          ┌───┼───┐
    DeBERTa    DINO    (2022)           │   │   │
    │           DINOv2               LLaMA DeepSeek Qwen
    ModernBERT SAM                   (Meta) (幻方) (阿里)
    (2024)     BEVFormer              LLaMA2→3→4  DeepSeek-V2→V3→R1
```

```
五大板块：

  1. 为什么是 Transformer? + Hero 展示 + 关键奠基论文
     └─ 并行计算、全局注意力、打破 RNN 顺序依赖

  2. 三大架构分支 + Attention 通用模块 + 架构变体
     Encoder 家族: BERT → RoBERTa → DeBERTa → ModernBERT
     Decoder 家族: GPT-1→2→3→4, LLaMA, DeepSeek, Qwen, Mistral
     Enc-Dec 家族: T5 → BART → Flan-T5
     Attention 模块: MHA → MQA → GQA → FlashAttention → MLA
     架构变体: ViT, Swin, BEVFormer（Transformer 进入 CV/自动驾驶）

  3. 跨领域融合（Fusion Band）
     六大模态（文本/图像/视频/语音/3D/时间序列）→ 统一 Transformer 表示空间
     └─ 核心标签：统一的 Transformer 表示空间

  4. 关键技术创新时间线（8 个节点）
     RoPE, FlashAttention, GQA, MoE, 长上下文...

  5. 产业影响 + Transformer 如何改变 AI 世界 + 未来演进
```

```
关系符号约定：
  → 实线：直接继承（同一路线、论文明确引用前作）
  ↗ 虚线：趋同/受启发但独立发展
  ＋ 点线：组合/拼接使用
```

**关键区分示例**：

```
继承（直系后代）：
  GPT-1 → GPT-2 → GPT-3 → GPT-4  ✓ 同一团队、同一路线
  LLaMA → LLaMA2 → LLaMA3 → LLaMA4  ✓ Meta 持续迭代

趋同（独立发展到相似方向）：
  BERT ↔ RoBERTa  不同团队各自优化，关系是"竞争"
  ViT ↔ Swin      Swin 用滑动窗口+层级结构，和 ViT 全局注意力不同路线
  LLaMA ↔ DeepSeek  两支独立团队，都从 GPT 分叉，互不继承

组合（跨层使用）：
  CLIP = ViT（视觉Encoder）+ GPT 风格（文本Encoder）+ 对比损失
  LLaVA = CLIP-ViT（视觉Encoder）+ LLaMA（语言Decoder）+ 投影层
```

---

### Vol.03：大语言模型时代

叙事定位：**LLM 的 Scaling、推理、对齐、工具使用的全栈故事**。

```
五大板块：

  1. LLM 发展时间线（11 卡片 + 火箭）
     2018 BERT/GPT-1 → 2019 GPT-2 → 2020 GPT-3(Scaling Law)
     → 2021 Chinchilla → 2022 ChatGPT/InstructGPT
     → 2023 GPT-4/LLaMA → 2024 LLaMA3/DeepSeek-V3/Qwen2.5
     → 2025 DeepSeek-R1/LLaMA4/Qwen3 → 2026 开源逼近闭源

  2. 模型家族树（3 Rails）
     GPT 系列: GPT-1→2→3→4→4o
     LLaMA 系列: LLaMA→2→3→4
     DeepSeek 系列: V2→V3→R1
     Qwen 系列: Qwen→2→2.5→3
     其他: Mistral, Gemma, Phi, Command R

  3. 核心能力栈
     Decoder-only 架构栈（Embedding→Attention→FFN→LM Head）
     Next-token 预测表
     SFT → RM → RLHF 训练流程
     6 个涌现能力芯片
     Scaling 3 卡（Kaplan Law + Chinchilla Law + 实际趋势）
     S-Curve 含各阶段标注

  4. 应用与风险
     6 个应用领域卡片
     5 层技术栈行
     6 个风险卡片（幻觉、安全、偏见...）

  5. 基础支撑 + 未来展望
     5 项基础（算力、数据、算法、框架、人才）
     通往 AGI 的 6 个 Chevrons
```

**LLM 关键技术栈**：

```
1. Scaling Law (2020-2022)
   Kaplan et al. → Chinchilla Law → DeepSeek 极致成本

2. 长上下文
   RoPE → NTK-aware → YaRN → RingAttention → 2M tokens

3. 推理增强（Reasoning）
   CoT → Tree-of-Thought → o1(MCTS+PRM) → DeepSeek-R1(GRPO)

4. 对齐技术
   SFT → RLHF(PPO) → DPO → KTO → ORPO → GRPO

5. 工具使用
   Toolformer → Function Calling → MCP 协议

6. RAG
   Naive RAG → Advanced RAG → Graph RAG → Agentic RAG
```

**开源 LLM 生态格局（2025-2026）**：

| 系列 | 机构 | 最新 | 特点 |
|------|------|------|------|
| LLaMA | Meta | LLaMA 4 | 开源社区"Linux"，最大生态 |
| Qwen | 阿里 | Qwen3 | 国内最强开源，多模态覆盖最全 |
| DeepSeek | 幻方 | DeepSeek-R1 | MoE 架构创新，训练成本极低 |
| Mistral | Mistral AI | Mistral Large | 欧洲最强，MoE 路线先驱 |
| Gemma | Google | Gemma 3 | 基于 Gemini 技术，轻量化 |
| Phi | Microsoft | Phi-4 | "小模型大能力"路线 |

---

### Vol.04：多模态 AI

叙事定位：**从"两个模型的拼接"到"一个模型的统一"**。

```
九大板块：

  1. 多模态 AI 发展时代（6 列）
     单模态时代 → 视觉-语言 → 多模态融合 → 多模态生成
     → 统一多模态 → 具身多模态

  2. 多模态 AI 发展时间线（6 个里程碑节点）
     CLIP(2021) → Stable Diffusion(2022) → LLaVA(2023)
     → GPT-4V(2023) → Gemini(2024) → Qwen2-VL(2024)

  3. 模态列表 + 2×2 范式矩阵
     模态: 文本·图像·视频·音频·3D·触觉·代码

  4. 多模态模型演进路径（5 列）
     双塔对比 → 单塔融合 → 跨注意力桥接 → 原生多模态 → 全模态

  5. 理解与生成 Pills
     理解: 图文检索 / VQA / 视频理解 / OCR
     生成: 文生图 / 文生视频 / 文生3D / 图生文

  6. 技术基础 + 能力 Wheel
     对比学习、跨注意力、Token 统一、模态对齐

  7. 代表模型 + 应用
     7 个里程碑模型 + 12 个应用场景

  8. 数据集 + 挑战与机遇
     训练/评估数据集 + 幻觉/细粒度/推理/效率

  9. 趋势 + 生态
     6 个未来趋势 + 4 列生态（含公司/框架/数据集/模型）
```

**多模态融合的四条技术路线**：

```
1. 双塔对比（Dual-Encoder + Contrastive）
   CLIP → SigLIP → EVA-CLIP
   └─ 图文分离编码，效率高但细粒度差

2. 单塔融合（Single-Encoder Fusion）
   ViLT → FLAVA → CoCa
   └─ 早期融合，效果好但计算量大

3. 跨注意力桥接（Cross-Attention Bridge）
   LLaVA-1.5 → LLaVA-NeXT → LLaVA-OneVision
   InternVL → InternVL2
   └─ 视觉 Encoder + LLM，中间加投影/对齐层（当前主流）

4. 原生多模态（Early Fusion + Next-Token）
   Gemini → Chameleon → Emu3 → Qwen2-VL
   └─ 图文交错训练，统一 token 空间（下一代方向）
```

**跨注意力桥接 vs 原生多模态**：
- 桥接式（LLaVA 系）：视觉 token 作为 cross-attention 输入，不参与自回归
- 原生式（Gemini 系）：视觉 token 和文本 token 一同进入自回归序列

---

### Vol.05：生成式 AI

叙事定位：**"U-Net 的规模瓶颈 → Transformer 替代 → 生成进入规模化时代"**。

```
五大板块：

  1. 生成式 AI 发展时间线（6 列 + 里程碑）
     GAN(2014) → VAE → DDPM(2020) → Stable Diffusion(2022)
     → DiT(2023) → Sora(2024) → Flux/Flow Matching(2024)

  2. 核心概念 + 模型类型
     6 个核心概念（潜空间/扩散/Flow/自回归/对抗/条件生成）
     6 种模型卡片（GAN/VAE/AR/Diffusion/Flow/Consistency）

  3. 生成过程 + 技术基础
     5 步生成流程
     5 项技术基础含示意图

  4. 架构迷你图
     Transformer / Encoder-Decoder / U-Net / Fusion

  5. 应用 + 数据集 + 评估 + 挑战 + 趋势 + 生态
     9 应用 tile + 8 行数据集表 + 4 评估指标组
     + 6 挑战 + 6 趋势 + 4 列生态
```

**扩散模型的完整演进**：

```
Sohl-Dickstein (2015, 原始扩散思想)
    │
DDPM (Ho et al. 2020) ── 奠基：正向加噪、反向去噪
    │
DDIM (Song et al. 2021) ── 去噪可跳步，加速采样
    │
Score-based SDE (Song et al. 2021) ── SDE/ODE 统一视角
    │
Classifier-Free Guidance (Ho & Salimans 2022) ── 当前标配
    │
Latent Diffusion (Rombach et al. 2022) ── 潜空间扩散，SD 基石
    │
    ├─ SDXL (U-Net 路线，2023)
    ├─ DiT (Peebles & Xie 2023) ── U-Net → Transformer
    │     ├─ PixArt (华为)
    │     ├─ SD3/MMDiT + Flow
    │     ├─ Flux (Black Forest Labs)
    │     ├─ Sora (OpenAI, 视频)
    │     └─ Cosmos (NVIDIA, World Model)
    │
    └─ Flow Matching (Lipman et al. 2023) ── 直线路径
          → Rectified Flow (Liu et al. 2023)
          → SiT (Ma et al. 2024, 扩散+Flow 统一)
```

```
生成模型的五条路线对比：

  路线        │ 代表         │ 原理        │ 优势          │ 劣势
  ────────────┼─────────────┼─────────────┼──────────────┼───────
  GAN         │ StyleGAN    │ 博弈生成     │ 推理快        │ 模式坍塌
  VAE         │ VQ-VAE      │ 变分推断     │ 潜空间好      │ 模糊
  AR          │ ImageGPT    │ 逐像素预测   │ 与LLM统一     │ 慢
  Diffusion   │ SD, DiT     │ 逐步去噪     │ 质量最高      │ 推理慢
  Flow        │ Flux, SD3   │ 直线路径     │ 推理快+质量高 │ 较新
```

---

### Vol.06：强化学习

叙事定位：**从 DQN 到 RLHF 到 GRPO——RL 从游戏走向对齐**。

```
五大板块：

  1. 强化学习发展时间线（6 列）
     DQN(2013) → A3C(2016) → PPO(2017) → SAC(2018)
     → RLHF(2022) → DPO(2023) → GRPO(2024)

  2. 核心要素 + RL 循环 + 范式
     9 个核心要素（State/Action/Reward/Policy/Value/Q-Function...）
     Agent → Action → Environment → Reward → Next State 循环
     4 种范式分类（Value/Policy/Actor-Critic/Model-Based）

  3. 理论基础
     MDP 五元组 (S, A, P, R, γ)
     Bellman 方程（期望 + 最优）
     价值函数与策略的关系（Value ↔ Policy Iteration）

  4. 算法对比 + 应用 + 问题设定
     6 行算法表（DQN/PPO/SAC/TD3/RLHF/GRPO）
     9 应用领域 + 7 问题设定
     挑战/未来 (5+5)

  5. 数据集/基准 + 学习路径
     Arcade Learning / MuJoCo / Gym / DM Control / RLHF 偏好数据
     5 步学习路线（基础 RL → 深度 RL → 策略梯度 → RLHF → 前沿）
```

```
RL 算法的演化树：

  Value-Based                 Policy-Based           Actor-Critic
      │                           │                      │
  DQN (2013)                  TRPO (2015)          A2C/A3C (2016)
  Double DQN                  PPO (2017)           SAC (2018)
  Rainbow (2017)                                   TD3 (2018)
      │                           │                      │
      └───────────────────────────┼──────────────────────┘
                                  │
                            Offline RL
                                  │
                        ┌─────────┴─────────┐
                        │                   │
                   RLHF (2022)          DPO (2023)
                   InstructGPT          直接偏好优化
                        │
                   GRPO (2024)
                   DeepSeek-R1
```

**注意**：RLHF 是 RL 在 LLM 对齐中的**应用**，不是 RL 的"下一代"——它同时继承了 Supervised Fine-tuning（SFT）的范式。正确画法：`RLHF = RL(PPO) ＋ SFT`。

**GRPO 的创新点**（DeepSeek-R1, 2025）：
- 不需要 Critic Model（价值网络），节省一半显存
- 组内相对比较（Group Relative）：同一 prompt 生成多个 response，好的加分、差的减分
- 用纯 RL 驱动推理能力涌现——"啊哈时刻"(Aha moment) 来自 RL 而非 SFT

---

### Vol.07：计算机视觉

叙事定位：**CV 的完整路线图——从 CNN 到 ViT 到自监督到密集预测**。

```
十大板块：

  1. 计算机视觉发展时间线（8 列）
     LeNet(1998) → AlexNet(2012) → ResNet(2015) → ViT(2020)
     → MAE(2022) → DINOv2(2023) → SAM(2023) → SAM 2(2024)

  2. 技术路线演化（4 阶段）
     手工特征 → CNN时代 → Transformer入侵 → Foundation Model时代

  3. 视觉技术全景图（4 层 Pills）
     任务层/架构层/方法层/应用层

  4. CNN 家族树（9 干 + 5 枝）
     LeNet → AlexNet → VGG → Inception → ResNet → DenseNet
     → MobileNet → EfficientNet → ConvNeXt

  5. ViT 家族（10 条目）
     ViT → DeiT → Swin → MAE → DINO → DINOv2 → SAM...

  6. 目标检测 + 分割 + 自监督路线（3×Pills）
     检测: R-CNN → YOLO → DETR → RT-DETR
     分割: FCN → U-Net → Mask R-CNN → SAM
     自监督: SimCLR → MoCo → BYOL → DINO → MAE → I-JEPA

  7. 应用 + 数据集 + 基准
     8 应用领域 + 10 行数据集表 + 8 行基准表

  8. 关键论文（11 篇）
  9. 公司与框架
  10. 未来趋势（7 项）
```

**视觉自监督学习的四条路线**：

```
1. 对比学习（Contrastive）
   SimCLR → MoCo v1/v2/v3 → CLIP
   └─ 拉近正样本对、推开负样本对

2. 掩码自编码（Masked Autoencoding）
   BEiT → MAE → SimMIM
   └─ 遮住 patch，让模型重建（CV 版 BERT）

3. 自蒸馏（Self-Distillation）
   BYOL → DINO → DINOv2
   └─ 无需负样本，teacher→student 自蒸馏

4. 特征正则化（Feature Regularization）
   Barlow Twins → VICReg
   └─ 对特征协方差矩阵施加正则化
```

**注意**：Swin Transformer 不应画成 ViT 的直接后代——Swin 用滑动窗口 + 层级结构，和 ViT 的全局注意力是不同技术路线，两者在 2020-2021 年是并行"竞争"关系。

---

### Vol.08：具身智能

叙事定位：**从传感器到执行器的完整闭环——"智能必须通过身体与世界交互"**。

```
11 个板块：

  1. 具身智能发展时间线（8 列 + 火箭）
  2. 具身智能系统架构（4 层）
     感知层 → 理解层 → 决策层 → 控制层
  3. 具身智能技术栈（8 行表格）
  4. 感知系统（12 传感器芯片）
     Camera, LiDAR, Radar, IMU, Tactile, Microphone, GPS...
  5. 大脑-模型流水线（8 阶段）+ 8 个代表模型
     RT-2 → OpenVLA → π0 → GR00T N1 → Qwen-VLA → ABot-N0
  6. 具身形态（6 种）+ 核心能力（6 种）
     人形/轮式/四足/双臂/无人机/协作臂
  7. 数据与训练（3 组）
     遥操作/仿真/真机; IL/RL/Sim-to-Real
  8. 挑战（10 项）+ 趋势（7 项）
  9. 公司/平台（15 家）
  10. 数据集（9 个）+ 路线图（9 节点）
  11. 学习路线（8 步）
```

**VLA（Vision-Language-Action）的三种范式**（具身智能的核心大脑）：

```
1. 端到端单一模型（Action as Token）
   代表：RT-2 (Google 2023), OpenVLA (Stanford 2024)
   思想：把机器人动作离散化为 token，LLM 直接预测
   ├─ 优势：极简架构
   └─ 劣势：高频控制（>10Hz）困难

2. 分层双系统（VLM as Brain + DiT as Muscle）
   代表：GR00T N1 (NVIDIA), Qwen-VLA (阿里), π0 (PI)
   思想：VLM 高层理解 + DiT 低层动作生成
   ├─ System 1 (VLM): 场景理解、语言指令
   └─ System 2 (DiT): 连续动作序列生成
   └─ 这是当前最重要的架构收敛趋势

3. 离散扩散折中
   代表：DDVLA (2025)
   思想：用离散扩散逐步去噪生成动作序列
```

**硬件生态（2025-2026）**：
- 人形：Tesla Optimus, Unitree G1/H1, Figure 02, 1X Neo, Fourier GR-2
- 仿真：Isaac Sim, MuJoCo, Genesis(10万倍实时), SAPIEN, Habitat

---

### Vol.09：自动驾驶

叙事定位：**最大单一 AI 应用领域——感知→预测→规划→控制的完整技术栈**。

```
十大板块：

  1. 自动驾驶发展时间线（7 列）
  2. 自动驾驶系统架构（6 传感器 + 5 流水线卡片）
  3. 技术路线演进（5 阶段）
     Rule-based → CNN感知 → BEV统一 → 端到端 → Foundation Model
  4. 感知技术全景（4 阶段）
     2D检测 → BEV感知 → 3D占用网络 → 3DGS感知
  5. 代表性算法与模型（5 列）
     BEVFormer, UniAD, VAD, StreamPETR, OccNet
  6. 主流公司与方案（10 卡片）
     Tesla/Waymo/华为/理想/小鹏/蔚来/Momenta/小米/Wayve
  7. 数据集 + 评估指标 + 基准
     10 数据集 + 5 指标组
  8. 当前挑战（7 项，红色）
  9. 未来趋势（6 项）+ 应用芯片（6 个）
  10. 学习路线（7 节点）
```

**各厂商路线（2025-2026，平行对比，不做继承线）**：

```
Tesla    FSD v12+    纯视觉端到端
Waymo    Wayformer   LiDAR+多模态
华为      ADS 3.0     多传感器融合+GOD网络
理想      端到端+VLM
小鹏      XNGP        纯视觉+端到端
蔚来      NAD         多Orin+端到端
Momenta   两段式      量产导向
小米      BeyondDrive 安全对齐
Wayve     GAIA-1/2    世界模型驱动
```

---

### Vol.10：世界模型

叙事定位：**"预测未来"——当前分裂最严重的领域，三条路线各执一词**。

```
八大板块：

  01 世界模型发展史（11 节点时间线）
  02 世界模型技术路线（8 芯片）
  03 世界模型系统架构
  04 四色家族树（A 绿/B 紫/C 红/D 褐红）
      生成式: Sora, Cosmos, Genie, CDiT (NWM)
      判别式: JEPA → I-JEPA → V-JEPA → V-JEPA2
      混合式: Dreamer → DreamerV2 → DreamerV3
      自动驾驶: GAIA-1/2, DriveDreamer
  05 范式对比表（4 行）
  06 代表模型 + 组织 + 挑战 + 应用 + 数据集
  07 学习路径 + 演进路线图
  08 世界模型全景（6 霓虹色列）+ 趋势（6 项）
```

**三条路线的核心分歧**：

```
1. 生成式（重建像素）
   代表：Sora, Cosmos, Genie
   优势：可视化、直观、视频生成自然
   劣势：计算量极大、重建细节浪费
   口号："看到未来，才能规划未来"

2. 判别式/能量式（预测隐状态，JEPA 系列）
   代表：I-JEPA, V-JEPA, V-JEPA2 (Meta, LeCun 路线)
   优势：效率高、聚焦语义、LeCun 认为这是通往 AGI 之路
   劣势：不可视化、评估困难
   口号："预测像素是浪费，预测表示才是智能"

3. 混合式（隐状态+行动→规划）
   代表：DreamerV3 (DeepMind)
   优势：直接产出行动策略、游戏/控制中验证有效
   劣势：隐状态不可解释、泛化存疑
```

**关键纠正**（原方案的错误）：
- 原方案：V-JEPA → V-JEPA2 → Cosmos ← 错误！
- 实际：V-JEPA 系列是 Meta 的判别式 JEPA 架构；Cosmos 是 NVIDIA 的生成式 DiT 架构。两者是**平行路线**，不是继承关系。
- 正确画法：JEPA → I-JEPA → V-JEPA → V-JEPA2（实线继承）；Sora ↗ Cosmos（虚线趋同）。

**LeCun vs 生成派的核心争论（2025）**：World Model 是否需要生成像素？目前尚无定论，混合方案（如 V-JEPA2 + Action Head）是近期折中方向。

---

### Vol.11：AI Agents

叙事定位：**从"Human in the Loop"到"Human on the Loop"——Agent 自主规划、执行、纠错**。

```
四大板块（11 个 Section）：

  01 AI Agent 核心能力（6 卫星 Hub，橙色 行动/反思 强调）
      感知 → 规划 → 记忆 → 工具 → 执行 → 反思

  02-04 工作流 + 工具 + MCP
      7 步工作流 + Memory 子面板 + Tools/Env Band
      7 工具芯片（搜索/代码/浏览器/API/数据库/文件/终端）
      MCP 流程 + Server 扇出（类比 USB 之于外设）

  05 记忆系统（3 Memory Cards）
      工作记忆 → 情景记忆 → 语义记忆
      MemGPT → Letta → 记忆分层架构

  06 规划与推理（6 Planning Cards）
      子目标分解 / 反思 / 多路搜索 / 辩论 / 自我纠错 / Plan+Execute

  07 多智能体协作（5 Multi-Agent 模式）
      流水线式 / 辩论式 / 投票式 / 层级式 / 角色扮演

  08 代表性框架/平台（8 框架芯片）
      LangChain / LlamaIndex / AutoGen / CrewAI / MetaGPT / CAMEL / LangGraph

  09 AI Agent 全景架构（5 列）
      含嵌套 Agent Brain 面板（Memory/Planning/Decision 子列表）

  10 当前挑战（10 项，红色）—— 幻觉/循环/安全/成本/评估
  11 未来趋势（9 项，青色）—— Agentic Workflow/MCP 标准化/多Agent协作
```

**Agent 的能力演进路线**：

```
阶段 1（2023）：单一 Agent + 工具
  ReAct → Toolformer → Gorilla

阶段 2（2023-2024）：多 Agent 协作
  AutoGPT → MetaGPT → ChatDev → AutoGen

阶段 3（2024）：Agent Framework 成熟
  LangChain → LlamaIndex → CrewAI → LangGraph（图编排替代线性链）

阶段 4（2024-2025）：Agentic Workflow
  自主规划→执行→验证→纠错，Human on the Loop
  代表：Devin, Claude Code, Cursor Agent, OpenAI Deep Research
```

---

### Vol.12：AI 系统

叙事定位：**"没有系统，就没有大模型"——从 GPU 到分布式训练到推理优化的完整基础设施**。

```
四大板块（10 个 Section）：

  01 计算底座
      9 代 GPU 列表 (TITAN→P100→V100→A100→H100→B200→GB200→Rubin)
      5 层计算栈（硬件/驱动/库/框架/应用）
      8 硬件组件（GPU/TPU/NPU/DPU/Interconnect/Memory/Storage/Network）

  02 并行计算与加速
      CUDA 面板 + Tensor Core 面板
      并行模式：数据并行 / 模型并行 / 张量并行 / 流水线并行 / 专家并行

  03 关键系统组件（5 卡片）
      PyTorch 2.x / DeepSpeed / Megatron-LM / vLLM / TensorRT-LLM

  04 大模型训练优化（12 卡片）
      Mixed Precision / Gradient Checkpointing / ZeRO 1-3
      / FlashAttention / 通信优化 / 数据加载优化
      / 激活重计算 / 序列并行 / PipeDream / FSDP

  05 推理优化（4+1）
      KV Cache 优化: PagedAttention / MLA / GQA
      量化: GPTQ / AWQ / GGUF / FP8/FP4
      投机解码: Medusa / EAGLE
      分布式推理: TP + PP + EP

  06 分布式系统与调度（5 卡片）
      Kubernetes + Volcano / Ray / SLURM / 云原生训练

  07 AI 系统全景图（7 层）
      硬件层→互联层→算子层→框架层→调度层→平台层→应用层

  08 评估与指标（8 芯片）
      MFU / 吞吐 / 延迟 / 显存 / 通信带宽 / TCO / 功耗 / 可用性

  09 未来趋势（6 项）
      Chiplet / 光互联 / 存内计算 / 绿色AI / 国产替代 / 边缘推理

  10 总结（深色摘要 Band）
      层级链 + 完整引用
```

---

### Vol.13：迈向 AGI

叙事定位：**"终点在哪？"——五种路线、能力阶梯、十年预测、生态全景**。

```
四大板块（8 个 Section）：

  01 发展回顾
      6 时代 Chevron 条带 + 10 里程碑（1969 Perceptron 起）
      3 行能力/规模趋势

  02 AGI 核心支柱
      8 支柱卡片 + 公式栏 + 安全条带
      Scaling / Reasoning / Memory / Tool Use / World Model
      / Embodiment / Multi-Agent / Alignment

  03 路线图
      未来十年预测（5 阶段，双语，2026→2035）
      AGI 路线图（5 阶段，阶段三高亮橙色）
      具身智能 + 世界模型闭环（4 节点循环）

  04 挑战 + 趋势 + 生态
      8 挑战卡片
      7 行生态全景图
      持续迭代条带
      总结（6 卫星芯片 + 完整引用）
```

**五种 AGI 路线**：

```
1. Scaling 派（OpenAI, Anthropic）
   └─ 更大模型 + 更多数据 + 更强算力 → AGI

2. 架构创新派（Meta, DeepSeek）
   └─ World Model + JEPA + 非生成式学习 → AGI
   └─ 代表：LeCun's "A Path Towards Autonomous Machine Intelligence"

3. Agent 派（Google DeepMind, Cognition AI）
   └─ LLM as Core + 工具使用 + 自主规划 → AGI

4. 具身派（NVIDIA, Physical Intelligence, Tesla）
   └─ 智能必须通过身体与世界交互 → AGI

5. 神经科学启发派（DeepMind, 少数派）
   └─ 从人脑逆向工程 → AGI
```

**AGI 能力阶梯**：

```
L0: 无 AI         —— 纯规则系统
L1: 初级推理      —— 模式匹配、简单分类
L2: 组合推理      —— 多步推理、工具使用（当前 SOTA 处在这一级）
L3: 自主规划      —— 长时间自主完成任务、自我纠错
L4: 创新与发现    —— 提出新假设、设计实验、发现新科学
L5: 通用智能      —— 在所有认知任务上达到或超越人类水平
```

---

## 三、关系语义规范（核心约束，不可违反）

### 3.1 三种基本关系

| 关系 | 英文 | 符号 | 线型 | 定义 |
|------|------|------|------|------|
| 直接继承 | inherits | `→` | 实线 | 同一路线、论文明确引用前作、架构连续性 |
| 趋同/受启发 | converges | `↗` | 虚线 (8-6) | 独立发展但思路相似、不同团队、并行竞争 |
| 组合/拼接 | composes | `＋` | 点线 (2-6) | 跨层使用、模块化拼接、多组件集成 |

### 3.2 关系判定决策树

```
A 和 B 之间是什么关系？

  ├─ 同一团队/机构？
  │   ├─ 是 → 论文写 "based on / extends A"？
  │   │   ├─ 是 → inherits（实线）
  │   │   └─ 否 → converges（虚线，团队内平行探索）
  │   └─ 否 → 继续
  │
  ├─ B 把 A 作为组件/模块使用？
  │   ├─ 是 → composes（点线）
  │   └─ 否 → 继续
  │
  ├─ 两者有共同技术来源 C，C→A 和 C→B 都是继承？
  │   ├─ 是 → converges（虚线，姐妹模型）
  │   └─ 否 → 继续
  │
  └─ 不确定 → 不画线（宁可漏画不可错画）
```

### 3.3 常见误判纠正清单

| 错误画法 | 正确画法 | 判断理由 |
|---------|---------|---------|
| BERT → GPT | BERT ↗ GPT | 2018 同时分叉，双向 vs 单向不同路线 |
| ViT → CLIP | CLIP = ViT ＋ GPT | CLIP 视觉用 ViT，对比框架来自独立路线 |
| CLIP → InternVL | CLIP ↗ InternVL | InternVL 自研视觉 backbone，对比思想趋同 |
| V-JEPA → Cosmos | V-JEPA ↗ Cosmos | 判别式 vs 生成式，不同机构不同路线 |
| RL → RLHF | RLHF = RL ＋ SFT | RLHF 同时继承 RL 和 SFT，跨层组合 |
| SD → DiT | SD ↗ DiT | 同领域但 U-Net→Transformer 换了核心架构 |
| GPT-4 → LLaMA | GPT-4 ↗ LLaMA | LLaMA 受启发但独立开发，架构细节不同 |
| RT-2 → π0 | RT-2 ↗ π0 | Action-as-Token vs Flow Matching，范式不同 |

**正确画成"继承"的关系**：

```
GPT-3 → GPT-4          同一团队、同一路线
LLaMA → LLaMA3 → LLaMA4  Meta 持续迭代
JEPA → V-JEPA → V-JEPA2  Meta 同一团队，连续演进
DINO → DINOv2            同一团队，明确续作
DeepSeek-V2 → V3 → R1    幻方同一团队，渐进演进
DDPM → Latent Diff → SD  生成范式连续演进
```

---

## 四、继承关系备注

GPT 原方案的"继承树"有美化历史之嫌——把独立发展且互有竞争的模型画成"一个生出一个"。真实技术史更乱也更精彩。

以下关系**不是继承**，应标注为"趋同"（虚线）：

| 原方案画法 | 实际关系 |
|-----------|---------|
| ViT → CLIP | CLIP 视觉用 ViT，但对比学习框架来自独立路线（SimCLR/MoCo）|
| V-JEPA → Cosmos | 完全不同架构、不同机构、不同路线 |
| BERT → GPT | 2018 年同时分叉的两条路线，GPT 不是 BERT 的后代 |
| CLIP → InternVL | InternVL 视觉 backbone 独立设计，非 CLIP 直系 |
| SD → DiT | 同领域但核心架构从 U-Net 换成了 Transformer |
| GPT-4 → LLaMA | LLaMA 独立开发，架构和训练细节均不同 |
| Sora → Cosmos | Cosmos 受 Sora 启发但独立开发，是竞争关系 |
| RT-2 → π0 | 架构范式不同（Action-as-Token vs Flow Matching）|

---

## 五、AGENTS.md / CLAUDE.md 需同步更新

本文档修订完成后，需同步更新以下项目文件：

1. **CLAUDE.md** — 13 卷列表需与本文档一致；四层金字塔作为概念框架补充
2. **AGENTS.md** — 关系语义（inherits/converges/composes）需与本文档 §三 对齐
3. **PROJECT_STATUS.md** — RFC-0002 知识 Schema 应包含本文档的四层分类和关系规范
