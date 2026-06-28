# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Modern AI Atlas is an open-source knowledge engineering project that organizes the evolution of AI into a unified, publication-quality visual knowledge graph. It covers 13 volumes spanning from AI evolution to embodied AI and agents.

## Pipeline (Knowledge First)

All figures are generated from structured data, not manually drawn:

```
Knowledge → Knowledge Graph → Atlas Generator → SVG → PDF → PNG → Website
```

- `knowledge/` — structured AI knowledge base (the source of truth)
- `atlas/` — atlas definitions and layouts
- `generator/` — SVG/PDF/PNG generation pipeline
- `assets/` — static assets
- `docs/` — documentation
- `export/` — output directory for generated files

## 13-Volume Structure

| Vol | Topic | Vol | Topic |
|-----|-------|-----|-------|
| 01 | AI Evolution | 08 | Multimodal & VLA |
| 02 | Transformer Empire | 09 | Autonomous Driving |
| 03 | Large Language Models | 10 | SLAM & Spatial AI |
| 04 | Vision Foundation Models | 11 | Embodied AI |
| 05 | Generative AI | 12 | AI Agents |
| 06 | Reinforcement Learning | 13 | Modern AI Atlas (synthesis) |
| 07 | World Models | | |

## Design System

Every volume follows the same publication-quality design language:
- A0 poster layout with SVG vector graphics at 300 DPI
- Unified color system and typography
- Publication-quality timelines and consistent technical evolution maps

## Roadmap

- **v0.1** — Design system, AI Evolution, Transformer Empire, SVG generator
- **v0.2** — Vision Foundation, Diffusion, Reinforcement Learning
- **v0.3** — World Models, Embodied AI, Autonomous Driving
- **v1.0** — Complete atlas, interactive website, PDF book, SVG collection
