# Proportion Redesign Spec — Card & Panel Density

**From:** k4 (aesthetics owner) · **To:** k2 (implementer) · **Cc:** k0 (PM)
**Trigger:** owner directive — "示意图的比例不好，导致整个页面有大量的空白，不够充实" (vol01 band cards: image strips too small, page feels empty).
**Scope:** `generator/layout/bands.py`, `generator/render/bands.py`, `generator/render/helpers.py`. One engine pass; all 14 volumes regenerate.
**Hard constraint:** the Round-2/Round-3 unified skeleton does NOT change — header/legend/footer/NEXT devices, circled numbering, neutral border discipline, font floors, canvas widths, and the portrait/landscape orientation split all stay exactly as accepted.

All numbers below are in SVG viewBox units (vol01: canvas 1682 × 2524, scale ≈ 5.9 export px per unit).

---

## 1. Measurements — current vs. owner's taste benchmark

### 1.1 vol01 band card (the complaint), current

Card box: **189 × 234** (band content area; `band_card_h: 238` in vol01 meta, 6 cards + 2 side panels per band).

| Zone | Units | % of card | Note |
|---|---|---|---|
| pad + year chip | 8 + 22 | 13% | fine |
| title zh (≤2) + title en | ~28–45 | 12–19% | fine |
| **image (photo block)** | **76 h (raster 64)** | **32% (raster 27%)** | **aspect 161:76 ≈ 2.3:1 letterbox — too thin** |
| desc (≤2 lines) | 16–32 | 7–14% | top-anchored under image |
| **void (desc → citation gap)** | **27–43** | **12–18%** | caused by bottom-anchored citation |
| citation (≤2 lines) | 13–26 | 6–11% | pinned to card bottom |

Image **area** fraction: 161 × 64 / (189 × 234) ≈ **23%**.

### 1.2 Reference benchmark `assets/reference/volumes/0.AI编年史.png` (1024 × 1536)

Era-1 card ≈ 94 × 164 px, measured on the full-res crop:

| Zone | % of card | Note |
|---|---|---|
| header (year + zh + en, centered) | ~28% | compact |
| **image** | **~35% of height, aspect ≈ 1.4:1, area fraction ≈ 32%** | square-ish, dominant |
| caption (bold desc ≤2 + citation, **one continuous block**) | ~30% | flows to card bottom |
| void | **≈ 0–5%** | no anchored gaps |

### 1.3 The gap, quantified

- Image area fraction: **23% (ours) vs ~32% (reference)**; image aspect **2.3:1 (ours) vs ~1.4:1 (reference)** — our images are thin letterbox strips; the reference's are near-3:2 blocks.
- Guaranteed dead zone in every card: **12–18%** of card height (bottom-anchored citation). Across 6 bands × 6 cards this is the "大量空白" the owner sees.
- Band side panels (`时代特征` / `为什么失败?`): top-packed 30-unit rows inside 234-unit content → 4-item side panel fills only 160/234 ≈ **68%**, bottom third empty.

### 1.4 Other volumes (sampled from current exports)

| Sample | Measurement | Verdict |
|---|---|---|
| vol05 §应用场景 icon cards | icon ≈ 13 units ≈ 22% of card height; reference vol05's equivalent icons ≈ 30–35% | icons one size too small; acceptable but thin |
| vol01b 关键人物 figures | generic person glyph ø ≈ 30 units, rows top-packed @68 | glyph small; reserved for portrait images later |
| vol10 §③ 系统架构 | 7 sparse mini-columns, panel fill < 50% | **not fixable by proportion alone — see §7** |
| vol10 §④ family panels | 4–5 short rows in tall panels | **content problem — see §7** |

---

## 2. D1 — Band card interior reallocation (vol01-style era bands)

**Same card box, better interior.** Do not grow the canvas to fix proportions; reallocate the 12–18% citation void into the image.

### New card anatomy (top → bottom)

```
┌─────────────────────────────┐
│ [year]            org       │  pad 8, chip 22 (unchanged)
│ 标题 Title (≤2 lines)        │  16 pt, pitch 17 (unchanged)
│ Title EN                    │  11 pt (unchanged)
│ ┌─────────────────────────┐ │
│ │                         │ │
│ │      IMAGE (elastic)    │ │  ← fills all space between
│ │      aspect 1.25–1.75   │ │    title zone and caption block
│ │                         │ │
│ └─────────────────────────┘ │
│ desc line 1                 │  ┐
│ desc line 2                 │  │ caption block = ONE bottom-
│ citation line 1 (italic)    │  │ anchored unit, no internal
│ citation line 2             │  ┘ gap (desc ≤2 @15, citation ≤2 @12)
└─────────────────────────────┘
```

### Rules

1. **Caption block (desc + citation) is bottom-anchored as ONE unit.** Citation immediately follows desc (4-unit gap), both inside the same block; the block's bottom sits at `y + h - 8`. This deletes the 27–43-unit void. (Current code anchors citation alone at the bottom and top-anchors desc under the image — that split is the bug.)
2. **Image is the elastic element.** `image_h = card_h − header_zone − caption_h − pads`. Text sets the minimum; the image absorbs per-card differences in caption length.
3. **Aspect clamp:** image aspect (w/h) must stay within **[1.25, 1.75]**. If a short caption would push aspect below 1.25, cap `image_h` and let the caption sit directly under the image (top-anchored), accepting a bottom void **≤ 8% of card height**; never stretch the image thinner than 1.75:1 — instead reduce the band's `card_h` (see rule 4).
4. **Band `card_h` is content-driven:** `card_h = max over cards( header_zone + caption_h + inner_w / 1.75 )`, clamped to ≥ 200. Keep `band_card_h` as a meta override floor. Layout must compute this per band (captions are already wrapped via `wrap_fit`, so line counts are known at layout time — add a `band_card_caption_lines()` helper in `render/helpers.py` shared by layout and render, same pattern as `list_row_height`).
5. **Worked vol01 numbers** (inner_w = 161, title 1 line + en):
   header_zone ≈ 74; caption 1 desc + 1 cite ≈ 31 → image 129 (aspect 1.25);
   caption 2 + 2 ≈ 58 → image 102 (aspect 1.58).
   `card_h` lands ≈ **234–248** vs. 234 today — image grows from 76 to **102–129 units** (+34–70%), image area fraction 23% → **~33–38%**, matching the reference.
