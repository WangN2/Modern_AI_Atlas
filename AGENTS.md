# AGENTS.md

This file is intended for AI coding agents working on the **Modern AI Atlas** repository. It describes the project as it currently exists, not as it is planned to become. Treat this as the ground-truth onboarding document.

---

## Project Overview

**Modern AI Atlas** is an open-source knowledge-engineering project that aims to organize the evolution of Artificial Intelligence into a unified, publication-quality visual knowledge graph. The end goal is a 13-volume atlas rendered as A0 posters (SVG → PDF → PNG) and eventually published as an interactive website and PDF book.

The generator pipeline is fully implemented and the **complete 14-volume poster series** (`atlas/vol01*` … `atlas/vol13*`) builds end-to-end in SVG/PDF/PNG at 300 DPI. Content-fidelity acceptance (`docs/ACCEPTANCE_REPORT.md`, two rounds) and visual acceptance (`docs/AESTHETIC_REVIEW.md`, three rounds, final verdict **GO**) are complete. The documentation (`README.md`, `README.zh-CN.md`, `CLAUDE.md`) still describes the broader vision (interactive website, PDF book), which remains future work.

### Core Philosophy

- **Knowledge first**: every figure is generated from structured data, not drawn by hand.
- **Pipeline**: `Knowledge → Knowledge Graph → Atlas Generator → SVG → PDF → PNG → Website`.
- **Publication quality**: A0 layout, SVG vector graphics, 300 DPI, unified color system and typography.

### 13-Volume Roadmap

| Volume | Topic | Volume | Topic |
|--------|-------|--------|-------|
| 01 | AI Evolution | 08 | Multimodal & VLA |
| 02 | Transformer Empire | 09 | Autonomous Driving |
| 03 | Large Language Models | 10 | SLAM & Spatial AI |
| 04 | Vision Foundation Models | 11 | Embodied AI |
| 05 | Generative AI | 12 | AI Agents |
| 06 | Reinforcement Learning | 13 | Modern AI Atlas (synthesis) |
| 07 | World Models | | |

Note: the delivered series in `atlas/` + `docs/specs/` re-titled the later volumes and added one — the actual 14 directories are `vol01_ai_evolution`, `vol01b_foundations_of_ai`, `vol02_transformer_empire`, `vol03_llm_era`, `vol04_multimodal_ai`, `vol05_generative_ai`, `vol06_reinforcement_learning`, `vol07_computer_vision`, `vol08_embodied_ai`, `vol09_autonomous_driving`, `vol10_world_models`, `vol11_ai_agents`, `vol12_ai_systems`, `vol13_towards_agi`.

Current status: **v0.1 delivered** — design system + full generator pipeline + all 14 volumes building in SVG/PDF/PNG at 300 DPI; visual acceptance **GO** (see `docs/AESTHETIC_REVIEW.md`, Round 3).

---

## Technology Stack

- **Language**: Python 3.12+
- **Project type**: Plain Python package (no build backend, no dependency manager yet)
- **Package layout**: `generator/` is the top-level Python package
- **Dependencies**: declared in `requirements.txt`, installed into the project virtual environment `.venv/` (gitignored)
  - `cairosvg>=2.7` — PDF/PNG export backend; requires the native cairo library (`brew install cairo`)
  - `pyyaml>=6.0` — YAML knowledge files in the parser (loaded via `yaml.safe_load` only); JSON works without it
  - Setup: `python3.12 -m venv .venv && .venv/bin/pip install -r requirements.txt`
  - Note: the sandboxed `python3.12` cannot discover Homebrew's `libcairo` by name; `generator/exporter/convert.py` points `ctypes.util.find_library` at its absolute path before importing cairosvg
- **Source code**: all code and docstrings are written in English
- **Documentation**: `README.md` and `CLAUDE.md` are in English; `README.zh-CN.md` is the Chinese translation

### Python Version Requirements

The code uses syntax that requires Python 3.10+ (union types with `|`, e.g. `Path | None`) and Python 3.12 is explicitly referenced in `.claude/settings.json` for compilation checks. Prefer running with **Python 3.12**.

---

## Repository Structure

The working directory is the project root. The following paths exist:

