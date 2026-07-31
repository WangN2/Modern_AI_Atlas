# Vol.07 计算机视觉 / Computer Vision

- Source image: `assets/reference/volumes/7.计算机视觉.png`
- Declared volume number in header: **Vol.07** (matches filename number 7 — no discrepancy)
- Aspect: portrait 2:3 (1024×1536 reference)
- Theme note: light background; sections are **numbered 1–15** with circled numerals (unlike Vol.04–06).

## 1. Header

- Left badge: dark navy `Modern AI Atlas` + pill `Vol.07`.
- Title (zh): **计算机视觉**
- Subtitle (en): **Computer Vision** (indigo)
- Tagline (zh): **从像素到理解，连接物理世界与智能未来**
- Top-right quote box:
  > 计算机视觉赋予机器"看"的能力，让它理解世界、创造价值、改变未来。
  > — Fei-Fei Li
- Far-right header illustration: glowing digital eye (blue/purple).

## 2. Legend row

No legend panel anywhere on this poster (no top row, no bottom 图例). Section family trees use colored node pills instead (see §6).

## 3. Sections (in top-to-bottom order)

### ① 计算机视觉发展时间线 (Timeline: 1970s – 2026+)

8 era columns above a navy axis with sketch images below (edge-map, SIFT keypoints photo, MNIST digits `01234 56789`, CNN diagram, multi-CNN sketch, detection/segmentation photos, ViT patch diagram, SAM collage).

| Era | Years | Bullets |
|-----|-------|---------|
| 图像处理时代 Image Processing Era | 1970s–1980s | 边缘检测 / 阈值分割 / 形态学 / 传统滤波 |
| 特征工程时代 Feature Engineering Era | 1990s | SIFT / SURF / HOG / LBP / 颜色直方图 |
| 浅层学习时代 Shallow Learning Era | 2000s | LeNet / SVM + HOG / AdaBoost / 传统分类器 |
| 深度学习突破 Deep Learning Breakthrough | 2012 | AlexNet 开启大规模CNN时代 / ImageNet 准确率大幅提升 |
| CNN快速发展 CNN Rapid Growth | 2014–2016 | VGG, GoogLeNet / ResNet, Inception / DenseNet / 更深、更准、更强 |
| 检测与分割爆发 Detection & Segmentation Boom | 2017–2019 | YOLO, SSD, RetinaNet / Mask R-CNN, FPN / DeepLab, U-Net++ / 实例分割、语义分割 |
| Transformer视觉崛起 Transformer for Vision | 2020–2022 | ViT, DeiT, Swin / MAE, BEiT, DINO / 视觉也进入大模型时代 |
| 视觉大模型时代 Vision Foundation Models Era | 2023–2026+ | SAM, SAM2 / DINOv2, SigLIP / Florence, InternVL / Qwen-VL Encoder / 通用视觉理解与生成 |

### ② 技术路线演化 (Evolution of Paradigms)

4-stage horizontal flow (large arrows between stages, icon sketches below):

1. 手工特征时代 Hand-crafted Feature Era (1970s–1990s) — 依赖人工设计特征 — icons: SIFT, HOG, Haar
2. CNN时代 CNN Era (2012–2016) — 端到端学习 特征自动提取
3. Transformer时代 Transformer Era (2017–2021) — 全局建模 更强泛化能力
4. 基础模型时代 Foundation Model Era (2022–现在) — 大规模预训练 通用视觉理解

### ③ 视觉技术全景图 (CV Technology Landscape)

4-layer stack (each layer = label + en subtitle + item chips):

