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


def card_title_layout(card: dict, card_w: float, tx_off: float) -> tuple[list[str], float]:
    """Return (title_lines, title_size) for a cards-kind mini card.

    Titles wrap to two lines at 13 pt; narrow cards drop one font step
    (11 pt) before any ellipsis fallback.
    """
    title = card.get("title", "")
    lines = wrap(title, (card_w - tx_off - 8) / 13)
    if len(lines) <= 2:
        return lines, 13.0
    shrunk = wrap(title, (card_w - tx_off - 8) / 11)
    if len(shrunk) <= 2:
        return shrunk, 11.0
    return wrap_fit(title, (card_w - tx_off - 8) / 13, 2), 13.0


def card_bullet_layout(bullet: str, card_w: float) -> tuple[list[str], float]:
    """Return (bullet_lines, bullet_size) for one cards-kind bullet.

    Bullets wrap to two lines at 11 pt; narrow cards drop to 9.5 pt
    (three lines) before any ellipsis fallback.
    """
    lines = wrap(bullet, (card_w - 34) / 11)
    if len(lines) <= 2:
        return lines, 11.0
    shrunk = wrap(bullet, (card_w - 34) / 9.5)
    if len(shrunk) <= 3:
        return shrunk, 9.5
    return wrap_fit(bullet, (card_w - 34) / 11, 2), 11.0


def cards_panel_card_height(items: list, card_w: float) -> float:
    """Uniform cards-kind card height that fits the tallest wrapped card.

    Baseline geometry (must match render.bands._draw_cards_panel): first
    title baseline at card top + 20, title pitch 16, bullets start at
    +44 (+16 per extra title line), each bullet occupies 18 plus its
    extra-line pitch (14 at 11 pt, 13 at 9.5 pt).
    """
    height = 0.0
    for card in items:
        tx_off = 36.0 if card.get("icon") else 12.0
        title_lines, _size = card_title_layout(card, card_w, tx_off)
        by = 44.0 + 16 * (len(title_lines) - 1)
        bullets = [str(b) for b in card.get("items", [])]
        desc = card.get("desc", "")
        if desc and bullets:
            by += 20
        for bullet in bullets:
            lines, size = card_bullet_layout(bullet, card_w)
            by += (13.0 if size < 10 else 14.0) * (len(lines) - 1) + 18
        if desc and not bullets:
            desc_lines = wrap_fit(desc, (card_w - 24) / 11, 3)
            by += 15 * (len(desc_lines) - 1) + 15
        height = max(height, by + 10)
    return height


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
