"""Panel-template layout engine (Stage 3 of the build pipeline).

Arranges an atlas volume as a grid of curated infographic panels, following
the Vol.02 "Transformer Empire" design mockup (see
``assets/reference/vol02_mockup.png``):

    header (+ legend)
    why-panel | hero-panel | key-papers
    family panels (one per architecture family)
    rail panels (variant / neighbouring families)
    fusion band
    innovation timeline band
    bottom panels (industry / changes / future)
    footer

Panel heights are derived from the content itself (number of model rows,
list items, ...), keeping the poster fully data-driven.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any

from generator import constants
from generator.graph.models import KnowledgeGraph
from generator.parser.loader import KnowledgeData

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Panel:
    """A positioned infographic panel, ready to render."""

    key: str
    x: float
    y: float
    width: float
    height: float
    color: str = ""
    payload: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class LayoutResult:
    """Complete spatial description of one atlas volume, ready to render."""

    width: int
    height: int
    panels: tuple[Panel, ...]

    def panel_by_key(self, key: str) -> Panel:
        """Return the panel with the given key."""
        for panel in self.panels:
            if panel.key == key:
                return panel
        raise KeyError(key)


def compute(
    graph: KnowledgeGraph,
    theme: dict[str, Any],
    knowledge: KnowledgeData | None = None,
) -> LayoutResult:
    """Compute panel positions for the poster template.

    Args:
        graph: The knowledge graph built by Stage 2 (used for statistics).
        theme: Theme dictionary (see ``assets/themes/empire_dark.json``).
        knowledge: Parsed knowledge data; poster sections are read from
            ``knowledge.extras`` (meta, features, hero, key_papers, families,
            rails, fusion, innovations, industry, changes, future).

    Returns:
        A LayoutResult with all positioned panels.
    """
    extras = knowledge.extras if knowledge is not None else {}
    meta = extras.get("meta", {})

    # Dispatch to the generic band-sections template when meta.layout asks
    # for it; the Vol.02 panel template remains the default.
    if meta.get("layout") == constants.LAYOUT_BANDS:
        from generator.layout.bands import compute_bands  # avoid circular import
        if knowledge is None:
            raise ValueError("bands template requires knowledge data")
        return compute_bands(graph, theme, knowledge)

    canvas = theme.get("canvas", {})
    width = int(canvas.get("width", constants.CANVAS_WIDTH))
    height = int(canvas.get("height", constants.CANVAS_HEIGHT))
    margin = float(canvas.get("margin", 40))
    gap = float(canvas.get("gap", 20))
    header_h = float(canvas.get("panel_header_h", 86))
    diagram_h = float(canvas.get("diagram_h", 120))
    family_row_h = float(canvas.get("family_row_h", 100))
    family_footer_h = float(canvas.get("family_footer_h", 96))
    paper_row_h = float(canvas.get("paper_row_h", 52))
    rail_row_h = float(canvas.get("rail_row_h", 44))

    families = extras.get("families", [])
    rails = extras.get("rails", [])
    usable = width - 2 * margin

    panels: list[Panel] = []
    y = margin

    # -- header (title block + legend) -------------------------------------
    top_h = 190.0
    panels.append(Panel("header", margin, y, usable, top_h))
    y += top_h + gap

    # -- row 1: why | hero | key papers ------------------------------------
    why_w, hero_w = 430.0, 560.0
    papers_w = usable - why_w - hero_w - 2 * gap
    papers = extras.get("key_papers", [])
    row1_h = max(440.0, header_h + len(papers) * paper_row_h + 20)
    panels.append(Panel("why", margin, y, why_w, row1_h,
                        color=theme["colors"]["accent"],
                        payload={"features": extras.get("features", [])}))
    panels.append(Panel("hero", margin + why_w + gap, y, hero_w, row1_h,
                        color=theme["colors"]["accent"],
                        payload=extras.get("hero", {})))
    panels.append(Panel("papers", margin + why_w + hero_w + 2 * gap, y,
                        papers_w, row1_h,
                        color=theme["colors"]["accent"],
                        payload={"papers": papers}))
    y += row1_h + gap

    # -- row 2: architecture family panels + right rail column --------------
    # Matches the mockup: 4 family columns, then a narrow 5th column with the
    # variant / neighbouring family panels stacked vertically.
    rail_col_w = float(canvas.get("rail_col_w", 320))
    rail_header_h = float(canvas.get("rail_header_h", 56))
    rail_gap = 12.0
    y_row2 = y
    if families:
        n = len(families)
        fam_w = (usable - rail_col_w - gap - (n - 1) * gap) / n
        max_models = max(len(f.get("models", [])) for f in families)
        fam_content_h = (header_h + diagram_h + max_models * family_row_h
                         + family_footer_h)
        rail_heights = [
            rail_header_h + len(r.get("items", [])) * rail_row_h
            + (26 if r.get("note") else 8)
            for r in rails
        ]
        rails_stack_h = sum(rail_heights) + rail_gap * max(len(rails) - 1, 0)
        fam_h = max(fam_content_h, rails_stack_h)
        for i, family in enumerate(families):
            panels.append(Panel(
                f"family:{family.get('id', i)}",
                margin + i * (fam_w + gap), y_row2, fam_w, fam_h,
                color=family.get("color", ""),
                payload=family,
            ))
        if rails:
            # Distribute leftover vertical space evenly across the rail panels
            extra = (fam_h - rails_stack_h) / len(rails)
            rail_x = width - margin - rail_col_w
            rail_y = y_row2
            for i, rail in enumerate(rails):
                rail_h = rail_heights[i] + extra
                panels.append(Panel(
                    f"rail:{rail.get('id', i)}",
                    rail_x, rail_y, rail_col_w, rail_h,
                    color=rail.get("color", ""),
                    payload=rail,
                ))
                rail_y += rail_h + rail_gap
        y = y_row2 + fam_h + gap

    # -- fusion band ---------------------------------------------------------
    fusion_h = 200.0
    panels.append(Panel("fusion", margin, y, usable, fusion_h,
                        color=theme["colors"]["accent"],
                        payload=extras.get("fusion", {})))
    y += fusion_h + gap

    # -- innovation timeline band --------------------------------------------
    timeline_h = 110.0
    panels.append(Panel("timeline", margin, y, usable, timeline_h,
                        payload={"innovations": extras.get("innovations", [])}))
    y += timeline_h + gap

    # -- bottom row: industry | changes | future ------------------------------
    bottom_h = 200.0
    bottom_w = (usable - 2 * gap) / 3
    bottom_specs = (
        ("bottom:industry", "产业影响 · Industry Impact",
         {"companies": extras.get("industry", [])}),
        ("bottom:changes", "Transformer 如何改变 AI 世界？",
         {"changes": extras.get("changes", [])}),
        ("bottom:future", "未来演进方向 · Future Directions",
         {"future": extras.get("future", [])}),
    )
    for i, (key, title, payload) in enumerate(bottom_specs):
        payload = {**payload, "title": title}
        panels.append(Panel(key, margin + i * (bottom_w + gap), y,
                            bottom_w, bottom_h,
                            color=theme["colors"]["accent"],
                            payload=payload))
    y += bottom_h + gap

    # -- footer ----------------------------------------------------------------
    panels.append(Panel("footer", margin, y, usable, 40,
                        payload=extras.get("meta", {})))
    y += 40

    # Canvas height is content-driven; the theme value acts as a minimum.
    height = max(height, int(y + margin))

    logger.info(
        "Computed poster layout: %d panel(s) on %dx%d canvas (%d graph nodes)",
        len(panels), width, height, len(graph),
    )
    return LayoutResult(width=width, height=height, panels=tuple(panels))