```
Modern_AI_Atlas/
├── .claude/
│   └── settings.json          # Claude Code permission allow-list
├── .git/                      # Git repository
├── assets/
│   ├── reference/
│   │   ├── vol02_mockup.png   # Vol.02 design mockup (visual target)
│   │   └── volumes/           # 14 GPT-generated reference posters + series overview (read-only)
│   └── themes/
│       ├── default.json       # Original light theme (superseded)
│       ├── empire_dark.json   # Dark theme (NVIDIA GTC style; Vol.01, 02)
│       └── atlas_light.json   # Light "Modern AI Atlas" series theme (Vol.01b, 03-13)
├── atlas/                     # Atlas volume definitions (14 volumes; each has knowledge_graph.json)
│   ├── vol01_ai_evolution/    # Vol.01 AI 编年史: bands, dark, portrait; images/ with 36 card photos
│   ├── vol01b_foundations_of_ai/  # Vol.01b 基础脉络: bands, light, portrait
│   ├── vol02_transformer_empire/  # Vol.02: panels template, dark, portrait
│   ├── vol03_llm_era/         # Vol.03 LLM 时代: bands, light, LANDSCAPE
│   ├── vol04_multimodal_ai/   # Vol.04 多模态 AI: bands, light, portrait
│   ├── vol05_generative_ai/
│   ├── vol06_reinforcement_learning/
│   ├── vol07_computer_vision/
│   ├── vol08_embodied_ai/
│   ├── vol09_autonomous_driving/
│   ├── vol10_world_models/    # Vol.10-13: bands, light, LANDSCAPE
│   ├── vol11_ai_agents/
│   ├── vol12_ai_systems/
│   └── vol13_towards_agi/
├── docs/
│   ├── AI圣经_修订版.md        # Content plan: 4-layer pyramid, 8 volumes, relation semantics
│   ├── specs/                 # 14 per-volume content specs (vol01..vol13 + vol01b)
│   ├── ACCEPTANCE_REPORT.md   # Content-fidelity acceptance (2 rounds; all 14 PASS)
│   ├── ACCEPTANCE_REPORT.zh-CN.md
│   └── AESTHETIC_REVIEW.md    # Visual acceptance (3 rounds; Round 3 verdict GO)
├── generator/                 # Python generator package
│   ├── __init__.py
│   ├── build.py               # CLI entry point (pipeline orchestrator)
│   ├── config.py              # Centralized path configuration
│   ├── constants.py           # Project-wide constants
│   ├── exporter/              # Implemented: Stage 5 — output writer (SVG/PDF/PNG)
│   │   ├── __init__.py        # Re-exports: export, ExportError
│   │   └── convert.py         # exporter.export(): SVG direct; PDF/PNG via cairosvg (300 DPI)
│   ├── graph/                 # Implemented: Stage 2 — knowledge graph
│   │   ├── __init__.py        # Re-exports: build, KnowledgeGraph, Node, Edge
│   │   ├── builder.py         # graph.build(): validation + construction
│   │   └── models.py          # Node, Edge, KnowledgeGraph (query helpers)
│   ├── layout/                # Implemented: Stage 3 — poster layout
│   │   ├── __init__.py        # Re-exports: compute, LayoutResult, LayoutNode, Lane
│   │   ├── engine.py          # layout.compute(): dispatches on meta.layout
│   │   └── bands.py           # Generic band-sections template (portrait + landscape)
│   ├── parser/                # Implemented: Stage 1 — knowledge loader
│   │   ├── __init__.py        # Re-exports: load, KnowledgeData, records
│   │   └── loader.py          # parser.load(): safe JSON/YAML loading + validation
│   ├── render/                # Implemented: Stage 4 — SVG renderer
│   │   ├── __init__.py        # Re-exports: draw, load_theme, kind_style
│   │   ├── svg.py             # render.draw(): Vol.02 panels + bands dispatch
│   │   ├── bands.py           # Band-sections renderer (header, cards, mainline, NEXT)
│   │   ├── helpers.py         # Shared SVG text helpers (fmt/trunc/fit/wrap/text)
│   │   ├── images.py          # Raster image embedding (base64 data URIs, ImageEmbedder)
│   │   └── theme.py           # Theme loading with built-in fallback
│   └── utils/
│       └── __init__.py        # Placeholder: shared helpers
├── export/                    # Generated output (gitignored artifacts)
│   └── vol*.{svg,pdf,png}     # 14 volumes × 3 formats (full series)
├── rfcs/                      # Design documents
│   ├── RFC-0001-generator.md  # Pipeline architecture (drafted)
│   ├── RFC-0002-knowledge-schema.md  # Knowledge schema (empty, next up)
│   └── RFC-0003-layout-engine.md     # Layout engine (empty)
├── tests/
│   └── test_bands_layout.py   # 6 checks: bands template + canvas sizing (plain-python
│                              # runnable, pytest-compatible; pytest not installed yet)
├── PROJECT_STATUS.md          # Sprint / milestone tracker
├── CLAUDE.md                  # High-level project guidance for Claude Code
├── README.md                  # English project overview
├── README.zh-CN.md            # Chinese project overview
└── AGENTS.md                  # This file
```

