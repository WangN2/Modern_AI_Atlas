"""Shared SVG text helpers used by the poster renderers."""

from __future__ import annotations

from xml.sax.saxutils import escape


def fmt(value: float) -> str:
    """Format a coordinate compactly for SVG output."""
    return f"{value:.0f}" if float(value).is_integer() else f"{value:.1f}"


def trunc(text: str, limit: int) -> str:
    """Truncate long text with an ellipsis (CJK-safe, by character)."""
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def text_width(text: str, size: float) -> float:
    """Estimate rendered text width (CJK chars count full, Latin ~0.55)."""
    units = sum(1.0 if ord(ch) > 0x2E7F else 0.55 for ch in text)
    return units * size


def _wrap_tokens(text: str) -> list[str]:
    """Split text into wrappable tokens: CJK chars, spaces, Latin words."""
    tokens: list[str] = []
    word = ""
    for ch in text:
        if ord(ch) > 0x2E7F or ch == " ":
            if word:
                tokens.append(word)
                word = ""
            tokens.append(ch)
        else:
            word += ch
    if word:
        tokens.append(word)
    return tokens


def wrap(text: str, max_units: float) -> list[str]:
    """Wrap text into lines of at most ``max_units`` width units (CJK=1).

    Latin text breaks at word boundaries when possible; overlong words and
    CJK runs fall back to hard character breaks.
    """
    lines: list[str] = []
    current = ""
    current_w = 0.0
    no_break_before = "，。；：、！？）》”’"
    for token in _wrap_tokens(text):
        token_w = sum(1.0 if ord(c) > 0x2E7F else 0.55 for c in token)
        if (current and current_w + token_w > max_units
                and token not in no_break_before):
            lines.append(current.rstrip())
            current, current_w = "", 0.0
            if token == " ":
                continue
        if token_w > max_units and len(token) > 1:
            # overlong Latin word: hard-break it character by character
            for ch in token:
                w = 0.55
                if current and current_w + w > max_units:
                    lines.append(current.rstrip())
                    current, current_w = "", 0.0
                current += ch
                current_w += w
            continue
        current += token
        current_w += token_w
    if current.strip():
        lines.append(current.rstrip())
    return lines or [""]


def fit(text: str, max_units: float) -> str:
    """Truncate text to fit ``max_units`` width units, adding an ellipsis."""
    units = 0.0
    for i, ch in enumerate(text):
        w = 1.0 if ord(ch) > 0x2E7F else 0.55
        if units + w > max_units:
            return text[:i].rstrip() + "…"
        units += w
    return text


def wrap_fit(text: str, max_units: float, max_lines: int = 2) -> list[str]:
    """Wrap text to at most ``max_lines`` lines, ellipsizing on overflow.

    Unlike :func:`fit`, the ellipsis lands on a wrap boundary instead of
    mid-word, so partially shown text never cuts a token in half.
    """
    lines = wrap(text, max_units)
    if len(lines) <= max_lines:
        return lines
    kept = lines[:max_lines]
    last = kept[-1]
    if text_width(last, 1) + 1 > max_units:
        # Drop trailing whole tokens (Latin words / CJK chars / spaces)
        # until the ellipsis fits, so the cut stays on a token boundary.
        tokens = _wrap_tokens(last)
        while tokens and text_width("".join(tokens).rstrip(), 1) + 1 > max_units:
            tokens.pop()
        last = "".join(tokens).rstrip()
        # Last-resort safety for a single overlong hard-broken fragment.
        while last and text_width(last, 1) + 1 > max_units:
            last = last[:-1].rstrip()
    # Avoid ending on an unclosed parenthesis fragment such as "(NeurIPS":
    # drop the dangling token so the ellipsis follows a complete word.
    tokens = _wrap_tokens(last)
    while (tokens and len(tokens) > 1
           and ("(" in tokens[-1] or "（" in tokens[-1])
           and ")" not in tokens[-1] and "）" not in tokens[-1]):
        tokens.pop()
    if tokens:
        last = "".join(tokens).rstrip()
    kept[-1] = (last + "…") if last else "…"
    return kept


def _font_safe(content: str) -> str:
    """Substitute glyphs the export backend cannot render.

    cairosvg picks a single font without fallback, so symbols missing from
    it tofu. Runs of superscript digits collapse into caret notation
    (``10¹³⁺`` -> ``10^13+``).
    """
    content = content.replace("π", "pi").replace("⊕", "＋").replace("×", "x")
    content = content.replace("↑", "＾").replace("↓", "v")
    sup = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5",
           "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁺": "+"}
    out: list[str] = []
    i = 0
    while i < len(content):
        ch = content[i]
        if ch in sup:
            run = ""
            while i < len(content) and content[i] in sup:
                run += sup[content[i]]
                i += 1
            out.append("^" + run)
            continue
        out.append(ch)
        i += 1
    return "".join(out)


