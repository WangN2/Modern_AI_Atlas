# RFC-0001: Reusable SVG Poster System

- **Status:** Accepted for prototype
- **Project:** Modern AI Atlas
- **Scope:** SVG poster foundation
- **Target version:** v0.1
- **Last updated:** 2026-08-01

---

## 1. Summary

Modern AI Atlas currently contains first-round raster infographic drafts for 13 AI technology volumes.

These drafts are useful as visual references, but they have three important limitations:

1. text becomes blurry when enlarged;
2. layout cannot be reliably edited;
3. technical content cannot be maintained independently from the image.

This RFC proposes a reusable SVG poster system that separates structured poster content from rendering logic.

The first implementation will generate clean portrait and landscape SVG posters from YAML input.

---

## 2. Motivation

The project requires posters that are:

- readable at large scale;
- editable;
- reproducible;
- technically accurate;
- visually consistent;
- maintainable over several years.

Raster image generation cannot satisfy these requirements by itself.

SVG is selected because it provides:

- vector text and shapes;
- browser compatibility;
- Figma and Illustrator compatibility;
- deterministic generation;
- direct source control;
- support for later PDF and PNG export.

---

## 3. Goals

The prototype must provide:

1. A shared visual theme.
2. Portrait and landscape templates.
3. Structured YAML poster input.
4. Reusable SVG rendering components.
5. Editable Chinese and English text.
6. Deterministic output.
7. A CLI build command.
8. Minimal automated tests.
9. Two generated demo posters.

---

## 4. Non-Goals

The prototype will not provide:

- automatic knowledge-graph layout;
- full poster recreation for all volumes;
- citation generation;
- web scraping;
- Figma API integration;
- font embedding;
- advanced illustration generation;
- PDF or PNG export;
- interactive web posters.

These features may be proposed in later RFCs.

---

## 5. Architecture

```text
poster YAML
     │
     ▼
schema validation
     │
     ▼
theme loading
     │
     ▼
layout calculation
     │
     ▼
SVG component rendering
     │
     ▼
standalone SVG file
```

The prototype should remain simple.

Do not introduce a large framework unless the repository already depends on one.

---

## 6. Data Model

A poster input file should support the following conceptual structure:

```yaml
poster:
  volume: "Vol.02"
  title: "Transformer Foundations"
  title_zh: "Transformer 基础"
  subtitle: "The architecture that unified modern AI"
  orientation: "landscape"
  domain: "transformer"

sections:
  - id: timeline
    title: "Timeline"
    title_zh: "发展时间线"
    layout: "horizontal"
    cards:
      - title: "Transformer"
        year: 2017
        organization: "Google"
        description: "Attention becomes the core computation."

  - id: branches
    title: "Architecture Branches"
    title_zh: "架构分支"
    layout: "grid"
    cards:
      - title: "Encoder"
        description: "Bidirectional representation learning."
      - title: "Decoder"
        description: "Causal autoregressive generation."
      - title: "Encoder–Decoder"
        description: "Sequence-to-sequence transformation."
```

The implementation may use Python dataclasses or validated dictionaries.

Avoid coupling the initial schema to any one volume.

---

## 7. Theme Model

The theme file should define at least:

```yaml
canvas:
  landscape:
    width: 12000
    height: 6750
  portrait:
    width: 6750
    height: 12000

colors:
  background: "#F8FAFC"
  surface: "#FFFFFF"
  text_primary: "#0F172A"
  text_secondary: "#475569"
  border: "#CBD5E1"

domains:
  transformer: "#2563EB"
  llm: "#2563EB"
  vision: "#16A34A"
  generative: "#EA580C"
  reinforcement_learning: "#DC2626"
  multimodal: "#7C3AED"
  world_model: "#0891B2"
  embodied_ai: "#9333EA"
  autonomous_driving: "#D97706"
  agents: "#8B5CF6"
  systems: "#0F766E"
  agi: "#1D4ED8"

typography:
  family: >
    Inter, Noto Sans SC, Source Han Sans SC,
    Microsoft YaHei, sans-serif
  title: 120
  subtitle: 48
  section: 44
  card_title: 34
  body: 28
  caption: 22

spacing:
  outer_margin: 220
  section_gap: 80
  card_gap: 48
  card_padding: 48

radius:
  card: 28
  panel: 36
```

Values are design tokens and should not be duplicated throughout renderer code.

---

## 8. SVG Requirements

Generated SVG must:

- use a valid `viewBox`;
- be standalone;
- include UTF-8 XML content;
- use actual `<text>` nodes;
- avoid rasterized text;
- avoid external network dependencies;
- group semantic sections using `<g id="...">`;
- use reusable definitions where practical;
- escape XML characters safely;
- remain readable when opened directly in a browser.