- 基础任务 (Tasks): 分类 Classification · 检测 Detection · 分割 Segmentation · 生成 Generation · 匹配 Matching · 三维视觉 3D Vision · 视频理解 Video Understanding
- 核心技术 (Methods): CNN 卷积神经网络 · Transformer 视觉Transformer · 自监督学习 Self-supervised Learning · 多模态视觉 Multimodal Vision · 基础模型 Vision Foundation Models
- 使能技术 (Enablers): 大规模数据 Large-scale Data · 高性能计算 High Performance Computing · 优化算法 Optimization · 标注与评估 Annotation & Evaluation
- 应用领域 (Applications): 自动驾驶 Autonomous Driving · 医疗影像 Medical Imaging · 遥感 Remote Sensing · 工业检测 Industrial Inspection · 安防监控 Surveillance · 机器人 Robotics · 人机交互 Human-Computer Interaction · 多模态AI Multimodal AI

### ④ CNN家族演化树 (CNN Family Tree)

Vertical chain (main trunk, green pills, downward arrows):

LeNet (1998) → AlexNet (2012) → VGG (2014) → GoogLeNet (2014) → ResNet (2015) → DenseNet (2017) → EfficientNet (2019) → ConvNeXt (2022) → RepLKNet (2022)

Side-branch pills (right of trunk): RegNet (2020) · ResNeXt (2017) · MobileNet (2017) · MobileNetV3 (2019) · ShuffleNet (2018)

### ⑤ Vision Transformer 家族 (Vision Transformer Family)

Vertical chain (blue pills):

ViT (2020) → DeiT (2021) → Swin Transformer (2021) → BEiT (2021) → MAE (2021) → DINO (2021) → DINOv2 (2023) → SigLIP (2023) → EVA (2023) → SAM Encoder (2023)

### ⑥ 视觉大模型与基础模型 (Vision Foundation Models)

List of logo + name + zh desc:

- SAM (Meta AI, 2023) — 通用分割模型
- SAM 2 (Meta AI, 2024) — 视频分割模型
- CLIP (OpenAI, 2021) — 跨模态对齐模型
- SigLIP (Google, 2023) — 更简洁的图文对齐 *(word "简洁" slightly uncertain at this resolution)*
- Florence (Microsoft, 2021) — 多任务视觉基础模型
- InternVL (上海人工智能实验室, 2023) — 多模态视觉理解
- Qwen-VL Vision Encoder (阿里巴巴, 2023) — 通用视觉编码器
- DINOv2 (Meta AI, 2023) — 自监督视觉基础模型

### ⑦ 目标检测发展路线 (Object Detection Lineage)

Three bracketed groups:

- **Two-Stage (两阶段)**: R-CNN (2014) → Fast R-CNN (2015) → Faster R-CNN (2015) → Mask R-CNN (2017)
- **One-Stage (单阶段)**: YOLO (2016) → YOLOv2 (2017) → YOLOv3 (2018) → YOLOv4 (2020) → YOLOv8 (2023); SSD (2016); RetinaNet (2017)
- **Transformer-Based (基于Transformer)**: DETR (2020) → Deformable DETR (2021) → RT-DETR (2023)

### ⑧ 语义/实例分割发展路线 (Segmentation Lineage)

Three bracketed groups (orange/red pills):

- **语义分割 (Semantic)**: FCN (2015) → U-Net (2015) → SegNet (2015) → DeepLab v1 (2017) → DeepLab v3 (2017) → DeepLab v3+ (2018) → PSPNet (2017)
- **实例分割 (Instance)**: Mask R-CNN (2017) → Panoptic FPN (2019)
- **通用分割 (Universal)**: SAM (2023) → SAM 2 (2024)

### ⑨ 自监督学习发展路线 (Self-supervised Learning)

Three bracketed groups (green pills):

- **对比学习 (Contrastive)**: SimCLR (2020) · MoCo v1/v2/v3 (2020–2021) · BYOL (2020) · SimSiam (2021) · SwAV (2021) · DINO (2021)
- **生成式预训练 (Generative)**: MAE (2021) · BEiT (2021) · DINOv2 (2023)
- **掩码预测与蒸馏 (Masked Prediction)**: iBOT (2023) · JEPA (Meta, 2023)

