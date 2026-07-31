# Vol.08 具身智能 / Embodied AI

- Source image: `assets/reference/volumes/8.具身智能.png`
- Declared volume number in header: **Vol.08** (matches filename number 8 — no discrepancy)
- Aspect: portrait 2:3 (1024×1536 reference)
- Theme note: light background; sections **numbered 1–13** with circled numerals (like Vol.07).

## 1. Header

- Left badge: dark navy `Modern AI Atlas` + pill `Vol.08`.
- Title (zh): **具身智能**
- Subtitle (en): **Embodied AI** (indigo)
- Tagline (zh): **让智能体拥有身体，感知世界，理解世界，改变世界**
- Top-right quote box:
  > 具身智能的本质，是智能与物理世界的深度融合，让AI不仅会思考，更能行动。
  > — Yann LeCun
- Far-right header illustration: silver humanoid robot in front of a holographic UI.

## 2. Legend row

No legend panel on this poster (no top row, no bottom 图例).

## 3. Sections (in top-to-bottom order)

### ① 具身智能发展时间线 (Timeline)

8 era columns above a navy axis; illustrations below each era (robot arm, mobile robot, drone point-cloud, humanoid sequence, human-robot imitation sketch, RT-1 transformer diagram labeled `RT-1`, OpenVLA / RT-2 / π0 logos, humanoid).

| Era | Years | Bullets |
|-----|-------|---------|
| 机器人学起源 | 1950s–1980s | 早期机器人研究 / 伺服控制与反馈 / 机器手与移动机器人 |
| 传统机器人 | 1990s–2000s | SLAM 与导航 / 视觉与感知算法 / 机器人操作系统 (ROS) |
| 深度学习进入感知 | 2010–2012 | 深度学习突破视觉 / 3D 感知与语义理解 / 大规模数据集出现 |
| 强化学习驱动控制 | 2013–2016 | Deep RL 用于控制 / 端到端学习尝试 / Sim2Real 概念提出 |
| 模仿学习与数据驱动 | 2017–2019 | Imitation Learning / 行为克隆 (BC)、GAIL / 大规模示范数据集 |
| 大模型与多模态融合 | 2020–2022 | Vision-Language / 预训练模型迁移到机器人 / RT-1 等统一模型出现 |
| 通用具身智能崛起 | 2023–2024 | RT-2, OpenVLA, π0 / 大规模多模态数据 / 世界模型 + VLA |
| 通用物理智能 | 2025+ 未来 | 世界模型驱动 / 长程任务规划 / 自主学习与进化 |

### ② 具身智能系统架构 (Embodied AI System Architecture)

Four-layer block diagram with left→right arrows:

- 感知层 Perception — items: 视觉 Vision · 听觉 Audio · 触觉 Touch · 力觉 Force · 惯导 IMU · 激光雷达 LiDAR · 位置 GPS / UWB · 编码器 Encoder · 其他传感器
- 认知层（大脑） Cognition (Brain) — blocks: 多模态理解 VLM / VLA · 世界模型 World Model · 任务规划 Task Planning · 决策推理 Reasoning
- (middle column of cognition sub-blocks): 运动控制 Motion Control · 操作控制 Manipulation · 导航控制 Navigation · 交互控制 Interaction
- 身体层 Body — blocks: 移动能力 Locomotion · 操作能力 Manipulation · 交互能力 Interaction

### ③ 具身智能技术栈 (Technology Stack)

Two-column table (capability chip | concrete techniques):

| 能力 | 技术 |
|------|------|
| 语言理解 Language | LLM, Instruction Following, Tool Use |
| 视觉理解 Vision | CNN, ViT, DINO, SAM, Depth Estimation |
| 多模态理解 Multimodal | CLIP, SigLIP, Qwen-VL, LLaVA |
| 世界模型 World Model | JEPA, Dreamer, Video Gen, Diffusion |
| 决策与规划 Planning | Task Decomposition, HTN, MCTS, POMDP |
| 控制与执行 Control | Motion Planning, MPC, PID, RL Control |
| 数据与训练 Data & Training | Simulation, Real Data, Imitation, RLHF |
| 部署与落地 Deployment | ROS2, Isaac Sim, Real Robot, Edge AI |

### ④ 具身智能感知系统 (Perception System)

Grid of 12 sensor cards (photo/icon + zh + en):

RGB 相机 Camera · 深度相机 Depth · 激光雷达 LiDAR · IMU / 惯导 IMU · 触觉传感器 Touch · 力/力矩传感器 Force / Torque · 麦克风阵列 Audio · 热成像相机 Thermal · GPS / 定位 · 编码器 Encoder · 温湿度 / 环境 Environment · 其他传感器

### ⑤ 具身智能"大脑"模型 (Embodied Brain Models)

Left: pipeline stack 指令输入 Instruction → 大语言模型 LLM → 视觉-语言模型 VLM → 具身智能模型 VLA (Vision-Language-Action) → 世界模型 World Model → 规划器 Planner → 控制器 Controller → 动作输出 Action Output.

