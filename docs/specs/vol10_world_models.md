# Vol.10 世界模型 / World Models

- Source image: `assets/reference/volumes/10.WorldModels.png`
- Declared volume number in header: **Vol.10** (matches filename number 10 — no discrepancy)
- Aspect: **landscape 3:2 (1536×1024 reference)** — filename batch was assumed portrait but this poster is actually landscape; flag to k2.

## 1. Header

- Badge (top-left): `Modern AI Atlas` + chip `Vol.10`
- Title (en+zh combined): World Models 世界模型
- Subtitle (en): Predict the World Before Acting
- Subtitle (zh): 让 AI 在行动之前，先学会理解和预测世界
- Top-right quote block:
  > 世界模型的目标，不是预测一个像素，而是理解一个世界，不是生成一个视频，而是推演未来的可能。— Yann LeCun
- Top-right artwork: humanoid robot reaching toward a glowing globe.

## 2. Legend row

No explicit edge-style legend. Section numbers use dark navy square badges (01–13). The Family Tree (04) color-codes families: A=green, B=purple, C=red/pink, D=dark red. The bottom "World Model Landscape" band uses per-column accent colors (green / purple / red / orange / teal / blue).

## 3. Sections (in top-to-bottom order)

### 01 世界模型发展史 (Timeline)
Horizontal 11-node timeline, each node: year chip + name + zh caption + small image:
1. **1980s Model-based Control** — 基于模型控制的短期阶段 [uncertain last char; reads 短期阶段]
2. **2000 Kalman Filter / Particle Filter** — 状态估计方法快速发展
3. **2013 Model Predictive Control (MPC)** — 模型预测控制广泛应用
4. **2017 PlaNet** — 学习隐空间动力学模型  *(poster dates PlaNet 2017; actual paper 2018 — transcribe as shown, flag)*
5. **2019 Dreamer** — 端到端学习世界模型
6. **2020 MuZero** — 无模型+模型融合突破
7. **2021 Decision Transformer** — 序列建模驱动决策
8. **2022 Video Prediction / JEPA** — 视频预测兴起，自监督表示突破
9. **2023 DreamerV3 / Genie** — 世界模型更强大，生成质量提升
10. **2024 Cosmos / Genie2 / OpenVLA WM / PI0 / GROOT** — 物理+生成+具身融合加速
11. **2025+ General World Model** — 通用世界模型，迈向 AGI

### 02 世界模型技术路线 (Technology Roadmap)
Eight arrow-linked icon chips:
Physics Model 物理模型 → Dynamic Model 动态模型 → Latent Dynamics 隐空间动力学 → Predictive Model 预测模型 → Video Generation 视频生成 → Generative World Model 生成式世界模型 → Embodied World Model 具身世界模型 → General World Model 通用世界模型

### 03 世界模型系统架构 (System Architecture)
Left-to-right pipeline diagram:
- **输入 Input**: Camera · LiDAR · Proprioception 本体感知 · Audio · …
- **编码器 Encoder**: Vision Encoder 视觉编码器 · Modality Encoder 多模态编码器
- **世界模型 World Model（学习世界的演化）**: latent `z_t` icon + Dynamics Model 隐空间 · Reward Model 奖励模型
- **未来预测 Future Prediction**: frame strip t+1, t+2 … t+H (driving video frames)
- **规划 Planner（优化未来轨迹）** → **策略 Policy（输出最优动作）** → **机器人执行 Robot Action** (robot arm + mobile robot photos)

### 04 技术家族 (Family Tree)
Four color-coded family columns with downward inheritance arrows:
- **A. Latent Dynamics 家族（以 RSSM 为核心）** (green): RSSM (2018) → PlaNet (2019) → Dreamer (2019) → DreamerV2 (2020) → DreamerV3 (2023)
- **B. JEPA 家族（自监督表征学习）** (purple): JEPA (2022) → I-JEPA (2022) → V-JEPA (2023) → V-JEPA2 (2024)
- **C. 生成式世界模型家族（视频生成路线）** (red): Video Diffusion (2022) → Genie (2023) → Genie 2 (2024) → Cosmos (2024)
- **D. 物理世界模型家族（物理规律建模）** (dark red): Cosmos (2024) → Newton (2024) → π0 (PI0) (2024) → GROOT (2024)

