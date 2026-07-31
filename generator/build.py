"""Build CLI — entry point for generating atlas volumes from knowledge definitions.

Usage:
    python build.py atlas/vol02_transformer_empire
    python build.py atlas/vol02_transformer_empire --format pdf
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import Sequence

from generator import constants, exporter, graph, layout, parser, render
from generator.config import ATLAS_DIR

logger = logging.getLogger(__name__)


def _setup_logging(*, verbose: bool = False) -> None:
    """Configure the root logger with a sensible default format."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="atlas-build",
        description="Build a Modern AI Atlas volume from its knowledge definition.",
    )
    parser.add_argument(
        "atlas_path",
        type=str,
        help="Path to an atlas volume directory (e.g. atlas/vol02_transformer_empire).",
    )
    parser.add_argument(
        "--format",
        choices=["svg", "pdf", "png"],
        default="svg",
        help="Output format (default: svg).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Explicit output path. Defaults to export/<volume_name>.<fmt>.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug-level logging.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"{constants.PROJECT_NAME} v{constants.VERSION}",
    )
    return parser.parse_args(argv)


def _resolve_atlas_dir(raw_path: str) -> Path:
    """Resolve and validate the user-supplied atlas path."""
    atlas_dir = Path(raw_path)
    if not atlas_dir.is_absolute():
        # Treat relative paths as relative to ATLAS_DIR's parent (the repo root)
        atlas_dir = ATLAS_DIR.parent / atlas_dir
    atlas_dir = atlas_dir.resolve()

    if not atlas_dir.is_dir():
        logger.error("Atlas directory not found: %s", atlas_dir)
        sys.exit(1)

    return atlas_dir


def build(atlas_path: str, *, fmt: str = "svg", output: Path | None = None) -> None:
    """Run the full build pipeline for a single atlas volume.

    Pipeline stages:
        1. Parse  — read YAML/JSON knowledge files
        2. Graph  — construct in-memory knowledge graph
        3. Layout — compute spatial node positions
        4. Render — draw to SVG canvas
        5. Export — convert to target format
    """
    logger.info("=== %s v%s ===", constants.PROJECT_NAME, constants.VERSION)

    atlas_dir = _resolve_atlas_dir(atlas_path)
    logger.info("Building atlas volume: %s", atlas_dir.name)
    logger.info("Output format: %s", fmt)

    # Stage 1: Parse — read YAML/JSON knowledge files
    knowledge = parser.load(atlas_dir)

    # Stage 2: Graph — construct in-memory knowledge graph
    knowledge_graph = graph.build(knowledge)

    # The knowledge file's meta section selects the theme and layout
    # template; empire_dark + the Vol.02 panel template stay the default.
    meta = knowledge.extras.get("meta", {})
    theme_name = meta.get("theme", constants.DEFAULT_THEME)
    theme = render.load_theme(theme_name)

    # Stage 3: Layout — compute poster panel positions
    positions = layout.compute(knowledge_graph, theme, knowledge=knowledge)

    # Stage 4: Render — draw to SVG canvas
    svg = render.draw(positions, theme, knowledge)

    # Stage 5: Export — convert to target format
    exporter.export(svg, fmt=fmt, output=output, volume_name=atlas_dir.name)

    logger.info("Build complete.")


def main(argv: Sequence[str] | None = None) -> None:
    """CLI entry point."""
    args = _parse_args(argv)
    _setup_logging(verbose=args.verbose)
    try:
        build(args.atlas_path, fmt=args.format, output=args.output)
    except (
        parser.KnowledgeLoadError,
        graph.GraphBuildError,
        exporter.ExportError,
    ) as exc:
        logger.error("%s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
