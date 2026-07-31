# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Modern AI Atlas organizes the evolution of AI into publication-quality A0 posters generated from structured data. 14 volumes (01–13 + 01b) span from AI Evolution to Towards AGI. The pipeline is: `Knowledge → Graph → Layout → Render → Export`.

## Tech Stack & Setup

- **Language**: Python 3.12+ (uses `X | None` union syntax)
- **Virtual env**: `.venv/` (gitignored) with `requirements.txt`
- **Dependencies**: `cairosvg>=2.7` (needs native cairo — `brew install cairo`), `pyyaml>=6.0` (optional; JSON works without it)
- **Setup**: `python3.12 -m venv .venv && .venv/bin/pip install -r requirements.txt`
- **No build backend** — `generator/` is a plain Python package at repo root

## Commands

### Run the generator

```bash
# Always set PYTHONPATH to repo root (generator/ is a top-level package)
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol02_transformer_empire
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol02_transformer_empire --format pdf
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol02_transformer_empire --format png

# SVG-only builds work without .venv (no third-party deps needed)
PYTHONPATH=$(pwd) python3.12 -m generator.build atlas/vol02_transformer_empire

# Help
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build --help
```

Running without `PYTHONPATH` fails with `ModuleNotFoundError: No module named 'generator'`.

### Build all volumes

```bash
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol01_ai_evolution --format svg
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol01b_foundations_of_ai --format svg
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol02_transformer_empire --format svg
# ... repeat for vol03–vol13
```

Or use a shell loop:
```bash
for vol in atlas/vol*/; do
  PYTHONPATH=$(pwd) .venv/bin/python -m generator.build "$vol" --format svg
done
```

### Run tests

```bash
.venv/bin/python tests/test_bands_layout.py
```

pytest is not installed yet; the test file is plain-python runnable and pytest-compatible.

### Compile-check modules

```bash
python3.12 -m py_compile generator/build.py generator/config.py generator/constants.py
```

## Pipeline Architecture (5 stages, all implemented)

`generator/build.py::build()` orchestrates:

1. **Parser** (`generator/parser/`) — `loader.load(atlas_dir) -> KnowledgeData`: safe-loads JSON/YAML knowledge files, validates required fields, returns `NodeRecord`/`EdgeRecord` tuples. Extra sections (meta, families, rails, etc.) pass through as `KnowledgeData.extras`.
2. **Graph** (`generator/graph/`) — `builder.build(KnowledgeData) -> KnowledgeGraph`: constructs immutable directed graph, validates edge endpoints exist (hard error on dangling refs). Provides query helpers: `node()`, `successors()`, `predecessors()`, `stats()`.
3. **Layout** (`generator/layout/`) — `engine.compute(graph, theme, knowledge) -> LayoutResult`: dispatches on `meta.layout`. Two templates:
   - `"panels"` (default) — Vol.02-style grid: header, why/hero/papers row, family panels, rail panels, fusion, timeline, bottom row, footer
   - `"bands"` — generic stacked sections: numbered era bands with cards/side panels, mainline, insights, NEXT teaser; supports portrait (1682×2524) and landscape (2524×1682)
4. **Render** (`generator/render/`) — `svg.draw(layout, theme, knowledge) -> str`: produces standalone SVG infographic poster. Dark theme (`empire_dark`) and light theme (`atlas_light`). Bilingual (zh/en). Dispatches panel rendering between `svg.py` (panels template) and `bands.py` (bands template).
5. **Exporter** (`generator/exporter/`) — `convert.export(svg, fmt, output, volume_name) -> Path`: SVG written directly; PDF/PNG via cairosvg at 300 DPI. Missing cairo raises `ExportError` with install instructions.

### Knowledge file structure

Each atlas volume directory (e.g., `atlas/vol02_transformer_empire/`) contains a `knowledge_graph.json` (or `.yaml`/`.yml`) with:

- `nodes` — `id` + `label` required; optional: `kind`, `year`, `summary`, `tags`
- `edges` — `source` + `target` required; `relation` should be `inherits`/`converges`/`composes`
- `meta` — `layout` (template selection), `theme`, `canvas` (width/height/margin/gap)
- Poster sections (passed through as `KnowledgeData.extras`): `features`, `hero`, `key_papers`, `families`, `rails`, `sections`, `mainline`, `insights`, `next`, etc.

### Key configuration

