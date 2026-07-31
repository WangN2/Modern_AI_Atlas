"""SVG poster renderer (Stage 4 of the build pipeline).

Draws the panel-template layout produced by ``generator.layout.compute`` as
a dark infographic poster, following the Vol.02 "Transformer Empire" design
mockup. All output is a standalone SVG string; conversion is Stage 5.
"""

from __future__ import annotations

import logging
from typing import Any
from xml.sax.saxutils import escape

from generator.layout.engine import LayoutResult, Panel
from generator.parser.loader import KnowledgeData
from generator.render import bands as bands_renderer
from generator.render.helpers import fmt as _fmt
from generator.render.helpers import text as _text
from generator.render.helpers import trunc as _trunc
from generator.render.images import ImageEmbedder

logger = logging.getLogger(__name__)


def _panel_frame(panel: Panel, theme: dict[str, Any], title: str,
                 subtitle: str = "") -> tuple[list[str], float]:
    """Draw a panel frame with a colored header band; return content y."""
    canvas = theme["canvas"]
    colors = theme["colors"]
    typo = theme["typography"]
    x, y, w = panel.x, panel.y, panel.width
    header_h = canvas["panel_header_h"]
    r = canvas["panel_radius"]
    color = panel.color or colors["accent"]

    parts = [
        f'<rect x="{_fmt(x)}" y="{_fmt(y)}" width="{_fmt(w)}" '
        f'height="{_fmt(panel.height)}" rx="{r}" '
        f'fill="{canvas["panel_fill"]}" stroke="{canvas["panel_stroke"]}" '
        f'stroke-width="1.5"/>',
        # header band (rounded top, squared bottom)
        f'<path d="M {_fmt(x)} {_fmt(y + r)} Q {_fmt(x)} {_fmt(y)} {_fmt(x + r)} {_fmt(y)} '
        f'L {_fmt(x + w - r)} {_fmt(y)} Q {_fmt(x + w)} {_fmt(y)} {_fmt(x + w)} {_fmt(y + r)} '
        f'L {_fmt(x + w)} {_fmt(y + header_h)} L {_fmt(x)} {_fmt(y + header_h)} Z" '
        f'fill="{color}"/>',
        _text(x + 24, y + header_h * 0.58, title, typo["panel_title_size"],
              "#ffffff", bold=True),
    ]
    if subtitle:
        parts.append(
            _text(x + 24, y + header_h * 0.58 + 26, subtitle,
                  typo["panel_sub_size"], "#ffffff")
        )
    return parts, y + header_h


# -- header + legend ---------------------------------------------------------


def _draw_header(panel: Panel, theme: dict[str, Any],
                 knowledge: KnowledgeData) -> list[str]:
    colors = theme["colors"]
    typo = theme["typography"]
    meta = knowledge.extras.get("meta", {})
    x, y = panel.x, panel.y
    parts = [
        _text(x, y + 30,
              f"{meta.get('series', 'AI TECHNOLOGY BIBLE')} · {meta.get('volume', '')}",
              typo["series_size"], colors["accent"], spacing=6),
        _text(x, y + 118, meta.get("title_en", ""), typo["title_size"],
              colors["title"], bold=True),
        _text(x, y + 170, meta.get("title_zh", ""), typo["title_zh_size"],
              colors["accent"], bold=True),
        _text(x + panel.width * 0.42, y + 170, meta.get("era", ""),
              typo["tagline_size"], colors["muted"]),
        _text(x + panel.width * 0.42, y + 60,
              _trunc(meta.get("tagline", ""), 24),
              typo["tagline_size"] - 4, colors["muted"], italic=True),
    ]
    parts += _draw_legend(panel, theme)
    return parts