Right: 代表模型 list (logo + name + zh desc):

- RT-1 (Google, 2022) — 首个视觉-语言-动作统一模型
- RT-2 (Google, 2023) — 大规模多模态数据训练 + VLA
- OpenVLA (2023) — 开源视觉-语言-动作模型
- π0 (Physical Intelligence, 2024) — 通用机器人基础模型
- GROOT (NVIDIA, 2024) — 通用人形机器人基础模型
- Qwen-VLA (阿里, 2024) — 通义视觉-语言-动作模型
- EmbodiedGPT (MS, 2023) — 具身智能与大语言模型结合
- Gemini Robotics (Google) — 多模态 + 推理 + 规划

### ⑥ 具身智能载体形态 (Embodiment Forms)

6 embodiment cards (photo + zh + en): 移动机器人 Mobile Robot · 四足机器人 Quadruped · 人形机器人 Humanoid · 机械臂 Manipulator · 空中机器人 Aerial Robot · 特种机器人 Special Robot

Below: 核心能力 (Core Capabilities) — 6 icon chips: 导航移动 Navigation · 物体操作 Manipulation · 抓取操作 Grasping · 工具使用 Tool Use · 人机交互 Human Interaction · 环境适应 Environment Adaptation

### ⑦ 具身智能数据与训练 (Data & Training)

Three groups:

- 数据来源: 真实机器人数据 Real Robot Data · 遥操作数据 Teleoperation Data · 仿真数据 Simulation Data · 互联网数据 Internet Data
- 训练范式: 模仿学习 (BC) · 强化学习 (RL) · 离线强化学习 (Offline RL) · 自监督学习 (SSL) · 多任务联合学习 (MTL)
- Sim2Real: 域随机化 Domain Randomization · 风格迁移 Style Transfer · 世界模型 World Model · 课程式学习 Curriculum Learning

### ⑧ 当前存在的挑战 (Challenges)

10 red icon items (two columns):

长程任务规划与泛化能力不足 · 复杂环境感知与理解仍不完备 · 通用操作能力不足、灵巧操作困难 · Sim2Real Gap 依然明显 · 高质量数据集严重不足 · 安全性与可靠性挑战 · 能耗与硬件限制 · 模型可解释性与可控性不足 · 伦理与社会影响 · 高昂研发成本、商业化落地困难

### ⑨ 未来趋势 (Future Trends)

7 green icon items (with a translucent humanoid graphic on the right):

通用具身基础模型 (Embodied Foundation Model) · 世界模型驱动的自主智能体 (World Model + Agent) · 大规模多模态数据与自监督学习 · 人机协作与具身智能社会化 · 更强的跨场景泛化能力 · 更高效的训练与推理 (边缘 + 云协同) · 走向通用物理智能 (General Physical Intelligence)

### ⑩ 代表性公司与机构 (Companies & Labs)

Logo grid: NVIDIA · Google DeepMind · OpenAI · TESLA · FIGURE · Physical Intelligence · Agility Robotics · Boston Dynamics · UNITREE · Fourier · EngineAI · 智元机器人 (Zhiyuan) · 银河通用 (Galaxy) · 普渡科技 (Pudu) · 优必选 (UBTECH) — footnote: 更多公司持续加入中…

### ⑪ 关键数据集 (Key Datasets)

List (with 3 small robot-setup photos on the right):

RT-1 Dataset (Google) · Open X-Embodiment · Bridge Data (Google) · RoboNet · ALOHA Dataset · Ego4D · DROID Dataset · RH20T Dataset · CALVIN Dataset

### ⑫ 技术路线演化 (Evolutionary Roadmap)

Horizontal chain of 9 icon nodes with arrows:

基于规则 Rule-based → 经典机器人 Classical Robotics → SLAM 与导航 SLAM & Navigation → 深度学习 Deep Learning → 深度强化学习 Deep RL → 视觉-语言 Vision-Language → VLA 模型 VLA Model → 世界模型 World Model → 通用具身智能 General Embodied AI

Below, a capability arrow strip: 能力持续提升： 感知 → 理解 → 推理 → 规划 → 行动 → 自主进化

### ⑬ 学习路线 (Learning Roadmap)

8-step horizontal arrow flow (step title + small desc):

1. 基础知识 — 数学、编程、控制、机器人学
2. 感知基础 — 计算机视觉、传感器融合
3. 学习方法 — 机器学习、深度学习
4. 强化学习 — RL 理论与算法
5. 多模态与大模型 — VLM、世界模型、VLA
6. 机器人实践 — ROS、仿真、硬件开发
7. 项目实践 — 数据采集、训练、部署
8. 持续迭代 — 优化、评估、创新

## 4. Bottom band(s)

