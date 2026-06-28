# AGENTS.md

This file is intended for AI coding agents working on the **Modern AI Atlas** repository. It describes the project as it currently exists, not as it is planned to become. Treat this as the ground-truth onboarding document.

---

## Project Overview

**Modern AI Atlas** is an open-source knowledge-engineering project that aims to organize the evolution of Artificial Intelligence into a unified, publication-quality visual knowledge graph. The end goal is a 13-volume atlas rendered as A0 posters (SVG → PDF → PNG) and eventually published as an interactive website and PDF book.

The repository currently contains the **project skeleton only**. The documentation (`README.md`, `README.zh-CN.md`, `CLAUDE.md`) describes the full vision, while the actual implementation is limited to a minimal Python generator scaffold under `generator/`.

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

Current milestone: **v0.1** — Design system, AI Evolution, Transformer Empire, SVG generator.

---

## Technology Stack

- **Language**: Python 3.12+
- **Project type**: Plain Python package (no build backend, no dependency manager yet)
- **Package layout**: `generator/` is the top-level Python package
- **No external dependencies** are declared at this time
  - No `pyproject.toml`, `requirements.txt`, `setup.py`, `setup.cfg`, `Pipfile`, `uv.lock`, etc.
  - No `package.json`, `Cargo.toml`, `Makefile`, or similar configuration files exist
- **Source code**: all code and docstrings are written in English
- **Documentation**: `README.md` and `CLAUDE.md` are in English; `README.zh-CN.md` is the Chinese translation

### Python Version Requirements

The code uses syntax that requires Python 3.10+ (union types with `|`, e.g. `Path | None`) and Python 3.12 is explicitly referenced in `.claude/settings.json` for compilation checks. Prefer running with **Python 3.12**.

---

## Repository Structure

The working directory is the project root. As of the latest commit, only these paths exist:

```
Modern_AI_Atlas/
├── .claude/
│   └── settings.json          # Claude Code permission allow-list
├── .git/                      # Git repository
├── generator/                 # Python generator package (skeleton)
│   ├── __init__.py
│   ├── build.py               # CLI entry point (pipeline orchestrator)
│   ├── config.py              # Centralized path configuration
│   ├── constants.py           # Project-wide constants
│   ├── exporter/
│   │   └── __init__.py        # Placeholder: SVG → PDF/PNG/...
│   ├── graph/
│   │   └── __init__.py        # Placeholder: in-memory knowledge graph
│   ├── layout/
│   │   └── __init__.py        # Placeholder: node spatial layout
│   ├── parser/
│   │   └── __init__.py        # Placeholder: YAML/JSON deserializer
│   ├── render/
│   │   └── __init__.py        # Placeholder: SVG drawing
│   └── utils/
│       └── __init__.py        # Placeholder: shared helpers
├── CLAUDE.md                  # High-level project guidance for Claude Code
├── README.md                  # English project overview
├── README.zh-CN.md            # Chinese project overview
└── AGENTS.md                  # This file
```

### Intended but Not-Yet-Existing Directories

The documentation and `generator/config.py` reference several directories that **do not exist yet**:

- `atlas/` — atlas volume definitions and layouts
- `knowledge/` — structured AI knowledge base (source of truth)
- `assets/` — static assets (themes, fonts, images)
  - `assets/themes/` is referenced in `config.py`
- `docs/` — documentation
- `export/` — output directory for generated files

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

Because `generator/` is a top-level package, you must ensure the repository root is on `PYTHONPATH`.

**Option A — run as a module (recommended):**

```bash
cd /Users/che.lin/Downloads/code/Modern_AI_Atlas
PYTHONPATH=$(pwd) python3.12 -m generator.build --help
PYTHONPATH=$(pwd) python3.12 -m generator.build atlas/vol02_transformer_empire --format svg
```

**Option B — run the script directly:**

```bash
cd /Users/che.lin/Downloads/code/Modern_AI_Atlas
PYTHONPATH=$(pwd) python3.12 generator/build.py --help
```

Running `python3.12 generator/build.py` without `PYTHONPATH` will fail with `ModuleNotFoundError: No module named 'generator'` because the parent directory is not on the module search path.

### Pipeline Stages (Planned)

`generator/build.py::build()` documents five stages, but they are currently commented out:

1. `parser.load(atlas_dir)` — read YAML/JSON knowledge files
2. `graph.build(parsed_data)` — construct in-memory knowledge graph
3. `layout.compute(graph)` — compute spatial node positions
4. `render.draw(layout)` — draw to SVG canvas
5. `exporter.export(render, fmt=fmt, output=output)` — convert to target format

The current implementation only resolves the atlas directory and logs pipeline metadata.

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

The `generator/` package is split into six functional subpackages. Each currently contains only an empty `__init__.py` with a docstring describing its intended responsibility:

| Module | Responsibility |
|--------|----------------|
| `generator.parser` | Deserialize knowledge definitions from structured files (YAML/JSON) |
| `generator.graph` | Build and query the in-memory knowledge graph |
| `generator.layout` | Compute spatial positioning for graph nodes on the atlas canvas |
| `generator.render` | Draw the atlas onto an SVG canvas using the computed layout |
| `generator.exporter` | Convert rendered SVG to PDF, PNG, and other output formats |
| `generator.utils` | Shared helpers for logging, file I/O, and validation |

### Style Conventions Observed So Far

- Use `from __future__ import annotations` at the top of every module
- Use type hints consistently
- Prefer `pathlib.Path` over string paths
- Use `logging` with module-level loggers
- Docstrings are written in English
- Module-level constants are uppercase; functions/methods are snake_case

---

## Testing Strategy

**There are no tests yet.** There is no `tests/`, `test_*.py`, or testing configuration (no `pytest.ini`, `tox.ini`, etc.).

When adding tests, the project maintainers will likely prefer:

- `pytest` as the test runner
- Tests placed under a top-level `tests/` directory mirroring the `generator/` package structure
- Unit tests for each pipeline stage: parser, graph, layout, render, exporter
- Snapshot or reference-image tests for SVG output once rendering is implemented

For now, the only verification step is to ensure modules compile:

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

- The generator will eventually parse YAML/JSON knowledge files. When implementing the parser, use safe-loading APIs (`yaml.safe_load`, `json.load`) and avoid `yaml.unsafe_load` or executing embedded code.
- The CLI accepts arbitrary `--output` paths. Validate that output paths are within the intended export area or explicitly allowed by the user.
- The `.claude/settings.json` file contains an allow-list of specific Bash commands. Do not modify it unless the new commands are safe and necessary.

---

## Deployment Process

No deployment process is defined yet. The repository is in a pre-MVP state. Future deployment artifacts are expected to include:

- Generated SVG/PDF/PNG files in `export/`
- A static website built from the atlas outputs
- A PDF book combining all volumes

Until the generator pipeline is implemented, there is nothing to deploy.

---

## Agent Reminders

- **Do not assume files or directories exist** that are described only in `README.md` or `CLAUDE.md`. Verify with `ls`/`Glob` before referencing them.
- **Prefer English** for code comments, docstrings, and agent-facing documentation, matching the existing source style.
- **Make minimal changes** to the skeleton; this project is intentionally small and each feature should be added incrementally.
- **Update this file** if you introduce new build tools, dependencies, tests, or deployment steps.
