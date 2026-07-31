"""Graph package — build and query the in-memory knowledge graph."""

from __future__ import annotations

from generator.graph.builder import GraphBuildError, build
from generator.graph.models import Edge, KnowledgeGraph, Node

__all__ = ["Edge", "GraphBuildError", "KnowledgeGraph", "Node", "build"]