*(Note: Cosmos appears in both C and D on the poster — keep both memberships in extras; in the graph use a single `cosmos` node with converges edges into family D.)*

### 05 四大技术路线对比 (Four Major Paradigms)
Table, columns: 技术路线 / 核心思想 / 优势 / 代表模型:
| Latent Dynamics 隐空间动力学 | 学习隐空间中的世界动力学模型 | 高效压缩表征，适合长时序预测 | PlaNet, Dreamer, DreamerV3 |
| Predictive Representation 预测式表征学习 | 通过预测未来学习世界的通用表示 | 强泛化能力，不依赖标签 | JEPA, I-JEPA, V-JEPA, V-JEPA2 |
| Video Generation 视频生成 | 直接生成未来的视频帧 | 生成质量高，直观可视化 | Genie, Genie2, VideoPoet |
| Physics-aware World Model 物理世界模型 | 学习物理规律，保证物理一致性 | 可解释性强，泛化性更好 | Cosmos, Newton, PI0, GROOT |

### 06 代表模型一览 (Representative Models)
Seven org-branded cards:
- **Google**: PlaNet (2019) 隐空间动力学模型开创者 · Dreamer 系列 2019 / 2020 / 2023 · Genie (2023) 可交互生成3D世界 · Genie 2 (2024) 更强一致性与3D扩展
- **Meta**: JEPA (2022) 自监督表征学习 · I-JEPA (2022) 图像表征学习 · V-JEPA (2023) 视频表征自监督学习 · V-JEPA2 (2024) 更强的时空理解能力
- **NVIDIA**: Cosmos (2024) 世界基础模型平台 — 物理一致性 + 仿真生成，支持机器人与自动驾驶
- **DeepMind**: MuZero (2020) 无模型RL突破 · Gato (2022) 通用智能体模型
- **Physical Intelligence**: π0 (2024) 通用机器人基础模型，世界模型驱动
- **Tesla**: Occupancy World Model (2024) 占用栅格 + 世界模型，用于自动驾驶
- **OpenAI**: World Model Research (2024) 世界模型研究探索

*(Google and DeepMind are separate cards on the poster despite same parent company — keep as printed.)*

### 07 当前挑战 (Current Challenges)
Ten numbered red-accent items:
1. 长时间预测误差累积 (Error Accumulation)
2. 物理一致性不足 (Physics Consistency)
3. 泛化能力有限 (Generalization)
4. 长时序规划困难 (Long Horizon Planning)
5. 世界模型与控制器耦合不足 (Planning–Control Gap)
6. 多模态世界建模困难 (Vision + Language + Action)
7. 数据规模不足 (Real-world Data)
8. Sim2Real Gap
9. 可解释性不足 (Lack of Interpretability)
10. 实时推理成本高 (High Computational Cost)

### 08 应用场景 (Applications)
Eight icon cards (2 rows): 人形机器人 Humanoid · 自动驾驶 Autonomous Driving · 数字孪生 Digital Twin · AI 智能体 AI Agent · 游戏 AI Game AI · 工业机器人 Industrial Robotics · 仿真训练 Simulation · XR / 元宇宙 XR / Metaverse

### 09–11 middle-lower band
- **12 关键数据集 (Key Datasets)** *(poster numbers it 12 even though it sits left of 10/11 — numbering quirk, transcribe as printed)*:
  - Ego4D — 大规模第一人称视频数据集
  - BridgeData — 自动驾驶场景数据集 *(poster mislabel; BridgeData is actually a robot-manipulation dataset — flag to k2)*
  - Open X-Embodiment — 机器人数据集
  - RT-1 Dataset — 机器人动作指令数据集
  - Waymo Open Dataset — 自动驾驶数据集
  - nuScenes — 多模态自动驾驶数据集
  - CALVIN — 机器人操作行为数据集
  - RoboNet — 机器人操作视频数据集
  - Habitat — 3D 环境导航数据集
- **10 学习路线 (Learning Path)**: Control Theory 控制理论 → RL → Transformer Transformer 架构 → Diffusion Model 扩散模型 → Video Generation 视频生成 → JEPA 世界模型 → Cosmos 物理世界模型 → Embodied AI 具身智能
- **11 技术路线演化 (Evolutionary Roadmap)**: Physics 物理规律 → Control Theory 控制理论 → State Estimation 状态估计 → Model-based RL 基于模型的RL → Latent Dynamics 隐空间动力学 → Transformer → Diffusion 扩散模型 → Video Generation 视频生成 → Embodied World Model → 通用人工智能 (AGI)

