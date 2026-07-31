"""Generic stacked band-sections layout (the ``bands`` poster template).

Where ``generator.layout.engine`` implements the original Vol.02 panel grid,
this module implements the generic template shared by the other atlas
volumes. Since the S2 design-system unification every volume shares ONE
skeleton (theme colors may vary, the skeleton may not):

    header (series line + volume chip / zh title + en subtitle / tagline /
            right quote block)
    legend row (whenever a legend exists — always directly under the header)
    sections — each top-level entry is either:
        * a full-width section (era band, table, pill rows, timeline,
          chevrons, fusion band, cards grid, list panel, ...), or
        * {"row": [cell, ...]} — cells placed side by side (optional
          per-cell "weight"; a cell may be {"stack": [...]} to stack
          several sections inside one grid cell), or
        * {"stack": [...]} — same, as a full-width column
    mainline band + insights row (optional)
    footer row: dark navy band (series line + closing quote) + NEXT teaser
        on every volume except the final one

Section ``kind`` values (default ``band``) drive both height computation
here and rendering in ``generator.render.bands``. All content comes from
``KnowledgeData.extras``; the canvas size is driven by ``meta.canvas`` so
the same template serves portrait 2:3 and landscape 3:2 volumes. The canvas
height is content-driven with ``meta.canvas.height`` acting as a minimum.
"""

from __future__ import annotations

import logging
import math
from dataclasses import replace
from typing import Any

from generator import constants
from generator.graph.models import KnowledgeGraph
from generator.layout.engine import LayoutResult, Panel
from generator.parser.loader import KnowledgeData
from generator.render.helpers import (
    cards_panel_card_height,
    family_desc_lines,
    family_label_lines,
    list_row_height,
    pills_line_breaks,
)

logger = logging.getLogger(__name__)

# Default geometry (theme canvas keys may override via `band_*` entries).
# S2 design-system skeleton: ONE header zone height and ONE footer pattern
# for every volume, regardless of theme.
HEADER_H = 150.0
LEGEND_H = 64.0
BAND_HEADER_H = 64.0
BAND_SIDE_W = 190.0
BAND_CARD_H = 250.0
SIDE_ROW_H = 30.0
MAINLINE_H = 205.0
INSIGHTS_H = 100.0
NEXT_W = 300.0
FOOTER_BAND_H = 100.0
PANEL_HEADER_H = 56.0


def _canvas_geometry(meta: dict[str, Any], theme: dict[str, Any]) -> dict[str, float]:
    """Resolve canvas width/height/margin/gap from meta, theme, constants."""
    theme_canvas = theme.get("canvas", {})
    meta_canvas = meta.get("canvas", {})
    return {
        "width": float(meta_canvas.get(
            "width", theme_canvas.get("width", constants.CANVAS_WIDTH))),
        "height": float(meta_canvas.get(
            "height", theme_canvas.get("height", constants.CANVAS_HEIGHT))),
        "margin": float(meta_canvas.get(
            "margin", theme_canvas.get("margin", 40))),
        "gap": float(meta_canvas.get(
            "gap", theme_canvas.get("gap", 16))),
    }


def _band_height(section: dict[str, Any], canvas: dict[str, Any]) -> float:
    """Derive one era band's height from its content (cards + side lists)."""
    header_h = float(canvas.get("band_header_h", BAND_HEADER_H))
    card_h = float(canvas.get("band_card_h", BAND_CARD_H))
    side_h = 0.0
    for side_key in ("left_panel", "right_panel"):
        side = section.get(side_key)
        if side:
            side_h = max(side_h, 40 + SIDE_ROW_H * len(side.get("items", [])))
    content_h = max(card_h if section.get("cards") else 0.0, side_h)
    return header_h + content_h + 16


