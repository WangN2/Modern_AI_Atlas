"""Render package — draw the atlas onto an SVG canvas using the computed layout."""

from __future__ import annotations

from generator.render.svg import draw
from generator.render.theme import kind_style, load_theme

__all__ = ["draw", "kind_style", "load_theme"]
