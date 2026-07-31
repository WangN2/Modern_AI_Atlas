# Vol.09 自动驾驶 / Autonomous Driving

- Source image: `assets/reference/volumes/9.自动驾驶.png`
- Declared volume number in header: **Vol.09** (matches filename number 9 — no discrepancy)
- Aspect: portrait 2:3 (1024×1536 reference) — this is the ONLY portrait poster among vols 9–13; vols 10–13 are landscape 1536×1024.

## 1. Header

- Badge (top-left): `Modern AI Atlas` + purple chip `Vol.09`
- Title (zh): 自动驾驶
- Title (en): Autonomous Driving
- Subtitle (zh): 从感知智能到认知智能，驱动未来出行变革
- Top-right quote block:
  > 自动驾驶的终极目标，不是让机器开车，而是让机器理解世界，并在复杂世界中安全地行动。— Kai-Fu Lee
- Top-right artwork: futuristic blue concept car on a glowing city road (AI-generated illustration)
- No explicit series line ("AI Technology Bible · Volume NN") on this poster; series identity is the "Modern AI Atlas" badge.

## 2. Legend row

This poster has **no dedicated legend row** for edge styles or node kinds (unlike vol02). Color coding is implicit:
- Numbered section badges: dark navy-blue squares with white numerals (❶–❶❸)
- Section 10 (挑战) uses red/warning accent icons instead of blue
- Timeline era chips in section 1 use dark blue year labels
- No 继承/趋同/组合 line-style legend is present.

## 3. Sections (in top-to-bottom order)

### ❶ 自动驾驶发展时间线 (Timeline: 1980s — 2026+)
Horizontal 7-column era strip, each era with title + 3 bullets and a small photo beneath.

1. **1980s–1990s 萌芽探索阶段 Early Exploration**
   - DARPA 自动驾驶挑战赛
   - 传统算法与规则系统
   - 简单环境感知
2. **2000–2010 技术积累阶段 Technology Accumulation**
   - 传感器技术发展
   - SLAM 与地图构建
   - 传统机器学习应用
3. **2011–2014 深度学习引入阶段 Deep Learning Emergence**
   - AlexNet 推动视觉突破
   - 深度 CNN 应用于感知
   - KITTI 数据集发布
4. **2015–2017 感知突破阶段 Perception Breakthrough**
   - 目标检测精度大幅提升
   - 语义分割与多任务学习
   - 端到端感知系统出现
5. **2018–2020 高精地图与融合阶段 HD Map & Fusion Era**
   - 高精地图广泛应用
   - 多传感器融合多模态
   - 规划与控制模块化
6. **2021–2023 端到端转型阶段 End-to-End Transition**
   - BEV 感知成为主流
   - Transformer 进入自动驾驶
   - 端到端自动驾驶落地测试
7. **2024–2026+ 大模型驱动阶段 Foundation Model Era**
   - VLM + 世界模型上车
   - 端到端大模型
   - 真实世界大规模商业化

Embedded mini-images per era: DARPA challenge vehicle, point-cloud SLAM map, annotated street scene, nighttime semantic segmentation, HD-map lane view, BEV sensor-fusion diagram, highway concept render.

### ❷ 自动驾驶系统架构 (System Architecture)
Left column (传感器输入 Sensor Input), verbatim:
- 摄像头 Camera
- 激光雷达 LiDAR
- 毫米波雷达 Radar
- 超声波雷达 USS
- IMU / GNSS
- 高精地图 HD Map

Pipeline cards (left→right flow):
- **感知 (Perception)**: 目标检测 Detection · 语义分割 Segmentation · 车道线检测 Lane Detection · 深度估计 Depth Estimation · 多目标跟踪 Tracking · 可行驶区域 Drivable Area
- **定位与建图 (Localization & Mapping)**: SLAM · 定位 Localization · 高精地图 HD Map
- **预测 (Prediction)**: 目标预测 Object Prediction · 轨迹预测 Trajectory Prediction · 场景预测 Scene Prediction
- **规划 (Planning)**: 全局规划 Global Planning · 行为规划 Behavior Planning · 路径规划 Path Planning
- **控制 (Control)**: 转向控制 Steering · 加速控制 Acceleration · 制动控制 Braking