- `generator/config.py` — all paths derived from `ROOT_DIR` (repo root)
- `generator/constants.py` — `PROJECT_NAME`, `VERSION` ("0.1.0"), `TARGET_DPI` (300), `DEFAULT_THEME` ("empire_dark"), canvas dimensions, layout template names
- Themes in `assets/themes/` — `empire_dark.json` (dark theme for Vol.01–02), `atlas_light.json` (light series theme for Vol.01b, 03–13)
- Volume images in `atlas/*/images/` — embedded image assets (author photos, architecture diagrams, etc.) referenced by knowledge graph nodes

## Key Reference Docs

- `docs/AI圣经_修订版.md` — content plan: 4-layer pyramid, 14-volume structure, relation semantics
- `docs/ACCEPTANCE_REPORT.md` / `ACCEPTANCE_REPORT.zh-CN.md` — final verification report for all 14 volumes
- `docs/CONTENT_ACCURACY_REVIEW.md` — content accuracy audit per volume
- `docs/PROPORTION_REDESIGN.md` — layout proportion redesign notes
- `rfcs/RFC-0001-generator.md` — pipeline architecture spec
- `rfcs/RFC-0002-knowledge-schema.md` — knowledge schema (next up)
- `rfcs/RFC-0003-layout-engine.md` — layout engine spec (planned)

## Code Conventions

- `from __future__ import annotations` at the top of every module
- Type hints consistently; union types with `|` (Python 3.10+)
- `pathlib.Path` over string paths
- `logging` with module-level loggers (never `print`)
- Docstrings in English; code and comments also in English
- Module-level constants UPPERCASE; functions/methods snake_case
- Frozen dataclasses for data models (`Node`, `Edge`, `Panel`, `LayoutResult`, etc.)

## Relation Semantics (from docs/AI圣经_修订版.md)

- **inherits** (solid) — 直接继承
- **converges** (dashed) — 趋同/受启发 (e.g., ViT ↔ Swin, BERT ↔ RoBERTa)
- **composes** (dotted) — 组合/拼接 (e.g., CLIP = ViT + GPT)

Never draw an inheritance edge the content plan marks as convergent.

## 14-Volume Structure

| Vol | Name (zh) | Name (en) | Theme |
|-----|-----------|-----------|-------|
| 01 | AI 编年史 | AI Evolution Timeline | empire_dark |
| 01b | 人工智能基础 | Foundations of AI | atlas_light |
| 02 | Transformer 帝国 | Transformer Empire | empire_dark |
| 03 | 大语言模型时代 | The LLM Era | atlas_light |
| 04 | 多模态 AI | Multimodal AI | atlas_light |
| 05 | 生成式 AI | Generative AI | atlas_light |
| 06 | 强化学习 | Reinforcement Learning | atlas_light |
| 07 | 计算机视觉 | Computer Vision | atlas_light |
| 08 | 具身智能 | Embodied AI | atlas_light |
| 09 | 自动驾驶 | Autonomous Driving | atlas_light |
| 10 | 世界模型 | World Models | atlas_light |
| 11 | 智能体 | AI Agents | atlas_light |
| 12 | AI 系统 | AI Systems | atlas_light |
| 13 | 迈向 AGI | Towards AGI | atlas_light |

Vol.01 (dark, historical overview) and Vol.02 (dark, flagship) use `empire_dark`; all others use `atlas_light` (light "Modern AI Atlas" series). Vol.03, 10–13 are landscape (2524×1682); the rest are portrait (1682×2524).

## Design System

- A0 poster layout, SVG vector graphics at 300 DPI
- Unified color system and typography across all volumes
- All volumes now use the `bands` template (stacked sections with era bands, cards, mainline, insights, NEXT teaser)
- Portrait 2:3 (1682×2524) for Vol.01–02, 04–09; landscape 3:2 (2524×1682) for Vol.03, 10–13
- Dark theme (empire_dark) for Vol.01–02; light theme (atlas_light) for Vol.01b, 03–13

## Roadmap

- **v0.1** — Design system, 14-volume atlas, SVG/PDF/PNG generator (complete)
- **v0.2** — Knowledge schema formalization (RFC-0002), author/logo asset pipeline, layout engine docs (RFC-0003)
- **v0.3** — Interactive website, PDF book, SVG collection
- **v1.0** — Complete atlas with community contributions

## Error Handling

- Fail fast, fail loud — malformed knowledge aborts with file+record details
- Custom exceptions: `KnowledgeLoadError`, `GraphBuildError`, `ExportError`
- No silent defaults for knowledge content; optional visual hints may fall back to theme