def _draw_legend(panel: Panel, theme: dict[str, Any]) -> list[str]:
    canvas = theme["canvas"]
    colors = theme["colors"]
    typo = theme["typography"]
    box_w, box_h = 400.0, 176.0
    bx = panel.x + panel.width - box_w
    by = panel.y
    parts = [
        f'<rect x="{_fmt(bx)}" y="{_fmt(by)}" width="{_fmt(box_w)}" '
        f'height="{_fmt(box_h)}" rx="12" fill="{canvas["panel_fill"]}" '
        f'stroke="{canvas["panel_stroke"]}" stroke-width="1.5"/>',
        _text(bx + 18, by + 30, "图例 Legend", typo["legend_size"],
              colors["title"], bold=True),
    ]
    categories = theme.get("categories", {})
    for i, cat in enumerate(categories.values()):
        col = i % 3
        row = i // 3
        cx = bx + 18 + col * 128
        cy = by + 52 + row * 26
        parts.append(f'<rect x="{_fmt(cx)}" y="{_fmt(cy - 12)}" width="14" '
                     f'height="14" rx="3" fill="{cat["color"]}"/>')
        parts.append(_text(cx + 20, cy, cat["label"], typo["small_size"] - 2,
                           colors["text"]))
    edge_styles = theme.get("edge_styles", {})
    for i, style in enumerate(edge_styles.values()):
        ly = by + 116 + i * 22
        dash = f' stroke-dasharray="{style["dash"]}"' if style.get("dash") else ""
        parts.append(f'<line x1="{_fmt(bx + 200)}" y1="{_fmt(ly)}" '
                     f'x2="{_fmt(bx + 250)}" y2="{_fmt(ly)}" '
                     f'stroke="{colors["muted"]}" stroke-width="2"{dash}/>')
        parts.append(_text(bx + 258, ly + 5, style["label"],
                           typo["small_size"] - 2, colors["muted"]))
    return parts


# -- row 1 panels --------------------------------------------------------------


def _draw_why(panel: Panel, theme: dict[str, Any]) -> list[str]:
    colors = theme["colors"]
    typo = theme["typography"]
    parts, content_y = _panel_frame(panel, theme, "为什么是 Transformer?",
                                    "Why Transformer")
    y = content_y + 20
    for feature in panel.payload.get("features", []):
        parts.append(f'<circle cx="{_fmt(panel.x + 34)}" cy="{_fmt(y + 18)}" '
                     f'r="6" fill="{panel.color or colors["accent"]}"/>')
        parts.append(_text(panel.x + 52, y + 26, feature.get("title", ""),
                           typo["model_name_size"], colors["title"], bold=True))
        parts.append(_text(panel.x + 52, y + 54,
                           _trunc(feature.get("desc", ""), 24),
                           typo["model_desc_size"], colors["muted"]))
        y += 62
    return parts


def _draw_hero(panel: Panel, theme: dict[str, Any]) -> list[str]:
    colors = theme["colors"]
    typo = theme["typography"]
    hero = panel.payload
    title = f"Transformer ({hero.get('year', '')})"
    parts, content_y = _panel_frame(panel, theme, title,
                                    hero.get("title", ""))
    canvas = theme["canvas"]
    # architecture diagram placeholder
    dx, dy = panel.x + 24, content_y + 16
    dw, dh = panel.width - 48, canvas["diagram_h"]
    parts.append(f'<rect x="{_fmt(dx)}" y="{_fmt(dy)}" width="{_fmt(dw)}" '
                 f'height="{_fmt(dh)}" rx="10" fill="none" '
                 f'stroke="{colors["line"]}" stroke-width="1.5" '
                 f'stroke-dasharray="8 6"/>')
    parts.append(_text(dx + dw / 2, dy + dh / 2 + 6,
                       f"Encoder — Decoder 架构 · {hero.get('org', '')}",
                       typo["small_size"], colors["muted"], anchor="middle"))
    y = dy + dh + 34
    for point in hero.get("points", []):
        parts.append(f'<circle cx="{_fmt(panel.x + 34)}" cy="{_fmt(y - 7)}" '
                     f'r="5" fill="{colors["accent"]}"/>')
        parts.append(_text(panel.x + 50, y, _trunc(point, 30),
                           typo["small_size"] + 1, colors["text"]))
        y += 34
    return parts