- Dark navy gradient banner (brain hologram + humanoid robot), bilingual quote:
  > 具身智能是AI的下一个前沿：让智能体拥有身体，感知世界，理解世界，改变世界。
  > Embodied AI is the next frontier of AI: Empowering intelligence with a body to perceive, understand, and change the physical world.
- No NEXT Vol.XX teaser, no summary stats row.

## 5. Graph content (for knowledge graph nodes/edges)

### Nodes

| id | zh label | en label | year | kind |
|----|----------|----------|------|------|
| ros | 机器人操作系统 | ROS | 2007 | industry |
| slam | 同步定位与建图 | SLAM | 1995 | concept |
| sim2real | 仿真到现实 | Sim2Real | 2016 | concept |
| behavior_cloning | 行为克隆 | Behavior Cloning (BC) | 2017 | concept |
| gail | 生成对抗模仿学习 | GAIL | 2016 | paper |
| rt_1 | RT-1 | RT-1 (Robotics Transformer) | 2022 | milestone |
| rt_2 | RT-2 | RT-2 (VLA) | 2023 | milestone |
| openvla | OpenVLA | OpenVLA | 2023 | model |
| pi_0 | π0 | π0 (Physical Intelligence) | 2024 | milestone |
| groot | GROOT | GROOT (NVIDIA) | 2024 | model |
| qwen_vla | Qwen-VLA | Qwen-VLA | 2024 | model |
| embodiedgpt | EmbodiedGPT | EmbodiedGPT | 2023 | model |
| gemini_robotics | Gemini Robotics | Gemini Robotics | 2024 | model |
| vla | 视觉-语言-动作模型 | VLA (Vision-Language-Action) | 2023 | concept |
| world_model | 世界模型 | World Model | 2024 | concept |
| dreamer | Dreamer | Dreamer | 2020 | model |
| jepa | JEPA | JEPA (Meta) | 2023 | concept |
| open_x_embodiment | Open X-Embodiment | Open X-Embodiment | 2023 | paper |
| bridge_data | Bridge Data | Bridge Data | 2022 | paper |
| droid | DROID | DROID Dataset | 2024 | paper |
| aloha | ALOHA | ALOHA (斯坦福双臂平台) | 2023 | industry |
| mobile_aloha | Mobile ALOHA | Mobile ALOHA | 2024 | industry |

### Suggested edges

- `rt_1 → rt_2` — **inherits** (same Google Robotics Transformer line)
- `rt_2 → openvla` — **converges** (OpenVLA is the open-source parallel of RT-2, built on Prismatic VLM — do not draw as direct descent)
- `clip → vla` — **composes** (VLA = vision-language representations + action head; cross-volume edge to Vol.04/07 CLIP)
- `vlm → rt_2` — **composes** (RT-2 co-fine-tunes a VLM on robot data)
- `rt_2 ↔ pi_0` — **converges** (parallel generalist-robot policies; π0 uses flow-matching action expert)
- `pi_0 ↔ groot` — **converges** (parallel 2024 generalist robot foundation models)
- `gemini → gemini_robotics` — **inherits** (same Google model line; cross-volume)
- `llm → embodiedgpt` — **composes** (LLM + embodiment, per poster wording)
- `gail → behavior_cloning` — **converges** (parallel imitation-learning routes; note GAIL (2016) predates the poster's BC placement)
- `world_model → dreamer` — **inherits** (Dreamer is the canonical world-model RL line)
- `jepa ↔ world_model` — **converges** (explicit AI圣经 rule: JEPA route is independent; relations like V-JEPA → Cosmos are 趋同 not 继承)
- `mcts → planning_stack` — n/a (concept reuse; optional, omit)
- Data dependencies (`open_x_embodiment → openvla`, `bridge_data → rt_1`) — outside the {inherits, converges, composes} vocabulary; record as `composes` only if k2 wants dataset nodes, otherwise keep in extras.

## 6. Style notes

- Same light theme as Vol.04–07; sections numbered 1–13 with circled navy numerals (Vol.07/08 share this denser numbered-grid look).
- Architecture diagram (②) is a 4-layer left-to-right flow with white rounded blocks and indigo arrows; the 认知层 has two sub-columns of blocks.
- Technology stack (③) is a clean two-column table: left chips with icons, right plain-text technique lists.
- Perception system (④) uses actual product photos of sensors (cameras, LiDAR, IMU) — for the SVG version k2 should substitute flat icon glyphs.
- Embodiment forms (⑥) use robot photos; 代表模型 (⑤) use brand logos (Google "G", NVIDIA, Physical Intelligence π, Qwen).
- Challenges (⑧) red icons; future trends (⑨) green icons with a faint humanoid watermark image at right.
- Evolutionary roadmap (⑫) nodes are small circular icons linked by arrows; the 能力持续提升 strip is a rounded bar with arrow-separated capability words.
- Bottom banner: dark navy gradient, holographic brain + humanoid, bilingual quote (zh white, en light blue).
