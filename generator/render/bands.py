"""Renderer for the generic band-sections poster template (Stage 4 helper).

Draws the panels produced by ``generator.layout.bands.compute_bands``:
three header styles, legend row/box, and the section ``kind`` library:

    band        numbered/titled era band with side panels + model cards
    list        titled bullet/icon list panel (optionally multi-column)
    cards       grid of small titled cards with bullets
    table       simple table with a colored header row
    pills       family-tree pill rows (row label + chips + arrows)
    chevrons    horizontal chevron/step flow
    timeline    horizontal milestone timeline (year chip + 2-line card)
    fusion      modalities -> glowing core -> capabilities band
    family      architecture family panel (year chips + model rows + footer)
    hero        centerpiece panel with architecture schematic + caption
    papers      key-papers list (year + authors + citation)
    industry    grouped chip columns (e.g. industry impact)
    pyramid     capability hierarchy pyramid
    wheel       donut wheel of concept segments + optional strip
    radial      radial discipline map (center + surrounding branch cards)
    figures     key-figures portrait rows
    curve       S-curve chart with stage callouts
    arch        decoder-only architecture diagram (+ token table, align
                flow, ability chips)

Both dark (empire_dark) and light (atlas_light) themes are supported; the
two themes share the same key structure. Mini diagrams and icons are simple
schematic placeholders — faithful text, layout, and color take priority.

This module is dispatched from ``generator.render.svg.draw`` for any panel
key it does not handle itself (see ``handles``).
"""

from __future__ import annotations

import logging
import math
from typing import Any
from xml.sax.saxutils import escape

from generator.layout.engine import Panel
from generator.render.helpers import (
    band_card_caption_height,
    band_card_caption_lines,
    band_card_header_offset,
    card_bullet_layout,
    card_bullet_pitch,
    card_image_height,
    card_step_up,
    card_text_height,
    card_title_layout,
    cards_geometry,
    cards_panel_card_height,
    family_desc_lines,
    family_label_lines,
    fit,
    fmt,
    list_item_layout,
    list_row_height,
    pills_line_breaks,
    text,
    text_width,
    trunc,
    wrap,
    wrap_fit,
)
from generator.render.images import ImageEmbedder

logger = logging.getLogger(__name__)

_KEYS = ("bands_header", "legend", "mainline", "insights", "next",
         "bands_footer", "footer_band")

# Text colors used on the always-dark mainline band / NEXT teaser /
# footer band, regardless of the active theme.
_DARK_TEXT = "#e6ecfa"
_DARK_MUTED = "#93a0c2"
_YELLOW = "#ffd75e"


def handles(key: str) -> bool:
    """Return True if this renderer draws the given panel key."""
    return key in _KEYS or key.startswith("section:")


def draw_panel(panel: Panel, theme: dict[str, Any],
               images: ImageEmbedder | None = None) -> list[str]:
    """Dispatch one bands-template panel to its drawing function."""
    key = panel.key
    if key == "bands_header":
        return _draw_header(panel, theme)
    if key == "legend":
        return _draw_legend(panel, theme)
    if key.startswith("section:"):
        return _draw_section(panel, theme, images)
    if key == "mainline":
        return _draw_mainline(panel, theme)
    if key == "insights":
        return _draw_insights(panel, theme)
    if key == "next":
        return _draw_next(panel, theme)
    if key == "footer_band":
        return _draw_footer_band(panel, theme)
    if key == "bands_footer":
        return _draw_footer(panel, theme)
    logger.warning("bands renderer: no drawing function for %r", key)
    return []


# -- shared bits ---------------------------------------------------------------


def _is_dark(theme: dict[str, Any]) -> bool:
    """Heuristic: dark theme iff the canvas background is dark."""
    bg = theme["canvas"].get("background", "#0a0e1c").lstrip("#")
    r, g, b = (int(bg[i:i + 2], 16) for i in (0, 2, 4))
    return (0.299 * r + 0.587 * g + 0.114 * b) < 128


def _bright(theme: dict[str, Any]) -> str:
    """Highlight color for subtitles/labels (yellow on dark, accent on light)."""
    return _YELLOW if _is_dark(theme) else theme["colors"]["accent"]


def _frame(panel: Panel, theme: dict[str, Any], *, fill: str | None = None,
           stroke: str | None = None, shadow: bool = True) -> str:
    """Rounded panel frame rectangle with optional soft drop-shadow."""
    canvas = theme["canvas"]
    use_shadow = shadow and bool(canvas.get("panel_shadow", True))
    flt = ' filter="url(#panel-shadow)"' if use_shadow else ""
    return (f'<rect x="{fmt(panel.x)}" y="{fmt(panel.y)}" '
            f'width="{fmt(panel.width)}" height="{fmt(panel.height)}" '
            f'rx="{canvas["panel_radius"]}"{flt} '
            f'fill="{fill or canvas["panel_fill"]}" '
            f'stroke="{stroke or canvas["panel_stroke"]}" stroke-width="1.5"/>')


def _bullet_list(x: float, y: float, items: list[str], *, color: str,
                 theme: dict[str, Any], size: float = 14,
                 row_h: float = 26, max_units: float = 12,
                 text_fill: str | None = None) -> list[str]:
    """Bulleted list with small colored dot markers (items wrap to 2 lines)."""
    colors = theme["colors"]
    parts: list[str] = []
    for item in items:
        lines = wrap_fit(item, max_units, 2)
        parts.append(f'<circle cx="{fmt(x + 5)}" cy="{fmt(y - 4)}" r="4" '
                     f'fill="{color}"/>')
        for i, line in enumerate(lines):
            parts.append(text(x + 16, y + i * 15, line, size,
                              text_fill or colors["text"]))
        y += row_h + 15 * (len(lines) - 1)
    return parts


def _panel_chrome(panel: Panel, theme: dict[str, Any],
                  title: str, subtitle: str = "") -> tuple[list[str], float]:
    """Frame + accent bar + section title; return (parts, content_y).

    When the section payload carries a ``number`` (Vol.07/08 numbered-grid
    style), a circled numeral replaces the accent bar in front of the
    title; sections without ``number`` render exactly as before.
    """
    colors = theme["colors"]
    accent = panel.color or colors["accent"]
    x, y = panel.x, panel.y
    parts = [_frame(panel, theme)]
    number = panel.payload.get("number")
    tx = x + 32
    if number is not None:
        ncx, ncy = x + 38, y + 27
        parts.append(f'<circle cx="{fmt(ncx)}" cy="{fmt(ncy)}" r="16" '
                     f'fill="none" stroke="{accent}" stroke-width="2.2"/>')
        parts.append(text(ncx, ncy + 7, str(number), 19, accent,
                          bold=True, anchor="middle"))
        tx = x + 64
    else:
        parts.append(f'<rect x="{fmt(x + 16)}" y="{fmt(y + 15)}" width="6" '
                     f'height="24" rx="3" fill="{accent}"/>')
    parts.append(text(tx, y + 34, title, 20, colors["title"], bold=True))
    if subtitle:
        parts.append(text(tx + text_width(title, 20) + 12, y + 33,
                          subtitle, 13, colors["muted"]))
    return parts, y + 54


def _arrow(x: float, y: float, size: float, color: str) -> list[str]:
    """Small right-pointing arrow drawn as SVG primitives (font-safe)."""
    half = size / 2
    head = size * 0.32
    return [
        f'<line x1="{fmt(x)}" y1="{fmt(y)}" x2="{fmt(x + size - head * .6)}" '
        f'y2="{fmt(y)}" stroke="{color}" stroke-width="1.6"/>',
        f'<path d="M {fmt(x + size - head)} {fmt(y - head)} '
        f'L {fmt(x + size)} {fmt(y)} L {fmt(x + size - head)} '
        f'{fmt(y + head)}" fill="{color}"/>',
    ]


def _text_rich(x: float, y: float, s: str, size: float, fill: str,
               *, bold: bool = False) -> list[str]:
    """Render text, substituting drawn arrows for "→" (fonts lack it)."""
    if "→" not in s:
        return [text(x, y, s, size, fill, bold=bold)]
    parts: list[str] = []
    cursor = x
    gap = size * 0.25
    for i, segment in enumerate(s.split("→")):
        segment = segment.strip()
        if i > 0:
            cursor += gap
            parts += _arrow(cursor, y - size * 0.32, size * 0.9, fill)
            cursor += size * 0.9 + gap
        if segment:
            parts.append(text(cursor, y, segment, size, fill, bold=bold))
            cursor += text_width(segment, size)
    return parts


def _chip(x: float, y: float, w: float, h: float, label: str, *,
          fill: str, stroke: str = "", text_fill: str = "#ffffff",
          size: float = 12, bold: bool = True, rx: float | None = None) -> list[str]:
    """One rounded chip/pill with centered label."""
    rx = h / 2 if rx is None else rx
    rect = (f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" '
            f'height="{fmt(h)}" rx="{fmt(rx)}" fill="{fill}"')
    if stroke:
        rect += f' stroke="{stroke}" stroke-width="1.2"'
    rect += "/>"
    return [rect,
            text(x + w / 2, y + h / 2 + size * 0.36, label, size,
                 text_fill, bold=bold, anchor="middle")]


def _icon(kind: str, cx: float, cy: float, s: float, color: str) -> list[str]:
    """Small primitive line icon (font-safe); unknown kinds draw a dot."""
    if kind == "check":
        return [f'<path d="M {fmt(cx - s)} {fmt(cy)} L {fmt(cx - s * .2)} '
                f'{fmt(cy + s * .8)} L {fmt(cx + s)} {fmt(cy - s * .8)}" '
                f'fill="none" stroke="{color}" stroke-width="2.5" '
                f'stroke-linecap="round"/>']
    if kind == "chart":
        return [f'<rect x="{fmt(cx - s)}" y="{fmt(cy)}" width="{fmt(s * .55)}" '
                f'height="{fmt(s)}" fill="{color}"/>',
                f'<rect x="{fmt(cx - s * .2)}" y="{fmt(cy - s * .6)}" '
                f'width="{fmt(s * .55)}" height="{fmt(s * 1.6)}" fill="{color}"/>',
                f'<rect x="{fmt(cx + s * .6)}" y="{fmt(cy - s * .2)}" '
                f'width="{fmt(s * .55)}" height="{fmt(s * 1.2)}" fill="{color}"/>']
    if kind == "person":
        return [f'<circle cx="{fmt(cx)}" cy="{fmt(cy - s * .45)}" '
                f'r="{fmt(s * .5)}" fill="{color}"/>',
                f'<path d="M {fmt(cx - s)} {fmt(cy + s)} '
                f'Q {fmt(cx)} {fmt(cy - s * .1)} {fmt(cx + s)} {fmt(cy + s)} Z" '
                f'fill="{color}"/>']
    if kind == "globe":
        return [f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(s)}" '
                f'fill="none" stroke="{color}" stroke-width="2"/>',
                f'<ellipse cx="{fmt(cx)}" cy="{fmt(cy)}" rx="{fmt(s * .45)}" '
                f'ry="{fmt(s)}" fill="none" stroke="{color}" stroke-width="1.2"/>',
                f'<line x1="{fmt(cx - s)}" y1="{fmt(cy)}" x2="{fmt(cx + s)}" '
                f'y2="{fmt(cy)}" stroke="{color}" stroke-width="1.2"/>']
    if kind == "rocket":
        return [f'<path d="M {fmt(cx)} {fmt(cy - s)} Q {fmt(cx + s * .8)} '
                f'{fmt(cy - s * .2)} {fmt(cx + s * .4)} {fmt(cy + s * .6)} '
                f'L {fmt(cx)} {fmt(cy + s * .3)} L {fmt(cx - s * .4)} '
                f'{fmt(cy + s * .6)} Q {fmt(cx - s * .8)} {fmt(cy - s * .2)} '
                f'{fmt(cx)} {fmt(cy - s)} Z" fill="{color}"/>',
                f'<circle cx="{fmt(cx)}" cy="{fmt(cy - s * .25)}" '
                f'r="{fmt(s * .22)}" fill="#ffffff"/>']
    if kind == "star":
        pts = " ".join(
            f"{fmt(cx + (s if i % 2 == 0 else s * .45) * math.cos(-1.5708 + i * 0.6283))},"
            f"{fmt(cy + (s if i % 2 == 0 else s * .45) * math.sin(-1.5708 + i * 0.6283))}"
            for i in range(10))
        return [f'<polygon points="{pts}" fill="{color}"/>']
    if kind == "cube":
        t = s * 0.9
        top = f'{fmt(cx)},{fmt(cy - t)} {fmt(cx + t)},{fmt(cy - t / 2)} {fmt(cx)},{fmt(cy)} {fmt(cx - t)},{fmt(cy - t / 2)}'
        left = f'{fmt(cx - t)},{fmt(cy - t / 2)} {fmt(cx)},{fmt(cy)} {fmt(cx)},{fmt(cy + t)} {fmt(cx - t)},{fmt(cy + t / 2)}'
        right = f'{fmt(cx + t)},{fmt(cy - t / 2)} {fmt(cx)},{fmt(cy)} {fmt(cx)},{fmt(cy + t)} {fmt(cx + t)},{fmt(cy + t / 2)}'
        return [f'<polygon points="{top}" fill="{color}" fill-opacity="0.95"/>',
                f'<polygon points="{left}" fill="{color}" fill-opacity="0.55"/>',
                f'<polygon points="{right}" fill="{color}" fill-opacity="0.75"/>']
    if kind == "book":
        return _legend_icon("book", cx, cy, color)
    if kind == "atom":
        return _legend_icon("atom", cx, cy, color)
    if kind == "gear":
        return _legend_icon("gear", cx, cy, color)
    if kind == "db":
        return [f'<ellipse cx="{fmt(cx)}" cy="{fmt(cy - s * .6)}" rx="{fmt(s)}" '
                f'ry="{fmt(s * .35)}" fill="none" stroke="{color}" stroke-width="1.8"/>',
                f'<path d="M {fmt(cx - s)} {fmt(cy - s * .6)} L {fmt(cx - s)} '
                f'{fmt(cy + s * .6)} A {fmt(s)} {fmt(s * .35)} 0 0 0 '
                f'{fmt(cx + s)} {fmt(cy + s * .6)} L {fmt(cx + s)} '
                f'{fmt(cy - s * .6)}" fill="none" stroke="{color}" '
                f' stroke-width="1.8"/>']
    if kind == "brain":
        return [f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(s)}" '
                f'fill="none" stroke="{color}" stroke-width="2"/>',
                f'<path d="M {fmt(cx - s * .6)} {fmt(cy - s * .2)} '
                f'Q {fmt(cx)} {fmt(cy + s * .35)} {fmt(cx + s * .6)} '
                f'{fmt(cy - s * .2)}" fill="none" stroke="{color}" '
                f'stroke-width="1.5"/>',
                f'<path d="M {fmt(cx)} {fmt(cy - s)} L {fmt(cx)} '
                f'{fmt(cy + s)}" stroke="{color}" stroke-width="1.5"/>']
    if kind == "bolt":
        return [f'<polygon points="{fmt(cx + s * .2)},{fmt(cy - s)} '
                f'{fmt(cx - s * .6)},{fmt(cy + s * .15)} '
                f'{fmt(cx - s * .05)},{fmt(cy + s * .15)} '
                f'{fmt(cx - s * .2)},{fmt(cy + s)} '
                f'{fmt(cx + s * .6)},{fmt(cy - s * .15)} '
                f'{fmt(cx + s * .05)},{fmt(cy - s * .15)}" fill="{color}"/>']
    if kind == "doc":
        return [f'<path d="M {fmt(cx - s * .7)} {fmt(cy - s)} '
                f'L {fmt(cx + s * .3)} {fmt(cy - s)} L {fmt(cx + s * .7)} '
                f'{fmt(cy - s * .6)} L {fmt(cx + s * .7)} {fmt(cy + s)} '
                f'L {fmt(cx - s * .7)} {fmt(cy + s)} Z" fill="none" '
                f'stroke="{color}" stroke-width="2"/>',
                f'<line x1="{fmt(cx - s * .4)}" y1="{fmt(cy - s * .2)}" '
                f'x2="{fmt(cx + s * .4)}" y2="{fmt(cy - s * .2)}" '
                f'stroke="{color}" stroke-width="1.5"/>',
                f'<line x1="{fmt(cx - s * .4)}" y1="{fmt(cy + s * .3)}" '
                f'x2="{fmt(cx + s * .4)}" y2="{fmt(cy + s * .3)}" '
                f'stroke="{color}" stroke-width="1.5"/>']
    if kind == "robot":
        return [f'<rect x="{fmt(cx - s * .8)}" y="{fmt(cy - s * .5)}" '
                f'width="{fmt(s * 1.6)}" height="{fmt(s * 1.2)}" rx="3" '
                f'fill="none" stroke="{color}" stroke-width="2"/>',
                f'<circle cx="{fmt(cx - s * .35)}" cy="{fmt(cy + s * .1)}" '
                f'r="{fmt(s * .16)}" fill="{color}"/>',
                f'<circle cx="{fmt(cx + s * .35)}" cy="{fmt(cy + s * .1)}" '
                f'r="{fmt(s * .16)}" fill="{color}"/>',
                f'<line x1="{fmt(cx)}" y1="{fmt(cy - s * .5)}" x2="{fmt(cx)}" '
                f'y2="{fmt(cy - s)}" stroke="{color}" stroke-width="2"/>',
                f'<circle cx="{fmt(cx)}" cy="{fmt(cy - s)}" '
                f'r="{fmt(s * .18)}" fill="{color}"/>']
    if kind == "network":
        return [f'<circle cx="{fmt(cx - s * .7)}" cy="{fmt(cy - s * .5)}" '
                f'r="{fmt(s * .3)}" fill="{color}"/>',
                f'<circle cx="{fmt(cx + s * .7)}" cy="{fmt(cy - s * .5)}" '
                f'r="{fmt(s * .3)}" fill="{color}"/>',
                f'<circle cx="{fmt(cx)}" cy="{fmt(cy + s * .6)}" '
                f'r="{fmt(s * .3)}" fill="{color}"/>',
                f'<line x1="{fmt(cx - s * .45)}" y1="{fmt(cy - s * .35)}" '
                f'x2="{fmt(cx - s * .05)}" y2="{fmt(cy + s * .4)}" '
                f'stroke="{color}" stroke-width="1.5"/>',
                f'<line x1="{fmt(cx + s * .45)}" y1="{fmt(cy - s * .35)}" '
                f'x2="{fmt(cx + s * .05)}" y2="{fmt(cy + s * .4)}" '
                f'stroke="{color}" stroke-width="1.5"/>',
                f'<line x1="{fmt(cx - s * .4)}" y1="{fmt(cy - s * .5)}" '
                f'x2="{fmt(cx + s * .4)}" y2="{fmt(cy - s * .5)}" '
                f'stroke="{color}" stroke-width="1.5"/>']
    if kind == "flow":
        return [f'<rect x="{fmt(cx - s)}" y="{fmt(cy - s * .7)}" '
                f'width="{fmt(s * .7)}" height="{fmt(s * .5)}" rx="2" '
                f'fill="{color}"/>',
                f'<rect x="{fmt(cx + s * .3)}" y="{fmt(cy + s * .2)}" '
                f'width="{fmt(s * .7)}" height="{fmt(s * .5)}" rx="2" '
                f'fill="{color}"/>',
                f'<path d="M {fmt(cx - s * .1)} {fmt(cy - s * .45)} '
                f'L {fmt(cx + s * .35)} {fmt(cy - s * .45)} '
                f'L {fmt(cx + s * .35)} {fmt(cy + s * .15)}" fill="none" '
                f'stroke="{color}" stroke-width="1.8"/>']
    if kind == "layers":
        return [f'<polygon points="{fmt(cx)},{fmt(cy - s)} '
                f'{fmt(cx + s)},{fmt(cy - s * .4)} {fmt(cx)},{fmt(cy + s * .2)} '
                f'{fmt(cx - s)},{fmt(cy - s * .4)}" fill="{color}"/>',
                f'<polygon points="{fmt(cx)},{fmt(cy - s * .1)} '
                f'{fmt(cx + s)},{fmt(cy + s * .5)} {fmt(cx)},{fmt(cy + s * 1.1)} '
                f'{fmt(cx - s)},{fmt(cy + s * .5)}" fill="{color}" '
                f'fill-opacity="0.55"/>']
    if kind == "target":
        return [f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(s)}" '
                f'fill="none" stroke="{color}" stroke-width="2"/>',
                f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(s * .55)}" '
                f'fill="none" stroke="{color}" stroke-width="1.8"/>',
                f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(s * .2)}" '
                f'fill="{color}"/>']
    if kind == "speech":
        return [f'<rect x="{fmt(cx - s * .25)}" y="{fmt(cy - s)}" '
                f'width="{fmt(s * .5)}" height="{fmt(s * 1.2)}" rx="3" '
                f'fill="{color}"/>',
                f'<path d="M {fmt(cx - s * .6)} {fmt(cy - s * .1)} '
                f'Q {fmt(cx)} {fmt(cy + s * .55)} {fmt(cx + s * .6)} '
                f'{fmt(cy - s * .1)}" fill="none" stroke="{color}" '
                f'stroke-width="1.8"/>',
                f'<line x1="{fmt(cx)}" y1="{fmt(cy + s * .35)}" x2="{fmt(cx)}" '
                f'y2="{fmt(cy + s)}" stroke="{color}" stroke-width="1.8"/>']
    if kind == "image":
        return [f'<rect x="{fmt(cx - s)}" y="{fmt(cy - s * .8)}" '
                f'width="{fmt(s * 2)}" height="{fmt(s * 1.6)}" rx="2" '
                f'fill="none" stroke="{color}" stroke-width="2"/>',
                f'<circle cx="{fmt(cx - s * .4)}" cy="{fmt(cy - s * .3)}" '
                f'r="{fmt(s * .18)}" fill="{color}"/>',
                f'<path d="M {fmt(cx - s)} {fmt(cy + s * .8)} '
                f'L {fmt(cx - s * .1)} {fmt(cy)} L {fmt(cx + s * .4)} '
                f'{fmt(cy + s * .45)} L {fmt(cx + s)} {fmt(cy - s * .1)} '
                f'L {fmt(cx + s)} {fmt(cy + s * .8)} Z" fill="{color}"/>']
    if kind == "video":
        return [f'<rect x="{fmt(cx - s)}" y="{fmt(cy - s * .7)}" '
                f'width="{fmt(s * 2)}" height="{fmt(s * 1.4)}" rx="3" '
                f'fill="none" stroke="{color}" stroke-width="2"/>',
                f'<polygon points="{fmt(cx - s * .25)},{fmt(cy - s * .35)} '
                f'{fmt(cx + s * .45)},{fmt(cy)} '
                f'{fmt(cx - s * .25)},{fmt(cy + s * .35)}" fill="{color}"/>']
    if kind == "audio":
        bars = []
        for i, h in enumerate((0.5, 0.9, 1.3, 0.8, 0.45)):
            bx = cx - s + i * (s * 0.5)
            bars.append(f'<rect x="{fmt(bx)}" y="{fmt(cy - h * s / 2)}" '
                        f'width="{fmt(s * .28)}" height="{fmt(h * s)}" rx="2" '
                        f'fill="{color}"/>')
        return bars
    if kind == "sensor":
        return [f'<circle cx="{fmt(cx)}" cy="{fmt(cy + s * .5)}" '
                f'r="{fmt(s * .3)}" fill="{color}"/>',
                f'<path d="M {fmt(cx - s * .6)} {fmt(cy - s * .1)} '
                f'A {fmt(s * .85)} {fmt(s * .85)} 0 0 1 '
                f'{fmt(cx + s * .6)} {fmt(cy - s * .1)}" fill="none" '
                f'stroke="{color}" stroke-width="1.8"/>',
                f'<path d="M {fmt(cx - s)} {fmt(cy - s * .5)} '
                f'A {fmt(s * 1.4)} {fmt(s * 1.4)} 0 0 1 '
                f'{fmt(cx + s)} {fmt(cy - s * .5)}" fill="none" '
                f'stroke="{color}" stroke-width="1.8"/>']
    if kind == "text":
        return _icon("doc", cx, cy, s, color)
    return [f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(s * .6)}" '
            f'fill="{color}"/>']