def _draw_papers(panel: Panel, theme: dict[str, Any]) -> list[str]:
    colors = theme["colors"]
    typo = theme["typography"]
    parts, content_y = _panel_frame(panel, theme, "关键奠基论文",
                                    "Key Papers")
    row_h = theme["canvas"]["paper_row_h"]
    y = content_y + 16
    for paper in panel.payload.get("papers", []):
        parts.append(_text(panel.x + 20, y + 24, str(paper.get("year", "")),
                           typo["year_size"], colors["accent"], bold=True))
        parts.append(_text(panel.x + 92, y + 22,
                           f"{paper.get('authors', '')} · {paper.get('venue', '')}",
                           typo["small_size"] - 2, colors["muted"]))
        parts.append(_text(panel.x + 92, y + 44,
                           _trunc(paper.get("title", ""), 34),
                           typo["small_size"], colors["text"]))
        y += row_h
    return parts


# -- family panels --------------------------------------------------------------


def _draw_family(panel: Panel, theme: dict[str, Any]) -> list[str]:
    colors = theme["colors"]
    typo = theme["typography"]
    payload = panel.payload
    parts, content_y = _panel_frame(panel, theme, payload.get("title", ""),
                                    payload.get("subtitle", ""))
    canvas = theme["canvas"]
    row_h = canvas["family_row_h"]
    color = panel.color or colors["accent"]

    # architecture diagram placeholder
    dx, dy = panel.x + 20, content_y + 12
    dw, dh = panel.width - 40, canvas["diagram_h"] - 24
    parts.append(f'<rect x="{_fmt(dx)}" y="{_fmt(dy)}" width="{_fmt(dw)}" '
                 f'height="{_fmt(dh)}" rx="10" fill="none" '
                 f'stroke="{colors["line"]}" stroke-width="1.5" '
                 f'stroke-dasharray="8 6"/>')
    parts.append(_text(dx + dw / 2, dy + dh / 2 + 5, "架构示意图",
                       typo["small_size"], colors["muted"], anchor="middle"))

    y = content_y + canvas["diagram_h"] + 8
    chip_cx = panel.x + 46
    prev_chip_bottom: float | None = None
    for model in payload.get("models", []):
        chip_y = y + 6
        year = model.get("year")
        if prev_chip_bottom is not None:
            parts.append(f'<line x1="{_fmt(chip_cx)}" y1="{_fmt(prev_chip_bottom)}" '
                         f'x2="{_fmt(chip_cx)}" y2="{_fmt(chip_y)}" '
                         f'stroke="{color}" stroke-width="2" '
                         f'marker-end="url(#arrowhead)"/>')
        if year is not None:
            parts.append(f'<rect x="{_fmt(chip_cx - 32)}" y="{_fmt(chip_y)}" '
                         f'width="64" height="34" rx="17" fill="{color}"/>')
            parts.append(_text(chip_cx, chip_y + 24, str(year),
                               typo["year_size"], "#ffffff", bold=True,
                               anchor="middle"))
            prev_chip_bottom = chip_y + 34
        else:
            parts.append(f'<circle cx="{_fmt(chip_cx)}" cy="{_fmt(chip_y + 17)}" '
                         f'r="9" fill="{color}"/>')
            prev_chip_bottom = chip_y + 26
        name = model.get("name", "")
        org = model.get("org", "")
        label = f"{name} · {org}" if org else name
        parts.append(_text(panel.x + 92, y + 26, _trunc(label, 18),
                           typo["model_name_size"], colors["title"], bold=True))
        parts.append(_text(panel.x + 92, y + 56,
                           _trunc(model.get("desc", ""), 20),
                           typo["model_desc_size"], colors["muted"]))
        y += row_h

    # family footer: applications / representative products
    footer_y = panel.y + panel.height - canvas["family_footer_h"] + 26
    parts.append(f'<line x1="{_fmt(panel.x + 20)}" y1="{_fmt(footer_y - 14)}" '
                 f'x2="{_fmt(panel.x + panel.width - 20)}" y2="{_fmt(footer_y - 14)}" '
                 f'stroke="{colors["line"]}" stroke-width="1"/>')
    parts.append(_text(panel.x + 20, footer_y + 10,
                       _trunc(f"应用：{payload.get('applications', '')}", 18),
                       typo["small_size"], colors["muted"]))
    parts.append(_text(panel.x + 20, footer_y + 38,
                       _trunc(f"代表产品：{payload.get('products', '')}", 18),
                       typo["small_size"], colors["muted"]))
    return parts


