<div align="center">

# 🌍 Modern AI Atlas

### 人工智能完整知识图谱

*一份出版物级别、持续演进的现代 AI 技术图谱。*

[![License](https://img.shields.io/badge/license-MIT-blue.svg)]()
[![Status](https://img.shields.io/badge/status-开发中-orange)]()
[![Version](https://img.shields.io/badge/version-v0.1-green)]()

</div>

---

# 📖 什么是 Modern AI Atlas？

Modern AI Atlas 是一个开源项目，系统性地将人工智能的演进组织为一个统一的知识图谱。

不同于传统的教程或零散的博客文章，本项目将 AI 呈现为一个互联的世界——每项重要技术都有其自身的历史、谱系和影响力。

我们的目标是构建现代 AI 最完整的可视化知识图谱。

---

# 🎯 愿景

人工智能不再是一系列孤立技术的集合。

如今，大语言模型、计算机视觉、强化学习、扩散模型、自动驾驶、机器人学与具身 AI 正在融合为统一的架构。

Modern AI Atlas 旨在回答以下问题：

- GPT 从何而来？
- ViT 为何取代了 CNN？
- DiT 与 Stable Diffusion 有何关联？
- JEPA 为何被视为世界模型？
- 机器人学与自动驾驶如何走向统一？
- 通往 AGI 的演化路径是什么？

---

# 🗺 图谱结构

本项目按出版物级海报系列组织。**全部 14 卷均已交付** ✅ —— 每一卷都可构建为 A0 海报，输出 SVG、PDF、PNG 三种格式（300 DPI）。

| 卷号 | 主题 | 状态 |
|------|-------------------------------|------|
| Vol.01 | AI 编年史（AI Evolution Timeline） | ✅ 已交付 |
| Vol.01B | AI 基础脉络（Foundations of AI） | ✅ 已交付 |
| Vol.02 | Transformer 帝国 | ✅ 已交付 |
| Vol.03 | 大语言模型时代 | ✅ 已交付 |
| Vol.04 | 多模态 AI | ✅ 已交付 |
| Vol.05 | 生成式 AI | ✅ 已交付 |
| Vol.06 | 强化学习 | ✅ 已交付 |
| Vol.07 | 计算机视觉 | ✅ 已交付 |
| Vol.08 | 具身 AI | ✅ 已交付 |
| Vol.09 | 自动驾驶 | ✅ 已交付 |
| Vol.10 | 世界模型 | ✅ 已交付 |
| Vol.11 | AI Agent | ✅ 已交付 |
| Vol.12 | AI 系统 | ✅ 已交付 |
| Vol.13 | 通往 AGI 之路 | ✅ 已交付 |

未来规划（尚未开始）：交互式网站与汇总全卷的 PDF 书籍——详见下方路线图。

---

# 🧠 知识优先

本仓库 **不是** 图片的集合。

而是一个结构化的 AI 知识库。

```
知识

↓

知识图谱

↓

图谱生成器

↓

SVG

↓

PDF

↓

PNG

↓

网站
```

所有图例均基于结构化知识生成，而非手工绘制。

---

# 🎨 设计原则

每一卷都遵循统一的出版物级设计语言。

- A0 海报版面
- SVG 矢量图形
- 300 DPI
- 统一色彩系统
- 统一字体排版
- 出版物级时间轴
- 统一的技术演进图谱

---

# 🏗 项目结构

```
Modern_AI_Atlas/

├── atlas/                      # 14 个图谱卷目录——每卷包含一个 knowledge_graph.json
│   ├── vol01_ai_evolution/     #   （驱动每张海报的结构化知识）
│   ├── vol01b_foundations_of_ai/
│   ├── vol02_transformer_empire/
│   └── ... vol03 … vol13       #   完整列表见上方「图谱结构」表格
│
├── generator/                  # Python 生成器包——五阶段流水线
│   ├── parser/                 # 阶段 1：安全加载并校验知识文件（JSON/YAML）
│   ├── graph/                  # 阶段 2：构建内存中的知识图谱
│   ├── layout/                 # 阶段 3：海报版面布局（panels 与 bands 两种模板）
│   ├── render/                 # 阶段 4：中英双语 SVG 渲染器（深色与浅色主题）
│   ├── exporter/               # 阶段 5：以 300 DPI 输出 SVG / PDF / PNG
│   └── build.py                # 编排五个阶段的 CLI 入口
│
├── assets/
│   ├── themes/                 # 色彩主题（empire_dark、atlas_light、default）
│   └── reference/              # 设计稿与参考海报（已被 gitignore）
│
├── docs/                       # 各卷内容规格说明 + 验收报告
├── tests/                      # 布局/渲染检查（纯 Python 可运行，兼容 pytest）
├── export/                     # 生成的海报：14 卷 × SVG/PDF/PNG（已被 gitignore）
├── rfcs/                       # 设计文档
└── requirements.txt            # cairosvg（PDF/PNG）+ pyyaml（YAML 知识文件）
```

## 各部分如何协作

每张海报都始于其卷目录下的一个 `knowledge_graph.json` 文件。生成器运行五阶段流水线——**parser → graph → layout → render → exporter**——将结构化知识转化为 A0 信息图海报，并以 300 DPI 输出 SVG、PDF、PNG 到 `export/` 目录。

已交付的系列共十四卷：**Vol.01** AI 编年史、**Vol.01B** AI 基础脉络、**Vol.02** Transformer 帝国、**Vol.03** 大语言模型时代、**Vol.04** 多模态 AI、**Vol.05** 生成式 AI、**Vol.06** 强化学习、**Vol.07** 计算机视觉、**Vol.08** 具身 AI、**Vol.09** 自动驾驶、**Vol.10** 世界模型、**Vol.11** AI Agent、**Vol.12** AI 系统、**Vol.13** 通往 AGI 之路。

## 快速开始

```bash
# 初始化（仅需一次）：创建虚拟环境并安装依赖
python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt   # PDF/PNG 导出还需原生 cairo：brew install cairo

# 以任意格式构建任意一卷（svg、pdf、png）
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol01_ai_evolution --format png
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol02_transformer_empire --format pdf
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol13_towards_agi --format svg
```

输出文件位于 `export/<卷名>.{svg,pdf,png}`。

---

# 🚀 路线图

## v0.1 ✅ 已交付

- 设计系统
- 完整的五阶段生成器流水线（300 DPI 输出 SVG → PDF → PNG）
- 全部 14 卷海报系列（见上方「图谱结构」）
- 内容保真验收：PASS（`docs/ACCEPTANCE_REPORT.md`）
- 视觉验收：GO（`docs/AESTHETIC_REVIEW.md`）

## v1.0（规划中）

- 完整 AI 图谱
- 交互式网站
- PDF 书籍
- SVG 合集

---

# 🤝 参与贡献

欢迎贡献。

无论你感兴趣的是

- AI 研究
- 图形设计
- 知识工程
- SVG 开发
- 文档编写

欢迎提交 Issue 或 Pull Request。

---

# ⭐ 理念

> 不要死记硬背 AI。
>
> 理解 AI 是如何演进的。

Modern AI Atlas 旨在帮助工程师构建对人工智能的完整心智地图。

---

<div align="center">

为 AI 社区倾心打造。

</div>