### ❸ 技术路线演进 (Evolutionary Roadmap)
Five arrow-linked stage cards (accent: blue gradient), each with era chip + 3 bullets:

1. **模块化 (Modular Pipeline) 2010s**: 分模块设计 · 规则 + 传统算法 · 高精地图依赖
2. **感知主导 (Perception-Centric) 2016–2019**: 深度学习感知 · 多任务学习 · 模块化规划控制
3. **BEV + 融合 (BEV + Fusion) 2020–2022**: BEV 表示 · 多传感器融合 · 端到端组件出现
4. **端到端 (End-to-End) 2022–2024**: 端到端模型 · 不依赖高精地图 · 大规模数据驱动
5. **大模型时代 (Foundation Model Era) 2024+**: VLM + 世界模型 · 通用场景理解 · 自主决策与泛化

Embedded mini-diagrams below the cards: modular pipeline block diagram, stacked network layers, isometric smart-city BEV grid, neural-net graph, brain-shaped AI outline.

### ❹ (unnumbered right half, part of ❸ row) — nothing separate; the layout merges ❸ across the right half.

### ❺ 感知技术全景 (Perception Panorama)
Four-stage flow with photos:
- **数据输入 Input**: street camera image + point-cloud render
- **感知任务 Perception Tasks**: 3D 目标检测 3D Detection · 语义分割 Semantic Segmentation · 车道线检测 Lane Detection · 可行驶区域 Drivable Area · 深度估计 Depth Estimation · 实例分割 Instance Segmentation
- **BEV 表示 BEV Representation**: BEV grid diagram + HD map ("HD Xap" [sic — poster misprint for "HD Map"])
- **输出结果 Output**: 3D检测结果 · 语义分割结果 · 车道线结果 · 可行驶区域 · 深度图 · 实例分割结果 (each with a small thumbnail)

### ❻ 代表性算法与模型 (Representative Algorithms & Models)
Five columns, verbatim bullet lists:
- **检测 (Detection)**: R-CNN 系列 · YOLO 系列 · CenterPoint · PV-RCNN · SECOND · RT-DETR
- **分割 (Segmentation)**: FCN · DeepLab 系列 · SegFormer · BEVFormer · Mask2Former
- **预测 (Prediction)**: Social LSTM · VectorNet · HiVT · MTR · MotionLM
- **规划 (Planning)**: A* / D* Lite · Hybrid A* · Lattice Planner · ILQR · CHOMP / STOMP
- **端到端 (End-to-End)**: UniAD · VAD · EMMA · DriveGPT4 · Tesla FSD

(Note for k2: the poster places BEVFormer under 分割/Segmentation even though it is a BEV perception model — transcribe as-is.)

### ❼ 主流自动驾驶公司与方案 (Companies & Solutions)
Ten logo cards (2 rows × 5):
- Tesla FSD · Waymo Driver · Baidu Apollo · 小鹏汽车 XNGP · 理想汽车 AD Max
- 蔚来 NIO Pilot · 华为 ADS · Momenta Mpilot · 智己汽车 IM AD · 滴滴自动驾驶 Didi Neuron

### ❽ 关键数据集 (Key Datasets)
- KITTI (2012)
- nuScenes (2019)
- Waymo Open Dataset (2019)
- Argoverse 2 (2019)
- Lyft Level 5 (2020)
- ONCE (2021)
- PandaSet (2021)
- BDD100K (2020)
- DIOR (2022)  *(poster says DIOR — likely a GPT-generated mistake; DIOR is a remote-sensing dataset. Transcribe verbatim, flag to k2.)*
- OpenLane (2023)

Right side: 2×5 grid of dataset sample thumbnails.

### ❾ 评价指标 (Evaluation Metrics)
Five columns:
- **检测类**: mAP · NDS · AMOTA
- **分割类**: mIoU · mAcc · Dice
- **预测类**: minADE · minFDE · HOTA
- **规划控制类**: L2 距离 · 碰撞率 · 成功率
- **综合指标**: 安全性 · 舒适性 · 效率性

### ❿ 当前面临的挑战 (Open Challenges)  — red/warning accent
Left column:
- 长尾场景与极端场景泛化能力不足
- 感知错误导致的级联风险
- 预测的不确定性与交互博弈难题