*(Note: DINOv2 appears under 生成式预训练 here while DINO appears under 对比学习 — reproduce as printed.)*

### ⑩ 视觉应用领域 (Applications of Computer Vision)

8 domain cards (icon + zh/en title + 4 bullets each):

- 自动驾驶 Autonomous Driving — 目标检测 / 车道线检测 / BEV感知 / 三维重建
- 医疗影像 Medical Imaging — 病灶检测 / 分割 / 图像生成 / 辅助诊断
- 遥感与地理 Remote Sensing — 地物分类 / 变化检测 / 目标检测 / 三维重建
- 工业视觉 Industrial Vision — 缺陷检测 / 质量控制 / 装配检测 / OCR识别
- 安防监控 Surveillance — 人脸识别 / 行为分析 / 目标跟踪 / 异常检测
- 机器人视觉 Robotics Vision — 三维感知 / 视觉定位 / SLAM / 导航避障
- 多媒体内容理解 Multimedia Understanding — 图像描述 / 视觉问答 / 图文检索 / 内容生成
- AR/VR/MR 增强现实 — 三维感知 / 三维重建 / 虚拟互动 / 场景理解

### ⑪ 经典数据集 (Datasets)

Table, headers: 任务 | 数据集 | 规模 | 简介

| 任务 | 数据集 | 规模 | 简介 |
|------|--------|------|------|
| 图像分类 | ImageNet | ~1400万图像 | 最著名的大规模分类数据集 |
| 目标检测 | COCO | 20万图像 | 多目标、多尺度检测 |
| 目标检测 | PASCAL VOC | 2万图像 | 经典检测数据集 |
| 实例分割 | ADE20K | 25K图像 | 场景解析分割 |
| 语义分割 | Cityscapes | 5K图像 | 自动驾驶场景分割 |
| 语义分割 | Pascal Context | 17万图像 | 像素级标注数据集 |
| 人脸识别 | LFW | 1.3万张人脸 | 人脸验证基准 |
| 遥感 | DIOR | 2.3万图像 | 遥感目标检测 |
| 视频理解 | Kinetics-700 | 65万视频 | 大规模动作识别 |
| 3D 视觉 | ScanNet | 250万视角 | 三维重建与理解 |

### ⑫ 重要基准 (Benchmarks)

Table, headers: 任务 | 基准 | 评价指标

| 任务 | 基准 | 评价指标 |
|------|------|----------|
| 图像分类 | ImageNet | Top-1 Accuracy |
| 目标检测 | COCO | mAP (AP@[.5:.95]) |
| 实例分割 | PASCAL | mAP (mask) |
| 语义分割 | ADE20K | mIoU |
| 图像分割 | Cityscapes | mIoU |
| 人脸识别 | LFW | Accuracy |
| 视频理解 | Kinetics | Top-1 Accuracy |
| 多模态检索 | Flickr30K | Recall@K |

### ⑬ 代表性论文 (Key Papers)

Year + citation list:

- 2012 — AlexNet: ImageNet Classification with Deep CNNs
- 2014 — Very Deep Convolutional Networks for Large-Scale Image Recognition (VGG)
- 2015 — Deep Residual Learning for Image Recognition (ResNet)
- 2016 — You Only Look Once: Unified, Real-Time Object Detection (YOLOv1)
- 2017 — Mask R-CNN
- 2017 — Attention Is All You Need (Transformer)
- 2020 — An Image is Worth 16x16 Words: Transformers for Image Recognition (ViT)
- 2021 — Masked Autoencoders Are Scalable Vision Learners (MAE)
- 2021 — Emerging Properties in Self-Supervised Vision Transformers (DINO)
- 2023 — Segment Anything (SAM)
- 2023 — DINOv2: Learning Robust Visual Features without Supervision

### ⑭ 代表公司与开源项目 (Companies & Open Source)

Two columns (公司/机构 | Models/Projects):

