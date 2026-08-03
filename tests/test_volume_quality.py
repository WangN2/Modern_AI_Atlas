"""Acceptance checks for selected atlas volumes.

This is a small, plain-python QA harness for content and export regressions
that are easy to miss during visual iteration. It intentionally focuses on
machine-checkable risks: graph references, card image paths, export headers,
SVG canvas metadata, and stale placeholder terms.
"""

from __future__ import annotations

import re
import struct
import sys
from pathlib import Path
from typing import Any, Iterable

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from generator import build as atlas_build  # noqa: E402
from generator import constants, graph, parser, render  # noqa: E402
from generator.config import EXPORT_DIR, ROOT_DIR  # noqa: E402
from generator.render.images import MIME_BY_EXT, sniff_size  # noqa: E402


VOLUMES = {
    "vol01b_foundations_of_ai": {
        "layout": constants.LAYOUT_BANDS,
        "theme": "foundations_reference",
        "width": constants.CANVAS_WIDTH,
        "min_height": 2200,
        "orientation": "portrait",
        "min_nodes": 50,
        "min_edges": 50,
    },
    "vol02_transformer_empire": {
        "layout": constants.LAYOUT_BANDS,
        "theme": "transformer_reference",
        "width": 3520,
        "min_height": 1980,
        "orientation": "landscape",
        "min_nodes": 55,
        "min_edges": 55,
    },
}

FORBIDDEN_TERMS = (
    "GPT-5?",
    "Qwen-VLA",
    "GROOT",
    "VLLM",
    "TODO",
    "TBD",
    "lorem",
    "undefined",
)

VOL01B_BEGINNER_MARKERS = (
    "先用 30 秒认识人工智能",
    "这个领域有什么：AI 基础知识全景",
    "发生了什么：AI 如何一步步走到今天",
    "AI 将走向哪里：未来五条主线",
    "Trends, Not a Timetable",
)

VOL02_FLAGSHIP_MARKERS = (
    "十年四幕",
    "旧世界的瓶颈，如何被击穿",
    "一条信息如何穿过 Transformer",
    "三类核心架构",
    "理解边界：Transformer 不是什么",
    "Attention(Q,K,V)",
    "三个具体例子：它到底怎样工作",
    "Long Context 与外部记忆",
    "关键奠基论文",
    "Encoder 王国",
    "Decoder 王国",
    "Encoder-Decoder 王国",
    "Vision 视觉疆域",
    "Diffusion 生成疆域",
    "Multimodal 多模态疆域",
    "World / Agent 物理疆域",
    "MQA / GQA",
    "RoPE",
    "FlashAttention",
    "KV Cache",
    "MoE",
    "SFT",
    "RLHF",
    "DeepSeek-R1",
    "Qwen3",
    "GPT-4.1",
    "Gemini 2.5",
    "Cosmos 3",
)

EXPORT_FORMATS = ("svg", "pdf", "png")


def _walk(value: Any) -> Iterable[Any]:
    """Yield every nested value in dictionaries/lists."""
    yield value
    if isinstance(value, dict):
        for item in value.values():
            yield from _walk(item)
    elif isinstance(value, list):
        for item in value:
            yield from _walk(item)


def _node_refs(value: Any) -> set[str]:
    """Collect poster-side node references from nested extras."""
    refs: set[str] = set()
    for item in _walk(value):
        if isinstance(item, dict):
            node = item.get("node")
            if isinstance(node, str) and node.strip():
                refs.add(node)
            nodes = item.get("nodes")
            if isinstance(nodes, list):
                refs.update(n for n in nodes if isinstance(n, str) and n.strip())
    return refs


def _image_refs(value: Any) -> list[str]:
    """Collect card/figure image paths from nested extras."""
    refs: list[str] = []
    for item in _walk(value):
        if isinstance(item, dict):
            image = item.get("image")
            if isinstance(image, str) and image.strip():
                refs.append(image)
    return refs


def _png_size(path: Path) -> tuple[int, int]:
    """Return PNG dimensions from the IHDR header."""
    data = path.read_bytes()[:24]
    assert data[:8] == b"\x89PNG\r\n\x1a\n", f"{path} is not a PNG"
    assert data[12:16] == b"IHDR", f"{path} lacks a PNG IHDR chunk"
    width, height = struct.unpack(">II", data[16:24])
    return int(width), int(height)


def _svg_without_data_uris(svg: str) -> str:
    """Strip embedded image payloads before scanning visible SVG text."""
    return re.sub(r"data:image/[^\"']+", "data:image/<omitted>", svg)