# -- rail panels ---------------------------------------------------------------


def _draw_rail(panel: Panel, theme: dict[str, Any]) -> list[str]:
    colors = theme["colors"]
    typo = theme["typography"]
    canvas = theme["canvas"]
    payload = panel.payload
    header_h = canvas["rail_header_h"]
    row_h = canvas["rail_row_h"]
    r = canvas["panel_radius"]
    color = panel.color or colors["accent"]
    x, y, w = panel.x, panel.y, panel.width

    parts = [
        f'<rect x="{_fmt(x)}" y="{_fmt(y)}" width="{_fmt(w)}" '
        f'height="{_fmt(panel.height)}" rx="{r}" '
        f'fill="{canvas["panel_fill"]}" stroke="{canvas["panel_stroke"]}" '
        f'stroke-width="1.5"/>',
        f'<path d="M {_fmt(x)} {_fmt(y + r)} Q {_fmt(x)} {_fmt(y)} {_fmt(x + r)} {_fmt(y)} '
        f'L {_fmt(x + w - r)} {_fmt(y)} Q {_fmt(x + w)} {_fmt(y)} {_fmt(x + w)} {_fmt(y + r)} '
        f'L {_fmt(x + w)} {_fmt(y + header_h)} L {_fmt(x)} {_fmt(y + header_h)} Z" '
        f'fill="{color}"/>',
        _text(x + 16, y + 25, _trunc(payload.get("title", ""), 20),
              typo["panel_sub_size"] + 2, "#ffffff", bold=True),
        _text(x + 16, y + 46, payload.get("subtitle", ""),
              typo["small_size"] - 2, "#ffffff"),
    ]
    item_y = y + header_h + 8
    for item in payload.get("items", []):
        year = item.get("year")
        if year is not None:
            parts.append(_text(x + 16, item_y + 18, str(year),
                               typo["small_size"] - 3, color, bold=True))
        name = item.get("name", "")
        org = item.get("org", "")
        label = f"{name} · {org}" if org else name
        parts.append(_text(x + 70, item_y + 18, _trunc(label, 22),
                           typo["small_size"] - 2, colors["text"]))
        item_y += row_h
    note = payload.get("note")
    if note:
        parts.append(_text(x + 16, panel.y + panel.height - 12,
                           _trunc(note, 26), typo["small_size"] - 3,
                           colors["muted"], italic=True))
    return parts


# -- bands + bottom row + footer -------------------------------------------------


