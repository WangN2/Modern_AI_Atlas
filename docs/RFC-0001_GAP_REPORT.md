# RFC-0001 Gap Report

## Summary

`rfcs/RFC-0001-svg-poster-system.md` is accepted as the reusable SVG poster system prototype. The repository, however, already contains a more advanced generator than the RFC's original from-scratch target.

This report maps RFC-0001 requirements onto the current implementation and defines the remaining closure work.

## Current Verdict

Status: `PARTIALLY SATISFIED`

The core poster system exists and is already used by the atlas volumes, but the exact RFC demo structure and CLI shape are not fully implemented.

## Repository Adjustments

The RFC suggests:

```text
themes/
templates/
examples/
generator/models.py
generator/theme_loader.py
generator/svg_renderer.py
export/demo/
```

The existing repository uses equivalent, more mature locations:

| RFC location | Existing location | Decision |
|---|---|---|
| `themes/modern_ai_atlas.yaml` | `assets/themes/*.json` | Accept existing theme directory; optional YAML demo can be added later. |
| `templates/poster_*.svg` | `generator/render/*.py` component renderers | Accept code-rendered templates; add template docs only if needed. |
| `examples/poster_demo.yaml` | `atlas/<volume>/knowledge_graph.json` | Gap remains if the exact RFC demo is required. |
| `generator/models.py` | `generator/graph/models.py`, parser records | Accept split modules. |
| `generator/theme_loader.py` | `generator/render/theme.py` | Accept existing module. |
| `generator/svg_renderer.py` | `generator/render/svg.py`, `generator/render/bands.py` | Accept existing split renderer. |
| `export/demo/*.svg` | `export/vol*.svg` | Gap remains if demo artifacts are required. |

## Functional Requirement Mapping

| Requirement | Status | Evidence / Notes |
|---|---|---|
| Portrait and landscape SVG canvases | Satisfied | `meta.canvas`; bands template supports portrait and landscape. |
| Configurable title and subtitle | Satisfied | `meta.title_zh`, `meta.title_en`, `meta.title_sub`, banner/callout fields. |
| Volume number | Satisfied | `meta.volume`. |
| Section cards | Satisfied | `sections` payload supports cards, tables, timelines, figures, radial maps, etc. |
| Domain colors from theme file | Satisfied | `assets/themes/*.json`; loaded by `generator/render/theme.py`. |
| Editable SVG text | Satisfied | Renderer emits `<text>` / `<tspan>` via `generator/render/helpers.py`. |
| Reusable background/header/footer/card/connector components | Satisfied | Implemented as renderer helpers and section renderers. |
| Deterministic output | Mostly satisfied | Outputs are deterministic for the same source data and theme. |
| UTF-8 Chinese text | Satisfied | Atlas data and SVG output include Chinese text directly. |
| Valid standalone SVG output | Satisfied | SVG embeds referenced raster card images as data URIs where needed; no external network dependency. |

## Non-Goal Mapping

| Non-goal | Current status |
|---|---|
| Automatic graph layout | Not implemented; current layouts are template/data driven. |
| PDF export | Implemented already, but not required for RFC-0001. Current SVG-first workflow should avoid PDF unless requested. |
| PNG export | Implemented already, but not required for RFC-0001. Use only for temporary QA or explicit delivery. |
| Figma export | Not implemented. |
| All 13 volumes | Repository has 14 volume directories, but RFC-0001 closure should not redesign all volumes. |
| Complex icon libraries | Not used; renderer uses simple SVG primitives. |
| Automatic paper citation retrieval | Not implemented. |
| Remote web access | Not required. |

## CLI Mapping

RFC target:

```bash
python -m generator.build \
  --input examples/poster_demo.yaml \
  --orientation landscape \
  --output export/demo/poster_demo_landscape.svg
```

Current CLI:

```bash
PYTHONPATH=$(pwd) .venv/bin/python -m generator.build \
  atlas/vol01b_foundations_of_ai \
  --format svg
```

Status: `GAP`

Decision needed:

1. Add compatibility flags `--input` and `--orientation` for RFC demo files.
2. Or formally accept atlas-directory input as the project CLI and document the adjustment.

Recommendation: accept the existing atlas-directory CLI for production, then add a small demo adapter only if ChatGPT requires exact RFC-0001 acceptance.

## Test Mapping

Existing tests:

- `tests/test_bands_layout.py`
- `tests/test_volume_quality.py`

RFC suggested tests:

- `tests/test_theme_loader.py`
- `tests/test_svg_renderer.py`

Status: `PARTIAL GAP`

Recommendation:

- Keep existing tests.
- Add focused tests for theme loading, editable SVG text, no full-poster raster screenshot, and deterministic SVG output.

## Acceptance Criteria Mapping

| Acceptance criterion | Status |
|---|---|
| CLI runs | Satisfied for existing atlas CLI. |
| Demo YAML produces portrait/landscape SVG files | Gap. |
| SVG files open in browser | Satisfied for atlas outputs. |
| Chinese text represented as SVG text | Satisfied; add explicit test. |
| Theme controls visual design | Satisfied. |
| Unit tests pass | Existing tests pass historically; rerun before closure. |
| Output deterministic | Likely satisfied; add explicit test. |
| Implementation documented | Partial; this gap report documents adjustments. |
| No raster screenshot used as poster body | Satisfied by renderer architecture; raster card images are allowed content assets, not full-poster screenshots. |

## Closure Plan

1. Run current focused tests.
2. Add explicit SVG editability/no-screenshot/determinism tests.
3. Decide whether to add RFC demo files or document the existing atlas directory CLI as the accepted equivalent.
4. Generate Vol.01B SVG as the current flagship demo artifact.
5. Update `.ai/CURRENT_TASK.md` from `Ready` to `In Progress` or `Done` only after the owner approves the interpretation.

## Known Limitations

- RFC-0001 text still references 13 volumes; the repository currently has 14 atlas directories including Vol.01B.
- The exact demo file tree is not present.
- The current generator can export PDF/PNG, but the active review workflow is SVG-first.
- Some existing generated PNG/PDF files may not reflect the latest SVG-only edits.

## Suggested Next Task

Continue with Vol.01B flagship polish after RFC-0001 closure decisions are accepted.
