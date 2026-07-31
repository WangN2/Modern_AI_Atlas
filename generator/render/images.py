"""Raster-image embedding for the poster renderer (Stage 4 helper).

Band-section cards may carry an ``image`` key holding a path relative to
the atlas volume directory (e.g. ``images/turing_test.jpg``). This module
loads such files, sniffs their mime type and natural pixel size with
pure-python header parsing (no Pillow dependency), and embeds them into
the SVG as base64 data URIs so the poster stays self-contained (cairosvg
renders data URIs directly).

Card schema (both keys optional):

    image        relative path to a jpg/png/webp file inside the atlas dir;
                 when present it replaces the line schematic in the card's
                 mini-diagram area (the schematic stays as fallback)
    image_focus  "top" | "center" | "bottom" — vertical anchor of the
                 slice-crop (preserveAspectRatio xMidYMin/Mid/Max slice)

Paths are confined to the atlas volume directory: absolute paths and
``..`` segments are rejected, and resolved paths must stay inside it.
"""

from __future__ import annotations

import base64
import itertools
import logging
import struct
from dataclasses import dataclass
from pathlib import Path

from generator.render.helpers import fmt

logger = logging.getLogger(__name__)

MIME_BY_EXT = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp",
}

_FOCUS_PAR = {
    "top": "xMidYMin slice",
    "center": "xMidYMid slice",
    "bottom": "xMidYMax slice",
}


@dataclass(frozen=True)
class EmbeddedImage:
    """One raster file resolved to an embeddable base64 data URI."""

    data_uri: str
    mime: str
    width: int  # natural pixel width; 0 when the header could not be parsed
    height: int


def sniff_size(data: bytes, mime: str) -> tuple[int, int] | None:
    """Parse PNG/JPEG/WebP headers for the natural pixel size.

    Returns ``None`` when the bytes do not match the expected container
    (e.g. an HTML error page saved with an image extension).
    """
    if mime == "image/png":
        # 8-byte signature, then IHDR length(4) + type(4) + width(4) + height(4)
        if data[:8] == b"\x89PNG\r\n\x1a\n" and data[12:16] == b"IHDR":
            width, height = struct.unpack(">II", data[16:24])
            return int(width), int(height)
        return None
    if mime == "image/jpeg":
        if data[:2] != b"\xff\xd8":
            return None
        # Walk marker segments until a start-of-frame marker with dimensions.
        pos = 2
        while pos + 9 < len(data):
            if data[pos] != 0xFF:
                pos += 1
                continue
            marker = data[pos + 1]
            if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                pos += 2  # stand-alone markers carry no length field
                continue
            seg_len = struct.unpack(">H", data[pos + 2: pos + 4])[0]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                          0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                height, width = struct.unpack(">HH", data[pos + 5: pos + 9])
                return int(width), int(height)
            pos += 2 + seg_len
        return None
    if mime == "image/webp":
        if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
            return None
        chunk = data[12:16]
        if chunk == b"VP8 ":
            # Lossy bitstream: 14-bit width/height after the start code.
            start = data.index(b"\x9d\x01\x2a", 20)
            width, height = struct.unpack("<HH", data[start + 3: start + 7])
            return width & 0x3FFF, height & 0x3FFF
        if chunk == b"VP8L":
            b0, b1, b2, b3 = data[21:25]
            width = 1 + (((b1 & 0x3F) << 8) | b0)
            height = 1 + (((b3 & 0x0F) << 10) | (b2 << 2) | ((b1 & 0xC0) >> 6))
            return width, height
        if chunk == b"VP8X":
            w_bytes = data[24:27] + b"\x00"
            h_bytes = data[27:30] + b"\x00"
            width = struct.unpack("<I", w_bytes)[0] + 1
            height = struct.unpack("<I", h_bytes)[0] + 1
            return width, height
    return None


class ImageEmbedder:
    """Resolve and base64-embed card images confined to the atlas dir.

    Results are cached per file for the lifetime of one render so repeated
    references to the same image embed only once.
    """

    def __init__(self, atlas_dir: Path) -> None:
        self._base = Path(atlas_dir).resolve()
        self._cache: dict[str, EmbeddedImage | None] = {}
        self._clip_ids = itertools.count(1)

    def _resolve(self, rel_path: str) -> Path | None:
        """Confinement check: reject absolute paths and escapes from base."""
        rel = Path(rel_path)
        if rel.is_absolute() or ".." in rel.parts:
            logger.warning("Card image path %r escapes the atlas dir; skipped",
                           rel_path)
            return None
        resolved = (self._base / rel).resolve()
        if not resolved.is_relative_to(self._base):
            logger.warning("Card image path %r resolves outside %s; skipped",
                           rel_path, self._base)
            return None
        if not resolved.is_file():
            logger.warning("Card image not found: %s", resolved)
            return None
        return resolved

    def embed(self, rel_path: str) -> EmbeddedImage | None:
        """Load one image file and return its embeddable form (cached)."""
        if rel_path in self._cache:
            return self._cache[rel_path]
        embedded: EmbeddedImage | None = None
        path = self._resolve(rel_path)
        if path is not None:
            mime = MIME_BY_EXT.get(path.suffix.lower())
            if mime is None:
                logger.warning("Unsupported card image type: %s", path)
            else:
                data = path.read_bytes()
                size = sniff_size(data, mime)
                if size is None:
                    logger.warning("Card image %s failed header sniff "
                                   "(not a real %s?); skipped", path, mime)
                else:
                    uri = f"data:{mime};base64,{base64.b64encode(data).decode()}"
                    embedded = EmbeddedImage(uri, mime, size[0], size[1])
        self._cache[rel_path] = embedded
        return embedded

    def svg_image(self, rel_path: str, x: float, y: float, w: float, h: float,
                  *, focus: str = "center", radius: float = 6.0) -> list[str] | None:
        """Render one image letterbox-cropped to the box, corners rounded.

        The image fills the ``w x h`` box while preserving aspect ratio
        (``preserveAspectRatio ... slice``); ``focus`` picks the vertical
        anchor of the crop. Returns ``None`` when the image cannot be
        embedded, so the caller can fall back to the line schematic.
        """
        image = self.embed(rel_path)
        if image is None:
            return None
        if image.width and image.width < w:
            logger.warning("Card image %s is %dpx wide but renders at %.0fpx; "
                           "it will look soft", rel_path, image.width, w)
        clip_id = f"card-img-clip-{next(self._clip_ids)}"
        par = _FOCUS_PAR.get(focus, _FOCUS_PAR["center"])
        return [
            f'<clipPath id="{clip_id}">'
            f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" '
            f'height="{fmt(h)}" rx="{fmt(radius)}"/></clipPath>',
            f'<image x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" '
            f'height="{fmt(h)}" preserveAspectRatio="{par}" '
            f'clip-path="url(#{clip_id})" href="{image.data_uri}"/>',
        ]
