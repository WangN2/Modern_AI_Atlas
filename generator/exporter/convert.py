"""Exporter (Stage 5 of the build pipeline).

SVG output is written directly. PDF/PNG conversion uses the optional
``cairosvg`` backend (see ``requirements.txt``), which in turn needs the
native cairo library (``brew install cairo``). Missing dependencies produce
a clear, actionable ExportError rather than a raw ImportError.
"""

from __future__ import annotations

import ctypes.util
import logging
from pathlib import Path

from generator import constants
from generator.config import EXPORT_DIR

logger = logging.getLogger(__name__)

# Standard locations of the Homebrew cairo library on macOS (ARM / Intel).
_CAIRO_CANDIDATES = (
    "/opt/homebrew/lib/libcairo.2.dylib",
    "/usr/local/lib/libcairo.2.dylib",
)


class ExportError(Exception):
    """Raised when an atlas cannot be exported to the requested format."""


def _load_cairosvg():
    """Import cairosvg, helping cairocffi locate a Homebrew cairo library.

    The sandboxed/hardened Python runtime cannot discover ``libcairo`` by
    name, so we point ``ctypes.util.find_library`` at the absolute path of
    the Homebrew installation before cairocffi performs its lookup.
    """
    cairo_path = next(
        (candidate for candidate in _CAIRO_CANDIDATES if Path(candidate).exists()),
        None,
    )
    if cairo_path is not None:
        original_find_library = ctypes.util.find_library

        def find_library(name: str, _orig=original_find_library) -> str | None:
            if "cairo" in name:
                return cairo_path
            return _orig(name)

        ctypes.util.find_library = find_library

    try:
        import cairosvg
    except (ImportError, OSError) as exc:
        raise ExportError(
            "PDF/PNG export requires the optional 'cairosvg' package and the "
            "native cairo library. Install them with: "
            "brew install cairo && .venv/bin/pip install cairosvg "
            f"(original error: {exc})"
        ) from exc
    return cairosvg


def _resolve_output(output: Path | None, volume_name: str, fmt: str) -> Path:
    """Resolve the output path, defaulting to export/<volume_name>.<fmt>."""
    if output is not None:
        path = Path(output)
    else:
        path = EXPORT_DIR / f"{volume_name}.{fmt}"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def export(
    svg: str,
    *,
    fmt: str = "svg",
    output: Path | None = None,
    volume_name: str = "atlas",
) -> Path:
    """Write the rendered atlas to disk in the requested format.

    Args:
        svg: The rendered SVG document.
        fmt: Target format: ``svg``, ``pdf``, or ``png``.
        output: Explicit output path; defaults to ``export/<volume>.<fmt>``.
        volume_name: Atlas volume name used for the default file name.

    Returns:
        The path of the written file.

    Raises:
        ExportError: If the format is unknown or its backend is unavailable.
    """
    path = _resolve_output(output, volume_name, fmt)

    if fmt == "svg":
        path.write_text(svg, encoding="utf-8")
    elif fmt in ("pdf", "png"):
        cairosvg = _load_cairosvg()
        converter = cairosvg.svg2pdf if fmt == "pdf" else cairosvg.svg2png
        converter(
            bytestring=svg.encode("utf-8"),
            write_to=str(path),
            dpi=constants.TARGET_DPI,
        )
    else:
        raise ExportError(f"Unknown export format: {fmt!r}")

    logger.info("Exported atlas to %s (%d bytes)", path, path.stat().st_size)
    return path
