"""Project-wide constants for the Modern AI Atlas Generator."""

from __future__ import annotations

PROJECT_NAME = "Modern AI Atlas Generator"
VERSION = "0.1.0"

# Output
TARGET_DPI = 300
DEFAULT_FORMAT = "A0"

# Atlas canvas fallback (used when neither meta nor theme specifies a size).
# Portrait volumes use a 2:3 poster (1024x1536 reference -> 1682x2524 canvas).
CANVAS_WIDTH = 1682
CANVAS_HEIGHT = 2524
# Landscape volumes use a 3:2 poster (1536x1024 reference -> 2524x1682 canvas).
CANVAS_WIDTH_LANDSCAPE = 2524
CANVAS_HEIGHT_LANDSCAPE = 1682

# Theme
DEFAULT_THEME = "empire_dark"

# Poster layout templates (selected via the knowledge file's meta.layout).
#   "panels" — Vol.02 panel-template grid (why/hero/papers/families/rails/...)
#   "bands"  — generic stacked band sections (numbered era bands, titled
#              bands, circled-numeral sections, landscape column grids)
LAYOUT_PANELS = "panels"
LAYOUT_BANDS = "bands"

# File extensions
EXT_SVG = ".svg"
EXT_PDF = ".pdf"
EXT_PNG = ".png"
EXT_YAML = ".yaml"
EXT_JSON = ".json"

# Knowledge file naming
KNOWLEDGE_GRAPH_FILE = "knowledge_graph"