- Meta — SAM, SAM 2, DINOv2, LLaMA Vision
- Google — SigLIP, ViT, PaLI, Florence *(as printed — Florence is also listed under Microsoft in §⑥; flag duplication for k2)*
- OpenAI — CLIP
- Microsoft — Florence, U-Former
- NVIDIA — NeMo Vision, Cosmos
- 阿里巴巴 — Qwen-VL, Qwen-VL-Chat

开源框架: PyTorch, TensorFlow, MMEngine, Detectron2, MMDetection, OpenMMLab, timm, Hugging Face Transformers

### ⑮ 未来趋势 (Future Trends)

7 icon items (zh + en):

1. 视觉基础模型 (更大、更通用) — Vision Foundation Models
2. 多模态视觉理解与生成 — Multimodal Vision Understanding & Generation
3. 自监督与无监督学习 — Self-supervised & Unsupervised Learning
4. 3D/4D 视觉与世界建模 — 3D/4D Vision & World Modeling
5. 具身智能与机器人视觉 — Embodied AI & Robotics Vision
6. 高效模型与边缘部署 — Efficient Models & Edge Deployment
7. 跨模态融合 (图文、语言、科学等) — Cross-domain Integration

## 4. Bottom band(s)

- Dark navy gradient banner (brain hologram, car, humanoid, robot-arm sketches), bilingual quote:
  > 计算机视觉正在从"看清"走向"理解"，从专用走向通用，从感知走向智能。
  > Computer Vision is evolving from "seeing" to "understanding", from task-specific to general-purpose, from perception to intelligence.
- No NEXT Vol.XX teaser, no summary stats row.

## 5. Graph content (for knowledge graph nodes/edges)

### Nodes (main; all years as printed on poster)

`lenet` (1998), `alexnet` (2012, milestone), `vgg` (2014), `googlenet` (2014), `resnet` (2015, milestone), `densenet` (2017), `efficientnet` (2019), `convnext` (2022), `replknet` (2022), `regnet` (2020), `resnext` (2017), `mobilenet` (2017), `mobilenetv3` (2019), `shufflenet` (2018) — kind: model/paper
`vit` (2020, milestone), `deit` (2021), `swin_transformer` (2021), `beit` (2021), `mae` (2021, milestone), `dino` (2021), `dinov2` (2023), `siglip` (2023), `eva` (2023), `sam_encoder` (2023)
`sam` (2023, milestone), `sam_2` (2024), `clip` (2021, milestone), `florence` (2021), `internvl` (2023), `qwen_vl_encoder` (2023)
`r_cnn` (2014), `fast_r_cnn` (2015), `faster_r_cnn` (2015), `mask_r_cnn` (2017), `yolo` (2016), `yolov2` (2017), `yolov3` (2018), `yolov4` (2020), `yolov8` (2023), `ssd` (2016), `retinanet` (2017), `detr` (2020), `deformable_detr` (2021), `rt_detr` (2023)
`fcn` (2015), `u_net` (2015), `segnet` (2015), `deeplab_v1` (2017), `deeplab_v3` (2017), `deeplab_v3plus` (2018), `pspnet` (2017), `panoptic_fpn` (2019)
`simclr` (2020), `moco` (2020–2021), `byol` (2020), `simsiam` (2021), `swav` (2021), `ibot` (2023), `jepa` (2023)
Concepts: `sift` (1999), `hog` (2005), `svm_hog_pipeline`, `adaboost` — kind: concept

### Suggested edges