### 13 未来趋势 (Future Trends)
Six items (2 columns × 3):
- 通用世界模型 (General World Model) — 构建统一、可泛化的世界模型
- 物理一致性建模 (Physics-aware Modeling) — 将物理规律融入世界模型
- 视频生成即预测 (Video Generation as Prediction) — 生成式模型成为世界预测的通用范式
- 世界模型 + Agent 深度融合 (World Model + Agent)
- 世界模型驱动具身智能 (Embodied World Models)
- 通向 AGI 的核心能力 (Prediction → Planning → Action) — 理解世界，推演未来，预见行动

## 4. Bottom band(s)

Full-width dark navy band, left: **世界模型全景地图 (World Model Landscape)** — 6 colored columns with chips (verbatim; tiny text, uncertain items marked):

- **Latent Dynamics 路线（隐空间动力学）** (green): RSSM · PlaNet · DreamerV3 · Ensemble Dynamics | CaITta [uncertain] · Fisher [uncertain] · MEPO · SimMBM [uncertain]
- **Predictive Representation 路线（表征学习）** (purple): JEPA · I-JEPA · V-JEPA · V-JEPA2 · MAE · BEIT
- **Video World Models 路线（视频生成）** (red): Video Diffusion · Genie · Genie 2 · VideoPoet · Sora (Research)
- **Physics World Models 路线（物理规律建模）** (orange): Cosmos · Newton · Galileo · Phyformer · Neural PDE
- **Embodied World Models 路线（具身世界模型）** (teal): OpenVLA WM · π0 (PI0) · RT-2-WM · RDT-1B · VIMA
- **Occupancy World Models 路线（占用栅格/场景）** (blue): Occupancy World Model · BEVFormer · UniAD · Wayve WM · DriveDreamer

Bottom-right: dark card with robot artwork and en quote:
> The next generation of AI will not only understand the world — it will imagine, predict, and reason about the future before acting.

No NEXT-volume teaser.

## 5. Graph content (for knowledge graph nodes/edges)

Nodes (id / zh / en / year / kind):
- `model_based_control` — 基于模型的控制 / Model-based Control / 1980 / concept
- `kalman_filter` — 卡尔曼滤波 / Kalman Filter & Particle Filter / 2000 / concept
- `mpc` — 模型预测控制 / Model Predictive Control (MPC) / 2013 / concept
- `rssm` — RSSM / Recurrent State-Space Model / 2018 / paper
- `planet` — PlaNet / PlaNet / 2019 / model
- `dreamer` — Dreamer / Dreamer / 2019 / model
- `dreamerv2` — DreamerV2 / DreamerV2 / 2020 / model
- `dreamerv3` — DreamerV3 / DreamerV3 / 2023 / model
- `muzero` — MuZero / MuZero / 2020 / model
- `decision_transformer` — Decision Transformer / Decision Transformer / 2021 / model
- `gato` — Gato / Gato / 2022 / model
- `jepa` — JEPA / Joint-Embedding Predictive Architecture / 2022 / paper
- `i_jepa` — I-JEPA / I-JEPA / 2022 / model
- `v_jepa` — V-JEPA / V-JEPA / 2023 / model
- `v_jepa2` — V-JEPA2 / V-JEPA2 / 2024 / model
- `video_diffusion` — 视频扩散模型 / Video Diffusion / 2022 / model
- `videopoet` — VideoPoet / VideoPoet / 2023 / model
- `sora` — Sora / Sora (Research) / 2024 / model
- `genie` — Genie / Genie / 2023 / model
- `genie2` — Genie 2 / Genie 2 / 2024 / model
- `cosmos` — Cosmos / NVIDIA Cosmos / 2024 / model
- `newton` — Newton / Newton / 2024 / model
- `pi0` — π0 / PI0 (Physical Intelligence) / 2024 / model
- `groot` — GROOT / NVIDIA GROOT / 2024 / model
- `openvla_wm` — OpenVLA WM / OpenVLA World Model / 2024 / model
- `rt2_wm` — RT-2-WM / RT-2 World Model / 2024 / model
- `rdt_1b` — RDT-1B / RDT-1B / 2024 / model
- `vima` — VIMA / VIMA / 2022 / model
- `occupancy_world_model` — 占用世界模型 / Occupancy World Model (Tesla) / 2024 / model
- `bevformer` — BEVFormer / BEVFormer / 2022 / model
- `uniad` — UniAD / UniAD / 2023 / model
- `wayve_wm` — Wayve WM / Wayve World Model / 2024 / model
- `drivedreamer` — DriveDreamer / DriveDreamer / 2023 / model
- `mae` — MAE / Masked Autoencoder / 2021 / model
- `beit` — BEiT / BEiT / 2021 / model
- `ensemble_dynamics` — Ensemble Dynamics / Ensemble Dynamics / 2020 / concept
- `galileo` — Galileo / Galileo (physics WM) / 2024 / model
- `neural_pde` — Neural PDE / Neural PDE / 2021 / concept
- `general_world_model` — 通用世界模型 / General World Model / 2025 / concept
- datasets: `ego4d`, `bridgedata`, `open_x_embodiment`, `rt1_dataset`, `calvin`, `robonet`, `habitat` / industry (dataset)

