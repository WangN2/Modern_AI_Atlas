"""In-memory knowledge graph model (Stage 2 of the build pipeline)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterator


@dataclass(frozen=True)
class Node:
    """A knowledge graph node (a paper, model, concept, event, ...)."""

    id: str
    label: str
    kind: str = "concept"
    year: int | None = None
    summary: str = ""
    tags: tuple[str, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Edge:
    """A directed relation between two nodes."""

    source: str
    target: str
    relation: str = "related"
    metadata: dict[str, Any] = field(default_factory=dict)


class KnowledgeGraph:
    """A directed graph of knowledge nodes with query helpers.

    The graph is immutable after construction: add nodes and edges through
    ``generator.graph.build`` rather than mutating instances directly.
    """

    def __init__(self, nodes: list[Node], edges: list[Edge]) -> None:
        self._nodes: dict[str, Node] = {node.id: node for node in nodes}
        self._edges: list[Edge] = list(edges)
        self._outgoing: dict[str, list[Edge]] = {node.id: [] for node in nodes}
        self._incoming: dict[str, list[Edge]] = {node.id: [] for node in nodes}
        for edge in self._edges:
            self._outgoing[edge.source].append(edge)
            self._incoming[edge.target].append(edge)

    # -- queries ----------------------------------------------------------

    def node(self, node_id: str) -> Node:
        """Return the node with the given id, raising KeyError if absent."""
        return self._nodes[node_id]

    def successors(self, node_id: str) -> list[Node]:
        """Return nodes directly reachable from ``node_id``."""
        return [self._nodes[edge.target] for edge in self._outgoing[node_id]]

    def predecessors(self, node_id: str) -> list[Node]:
        """Return nodes with an edge pointing to ``node_id``."""
        return [self._nodes[edge.source] for edge in self._incoming[node_id]]

    def out_edges(self, node_id: str) -> list[Edge]:
        """Return edges leaving ``node_id``."""
        return list(self._outgoing[node_id])

    def in_edges(self, node_id: str) -> list[Edge]:
        """Return edges entering ``node_id``."""
        return list(self._incoming[node_id])

    # -- containers ---------------------------------------------------------

    @property
    def nodes(self) -> tuple[Node, ...]:
        return tuple(self._nodes.values())

    @property
    def edges(self) -> tuple[Edge, ...]:
        return tuple(self._edges)

    def __len__(self) -> int:
        return len(self._nodes)

    def __contains__(self, node_id: object) -> bool:
        return node_id in self._nodes

    def __iter__(self) -> Iterator[Node]:
        return iter(self._nodes.values())

    # -- diagnostics --------------------------------------------------------

    def stats(self) -> dict[str, Any]:
        """Return summary statistics for logging and debugging."""
        degrees = {
            node_id: len(out) + len(self._incoming[node_id])
            for node_id, out in self._outgoing.items()
        }
        return {
            "nodes": len(self._nodes),
            "edges": len(self._edges),
            "kinds": sorted({node.kind for node in self._nodes.values()}),
            "isolated_nodes": sorted(
                node_id for node_id, degree in degrees.items() if degree == 0
            ),
        }