def _kind_height(section: dict[str, Any], canvas: dict[str, Any],
                 width: float) -> float:
    """Derive a section's height from its kind, content, and cell width.

    ``width`` is the section's prospective cell width: text-heavy kinds
    (list / cards / family) wrap long labels instead of ellipsizing them,
    so their heights depend on how wide the panel will be. The geometry
    formulas are shared with the renderer via generator.render.helpers.
    """
    kind = section.get("kind", "band")
    header = float(canvas.get("panel_header_h2", PANEL_HEADER_H))
    if kind == "band":
        return _band_height(section, canvas)
    if kind == "list":
        items = section.get("items", [])
        cols = max(int(section.get("columns", 1)), 1)
        col_w = (width - 40 - (cols - 1) * 20) / cols
        row_h = list_row_height(items, col_w)
        rows = math.ceil(len(items) / cols)
        return header + rows * row_h + (36 if section.get("summary") else 0) + 14
    if kind == "cards":
        items = section.get("items", [])
        cols = max(int(section.get("columns", 3)), 1)
        card_w = (width - 32 - (cols - 1) * 10) / cols
        card_h = cards_panel_card_height(items, card_w)
        return header + math.ceil(len(items) / cols) * (card_h + 10) + 10
    if kind == "table":
        return header + (1 + len(section.get("rows", []))) * 30 + 14
    if kind == "pills":
        col_header = 30.0 if section.get("col_header") else 0.0
        label_w = float(section.get("label_w", 150))
        rows_h = sum(42 + 36 * (len(pills_line_breaks(
            row.get("pills", []), width, label_w)) - 1)
            for row in section.get("rows", []))
        return header + col_header + rows_h + 12
    if kind == "chevrons":
        # The floating globe illustration was removed (S8); bands are always
        # a single chevron row tall.
        return header + 76.0
    if kind == "timeline":
        return header + 132
    if kind == "fusion":
        return header + 150
    if kind == "family":
        compact = bool(section.get("compact"))
        rows = 0.0
        for model in section.get("models", []):
            label = (f"{model.get('name', '')} ({model.get('org', '')})"
                     if model.get("org") else model.get("name", ""))
            extra_h = 16 * (len(family_label_lines(
                label, width, with_year=bool(model.get("year")))) - 1)
            if model.get("desc"):
                desc_h = 14 * (len(family_desc_lines(
                    model["desc"], width)) - 1)
                rows += (36 if compact else 52) + extra_h + desc_h
            else:
                rows += (26 if compact else 30) + extra_h
        footer = section.get("footer", [])
        diagram = 88.0 if section.get("diagram") else 0.0
        footer_h = 26 * len(footer) + 14 if footer else 10
        return header + diagram + rows + footer_h
    if kind == "hero":
        return 64 + 196 + 76
    if kind == "papers":
        return header + len(section.get("papers", [])) * 68 + 10
    if kind == "industry":
        groups = section.get("groups", [])
        max_items = max((len(g.get("items", [])) for g in groups), default=0)
        return header + 34 + max_items * 30 + 14
    if kind == "pyramid":
        return header + len(section.get("levels", [])) * 46 + 34
    if kind == "wheel":
        strip = 60.0 if section.get("strip") else 0.0
        return header + 272 + strip + 12
    if kind == "radial":
        return header + 320
    if kind == "figures":
        return header + len(section.get("figures", [])) * 68 + 10
    if kind == "curve":
        return header + 258
    if kind == "arch":
        layers = len(section.get("layers", []))
        parts = 40 + layers * 36 + 90
        if section.get("token_table"):
            parts += 104
        if section.get("align_flow"):
            parts += 76
        if section.get("abilities"):
            parts += 88
        return header + parts
    if kind == "quote":
        return FOOTER_BAND_H
    logger.warning("Unknown section kind %r; using fallback height", kind)
    return 140.0