Edges (relation semantics per AI圣经_修订版.md):
- `rssm` → `planet` (inherits); `planet` → `dreamer` (inherits); `dreamer` → `dreamerv2` (inherits); `dreamerv2` → `dreamerv3` (inherits) — same Google/DeepMind line, poster family A
- `jepa` → `i_jepa` (inherits); `i_jepa` → `v_jepa` (inherits); `v_jepa` → `v_jepa2` (inherits) — Meta line, family B
- `mae` → `i_jepa` (converges — masked prediction vs joint embedding); `beit` → `i_jepa` (converges)
- `video_diffusion` → `genie` (inherits per poster family C); `genie` → `genie2` (inherits); `genie2` → `cosmos` (converges — different orgs, same generative-WM direction)
- `video_diffusion` → `sora` (converges); `sora` → `genie2` (converges)
- `cosmos` → `newton` (converges); `newton` → `pi0` (converges); `pi0` → `groot` (converges — poster family D shows arrows; orgs differ so converges not inherits)
- `muzero` → `dreamer` line: `muzero` → `planet` (converges — model-based RL, different approach); `decision_transformer` → `dreamer` (converges — sequence modeling vs RSSM)
- `dreamerv3` → `general_world_model` (converges); `v_jepa2` → `general_world_model` (converges); `cosmos` → `general_world_model` (converges)
- `bevformer` → `uniad` (composes); `occupancy_world_model` → `drivedreamer` (converges); `wayve_wm` → `drivedreamer` (converges)
- `openvla_wm` → `pi0` (converges — embodied WM); `rt2_wm` → `openvla_wm` (converges); `vima` → `rt2_wm` (converges)
- `cosmos` → `groot` (composes — NVIDIA platform ＋ robot foundation model; same org so inherits also acceptable, poster arrow implies inherits within family D)
- `gato` → `pi0` (converges — generalist agents)

## 6. Style notes

- Same light "Modern AI Atlas" series style as vol09: off-white/very light blue background (#F5F8FE-ish), white cards with light-blue borders, navy section badges with white numbers.
- Header: giant black `World Models` + zh 世界模型; blue en subtitle; violet `Vol.10` chip.
- Family tree colors: A green (#2FA84F-ish), B purple (#7B5EA7-ish), C red/pink (#D94F5C-ish), D dark red/maroon — column headers and arrow connectors tinted accordingly.
- Section 05 is a 4-row comparison table with alternating very light row fills.
- Org cards (06) carry real brand logos (Google colors, Meta blue, NVIDIA green, Tesla red, OpenAI black).
- Challenges (07) in red accent; Applications (08) as photo thumbnails with blue captions.
- Bottom "World Model Landscape" band: dark navy background (#0A1A3F-ish), gold star icon, six neon-outlined columns (green/purple/red/orange/teal/blue chips).
- Landscape orientation (1536×1024) — denser 3-row grid: top band (01,02), middle band (03,04,05), lower band (06,07,08), bottom band (12,10,11 over landscape map, 13).
- Poster numbering quirk: datasets section is numbered `12` while learning path is `10` and evolution `11`, all sitting in the same lower band — reproduce numbers as printed.
