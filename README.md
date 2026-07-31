<div align="center">

# 🌍 Modern AI Atlas

### The Complete Knowledge Graph of Artificial Intelligence

*A publication-quality, continuously evolving atlas of modern AI technologies.*

[![License](https://img.shields.io/badge/license-MIT-blue.svg)]()
[![Status](https://img.shields.io/badge/status-Under%20Development-orange)]()
[![Version](https://img.shields.io/badge/version-v0.1-green)]()

</div>

---

# 📖 What is Modern AI Atlas?

Modern AI Atlas is an open-source project that systematically organizes the evolution of Artificial Intelligence into a unified knowledge graph.

Unlike traditional tutorials or scattered blog posts, this project presents AI as an interconnected world, where every major technology has its own history, lineage, and influence.

The goal is to build the most complete visual knowledge atlas for modern AI.

---

# 🎯 Vision

Artificial Intelligence is no longer a collection of isolated technologies.

Today, Large Language Models, Computer Vision, Reinforcement Learning, Diffusion Models, Autonomous Driving, Robotics and Embodied AI are all converging toward a unified architecture.

Modern AI Atlas aims to answer questions such as:

- Where did GPT come from?
- Why did ViT replace CNN?
- How is DiT related to Stable Diffusion?
- Why is JEPA considered a World Model?
- How are Robotics and Autonomous Driving becoming unified?
- What is the evolutionary path toward AGI?

---

# 🗺 Atlas Structure

The project is organized into a publication-quality poster series. **All 14 volumes are delivered** ✅ — each one builds as an A0 poster in SVG, PDF, and PNG at 300 DPI.

| Volume | Topic | Status |
|----------|-------------------------------|--------|
| Vol.01 | AI Evolution Timeline (AI 编年史) | ✅ delivered |
| Vol.01B | Foundations of AI | ✅ delivered |
| Vol.02 | Transformer Empire | ✅ delivered |
| Vol.03 | The LLM Era | ✅ delivered |
| Vol.04 | Multimodal AI | ✅ delivered |
| Vol.05 | Generative AI | ✅ delivered |
| Vol.06 | Reinforcement Learning | ✅ delivered |
| Vol.07 | Computer Vision | ✅ delivered |
| Vol.08 | Embodied AI | ✅ delivered |
| Vol.09 | Autonomous Driving | ✅ delivered |
| Vol.10 | World Models | ✅ delivered |
| Vol.11 | AI Agents | ✅ delivered |
| Vol.12 | AI Systems | ✅ delivered |
| Vol.13 | The Road to AGI | ✅ delivered |

Future plans (not yet started): an interactive website and a PDF book combining all volumes — see the Roadmap below.

---

# 🧠 Knowledge First

This repository is **not** a collection of images.

Instead, it is a structured AI knowledge base.

```
Knowledge

↓

Knowledge Graph

↓

Atlas Generator

↓

SVG

↓

PDF

↓

PNG

↓

Website
```

All figures are generated from structured knowledge rather than manually drawn.

---

# 🎨 Design Principles

Every volume follows the same publication-quality design language.

- A0 Poster Layout
- SVG Vector Graphics
- 300 DPI
- Unified Color System
- Unified Typography
- Publication-quality Timeline
- Consistent Technical Evolution Maps

---

# 🏗 Project Structure

```
Modern_AI_Atlas/

├── atlas/                      # 14 atlas volumes — each holds a knowledge_graph.json
│   ├── vol01_ai_evolution/     #   (the structured knowledge that drives each poster)
│   ├── vol01b_foundations_of_ai/
│   ├── vol02_transformer_empire/
│   └── ... vol03 … vol13       #   full list in the Atlas Structure table above
│
├── generator/                  # Python generator package — 5-stage pipeline
│   ├── parser/                 # Stage 1: safe-load + validate knowledge files (JSON/YAML)
│   ├── graph/                  # Stage 2: build the in-memory knowledge graph
│   ├── layout/                 # Stage 3: poster layout (panels & bands templates)
│   ├── render/                 # Stage 4: bilingual SVG renderer (dark & light themes)
│   ├── exporter/               # Stage 5: write SVG / PDF / PNG at 300 DPI
│   └── build.py                # CLI entry point orchestrating the five stages
│
├── assets/
│   ├── themes/                 # Color themes (empire_dark, atlas_light, default)
│   └── reference/              # Design mockups & reference posters (gitignored)
│
├── docs/                       # Per-volume content specs + acceptance reports
├── tests/                      # Layout/renderer checks (plain-python, pytest-compatible)
├── export/                     # Generated posters: 14 volumes × SVG/PDF/PNG (gitignored)
├── rfcs/                       # Design documents
└── requirements.txt            # cairosvg (PDF/PNG) + pyyaml (YAML knowledge files)
```

## How It Fits Together

Every poster starts as a `knowledge_graph.json` inside its volume directory under `atlas/`. The generator runs a five-stage pipeline — **parser → graph → layout → render → exporter** — that turns that structured knowledge into an A0 infographic poster, exported as SVG, PDF, and PNG at 300 DPI into `export/`.

The delivered series covers fourteen volumes: **Vol.01** AI Evolution Timeline (AI 编年史), **Vol.01B** Foundations of AI, **Vol.02** Transformer Empire, **Vol.03** The LLM Era, **Vol.04** Multimodal AI, **Vol.05** Generative AI, **Vol.06** Reinforcement Learning, **Vol.07** Computer Vision, **Vol.08** Embodied AI, **Vol.09** Autonomous Driving, **Vol.10** World Models, **Vol.11** AI Agents, **Vol.12** AI Systems, and **Vol.13** The Road to AGI.

## Quick Start

```bash
# Setup (once): create the virtual environment and install dependencies
python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt   # PDF/PNG export also needs native cairo: brew install cairo

# Build any volume in any format (svg, pdf, png)
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol01_ai_evolution --format png
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol02_transformer_empire --format pdf
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol13_towards_agi --format svg
```

Output lands in `export/<volume>.{svg,pdf,png}`.

---

# 🚀 Roadmap

## v0.1 ✅ Delivered

- Design System
- Full 5-stage generator pipeline (SVG → PDF → PNG at 300 DPI)
- Complete 14-volume poster series (see Atlas Structure above)
- Content-fidelity acceptance: PASS (`docs/ACCEPTANCE_REPORT.md`)
- Visual acceptance: GO (`docs/AESTHETIC_REVIEW.md`)

## v1.0 (planned)

- Complete AI Atlas
- Interactive Website
- PDF Book
- SVG Collection

---

# 🤝 Contributing

Contributions are welcome.

Whether you are interested in

- AI Research
- Graphics Design
- Knowledge Engineering
- SVG Development
- Documentation

feel free to submit issues or pull requests.

---

# ⭐ Philosophy

> Don't memorize AI.
>
> Understand how AI evolved.

Modern AI Atlas is designed to help engineers build a complete mental map of Artificial Intelligence.

---

<div align="center">

Made with ❤️ for the AI Community.

</div>