Recommended document header:

```xml
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 12000 6750"
  role="img"
  aria-labelledby="poster-title poster-description"
>
```

The output should include accessible `<title>` and `<desc>` nodes.

---

## 9. Components

The initial renderer should provide conceptual components for:

### Poster frame

- background;
- outer margins;
- optional top accent line.

### Header

- project name;
- volume number;
- Chinese and English title;
- subtitle.

### Section panel

- section number;
- section title;
- optional description;
- child card region.

### Card

- card title;
- year or metadata;
- concise description;
- optional category accent.

### Connector

- simple straight or orthogonal line;
- optional arrow marker;
- semantic CSS class.

### Footer

- project name;
- version;
- volume position;
- next volume label.

Components may initially be renderer methods rather than classes.

---

## 10. Layout Strategy

The prototype uses deterministic grid layout.

It does not attempt automatic graph optimization.

### Landscape

Recommended structure:

```text
Header
────────────────────────────────────
Row 1: timeline or primary overview
────────────────────────────────────
Row 2: 2–4 large sections
────────────────────────────────────
Row 3: 2–4 supporting sections
────────────────────────────────────
Footer
```

### Portrait

Recommended structure:

```text
Header
──────────────
Timeline
──────────────
Section grid
──────────────
Section grid
──────────────
Summary
──────────────
Footer
```

Section positions may initially be explicitly defined by the input or calculated through a simple grid.

---

## 11. Typography

The renderer must not embed font binaries.

Use a font stack.

Chinese text must remain live SVG text.

Avoid font sizes that become unreadable at normal poster preview scale.

Use shorter descriptions rather than shrinking text to fit.

When content overflows:

1. wrap text;
2. increase card height;
3. reduce the amount of content;
4. report overflow if still unresolved.

Do not silently reduce text to tiny sizes.

---

## 12. Text Wrapping

SVG does not provide normal browser text wrapping for `<text>`.

The renderer should implement simple wrapping using `<tspan>` elements.

Example:

```xml
<text x="100" y="100">
  <tspan x="100" dy="0">第一行文字</tspan>
  <tspan x="100" dy="38">第二行文字</tspan>
</text>
```

The prototype may approximate text width based on character count.

A later RFC may introduce accurate font metrics.

---

## 13. File Structure

Recommended prototype:

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
```

If an equivalent existing structure is present, adapt rather than duplicate.

---

## 14. CLI

Required usage:

```bash
python -m generator.build \
  --input examples/poster_demo.yaml \
  --orientation landscape \
  --output export/demo/poster_demo_landscape.svg
```

Supported arguments:

```text
--input
--output
--orientation
--theme
--validate-only
--verbose
```

The prototype may default the theme to `themes/modern_ai_atlas.yaml`.

CLI errors must produce clear messages and non-zero exit codes.

---

## 15. Dependencies

Prefer minimal dependencies.

Recommended:

- Python 3.11 or newer
- PyYAML
- pytest for tests

Optional validation libraries should only be introduced when they clearly simplify the implementation.

Do not add a web framework.

---

## 16. Testing

Minimum tests:

### Theme loading

- valid theme loads;
- missing required theme key fails clearly;
- domain color lookup works.

### Poster parsing

- valid poster data loads;
- missing title fails;
- unsupported orientation fails.

### SVG rendering

- output begins with SVG markup;
- viewBox matches orientation;
- poster title appears in `<text>`;
- Chinese text remains present;
- no `<image>` element is generated by the demo renderer;
- output is deterministic.

---

## 17. Acceptance Criteria

RFC-0001 is successfully implemented when:

1. the CLI runs;
2. the demo YAML produces portrait and landscape SVG files;
3. generated SVG files open in a browser;
4. Chinese text is represented as SVG text;
5. the theme controls visual design;
6. unit tests pass;
7. output is deterministic;
8. implementation is documented;
9. no raster screenshot is used as the poster body.

---

## 18. Future RFCs

Potential follow-up work:

- RFC-0002: Knowledge schema
- RFC-0003: Poster layout engine
- RFC-0004: PNG and PDF export
- RFC-0005: Vol.01 SVG reconstruction
- RFC-0006: Vol.02 SVG reconstruction
- RFC-0007: Shared icon system
- RFC-0008: Interactive web atlas
- RFC-0009: Citation and source management

---

## 19. Implementation Instruction

Codex should implement the smallest clean system that satisfies this RFC.

Do not pre-implement future RFCs.

Do not redesign all 13 volumes during this task.

The output of this RFC is a reusable foundation and a demo, not the final atlas collection.