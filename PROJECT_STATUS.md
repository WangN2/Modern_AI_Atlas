# Modern AI Atlas Project Status

## Current Sprint

RFC-0001 gap closure + flagship volume polish

## Current Milestone

Stabilize the reusable SVG poster system on top of the existing 14-volume generator, then turn Vol.01, Vol.01B, and Vol.02 into flagship-quality reference volumes.

Status:

`IN PROGRESS` — v0.1 generator delivery exists, but project governance and flagship visual quality are being raised to the new ChatGPT/Codex workflow.

---

## Current Branch

`main`

## Latest Commit

`f5e618d Document SVG poster system task baseline`

Note: local commits may need pushing after this status update.

---

## Active Task

`.ai/CURRENT_TASK.md`

- Task ID: `TASK-0001`
- Title: `Initialize the reusable SVG poster system`
- Status: `Ready`
- Owner: `Codex`
- Architect: `ChatGPT`

Interpretation for this repository:

The repository already has a working generator and 14 atlas volume directories. Therefore TASK-0001 should be executed as a gap-closure and standardization pass, not as a from-scratch rewrite.

---

## Completed

- [x] Repository initialized
- [x] README / README.zh-CN / CLAUDE.md
- [x] Project architecture and design-system direction
- [x] RFC-0001 Generator Architecture (`rfcs/RFC-0001-generator.md`)
- [x] RFC-0001 SVG Poster System accepted for prototype (`rfcs/RFC-0001-svg-poster-system.md`)
- [x] Current task record created (`.ai/CURRENT_TASK.md`)
- [x] Agent workflow and guardrails updated (`AGENTS.md`)
- [x] Python generator package under `generator/`
- [x] Safe JSON/YAML parser
- [x] Knowledge graph builder
- [x] Layout engine with panels and bands templates
- [x] SVG renderer with editable text and reusable section renderers
- [x] Theme loading from `assets/themes/`
- [x] SVG / PDF / PNG exporter through `generator.exporter`
- [x] Vol.01 image-rich chronicle restored as `The Story of AI`
- [x] Vol.01B foundations poster improved with denser content and refined header/legend
- [x] Vol.02 transformed into a landscape Transformer knowledge map
- [x] 14 per-volume specs and atlas knowledge files
- [x] `tests/test_bands_layout.py`
- [x] `tests/test_volume_quality.py`

---

## In Progress

- [ ] RFC-0001 gap report and acceptance mapping
- [ ] PROJECT_STATUS alignment with the current workflow
- [ ] Vol.01B flagship polish pass
- [ ] SVG-first iteration workflow: generate SVG by default; generate PNG/PDF only when explicitly requested or needed for temporary QA

---

## Next

1. Finish `docs/RFC-0001_GAP_REPORT.md`.
2. Add or adapt demo artifacts if RFC-0001 requires a standalone demo path.
3. Decide whether to support the RFC sample CLI (`--input examples/poster_demo.yaml`) or document the existing atlas-directory CLI as the accepted adjustment.
4. Continue Vol.01B visual/content polish.
5. Use Vol.01, Vol.01B, and Vol.02 as the design-quality baseline for Vol.03-Vol.13.

---

## RFC-0001 Implementation Notes

The accepted RFC describes a clean prototype:

```text
poster YAML -> theme loading -> layout -> SVG rendering -> standalone SVG
```

The existing implementation already covers the core architecture, but with adjusted repository locations:

- Theme files live in `assets/themes/`, not top-level `themes/`.
- Poster data lives in `atlas/<volume>/knowledge_graph.json`, not `examples/poster_demo.yaml`.
- Rendering is split under `generator/parser`, `generator/graph`, `generator/layout`, `generator/render`, and `generator/exporter`, not a single `svg_renderer.py`.
- The CLI currently accepts an atlas volume directory, not `--input`.
- Demo output is represented by real atlas outputs under `export/`, not `export/demo/`.

These are acceptable if documented and tested, because they reflect the current repository architecture.

---

## Known Issues

1. `rfcs/RFC-0001-svg-poster-system.md` still describes a 13-volume first-round raster stage, while the repository now has 14 generated atlas directories.
2. TASK-0001 deliverables include top-level `themes/`, `templates/`, `examples/`, and `export/demo/`; equivalent functionality currently lives in existing directories.
3. Current CLI does not support the exact RFC sample command with `--input`.
4. Vol.01B is improved but still needs another design pass for hierarchy, density, and premium visual finish.
5. Some generated PNG/PDF files may lag behind SVG during the new SVG-first review workflow.

---

## Quality Gates

Before marking a volume or system task complete:

- Run relevant tests.
- Generate the required SVG artifact.
- Confirm Chinese text remains live SVG text.
- Confirm no full-poster raster screenshot is embedded as the final poster body.
- Report generated paths and known limitations.

---

## Team Model

- `gpt_项目 / Bernoulli`: overall coordination, milestone tracking, acceptance review.
- `gpt_产品 / Peirce`: format, layout, art direction, and visual polish.
- `gpt_技术 / Ampere`: AI technical accuracy, lineage semantics, and content completeness.
- `gpt_开发`: implementation in the generator, themes, and atlas data.
- `gpt_测试`: validation plan, regression checks, and issue feedback.