Right column:
- 高精地图成本高、更新难、覆盖不足
- Sim2Real Gap 与域迁移困难
- 数据隐私、合规与安全问题
- 大规模端到端模型的可解释性不足
- 算力需求巨大，成本与能耗高

### ⓫ 未来趋势 (Future Trends)
- 大模型驱动的自动驾驶（VLM + World Model）
- 无图化（Mapless）与轻地图方案
- 端到端自动驾驶大模型
- 多模态融合与自监督学习
- 车路协同（V2X）与智慧交通
- 更安全、更可解释、更可靠的自动驾驶

### ⓬ 典型场景应用 (Typical Applications)
Six icon chips: 城市道路 Urban Road · 高速公路 Highway · 自动泊车 Auto Parking · Robotaxi 自动驾驶出租车 · 干线物流 Autonomous Trucking · 矿区/港口 Industrial & Mining

### ⓭ 学习路线图 (Learning Roadmap)
Right-ascending curved path with 7 nodes:
基础知识（数学、编程、线性代数）→ 机器学习基础 ML Basics → 计算机视觉 CV → 深度学习 Deep Learning → 自动驾驶核心（感知/定位/规划）→ 仿真与工具（CARLA/ROS）→ 工程实践（项目实战）

## 4. Bottom band(s)

Dark navy footer band with car artwork left and right, centered bilingual quote:
> 自动驾驶的本质是：让机器理解世界，在复杂、不确定的环境中做出安全、智能的决策。
> The essence of autonomous driving is to enable machines to understand the world and make safe and intelligent decisions in complex and uncertain environments.

No NEXT-volume teaser on this poster.

## 5. Graph content (for knowledge graph nodes/edges)

Nodes (id suggestion / zh label / en label / year / kind):
- `darpa_challenge` — DARPA 自动驾驶挑战赛 / DARPA Grand Challenge / 2004 / milestone
- `slam` — SLAM 与地图构建 / SLAM / 2000s / concept
- `alexnet` — AlexNet / AlexNet / 2012 / model
- `kitti` — KITTI 数据集 / KITTI / 2012 / industry (dataset)
- `rcnn_family` — R-CNN 系列 / R-CNN family / 2014 / model
- `yolo_family` — YOLO 系列 / YOLO family / 2016 / model
- `fcn` — FCN / Fully Convolutional Network / 2015 / model
- `deeplab_family` — DeepLab 系列 / DeepLab family / 2016 / model
- `social_lstm` — Social LSTM / Social LSTM / 2016 / model
- `second` — SECOND / SECOND / 2018 / model
- `pointpillars_centerpoint` — CenterPoint / CenterPoint / 2020 / model
- `pv_rcnn` — PV-RCNN / PV-RCNN / 2020 / model
- `nuscenes` — nuScenes / nuScenes / 2019 / industry (dataset)
- `waymo_open_dataset` — Waymo Open Dataset / Waymo Open Dataset / 2019 / industry (dataset)
- `bev_perception` — BEV 感知 / BEV Perception / 2021 / concept
- `bevformer` — BEVFormer / BEVFormer / 2022 / model
- `transformer` — Transformer / Transformer / 2017 / paper
- `vectornet` — VectorNet / VectorNet / 2020 / model
- `hivt` — HiVT / HiVT / 2021 / model
- `mtr` — MTR / MTR / 2022 / model
- `motionlm` — MotionLM / MotionLM / 2023 / model
- `segformer` — SegFormer / SegFormer / 2021 / model
- `mask2former` — Mask2Former / Mask2Former / 2022 / model
- `rt_detr` — RT-DETR / RT-DETR / 2023 / model
- `hybrid_a_star` — Hybrid A* / Hybrid A* / 2010 / concept (algorithm)
- `lattice_planner` — Lattice Planner / Lattice Planner / 2010s / concept (algorithm)
- `ilqr` — ILQR / iLQR / 2010s / concept (algorithm)
- `chomp_stomp` — CHOMP / STOMP / CHOMP/STOMP / 2010s / concept (algorithm)
- `uniad` — UniAD / UniAD / 2023 / model
- `vad` — VAD / VAD / 2023 / model
- `emma` — EMMA / EMMA (Waymo) / 2024 / model
- `drivegpt4` — DriveGPT4 / DriveGPT4 / 2024 / model
- `tesla_fsd` — Tesla FSD / Tesla FSD / 2020 / industry
- `waymo_driver` — Waymo Driver / Waymo Driver / 2018 / industry
- `baidu_apollo` — 百度 Apollo / Baidu Apollo / 2017 / industry
- `xpeng_xngp` — 小鹏 XNGP / Xpeng XNGP / 2023 / industry
- `li_auto_ad_max` — 理想 AD Max / Li Auto AD Max / 2023 / industry
- `nio_pilot` — 蔚来 NIO Pilot / NIO Pilot / 2020 / industry
- `huawei_ads` — 华为 ADS / Huawei ADS / 2021 / industry
- `momenta_mpilot` — Momenta Mpilot / Momenta Mpilot / 2020 / industry
- `im_ad` — 智己 IM AD / IM AD / 2022 / industry
- `didi_neuron` — 滴滴自动驾驶 Didi Neuron / Didi Neuron / 2023 / industry
- `vlm_world_model_ad` — VLM + 世界模型上车 / VLM + World Model for AD / 2024 / concept
- `occupancy_network` — 占用网络 / Occupancy Network / 2022 / concept (implied by 端到端转型; not named on poster — optional)
- `bdd100k`, `argoverse2`, `lyft_l5`, `once`, `pandaset`, `openlane` — dataset nodes / 2020–2023 / industry