### Directories Referenced but Not Yet Created

The documentation and `generator/config.py` reference these directories that **do not exist yet**:

- `knowledge/` — structured AI knowledge base (source of truth)

(`atlas/`, `assets/`, `docs/`, and `export/` now exist.)

When implementing features, create these directories as needed and keep paths in sync with `generator/config.py`.

---

## Build and Runtime Architecture

### Entry Point

The CLI is implemented in `generator/build.py`.

```python
# generator/build.py
main(argv: Sequence[str] | None = None) -> None
```

It exposes the command `atlas-build` with the following interface:

```text
usage: atlas-build [-h] [--format {svg,pdf,png}] [--output OUTPUT] [--verbose]
                   [--version]
                   atlas_path
```

Examples from the docstring:

```bash
python build.py atlas/vol02_transformer_empire
python build.py atlas/vol02_transformer_empire --format pdf
```

### Running the Generator

Because `generator/` is a top-level package, you must ensure the repository root is on `PYTHONPATH`. Use the project virtual environment (`.venv/`) so that PDF/PNG export and YAML support are available:

**Option A — run as a module (recommended):**

```bash
cd /Users/che.lin/Downloads/code/Modern_AI_Atlas
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build --help
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol02_transformer_empire --format svg
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol02_transformer_empire --format pdf
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build atlas/vol02_transformer_empire --format png
```

**Option B — run the script directly:**

```bash
cd /Users/che.lin/Downloads/code/Modern_AI_Atlas
PYTHONPATH=$(pwd) .venv/bin/python generator/build.py --help
```

Running `python generator/build.py` without `PYTHONPATH` will fail with `ModuleNotFoundError: No module named 'generator'` because the parent directory is not on the module search path. Plain `python3.12` (without `.venv`) still works for SVG/JSON-only builds, since those have no third-party dependencies.

### Pipeline Stages

`generator/build.py::build()` orchestrates five stages; all are wired up:

1. `parser.load(atlas_dir)` — read YAML/JSON knowledge files ✅
2. `graph.build(knowledge)` — construct in-memory knowledge graph ✅
3. `layout.compute(graph, theme, knowledge=...)` — poster layout ✅
4. `render.draw(layout, theme, knowledge)` — infographic SVG poster ✅
5. `exporter.export(svg, fmt=fmt, ...)` — write output: SVG direct ✅, PDF/PNG via cairosvg ✅ (300 DPI)

The knowledge file's `meta` section selects the poster template and theme:

- `meta.layout`: `"panels"` (default; Vol.02 panel-template grid) or
  `"bands"` (generic stacked band sections — see `generator/layout/bands.py`)
- `meta.theme`: theme name under `assets/themes/` (default `empire_dark`;
  `atlas_light` is the light series theme for Vol.01b/03-13)
- `meta.canvas`: `{width, height, margin, gap}` — portrait 2:3 volumes use
  1682×2524; landscape 3:2 volumes (Vol.03, 10-13) use 2524×1682
  (`constants.CANVAS_WIDTH_LANDSCAPE` / `CANVAS_HEIGHT_LANDSCAPE`). The
  canvas height is content-driven: the configured value acts as a minimum,
  taller content extends the canvas, and when content is shorter the S1
  fit-to-canvas pass expands the inter-band gaps so the footer band lands
  flush at the bottom margin (no dead void below the footer).
- Raster image embedding: band-section cards may carry an `image` key with
  a path relative to the atlas volume directory (plus optional
  `image_focus`: `top` / `center` / `bottom` crop anchor). Stage 4's
  `generator/render/images.py` (`ImageEmbedder`) sniffs mime type and
  natural pixel size with pure-python header parsing (no Pillow) and embeds
  the file as a base64 data URI so the SVG stays self-contained; it
  replaces the card's line schematic, which remains as fallback. Paths are
  confined to the atlas directory (absolute paths and `..` are rejected).

Running the CLI against `atlas/vol02_transformer_empire` produces
`export/vol02_transformer_empire.{svg,pdf,png}` — a portrait poster
(1682×2650 viewBox, 841×1325 mm) in the dark "empire_dark" theme, matching
the design mockup at `assets/reference/vol02_mockup.png`. Running it against
`atlas/vol01_ai_evolution` produces the Vol.01 AI 编年史 poster (bands
template, dark theme, 6 numbered era bands + mainline timeline + NEXT
teaser), matching `assets/reference/volumes/0.AI编年史.png`.

### Design References