def _check_volume(volume: str, expected: dict[str, Any]) -> None:
    atlas_dir = ROOT_DIR / "atlas" / volume

    for fmt in EXPORT_FORMATS:
        atlas_build.build(str(atlas_dir), fmt=fmt)

    knowledge = parser.load(atlas_dir)
    knowledge_graph = graph.build(knowledge)
    stats = knowledge_graph.stats()
    node_ids = {node.id for node in knowledge_graph.nodes}
    meta = knowledge.extras.get("meta", {})

    assert meta.get("layout") == expected["layout"], (volume, meta.get("layout"))
    assert meta.get("theme") == expected["theme"], (volume, meta.get("theme"))
    render.load_theme(expected["theme"])

    assert len(knowledge_graph.nodes) >= expected["min_nodes"], stats
    assert len(knowledge_graph.edges) >= expected["min_edges"], stats
    assert stats["isolated_nodes"] == [], (volume, stats["isolated_nodes"])

    missing_refs = sorted(_node_refs(knowledge.extras) - node_ids)
    assert missing_refs == [], (volume, missing_refs)

    for rel_path in _image_refs(knowledge.extras):
        rel = Path(rel_path)
        assert not rel.is_absolute() and ".." not in rel.parts, (volume, rel_path)
        image_path = (atlas_dir / rel).resolve()
        assert image_path.is_relative_to(atlas_dir.resolve()), (volume, rel_path)
        assert image_path.is_file(), (volume, rel_path)
        mime = MIME_BY_EXT.get(image_path.suffix.lower())
        assert mime is not None, (volume, rel_path)
        assert sniff_size(image_path.read_bytes(), mime) is not None, (
            volume,
            rel_path,
        )

    svg_path = EXPORT_DIR / f"{volume}.svg"
    pdf_path = EXPORT_DIR / f"{volume}.pdf"
    png_path = EXPORT_DIR / f"{volume}.png"
    for path in (svg_path, pdf_path, png_path):
        assert path.is_file(), f"missing export: {path}"
        assert path.stat().st_size > 10_000, f"export too small: {path}"

    svg = svg_path.read_text(encoding="utf-8")
    visible_svg = _svg_without_data_uris(svg)
    viewbox = re.search(r'viewBox="0 0 ([0-9.]+) ([0-9.]+)"', svg)
    assert viewbox is not None, f"{svg_path} lacks viewBox"
    width = int(float(viewbox.group(1)))
    height = int(float(viewbox.group(2)))
    assert width == expected["width"], (volume, width)
    assert height >= expected["min_height"], (volume, height)
    if expected.get("orientation") == "landscape":
        assert width > height, f"{volume} should remain landscape"
    else:
        assert width < height, f"{volume} should remain portrait"
    assert meta.get("series", "") in visible_svg, (volume, meta.get("series"))
    assert meta.get("volume", "") in visible_svg, (volume, meta.get("volume"))
    assert ";base64," not in visible_svg

    for term in FORBIDDEN_TERMS:
        assert term not in visible_svg, (volume, term)

    if volume == "vol01b_foundations_of_ai":
        for marker in VOL01B_BEGINNER_MARKERS:
            assert marker in visible_svg, (volume, marker)
    if volume == "vol02_transformer_empire":
        for marker in VOL02_FLAGSHIP_MARKERS:
            assert marker in visible_svg, (volume, marker)
        edge_keys = {
            (edge.source, edge.target, edge.relation)
            for edge in knowledge_graph.edges
        }
        assert ("vla", "openvla", "composes") in edge_keys
        assert ("qwen_vl", "openvla", "composes") not in edge_keys
        assert ("llava", "gpt4o", "converges") not in edge_keys
        assert ("llava", "gemini", "converges") not in edge_keys
        assert svg.count("<image ") >= 4, "Vol.02 must embed four source figures"

    pdf_head = pdf_path.read_bytes()[:5]
    assert pdf_head == b"%PDF-", f"{pdf_path} is not a PDF"
    png_width, png_height = _png_size(png_path)
    assert png_width > 3000 and png_height > 3000, (volume, png_width, png_height)
    if expected.get("orientation") == "landscape":
        assert png_width > png_height, f"{volume} PNG should remain landscape"
    else:
        assert png_width < png_height, f"{volume} PNG should remain portrait"


def test_selected_volume_quality() -> None:
    """Vol.01B and Vol.02 pass the bounded acceptance checklist."""
    for volume, expected in VOLUMES.items():
        _check_volume(volume, expected)


if __name__ == "__main__":
    test_selected_volume_quality()
    print(f"{len(VOLUMES)} volume(s) passed quality checks.")
