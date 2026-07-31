"""Unit checks for the generic bands layout template and canvas sizing.

Covers the multi-volume generalization contract:

- the Vol.02 panel template stays the default (no ``meta.layout`` key),
- ``meta.layout = "bands"`` selects the stacked band-sections template,
- ``meta.canvas`` drives the canvas size: portrait 2:3 volumes come out
  portrait, landscape 3:2 volumes (Vol.03, 10-13) come out landscape,
- the light theme (``atlas_light``) loads and renders through the same
  bands pipeline.

Plain-python runnable (``python tests/test_bands_layout.py``); the test
functions are also pytest-compatible for when pytest is adopted.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from generator import constants, graph, layout, render  # noqa: E402
from generator.parser.loader import KnowledgeData  # noqa: E402


def _knowledge(meta: dict, sections: list[dict]) -> KnowledgeData:
    """Build minimal KnowledgeData with the given poster extras."""
    return KnowledgeData(
        nodes=(),
        edges=(),
        source_files=(),
        extras={"meta": meta, "sections": sections},
    )


def _section(number: int) -> dict:
    """One minimal band section with a side panel and two cards."""
    return {
        "number": number,
        "title": f"Section {number}",
        "years": "2000-2010",
        "color": "#3b82f6",
        "left_panel": {"title": "特征", "items": ["甲", "乙"]},
        "cards": [
            {"year": "2001", "title": "Model A", "desc": "desc"},
            {"year": "2002", "title": "Model B", "desc": "desc"},
        ],
    }


def test_panels_template_stays_default() -> None:
    """Without meta.layout, the Vol.02 panel template is used."""
    knowledge = _knowledge(meta={}, sections=[])
    theme = render.load_theme(constants.DEFAULT_THEME)
    result = layout.compute(graph.build(knowledge), theme, knowledge=knowledge)
    keys = {panel.key for panel in result.panels}
    assert "why" in keys and "hero" in keys, f"panel template keys: {keys}"


def test_bands_portrait_canvas() -> None:
    """Portrait 2:3 meta.canvas yields a portrait bands poster."""
    meta = {"layout": "bands", "canvas": {"width": 1682, "height": 2524}}
    knowledge = _knowledge(meta, [_section(1)])
    theme = render.load_theme(constants.DEFAULT_THEME)
    result = layout.compute(graph.build(knowledge), theme, knowledge=knowledge)
    assert result.width == 1682
    assert result.height >= 2524
    assert result.width < result.height, "portrait volume must be portrait"
    keys = {panel.key for panel in result.panels}
    assert "section:0" in keys and "bands_header" in keys


def test_bands_landscape_canvas() -> None:
    """Landscape 3:2 meta.canvas yields a landscape bands poster."""
    meta = {"layout": "bands", "theme": "atlas_light",
            "canvas": {"width": constants.CANVAS_WIDTH_LANDSCAPE,
                       "height": constants.CANVAS_HEIGHT_LANDSCAPE}}
    knowledge = _knowledge(meta, [_section(1), _section(2)])
    theme = render.load_theme("atlas_light")
    knowledge_graph = graph.build(knowledge)
    result = layout.compute(knowledge_graph, theme, knowledge=knowledge)
    assert result.width == constants.CANVAS_WIDTH_LANDSCAPE
    assert result.width > result.height, "landscape volume must be landscape"

    # Smoke-render the full SVG through Stage 4.
    svg = render.draw(result, theme, knowledge)
    assert f'viewBox="0 0 {result.width} {result.height}"' in svg
    assert "Section 1" in svg and "Section 2" in svg


def test_light_theme_loads() -> None:
    """The light series theme shares the empire_dark key structure."""
    dark = render.load_theme("empire_dark")
    light = render.load_theme("atlas_light")
    for group in ("canvas", "colors", "typography"):
        assert set(dark[group]) <= set(light[group]), (
            f"atlas_light is missing {group} keys: "
            f"{set(dark[group]) - set(light[group])}")


def test_renderer_dispatch_is_disjoint() -> None:
    """Panels-template keys never reach the bands renderer and vice versa."""
    from generator.render import bands as bands_renderer

    for key in ("header", "why", "hero", "papers", "fusion", "timeline",
                "footer", "family:0", "rail:0", "bottom:industry"):
        assert not bands_renderer.handles(key), key
    for key in ("bands_header", "legend", "mainline", "insights", "next",
                "bands_footer", "footer_band", "section:0"):
        assert bands_renderer.handles(key), key


def test_bands_row_edge_cases() -> None:
    """Empty rows are skipped; zero/negative weights cannot divide by zero."""
    meta = {"layout": "bands"}
    sections = [
        {"row": []},
        {"row": [{**_section(1), "weight": 0.0},
                 {**_section(2), "weight": 0.0}]},
    ]
    knowledge = _knowledge(meta, sections)
    theme = render.load_theme(constants.DEFAULT_THEME)
    result = layout.compute(graph.build(knowledge), theme, knowledge=knowledge)
    keys = [panel.key for panel in result.panels]
    assert keys.count("section:0") == 1 and keys.count("section:1") == 1, keys


if __name__ == "__main__":
    checks = [value for name, value in sorted(globals().items())
              if name.startswith("test_") and callable(value)]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print(f"{len(checks)} check(s) passed.")