Edges (relation: inherits / converges / composes):
- `alexnet` → `kitti`-era perception models: `alexnet` → `rcnn_family` (inherits)
- `rcnn_family` → `pv_rcnn` (inherits); `second` → `pv_rcnn` (converges); `second` → `pointpillars_centerpoint` (inherits)
- `fcn` → `deeplab_family` (inherits); `deeplab_family` → `segformer` (converges — CNN vs Transformer segmentation); `segformer` → `mask2former` (converges)
- `transformer` → `bevformer` (composes — Transformer ＋ BEV); `bev_perception` → `bevformer` (inherits)
- `social_lstm` → `vectornet` (converges); `vectornet` → `hivt` (converges); `hivt` → `mtr` (converges); `mtr` → `motionlm` (converges)
- `bevformer` → `uniad` (composes — UniAD 组合 BEV 感知＋预测＋规划); `transformer` → `uniad` (composes)
- `uniad` → `vad` (inherits); `vad` → `emma` (converges); `transformer` → `emma` (composes)
- `vlm_world_model_ad` → `emma` (converges); `vlm_world_model_ad` → `drivegpt4` (converges)
- `tesla_fsd` → `emma` (converges — industry end-to-end); `hybrid_a_star`/`lattice_planner` → `uniad` (converges — modular → end-to-end replacement)
- Datasets as composes-inputs: `kitti` → `nuscenes` (converges), etc. (optional; datasets are flat list on poster)

## 6. Style notes

- Background: very light blue-white gradient (#F4F8FF-ish) with faint dot-grid texture — NOT the dark empire theme; the whole vol 9–13 series is the light "Modern AI Atlas" blue style.
- Header: white/very light background, huge black zh title + blue en title; `Vol.09` chip is violet-blue (#5B5BD6-ish) rounded rectangle, white text.
- Quote box: soft blue gradient card, dark blue text.
- Section headers: dark navy square badge with white number + bold navy zh title + lighter gray-blue en subtitle in parentheses.
- Cards: white fill, thin light-blue border, soft shadow; blue accent titles.
- Section 10 (challenges): red accents (#E5484D-ish icons/text) on white cards.
- Timeline arrows: blue chevron/arrow connectors between era columns and roadmap stages.
- Company logos rendered in brand colors inside white cards.
- Bottom band: dark navy (#0B1B3F-ish) with cyan glowing car artwork, white zh + light gray en text.
- Typography: bold sans-serif (zh appears as a PingFang/Source-Han style), en labels in a grotesque sans; hierarchy = black zh > blue en.
- k2 note: vol09 is portrait 1024×1536 while vols 10–13 are landscape 1536×1024 — layout templates cannot be shared blindly across this batch.