- `assets/reference/vol02_mockup.png` — the visual target for Vol.02 (dark
  NVIDIA GTC style, curated infographic panels)
- `assets/reference/volumes/` — 14 GPT-generated reference posters (one per
  volume, e.g. `0.AI编年史.png`, `2.Transformer帝国.png`) plus a series
  overview (`十三卷彩图纵览.png`); read-only visual targets. Each volume's
  authoritative content spec lives in `docs/specs/<volume>.md`.
- `docs/AI圣经_修订版.md` — the project's content plan: 4-layer pyramid
  (基础架构 → 多模态 → 能力层 → 应用), 8 volumes, and the **relation
  semantics** that must be respected: 直接继承 (inherits, solid), 趋同
  (converges, dashed — e.g. ViT ↔ Swin, BERT ↔ RoBERTa), 组合 (composes,
  dotted — e.g. CLIP = ViT ＋ GPT). Never draw an inheritance edge the plan
  marks as convergent.

### Key Configuration

- `generator/config.py` — derives all paths from `ROOT_DIR` (repository root)
- `generator/constants.py` — project name, version, output specs, file extensions
  - `PROJECT_NAME = "Modern AI Atlas Generator"`
  - `VERSION = "0.1.0"`
  - `TARGET_DPI = 300`
  - `DEFAULT_FORMAT = "A0"`
  - `KNOWLEDGE_GRAPH_FILE = "knowledge_graph"`

---

## Code Organization and Module Divisions

The `generator/` package is split into six functional subpackages. Only `utils` remains a placeholder:

| Module | Status | Responsibility |
|--------|--------|----------------|
| `generator.parser` | ✅ implemented | Safe-load and validate knowledge definitions (JSON; YAML via `pyyaml` + `yaml.safe_load`). Entry: `parser.load(atlas_dir) -> KnowledgeData`; errors raise `KnowledgeLoadError`. Extra top-level sections (meta, families, rails, ...) pass through as `KnowledgeData.extras` |
| `generator.graph` | ✅ implemented | Build and query the in-memory knowledge graph. Entry: `graph.build(KnowledgeData) -> KnowledgeGraph`; dangling edge endpoints raise `GraphBuildError` |
| `generator.layout` | ✅ implemented | Two poster templates dispatched on `meta.layout`: Vol.02 panel-template grid (`engine.py`: header, why/hero/papers row, family panels, rail panels, fusion band, timeline band, bottom row, footer) and the generic band-sections template (`bands.py`: numbered/titled/circled-numeral bands with side panels + card rows, mainline band, insights, NEXT teaser; portrait + landscape via `meta.canvas`). Panel heights derive from content. Entry: `layout.compute(KnowledgeGraph, theme, knowledge=...) -> LayoutResult` |
| `generator.render` | ✅ implemented | Infographic SVG renderer (bilingual zh/en), dark + light themes. `svg.py`: Vol.02 panel renderers + dispatch of bands-template panels to `bands.py` (band headers with number chips, model cards with year chips + schematic diagram placeholders, legend row, mainline timeline, insights, NEXT teaser). `helpers.py`: shared text helpers (wrap/fit/measure, CJK-aware). `images.py`: raster image embedding (`ImageEmbedder`, base64 data URIs, path confinement). Entry: `render.draw(LayoutResult, theme, knowledge) -> str`; themes via `render.load_theme(name)` with built-in fallback |
| `generator.exporter` | ✅ implemented | Write rendered output in all three formats: SVG direct; PDF/PNG via cairosvg at 300 DPI (native cairo required). Entry: `exporter.export(svg, fmt=..., ...) -> Path`; missing backends raise `ExportError` with install instructions |
| `generator.utils` | placeholder | Shared helpers for logging, file I/O, and validation |

A knowledge file (`knowledge_graph.json` / `.yaml` / `.yml` inside an atlas volume directory) has two parts:

1. **Graph sections** (validated): `nodes` (`id` + `label` required) and `edges` (`source` + `target` required; `relation` should be one of `inherits` / `converges` / `composes` per the relation semantics above).
2. **Poster sections** (passed through as `KnowledgeData.extras`, schema to be formalized in RFC-0002):
   - panels template (`meta.layout` absent): `meta`, `features`, `hero`, `key_papers`, `families`, `rails`, `fusion`, `innovations`, `industry`, `changes`, `future`. See `atlas/vol02_transformer_empire/knowledge_graph.json` for the reference instance.
   - bands template (`meta.layout = "bands"`): `meta` (+ `layout` / `theme` / `canvas`), `legend` (icon chips), `sections` (band list: `number` + `number_style` (`chip` / `circle`; omit `number` for a plain titled band), `title`, `years`, `subtitle`, `color`, optional `left_panel` / `right_panel` (`{title, items}`), `cards` (`{year, title, title_en, org, desc, desc2, citation, diagram, node}`; `diagram` is a schematic placeholder kind: `board` / `grid` / `net` / `flow` / `curve` / `margin` / `stack` / `encoder` / `residual` / `attention` / `photo`; a card may instead carry `image` — a raster file relative to the atlas volume dir — plus optional `image_focus` (`top` / `center` / `bottom`), embedded via `generator/render/images.py`)), `mainline` (`{title, stages, axis, drivers}`), `insights`, `quote`, `next`. Sections beyond plain bands support a `kind` library (`list` / `cards` / `table` / `pills` / `chevrons` / `timeline` / `fusion` / `family` / `hero`) and `{"row": [...]}` / `{"stack": [...]}` grid grouping. See `atlas/vol01_ai_evolution/knowledge_graph.json` for the reference instance and `docs/specs/` for the per-volume content specs.

### Style Conventions Observed So Far

- Use `from __future__ import annotations` at the top of every module
- Use type hints consistently
- Prefer `pathlib.Path` over string paths
- Use `logging` with module-level loggers
- Docstrings are written in English
- Module-level constants are uppercase; functions/methods are snake_case

---

## Testing Strategy

There is one test file so far: `tests/test_bands_layout.py` — **6 checks**
covering the bands template and canvas sizing:

1. panels template stays the default without `meta.layout`
2. portrait 2:3 `meta.canvas` yields a portrait bands poster
3. landscape 3:2 `meta.canvas` yields a landscape bands poster + SVG smoke render
4. `atlas_light` theme key parity with `empire_dark`
5. renderer dispatch is disjoint (panels keys never reach the bands renderer)
6. row edge cases (empty rows skipped, zero weights cannot divide by zero)

Run it with:

```bash
cd /Users/che.lin/Downloads/code/Modern_AI_Atlas
.venv/bin/python tests/test_bands_layout.py   # prints "6 check(s) passed."
```

It is plain-python runnable and pytest-compatible. pytest is **not installed
yet** in `.venv`. When adding more tests, the project maintainers will likely
prefer:

- `pytest` as the test runner
- Tests placed under a top-level `tests/` directory mirroring the `generator/` package structure
- Unit tests for each pipeline stage: parser, graph, layout, render, exporter
- Snapshot or reference-image tests for SVG output once rendering is implemented

A compile check also works as a quick smoke test:

```bash
cd /Users/che.lin/Downloads/code/Modern_AI_Atlas
python3.12 -m py_compile generator/build.py generator/config.py generator/constants.py
```

---

## Development Workflow

1. Keep paths centralized in `generator/config.py`.
2. Keep constants in `generator/constants.py`.
3. Implement each pipeline stage in its own subpackage under `generator/`.
4. Update `generator/build.py` to wire up stages as they become available.
5. Create `atlas/`, `knowledge/`, `assets/`, `docs/`, and `export/` directories as the content pipeline grows.
6. Add `requirements.txt` or `pyproject.toml` once external dependencies (e.g. `pyyaml`, `cairosvg`, `svglib`, `reportlab`, `Pillow`) are introduced.

---

## Security Considerations

- The generator parses YAML/JSON knowledge files via safe-loading APIs (`yaml.safe_load`, `json.load`); keep it that way — never `yaml.unsafe_load` or executing embedded code. Raster images referenced by card `image` keys are confined to the atlas volume directory by `generator/render/images.py` (absolute paths and `..` segments are rejected).
- The CLI accepts arbitrary `--output` paths. Validate that output paths are within the intended export area or explicitly allowed by the user.
- The `.claude/settings.json` file contains an allow-list of specific Bash commands. Do not modify it unless the new commands are safe and necessary.

---

## Deployment Process

No deployment process is defined yet. The full 14-volume series already exists
as generated artifacts in `export/` (SVG/PDF/PNG at 300 DPI, gitignored).
Future deployment artifacts are expected to include:

- A static website built from the atlas outputs
- A PDF book combining all volumes

---

## Agent Reminders

- **Do not assume files or directories exist** that are described only in `README.md` or `CLAUDE.md`. Verify with `ls`/`Glob` before referencing them.
- **Prefer English** for code comments, docstrings, and agent-facing documentation, matching the existing source style.
- **Make minimal changes** to the skeleton; this project is intentionally small and each feature should be added incrementally.
- **Update this file** if you introduce new build tools, dependencies, tests, or deployment steps.