# -- header (three styles) -----------------------------------------------------


def _legend_icon(kind: str, cx: float, cy: float, color: str) -> list[str]:
    """Small primitive legend icon (no emoji, font-safe)."""
    s = 9.0
    if kind in ("image", "video", "text", "audio", "sensor", "cube",
                "speech", "rocket", "star", "doc", "flow", "layers",
                "target", "bolt", "network", "robot"):
        return _icon(kind, cx, cy, 8, color)
    if kind == "timeline":
        return [f'<line x1="{fmt(cx - s)}" y1="{fmt(cy)}" x2="{fmt(cx + s)}" '
                f'y2="{fmt(cy)}" stroke="{color}" stroke-width="2"/>',
                f'<circle cx="{fmt(cx - s * .5)}" cy="{fmt(cy)}" r="3" '
                f'fill="{color}"/>',
                f'<circle cx="{fmt(cx + s * .5)}" cy="{fmt(cy)}" r="3" '
                f'fill="none" stroke="{color}" stroke-width="2"/>']
    if kind == "person":
        return [f'<circle cx="{fmt(cx)}" cy="{fmt(cy - s * .45)}" r="4" '
                f'fill="{color}"/>',
                f'<path d="M {fmt(cx - s * .7)} {fmt(cy + s)} '
                f'Q {fmt(cx)} {fmt(cy - s * .1)} {fmt(cx + s * .7)} '
                f'{fmt(cy + s)} Z" fill="{color}"/>']
    if kind == "chart":
        return [f'<rect x="{fmt(cx - s)}" y="{fmt(cy)}" width="5" '
                f'height="{fmt(s)}" fill="{color}"/>',
                f'<rect x="{fmt(cx - 2.5)}" y="{fmt(cy - s * .55)}" width="5" '
                f'height="{fmt(s * 1.55)}" fill="{color}"/>',
                f'<rect x="{fmt(cx + 5)}" y="{fmt(cy - s)}" width="5" '
                f'height="{fmt(s * 2)}" fill="{color}"/>']
    if kind == "brain":
        return [f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(s - 1)}" '
                f'fill="none" stroke="{color}" stroke-width="2"/>',
                f'<path d="M {fmt(cx - s * .5)} {fmt(cy - 2)} '
                f'Q {fmt(cx)} {fmt(cy + 3)} {fmt(cx + s * .5)} {fmt(cy - 2)}" '
                f'fill="none" stroke="{color}" stroke-width="1.5"/>',
                f'<path d="M {fmt(cx)} {fmt(cy - s + 1)} L {fmt(cx)} '
                f'{fmt(cy + s - 1)}" stroke="{color}" stroke-width="1.5"/>']
    if kind == "circles":
        return [f'<circle cx="{fmt(cx - s * .45)}" cy="{fmt(cy)}" r="5.5" '
                f'fill="none" stroke="{color}" stroke-width="2"/>',
                f'<circle cx="{fmt(cx + s * .45)}" cy="{fmt(cy)}" r="5.5" '
                f'fill="{color}" fill-opacity="0.55"/>']
    if kind == "milestone":
        return [f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(s)}" '
                f'fill="none" stroke="{color}" stroke-width="2.5"/>',
                f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="3" fill="{color}"/>']
    if kind == "gear":
        parts = [f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(s - 2)}" '
                 f'fill="none" stroke="{color}" stroke-width="2.5"/>']
        for dx, dy in ((0, -s), (0, s), (-s, 0), (s, 0),
                       (-s * .7, -s * .7), (s * .7, s * .7),
                       (-s * .7, s * .7), (s * .7, -s * .7)):
            parts.append(f'<circle cx="{fmt(cx + dx)}" cy="{fmt(cy + dy)}" '
                         f'r="2" fill="{color}"/>')
        return parts
    if kind == "atom":
        return [f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="2.5" fill="{color}"/>',
                f'<ellipse cx="{fmt(cx)}" cy="{fmt(cy)}" rx="{fmt(s)}" ry="4" '
                f'fill="none" stroke="{color}" stroke-width="1.5"/>',
                f'<ellipse cx="{fmt(cx)}" cy="{fmt(cy)}" rx="4" ry="{fmt(s)}" '
                f'fill="none" stroke="{color}" stroke-width="1.5"/>']
    if kind == "book":
        return [f'<path d="M {fmt(cx - s)} {fmt(cy - s + 3)} '
                f'L {fmt(cx)} {fmt(cy - s + 6)} L {fmt(cx + s)} {fmt(cy - s + 3)} '
                f'L {fmt(cx + s)} {fmt(cy + s - 3)} L {fmt(cx)} {fmt(cy + s)} '
                f'L {fmt(cx - s)} {fmt(cy + s - 3)} Z" '
                f'fill="none" stroke="{color}" stroke-width="2"/>']
    if kind == "factory":
        return [f'<path d="M {fmt(cx - s)} {fmt(cy + s)} L {fmt(cx - s)} {fmt(cy - 2)} '
                f'L {fmt(cx - 2)} {fmt(cy - s + 2)} L {fmt(cx - 2)} {fmt(cy - 2)} '
                f'L {fmt(cx + 5)} {fmt(cy - s + 2)} L {fmt(cx + 5)} {fmt(cy - 2)} '
                f'L {fmt(cx + s)} {fmt(cy - s + 2)} L {fmt(cx + s)} {fmt(cy + s)} Z" '
                f'fill="{color}"/>']
    return [f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(s - 2)}" '
            f'fill="{color}"/>']