def _draw_fusion(panel: Panel, theme: dict[str, Any]) -> list[str]:
    colors = theme["colors"]
    typo = theme["typography"]
    payload = panel.payload
    parts, content_y = _panel_frame(panel, theme,
                                    payload.get("title", "跨领域融合"), "")
    cy = content_y + (panel.y + panel.height - content_y) / 2 + 6

    modalities = payload.get("modalities", [])
    chip_w, chip_h, chip_gap = 108.0, 44.0, 12.0
    mx = panel.x + 24
    hub_cx = panel.x + panel.width / 2
    for i, modality in enumerate(modalities):
        row, col = divmod(i, 3)
        cx = mx + col * (chip_w + chip_gap)
        cy_chip = cy - chip_h - 8 + row * (chip_h + 16)
        parts.append(f'<rect x="{_fmt(cx)}" y="{_fmt(cy_chip)}" '
                     f'width="{_fmt(chip_w)}" height="{_fmt(chip_h)}" rx="10" '
                     f'fill="{theme["canvas"]["panel_stroke"]}"/>')
        parts.append(_text(cx + chip_w / 2, cy_chip + 29, modality,
                           typo["small_size"], colors["text"], anchor="middle"))
        parts.append(f'<line x1="{_fmt(cx + chip_w)}" y1="{_fmt(cy_chip + chip_h / 2)}" '
                     f'x2="{_fmt(hub_cx - 120)}" y2="{_fmt(cy)}" '
                     f'stroke="{colors["line"]}" stroke-width="1.5"/>')

    parts.append(f'<circle cx="{_fmt(hub_cx)}" cy="{_fmt(cy)}" r="58" '
                 f'fill="{colors["accent"]}" fill-opacity="0.25" '
                 f'stroke="{colors["accent"]}" stroke-width="2.5"/>')
    parts.append(_text(hub_cx, cy - 4, "统一 Transformer",
                       typo["small_size"] + 2, colors["title"], bold=True,
                       anchor="middle"))
    parts.append(_text(hub_cx, cy + 22, "基座架构",
                       typo["small_size"] + 2, colors["title"], bold=True,
                       anchor="middle"))

    capabilities = payload.get("capabilities", [])
    cap_x = hub_cx + 120
    cap_w = (panel.x + panel.width - 24 - cap_x - 10 * len(capabilities)) / max(len(capabilities), 1)
    for i, capability in enumerate(capabilities):
        cx = cap_x + 10 + i * (cap_w + 10)
        parts.append(f'<line x1="{_fmt(hub_cx + 58)}" y1="{_fmt(cy)}" '
                     f'x2="{_fmt(cx)}" y2="{_fmt(cy)}" '
                     f'stroke="{colors["line"]}" stroke-width="1.5"/>')
        parts.append(f'<rect x="{_fmt(cx)}" y="{_fmt(cy - 24)}" '
                     f'width="{_fmt(cap_w)}" height="48" rx="24" '
                     f'fill="{colors["accent"]}"/>')
        parts.append(_text(cx + cap_w / 2, cy + 7, capability,
                           typo["small_size"] + 2, "#ffffff", bold=True,
                           anchor="middle"))
    return parts


def _draw_timeline(panel: Panel, theme: dict[str, Any]) -> list[str]:
    colors = theme["colors"]
    typo = theme["typography"]
    innovations = panel.payload.get("innovations", [])
    parts = [
        _text(panel.x, panel.y + 26, "关键技术创新时间线",
              typo["panel_sub_size"] + 2, colors["title"], bold=True),
    ]
    if not innovations:
        return parts
    y_line = panel.y + 58
    x0, x1 = panel.x + 400, panel.x + panel.width - 60
    parts.append(f'<line x1="{_fmt(x0)}" y1="{_fmt(y_line)}" x2="{_fmt(x1)}" '
                 f'y2="{_fmt(y_line)}" stroke="{colors["line"]}" '
                 f'stroke-width="2"/>')
    step = (x1 - x0) / (len(innovations) - 1) if len(innovations) > 1 else 0
    for i, item in enumerate(innovations):
        x = x0 + i * step
        parts.append(f'<circle cx="{_fmt(x)}" cy="{_fmt(y_line)}" r="6" '
                     f'fill="{colors["accent"]}"/>')
        parts.append(_text(x, y_line - 14, item.get("year", ""),
                           typo["small_size"], colors["accent"], bold=True,
                           anchor="middle"))
        parts.append(_text(x, y_line + 30, _trunc(item.get("text", ""), 10),
                           typo["small_size"] - 2, colors["muted"],
                           anchor="middle"))
    return parts


def _draw_bottom(panel: Panel, theme: dict[str, Any]) -> list[str]:
    colors = theme["colors"]
    typo = theme["typography"]
    payload = panel.payload
    header_h = theme["canvas"]["compact_header_h"]
    parts = [
        f'<rect x="{_fmt(panel.x)}" y="{_fmt(panel.y)}" width="{_fmt(panel.width)}" '
        f'height="{_fmt(panel.height)}" rx="{theme["canvas"]["panel_radius"]}" '
        f'fill="{theme["canvas"]["panel_fill"]}" '
        f'stroke="{theme["canvas"]["panel_stroke"]}" stroke-width="1.5"/>',
        _text(panel.x + 20, panel.y + 36, payload.get("title", ""),
              typo["panel_sub_size"] + 2, colors["title"], bold=True),
    ]
    y = panel.y + header_h + 18

    companies = payload.get("companies")
    if companies is not None:
        chip_w = (panel.width - 40 - 2 * 12) / 3
        for i, company in enumerate(companies):
            row, col = divmod(i, 3)
            cx = panel.x + 20 + col * (chip_w + 12)
            cy = y + row * 32
            parts.append(f'<rect x="{_fmt(cx)}" y="{_fmt(cy)}" '
                         f'width="{_fmt(chip_w)}" height="28" rx="8" '
                         f'fill="{theme["canvas"]["panel_stroke"]}"/>')
            parts.append(_text(cx + chip_w / 2, cy + 20, _trunc(company, 12),
                               typo["small_size"] - 2, colors["text"],
                               anchor="middle"))
        return parts

    for key, marker in (("changes", "✓"), ("future", "▸")):
        items = payload.get(key)
        if items is not None:
            for item in items:
                parts.append(_text(panel.x + 22, y + 8, marker,
                                   typo["small_size"] + 2,
                                   panel.color or colors["accent"], bold=True))
                parts.append(_text(panel.x + 48, y + 8, _trunc(item, 24),
                                   typo["small_size"], colors["text"]))
                y += 28
            return parts
    return parts