6. **Band bottom padding** 16 → 8 to absorb the small `card_h` growth (net band delta ≤ +2 units; vol01 poster ratio moves ≤ +0.01, inside the 1.35–1.63 portrait band — verify after regen and report the new ratio).
7. Keep the polaroid matte (6-unit `photo_fill` border) and `image_focus` behavior unchanged.

## 3. D2 — Band side panels: justify, don't top-pack

Current: items at fixed 30-unit rows from the top; bottom third empty when items are few.

Rule: `pitch = clamp(30, content_h / max(n_items, 1), 52)`; if the clamped stack is still shorter than `content_h`, **vertically center** the stack. Side panels reach ≥ 90% fill at any item count. Header row of the side panel keeps its current style.

## 4. D3 — `cards` kind (vol03–13 icon mini-cards): image-ready proportions

The follow-up task will bring images to these cards. Define the geometry NOW so images drop in without a second layout pass:

1. **With `image` set:** image strip at the card top, full inner width, height = **42% of card body** (clamp aspect [1.6, 2.2]); the icon (if any) becomes a 20-unit badge overlapping the image's bottom-left corner; title/bullets flow below. Card height formula gains `image_h + 8`.
2. **Without image (today):** icon size 13 → **18 units** when the card has ≤ 2 bullets (fills the card better, matches reference vol05's icon weight); unchanged for denser cards.
3. Min-fill rule: bullets zone must occupy ≥ 55% of card body; if not, step title/bullet fonts up one step (they currently only ever step down) before accepting void.

## 5. D4 — `figures` kind (vol01b 关键人物)

1. Avatar glyph ø 30 → **44 units**; when a portrait `image` is supplied later, it fills that circle (or a 44 × 56 rounded rect with the polaroid matte for non-headshot sources).
2. Rows: distribute the N figure rows evenly across the panel body (pitch = body_h / n, clamp [68, 96]) instead of top-packing at 68 — same justify rule as D2.

## 6. D5 — Page-level density rules (engine-wide)

1. **Panel body fill ≥ 85%.** After layout, if a panel's content fills less than 85% of its body, apply the grow order: (a) image areas (elastic kinds), (b) row pitch up to 1.4× natural, (c) one font step up where allowed, (d) only then shrink the panel. Never ship dead space inside a card/panel when (a)–(c) can absorb it.
2. **Void caps:** ≤ 8% of height inside any card; ≤ 15% inside any panel body (tables/pills/chevrons exempt — their geometry is already exact).
3. **Row equalization:** extend the existing stack slack-distribution (layout/bands.py `compute_bands`) so a short cell in a `row` distributes leftover into its *internal* pitch (list rows, card bullets) rather than hugging the top.
4. **No-image kinds** (never add images, keep textual): `table`, `pills`, `chevrons`, `timeline` milestone chips, `family` model rows, `industry`, `pyramid`, `wheel`, `radial`, `curve`, `arch` flow rows, `quote`, `mainline`, `insights`. Images live only in: `band` cards (D1), `cards` (D3), `figures` (D4), `hero` diagram zone.
5. **Guardrails (must not regress):** font floors (caption ≥ 12 pt, citation ≥ 9.5 pt); polaroid matte 6; `wrap_fit` whole-token wrapping from Round 3; all Round-2 skeleton elements; canvas widths and orientation split; export still SVG→PDF/PNG at 300 DPI.

---

## 7. For k0 — proportion alone won't fix these (need content/layout restructuring)

1. **vol10 §③ 系统架构** — 7 sparse mini-columns in a wide frame (< 50% fill even after pitch rules). Needs restructuring into an `arch`-style flow or merging with §②; assign to content + layout, not this pass.
2. **vol10 §④ 四大世界模型家族** — family panels carry 4–5 short rows; panels stay thin unless content adds rows (desc/应用 footer per family, as other volumes do).
3. **vol03 生态图谱 / vol13 §⑦ AGI 生态全景** — ragged chip-row ends are a column-count/content problem, not proportions.
4. **vol06 canvas ratio 1.308** — marginally under the 1.35 portrait floor (carried from Round 3, cosmetic).

---

## 8. Acceptance checks (k4 will verify after regen)

1. vol01 band-1 full-res crop: image aspect in [1.25, 1.75], image ≥ 40% of card height, zero measurable gap between desc and citation, all 36 cards equal height per band.
2. Side panels: no bottom void > 10% in any of vol01's 12 side panels.
3. Full sweep of all 14 posters: no panel body below 85% fill except exempt kinds; no new overflow/collision; skeleton elements (header/legend/footer/NEXT/numbering) pixel-identical in style.
4. vol01 poster ratio within 1.35–1.65; other 13 ratios unchanged ±0.02.