# -- shared bands text geometry -------------------------------------------------
# The helpers below are consumed by BOTH generator.layout.bands (panel
# heights) and generator.render.bands (drawing), so wrapped text can never
# outgrow the panel that contains it. Widths are in SVG units; text is
# measured in CJK width units (see text_width).


def list_item_layout(item: dict, col_w: float) -> tuple[list[str], float, list[str]]:
    """Return (title_lines, title_size, desc_lines) for a list-kind item.

    Titles wrap to two lines at 15 pt; when two lines still overflow a
    narrow column the title drops one font step (13 pt) before any
    ellipsis fallback. Descriptions wrap to two lines at 11.5 pt.
    """
    title = item.get("title", "")
    lines = wrap(title, (col_w - 28) / 15)
    size = 15.0
    if len(lines) > 2:
        shrunk = wrap(title, (col_w - 28) / 13)
        if len(shrunk) <= 2:
            lines, size = shrunk, 13.0
        else:
            lines = wrap_fit(title, (col_w - 28) / 15, 2)
    desc = item.get("desc", "")
    desc_lines = wrap_fit(desc, (col_w - 28) / 11.5, 2) if desc else []
    return lines, size, desc_lines


def list_row_height(items: list, col_w: float) -> float:
    """Uniform list-kind row height that fits every wrapped item.

    Baseline geometry (must match render.bands._draw_list): first title
    baseline at row top + 8, title pitch 17, desc block starts 20 below
    the last title baseline with pitch 15; bottom padding 13 with a desc,
    26 without (matches the legacy 56/34 single-line heights).
    """
    height = 0.0
    for item in items:
        if isinstance(item, str):
            item = {"title": item}
        title_lines, _size, desc_lines = list_item_layout(item, col_w)
        last = 8 + 17 * (len(title_lines) - 1)
        if desc_lines:
            last += 20 + 15 * (len(desc_lines) - 1) + 13
        else:
            last += 26
        height = max(height, last)
    return height


def card_title_layout(card: dict, card_w: float, tx_off: float,
                      step_up: bool = False) -> tuple[list[str], float]:
    """Return (title_lines, title_size) for a cards-kind mini card.

    Titles wrap to two lines at 13 pt (15 pt stepped up); narrow cards
    drop one font step (11 / 13 pt) before any ellipsis fallback.
    """
    base = 15.0 if step_up else 13.0
    small = 13.0 if step_up else 11.0
    title = card.get("title", "")
    lines = wrap(title, (card_w - tx_off - 8) / base)
    if len(lines) <= 2:
        return lines, base
    shrunk = wrap(title, (card_w - tx_off - 8) / small)
    if len(shrunk) <= 2:
        return shrunk, small
    return wrap_fit(title, (card_w - tx_off - 8) / base, 2), base


def card_bullet_layout(bullet: str, card_w: float,
                       step_up: bool = False) -> tuple[list[str], float]:
    """Return (bullet_lines, bullet_size) for one cards-kind bullet.

    Bullets wrap to two lines at 11 pt (12 pt stepped up); narrow cards
    drop to 9.5 / 10.5 pt (three lines) before any ellipsis fallback.
    """
    base = 12.0 if step_up else 11.0
    small = 10.5 if step_up else 9.5
    lines = wrap(bullet, (card_w - 34) / base)
    if len(lines) <= 2:
        return lines, base
    shrunk = wrap(bullet, (card_w - 34) / small)
    if len(shrunk) <= 3:
        return shrunk, small
    return wrap_fit(bullet, (card_w - 34) / base, 2), base


def cards_geometry(step_up: bool = False) -> dict[str, float]:
    """Vertical geometry constants for a cards-kind mini card.

    Must match render.bands._draw_cards_panel: first title baseline at
    card top + 20, bullets start at ``bullets_start`` (+ title pitch per
    extra title line), each bullet occupies ``bullet_row`` plus its
    extra-line pitch; a desc above the bullets costs ``desc_row``.
    ``step_up`` shifts one font step up for sparse cards (D3 min-fill).
    """
    return {
        "title_pitch": 17.0 if step_up else 16.0,
        "bullets_start": 46.0 if step_up else 44.0,
        "bullet_row": 20.0 if step_up else 18.0,
        "desc_row": 22.0 if step_up else 20.0,
    }


