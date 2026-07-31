"""Knowledge graph construction from parsed data (Stage 2 of the pipeline)."""

from __future__ import annotations

import logging

from generator.graph.models import Edge, KnowledgeGraph, Node
from generator.parser.loader import KnowledgeData

logger = logging.getLogger(__name__)


class GraphBuildError(Exception):
    """Raised when parsed knowledge data cannot form a valid graph."""


def build(data: KnowledgeData) -> KnowledgeGraph:
    """Build a KnowledgeGraph from parser output.

    Performs referential validation: every edge endpoint must reference an
    existing node id. Violations are hard errors — a silently dropped edge
    would produce a silently wrong poster (see RFC-0001, section 5).

    Args:
        data: Validated records produced by ``generator.parser.load``.

    Returns:
        The constructed KnowledgeGraph.

    Raises:
        GraphBuildError: If an edge references an unknown node id.
    """
    nodes = [
        Node(
            id=record.id,
            label=record.label,
            kind=record.kind,
            year=record.year,
            summary=record.summary,
            tags=record.tags,
            metadata=record.metadata,
        )
        for record in data.nodes
    ]
    known_ids = {node.id for node in nodes}

    edges: list[Edge] = []
    for index, record in enumerate(data.edges):
        for endpoint in (record.source, record.target):
            if endpoint not in known_ids:
                raise GraphBuildError(
                    f"edges[{index}]: unknown node id '{endpoint}' "
                    f"({record.source!r} -> {record.target!r})"
                )
        edges.append(
            Edge(
                source=record.source,
                target=record.target,
                relation=record.relation,
                metadata=record.metadata,
            )
        )

    graph = KnowledgeGraph(nodes, edges)
    stats = graph.stats()
    logger.info(
        "Built knowledge graph: %d node(s), %d edge(s), kinds=%s",
        stats["nodes"],
        stats["edges"],
        ", ".join(stats["kinds"]) or "-",
    )
    if stats["isolated_nodes"]:
        logger.warning("Isolated node(s) with no edges: %s", stats["isolated_nodes"])
    return graph
