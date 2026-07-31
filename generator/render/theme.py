"""Theme loading for the atlas renderer.

Themes are JSON files under ``assets/themes/`` (see ``generator/config.py``).
A built-in fallback keeps the renderer usable even without theme files.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from generator.config import THEME_DIR

logger = logging.getLogger(__name__)

# Minimal built-in fallback, mirrors assets/themes/default.json structurally.
_FALLBACK_THEME: dict[str, Any] = {
    "canvas": {
        "background": "#f7f5f0",
        "margin": 120,
        "header_height": 170,
        "node_width": 320,
        "node_height": 120,
        "node_gap_x": 60,
        "corner_radius": 14,
    },
    "colors": {
        "ink": "#1a2332",
        "ink_muted": "#5b6572",
        "card_fill": "#ffffff",
        "card_stroke": "#d8d4cc",
        "edge": "#9aa5b1",
        "lane_label": "#8a8578",
        "title": "#14202e",
    },
    "kinds": {
        "paper": {"color": "#2563eb", "label": "Paper"},
        "model": {"color": "#7c3aed", "label": "Model"},
        "concept": {"color": "#0891b2", "label": "Concept"},
        "event": {"color": "#d97706", "label": "Event"},
        "default": {"color": "#475569", "label": "Other"},
    },
    "typography": {
        "font_family": "Helvetica, Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif",
        "title_size": 64,
        "subtitle_size": 28,
        "node_title_size": 30,
        "node_meta_size": 22,
        "lane_label_size": 26,
        "edge_label_size": 20,
        "legend_size": 24,
    },
}


def load_theme(name: str, *, theme_dir: Path = THEME_DIR) -> dict[str, Any]:
    """Load a theme by name, falling back to the built-in default.

    Args:
        name: Theme name, e.g. ``default`` for ``<theme_dir>/default.json``.
        theme_dir: Directory containing theme JSON files.

    Returns:
        The theme dictionary.
    """
    path = theme_dir / f"{name}.json"
    if Path(name).name != name:
        logger.warning("Invalid theme name %r; using built-in fallback", name)
        return _FALLBACK_THEME
    if not path.is_file():
        logger.warning("Theme %r not found at %s; using built-in fallback", name, path)
        return _FALLBACK_THEME
    with path.open("r", encoding="utf-8") as fh:
        theme = json.load(fh)
    logger.info("Loaded theme %r from %s", name, path)
    return theme


def kind_style(theme: dict[str, Any], kind: str) -> dict[str, str]:
    """Return the color/label style for a node kind."""
    kinds = theme.get("kinds", {})
    return kinds.get(kind, kinds.get("default", {"color": "#475569", "label": kind}))