def card_bullet_pitch(size: float) -> float:
    """Line pitch for a cards-kind bullet at the given font size."""
    if size < 10:
        return 13.0
    if size < 11.5:
        return 14.0
    return 15.0


def card_step_up(card: dict, card_w: float) -> bool:
    """Whether a cards-kind mini card steps its fonts up one step.

    D3 min-fill rule: when the bullets zone would occupy less than 55%
    of the card body at base fonts, the title/bullets bump one font step
    so the text fills the card instead of leaving a bottom void. Cards
    with an image strip never step up (the image is the elastic filler).
    """
    bullets = [str(b) for b in card.get("items", [])]
    if not bullets or card.get("image"):
        return False
    tx_off = 36.0 if card.get("icon") else 12.0
    title_lines, _size = card_title_layout(card, card_w, tx_off)
    geo = cards_geometry(False)
    by = geo["bullets_start"] + geo["title_pitch"] * (len(title_lines) - 1)
    if card.get("desc"):
        by += geo["desc_row"]
    zone = 0.0
    for bullet in bullets:
        lines, size = card_bullet_layout(bullet, card_w)
        zone += card_bullet_pitch(size) * (len(lines) - 1) + geo["bullet_row"]
    body = by + zone + 10
    return zone / body < 0.55


def card_text_height(card: dict, card_w: float,
                     step_up: bool | None = None) -> float:
    """Text-zone height of one cards-kind mini card (title + bullets).

    Excludes the optional top image strip; includes the top offset to
    the first title baseline (20) and the 10-unit bottom pad. Mirrors
    render.bands._draw_cards_panel exactly.
    """
    if step_up is None:
        step_up = card_step_up(card, card_w)
    geo = cards_geometry(step_up)
    tx_off = 36.0 if card.get("icon") and not card.get("image") else 12.0
    title_lines, _size = card_title_layout(card, card_w, tx_off, step_up)
    by = geo["bullets_start"] + geo["title_pitch"] * (len(title_lines) - 1)
    bullets = [str(b) for b in card.get("items", [])]
    desc = card.get("desc", "")
    if desc and bullets:
        by += geo["desc_row"]
    for bullet in bullets:
        lines, size = card_bullet_layout(bullet, card_w, step_up)
        by += card_bullet_pitch(size) * (len(lines) - 1) + geo["bullet_row"]
    if desc and not bullets:
        desc_lines = wrap_fit(desc, (card_w - 24) / 11, 3)
        by += 15 * (len(desc_lines) - 1) + 15
    return by + 10


def card_image_height(card: dict, card_w: float, card_h: float) -> float:
    """Elastic image-strip height for a cards-kind card with ``image``.

    D3: the strip targets 42% of the card body with the aspect clamped
    to [1.6, 2.2]; it elastically absorbs any card height the text zone
    does not use. Strip geometry: 10-unit inset, 8-unit gap to the text.
    """
    strip_w = card_w - 20.0
    text_h = card_text_height(card, card_w)
    image_h = card_h - 18.0 - text_h
    return min(max(image_h, strip_w / 2.2), strip_w / 1.6)


def cards_panel_card_height(items: list, card_w: float) -> float:
    """Uniform cards-kind card height that fits the tallest wrapped card.

    Cards with an ``image`` key gain a top image strip sized at 42% of
    the card body (aspect clamped to [1.6, 2.2]) plus an 8-unit gap.
    """
    height = 0.0
    for card in items:
        text_h = card_text_height(card, card_w)
        if card.get("image"):
            strip_w = card_w - 20.0
            # image_h = 0.42 * card_h and card_h = 18 + image_h + text_h.
            image_h = 0.42 / 0.58 * (18.0 + text_h)
            image_h = min(max(image_h, strip_w / 2.2), strip_w / 1.6)
            height = max(height, 18.0 + image_h + text_h)
        else:
            height = max(height, text_h)
    return height


# -- band card (vol01-style era bands) shared geometry ------------------------------
# Consumed by BOTH generator.layout.bands (_band_height) and
# generator.render.bands (_draw_card), so the elastic image zone and the
# bottom-anchored caption block never disagree (D1).


def band_card_header_offset(card: dict, inner_w: float) -> float:
    """Distance from card top to the image zone top (photo_y - y).

    Geometry (frozen from Round 3): pad 8, year chip zone 42, zh title
    (16 pt, pitch 17, up to two lines), en title slot, 9-unit gap.
    """
    title_lines = wrap(card.get("title", ""), inner_w / 16)[:2]
    return 50.0 + 17.0 * len(title_lines) + 9.0