def _draw_footer(panel: Panel, theme: dict[str, Any]) -> list[str]:
    colors = theme["colors"]
    typo = theme["typography"]
    meta = panel.payload
    return [
        _text(panel.x + panel.width / 2, panel.y + 26, meta.get("quote", ""),
              typo["footer_size"] - 2, colors["muted"], anchor="middle",
              italic=True),
        _text(panel.x + panel.width, panel.y + 26, meta.get("next", ""),
              typo["footer_size"] - 2, colors["accent"], anchor="end",
              bold=True),
    ]


# -- entry point ------------------------------------------------------------------


def draw(
    layout: LayoutResult,
    theme: dict[str, Any],
    knowledge: KnowledgeData,
) -> str:
    """Render a computed poster layout to a standalone SVG string.

    Args:
        layout: Positioned panels from ``generator.layout.compute``.
        theme: Theme dictionary (see ``generator.render.theme.load_theme``).
        knowledge: Parsed knowledge data (meta section drives the header).

    Returns:
        The complete SVG document as a string.
    """
    canvas = theme["canvas"]
    colors = theme["colors"]
    typo = theme["typography"]
    background = canvas.get("background", "#0a0e1c")

    # Card images ("image" keys) resolve relative to the atlas volume dir,
    # derived from the parsed knowledge file's location.
    images = (ImageEmbedder(knowledge.source_files[0].parent)
              if knowledge.source_files else None)

    body: list[str] = [
        f'<rect width="{layout.width}" height="{layout.height}" '
        f'fill="{background}"/>',
    ]
    for panel in layout.panels:
        if panel.key == "header":
            body += _draw_header(panel, theme, knowledge)
        elif panel.key == "why":
            body += _draw_why(panel, theme)
        elif panel.key == "hero":
            body += _draw_hero(panel, theme)
        elif panel.key == "papers":
            body += _draw_papers(panel, theme)
        elif panel.key.startswith("family:"):
            body += _draw_family(panel, theme)
        elif panel.key.startswith("rail:"):
            body += _draw_rail(panel, theme)
        elif panel.key == "fusion":
            body += _draw_fusion(panel, theme)
        elif panel.key == "timeline":
            body += _draw_timeline(panel, theme)
        elif panel.key.startswith("bottom:"):
            body += _draw_bottom(panel, theme)
        elif panel.key == "footer":
            body += _draw_footer(panel, theme)
        elif bands_renderer.handles(panel.key):
            body += bands_renderer.draw_panel(panel, theme, images)
        else:
            logger.warning("No renderer for panel %r; skipped", panel.key)

    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{layout.width / 2:.0f}mm" height="{layout.height / 2:.0f}mm"
     viewBox="0 0 {layout.width} {layout.height}"
     font-family="{escape(typo["font_family"])}">
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="8"
            refX="9" refY="4" orient="auto">
      <polygon points="0 0, 10 4, 0 8" fill="{colors["muted"]}"/>
    </marker>
  </defs>
  {chr(10).join(body)}
</svg>
"""
    logger.info("Rendered SVG poster: %d panel(s), canvas %dx%d",
                len(layout.panels), layout.width, layout.height)
    return svg