def _draw_legend(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Legend row under the header: `图例:` label + icon chips.

    The payload ``items`` is either a list of ``{icon, label, color}``
    entries or the Vol.02 dict form ``{categories: [...], edges: [...]}``
    (category chips + edge-style line samples). Both render as one row.
    """
    colors = theme["colors"]
    canvas = theme["canvas"]
    x, y = panel.x, panel.y
    cy = y + panel.height / 2 + 5
    legend_fill = canvas.get("legend_fill")
    text_fill = colors.get("legend_text", colors["text"]) if legend_fill else colors["text"]
    title_fill = colors.get("legend_text", colors["title"]) if legend_fill else colors["title"]
    muted_fill = colors.get("legend_text", colors["muted"]) if legend_fill else colors["muted"]
    parts = []
    if legend_fill:
        parts.append(_frame(panel, theme, fill=legend_fill,
                            stroke=canvas.get("legend_stroke"), shadow=False))
    label_x = x + (12 if legend_fill else 0)
    parts.append(text(label_x, cy, "图例:", 18, title_fill, bold=True))
    cx = x + (82 if legend_fill else 70)
    items = panel.payload.get("items", [])
    if isinstance(items, dict):
        for cat in items.get("categories", []):
            color = cat.get("color", colors["accent"])
            parts.append(f'<rect x="{fmt(cx)}" y="{fmt(cy - 17)}" width="14" '
                         f'height="14" rx="3" fill="{color}"/>')
            label = cat.get("label", "")
            parts.append(text(cx + 20, cy, label, 15, text_fill))
            cx += 20 + text_width(label, 15) + 26
        cx += 12
        for style in items.get("edges", []):
            dash = (f' stroke-dasharray="{style["dash"]}"'
                    if style.get("dash") else "")
            width = 4 if style.get("double") else 2
            parts.append(f'<line x1="{fmt(cx)}" y1="{fmt(cy - 10)}" '
                         f'x2="{fmt(cx + 44)}" y2="{fmt(cy - 10)}" '
                         f'stroke="{muted_fill}" stroke-width="{width}"'
                         f'{dash}/>')
            label = style.get("label", "")
            parts.append(text(cx + 52, cy, label, 13, muted_fill))
            cx += 52 + text_width(label, 13) + 22
        return parts
    for item in items:
        color = item.get("color", colors["accent"])
        label = item.get("label", "")
        label_en = item.get("label_en", "")
        chip_w = max(88.0, text_width(label, 13) + text_width(label_en, 9) + 40)
        parts.append(f'<rect x="{fmt(cx)}" y="{fmt(cy - 22)}" '
                     f'width="{fmt(chip_w)}" height="38" rx="19" '
                     f'fill="{canvas.get("card_fill", "#ffffff")}" '
                     f'stroke="{canvas.get("card_stroke", colors["line"])}" '
                     f'stroke-width="1"/>')
        parts.append(f'<circle cx="{fmt(cx + 18)}" cy="{fmt(cy - 3)}" '
                     f'r="8" fill="{color}" fill-opacity="0.14"/>')
        parts += _legend_icon(item.get("icon", ""), cx + 18, cy - 3, color)
        parts.append(text(cx + 34, cy - 5, label, 12.5, text_fill,
                          bold=True))
        if label_en:
            parts.append(text(cx + 34, cy + 9, label_en, 8.5, muted_fill))
        cx += chip_w + 10
    return parts


def _quote_block(qx: float, y: float, quote: str, by: str,
                 theme: dict[str, Any], *, width_units: float = 21) -> list[str]:
    """Right-aligned italic quote lines + attribution."""
    colors = theme["colors"]
    header_fill = theme["canvas"].get("header_fill")
    quote_fill = colors.get("header_text", colors["title"]) if header_fill else colors["title"]
    muted_fill = colors.get("header_muted", colors["muted"]) if header_fill else colors["muted"]
    parts: list[str] = []
    lines = wrap(quote, width_units)[:3]
    for i, line in enumerate(lines):
        parts.append(text(qx, y + 24 + i * 20, line, 14, quote_fill,
                          anchor="end", italic=True))
    if by:
        parts.append(text(qx, y + 24 + len(lines) * 20 + 4, f"—— {by}", 12,
                          muted_fill, anchor="end"))
    return parts


def _draw_header_map(x: float, y: float, w: float, h: float,
                     payload: dict[str, Any],
                     theme: dict[str, Any]) -> list[str]:
    """Compact right-header concept chain for prologue/foundations volumes."""
    colors = theme["colors"]
    canvas = theme["canvas"]
    title = payload.get("title", "")
    subtitle = payload.get("subtitle", "")
    steps = payload.get("steps", [])
    accent = payload.get("color", colors.get("accent", "#2563eb"))
    parts: list[str] = []

    parts.append(f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" '
                 f'height="{fmt(h)}" rx="14" fill="#ffffff" fill-opacity="0.76" '
                 f'stroke="{canvas.get("card_stroke", colors["line"])}" '
                 f'stroke-width="1.1"/>')
    parts.append(f'<rect x="{fmt(x)}" y="{fmt(y)}" width="5" '
                 f'height="{fmt(h)}" rx="2.5" fill="{accent}"/>')
    if title:
        parts.append(text(x + 20, y + 26, title, 15, colors["title"], bold=True))
    if subtitle:
        parts.append(text(x + 20, y + 46, fit(subtitle, (w - 44) / 8.8),
                          10.5, colors["muted"]))

    if not steps:
        return parts

    step_count = min(len(steps), 5)
    gap = 8.0
    sx = x + 18
    sy = y + h - 42
    node_w = (w - 36 - gap * (step_count - 1)) / step_count
    for i, step in enumerate(steps[:step_count]):
        nx = sx + i * (node_w + gap)
        color = step.get("color", accent)
        parts.append(f'<rect x="{fmt(nx)}" y="{fmt(sy)}" width="{fmt(node_w)}" '
                     f'height="28" rx="14" fill="{color}" fill-opacity="0.10" '
                     f'stroke="{color}" stroke-opacity="0.45"/>')
        parts += _icon(step.get("icon", "circles"), nx + 16, sy + 14, 12, color)
        parts.append(text(nx + 30, sy + 18,
                          fit(step.get("label", ""), (node_w - 36) / 10.0),
                          10.5, colors["title"], bold=True))
        if i < step_count - 1:
            ax = nx + node_w + 1
            ay = sy + 14
            parts.append(f'<path d="M {fmt(ax)} {fmt(ay)} L {fmt(ax + gap - 2)} {fmt(ay)}" '
                         f'stroke="{accent}" stroke-width="1.4" stroke-opacity="0.55"/>')
            parts.append(f'<path d="M {fmt(ax + gap - 2)} {fmt(ay)} '
                         f'L {fmt(ax + gap - 6)} {fmt(ay - 3)} '
                         f'L {fmt(ax + gap - 6)} {fmt(ay + 3)} Z" '
                         f'fill="{accent}" fill-opacity="0.55"/>')
    return parts


def _draw_header(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Unified header skeleton (S2) — identical zone layout on every volume.

    Zones (theme colors may vary, the skeleton may not):
      1. series line + volume chip (top-left)
      2. zh title + en subtitle (center-left)
      3. tagline (under the subtitle)
      4. right quote block or compact concept map
    """
    colors = theme["colors"]
    meta = panel.payload.get("meta", panel.payload)
    x, y, w = panel.x, panel.y, panel.width
    bright = colors.get("header_accent", _bright(theme))
    dark = _is_dark(theme)

    header_fill = theme["canvas"].get("header_fill")
    title_fill = colors.get("header_title", colors["title"]) if header_fill else colors["title"]
    muted_fill = colors.get("header_muted", colors["muted"]) if header_fill else colors["muted"]

    parts: list[str] = []
    if header_fill:
        parts.append(_frame(
            panel, theme, fill=header_fill,
            stroke=theme["canvas"].get("header_stroke"), shadow=False))

    # 1. series line + volume chip -------------------------------------------
    series = meta.get("series", "AI Technology Bible")
    parts.append(text(x + (12 if header_fill else 0), y + 26, series, 17,
                      bright, bold=True, spacing=2))
    volume = meta.get("volume", "")
    if volume:
        vx = x + (12 if header_fill else 0) + text_width(series, 17) + 2 * 2 + 14
        chip_fill = colors.get("header_chip_fill", _YELLOW if dark else colors["accent"])
        chip_text = colors.get("header_chip_text", "#1a2332" if dark else "#ffffff")
        parts += _chip(vx, y + 6, text_width(volume, 13) + 24, 26, volume,
                       fill=chip_fill, text_fill=chip_text, size=13)

    # 2. zh title + en subtitle -----------------------------------------------
    title_zh = meta.get("title_zh", "")
    title_size = float(theme.get("typography", {}).get("header_title_size", 46.0))
    title_x = x + (12 if header_fill else 0)
    parts.append(text(title_x, y + 82, title_zh, title_size, title_fill,
                      bold=True))
    sub = meta.get("title_sub", "")
    if sub:
        parts.append(text(title_x + text_width(title_zh, title_size) + 24, y + 78,
                          sub, 24, bright, bold=True))
    title_en = meta.get("title_en", "")
    if title_en:
        subtitle_size = float(theme.get("typography", {}).get("header_subtitle_size", 19.0))
        parts.append(text(title_x, y + 116, title_en, subtitle_size, muted_fill))

    # 3. tagline / banner ribbon ------------------------------------------------
    tagline = meta.get("tagline", "") or meta.get("banner", "")
    if tagline:
        ribbon_h = 24.0
        ribbon_y = y + (118 if header_fill else 124)
        # Colored ribbon band extending across most of the panel width
        ribbon_color = panel.color or colors["accent"]
        parts.append(
            f'<rect x="{fmt(title_x)}" y="{fmt(ribbon_y)}" '
            f'width="{fmt(w - (24 if header_fill else 0))}" '
            f'height="{fmt(ribbon_h)}" rx="6" '
            f'fill="{ribbon_color}" fill-opacity="0.12"/>')
        parts.append(
            f'<rect x="{fmt(title_x)}" y="{fmt(ribbon_y)}" width="6" '
            f'height="{fmt(ribbon_h)}" rx="3" fill="{ribbon_color}"/>')
        parts.append(text(title_x + 18, ribbon_y + ribbon_h / 2 + 5, tagline, 13,
                          ribbon_color, bold=True))

    # 4. right quote block / compact concept map ------------------------------
    quote = meta.get("quote", "") or meta.get("callout", "")
    header_map = meta.get("header_map")
    if isinstance(header_map, dict):
        map_w = min(560.0, w * 0.42)
        parts += _draw_header_map(x + w - map_w, y + 18, map_w, 112,
                                  header_map, theme)
    elif quote:
        parts += _quote_block(x + w - (12 if header_fill else 0), y + 26, quote,
                              meta.get("quote_by", ""), theme,
                              width_units=22)
    return parts


# -- schematic mini diagrams -----------------------------------------------------


def _schematic(kind: str, x: float, y: float, w: float, h: float,
               ink: str) -> list[str]:
    """Simple schematic placeholder for a card's mini diagram area."""
    parts: list[str] = []
    cx, cy = x + w / 2, y + h / 2

    def box(bx: float, by: float, bw: float, bh: float, r: float = 4) -> str:
        return (f'<rect x="{fmt(bx)}" y="{fmt(by)}" width="{fmt(bw)}" '
                f'height="{fmt(bh)}" rx="{fmt(r)}" fill="none" '
                f'stroke="{ink}" stroke-width="1.5"/>')

    def line(x1: float, y1: float, x2: float, y2: float, sw: float = 1.2,
             dash: str = "") -> str:
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return (f'<line x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" '
                f'y2="{fmt(y2)}" stroke="{ink}" stroke-width="{fmt(sw)}"{d}/>')

    if kind in ("board", "grid"):
        n = 6 if kind == "board" else 4
        side = min(w, h) - 8
        gx, gy = cx - side / 2, cy - side / 2
        parts.append(box(gx, gy, side, side, 2))
        for i in range(1, n):
            parts.append(line(gx + side * i / n, gy, gx + side * i / n, gy + side))
            parts.append(line(gx, gy + side * i / n, gx + side, gy + side * i / n))
    elif kind == "net":
        cols = ((x + 10, 3), (cx, 4), (x + w - 10, 2))
        positions: list[list[tuple[float, float]]] = []
        for col_x, count in cols:
            ys = [y + 8 + (h - 16) * (i + 1) / (count + 1) for i in range(count)]
            positions.append([(col_x, py) for py in ys])
        for a, b in zip(positions, positions[1:]):
            for ax, ay in a:
                for bx, by in b:
                    parts.append(line(ax, ay, bx, by, 0.6))
        for col in positions:
            for px, py in col:
                parts.append(f'<circle cx="{fmt(px)}" cy="{fmt(py)}" r="3.5" '
                             f'fill="{ink}"/>')
    elif kind == "flow":
        bw, bh = (w - 26) / 2 - 8, h * 0.42
        parts.append(box(x + 6, cy - bh / 2, bw, bh))
        parts.append(box(x + 20 + bw, cy - bh / 2, bw, bh))
        parts.append(line(x + 6 + bw + 2, cy, x + 18 + bw, cy, 1.8))
        parts.append(f'<polygon points="{fmt(x + 18 + bw)},{fmt(cy)} '
                     f'{fmt(x + 12 + bw)},{fmt(cy - 3.5)} '
                     f'{fmt(x + 12 + bw)},{fmt(cy + 3.5)}" fill="{ink}"/>')
    elif kind == "curve":
        parts.append(line(x + 8, y + 6, x + 8, y + h - 6, 1.5))
        parts.append(line(x + 8, y + h - 6, x + w - 4, y + h - 6, 1.5))
        parts.append(f'<path d="M {fmt(x + 10)} {fmt(y + 10)} '
                     f'Q {fmt(cx)} {fmt(y + h * 0.45)} '
                     f'{fmt(x + w - 8)} {fmt(y + h - 10)}" fill="none" '
                     f'stroke="{ink}" stroke-width="1.8"/>')
    elif kind == "margin":
        parts.append(line(cx, y + 6, cx, y + h - 6, 1.8))
        for i in range(4):
            parts.append(f'<circle cx="{fmt(x + 12 + i * w * 0.09)}" '
                         f'cy="{fmt(y + 12 + (i % 2) * h * 0.5)}" r="3" '
                         f'fill="{ink}"/>')
            parts.append(f'<rect x="{fmt(x + w - 20 - i * w * 0.09)}" '
                         f'y="{fmt(y + 10 + (i % 2) * h * 0.45)}" width="6" '
                         f'height="6" fill="{ink}"/>')
    elif kind == "stack":
        bw = w * 0.55
        for i in range(3):
            parts.append(box(cx - bw / 2, y + 8 + i * (h - 16) / 3, bw,
                             (h - 16) / 3 - 6, 6))
    elif kind == "encoder":
        bw = (w - 30) / 2
        parts.append(box(x + 6, y + 8, bw, h - 16))
        parts.append(box(x + 24 + bw, y + 8, bw, h - 16))
        parts.append(line(x + 6 + bw + 2, cy, x + 22 + bw, cy, 1.8))
    elif kind == "residual":
        bw, bh = w * 0.4, h * 0.5
        parts.append(box(cx - bw / 2, cy - bh / 2 + 6, bw, bh))
        parts.append(f'<path d="M {fmt(cx - bw / 2 - 8)} {fmt(cy + bh / 2)} '
                     f'Q {fmt(cx - bw / 2 - 8)} {fmt(cy - bh / 2 - 4)} '
                     f'{fmt(cx + bw / 2 + 8)} {fmt(cy - bh / 2 - 4)}" '
                     f'fill="none" stroke="{ink}" stroke-width="1.5"/>')
    elif kind == "attention":
        for row_y in (y + 12, y + h - 12):
            for i in range(5):
                parts.append(f'<circle cx="{fmt(x + 12 + i * (w - 24) / 4)}" '
                             f'cy="{fmt(row_y)}" r="3" fill="{ink}"/>')
        for i in range(5):
            parts.append(line(x + 12 + i * (w - 24) / 4, y + 12,
                              x + 12 + ((i * 2 + 1) % 5) * (w - 24) / 4,
                              y + h - 12, 0.7))
    elif kind == "chat":  # dialog bubbles (chatbots: ELIZA, ChatGPT)
        bw, bh = w * 0.44, h * 0.34
        parts.append(box(x + 4, y + 5, bw, bh, 7))
        parts.append(f'<polygon points="{fmt(x + 12)},{fmt(y + 5 + bh)} '
                     f'{fmt(x + 12)},{fmt(y + 12 + bh)} '
                     f'{fmt(x + 21)},{fmt(y + 5 + bh)}" fill="{ink}"/>')
        bx2, by2 = x + w - 4 - bw, y + h - 5 - bh
        parts.append(box(bx2, by2, bw, bh, 7))
        parts.append(f'<polygon points="{fmt(bx2 + bw - 12)},{fmt(by2)} '
                     f'{fmt(bx2 + bw - 12)},{fmt(by2 - 7)} '
                     f'{fmt(bx2 + bw - 21)},{fmt(by2)}" fill="{ink}"/>')
        for i in range(2):
            parts.append(line(x + 10, y + 13 + i * 8,
                              x + 4 + bw - 10 - i * 12, y + 13 + i * 8, 1.0))
            parts.append(line(bx2 + 10, by2 + 8 + i * 8,
                              bx2 + bw - 10 - i * 12, by2 + 8 + i * 8, 1.0))
    elif kind == "rules":  # IF-THEN rule list (expert systems)
        for i in range(3):
            ry = y + 6 + i * (h - 12) / 3
            rh = (h - 12) / 3 - 5
            cw = w * 0.2
            parts.append(box(x + 4, ry, cw, rh, 2))
            ax = x + 4 + cw + 8
            parts.append(line(x + 6 + cw, ry + rh / 2, ax, ry + rh / 2, 1.5))
            parts.append(f'<polygon points="{fmt(ax)},{fmt(ry + rh / 2)} '
                         f'{fmt(ax - 4.5)},{fmt(ry + rh / 2 - 3)} '
                         f'{fmt(ax - 4.5)},{fmt(ry + rh / 2 + 3)}" '
                         f'fill="{ink}"/>')
            parts.append(line(ax + 5, ry + rh / 2,
                              x + w - 6 - (i % 2) * w * 0.14, ry + rh / 2, 1.1))
    elif kind == "conference":  # people around a table (Dartmouth workshop)
        parts.append(f'<ellipse cx="{fmt(cx)}" cy="{fmt(cy)}" '
                     f'rx="{fmt(w * 0.24)}" ry="{fmt(h * 0.17)}" fill="none" '
                     f'stroke="{ink}" stroke-width="1.5"/>')
        for fx, fy in ((-0.4, -0.2), (0.4, -0.2), (0.0, -0.4),
                       (-0.3, 0.34), (0.3, 0.34)):
            px, py = cx + fx * w, cy + fy * h
            parts.append(f'<circle cx="{fmt(px)}" cy="{fmt(py)}" r="3.2" '
                         f'fill="{ink}"/>')
            parts.append(f'<path d="M {fmt(px - 5)} {fmt(py + 9)} '
                         f'Q {fmt(px)} {fmt(py + 2)} {fmt(px + 5)} '
                         f'{fmt(py + 9)}" fill="none" stroke="{ink}" '
                         f'stroke-width="1.4"/>')
    elif kind == "perceptron":  # single neuron, weighted inputs (Rosenblatt)
        nx, nr = cx + w * 0.06, min(w, h) * 0.17
        for i in range(3):
            iy = y + h * (0.2 + i * 0.3)
            parts.append(f'<circle cx="{fmt(x + 10)}" cy="{fmt(iy)}" r="3" '
                         f'fill="{ink}"/>')
            parts.append(line(x + 13, iy, nx - nr * 0.9,
                              cy + (iy - cy) * 0.4, 1.0))
        parts.append(f'<circle cx="{fmt(nx)}" cy="{fmt(cy)}" r="{fmt(nr)}" '
                     f'fill="none" stroke="{ink}" stroke-width="1.6"/>')
        parts.append(line(nx - nr * 0.5, cy, nx + nr * 0.5, cy, 1.3))
        parts.append(line(nx, cy - nr * 0.5, nx, cy + nr * 0.5, 1.3))
        parts.append(line(nx + nr, cy, x + w - 12, cy, 1.6))
        parts.append(f'<polygon points="{fmt(x + w - 6)},{fmt(cy)} '
                     f'{fmt(x + w - 12)},{fmt(cy - 3.5)} '
                     f'{fmt(x + w - 12)},{fmt(cy + 3.5)}" fill="{ink}"/>')
    elif kind == "conv":  # conv kernel over a grid -> feature map (CNNs)
        n = 4
        side = min(h - 10, w * 0.42)
        gx, gy = x + 5, cy - side / 2
        parts.append(box(gx, gy, side, side, 1))
        for i in range(1, n):
            parts.append(line(gx + side * i / n, gy,
                              gx + side * i / n, gy + side, 0.8))
            parts.append(line(gx, gy + side * i / n,
                              gx + side, gy + side * i / n, 0.8))
        ks = side / n * 2  # highlighted kernel window
        parts.append(f'<rect x="{fmt(gx + side / n)}" y="{fmt(gy + side / n)}" '
                     f'width="{fmt(ks)}" height="{fmt(ks)}" fill="none" '
                     f'stroke="{ink}" stroke-width="2.4"/>')
        fx0, fs = gx + side + 16, side * 0.62
        parts.append(line(gx + side + 3, cy, fx0 - 4, cy, 1.6))
        parts.append(f'<polygon points="{fmt(fx0)},{fmt(cy)} '
                     f'{fmt(fx0 - 5)},{fmt(cy - 3.5)} '
                     f'{fmt(fx0 - 5)},{fmt(cy + 3.5)}" fill="{ink}"/>')
        parts.append(box(fx0, cy - fs / 2, fs, fs, 1))
        parts.append(line(fx0 + fs / 2, cy - fs / 2,
                          fx0 + fs / 2, cy + fs / 2, 0.8))
        parts.append(line(fx0, cy, fx0 + fs, cy, 0.8))
        parts.append(f'<rect x="{fmt(fx0)}" y="{fmt(cy - fs / 2)}" '
                     f'width="{fmt(fs / 2)}" height="{fmt(fs / 2)}" '
                     f'fill="{ink}"/>')
    elif kind == "lstm":  # recurrent cell with gates (LSTM/RNN)
        bw, bh = w * 0.34, h * 0.46
        bx, by = cx - bw / 2, cy - bh / 2 + 3
        parts.append(f'<path d="M {fmt(bx + bw * 0.75)} {fmt(by)} '
                     f'C {fmt(bx + bw * 0.75)} {fmt(by - 14)}, '
                     f'{fmt(bx + bw * 0.25)} {fmt(by - 14)}, '
                     f'{fmt(bx + bw * 0.25)} {fmt(by - 3)}" fill="none" '
                     f'stroke="{ink}" stroke-width="1.3"/>')
        parts.append(f'<polygon points="{fmt(bx + bw * 0.25)},{fmt(by + 1)} '
                     f'{fmt(bx + bw * 0.25 - 3.2)},{fmt(by - 4.5)} '
                     f'{fmt(bx + bw * 0.25 + 3.2)},{fmt(by - 4.5)}" '
                     f'fill="{ink}"/>')
        parts.append(box(bx, by, bw, bh, 8))
        parts.append(line(bx - 12, by + bh * 0.25, bx + bw + 12,
                          by + bh * 0.25, 1.3))
        for gxf in (-0.18, 0.18):  # gate symbols (sigma circles with x)
            gx0 = bx + bw / 2 + gxf * bw
            gy0 = by + bh * 0.62
            parts.append(f'<circle cx="{fmt(gx0)}" cy="{fmt(gy0)}" r="3.6" '
                         f'fill="none" stroke="{ink}" stroke-width="1.2"/>')
            parts.append(line(gx0 - 1.8, gy0 - 1.8, gx0 + 1.8, gy0 + 1.8, 1.0))
            parts.append(line(gx0 - 1.8, gy0 + 1.8, gx0 + 1.8, gy0 - 1.8, 1.0))
        parts.append(line(cx, y + h - 4, cx, by + bh + 4, 1.5))
        parts.append(f'<polygon points="{fmt(cx)},{fmt(by + bh)} '
                     f'{fmt(cx - 3.5)},{fmt(by + bh + 5)} '
                     f'{fmt(cx + 3.5)},{fmt(by + bh + 5)}" fill="{ink}"/>')
    elif kind == "embedding":  # words projected into vector space (Word2Vec)
        parts.append(line(x + 6, y + h - 6, x + w - 8, y + h - 6, 1.0))
        parts.append(line(x + 6, y + h - 6, x + 6, y + 6, 1.0))
        for px, py in ((0.16, 0.32), (0.22, 0.6), (0.3, 0.42),
                       (0.68, 0.36), (0.78, 0.62), (0.88, 0.3)):
            parts.append(f'<circle cx="{fmt(x + px * w)}" '
                         f'cy="{fmt(y + py * h)}" r="2.6" fill="{ink}"/>')
        ex, ey = x + 0.66 * w, y + 0.34 * h
        parts.append(f'<path d="M {fmt(x + 0.32 * w)} {fmt(y + 0.42 * h)} '
                     f'Q {fmt(cx)} {fmt(y + 0.12 * h)} {fmt(ex - 4)} '
                     f'{fmt(ey)} " fill="none" stroke="{ink}" '
                     f'stroke-width="1.2"/>')
        parts.append(f'<polygon points="{fmt(ex)},{fmt(ey)} '
                     f'{fmt(ex - 6)},{fmt(ey - 3)} {fmt(ex - 5.5)},'
                     f'{fmt(ey + 3)}" fill="{ink}"/>')
    elif kind == "brain":  # brain-ish network blob (Google Brain)
        parts.append(
            f'<path d="M {fmt(x + 0.2 * w)} {fmt(cy)} '
            f'C {fmt(x + 0.12 * w)} {fmt(y + 0.12 * h)}, '
            f'{fmt(x + 0.42 * w)} {fmt(y + 0.04 * h)}, '
            f'{fmt(cx)} {fmt(y + 0.16 * h)} '
            f'C {fmt(x + 0.68 * w)} {fmt(y + 0.02 * h)}, '
            f'{fmt(x + 0.9 * w)} {fmt(y + 0.2 * h)}, '
            f'{fmt(x + 0.82 * w)} {fmt(cy)} '
            f'C {fmt(x + 0.92 * w)} {fmt(y + 0.72 * h)}, '
            f'{fmt(x + 0.62 * w)} {fmt(y + 0.92 * h)}, '
            f'{fmt(cx)} {fmt(y + 0.82 * h)} '
            f'C {fmt(x + 0.34 * w)} {fmt(y + 0.94 * h)}, '
            f'{fmt(x + 0.08 * w)} {fmt(y + 0.76 * h)}, '
            f'{fmt(x + 0.2 * w)} {fmt(cy)} Z" fill="none" stroke="{ink}" '
            f'stroke-width="1.5"/>')
        nodes = [(0.36, 0.4), (0.52, 0.3), (0.66, 0.46),
                 (0.44, 0.6), (0.6, 0.64)]
        for a, b in ((0, 1), (1, 2), (0, 3), (2, 4), (3, 4), (1, 3)):
            parts.append(line(x + nodes[a][0] * w, y + nodes[a][1] * h,
                              x + nodes[b][0] * w, y + nodes[b][1] * h, 0.7))
        for px, py in nodes:
            parts.append(f'<circle cx="{fmt(x + px * w)}" '
                         f'cy="{fmt(y + py * h)}" r="2.4" fill="{ink}"/>')
    elif kind == "gpu":  # compute chip with pins (GPU-driven training)
        side = min(w, h) - 16
        gx, gy = cx - side / 2, cy - side / 2
        parts.append(box(gx, gy, side, side, 3))
        inner = side * 0.46
        parts.append(box(cx - inner / 2, cy - inner / 2, inner, inner, 2))
        for i in range(4):
            t = (i + 1) / 5
            parts.append(line(gx + side * t, gy - 5, gx + side * t, gy, 1.4))
            parts.append(line(gx + side * t, gy + side,
                              gx + side * t, gy + side + 5, 1.4))
            parts.append(line(gx - 5, gy + side * t, gx, gy + side * t, 1.4))
            parts.append(line(gx + side, gy + side * t,
                              gx + side + 5, gy + side * t, 1.4))
    elif kind == "go":  # Go board with stones (AlphaGo)
        n = 4  # 5x5 lines evoke the 19x19 board in miniature
        side = min(w, h) - 10
        gx, gy = cx - side / 2, cy - side / 2
        parts.append(box(gx, gy, side, side, 2))
        for i in range(1, n):
            parts.append(line(gx + side * i / n, gy,
                              gx + side * i / n, gy + side, 0.8))
            parts.append(line(gx, gy + side * i / n,
                              gx + side, gy + side * i / n, 0.8))
        sr = side / n * 0.42
        for cxi, cyi, black in ((1, 1, True), (2, 2, False), (3, 1, True),
                                (2, 3, True), (1, 3, False), (3, 3, False)):
            px, py = gx + side * cxi / n, gy + side * cyi / n
            if black:
                parts.append(f'<circle cx="{fmt(px)}" cy="{fmt(py)}" '
                             f'r="{fmt(sr)}" fill="{ink}"/>')
            else:
                parts.append(f'<circle cx="{fmt(px)}" cy="{fmt(py)}" '
                             f'r="{fmt(sr)}" fill="none" stroke="{ink}" '
                             f'stroke-width="1.4"/>')
    elif kind == "rl_loop":  # agent <-> environment loop (RLHF/RL)
        bw, bh = w * 0.26, h * 0.4
        parts.append(box(x + 6, cy - bh / 2, bw, bh))
        parts.append(box(x + w - 6 - bw, cy - bh / 2, bw, bh))
        ax1, ax2 = x + 8 + bw, x + w - 8 - bw
        parts.append(line(ax1, cy - 7, ax2, cy - 7, 1.5))
        parts.append(f'<polygon points="{fmt(ax2 + 4)},{fmt(cy - 7)} '
                     f'{fmt(ax2 - 2)},{fmt(cy - 10.5)} '
                     f'{fmt(ax2 - 2)},{fmt(cy - 3.5)}" fill="{ink}"/>')
        parts.append(line(ax2, cy + 8, ax1, cy + 8, 1.5))
        parts.append(f'<polygon points="{fmt(ax1 - 4)},{fmt(cy + 8)} '
                     f'{fmt(ax1 + 2)},{fmt(cy + 4.5)} '
                     f'{fmt(ax1 + 2)},{fmt(cy + 11.5)}" fill="{ink}"/>')
    elif kind == "feedback":  # thumbs up / down (human feedback)
        up = ((0.26, 0.78), (0.26, 0.48), (0.31, 0.26), (0.36, 0.27),
              (0.33, 0.48), (0.48, 0.48), (0.48, 0.78))
        pts = " ".join(f"{fmt(x + px * w)},{fmt(y + py * h)}" for px, py in up)
        parts.append(f'<polygon points="{pts}" fill="{ink}"/>')
        down = ((0.54, 0.22), (0.54, 0.52), (0.59, 0.74), (0.64, 0.73),
                (0.61, 0.52), (0.76, 0.52), (0.76, 0.22))
        pts = " ".join(f"{fmt(x + px * w)},{fmt(y + py * h)}"
                       for px, py in down)
        parts.append(f'<polygon points="{pts}" fill="none" stroke="{ink}" '
                     f'stroke-width="1.5"/>')
    elif kind == "robot":  # humanoid robot (embodied AI)
        hw = w * 0.3
        parts.append(line(cx, y + h * 0.16, cx, y + h * 0.07, 1.4))
        parts.append(f'<circle cx="{fmt(cx)}" cy="{fmt(y + h * 0.06)}" r="2" '
                     f'fill="{ink}"/>')
        parts.append(box(cx - hw * 0.4, y + h * 0.16, hw * 0.8, h * 0.24, 3))
        for ex in (-0.18, 0.18):
            parts.append(f'<circle cx="{fmt(cx + ex * hw)}" '
                         f'cy="{fmt(y + h * 0.28)}" r="2" fill="{ink}"/>')
        parts.append(line(cx, y + h * 0.4, cx, y + h * 0.45, 1.4))
        parts.append(box(cx - hw * 0.5, y + h * 0.45, hw, h * 0.32, 4))
        parts.append(line(cx - hw * 0.5, y + h * 0.52,
                          cx - hw * 0.74, y + h * 0.68, 1.6))
        parts.append(line(cx + hw * 0.5, y + h * 0.52,
                          cx + hw * 0.74, y + h * 0.68, 1.6))
        parts.append(line(cx - hw * 0.2, y + h * 0.77,
                          cx - hw * 0.2, y + h * 0.94, 1.6))
        parts.append(line(cx + hw * 0.2, y + h * 0.77,
                          cx + hw * 0.2, y + h * 0.94, 1.6))
    elif kind == "globe":  # physical world sphere (world models)
        r = min(w, h) / 2 - 6
        parts.append(f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(r)}" '
                     f'fill="none" stroke="{ink}" stroke-width="1.6"/>')
        parts.append(f'<ellipse cx="{fmt(cx)}" cy="{fmt(cy)}" '
                     f'rx="{fmt(r)}" ry="{fmt(r * 0.42)}" fill="none" '
                     f'stroke="{ink}" stroke-width="1.0"/>')
        parts.append(f'<ellipse cx="{fmt(cx)}" cy="{fmt(cy)}" '
                     f'rx="{fmt(r * 0.42)}" ry="{fmt(r)}" fill="none" '
                     f'stroke="{ink}" stroke-width="1.0"/>')
        parts.append(line(cx - r, cy, cx + r, cy, 1.0))
    elif kind == "multimodal":  # vision + audio + text fusing (GPT-4 etc.)
        ys = (y + h * 0.2, cy, y + h * 0.8)
        parts.append(f'<ellipse cx="{fmt(x + 14)}" cy="{fmt(ys[0])}" rx="7" '
                     f'ry="4.2" fill="none" stroke="{ink}" '
                     f'stroke-width="1.3"/>')
        parts.append(f'<circle cx="{fmt(x + 14)}" cy="{fmt(ys[0])}" r="2" '
                     f'fill="{ink}"/>')
        parts.append(f'<path d="M {fmt(x + 7)} {fmt(ys[1])} '
                     f'L {fmt(x + 10)} {fmt(ys[1] - 5)} '
                     f'L {fmt(x + 13)} {fmt(ys[1] + 4)} '
                     f'L {fmt(x + 16)} {fmt(ys[1] - 4)} '
                     f'L {fmt(x + 19)} {fmt(ys[1] + 3)} '
                     f'L {fmt(x + 22)} {fmt(ys[1])}" fill="none" '
                     f'stroke="{ink}" stroke-width="1.3"/>')
        for i in range(3):
            parts.append(line(x + 7, ys[2] - 4 + i * 4,
                              x + 21 - (i % 2) * 6, ys[2] - 4 + i * 4, 1.2))
        for yy in ys:
            parts.append(line(x + 27, yy, x + w - 18,
                              cy + (yy - cy) * 0.2, 1.1))
        parts.append(f'<circle cx="{fmt(x + w - 13)}" cy="{fmt(cy)}" r="5" '
                     f'fill="{ink}"/>')
    elif kind == "road":  # perspective road + car (autonomous driving)
        parts.append(f'<path d="M {fmt(x + 8)} {fmt(y + h - 6)} '
                     f'L {fmt(cx - w * 0.09)} {fmt(y + 8)} '
                     f'L {fmt(cx + w * 0.09)} {fmt(y + 8)} '
                     f'L {fmt(x + w - 8)} {fmt(y + h - 6)}" fill="none" '
                     f'stroke="{ink}" stroke-width="1.5"/>')
        for i in range(3):  # dashed centre line, shrinking with distance
            y0 = y + h - 14 - i * (h - 26) / 3
            y1 = y0 - (h - 26) / 3 * 0.45
            parts.append(line(cx, y0, cx, y1, 1.6 - i * 0.3))
        parts.append(box(cx - 10, y + h - 26, 20, 11, 3))
        parts.append(f'<circle cx="{fmt(cx - 5)}" cy="{fmt(y + h - 14)}" '
                     f'r="2" fill="{ink}"/>')
        parts.append(f'<circle cx="{fmt(cx + 5)}" cy="{fmt(y + h - 14)}" '
                     f'r="2" fill="{ink}"/>')
    elif kind == "diffusion":  # noise -> ordered image (Stable Diffusion)
        for px, py in ((0.1, 0.25), (0.16, 0.6), (0.22, 0.4), (0.08, 0.72),
                       (0.2, 0.14), (0.26, 0.68), (0.13, 0.46), (0.24, 0.3)):
            parts.append(f'<circle cx="{fmt(x + px * w)}" '
                         f'cy="{fmt(y + py * h)}" r="1.7" fill="{ink}"/>')
        parts.append(line(x + w * 0.3, cy, x + w * 0.46, cy, 1.6))
        parts.append(f'<polygon points="{fmt(x + w * 0.52)},{fmt(cy)} '
                     f'{fmt(x + w * 0.46)},{fmt(cy - 3.5)} '
                     f'{fmt(x + w * 0.46)},{fmt(cy + 3.5)}" fill="{ink}"/>')
        side = min(h - 12, w * 0.36)
        gx, gy = x + w - 5 - side, cy - side / 2
        parts.append(box(gx, gy, side, side, 1))
        for i in (1, 2):
            parts.append(line(gx + side * i / 3, gy,
                              gx + side * i / 3, gy + side, 0.8))
            parts.append(line(gx, gy + side * i / 3,
                              gx + side, gy + side * i / 3, 0.8))
        parts.append(f'<rect x="{fmt(gx)}" y="{fmt(gy)}" '
                     f'width="{fmt(side / 3)}" height="{fmt(side / 3)}" '
                     f'fill="{ink}"/>')
        parts.append(f'<rect x="{fmt(gx + side / 3)}" '
                     f'y="{fmt(gy + side / 3)}" width="{fmt(side / 3)}" '
                     f'height="{fmt(side / 3)}" fill="{ink}"/>')
    else:  # "photo" default: generic image glyph (mountain + sun)
        parts.append(f'<circle cx="{fmt(x + w * 0.68)}" cy="{fmt(y + h * 0.3)}" '
                     f'r="{fmt(min(w, h) * 0.12)}" fill="{ink}"/>')
        parts.append(f'<path d="M {fmt(x + w * 0.14)} {fmt(y + h * 0.8)} '
                     f'L {fmt(x + w * 0.42)} {fmt(y + h * 0.36)} '
                     f'L {fmt(x + w * 0.58)} {fmt(y + h * 0.62)} '
                     f'L {fmt(x + w * 0.72)} {fmt(y + h * 0.48)} '
                     f'L {fmt(x + w * 0.88)} {fmt(y + h * 0.8)} Z" '
                     f'fill="{ink}"/>')
    return parts