def band_card_caption_lines(card: dict, inner_w: float) -> tuple[list[str], list[str]]:
    """Return (desc_lines, citation_lines) for a band card's caption block.

    desc + desc2 wrap together to at most two lines at 12 pt; the
    citation ellipsizes on a wrap boundary at two lines of 9.5 pt.
    """
    desc_lines: list[str] = []
    for field in ("desc", "desc2"):
        value = card.get(field, "")
        if value:
            desc_lines.extend(wrap(value, inner_w / 12))
    citation = card.get("citation", "")
    cite_lines = wrap_fit(citation, inner_w / 9.5, 2) if citation else []
    return desc_lines[:2], cite_lines


def band_card_caption_height(desc_lines: list, cite_lines: list) -> float:
    """Caption-block height including the 8-unit bottom pad.

    D1: desc (pitch 15) and citation (pitch 12) form ONE bottom-anchored
    unit separated by a 4-unit gap — no internal void.
    """
    height = 15.0 * len(desc_lines) + 12.0 * len(cite_lines)
    if desc_lines and cite_lines:
        height += 4.0
    return height + 8.0


def band_card_height(cards: list, card_w: float, floor: float = 200.0) -> float:
    """Content-driven uniform band card height (D1 rule 4).

    Every card's image zone is guaranteed at least ``inner_w / 1.75``
    tall (the letterbox end of the aspect clamp); ``band_card_h`` from
    meta/theme acts as an override floor and the result never drops
    below 200.
    """
    inner_w = card_w - 16.0
    need = 0.0
    for card in cards:
        desc_lines, cite_lines = band_card_caption_lines(card, inner_w)
        need = max(need,
                   band_card_header_offset(card, inner_w)
                   + band_card_caption_height(desc_lines, cite_lines)
                   + inner_w / 1.75)
    return max(200.0, floor, need)


def family_label_lines(label: str, w: float, *, with_year: bool) -> list[str]:
    """Family model-row label: legacy single line, else wrap to two lines.

    Labels that fit the legacy one-line budget keep rendering exactly as
    before; only labels that would have been ellipsized wrap (at 12.5 pt).
    """
    if with_year:
        budget = (w - 96) / 11.5 + 3
        wrap_units = (w - 96) / 12.5
    else:
        budget = (w - 54) / 11.5
        wrap_units = budget
    if text_width(label, 1) <= budget:
        return [label]
    return wrap_fit(label, wrap_units, 2)


def family_desc_lines(desc: str, w: float) -> list[str]:
    """Family model-row description: wraps to two lines (all row styles)."""
    return wrap_fit(desc, (w - 96) / 11.5, 2)


def pills_line_breaks(pills: list, panel_w: float, label_w: float) -> list[int]:
    """Start index of each line when a pills-kind row wraps its chips to
    new lines instead of dropping them at the panel edge.

    Mirrors render.bands._draw_pills geometry: chips start after the
    label cell; a chip followed by a same-line chip costs 16 (arrow),
    otherwise 8.
    """
    avail = panel_w - 32 - label_w - 12
    widths = [text_width((p if isinstance(p, str) else p.get("text", "")), 11) + 20
              for p in pills]
    breaks = [0]
    px = 0.0
    for j, pw in enumerate(widths):
        if px + pw > avail and px > 0:
            breaks.append(j)
            px = 0.0
        px += pw
        if j < len(widths) - 1:
            if px + 18 < avail and px + 16 + widths[j + 1] <= avail:
                px += 16
            else:
                px += 8
    return breaks


def text(x: float, y: float, content: str, size: float, fill: str,
         *, bold: bool = False, anchor: str = "start",
         spacing: float | None = None, italic: bool = False,
         opacity: float | None = None) -> str:
    """Build one <text> element.

    Applies font-safe substitutions for glyphs the export backend cannot
    render (cairosvg picks a single font without fallback).
    """
    content = _font_safe(content)
    attrs = (f'x="{fmt(x)}" y="{fmt(y)}" font-size="{fmt(size)}" '
             f'text-anchor="{anchor}" fill="{fill}"')
    if bold:
        attrs += ' font-weight="bold"'
    if italic:
        attrs += ' font-style="italic"'
    if spacing:
        attrs += f' letter-spacing="{spacing}"'
    if opacity is not None:
        attrs += f' fill-opacity="{opacity}"'
    return f"<text {attrs}>{escape(content)}</text>"