def compute_bands(
    graph: KnowledgeGraph,
    theme: dict[str, Any],
    knowledge: KnowledgeData,
) -> LayoutResult:
    """Compute panel positions for the generic band-sections template.

    Args:
        graph: The knowledge graph built by Stage 2 (used for statistics).
        theme: Theme dictionary (dark or light; both share the key layout).
        knowledge: Parsed knowledge data; poster content is read from
            ``knowledge.extras`` (meta, legend, sections, mainline,
            insights, quote, next, footer).

    Returns:
        A LayoutResult with all positioned panels.
    """
    extras = knowledge.extras
    meta = extras.get("meta", {})
    # Per-volume geometry overrides: meta.canvas may tune width/height/
    # margin/gap (see _canvas_geometry) and any band_* sizing key.
    canvas = {**theme.get("canvas", {}),
              **{k: v for k, v in meta.get("canvas", {}).items()}}
    geo = _canvas_geometry(meta, theme)
    width, min_height = geo["width"], geo["height"]
    margin, gap = geo["margin"], geo["gap"]
    usable = width - 2 * margin

    panels: list[Panel] = []
    y = margin

    # -- header (unified skeleton: series+chip / zh title / en sub / quote) --
    panels.append(Panel("bands_header", margin, y, usable, HEADER_H,
                        payload={"meta": meta,
                                 "legend": extras.get("legend")}))
    y += HEADER_H + gap

    # -- legend row (always directly under the header when a legend exists) --
    legend = extras.get("legend", [])
    if legend:
        panels.append(Panel("legend", margin, y, usable, LEGEND_H,
                            payload={"items": legend}))
        y += LEGEND_H + gap

    # -- sections (full width, row groups, stack groups) ----------------------
    side_w = float(canvas.get("band_side_w", BAND_SIDE_W))
    index = 0

    def emit(section: dict[str, Any], sx: float, sy: float,
             sw: float, sh: float) -> None:
        nonlocal index
        payload = {**section, "side_w": side_w}
        panels.append(Panel(f"section:{index}", sx, sy, sw, sh,
                            color=section.get("color", ""), payload=payload))
        index += 1

    def cell_height(cell: dict[str, Any], cw: float) -> float:
        if "stack" in cell:
            members = cell["stack"]
            return (sum(_kind_height(m, canvas, cw) for m in members)
                    + gap * max(len(members) - 1, 0))
        return _kind_height(cell, canvas, cw)

    for item in extras.get("sections", []):
        if "row" in item or "stack" in item:
            cells = item.get("row", [item])
            if not cells:
                logger.warning("Empty row/stack section skipped: %r", item)
                continue
            weights = [float(c.get("weight", 1.0)) for c in cells]
            total_w = sum(weights) or 1.0
            avail = usable - gap * (len(cells) - 1)
            # Cell widths depend only on weights, so resolve them first:
            # content-driven heights (list/cards/family wrap long text)
            # are then computed against each cell's real width.
            cws = [avail * wgt / total_w for wgt in weights]
            row_h = max(cell_height(c, cw) for c, cw in zip(cells, cws))
            cx = margin
            for cell, cw in zip(cells, cws):
                if "stack" in cell:
                    members = cell["stack"]
                    heights = [_kind_height(m, canvas, cw) for m in members]
                    # Distribute leftover row height evenly across members so
                    # a short stack fills its cell instead of hugging the top.
                    natural = sum(heights) + gap * max(len(members) - 1, 0)
                    extra = (row_h - natural) / len(members)
                    if extra > 0:
                        heights = [h + extra for h in heights]
                    sy = y
                    for member, mh in zip(members, heights):
                        emit(member, cx, sy, cw, mh)
                        sy += mh + gap
                else:
                    emit(cell, cx, y, cw, row_h)
                cx += cw + gap
            y += row_h + gap
        else:
            h = _kind_height(item, canvas, usable)
            emit(item, margin, y, usable, h)
            y += h + gap

    # -- mainline band + insights row -----------------------------------------
    mainline = extras.get("mainline")
    insights = extras.get("insights", [])
    next_teaser = extras.get("next")
    if mainline or insights:
        # Driver-only mainlines (no stages/axis) get a slimmer band.
        band_h = (MAINLINE_H if (mainline.get("stages") or mainline.get("axis"))
                  else 150.0) if mainline else 0.0
        insights_h = INSIGHTS_H if insights else 0.0
        stack_h = band_h + (gap + insights_h if band_h and insights_h
                            else 0.0)
        if not mainline:
            stack_h = insights_h
        if mainline:
            panels.append(Panel("mainline", margin, y, usable, band_h,
                                payload=mainline))
        if insights_h:
            panels.append(Panel("insights", margin, y + band_h + gap,
                                usable, insights_h,
                                payload={"items": insights}))
        y += stack_h + gap

    # -- footer row (S2): dark quote band + NEXT teaser on every volume -------
    # Every volume gets the dark navy footer band; the NEXT teaser sits at
    # its right on all volumes except the final one (Vol.13 keeps its Grand
    # Summary mainline and a full-width footer instead).
    footer = extras.get("footer") or {}
    quote_text = footer.get("quote_zh") or extras.get("quote", "")
    footer_payload = {**footer, "meta": meta, "quote_zh": quote_text}
    if next_teaser:
        panels.append(Panel("footer_band", margin, y,
                            usable - NEXT_W - gap, FOOTER_BAND_H,
                            payload=footer_payload))
        panels.append(Panel("next", margin + usable - NEXT_W, y,
                            NEXT_W, FOOTER_BAND_H, payload=next_teaser))
    else:
        panels.append(Panel("footer_band", margin, y, usable, FOOTER_BAND_H,
                            payload=footer_payload))
    y += FOOTER_BAND_H

    # S1 fit-to-canvas: when the sanctioned minimum height exceeds the
    # content, expand the inter-band gaps (never the canvas, never a dead
    # void below the footer) so the footer band lands flush at the bottom
    # margin. Panels are frozen dataclasses, so shift them in place order.
    slack = min_height - (y + margin)
    if slack > 0:
        # Each boundary (distinct band top below the header) is preceded by
        # exactly one inter-band gap; growing every gap by `step` absorbs
        # the slack and lands the footer flush at the bottom margin.
        boundaries = sorted({p.y for p in panels if p.y > margin})
        step = slack / len(boundaries)
        shifts = {by: step * (i + 1) for i, by in enumerate(boundaries)}
        panels = [p if p.y <= margin else replace(p, y=p.y + shifts[p.y])
                  for p in panels]
        y += slack

    # Canvas height is content-driven; the meta/theme value acts as a minimum.
    height = max(min_height, y + margin)

    logger.info(
        "Computed bands layout: %d panel(s) on %dx%d canvas (%d graph nodes)",
        len(panels), int(width), int(height), len(graph),
    )
    return LayoutResult(width=int(width), height=int(height),
                        panels=tuple(panels))
