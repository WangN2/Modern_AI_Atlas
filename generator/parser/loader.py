"""Loader for atlas knowledge files (Stage 1 of the build pipeline).

Reads the knowledge definition of one atlas volume from JSON (always
supported) or YAML (requires the optional ``pyyaml`` dependency, loaded via
``yaml.safe_load`` only) and returns validated, normalized records.

See RFC-0001 for the pipeline contract; the file format itself is specified
in RFC-0002.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from generator import constants

logger = logging.getLogger(__name__)

SUPPORTED_EXTENSIONS = (constants.EXT_JSON, constants.EXT_YAML, ".yml")


class KnowledgeLoadError(Exception):
    """Raised when a knowledge file cannot be read or fails validation."""


@dataclass(frozen=True)
class NodeRecord:
    """One parsed knowledge node (a paper, model, concept, event, ...)."""

    id: str
    label: str
    kind: str = "concept"
    year: int | None = None
    summary: str = ""
    tags: tuple[str, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class EdgeRecord:
    """One parsed knowledge edge between two node ids."""

    source: str
    target: str
    relation: str = "related"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class KnowledgeData:
    """Normalized intermediate representation produced by the Parser."""

    nodes: tuple[NodeRecord, ...]
    edges: tuple[EdgeRecord, ...]
    source_files: tuple[Path, ...]
    extras: dict[str, Any] = field(default_factory=dict)


def _load_yaml(path: Path) -> Any:
    """Safe-load a YAML file, requiring the optional pyyaml dependency."""
    try:
        import yaml
    except ImportError as exc:
        raise KnowledgeLoadError(
            f"Cannot parse YAML file {path}: the optional 'pyyaml' package is "
            "not installed. Install it (pip install pyyaml) or provide the "
            "knowledge definition as JSON instead."
        ) from exc
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _load_file(path: Path) -> Any:
    """Deserialize one knowledge file using only safe-loading APIs."""
    suffix = path.suffix.lower()
    try:
        if suffix == constants.EXT_JSON:
            with path.open("r", encoding="utf-8") as fh:
                return json.load(fh)
        if suffix in (constants.EXT_YAML, ".yml"):
            return _load_yaml(path)
    except (OSError, json.JSONDecodeError) as exc:
        raise KnowledgeLoadError(f"Failed to read {path}: {exc}") from exc
    raise KnowledgeLoadError(f"Unsupported knowledge file type: {path}")


def _require_str(record: dict[str, Any], key: str, *, where: str) -> str:
    """Extract a required non-empty string field from a record."""
    value = record.get(key)
    if not isinstance(value, str) or not value.strip():
        raise KnowledgeLoadError(
            f"{where}: field '{key}' must be a non-empty string, got {value!r}"
        )
    return value


def _parse_nodes(raw: Any, *, where: str) -> list[NodeRecord]:
    """Validate and normalize the 'nodes' section of one file."""
    if raw is None:
        return []
    if not isinstance(raw, list):
        raise KnowledgeLoadError(f"{where}: 'nodes' must be a list")

    nodes: list[NodeRecord] = []
    seen_ids: set[str] = set()
    for index, item in enumerate(raw):
        item_where = f"{where}: nodes[{index}]"
        if not isinstance(item, dict):
            raise KnowledgeLoadError(f"{item_where}: must be an object")
        node_id = _require_str(item, "id", where=item_where)
        label = _require_str(item, "label", where=item_where)
        if node_id in seen_ids:
            raise KnowledgeLoadError(f"{item_where}: duplicate node id '{node_id}'")
        seen_ids.add(node_id)

        year = item.get("year")
        if year is not None and not isinstance(year, int):
            raise KnowledgeLoadError(f"{item_where}: 'year' must be an integer")
        tags = item.get("tags", [])
        if not isinstance(tags, list) or not all(isinstance(t, str) for t in tags):
            raise KnowledgeLoadError(f"{item_where}: 'tags' must be a list of strings")

        nodes.append(
            NodeRecord(
                id=node_id,
                label=label,
                kind=item.get("kind", "concept"),
                year=year,
                summary=item.get("summary", ""),
                tags=tuple(tags),
                metadata=item.get("metadata", {}),
            )
        )
    return nodes


def _parse_edges(raw: Any, *, where: str) -> list[EdgeRecord]:
    """Validate and normalize the 'edges' section of one file."""
    if raw is None:
        return []
    if not isinstance(raw, list):
        raise KnowledgeLoadError(f"{where}: 'edges' must be a list")

    edges: list[EdgeRecord] = []
    for index, item in enumerate(raw):
        item_where = f"{where}: edges[{index}]"
        if not isinstance(item, dict):
            raise KnowledgeLoadError(f"{item_where}: must be an object")
        edges.append(
            EdgeRecord(
                source=_require_str(item, "source", where=item_where),
                target=_require_str(item, "target", where=item_where),
                relation=item.get("relation", "related"),
                metadata=item.get("metadata", {}),
            )
        )
    return edges


def _find_knowledge_files(atlas_dir: Path) -> list[Path]:
    """Locate the knowledge file(s) of an atlas volume directory."""
    candidates = sorted(
        path
        for ext in SUPPORTED_EXTENSIONS
        if (path := atlas_dir / f"{constants.KNOWLEDGE_GRAPH_FILE}{ext}").is_file()
    )
    if not candidates:
        expected = ", ".join(
            f"{constants.KNOWLEDGE_GRAPH_FILE}{ext}" for ext in SUPPORTED_EXTENSIONS
        )
        raise KnowledgeLoadError(
            f"No knowledge file found in {atlas_dir} (expected one of: {expected})"
        )
    return candidates


def load(atlas_dir: Path) -> KnowledgeData:
    """Load and validate all knowledge files for one atlas volume.

    Args:
        atlas_dir: Directory of the atlas volume to parse.

    Returns:
        KnowledgeData with normalized node and edge records.

    Raises:
        KnowledgeLoadError: If a file is missing, unreadable, or invalid.
    """
    atlas_dir = Path(atlas_dir)
    files = _find_knowledge_files(atlas_dir)
    logger.info("Parsing %d knowledge file(s) from %s", len(files), atlas_dir)

    nodes: list[NodeRecord] = []
    edges: list[EdgeRecord] = []
    extras: dict[str, Any] = {}
    global_ids: set[str] = set()
    for path in files:
        raw = _load_file(path)
        if not isinstance(raw, dict):
            raise KnowledgeLoadError(f"{path}: top level must be an object")
        file_nodes = _parse_nodes(raw.get("nodes"), where=str(path))
        for node in file_nodes:
            if node.id in global_ids:
                raise KnowledgeLoadError(
                    f"{path}: node id '{node.id}' already defined in another file"
                )
            global_ids.add(node.id)
        nodes.extend(file_nodes)
        edges.extend(_parse_edges(raw.get("edges"), where=str(path)))
        # Extra top-level sections (meta, families, ...) are passed through
        # for the poster renderer; their schema is formalized in RFC-0002.
        for key, value in raw.items():
            if key not in ("nodes", "edges"):
                extras[key] = value

    logger.info("Parsed %d node(s) and %d edge(s)", len(nodes), len(edges))
    return KnowledgeData(
        nodes=tuple(nodes),
        edges=tuple(edges),
        source_files=tuple(files),
        extras=extras,
    )