# -- section kind: band (era bands, as in Vol.01) -------------------------------


def _draw_side_panel(x: float, y: float, w: float, h: float,
                     side: dict[str, Any], color: str,
                     theme: dict[str, Any]) -> list[str]:
    """Left/right bullet-list column inside a band.

    D2: items justify across the full panel body — pitch clamps to
    [30, 52] and the stack vertically centers when shorter — so the
    panel reaches >= 90% fill at any item count.
    """
    canvas = theme["canvas"]
    colors = theme["colors"]
    fill = canvas.get("band_side_fill", canvas["side_fill"])
    stroke = canvas.get("band_side_stroke", canvas["panel_stroke"])
    radius = float(canvas.get("side_radius", 12))
    parts = [
        f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" '
        f'rx="{fmt(radius)}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="1"/>',
        text(x + 14, y + 28, side.get("title", ""), 17, color, bold=True),
    ]
    items = side.get("items", [])
    max_units = (w - 30) / 14
    region_top = y + 46
    region_h = h - 46 - 10
    if items:
        pitch = min(52.0, max(30.0, region_h / len(items)))
        lines_per = [wrap_fit(item, max_units, 2) for item in items]
        stack = sum(pitch + 15 * (len(lines) - 1) for lines in lines_per)
        if stack > region_h and pitch > 30.0:
            # Wrapped items make the true stack taller than n * pitch;
            # trade pitch back down (never below the 30-unit floor).
            pitch = max(30.0, pitch - (stack - region_h) / len(items))
            stack = sum(pitch + 15 * (len(lines) - 1) for lines in lines_per)
        y_off = max(0.0, (region_h - stack) / 2)
        parts += _bullet_list(x + 14, region_top + 8 + y_off, items,
                              color=color, theme=theme, size=14,
                              row_h=pitch, max_units=max_units)
    return parts


def _draw_card(x: float, y: float, w: float, h: float,
               card: dict[str, Any], color: str,
               theme: dict[str, Any],
               images: ImageEmbedder | None = None) -> list[str]:
    """One model/event card: year chip, titles, image, caption block.

    D1 anatomy: the header (chip + zh/en titles) is frozen; desc and
    citation form ONE bottom-anchored caption block with no internal
    gap; the image is the elastic element filling everything between
    the two, aspect-clamped to [1.25, 1.75]. Geometry is shared with
    the layout pass via helpers (band_card_*), so a short caption never
    opens a void and a long one never overlaps the image.
    """
    canvas = theme["canvas"]
    colors = theme["colors"]
    pad = 8.0
    inner_w = w - 2 * pad
    fill = canvas.get("band_card_fill", canvas["card_fill"])
    stroke = canvas.get("band_card_stroke", canvas["card_stroke"])
    radius = float(canvas.get("card_radius", 10))
    photo_fill = canvas.get("band_photo_fill", canvas["photo_fill"])
    parts = [
        f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" '
        f'rx="{fmt(radius)}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="1.2"/>',
    ]
    # year chip
    year = str(card.get("year", ""))
    chip_w = text_width(year, 14) + 18
    parts.append(f'<rect x="{fmt(x + pad)}" y="{fmt(y + pad)}" '
                 f'width="{fmt(chip_w)}" height="22" rx="11" fill="{color}"/>')
    parts.append(text(x + pad + chip_w / 2, y + pad + 16, year, 14,
                      colors.get("chip_text", "#ffffff"), bold=True,
                      anchor="middle"))
    org = card.get("org", "")
    if org:
        parts.append(text(x + w - pad, y + pad + 16, trunc(org, 10), 11,
                          colors["muted"], anchor="end"))
    # titles (zh title may wrap to a second line when long)
    title_y = y + pad + 42
    title_lines = wrap(card.get("title", ""), inner_w / 16)[:2]
    for i, line_text in enumerate(title_lines):
        parts.append(text(x + pad, title_y + i * 17, line_text, 16,
                          colors["title"], bold=True))
    title_en = card.get("title_en", "")
    en_y = title_y + 17 * len(title_lines)
    if title_en:
        parts.append(text(x + pad, en_y, fit(title_en, inner_w / 11), 11,
                          colors["muted"]))
    # Elastic image zone (polaroid matte + raster/ schematic fill).
    header_h = band_card_header_offset(card, inner_w)
    desc_lines, cite_lines = band_card_caption_lines(card, inner_w)
    caption_h = band_card_caption_height(desc_lines, cite_lines)
    photo_y = y + header_h
    photo_h = h - header_h - caption_h
    # Aspect clamp: never squarer than 1.25:1 — cap the image and let the
    # caption follow it top-anchored (bottom void stays <= 8% by rule 3).
    max_photo_h = inner_w / 1.25
    top_anchored = photo_h > max_photo_h
    if top_anchored:
        photo_h = max_photo_h
    parts.append(f'<rect x="{fmt(x + pad)}" y="{fmt(photo_y)}" '
                 f'width="{fmt(inner_w)}" height="{fmt(photo_h)}" rx="6" '
                 f'fill="{photo_fill}"/>')
    # A real raster image (card["image"]) sits inset on the matte so a thin
    # uniform border of photo_fill shows around it (polaroid look); the line
    # schematic stays as fallback when no image is set or it fails to load.
    drawn = (images.svg_image(card["image"], x + pad + 6, photo_y + 6,
                              inner_w - 12, photo_h - 12,
                              focus=card.get("image_focus", "center"),
                              radius=4)
             if images is not None and card.get("image") else None)
    if drawn is not None:
        parts += drawn
    else:
        parts += _schematic(card.get("diagram", "photo"),
                            x + pad + 6, photo_y + 6, inner_w - 12,
                            photo_h - 12, canvas["photo_ink"])
    # Caption block: desc + citation as ONE unit, bottom-anchored unless
    # the aspect clamp capped the image (then it follows the image).
    caption_y = (photo_y + photo_h + 8) if top_anchored else (y + h - caption_h)
    for line_text in desc_lines:
        caption_y += 15
        parts.append(text(x + pad, caption_y, line_text, 12, colors["text"]))
    if desc_lines and cite_lines:
        caption_y += 4
    for line_text in cite_lines:
        caption_y += 12
        parts.append(text(x + pad, caption_y, line_text, 9.5,
                          colors["muted"], italic=True))
    return parts


