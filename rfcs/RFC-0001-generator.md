# RFC-0001: Atlas Generator Architecture

- **Status**: Draft (partially implemented — parser and graph stages)
- **Author**: Modern AI Atlas maintainers
- **Created**: 2026-07-20
- **Related**: RFC-0002 (Knowledge Schema), RFC-0003 (Layout Engine)

---

## 1. Summary

The Atlas Generator is a Python pipeline that turns structured AI knowledge
definitions into publication-quality atlas volumes (A0 posters). The pipeline
is strictly data-driven: **no figure is drawn by hand**; every visual element
is derived from the knowledge graph.

```
Knowledge files ──▶ Parser ──▶ Graph ──▶ Layout ──▶ Render ──▶ Export
 (YAML / JSON)    (load)    (build)  (compute)   (draw)   (svg/pdf/png)
```

This RFC defines the pipeline architecture, stage contracts, and module
responsibilities. Detailed formats are specified in follow-up RFCs:

- **RFC-0002** — the knowledge file schema consumed by the Parser.
- **RFC-0003** — the layout algorithms used by the Layout stage.

## 2. Goals and Non-Goals

### Goals

- One command (`atlas-build`) builds one atlas volume end to end.
- Each pipeline stage is an independent, testable module with a typed
  input/output contract.
- The pipeline runs with **zero mandatory third-party dependencies**;
  YAML support is optional and activated when `pyyaml` is installed.
- All paths are centralized in `generator/config.py`; all tunables live in
  `generator/constants.py`.

### Non-Goals (for v0.1)

- Incremental/partial rebuilds and caching.
- Parallel builds of multiple volumes.
- A plugin system for custom renderers.
- The interactive website export (post-MVP).

## 3. Pipeline Stages

### Stage 1 — Parser (`generator/parser`)

Reads every knowledge file for an atlas volume and returns a validated,
normalized intermediate representation.

- **Input**: path to an atlas volume directory (e.g.
  `atlas/vol02_transformer_empire/`).
- **Output**: `KnowledgeData` — typed containers of node and edge records.
- **Rules**:
  - JSON is always supported; YAML (`.yaml` / `.yml`) requires the optional
    `pyyaml` dependency and is loaded exclusively via `yaml.safe_load`.
  - Structural validation happens here (required fields, unique node ids);
    referential validation (edge endpoints) belongs to the Graph stage.

### Stage 2 — Graph (`generator/graph`)

Builds the in-memory knowledge graph from parsed data.

- **Input**: `KnowledgeData` from the Parser.
- **Output**: `KnowledgeGraph` — nodes, edges, and query helpers
  (lookup by id, successors/predecessors, statistics).
- **Rules**:
  - Every edge endpoint must reference an existing node id; violations are
    hard errors, not warnings. A silently broken reference would produce a
    silently wrong poster.

### Stage 3 — Layout (`generator/layout`) — *planned*

Computes spatial positions for all nodes on the A0 canvas. See RFC-0003.

### Stage 4 — Render (`generator/render`) — *planned*

Draws the laid-out graph onto an SVG canvas using the design system
(colors, typography, grid) defined in `assets/themes/`.

### Stage 5 — Exporter (`generator/exporter`) — *planned*

Converts the rendered SVG into the requested output format(s): SVG (native),
PDF, PNG at `TARGET_DPI` (300).

## 4. CLI Contract

```
atlas-build <atlas_path> [--format {svg,pdf,png}] [--output PATH] [--verbose] [--version]
```

- `atlas_path` may be absolute or relative to the repository root.
- Default output: `export/<volume_name>.<fmt>`.
- Exit codes: `0` success, `1` user error (bad path, invalid knowledge
  files), `2` unexpected internal failure.

## 5. Error Handling Philosophy

- **Fail fast, fail loud.** A malformed knowledge file aborts the build with
  a message that names the file and the offending record.
- **No silent defaults for content.** Missing optional visual hints may fall
  back to the theme; missing knowledge data may not.
- Errors are reported through module-level `logging`, never bare `print`.

## 6. Testing Strategy

- Unit tests per stage under `tests/`, mirroring the `generator/` layout.
- Parser tests use small fixture files; Graph tests use in-memory
  `KnowledgeData`.
- Once Render lands: snapshot tests against reference SVGs.
- Minimum bar until then: `python3.12 -m py_compile` over the package and a
  successful end-to-end build of the sample volume.

## 7. Open Questions

1. Should one atlas volume support multiple knowledge files that get merged
   (e.g. `papers.json` + `relations.json`)? The Parser API accepts a
   directory to keep this option open.
2. Versioning of the knowledge schema (a `schema_version` field) — to be
   decided in RFC-0002.
