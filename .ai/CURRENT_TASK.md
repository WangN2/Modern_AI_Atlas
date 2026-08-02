# Current Task

## Task ID

TASK-0001

## Title

Initialize the reusable SVG poster system

## Status

Ready

## Owner

Codex

## Architect

ChatGPT

## Objective

Create the first reusable SVG poster foundation for Modern AI Atlas.

The goal is not to complete all 13 volumes in this task.

The goal is to create a clean, reusable base that can later support every volume.

---

## Required Context

Read these files before implementation:

1. `AGENTS.md`
2. `PROJECT_STATUS.md`
3. `rfcs/RFC-0001-svg-poster-system.md`
4. Existing repository structure
5. Existing Markdown content for Vol.01 and Vol.02, if present

---

## Deliverables

Create:

```text
themes/
└── modern_ai_atlas.yaml

templates/
├── poster_landscape.svg
└── poster_portrait.svg

generator/
├── __init__.py
├── build.py
├── config.py
├── models.py
├── theme_loader.py
└── svg_renderer.py

examples/
└── poster_demo.yaml

tests/
├── test_theme_loader.py
└── test_svg_renderer.py

export/
└── demo/
    ├── poster_demo_landscape.svg
    └── poster_demo_portrait.svg
```

The exact structure may be adjusted only when the existing repository already has an equivalent location. Explain any adjustment.

---

## Functional Requirements

The prototype must support:

- portrait and landscape SVG canvases;
- configurable title and subtitle;
- volume number;
- section cards;
- domain colors loaded from a theme file;
- editable SVG text;
- reusable background, header, footer, card, and connector components;
- deterministic output;
- UTF-8 Chinese text;
- valid standalone SVG output.

---

## Non-Goals

Do not implement:

- automatic graph layout;
- PDF export;
- PNG export;
- Figma export;
- all 13 volumes;
- complex icon libraries;
- automatic paper citation retrieval;
- remote web access.

---

## CLI

Provide a command similar to:

```bash
python -m generator.build \
  --input examples/poster_demo.yaml \
  --orientation landscape \
  --output export/demo/poster_demo_landscape.svg
```

And:

```bash
python -m generator.build \
  --input examples/poster_demo.yaml \
  --orientation portrait \
  --output export/demo/poster_demo_portrait.svg
```

If the repository already uses a package manager or CLI framework, integrate with it rather than duplicating it.

---

## Validation

Before completion:

1. Run unit tests.
2. Generate both demo SVG files.
3. Confirm that SVG text is editable.
4. Confirm that Chinese characters appear as `<text>` content.
5. Confirm that generated SVG files do not contain embedded raster screenshots.
6. Report the commands and results.

---

## Completion Report

Return a concise report containing:

- implementation summary;
- files added or changed;
- test commands;
- test results;
- generated artifacts;
- known limitations;
- suggested next task.