def _draw_band(panel: Panel, theme: dict[str, Any],
               images: ImageEmbedder | None = None) -> list[str]:
    """One era band: header + left panel + card row + right panel."""
    colors = theme["colors"]
    canvas = theme["canvas"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    x, y, w = panel.x, panel.y, panel.width
    header_h = float(canvas.get("band_header_h", 64))
    side_w = float(payload.get("side_w", 190))

    band_fill = canvas.get("band_panel_fill", canvas["panel_fill"])
    band_stroke = canvas.get("band_panel_stroke", canvas["panel_stroke"])
    parts = [_frame(panel, theme, fill=band_fill, stroke=band_stroke)]

    # -- band header: number chip + title + years + subtitle ----------------
    hx = x + 16
    number = payload.get("number")
    number_style = payload.get("number_style", "chip")
    if number is not None:
        chip_cx, chip_cy = hx + 18, y + header_h / 2
        if number_style == "circle":
            parts.append(f'<circle cx="{fmt(chip_cx)}" cy="{fmt(chip_cy)}" '
                         f'r="17" fill="none" stroke="{color}" '
                         f'stroke-width="2.5"/>')
            parts.append(text(chip_cx, chip_cy + 7, str(number), 20, color,
                              bold=True, anchor="middle"))
        else:  # "chip": filled circle
            parts.append(f'<circle cx="{fmt(chip_cx)}" cy="{fmt(chip_cy)}" '
                         f'r="17" fill="{color}"/>')
            parts.append(text(chip_cx, chip_cy + 7, str(number), 20,
                              colors.get("chip_text", "#ffffff"), bold=True,
                              anchor="middle"))
        hx += 46
    title = payload.get("title", "")
    title_size = 26.0
    parts.append(text(hx, y + header_h / 2 + 9, title, title_size, color,
                      bold=True))
    hx += text_width(title, title_size) + 18
    years = payload.get("years", "")
    if years:
        parts.append(text(hx, y + header_h / 2 + 7, years, 17,
                          colors["title"], bold=True))
        hx += text_width(years, 17) + 14
    subtitle = payload.get("subtitle", "")
    if subtitle:
        parts.append(text(hx, y + header_h / 2 + 6, f"|  {subtitle}", 15,
                          colors["muted"]))

    # -- content: side panels + card row --------------------------------------
    # D1 rule 6: band bottom padding is 8 (was 16) to absorb card growth.
    content_y = y + header_h + 4
    content_h = panel.height - header_h - 12
    cards_x = x + 12
    cards_w = w - 24
    left = payload.get("left_panel")
    right = payload.get("right_panel")
    if left:
        parts += _draw_side_panel(cards_x, content_y, side_w, content_h,
                                  left, color, theme)
        cards_x += side_w + 12
        cards_w -= side_w + 12
    if right:
        parts += _draw_side_panel(x + w - 12 - side_w, content_y, side_w,
                                  content_h, right, color, theme)
        cards_w -= side_w + 12

    cards = payload.get("cards", [])
    if cards:
        card_gap = 10.0
        card_w = (cards_w - (len(cards) - 1) * card_gap) / len(cards)
        for i, card in enumerate(cards):
            parts += _draw_card(cards_x + i * (card_w + card_gap), content_y,
                                card_w, content_h, card, color, theme, images)
    return parts


# -- section kind: list ------------------------------------------------------------


def _draw_list(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Titled bullet/icon list panel (items may carry title + desc + icon).

    Item titles wrap to two lines (dropping one font step on narrow
    columns) instead of hard-ellipsizing; the uniform row height comes
    from the shared geometry helpers so layout reserves exactly the same
    vertical space — the void below the items is put to use.
    """
    colors = theme["colors"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    parts, content_y = _panel_chrome(panel, theme, payload.get("title", ""),
                                     payload.get("subtitle", ""))
    items = payload.get("items", [])
    cols = max(int(payload.get("columns", 1)), 1)
    col_w = (panel.width - 40 - (cols - 1) * 20) / cols
    row_h = list_row_height(items, col_w)
    per_col = math.ceil(len(items) / cols)
    # D5 density: when a row sibling stretches this panel beyond its
    # content, first grow the row pitch (up to 1.4x natural), then
    # center the items vertically above any remainder (the summary line
    # stays bottom-anchored).
    summary = payload.get("summary", "")
    reserve = 36 if summary else 14
    panel_bottom = panel.y + panel.height - reserve
    slack = panel_bottom - (content_y + 10 + per_col * row_h)
    if slack > 0 and per_col:
        row_h = min(row_h * 1.4, row_h + slack / per_col)
        slack = panel_bottom - (content_y + 10 + per_col * row_h)
    y_off = slack / 2 if slack > 30 else 0.0
    for i, item in enumerate(items):
        col, row = divmod(i, per_col)
        ix = panel.x + 20 + col * (col_w + 20)
        iy = content_y + 10 + y_off + row * row_h
        if isinstance(item, str):
            item = {"title": item}
        icon = item.get("icon", "")
        marker = payload.get("marker", "dot")
        if icon:
            parts += _icon(icon, ix + 12, iy + 4, 10, color)
        elif marker == "check":
            parts += _icon("check", ix + 10, iy + 2, 8, color)
        else:
            parts.append(f'<circle cx="{fmt(ix + 8)}" cy="{fmt(iy + 2)}" '
                         f'r="5" fill="{color}"/>')
        title_lines, title_size, desc_lines = list_item_layout(item, col_w)
        for j, line in enumerate(title_lines):
            parts += _text_rich(ix + 28, iy + 8 + j * 17, line, title_size,
                                colors["title"], bold=True)
        desc_y = iy + 8 + 17 * (len(title_lines) - 1) + 20
        for j, line in enumerate(desc_lines):
            parts += _text_rich(ix + 28, desc_y + j * 15, line, 11.5,
                                colors["muted"])
    if summary:
        sy = panel.y + panel.height - 18
        parts.append(text(panel.x + panel.width / 2, sy, summary, 15, color,
                          bold=True, anchor="middle"))
    # S8 declutter: the pale "illustration" ornament (cube/brain radar
    # circles) was removed engine-wide; the JSON key is ignored.
    return parts


# -- section kind: cards (grid of small titled cards) -------------------------------


def _draw_cards_panel(panel: Panel, theme: dict[str, Any],
                      images: ImageEmbedder | None = None) -> list[str]:
    """Grid of small cards (icon + zh/en title + bullets), pastel-tinted.

    Card titles and bullets wrap (two lines at full size, one font step
    down on narrow cards) instead of hard-ellipsizing; the uniform card
    height comes from the shared geometry helpers so layout reserves
    exactly the same vertical space.

    D3 image-ready geometry: a card carrying an ``image`` key draws a
    top image strip (42% of the card body, aspect clamped to [1.6, 2.2],
    elastic under stretch) with the icon demoted to a 20-unit badge on
    the strip's bottom-left corner; without ``image`` nothing is drawn
    (no placeholder holes) and sparse cards (<= 2 bullets) get a larger
    18-unit icon. D3 min-fill: cards whose bullets zone would cover less
    than 55% of the body step title/bullet fonts up one step. D5: when a
    row sibling stretches the panel, card boxes grow up to 1.4x and the
    grid centers vertically.
    """
    colors = theme["colors"]
    canvas = theme["canvas"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    parts, content_y = _panel_chrome(panel, theme, payload.get("title", ""),
                                     payload.get("subtitle", ""))
    items = payload.get("items", [])
    cols = max(int(payload.get("columns", 3)), 1)
    gap = 10.0
    card_w = (panel.width - 32 - (cols - 1) * gap) / cols
    card_h = cards_panel_card_height(items, card_w)
    rows = math.ceil(len(items) / cols) or 1
    # D5.3 row equalization: when a row sibling stretches this panel,
    # the card boxes grow to fill the cell and each card distributes
    # its share of the leftover into its internal bullet pitch (or
    # centers bullet-less content) instead of hugging the top.
    avail = panel.y + panel.height - 10 - (content_y + 6)
    grid_nat = rows * (card_h + gap) - gap
    if avail > grid_nat:
        card_h = (avail - (rows - 1) * gap) / rows
    for i, card in enumerate(items):
        row, col = divmod(i, cols)
        cx = panel.x + 16 + col * (card_w + gap)
        cy = content_y + 6 + row * (card_h + gap)
        card_color = card.get("color", color)
        step_up = card_step_up(card, card_w)
        geo = cards_geometry(step_up)
        # Neutral border (S5): accent lives in the icon/bullets only, so a
        # panel of mixed-color items reads as one calm grid, not confetti.
        parts.append(f'<rect x="{fmt(cx)}" y="{fmt(cy)}" width="{fmt(card_w)}" '
                     f'height="{fmt(card_h)}" rx="10" '
                     f'fill="{canvas["card_fill"]}" '
                     f'stroke="{canvas["card_stroke"]}" stroke-width="1.2"/>')
        title_en = card.get("title_en", "")
        icon = card.get("icon", "")
        bullets = card.get("items", [])
        # D5.3: the box may be taller than the text zone (row-sibling
        # stretch). Cards with an image let the strip absorb it (elastic);
        # cards with bullets spread it across the bullet pitch; bullet-
        # less cards center their text zone vertically.
        bonus = 0.0
        center_off = 0.0
        if not card.get("image"):
            slack_in = max(0.0, card_h - card_text_height(card, card_w,
                                                          step_up))
            if bullets:
                bonus = slack_in / len(bullets)
            else:
                center_off = slack_in / 2
        # Optional top image strip (D3): rendered only when the card has
        # an "image" key — no placeholder hole otherwise.
        text_top = cy + center_off
        if card.get("image"):
            strip_w = card_w - 20
            image_h = card_image_height(card, card_w, card_h)
            drawn = (images.svg_image(card["image"], cx + 10, cy + 10,
                                      strip_w, image_h,
                                      focus=card.get("image_focus", "center"),
                                      radius=6)
                     if images is not None else None)
            if drawn is not None:
                parts += drawn
                if icon:
                    # 20-unit badge overlapping the strip's bottom-left.
                    bcx, bcy = cx + 24, cy + 10 + image_h
                    parts.append(f'<circle cx="{fmt(bcx)}" cy="{fmt(bcy)}" '
                                 f'r="10" fill="{card_color}" '
                                 f'stroke="{canvas["card_fill"]}" '
                                 f'stroke-width="2"/>')
                    parts += _icon(icon, bcx, bcy, 6,
                                   colors.get("chip_text", "#ffffff"))
                text_top = cy + 18 + image_h
                icon = ""  # icon already drawn as the strip badge
        tx = cx + 12
        if icon:
            # D3.2: sparse cards (<= 2 bullets) get an 18-unit icon.
            icon_s = 14.0 if len(bullets) <= 2 else 10.0
            parts += _icon(icon, cx + 18, text_top + 20, icon_s, card_color)
            tx = cx + 36
        title_lines, title_size = card_title_layout(card, card_w, tx - cx,
                                                    step_up)
        title_fill = card_color if _is_dark(theme) else colors["title"]
        for j, line in enumerate(title_lines):
            parts.append(text(tx, text_top + 20 + j * geo["title_pitch"],
                              line, title_size, title_fill, bold=True))
        if title_en:
            en_x = tx + text_width(title_lines[-1], title_size) + 8
            en_y = (text_top + 19
                    + geo["title_pitch"] * (len(title_lines) - 1))
            parts.append(text(en_x, en_y, fit(title_en, 16), 10,
                              colors["muted"]))
        by = (text_top + geo["bullets_start"]
              + geo["title_pitch"] * (len(title_lines) - 1))
        desc = card.get("desc", "")
        if desc and bullets:
            parts.append(text(cx + 12, by, fit(desc, (card_w - 24) / 10.5),
                              10.5, colors["muted"]))
            by += geo["desc_row"]
        for bullet in bullets:
            lines, size = card_bullet_layout(str(bullet), card_w, step_up)
            pitch = card_bullet_pitch(size)
            parts.append(f'<circle cx="{fmt(cx + 16)}" cy="{fmt(by - 4)}" '
                         f'r="3" fill="{card_color}"/>')
            for j, line in enumerate(lines):
                parts.append(text(cx + 26, by + j * pitch, line, size,
                                  colors["text"]))
            by += pitch * (len(lines) - 1) + geo["bullet_row"] + bonus
        if desc and not bullets:
            for j, line in enumerate(wrap_fit(desc, (card_w - 24) / 11, 3)):
                parts.append(text(cx + 12, by + j * 15, line, 11,
                                  colors["muted"]))
    return parts


# -- section kind: table -------------------------------------------------------------


def _draw_table(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Simple table with a colored header row and alternating row fills."""
    colors = theme["colors"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    parts, content_y = _panel_chrome(panel, theme, payload.get("title", ""),
                                     payload.get("subtitle", ""))
    columns = payload.get("columns", [])
    rows = payload.get("rows", [])
    if not columns:
        return parts
    tx, ty = panel.x + 16, content_y + 6
    tw = panel.width - 32
    weights = payload.get("col_widths", [1.0] * len(columns))
    total = sum(weights)
    col_ws = [tw * wgt / total for wgt in weights]
    row_h = 30.0
    parts.append(f'<rect x="{fmt(tx)}" y="{fmt(ty)}" width="{fmt(tw)}" '
                 f'height="{fmt(row_h)}" rx="8" fill="{color}"/>')
    cx = tx
    for col_w, heading in zip(col_ws, columns):
        parts.append(text(cx + 12, ty + 24, fit(str(heading), col_w / 13),
                          13, "#ffffff", bold=True))
        cx += col_w
    canvas = theme["canvas"]
    for r, row in enumerate(rows):
        ry = ty + row_h * (r + 1)
        if r % 2 == 0:
            parts.append(f'<rect x="{fmt(tx)}" y="{fmt(ry)}" width="{fmt(tw)}" '
                         f'height="{fmt(row_h)}" fill="{canvas["side_fill"]}"/>')
        cx = tx
        for col_w, cell in zip(col_ws, row):
            parts.append(text(cx + 12, ry + 24,
                              fit(str(cell), (col_w - 16) / 12), 12,
                              colors["text"]))
            cx += col_w
    return parts


# -- section kind: pills (family-tree / tech-stack pill rows) ------------------------


def _draw_pills(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Rows of labeled pill chips (model family trees, tech stacks)."""
    colors = theme["colors"]
    canvas = theme["canvas"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    parts, content_y = _panel_chrome(panel, theme, payload.get("title", ""),
                                     payload.get("subtitle", ""))
    rows = payload.get("rows", [])
    label_w = float(payload.get("label_w", 150))
    x = panel.x + 16
    y = content_y + 4
    col_header = payload.get("col_header", [])
    if col_header:
        hx = x + label_w + 10
        hw = (panel.width - 32 - label_w - 10) / len(col_header)
        for heading in col_header:
            parts.append(text(hx + hw / 2, y + 14, str(heading), 11,
                              colors["muted"], bold=True, anchor="middle"))
            hx += hw
        y += 26
    for row in rows:
        row_color = row.get("color", color)
        ry = y + 6
        pills = row.get("pills", [])
        breaks = set(pills_line_breaks(pills, panel.width, label_w)[1:])
        n_lines = len(breaks) + 1
        # colored left rail + row label cell
        parts.append(f'<rect x="{fmt(x)}" y="{fmt(ry)}" width="6" '
                     f'height="{fmt(38 + 36 * (n_lines - 1))}" rx="3" '
                     f'fill="{row_color}"/>')
        label = row.get("label", "")
        sublabel = row.get("sublabel", "")
        if label:
            parts.append(text(x + 16, ry + 18, fit(label, (label_w - 20) / 13),
                              13, colors["title"], bold=True))
        if sublabel:
            parts.append(text(x + 16, ry + 34,
                              fit(sublabel, (label_w - 20) / 10), 10,
                              colors["muted"]))
        # pills with connecting arrows; chips that would overflow the
        # panel wrap to a new line instead of being dropped (row height
        # grows by 36 per extra line, kept in sync with layout via
        # pills_line_breaks).
        px0 = x + label_w + 12
        px = px0
        max_px = panel.x + panel.width - 16
        pill_h = 26.0
        line_dy = 0.0
        if payload.get("spread") and pills:
            slot_w = (max_px - px0) / len(pills)
            prev_right = None
            for pill in pills:
                if isinstance(pill, str):
                    pill = {"text": pill}
                label_text = pill.get("text", "")
                pw = min(max(text_width(label_text, 11) + 20, 72), slot_w - 10)
                cx = px + slot_w / 2
                chip_x = cx - pw / 2
                highlight = pill.get("highlight", False)
                fill = row_color if highlight else canvas["card_fill"]
                tfill = "#ffffff" if highlight else colors["text"]
                stroke = "" if highlight else canvas["card_stroke"]
                if prev_right is not None and prev_right + 10 < chip_x:
                    parts.append(f'<line x1="{fmt(prev_right + 3)}" y1="{fmt(ry + 19)}" '
                                 f'x2="{fmt(chip_x - 8)}" y2="{fmt(ry + 19)}" '
                                 f'stroke="{colors["muted"]}" stroke-width="1.2" '
                                 f'marker-end="url(#arrowhead)"/>')
                parts += _chip(chip_x, ry + 6, pw, pill_h, label_text,
                               fill=fill, stroke=stroke, text_fill=tfill,
                               size=11, bold=highlight)
                prev_right = chip_x + pw
                px += slot_w
            y += 42
            continue
        for j, pill in enumerate(pills):
            if isinstance(pill, str):
                pill = {"text": pill}
            label_text = pill.get("text", "")
            pw = text_width(label_text, 11) + 20
            if j in breaks:
                px = px0
                line_dy += 36
            highlight = pill.get("highlight", False)
            fill = row_color if highlight else canvas["card_fill"]
            tfill = "#ffffff" if highlight else colors["text"]
            # Neutral border (S5): the row's left rail carries the accent.
            stroke = "" if highlight else canvas["card_stroke"]
            # chip width already derives from the full label, so draw it
            # verbatim (fitting here would ellipsize text that fits fine).
            parts += _chip(px, ry + 6 + line_dy, pw, pill_h, label_text,
                           fill=fill, stroke=stroke, text_fill=tfill,
                           size=11, bold=highlight)
            px += pw
            next_pw = (text_width(pills[j + 1] if isinstance(pills[j + 1], str)
                                  else pills[j + 1].get("text", ""), 11) + 20
                       if j < len(pills) - 1 else 0)
            on_same_line = j + 1 < len(pills) and (j + 1) not in breaks
            if on_same_line and px + 18 < max_px and px + 16 + next_pw <= max_px:
                parts.append(f'<line x1="{fmt(px + 2)}" y1="{fmt(ry + 19 + line_dy)}" '
                             f'x2="{fmt(px + 12)}" y2="{fmt(ry + 19 + line_dy)}" '
                             f'stroke="{colors["muted"]}" stroke-width="1.2" '
                             f'marker-end="url(#arrowhead)"/>')
                px += 16
            else:
                px += 8
        y += 42 + 36 * (n_lines - 1)
    return parts


# -- section kind: chevrons ---------------------------------------------------------


def _draw_chevrons(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Horizontal chevron/step flow (Road to AGI, paradigm arrows)."""
    colors = theme["colors"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    parts, content_y = _panel_chrome(panel, theme, payload.get("title", ""),
                                     payload.get("subtitle", ""))
    steps = payload.get("steps", [])
    if not steps:
        return parts
    x0, x1 = panel.x + 16, panel.x + panel.width - 16
    step_w = (x1 - x0) / len(steps)
    ch = 40.0
    # center the flow vertically when the panel is stretched by a row sibling
    avail = panel.y + panel.height - 16 - content_y
    cy = content_y + max(26.0, (avail - ch - (16 if payload.get("loop") else 0)) / 2)
    palette = payload.get("colors", [])
    for i, step in enumerate(steps):
        sx = x0 + i * step_w
        step_color = (palette[i % len(palette)] if palette
                      else payload.get("color", color))
        notch = min(14.0, step_w * 0.18)
        if isinstance(step, str):
            step = {"label": step}
        d = (f'M {fmt(sx)} {fmt(cy)} L {fmt(sx + step_w - notch)} {fmt(cy)} '
             f'L {fmt(sx + step_w)} {fmt(cy + ch / 2)} '
             f'L {fmt(sx + step_w - notch)} {fmt(cy + ch)} '
             f'L {fmt(sx)} {fmt(cy + ch)} ')
        if i:
            d += (f'L {fmt(sx + notch)} {fmt(cy + ch / 2)} ')
        d += 'Z'
        parts.append(f'<path d="{d}" fill="{step_color}" '
                     f'fill-opacity="{0.35 + 0.65 * (i + 1) / len(steps):.2f}"/>')
        cx = sx + step_w / 2 + (notch / 2 if i else 0)
        label_fill = payload.get("label_color", "#ffffff")
        parts.append(text(cx, cy + ch / 2 - 1,
                          fit(step.get("label", ""), step_w / 12), 12,
                          label_fill, bold=True, anchor="middle"))
        en = step.get("label_en", "")
        if en:
            parts.append(text(cx, cy + ch / 2 + 14, fit(en, step_w / 6.5),
                              9.5, label_fill, anchor="middle"))
    if payload.get("loop"):
        parts.append(f'<path d="M {fmt(x1 - 10)} {fmt(cy + ch + 10)} '
                     f'L {fmt(x0 + 20)} {fmt(cy + ch + 10)}" '
                     f'stroke="{color}" stroke-width="1.8" '
                     f'marker-end="url(#arrowhead)"/>')
    # S8 declutter: the floating "earth" globe illustration + caption was
    # removed engine-wide; the JSON keys are ignored.
    return parts


# -- section kind: timeline ----------------------------------------------------------


def _draw_timeline(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Horizontal milestone timeline: year chip + title + 2-line card."""
    colors = theme["colors"]
    canvas = theme["canvas"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    parts, content_y = _panel_chrome(panel, theme, payload.get("title", ""),
                                     payload.get("subtitle", ""))
    milestones = payload.get("milestones", [])
    if not milestones:
        return parts
    rocket_w = 90.0 if payload.get("rocket") else 0.0
    x0, x1 = panel.x + 24, panel.x + panel.width - 24 - rocket_w
    y_line = content_y + 90
    parts.append(f'<line x1="{fmt(x0)}" y1="{fmt(y_line)}" x2="{fmt(x1)}" '
                 f'y2="{fmt(y_line)}" stroke="{color}" stroke-width="2.5"/>')
    step = (x1 - x0) / len(milestones)
    card_w = step - 12
    for i, milestone in enumerate(milestones):
        mx = x0 + i * step + step / 2
        m_color = milestone.get("color", color)
        parts.append(f'<circle cx="{fmt(mx)}" cy="{fmt(y_line)}" r="7" '
                     f'fill="{m_color}"/>')
        # card above the line
        card_x = mx - card_w / 2
        card_top = content_y + 2
        parts.append(f'<rect x="{fmt(card_x)}" y="{fmt(card_top)}" '
                     f'width="{fmt(card_w)}" height="78" rx="8" '
                     f'fill="{canvas["card_fill"]}" '
                     f'stroke="{canvas["card_stroke"]}" stroke-width="1"/>')
        year = str(milestone.get("year", ""))
        parts += _chip(card_x + 6, card_top + 5,
                       text_width(year, 10.5) + 14, 18, year,
                       fill=m_color, size=10.5)
        # Long titles wrap to a second line (tighter pitch, desc drops to
        # one line) instead of being silently cut at the first line.
        title_lines = wrap(milestone.get("title", ""), (card_w - 14) / 12)
        desc_lines: list[str] = []
        for field in ("desc", "desc2"):
            if milestone.get(field):
                desc_lines += wrap(milestone[field], (card_w - 14) / 10.5)
        if len(title_lines) <= 1:
            parts.append(text(card_x + 7, card_top + 40, title_lines[0], 12,
                              colors["title"], bold=True))
            for j, line in enumerate(desc_lines[:2]):
                parts.append(text(card_x + 7, card_top + 56 + j * 14, line,
                                  10.5, colors["muted"]))
        else:
            title_lines = wrap_fit(milestone.get("title", ""),
                                   (card_w - 14) / 12, 2)
            parts.append(text(card_x + 7, card_top + 33, title_lines[0], 12,
                              colors["title"], bold=True))
            parts.append(text(card_x + 7, card_top + 47, title_lines[1], 12,
                              colors["title"], bold=True))
            if desc_lines:
                parts.append(text(card_x + 7, card_top + 66,
                                  wrap_fit(" ".join(desc_lines),
                                           (card_w - 14) / 10.5, 1)[0],
                                  10.5, colors["muted"]))
    if payload.get("rocket"):
        rx = x1 + rocket_w / 2 + 6
        parts += _icon("rocket", rx, y_line - 20, 26, color)
    return parts


# -- section kinds: fusion / family / hero / papers / industry --------------------


def _draw_fusion(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Fusion band: modality chips -> glowing core -> capability chips."""
    colors = theme["colors"]
    canvas = theme["canvas"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    dark_fill = canvas.get("band_dark_fill", "#0a1330")
    parts = [_frame(panel, theme, fill=dark_fill)]
    parts.append(text(panel.x + 18, panel.y + 32, payload.get("title", ""),
                      19, _DARK_TEXT, bold=True))
    cy = panel.y + panel.height / 2 + 2

    modalities = payload.get("modalities", [])
    core_cx = panel.x + panel.width * 0.46
    chip_w = 116.0
    left_zone = (panel.x + 24, panel.y + 58, core_cx - panel.x - 154,
                 panel.height - 128)
    right_zone = (core_cx + 92, panel.y + 58,
                  panel.x + panel.width - core_cx - 122, panel.height - 128)
    for zx, zy, zw, zh, label in (
        (*left_zone, "Input modalities"),
        (core_cx - 86, panel.y + 58, 172, panel.height - 128, "Shared space"),
        (*right_zone, "Capabilities"),
    ):
        parts.append(f'<rect x="{fmt(zx)}" y="{fmt(zy)}" width="{fmt(zw)}" '
                     f'height="{fmt(max(zh, 90))}" rx="16" fill="#ffffff" '
                     f'fill-opacity="0.035" stroke="#6d86ff" '
                     f'stroke-opacity="0.22" stroke-width="1"/>')
        parts.append(text(zx + 14, zy + 24, label, 11, _DARK_MUTED,
                          bold=True))
    # 3a: distribute the modality grid across the whole left zone instead of
    # hugging the panel edge, so the band has no dead void on the left.
    rows = math.ceil(len(modalities) / 2) or 1
    grid_w = 2 * chip_w + 14
    zone_l, zone_r = left_zone[0] + 16, left_zone[0] + left_zone[2] - 16
    mx = zone_l + max((zone_r - zone_l - grid_w) / 2, 0)
    row_gap = min(64.0, max(52.0, (left_zone[3] - 44) / max(rows, 1)))
    grid_h = rows * 40 + (rows - 1) * (row_gap - 40)
    for i, modality in enumerate(modalities):
        if isinstance(modality, str):
            modality = {"label": modality}
        col = i % 2
        row = i // 2
        cx = mx + col * (chip_w + 14)
        chy = cy - grid_h / 2 + row * row_gap
        parts += _chip(cx, chy, chip_w, 40, modality.get("label", ""),
                       fill=canvas["card_fill"],
                       stroke=canvas["card_stroke"],
                       text_fill=colors["text"], size=12)
        parts.append(f'<line x1="{fmt(cx + chip_w)}" y1="{fmt(chy + 20)}" '
                     f'x2="{fmt(core_cx - 72)}" y2="{fmt(cy)}" '
                     f'stroke="{color}" stroke-width="1.2" '
                     f'stroke-opacity="0.6"/>')
    core = payload.get("core", "")
    parts.append(f'<circle cx="{fmt(core_cx)}" cy="{fmt(cy)}" r="72" '
                 f'fill="{color}" fill-opacity="0.22"/>')
    parts.append(f'<circle cx="{fmt(core_cx)}" cy="{fmt(cy)}" r="96" '
                 f'fill="none" stroke="{color}" stroke-opacity="0.18" '
                 f'stroke-width="10"/>')
    parts.append(f'<circle cx="{fmt(core_cx)}" cy="{fmt(cy)}" r="52" '
                 f'fill="{color}" fill-opacity="0.35" '
                 f'stroke="{color}" stroke-width="2"/>')
    core_lines = wrap(core, 7)[:3]
    for i, line in enumerate(core_lines):
        ly = cy + 5 + (i - (len(core_lines) - 1) / 2) * 18
        parts.append(text(core_cx, ly, line, 13, "#ffffff",
                          bold=True, anchor="middle"))
    capabilities = payload.get("capabilities", [])
    cap_x = right_zone[0] + 20
    cap_end = right_zone[0] + right_zone[2] - 20
    cap_w = (cap_end - cap_x - 10 * len(capabilities)) / max(len(capabilities), 1)
    # Draw all connectors first: the chip fills then cover the line segments
    # passing underneath, so no stripe crosses a preceding chip's label.
    for i, capability in enumerate(capabilities):
        cx = cap_x + 10 + i * (cap_w + 10)
        parts.append(f'<line x1="{fmt(core_cx + 72)}" y1="{fmt(cy)}" '
                     f'x2="{fmt(cx)}" y2="{fmt(cy)}" '
                     f'stroke="{color}" stroke-width="1.2" '
                     f'stroke-opacity="0.6"/>')
    for i, capability in enumerate(capabilities):
        cx = cap_x + 10 + i * (cap_w + 10)
        parts += _chip(cx, cy - 22, cap_w, 44, capability, fill=color,
                       size=14)
    mechanisms = payload.get("mechanisms", [
        "Tokenization", "Attention Routing", "Shared Embedding",
        "Transfer Learning", "Scaling"
    ])
    mech_y = panel.y + panel.height - 54
    mech_w = (panel.width - 68 - 12 * (len(mechanisms) - 1)) / len(mechanisms)
    for i, mechanism in enumerate(mechanisms):
        mx2 = panel.x + 34 + i * (mech_w + 12)
        parts.append(f'<rect x="{fmt(mx2)}" y="{fmt(mech_y)}" '
                     f'width="{fmt(mech_w)}" height="30" rx="15" '
                     f'fill="{color}" fill-opacity="0.12" stroke="{color}" '
                     f'stroke-opacity="0.55" stroke-width="1"/>')
        parts.append(text(mx2 + mech_w / 2, mech_y + 20,
                          fit(mechanism, (mech_w - 20) / 10.5), 10.5,
                          _DARK_TEXT, anchor="middle"))
    return parts


def _draw_family(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Architecture family panel: colored header + model rows + footer."""
    colors = theme["colors"]
    canvas = theme["canvas"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    x, y, w = panel.x, panel.y, panel.width
    header_h = 56.0
    r = canvas["panel_radius"]
    number = payload.get("number")
    tx = x + 18
    if number is not None:
        # Circled section numeral on the colored header band (Vol.07/08).
        tx = x + 60
    parts = [
        _frame(panel, theme),
        f'<path d="M {fmt(x)} {fmt(y + r)} Q {fmt(x)} {fmt(y)} {fmt(x + r)} {fmt(y)} '
        f'L {fmt(x + w - r)} {fmt(y)} Q {fmt(x + w)} {fmt(y)} {fmt(x + w)} {fmt(y + r)} '
        f'L {fmt(x + w)} {fmt(y + header_h)} L {fmt(x)} {fmt(y + header_h)} Z" '
        f'fill="{color}"/>',
    ]
    if number is not None:
        parts.append(f'<circle cx="{fmt(x + 34)}" cy="{fmt(y + 28)}" r="15" '
                     f'fill="none" stroke="#ffffff" stroke-width="2.2"/>')
        parts.append(text(x + 34, y + 34, str(number), 17, "#ffffff",
                          bold=True, anchor="middle"))
    parts.append(text(tx, y + 26, fit(payload.get("title", ""), (w - tx + x - 18) / 16),
                      16, "#ffffff", bold=True))
    parts.append(text(tx, y + 45, fit(payload.get("subtitle", ""), (w - tx + x - 18) / 6.5),
                      11, "#ffffff", opacity=0.85))
    content_y = y + header_h
    if payload.get("diagram"):
        dx, dy = x + 16, content_y + 10
        dw, dh = w - 32, 68.0
        parts.append(f'<rect x="{fmt(dx)}" y="{fmt(dy)}" width="{fmt(dw)}" '
                     f'height="{fmt(dh)}" rx="8" '
                     f'fill="{canvas["photo_fill"]}"/>')
        parts += _schematic(payload.get("diagram_kind", "encoder"),
                            dx + 6, dy + 6, dw - 12, dh - 12,
                            canvas["photo_ink"])
        content_y += 88
    compact = bool(payload.get("compact"))
    for model in payload.get("models", []):
        year = str(model.get("year", ""))
        my = content_y + 8
        year_chip_w = max(42.0, min(text_width(year, 10) + 14, 58.0)) if year else 0.0
        year_label = fit(year, (year_chip_w - 10) / 5.6) if year else ""
        label_x = x + 14 + year_chip_w + 10 if year else x + 38
        text_reserve = label_x - x + 30
        name = model.get("name", "")
        org = model.get("org", "")
        label = f"{name} ({org})" if org else name
        desc = model.get("desc", "")
        # Labels that fit the legacy one-line budget render exactly as
        # before; only labels that would have ellipsized wrap to two
        # lines (row height grows by 16 per extra line, kept in sync
        # with layout.bands._kind_height via family_label_lines).
        label_lines = family_label_lines(
            label, w, with_year=bool(year), year_slot=text_reserve)
        extra_h = 16 * (len(label_lines) - 1)
        if not desc:
            if year:
                parts += _chip(x + 14, my + 2, year_chip_w, 20, year_label,
                               fill=color, size=10)
                for j, line in enumerate(label_lines):
                    parts.append(text(label_x, my + 12 + j * 16, line, 12.5,
                                      colors["title"], bold=True))
            else:
                parts.append(f'<circle cx="{fmt(x + 24)}" cy="{fmt(my + 4)}" '
                             f'r="4" fill="{color}"/>')
                for j, line in enumerate(label_lines):
                    parts.append(text(x + 38, my + 8 + j * 16, line, 11.5,
                                      colors["text"]))
            content_y += (26 if compact else 30) + extra_h
            continue
        if year:
            parts += _chip(x + 14, my + 2, year_chip_w, 20, year_label,
                           fill=color, size=10)
        for j, line in enumerate(label_lines):
            parts.append(text(label_x, my + 12 + j * 16, line, 12.5,
                              colors["title"], bold=True))
        # Descriptions wrap to two lines in every row style (compact rows
        # used to cap at one, silently dropping the second line).
        lines = family_desc_lines(desc, w)
        desc_h = 14 * (len(lines) - 1)
        for j, line in enumerate(lines):
            parts.append(text(label_x, my + 29 + extra_h + j * 14, line, 10.5,
                              colors["muted"]))
        content_y += (36 if compact else 52) + extra_h + desc_h
    footer = payload.get("footer", [])
    if footer:
        fy = panel.y + panel.height - 12 - 20 * (len(footer) - 1)
        parts.append(f'<line x1="{fmt(x + 16)}" y1="{fmt(fy - 22)}" '
                     f'x2="{fmt(x + w - 16)}" y2="{fmt(fy - 22)}" '
                     f'stroke="{colors["line"]}" stroke-width="1"/>')
        for i, line_text in enumerate(footer):
            parts.append(text(x + 16, fy + i * 20,
                              fit(line_text, (w - 32) / 10.5), 10.5,
                              colors["muted"]))
    return parts


def _draw_hero(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Centerpiece hero panel: title + architecture schematic + caption."""
    colors = theme["colors"]
    canvas = theme["canvas"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    x, y, w = panel.x, panel.y, panel.width
    parts = [_frame(panel, theme)]
    title = payload.get("title", "")
    subtitle = payload.get("subtitle", "")
    parts.append(text(x + w / 2, y + 36, title, 22, color, bold=True,
                      anchor="middle"))
    if subtitle:
        parts.append(text(x + w / 2, y + 58, subtitle, 13, colors["muted"],
                          anchor="middle"))
    org = payload.get("org", "")
    if org:
        parts.append(text(x + 24, y + 88, org, 13, colors["text"], bold=True))
    dx, dy = x + 20, y + 96
    dw, dh = w - 40, 150.0
    parts.append(f'<rect x="{fmt(dx)}" y="{fmt(dy)}" width="{fmt(dw)}" '
                 f'height="{fmt(dh)}" rx="10" fill="{canvas["photo_fill"]}"/>')
    # encoder-decoder schematic with block stacks
    bw = dw * 0.3
    for k, bx in enumerate((dx + dw * 0.12, dx + dw * 0.58)):
        for i in range(4):
            parts.append(f'<rect x="{fmt(bx)}" y="{fmt(dy + 14 + i * 30)}" '
                         f'width="{fmt(bw)}" height="22" rx="5" '
                         f'fill="none" stroke="{canvas["photo_ink"]}" '
                         f'stroke-width="1.5"/>')
        label = "Encoder" if k == 0 else "Decoder"
        parts.append(text(bx + bw / 2, dy + dh - 6, label, 10,
                          canvas["photo_ink"], anchor="middle"))
    parts.append(f'<line x1="{fmt(dx + dw * 0.12 + bw)}" y1="{fmt(dy + dh / 2)}" '
                 f'x2="{fmt(dx + dw * 0.58)}" y2="{fmt(dy + dh / 2)}" '
                 f'stroke="{canvas["photo_ink"]}" stroke-width="1.5" '
                 f'marker-end="url(#arrowhead)"/>')
    caption = payload.get("caption", "")
    cap_y = dy + dh + 24
    for i, line in enumerate(wrap(caption, (w - 48) / 12)[:3]):
        parts.append(text(x + 24, cap_y + i * 17, line, 12, colors["text"]))
    return parts


def _draw_papers(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Key-papers list: portrait dot + year chip + authors + citation."""
    colors = theme["colors"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    parts, content_y = _panel_chrome(panel, theme, payload.get("title", ""),
                                     payload.get("subtitle", ""))
    canvas = theme["canvas"]
    y = content_y + 8
    for paper in payload.get("papers", []):
        parts.append(f'<circle cx="{fmt(panel.x + 34)}" cy="{fmt(y + 18)}" '
                     f'r="16" fill="{canvas["side_fill"]}" '
                     f'stroke="{color}" stroke-width="1.5"/>')
        parts += _icon("person", panel.x + 34, y + 20, 8, colors["muted"])
        parts += _chip(panel.x + 60, y + 4,
                       text_width(str(paper.get("year", "")), 11) + 16, 22,
                       str(paper.get("year", "")), fill=color, size=11)
        parts.append(text(panel.x + 60 + text_width(str(paper.get("year", "")), 11) + 26,
                          y + 19, fit(paper.get("authors", ""), 20), 11.5,
                          colors["text"], bold=True))
        max_units = (panel.width - 76) / 10.5
        citation = f"{paper.get('title', '')} ({paper.get('venue', '')})"
        for j, line in enumerate(wrap(citation, max_units)[:2]):
            parts.append(text(panel.x + 60, y + 38 + j * 15, line, 10.5,
                              colors["muted"]))
        y += 68
    return parts


def _draw_industry(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Grouped chip columns (e.g. industry impact: giants / OSS / apps)."""
    colors = theme["colors"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    parts, content_y = _panel_chrome(panel, theme, payload.get("title", ""),
                                     payload.get("subtitle", ""))
    groups = payload.get("groups", [])
    if not groups:
        return parts
    col_w = (panel.width - 32 - (len(groups) - 1) * 16) / len(groups)
    max_items = max((len(g.get("items", [])) for g in groups), default=1) or 1
    # S3 whitespace: grow chip height/spacing so the tallest group fills the
    # panel vertically, and center shorter groups instead of leaving them
    # top-anchored above a ragged void.
    area_y = content_y + 28
    area_h = panel.y + panel.height - 14 - area_y
    chip_h = min(44.0, max(24.0, (area_h - (max_items - 1) * 10) / max_items))
    pitch = chip_h + 10
    for g, group in enumerate(groups):
        gx = panel.x + 16 + g * (col_w + 16)
        g_color = group.get("color", color)
        parts.append(text(gx, content_y + 16, group.get("title", ""), 13,
                          g_color, bold=True))
        items = group.get("items", [])
        group_h = len(items) * pitch - 10
        iy = area_y + max(0.0, (area_h - group_h) / 2)
        for item in items:
            parts += _chip(gx, iy, col_w, chip_h, fit(item, col_w / 11),
                           fill=theme["canvas"]["card_fill"],
                           stroke=theme["canvas"]["card_stroke"],
                           text_fill=colors["text"], size=11, bold=False,
                           rx=min(12.0, chip_h / 2))
            iy += pitch
    return parts


# -- section kinds: pyramid / wheel / radial / figures / curve / arch ------------


def _draw_pyramid(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Capability hierarchy pyramid (bottom = base, top = advanced)."""
    colors = theme["colors"]
    payload = panel.payload
    parts, content_y = _panel_chrome(panel, theme, payload.get("title", ""),
                                     payload.get("subtitle", ""))
    levels = payload.get("levels", [])
    if not levels:
        return parts
    axis_w = 110.0
    cx = panel.x + (panel.width - axis_w) / 2
    top_y = content_y + 8
    n = len(levels)
    level_h = (panel.y + panel.height - 16 - top_y) / n
    max_w = panel.width - axis_w - 120
    palette = payload.get("colors",
                          ["#22c55e", "#65a30d", "#f59e0b", "#f97316", "#ef4444"])
    for i, level in enumerate(levels):
        # draw from top (last level) to bottom (first level)
        li = n - 1 - i
        frac0 = (n - 1 - li) / n
        frac1 = (n - li) / n
        w0 = max_w * (0.18 + 0.82 * frac0)
        w1 = max_w * (0.18 + 0.82 * frac1)
        ly = top_y + i * level_h
        color = palette[li % len(palette)]
        d = (f'M {fmt(cx - w0 / 2)} {fmt(ly)} L {fmt(cx + w0 / 2)} {fmt(ly)} '
             f'L {fmt(cx + w1 / 2)} {fmt(ly + level_h - 3)} '
             f'L {fmt(cx - w1 / 2)} {fmt(ly + level_h - 3)} Z')
        parts.append(f'<path d="{d}" fill="{color}" fill-opacity="0.85"/>')
        label = level.get("label", "")
        label_en = level.get("label_en", "")
        parts.append(text(cx, ly + level_h / 2 + 2,
                          f"{label} ({label_en})" if label_en else label,
                          13, "#ffffff", bold=True, anchor="middle"))
        desc = level.get("desc", "")
        if desc:
            parts.append(text(cx, ly + level_h / 2 + 18,
                              fit(desc, max_w / 11), 10, "#ffffff",
                              anchor="middle", opacity=0.9))
    axis = payload.get("axis", [])
    if len(axis) == 2:
        ax = panel.x + panel.width - 56
        parts.append(f'<line x1="{fmt(ax)}" y1="{fmt(top_y + 6)}" '
                     f'x2="{fmt(ax)}" y2="{fmt(top_y + n * level_h - 6)}" '
                     f'stroke="{colors["muted"]}" stroke-width="1.5" '
                     f'marker-end="url(#arrowhead)"/>')
        parts.append(text(ax, top_y - 2, axis[1], 11, colors["muted"],
                          anchor="middle", bold=True))
        parts.append(text(ax, top_y + n * level_h + 14, axis[0], 11,
                          colors["muted"], anchor="middle", bold=True))
    return parts


def _draw_wheel(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Donut wheel of concept segments around a center label + agent strip.

    S4: the wheel now scales to fill the available panel height so it
    looks intentional instead of floating in a void.
    """
    colors = theme["colors"]
    payload = panel.payload
    parts, content_y = _panel_chrome(panel, theme, payload.get("title", ""),
                                     payload.get("subtitle", ""))
    segments = payload.get("segments", [])
    strip = payload.get("strip")
    strip_h = 46.0 if strip else 0.0
    # Scale to available space; leave room for the agent strip at the bottom
    av_h = panel.y + panel.height - 24 - content_y - strip_h
    cx = panel.x + panel.width / 2
    cy = content_y + 8 + av_h / 2
    radius = min(av_h / 2 - 10, panel.width * 0.21)
    inner = radius * 0.50
    n = len(segments)
    for i, segment in enumerate(segments):
        a0 = -math.pi / 2 + i * 2 * math.pi / n
        a1 = a0 + 2 * math.pi / n - 0.06
        color = segment.get("color", colors["accent"])
        x0, y0 = cx + radius * math.cos(a0), cy + radius * math.sin(a0)
        x1, y1 = cx + radius * math.cos(a1), cy + radius * math.sin(a1)
        xi1, yi1 = cx + inner * math.cos(a1), cy + inner * math.sin(a1)
        xi0, yi0 = cx + inner * math.cos(a0), cy + inner * math.sin(a0)
        d = (f'M {fmt(x0)} {fmt(y0)} A {fmt(radius)} {fmt(radius)} 0 0 1 '
             f'{fmt(x1)} {fmt(y1)} L {fmt(xi1)} {fmt(yi1)} '
             f'A {fmt(inner)} {fmt(inner)} 0 0 0 {fmt(xi0)} {fmt(yi0)} Z')
        parts.append(f'<path d="{d}" fill="{color}" fill-opacity="0.9"/>')
        mid = (a0 + a1) / 2
        tx = cx + (radius + inner) / 2 * math.cos(mid)
        ty = cy + (radius + inner) / 2 * math.sin(mid)
        parts.append(text(tx, ty, segment.get("label", ""), 12, "#ffffff",
                          bold=True, anchor="middle"))
        en = segment.get("label_en", "")
        if en:
            parts.append(text(tx, ty + 14, en, 9, "#ffffff", anchor="middle"))
        desc = segment.get("desc", "")
        if desc:
            parts.append(text(tx, ty + 26, fit(desc, 7), 8.5, "#ffffff",
                              anchor="middle", opacity=0.9))
    center = payload.get("center", {})
    parts.append(f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(inner - 8)}" '
                 f'fill="{theme["canvas"]["panel_fill"]}" '
                 f'stroke="{colors["line"]}" stroke-width="1.5"/>')
    parts.append(text(cx, cy + 2, center.get("zh", ""), 16, colors["title"],
                      bold=True, anchor="middle"))
    parts.append(text(cx, cy + 20, center.get("en", ""), 11, colors["muted"],
                      anchor="middle"))
    if strip:
        sy = content_y + 8 + av_h + 8
        steps = strip.get("steps", [])
        parts.append(text(panel.x + 20, sy + 16, strip.get("title", ""), 13,
                          colors["title"], bold=True))
        sx = panel.x + 20 + text_width(strip.get("title", ""), 13) + 20
        step_w = (panel.x + panel.width - 20 - sx) / max(len(steps), 1)
        for i, step in enumerate(steps):
            parts += _chip(sx + i * step_w + 2, sy, step_w - 8, 26, step,
                           fill=theme["canvas"]["card_fill"],
                           stroke=colors["accent"],
                           text_fill=colors["text"], size=11, bold=False)
            if i < len(steps) - 1:
                parts += _arrow(sx + (i + 1) * step_w - 10, sy + 13, 11,
                                colors["muted"])
    return parts


def _draw_radial(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Radial discipline map: center hub + surrounding branch cards."""
    colors = theme["colors"]
    canvas = theme["canvas"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    parts, content_y = _panel_chrome(panel, theme, payload.get("title", ""),
                                     payload.get("subtitle", ""))
    branches = payload.get("branches", [])
    area_h = panel.y + panel.height - 12 - content_y
    cx = panel.x + panel.width / 2
    cy = content_y + area_h / 2
    n = len(branches)
    # S3 whitespace: scale the hub and branch cards with the available area
    # so a sparse radial fills its panel instead of floating in a void.
    bw = min(320.0, max(190.0, panel.width * 0.24))
    bh = min(140.0, max(96.0, area_h * 0.30))
    hub_r = min(92.0, max(56.0, area_h * 0.22))
    rx = panel.width / 2 - bw / 2 - 40
    ry = area_h / 2 - bh / 2 - 16
    hub = payload.get("center", {})
    parts.append(f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(hub_r)}" '
                 f'fill="{color}"/>')
    parts.append(text(cx, cy - 2, hub.get("zh", ""), 16, "#ffffff",
                      bold=True, anchor="middle"))
    parts.append(text(cx, cy + 18, hub.get("en", ""), 11, "#ffffff",
                      anchor="middle"))

    def branch_card(branch: dict[str, Any], bx0: float, by0: float) -> None:
        b_color = branch.get("color", color)
        parts.append(f'<line x1="{fmt(cx)}" y1="{fmt(cy)}" '
                     f'x2="{fmt(bx0 + bw / 2)}" y2="{fmt(by0 + bh / 2)}" '
                     f'stroke="{b_color}" stroke-width="1.2" '
                     f'stroke-opacity="0.6"/>')
        # Neutral border (S5): accent lives in label text, bullets, and the
        # connector line, not in a per-branch card outline.
        parts.append(f'<rect x="{fmt(bx0)}" y="{fmt(by0)}" width="{fmt(bw)}" '
                     f'height="{fmt(bh)}" rx="10" '
                     f'fill="{canvas["card_fill"]}" '
                     f'stroke="{canvas["card_stroke"]}" stroke-width="1.2"/>')
        label = fit(branch.get("label", ""), (bw - 20) / 11.5)
        parts.append(text(bx0 + 10, by0 + 18, label, 11.5, b_color,
                          bold=True))
        en = branch.get("label_en", "")
        if en:
            parts.append(text(bx0 + 10 + text_width(label, 11.5) + 6,
                              by0 + 17, fit(en, (bw - 30) / 9), 9,
                              colors["muted"]))
        for j, item in enumerate(branch.get("items", [])[:3]):
            parts.append(f'<circle cx="{fmt(bx0 + 13)}" '
                         f'cy="{fmt(by0 + 34 + j * 17)}" r="2.5" '
                         f'fill="{b_color}"/>')
            parts.append(text(bx0 + 20, by0 + 38 + j * 17,
                              fit(item, (bw - 30) / 9.5), 9.5, colors["text"]))

    if n >= 7:
        # Too many cards for the ellipse: left/right columns + top/bottom
        # cards flanking the hub (matches the reference discipline map).
        mid = 2 if n % 2 == 0 else 1
        side = (n - mid) // 2
        groups = [(branches[:side], panel.x + 12),
                  (branches[side + mid:], panel.x + panel.width - 12 - bw)]
        top_y = content_y + 4
        bot_y = panel.y + panel.height - 12 - bh
        for group, gx in groups:
            k = len(group)
            span = bot_y - top_y
            step = span / (k - 1) if k > 1 else 0.0
            for j, branch in enumerate(group):
                gy = top_y + j * step if k > 1 else (top_y + bot_y) / 2
                branch_card(branch, gx, gy)
        for j, branch in enumerate(branches[side:side + mid]):
            branch_card(branch, cx - bw / 2, top_y if j == 0 else bot_y)
        return parts
    for i, branch in enumerate(branches):
        angle = -math.pi / 2 + i * 2 * math.pi / n
        bx = cx + rx * math.cos(angle)
        by = cy + ry * math.sin(angle)
        bx0, by0 = bx - bw / 2, by - bh / 2
        bx0 = max(panel.x + 12, min(panel.x + panel.width - 12 - bw, bx0))
        by0 = max(content_y + 4, min(panel.y + panel.height - 12 - bh, by0))
        branch_card(branch, bx0, by0)
    return parts


def _draw_figures(panel: Panel, theme: dict[str, Any],
                  images: ImageEmbedder | None = None) -> list[str]:
    """Key-figures profile cards with dates and contribution bullets."""
    colors = theme["colors"]
    canvas = theme["canvas"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    parts, content_y = _panel_chrome(panel, theme, payload.get("title", ""),
                                     payload.get("subtitle", ""))
    figures = payload.get("figures", [])
    if not figures:
        return parts
    cols = max(int(payload.get("columns", 2 if panel.width > 300 else 1)), 1)
    gap = 10.0
    body_top = content_y + 8
    body_bottom = panel.y + panel.height - 12
    rows = math.ceil(len(figures) / cols)
    card_w = (panel.width - 32 - gap * (cols - 1)) / cols
    card_h = (body_bottom - body_top - gap * max(rows - 1, 0)) / rows
    card_h = max(104.0, card_h)
    for i, figure in enumerate(figures):
        col = i % cols
        row = i // cols
        fx = panel.x + 16 + col * (card_w + gap)
        fy = body_top + row * (card_h + gap)
        parts.append(f'<rect x="{fmt(fx)}" y="{fmt(fy)}" '
                     f'width="{fmt(card_w)}" height="{fmt(card_h)}" rx="10" '
                     f'fill="{canvas["card_fill"]}" '
                     f'stroke="{canvas["card_stroke"]}" stroke-width="1.1"/>')
        parts.append(f'<rect x="{fmt(fx)}" y="{fmt(fy)}" width="4" '
                     f'height="{fmt(card_h)}" rx="2" fill="{color}" '
                     f'fill-opacity="0.85"/>')
        acx, acy = fx + 34, fy + 34
        avatar = min(48.0, max(38.0, card_h * 0.34))
        drawn = (images.svg_image(figure["image"], acx - avatar / 2,
                                  acy - avatar / 2, avatar, avatar,
                                  focus=figure.get("image_focus", "center"),
                                  radius=avatar / 2)
                 if images is not None and figure.get("image") else None)
        if drawn is not None:
            parts += drawn
        else:
            parts.append(f'<circle cx="{fmt(acx)}" cy="{fmt(acy)}" '
                         f'r="{fmt(avatar / 2)}" '
                         f'fill="{canvas["photo_fill"]}"/>')
            parts += _icon("person", acx, acy + 2, avatar * 0.28,
                           canvas["photo_ink"])
        tx = fx + 66
        name = fit(figure.get("name", ""), (card_w - 78) / 9.2)
        parts.append(text(tx, fy + 24, name, 13.2,
                          colors["title"], bold=True))
        years = figure.get("years", "") or figure.get("life", "")
        if years:
            chip_w = min(card_w - 78, max(66.0, text_width(years, 9.5) + 18))
            parts += _chip(tx, fy + 32, chip_w, 19, years,
                           fill=canvas["side_fill"], stroke=color,
                           text_fill=color, size=9.5, bold=True)
        role_y = fy + (64 if years else 42)
        role = figure.get("role", "")
        if role:
            parts.append(text(tx, role_y, fit(role, (card_w - 78) / 9.8),
                              10.2, colors["text"], bold=True))
            role_y += 15
        available_lines = max(2, min(3, int((fy + card_h - 10 - role_y) / 13)))
        lines: list[str] = []
        for line in figure.get("lines", []):
            lines.extend(wrap(line, (card_w - 82) / 8.8))
        for j, line in enumerate(lines[:available_lines]):
            parts.append(f'<circle cx="{fmt(tx + 2)}" '
                         f'cy="{fmt(role_y + 4 + j * 13)}" r="2" '
                         f'fill="{color}" fill-opacity="0.8"/>')
            parts.append(text(tx + 8, role_y + 8 + j * 13,
                              fit(line, (card_w - 94) / 8.8), 8.8,
                              colors["muted"]))
    return parts


_SUP_CHARS = "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻"
_SUP_ASCII = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5",
              "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁺": "+", "⁻": "-"}


def _text_super(x: float, y: float, s: str, size: float, fill: str, *,
                anchor: str = "middle") -> str:
    """Render text with unicode superscripts as true raised small digits.

    The poster font lacks superscript glyphs (``helpers._font_safe`` falls
    back to caret notation for ordinary text), so chart tick labels emit
    ``<tspan dy>`` superscripts instead — font-independent and clean.
    """
    runs: list[tuple[str, bool]] = []
    cur, cur_sup = "", False
    for ch in s:
        is_sup = ch in _SUP_CHARS
        if cur and is_sup != cur_sup:
            runs.append((cur, cur_sup))
            cur = ""
        cur += ch
        cur_sup = is_sup
    if cur:
        runs.append((cur, cur_sup))
    sup_size = size * 0.72
    lift = size * 0.38
    total_w = sum(text_width(run, sup_size if is_sup else size)
                  for run, is_sup in runs)
    cursor = {"start": x, "middle": x - total_w / 2, "end": x - total_w}[anchor]
    tspans: list[str] = []
    for run, is_sup in runs:
        content = "".join(_SUP_ASCII.get(c, c) for c in run) if is_sup else run
        if is_sup:
            tspans.append(f'<tspan dy="-{fmt(lift)}" '
                          f'font-size="{fmt(sup_size)}">{escape(content)}</tspan>')
        else:
            back = f' dy="{fmt(lift)}"' if tspans else ""
            tspans.append(f'<tspan{back}>{escape(content)}</tspan>')
    return (f'<text x="{fmt(cursor)}" y="{fmt(y)}" font-size="{fmt(size)}" '
            f'fill="{fill}">{"".join(tspans)}</text>')


def _draw_curve(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """S-curve chart with log x ticks and stage callouts."""
    colors = theme["colors"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    parts, content_y = _panel_chrome(panel, theme, payload.get("title", ""),
                                     payload.get("subtitle", ""))
    x0 = panel.x + 60
    x1 = panel.x + panel.width - 30
    y0 = panel.y + panel.height - 44
    y1 = content_y + 30
    parts.append(f'<line x1="{fmt(x0)}" y1="{fmt(y0)}" x2="{fmt(x1)}" '
                 f'y2="{fmt(y0)}" stroke="{colors["muted"]}" stroke-width="1.5"/>')
    parts.append(f'<line x1="{fmt(x0)}" y1="{fmt(y0)}" x2="{fmt(x0)}" '
                 f'y2="{fmt(y1)}" stroke="{colors["muted"]}" stroke-width="1.5"/>')
    # S-curve as a cubic-ish path
    mid_x = x0 + (x1 - x0) * 0.55
    d = (f'M {fmt(x0)} {fmt(y0 - 10)} '
         f'C {fmt(x0 + (x1 - x0) * 0.3)} {fmt(y0 - 10)} '
         f'{fmt(mid_x - 40)} {fmt(y0 - (y0 - y1) * 0.45)} '
         f'{fmt(mid_x)} {fmt(y0 - (y0 - y1) * 0.6)} '
         f'S {fmt(x1 - 60)} {fmt(y1 + 20)} {fmt(x1 - 10)} {fmt(y1 + 8)}')
    parts.append(f'<path d="{d}" fill="none" stroke="{color}" '
                 f'stroke-width="2.5"/>')
    ticks = payload.get("ticks", [])
    for i, tick in enumerate(ticks):
        tx = x0 + (x1 - x0) * (i + 0.5) / len(ticks)
        parts.append(_text_super(tx, y0 + 18, tick, 9.5, colors["muted"]))
    if payload.get("x_label"):
        parts.append(text((x0 + x1) / 2, y0 + 36, payload["x_label"], 11,
                          colors["muted"], anchor="middle"))
    if payload.get("y_label"):
        parts.append(text(x0 - 10, y1 - 8, payload["y_label"], 11,
                          colors["muted"], anchor="middle"))
    stages = payload.get("stages", [])
    n = len(stages)
    if not n:
        return parts
    # S7 label placement: labels wrap wide enough to avoid mid-word breaks,
    # sit below their dot whenever the x-axis clearance allows (the dots
    # ride under the curve there, so below is always collision-free), and
    # otherwise float well above the dot with extra curve clearance; the
    # anchor point is clamped inside the plot area.
    label_units = min(14.0, max(9.0, (x1 - x0) / n / 10 * 0.9))
    for i, stage in enumerate(stages):
        frac = (i + 0.6) / n
        sx = x0 + (x1 - x0) * frac * 0.92
        sy = y0 - (y0 - y1) * min(0.08 + 0.92 * frac ** 2.2, 0.96)
        parts.append(f'<circle cx="{fmt(sx)}" cy="{fmt(sy)}" r="5" '
                     f'fill="{color}"/>')
        label_lines = wrap(stage, label_units)[:2]
        half = max(text_width(line, 10) for line in label_lines) / 2
        lx = min(max(sx, x0 + half), x1 - half)
        below_bottom = sy + 18 + 13 * (len(label_lines) - 1) + 10
        if below_bottom <= y0 - 4:
            ly = sy + 20  # below the dot, above the axis
        else:
            ly = sy - 22 - 13 * (len(label_lines) - 1)  # above, curve-safe
        for j, line in enumerate(label_lines):
            parts.append(text(lx, ly + j * 13, line, 10, colors["title"],
                              bold=True, anchor="middle"))
    return parts


def _draw_arch(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Decoder-only architecture diagram + token table + align flow + chips."""
    colors = theme["colors"]
    canvas = theme["canvas"]
    payload = panel.payload
    color = panel.color or colors["accent"]
    parts, content_y = _panel_chrome(panel, theme, payload.get("title", ""),
                                     payload.get("subtitle", ""))
    x = panel.x + 16
    w = panel.width - 32
    y = content_y + 6

    def flow_box(bx: float, by: float, bw: float, label: str,
                 fill: str, tfill: str, size: float = 11.5) -> None:
        parts.append(f'<rect x="{fmt(bx)}" y="{fmt(by)}" width="{fmt(bw)}" '
                     f'height="26" rx="7" fill="{fill}"/>')
        parts.append(text(bx + bw / 2, by + 17, fit(label, bw / 6.5), size,
                          tfill, bold=True, anchor="middle"))

    # vertical decoder stack (top = output, bottom = input)
    stack_w = w * 0.62
    sx = x + (w - stack_w) / 2 - 40
    top_blocks = [payload.get("output_label", ""), *payload.get("output_layers", [])]
    layers = payload.get("layers", [])
    blocks = [b for b in top_blocks if b] + ["__REPEAT__"] + \
             [payload.get("embedding", ""), payload.get("input_label", "")]
    blocks = [b for b in blocks if b]
    for block in blocks:
        if block == "__REPEAT__":
            repeat_h = len(layers) * 32 + 8
            parts.append(f'<rect x="{fmt(sx - 14)}" y="{fmt(y - 4)}" '
                         f'width="{fmt(stack_w + 28)}" height="{fmt(repeat_h)}" '
                         f'rx="10" fill="none" stroke="{color}" '
                         f'stroke-width="1.5" stroke-dasharray="6 4"/>')
            repeat = payload.get("repeat", "× N Layers")
            parts.append(text(sx + stack_w + 22, y + repeat_h / 2, repeat,
                              10.5, color, bold=True))
            for layer in layers:
                y += 4
                fill = (canvas["side_fill"] if "⊕" not in layer
                        else canvas["card_fill"])
                flow_box(sx, y, stack_w, layer, fill, colors["text"], 11)
                y += 28
            y += 8
            continue
        is_io = block in (payload.get("output_label"),
                          payload.get("input_label"))
        flow_box(sx, y, stack_w, block,
                 color if is_io else canvas["side_fill"],
                 "#ffffff" if is_io else colors["text"])
        y += 32
    y += 6

    token_table = payload.get("token_table")
    if token_table:
        parts.append(text(x, y + 14, token_table.get("title", ""), 13,
                          colors["title"], bold=True))
        y += 24
        rows = token_table.get("rows", [])
        cells = max(len(r.get("cells", [])) for r in rows)
        cell_w = (w - 70) / cells
        for r, row in enumerate(rows):
            parts.append(text(x + 4, y + 17, row.get("label", ""), 10.5,
                              colors["muted"]))
            for c, cell in enumerate(row.get("cells", [])):
                cell_color = row.get("color", colors["accent"])
                highlight = row.get("highlight", []) and c in row["highlight"]
                parts += _chip(x + 64 + c * cell_w + 1, y, cell_w - 4, 22,
                               fit(cell, cell_w / 7),
                               fill=(_YELLOW if highlight else
                                     canvas["card_fill"]),
                               stroke=cell_color,
                               text_fill=("#1a2332" if highlight
                                          else colors["text"]),
                               size=10, bold=highlight)
            y += 28
        y += 8

    align = payload.get("align_flow", [])
    if align:
        parts.append(text(x, y + 14, payload.get("align_title", ""), 13,
                          colors["title"], bold=True))
        y += 24
        box_w = (w - 2 * 30) / len(align)
        for i, step in enumerate(align):
            flow_box(x + i * (box_w + 30), y, box_w, step,
                     canvas["card_fill"], colors["text"], 11)
            if i < len(align) - 1:
                ax = x + (i + 1) * (box_w + 30) - 26
                parts += _arrow(ax, y + 14, 13, colors["muted"])
        y += 36

    abilities = payload.get("abilities", [])
    if abilities:
        parts.append(text(x, y + 14, payload.get("abilities_title", ""), 13,
                          colors["title"], bold=True))
        y += 24
        chip_w = (w - 5 * 8) / len(abilities)
        for i, ability in enumerate(abilities):
            parts += _chip(x + i * (chip_w + 8), y, chip_w, 40,
                           fit(ability, chip_w / 10.5),
                           fill=canvas["card_fill"], stroke=color,
                           text_fill=colors["text"], size=10.5, bold=False)
    return parts


# -- section dispatch -------------------------------------------------------------


def _draw_section(panel: Panel, theme: dict[str, Any],
                  images: ImageEmbedder | None = None) -> list[str]:
    """Dispatch one section panel to its kind renderer."""
    kind = panel.payload.get("kind", "band")
    renderers = {
        "band": _draw_band,
        "list": _draw_list,
        "cards": _draw_cards_panel,
        "table": _draw_table,
        "pills": _draw_pills,
        "chevrons": _draw_chevrons,
        "timeline": _draw_timeline,
        "fusion": _draw_fusion,
        "family": _draw_family,
        "hero": _draw_hero,
        "papers": _draw_papers,
        "industry": _draw_industry,
        "pyramid": _draw_pyramid,
        "wheel": _draw_wheel,
        "radial": _draw_radial,
        "figures": _draw_figures,
        "curve": _draw_curve,
        "arch": _draw_arch,
    }
    renderer = renderers.get(kind)
    if renderer is None:
        logger.warning("Unknown section kind %r; skipped", kind)
        return []
    if kind == "band":
        return _draw_band(panel, theme, images)
    if kind == "cards":
        return _draw_cards_panel(panel, theme, images)
    if kind == "figures":
        return _draw_figures(panel, theme, images)
    return renderer(panel, theme)


# -- mainline band + insights + next + footer -------------------------------------


def _draw_mainline(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Main-line timeline band: glowing stage nodes, axis ticks, driver chips."""
    canvas = theme["canvas"]
    payload = panel.payload
    x, y, w = panel.x, panel.y, panel.width
    dark_fill = canvas.get("band_dark_fill", "#0a1330")

    parts = [_frame(panel, theme, fill=dark_fill)]
    tx = x + 18
    number = payload.get("number")
    if number is not None:
        # Circled numeral badge, matching the light-section numbering.
        ncx, ncy = x + 34, y + 26
        parts.append(f'<circle cx="{fmt(ncx)}" cy="{fmt(ncy)}" r="15" '
                     f'fill="none" stroke="{_YELLOW}" stroke-width="2.2"/>')
        parts.append(text(ncx, ncy + 6, str(number), 17, _YELLOW,
                          bold=True, anchor="middle"))
        tx = x + 58
    parts.append(text(tx, y + 30, payload.get("title", ""), 19,
                      _DARK_TEXT, bold=True))

    stages = payload.get("stages", [])
    if stages:
        x0, x1 = x + w * 0.09, x + w - w * 0.04
        step = (x1 - x0) / (len(stages) - 1) if len(stages) > 1 else 0
        cy = y + 84
        for i, stage in enumerate(stages):
            cx = x0 + i * step
            color = stage.get("color", "#4f7cff")
            if i:
                parts.append(f'<line x1="{fmt(cx - step + 18)}" y1="{fmt(cy)}" '
                             f'x2="{fmt(cx - 22)}" y2="{fmt(cy)}" '
                             f'stroke="{_DARK_MUTED}" stroke-width="2" '
                             f'marker-end="url(#arrowhead)"/>')
            parts.append(f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="24" '
                         f'fill="{color}" fill-opacity="0.25"/>')
            parts.append(f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="13" '
                         f'fill="{color}"/>')
            parts.append(text(cx, cy + 42, stage.get("label", ""), 13,
                              _DARK_TEXT, bold=True, anchor="middle"))
            parts.append(text(cx, cy + 58, stage.get("sub", ""), 11,
                              _DARK_MUTED, anchor="middle"))

    axis = payload.get("axis", [])
    if axis:
        ax0, ax1 = x + 20, x + w - 20
        step = (ax1 - ax0) / len(axis)
        for i, tick in enumerate(axis):
            tx = ax0 + i * step + step / 2
            parts.append(f'<rect x="{fmt(tx - step / 2 + 3)}" y="{fmt(y + 148)}" '
                         f'width="{fmt(step - 6)}" height="20" rx="10" '
                         f'fill="{canvas["card_fill"]}" '
                         f'stroke="{canvas["card_stroke"]}" stroke-width="1"/>')
            parts.append(text(tx, y + 162, tick, 11, _DARK_MUTED,
                              anchor="middle"))

    drivers = payload.get("drivers", [])
    if drivers:
        # Without stages/axis the driver row is the only content: center it
        # under the title instead of bottom-anchoring it.
        dy = y + 172 if (stages or axis) else y + 108
        dx0, dx1 = x + 20, x + w - 20
        step = (dx1 - dx0) / len(drivers)
        for i, driver in enumerate(drivers):
            dcx = dx0 + i * step
            color = driver.get("color", "#22c55e")
            parts.append(f'<rect x="{fmt(dcx + 3)}" y="{fmt(dy)}" '
                         f'width="{fmt(step - 6)}" height="28" rx="8" '
                         f'fill="{color}" fill-opacity="0.18" '
                         f'stroke="{color}" stroke-width="1"/>')
            parts.append(text(dcx + step / 2, dy + 12,
                              fit(driver.get("label", ""), (step - 14) / 10.5),
                              10.5, _DARK_TEXT, bold=True, anchor="middle"))
            parts.append(text(dcx + step / 2, dy + 24,
                              fit(driver.get("sub", ""), (step - 14) / 9),
                              9, _DARK_MUTED, anchor="middle"))
    return parts


def _draw_insights(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Insights row: labeled chips + large closing quote."""
    colors = theme["colors"]
    canvas = theme["canvas"]
    payload = panel.payload
    x, y, w = panel.x, panel.y, panel.width

    dark_insights = bool(canvas.get("insights_dark", False))
    if dark_insights:
        parts = [_frame(panel, theme, fill=canvas.get("band_dark_fill", "#0a1330"))]
        title_fill = _DARK_TEXT
        chip_text = _DARK_TEXT
        chip_fill = "#17213b"
        chip_stroke = "#33446d"
    else:
        parts = [_frame(panel, theme)]
        title_fill = colors["title"]
        chip_text = colors["text"]
        chip_fill = canvas["card_fill"]
        chip_stroke = colors["line"]
    items = payload.get("items", [])
    if items:
        parts.append(text(x + 18, y + 34, "历史启示", 17, title_fill, bold=True))
        chip_x = x + 110
        chip_h = 30.0
        for item in items:
            chip_w = text_width(item, 13) + 26
            parts.append(f'<rect x="{fmt(chip_x)}" y="{fmt(y + 14)}" '
                         f'width="{fmt(chip_w)}" height="{fmt(chip_h)}" '
                         f'rx="15" fill="{chip_fill}" '
                         f'stroke="{chip_stroke}" stroke-width="1"/>')
            parts.append(text(chip_x + chip_w / 2, y + 34, item, 13,
                              chip_text, anchor="middle"))
            chip_x += chip_w + 14
    quote = payload.get("quote", "")
    if quote:
        parts.append(text(x + w / 2, y + panel.height - 28, quote, 30,
                          colors["title"], bold=True, anchor="middle"))
    return parts


def _draw_next(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """NEXT-volume teaser: yellow label, volume title, glowing cube.

    Sits at the right of the footer band (same height, 100) on every
    volume except the last; renders compactly in that footprint.
    """
    canvas = theme["canvas"]
    payload = panel.payload
    x, y, w, h = panel.x, panel.y, panel.width, panel.height
    dark_fill = canvas.get("band_dark_fill", "#0a1330")
    compact = h < 160

    parts = [_frame(panel, theme, fill=dark_fill, stroke="#3a55c9")]

    parts.append(text(x + 18, y + (30 if compact else 36),
                      payload.get("label", "NEXT"), 15 if compact else 20,
                      _YELLOW, bold=True, spacing=3))

    # Glowing cube illustration (isometric placeholder, top-right corner).
    cx, cy = x + w - 46, y + (46 if compact else 52)
    s = 19.0 if compact else 22.0
    top = f'{fmt(cx)},{fmt(cy - s)} {fmt(cx + s)},{fmt(cy - s / 2)} {fmt(cx)},{fmt(cy)} {fmt(cx - s)},{fmt(cy - s / 2)}'
    left = f'{fmt(cx - s)},{fmt(cy - s / 2)} {fmt(cx)},{fmt(cy)} {fmt(cx)},{fmt(cy + s)} {fmt(cx - s)},{fmt(cy + s / 2)}'
    right = f'{fmt(cx + s)},{fmt(cy - s / 2)} {fmt(cx)},{fmt(cy)} {fmt(cx)},{fmt(cy + s)} {fmt(cx + s)},{fmt(cy + s / 2)}'
    parts.append(f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="30" '
                 f'fill="#3a55c9" fill-opacity="0.25"/>')
    parts.append(f'<polygon points="{top}" fill="#5f7dff" fill-opacity="0.9"/>')
    parts.append(f'<polygon points="{left}" fill="#2f49b8" fill-opacity="0.9"/>')
    parts.append(f'<polygon points="{right}" fill="#4460d8" fill-opacity="0.9"/>')

    title = payload.get("title", "")
    if compact:
        title_lines = wrap(title, (w - 100) / 15)[:2]
        for i, line in enumerate(title_lines):
            parts.append(text(x + 18, y + 56 + i * 21, line, 15, _DARK_TEXT,
                              bold=True))
        desc = payload.get("desc", "")
        if desc and len(title_lines) < 2:
            desc_y = y + 56 + len(title_lines) * 21
            for i, line in enumerate(wrap_fit(desc, (w - 36) / 11.5, 2)):
                parts.append(text(x + 18, desc_y + i * 15, line, 11.5,
                                  _DARK_MUTED))
    else:
        title_lines = wrap(title, (w - 36) / 19)[:2]
        for i, line in enumerate(title_lines):
            parts.append(text(x + 18, y + 96 + i * 26, line, 19, _YELLOW,
                              bold=True))
        desc = payload.get("desc", "")
        desc_y = y + 96 + len(title_lines) * 26 + 12
        for i, line in enumerate(wrap(desc, (w - 36) / 12)[:3]):
            parts.append(text(x + 18, desc_y + i * 18, line, 12, _DARK_MUTED))
    parts.append(text(x + w - 16, y + h - 14, ">>>", 18, _YELLOW, bold=True,
                      anchor="end"))
    return parts


def _draw_footer_band(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Unified dark navy footer band (S2): series line left, quote center.

    When ``legend_items`` is present in the payload (bottom-legend volumes),
    legend icon chips are drawn right-aligned in the band.
    """
    payload = panel.payload
    x, y, w, h = panel.x, panel.y, panel.width, panel.height
    canvas = theme["canvas"]
    dark_fill = canvas.get("band_dark_fill", "#0a1330")
    parts = [_frame(panel, theme, fill=dark_fill)]

    meta = payload.get("meta", {})
    parts.append(text(x + 22, y + 38, "Modern AI Atlas", 16, _DARK_TEXT,
                      bold=True))
    volume = meta.get("volume", "")
    title_en = meta.get("title_en", "")
    series_line = f"Modern AI Atlas · {volume}" if volume else "Modern AI Atlas"
    if title_en:
        series_line += f" | {title_en}"
    parts.append(text(x + 22, y + 62, series_line, 11, _DARK_MUTED))

    # bottom-legend: render icon chips right-aligned
    legend_items = payload.get("legend_items", [])
    if legend_items:
        lx = x + w - 22
        for item in reversed(legend_items):
            color = item.get("color", _DARK_MUTED)
            label = item.get("label", "")
            label_en = item.get("label_en", "")
            lw = max(72.0, text_width(label, 11.5) + 38)
            lx -= lw
            parts.append(f'<rect x="{fmt(lx)}" y="{fmt(y + 18)}" width="{fmt(lw)}" '
                         f'height="38" rx="19" fill="#ffffff" fill-opacity="0.09" '
                         f'stroke="#ffffff" stroke-opacity="0.14"/>')
            parts.append(f'<circle cx="{fmt(lx + 18)}" cy="{fmt(y + 37)}" r="9" '
                         f'fill="{color}" fill-opacity="0.18"/>')
            parts += _legend_icon(item.get("icon", ""), lx + 18, y + 37, color)
            parts.append(text(lx + 33, y + 33, label, 11.5, _DARK_TEXT,
                              bold=True))
            if label_en:
                parts.append(text(lx + 33, y + 48, label_en, 8,
                                  _DARK_MUTED))
            else:
                parts.append(text(lx + 33, y + 48, "Legend", 8,
                                  _DARK_MUTED))
            lx -= 8

    quote_zh = payload.get("quote_zh", "")
    quote_en = payload.get("quote_en", "")
    qcx = x + 260 + (w - 260) / 2
    if quote_zh:
        parts.append(text(qcx, y + h / 2 + (2 if quote_en else 6), quote_zh,
                          18, _DARK_TEXT, bold=True, anchor="middle"))
    if quote_en:
        en_units = (w - 300) / 10.5
        if text_width(quote_en, 10.5) <= en_units:
            parts.append(text(qcx, y + h / 2 + 26, quote_en, 10.5,
                              _DARK_MUTED, anchor="middle", italic=True))
        else:
            for j, line in enumerate(wrap_fit(quote_en, en_units, 2)):
                parts.append(text(qcx, y + h / 2 + 18 + j * 14, line, 10.5,
                                  _DARK_MUTED, anchor="middle", italic=True))
    return parts


def _draw_footer(panel: Panel, theme: dict[str, Any]) -> list[str]:
    """Footer: centered series line."""
    colors = theme["colors"]
    meta = panel.payload if "title_en" in panel.payload else {}
    series = (f"{meta.get('series', 'AI Technology Bible')} · "
              f"{meta.get('volume', '')}  |  {meta.get('title_en', '')}")
    return [
        text(panel.x + panel.width / 2, panel.y + 26,
             f"{series}  ·  Modern AI Atlas", 15, colors["muted"],
             anchor="middle"),
    ]
