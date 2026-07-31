"""Parser package — deserialize knowledge definitions from structured files."""

from __future__ import annotations

from generator.parser.loader import (
    EdgeRecord,
    KnowledgeData,
    KnowledgeLoadError,
    NodeRecord,
    load,
)

__all__ = [
    "EdgeRecord",
    "KnowledgeData",
    "KnowledgeLoadError",
    "NodeRecord",
    "load",
]
