# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Modern AI Atlas organizes the evolution of AI into publication-quality A0 posters generated from structured data. 13 volumes span from AI Evolution to Embodied AI & Agents. The pipeline is: `Knowledge → Graph → Layout → Render → Export`.

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
- Themes in `assets/themes/` — `empire_dark.json` (active dark theme), `atlas_light.json` (light series theme for Vol.01b/03-13)

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

- A0 poster layout, SVG vector graphics at 300 DPI
- Unified color system and typography across all volumes
- Two poster templates: panel grid (Vol.02) and stacked bands (generic, all other volumes)
- Portrait 2:3 (1682×2524) for most volumes; landscape 3:2 (2524×1682) for Vol.03, 10-13

## Roadmap

- **v0.1** — Design system, AI Evolution, Transformer Empire, SVG generator (current)
- **v0.2** — Vision Foundation, Diffusion, Reinforcement Learning
- **v0.3** — World Models, Embodied AI, Autonomous Driving
- **v1.0** — Complete atlas, interactive website, PDF book, SVG collection

## Error Handling

- Fail fast, fail loud — malformed knowledge aborts with file+record details
- Custom exceptions: `KnowledgeLoadError`, `GraphBuildError`, `ExportError`
- No silent defaults for knowledge content; optional visual hints may fall back to theme