**CNN trunk** (poster draws them as a single chain, but per AI圣经 anti-beautification rule, only same-line descents are 直接继承):
- `lenet → alexnet` — **inherits** (direct CNN revival lineage)
- `alexnet → vgg` — **converges** (both deepen plain CNNs; VGG is parallel refinement, commonly cited as evolution — k2 may choose inherits; flag)
- `alexnet ↔ googlenet` — **converges** (ILSVRC'14 parallel routes: plain-deep vs Inception)
- `vgg → resnet` — **converges** (ResNet's plain-net baseline follows VGG, but residual learning is a new branch)
- `resnet → densenet` — **converges** (parallel "skip-connection" routes)
- `resnet → resnext → regnet` — **inherits** (same Meta/Facebook design lineage)
- `resnet → convnext` — **composes** (ResNet modernized with Transformer design elements)
- `efficientnet`, `replknet`, `mobilenet` family — **converges** with trunk (efficiency branch); `mobilenet → mobilenetv3` — **inherits**
- `googlenet → shufflenet` — **converges** (efficient-architecture branch)

**ViT family:**
- `vit → deit` — **inherits** (distillation of ViT)
- `vit → swin_transformer` — **converges** (hierarchical shifted-window route)
- `vit → beit` — **converges** (masked image modeling on ViT)
- `beit ↔ mae` — **converges** (parallel MIM routes, 2021)
- `vit → dino → dinov2` — **inherits** (self-distillation lineage)
- `clip → siglip` — **inherits** (SigLIP = sigmoid-loss CLIP variant)
- `mae → sam_encoder` — **inherits** (SAM image encoder is MAE-pretrained ViT-H)
- `vit → clip` — **composes** (explicit AI圣经 rule: CLIP combines ViT + text transformer; do NOT draw ViT → CLIP as inheritance)
- `clip → internvl` — **converges** (explicit AI圣经 rule)
- `clip → florence` — **converges**
- `mae → ibot` — **converges**; `jepa` — **converges** with all SSL routes (independent LeCun route per AI圣经 JEPA note)

**Detection:**
- `r_cnn → fast_r_cnn → faster_r_cnn → mask_r_cnn` — **inherits**
- `yolo → yolov2 → yolov3 → yolov4 → yolov8` — **inherits**
- `yolo ↔ ssd` — **converges** (parallel one-stage routes)
- `retinanet` — **converges** with one-stage trunk (focal loss branch)
- `detr → deformable_detr → rt_detr` — **inherits**
- `detr ↔ faster_r_cnn` — **converges** (transformer vs two-stage paradigms)

**Segmentation:**
- `fcn → u_net`, `fcn → segnet`, `fcn → deeplab_v1`, `fcn → pspnet` — **converges** (all descend conceptually from FCN's fully-convolutional idea but are parallel designs; k2 may draw `fcn → *` as converges fan-out)
- `deeplab_v1 → deeplab_v3 → deeplab_v3plus` — **inherits**
- `mask_r_cnn → panoptic_fpn` — **inherits**
- `mae → sam` — **composes** (SAM = MAE ViT encoder + prompt encoder + mask decoder)
- `sam → sam_2` — **inherits**

**SSL:**
- `simclr ↔ moco ↔ byol ↔ simsiam ↔ swav` — **converges** (parallel contrastive/self-distillation routes)
- `moco → dino` — **converges**

## 6. Style notes

- Same light theme as Vol.04–06, but layout is a **numbered grid**: circled navy numerals 1–15 prefix section titles.
- Family-tree panels (④⑤⑦⑧⑨) render models as rounded pills with year in parentheses, connected by thin arrows, with a curly-brace bracket + group label (zh + en) on the right of each group. Pill fill colors by family: CNN = light green, ViT = light blue, segmentation = light orange, SAM/universal = pink/red, SSL = light green.
- Foundation-model list (⑥) includes brand logo glyphs (Meta infinity, OpenAI swirl, Google "G", Microsoft squares, InternVL, Qwen).
- Timeline era decorations are grayscale/colored sketch thumbnails (edge maps, MNIST digits, architecture diagrams) — ornamental.
- Tables (⑪⑫⑬) are compact with indigo header rows.
- Bottom banner: dark navy gradient, white zh quote + light-blue en translation; holographic brain/car/robot line-art as decoration.
- Highest information density of the five assigned volumes — body text ≈9–10px at 1024px width.
