# Aesthetic Review — Modern AI Atlas Posters (v0.1 series, 14 volumes)

**From:** k4 (visual acceptance) · **To:** k0 (PM) · **Scope:** design quality only — content fidelity already passed (see `docs/ACCEPTANCE_REPORT.md`)
**Benchmark:** Apple / Google design language — generous whitespace, restrained color, clear typographic hierarchy, consistent alignment, zero visual noise. **Method:** full-view inspection of all 14 export PNGs plus ~25 targeted full-resolution crops of weak areas.

**Verdict in one line:** the series currently looks like **three different products** — a dark engine (vol01/vol02), a light engine (vol01b, vol03–13), and wild per-volume canvas sizes. Individual panels are often good (vol02's family grid, vol01's new image cards), but the set does not yet read as ONE atlas from ONE design system. Most fixes below are **engine-level**, so k2 can fix once and regenerate all 14.

---

## 1. Executive Summary — Top Systemic Issues (ranked by visual impact)

### S1. Canvas size chaos — the 14 posters are not one physical series
Widths alternate between 9933 px and 14906 px; heights range from 10996 px (vol11) to 24012 px (vol08) — a **2.2× height spread**. vol03/vol11 are landscape, vol07/vol08 are ultra-tall portrait (aspect ≈ 0.42), the rest hover near A-ratio. Printed side by side they cannot tile, and aspect alone makes them look unrelated.
**Fix (engine):** pick ONE sanctioned canvas per orientation (recommend: all portrait A-ratio, e.g. 9933 × 14058) and make `layout.compute()` fit content to the canvas — compress/expand section gaps, not the canvas. Overflow should trigger font/spacing scale-down, never canvas growth.
**Effect:** instant series identity; the single highest-impact change.

### S2. Two unrelated design systems (dark vol01/02 vs light vol01b + vol03–13)
Header grammar differs per engine: vol01 = bare white title on dark; vol02 = gold "AI Technology Bible" + legend panel inside the header; light engine = dark rounded brand chip "Modern AI Atlas · Vol.xx" + bilingual title + quote box. Legend placement differs (header vs footer). Only vol01/vol02 have the NEXT-volume panel. Nothing tells a viewer these belong to the same atlas.
**Fix (engine):** define ONE header spec and ONE footer spec used by every volume regardless of theme: brand block + volume chip (left), bilingual title + subtitle (center-left), quote (right), legend (footer, single position), dark footer band with series line, and the NEXT-volume card on **all** volumes. Theme (dark/light) may vary per volume but the skeleton must not.
**Effect:** series coherence without forcing a single color scheme.

### S3. Vertical whitespace mismanagement — half-empty panels everywhere
Panels take equal row heights while content is unequal, producing large voids: vol01b "典型 AI 系统工作流程" panel is ~70% empty white box; vol10 "系统架构" is 7 sparse mini-columns in a wide empty frame; vol11 "代表性框架/平台" ends at 40% height; vol08 "身体层" box: 3 items in a tall box; vol13 "具身智能+世界模型闭环": a small diagram floating in a panel ~60% void; vol07 "技术路线演化" boxes ~40% empty at bottom.
**Fix (engine):** content-driven panel heights + row-level height balancing (distribute leftover space to gaps, not inside panels); vertically center sparse diagram content; enforce a "max emptiness" rule (e.g. panel content must fill ≥ 70% or the panel shrinks).
**Effect:** the Apple-style "everything breathes, nothing is abandoned" feel.

### S4. Section numbering is inconsistent — and buggy
Three numbering styles coexist: none (vol03/04/05/06), circled digits ① (vol07/08/09/12/13), zero-padded "01" (vol10/11). vol09 **skips ④ entirely** (jumps ③→⑤). vol10 places numbers out of reading order ("13 未来趋势" sits in the upper-right middle of the poster, before 06/07/08; "12/10/11" at the bottom). vol13 mixes circle colors per section without a legible rule.
**Fix (engine):** one numbering style for all volumes (recommend the vol10/11 "01" plain style — quietest), auto-assigned strictly in visual reading order (row-major), with a build-time assertion for gaps.
**Effect:** removes an entire class of "why does this jump?" moments.

### S5. Rainbow borders — accent color has no discipline
Item chips/cards each get their own saturated border: vol05 "应用场景" uses 9 border colors in one panel; vol08 "感知系统" 12; vol13 "关键挑战" 8; vol06 "应用领域" 6. Against the Apple/Google bar this reads as confetti, not hierarchy — color stops meaning anything.
**Fix (engine):** neutral gray (or theme-border) outlines for all item chips; one accent hue per *panel* expressed through the small icon/bullet only. Reserve saturated fills for year chips and era headers (which already work well).
**Effect:** immediate calm; hierarchy comes from type and spacing, not chroma.

### S6. Chevron band overuse and floating bands
Thin full-width chevron strips appear as standalone bands with dead space above/below (vol10 has **three** near-identical ones: "02 技术路线", "10 学习路线", "11 技术路线演化"; vol13 has two; vol09/12 one each). They duplicate content and fragment the grid.
**Fix (engine + content):** cap at ONE chevron band per poster, always embedded inside a padded section panel (never floating between sections); merge duplicate roadmap/evolution bands in vol10's knowledge file.
**Effect:** fewer horizontal seams, less repetition.

### S7. Chart quality below the bar (vol03 "涌现能力阶梯")
Data labels collide with the curve ("上下文学习 ICL" crosses the line; "通用智能 AGI 潜力" wraps mid-word above its dot); axis ticks are literal strings "10^8" instead of superscripts; no label-collision avoidance.
**Fix (engine):** label placement rules (offset above/below alternating, clamp inside plot), render exponents as superscripts, drop labels that can't fit.
**Effect:** the one true "chart" in the series stops looking hand-drawn.

### S8. Decorative clutter
Floating ornaments with no function: pale radar-circle inside vol04 "未来趋势", pale globe icons (vol09, vol13), a tiny ✦ sparkle at the right header edge of every light-engine poster, heavy connector lines in vol02's fusion band. None survive an Apple-style edit.
**Fix (engine):** delete or demote to ≤5% opacity brand marks; keep the footer globe only.

---

## 2. Per-Volume Notes

| Volume | Biggest aesthetic weakness | Specific fix | Severity |
|---|---|---|---|
| vol01 AI Evolution | Era-6 right region and card rows leave ragged voids; white-background images glow against dark cards | Balance last-row cell widths; add consistent 8 px inner matte + radius to all image cards | Medium |
| vol01b Foundations | "典型 AI 系统工作流程" panel ~70% empty; "表示范式演进" band has a right-side void | Fill/shrink panel per S3; right-align or widen the band content | **High** |
| vol02 Transformer Empire | Fusion band: content floats in a tall dark void; connector lines heavy | Vertically center band content or cut band height ~40%; thin the fan-in lines | Medium |
| vol03 LLM Era | Landscape canvas (series outlier); 涌现能力阶梯 chart label collisions (S7) | Re-flow to portrait canvas; fix chart labels | **High** |
| vol04 Multimodal AI | Ultra-narrow tall canvas; radar ornament; ecosystem pill columns ragged at bottom | Re-fit canvas per S1; delete ornament; equalize pill column lengths | **High** |
| vol05 Generative AI | "应用场景" 9-color chip borders; bottom ecosystem columns unbalanced | Apply S5 neutral borders; balance column item counts | Medium |
| vol06 Reinforcement Learning | RL Loop chevron floats with void; rainbow paradigm chips | Embed loop in its panel; S5 borders | Low–Med |
| vol07 Computer Vision | Aspect 0.42 — absurdly tall; sec② boxes ~40% empty; very dense bottom | Fixed canvas (S1) forces re-flow; shrink boxes to content (S3) | **High** |
| vol08 Embodied AI | Tallest poster (24012 px); repeated half-empty boxes (身体层, 大脑模型) | S1 + S3; this volume needs the deepest re-flow | **High** |
| vol09 Autonomous Driving | **Section ④ missing**; "HD Xap" typo in 感知技术全景 (should be HD Map); bottom 学习路线图 floats | Fix numbering (S4); correct label; embed band | **High** |
| vol10 World Models | Numbering spatially scrambled (13 before 06); 3 duplicate chevron bands; family panels half-empty; "V→JEPA2" arrow-glyph glitch (should be V-JEPA2) | S4 re-order; merge bands (S6); fill family panels (S3); fix glyph/font | **High** |
| vol11 AI Agents | Landscape, shortest poster; 09 全景架构 columns ragged (6/12/5 rows); 框架/平台 panel half-empty | Balance column row counts; S3 fill | Medium |
| vol12 AI Systems | Closest to bar; ⑦ stack rows end ragged mid-panel; 推理引擎 chip row floats | Extend rows or center them; minor | Low |
| vol13 Towards AGI | 闭环 diagram lost in a 60%-void panel; right prediction column overlong vs left; mixed circle colors | Rebalance two-column ratio; center/enlarge diagram; unify numbering style | Medium |

---

## 3. vol01 Image-Card Appendix (all 36 cards, deep check)

Crop quality: the wide letterbox slice-crop works well overall — subjects survive in 30 of 36 cards. Rounded corners and consistent card geometry confirmed. Mixing photos with white-background diagrams is acceptable, but white-background images visually "glow" against the dark theme; a uniform inner matte (already mostly present) should be enforced on every card.

| Era | Card | Verdict |
|---|---|---|
| 1 萌芽时代 | 1950 图灵测试 (Turing portrait) | **Keep** — face well framed |
| | 1956 达特茅斯会议 (group photo) | **Keep** |
| | 1966 ELIZA (terminal screenshot) | **Keep** — dark but legible; watch contrast at print size |
| | 1970s 专家系统 (computer photo) | **Keep** |
| | 1980s AI Winter (snowflake grid) | **Re-source** — decorative, off-topic; use a period headline/funding-drought graphic |
| | 1989 Backprop (network diagram) | **Keep** |
| 2 机器学习时代 | 1990 统计学习 (VC diagram) | **Keep** |
| | 1995 SVM (margin diagram) | **Keep** |
| | 1998 CNN (LeNet diagram) | **Keep** |
| | 2001 LSTM (cell diagram) | **Keep** |
| | 2008 深度学习复兴 (GPU chip photo) | **Keep** — strong |
| | 2011 Google Brain (face collage) | **Keep** — busy but on-topic |
| 3 深度学习革命 | 2012 AlexNet (architecture) | **Keep** |
| | 2013 Word2Vec (CBOW/skip-gram) | **Keep** |
| | 2014 Seq2Seq (diagram) | **Keep** |
| | 2015 ResNet (residual diagram) | **Keep** |
| | 2015 Attention (dark text screenshot) | **Re-source** — illegible gray-on-black at card size; use the Bahdanau alignment heatmap on white |
| | 2016 AlphaGo (Go board photo) | **Keep** — excellent |
| 4 Transformer时代 | 2017 Transformer (architecture) | **Keep** |
| | 2018 BERT (pre-training diagram) | **Keep** |
| | 2019 GPT-2 (diagram) | **Keep** |
| | 2019 T5 (diagram) | **Keep** |
| | 2020 GPT-3 (pale table screenshot) | **Re-source** — washed-out light-blue text, near-illegible; use the GPT-3 scaling curve or few-shot table with real contrast |
| | 2020 ViT (architecture) | **Keep** |
| 5 Foundation Model时代 | 2021 InstructGPT (scaling chart) | **Keep** |
| | 2022 RLHF (pipeline diagram) | **Keep** |
| | 2022 ChatGPT (OpenAI knot) | **Keep** — brand mark acceptable for a product card |
| | 2023 GPT-4 (benchmark bars) | **Keep** |
| | 2023 Stable Diffusion (astronaut horse) | **Keep** — best card on the poster |
| | 2023 SAM/DINOv2 (diagram) | **Keep** |
| 6 Foundation AI时代 | 2024 Qwen/DeepSeek (logo strip) | **Re-source or re-compose** — truncated mid-logo ("Qwe…deepse"), harsh white strip; compose proper side-by-side logos with padding |
| | 2024 多模态大模型 (diagram) | **Keep** |
| | 2024 World Model (Earth from space) | **Keep** — strong |
| | 2024 VLA/OpenVLA (diagram) | **Keep** |
| | 2024 Embodied AI (humanoid face) | **Adjust focus → center/bottom** — top of head clipped by the slice-crop; or re-source to a full-body humanoid shot |
| | 2024+ AutoDriving (self-driving car photo) | **Keep** |

**Score: 30 keep · 4 re-source (AI Winter, Attention, GPT-3, Qwen/DeepSeek) · 1 focus-adjust (Embodied AI) · 1 contrast-watch (ELIZA).**

---

## 4. What Already Looks Good (do NOT regress)

1. **vol01 era-band system** — numbered era headers with accent colors, consistent card grid, year chips; the new real-image cards are a major upgrade and the crop treatment mostly works.
2. **vol02 header typography** — gold kicker / huge white title / bilingual subtitle hierarchy is the best title block in the series; adopt it as the header spec baseline.
3. **vol02 family-panel grid** — colored header bands + aligned model rows + year chips: clean, dense, aligned; this is the panel system to generalize.
4. **Dark footer quote band + NEXT-volume card (vol01/02)** — a great series device; standardize it across all 14 (S2).
5. **Light-engine bilingual section headers** (bold zh + quiet gray en) — consistent and readable across vol01b/03–13.
6. **vol12 overall** — density, alignment, and restraint are closest to the reference posters; use it as the light-engine reference implementation.
7. **Legend-in-footer pattern** (light engine) — right idea; just make the position identical everywhere.

---

# Round 1+2 Verification (k4 re-inspection of regenerated exports)

**Method:** fresh full-view inspection of all 14 regenerated PNGs + 15 targeted full-res crops (vol01 image rows 1/3/4/6, vol03 chart, vol06/vol09 footers, vol07 §⑥/§⑮, vol09 §⑨, vol10 §⑦, vol12 §⑤, vol02 fusion band, vol13 loop panel).

## Per-finding status

| Finding | Status | Evidence |
|---|---|---|
| S1 canvas chaos | **FIXED** | Measured: portrait 1.367–1.631 (9 volumes), landscape 0.711–0.943 (5 volumes). All within stated targets; series tiles correctly |
| S2 two design systems | **FIXED (1 residual)** | All 14 share one header skeleton (wordmark + Vol chip / bilingual title / quote right), legend row under header where a legend exists, unified footer band, NEXT teaser on all except vol13. *Residual:* vol01/02 header wordmark reads "AI Technology Bible" while their footer brand reads "Modern AI Atlas" — pick one |
| S3 whitespace voids | **FIXED** | vol01b workflow panel now filled with chevron flow; vol13 loop diagram enlarged; vol11 rebalanced; vol02 fusion band fills the width. Remaining voids (vol10 family panels, §⑦) are coupled to the text-fit bug below, not layout |
| S4 numbering | **FIXED** | vol09 continuous ①–⑫ (④ 感知技术全景 restored, "HD Map" confirmed); vol10 renumbered ①–⑫ in reading order (spot-checked: ⑥ 未来趋势 now correctly sequenced after ⑤); circled numerals engine-wide; vol10 family panels no longer A–D |
| S5 rainbow borders | **FIXED** | vol05 应用场景, vol08 感知系统, vol13 挑战 all now neutral gray borders + colored icon/bullet only. Saturated fills remain only on year chips / era headers, as intended |
| S6 chevron overuse | **FIXED** | vol04 radar ornament gone; vol13 down to embedded flow strips; vol06 RL loop embedded in its panel. vol10 still carries 3 flow strips (②/⑪/⑫) but all embedded in padded panels with distinct content — acceptable |
| S7 vol03 chart | **FIXED** | Verified at full res: true superscripts (10⁸–10¹³⁺), all five labels clear of the curve, no collisions, no mid-word wraps |
| S8 decorative clutter | **FIXED** | vol04 radar circle deleted; floating globes deleted (vol09/13); ✦ sparkle gone from light-engine headers |
| vol01 image cards | **FIXED** | All 4 re-sources verified at full res: AI Winter→DEC PDP-10 panel (on-topic), Attention→Bahdanau alignment heatmap (legible), GPT-3→arXiv scaling figure (colored curves, readable), Qwen/DeepSeek→clean side-by-side composite. Embodied AI humanoid now full head + shoulders (focus=bottom ✓). Uniform light matte confirmed on all checked cards (eras 1–6) |

## New defects introduced by Round 2 (must-fix before delivery)

The canvas normalization squeezed column widths, and the text-fitting rule **hard-ellipsizes instead of wrapping** — while unused void sits directly below the same items:

1. **vol07 §⑥ 视觉大模型与基础模型 — 6 of 8 items ellipsized** ("SAM 2 (Meta AI, 202…", "Florence (Microsoft…", "InternVL (上海人工智…", "Qwen-VL Vision Enco…", "SigLIP (Google, 202…", "DINOv2 (Meta AI, 20…"). **Severity: high.**
2. **vol07 §⑮ 未来趋势 — 5 of 7 items ellipsized** ("视觉基础模型 (更大…", "多模态视觉理解与生…", "3D/4D 视觉与世界建…", "具身智能与机器人视…", "跨模态融合 (图文、…"). **Severity: high.**
3. **vol10 §⑦ 代表模型一览 — ~15 items ellipsized across all 7 company boxes** ("PlaNet (201…", "Dreamer 系…", "Physical In…", "Occupancy W…", "World Model…"). Panel bottom ~50% empty — room to wrap exists. **Severity: high.**
4. **vol09 §⑨ 当前面临的挑战 — 4 of 8 items ellipsized** ("长尾场景与极端场景泛化能力…", "预测的不确定性与交互博弈难…", "高精地图成本高、更新难、覆…", "大规模端到端模型的可解释性…"). **Severity: high.**
5. **Footer English line clipped mid-word — vol06** ("…towards Artificial General Int…") **and vol09** ("…in complex and uncertain…"). The other 12 footers render complete; the two longest EN strings overflow the portrait footer band's text budget. **Severity: medium.**
6. **vol12 §⑤ duplicated label** — panel header "推理引擎 Inference Engines" plus an identical row label "推理引擎 Engines" on the chip row. **Severity: low.**
7. **vol01b header chip reads "Vol.01"** — collides with vol01's "Volume 01" in the series; recommend "Vol.01b" or "Vol.01·Foundations". **Severity: low.**

**Recommended single fix (engine):** replace ellipsizing with wrap-to-two-lines (or auto-shrink font one step) inside item chips/list rows, and add a width budget + wrap for the footer EN line. One pass fixes defects 1–5 across all volumes.

## Per-volume grades (Apple/Google bar)

| Volume | Grade | Note |
|---|---|---|
| vol01 AI Evolution | **A−** | Image cards + matte are now series-best; wordmark residual only |
| vol01b Foundations | **B+** | Workflow void fixed; Vol.01 chip collision |
| vol02 Transformer Empire | **A−** | Fusion band fills width; dense but controlled |
| vol03 LLM Era | **B+** | Chart now clean; tree rows still end ragged |
| vol04 Multimodal AI | **B+** | Ornament gone; balanced; pill-heavy but tidy |
| vol05 Generative AI | **B+** | Neutral borders landed well |
| vol06 Reinforcement Learning | **B** | Footer EN clipped; otherwise solid |
| vol07 Computer Vision | **C+** | Structure hugely improved, but §⑥/§⑮ truncation is delivery-blocking; would be A− once fixed |
| vol08 Embodied AI | **B+** | Deep re-flow worked; minor airy grids |
| vol09 Autonomous Driving | **B−** | Numbering/HD Map fixed; §⑨ truncation + footer clip |
| vol10 World Models | **B−** | Renumbering correct; §⑦ truncation blocking; family panels still thin |
| vol11 AI Agents | **B+** | Whitespace much improved |
| vol12 AI Systems | **A−** | Cleanest light-engine volume; duplicate 推理引擎 label |
| vol13 Towards AGI | **B+** | Loop panel improved; ecosystem rows ragged; no NEXT (correct) |

## Verdict

**Series coherence: PASS** — the 14 posters now read as ONE design system (skeleton, type scale, footer/NEXT, numbering, border discipline all unified). **Final delivery: NO-GO until the text-fit pass lands** — defects 1–5 are all one engine change (wrap/shrink instead of ellipsize + footer EN budget). After that pass, grades project to: vol07 A−, vol09 B+, vol10 B+, vol06 B+ → series-wide GO.

---

# Round 3 Final Verification (k4 final acceptance)

**Method:** fresh JPEG full views of all 14 regenerated PNGs + full-res crops of vol07 §⑥/§⑮, vol10 §⑦, vol09 §⑨, vol06/vol09 footers, vol12 §⑤, vol01b header.

## Per-item status

| Item | Status | Evidence |
|---|---|---|
| vol07 §⑥ (was 6/8 ellipsized) | **FIXED** | All 8 items render complete with whole-token wraps ("SAM 2 (Meta AI, 2024)", "Florence (Microsoft, 2021)", "InternVL （上海人工智能实验室， 2023)", "Qwen-VL Vision Encoder （阿里巴巴， 2023)") |
| vol07 §⑮ (was 5/7) | **FIXED** | All 7 items complete; dangling parens handled ("视觉基础模型 （更大、更通用）", "3D/4D 视觉与世界建模") |
| vol10 §⑦ (was ~15) | **FIXED** | All 7 company boxes fully wrapped, zero ellipses; former bottom void absorbed by wrapped text |
| vol09 §⑨ (was 4/8) | **FIXED** | All 8 items complete ("…泛化能力不足", "…更新难、覆盖不足", "…可解释性不足") |
| Footer EN clip vol06 + vol09 | **FIXED** | vol06 ends "…Artificial General Intelligence."; vol09 ends "…uncertain environments." — both complete; other 12 footers verified complete |
| vol12 §⑤ duplicate label | **FIXED** | Single "推理引擎 Inference Engines" block; duplicated row label removed |
| vol01b chip | **FIXED** | Header chip reads "Vol.01B" |
| Footer series lines | **FIXED** | "Modern AI Atlas · Vol.xx \| <title EN>" confirmed across spot-checked volumes (02/05/06/09/13) |
| Regression sweep | **PASS** | Headers/legends/NEXT intact on all 14 (vol13 correctly has none); vol01's 36 image cards + uniform matte unchanged; numbering continuous; no wrap-induced overflows, collisions, or canvas breaches |

## Final per-volume grades

vol01 **A−** · vol01b **A−** · vol02 **A−** · vol03 **A−** · vol04 **B+** · vol05 **B+** · vol06 **A−** · vol07 **A−** · vol08 **B+** · vol09 **A−** · vol10 **B+** · vol11 **B+** · vol12 **A−** · vol13 **B+**

## Residual issues (non-blocking, ranked)

1. vol01/02 header wordmark "AI Technology Bible" vs footer brand "Modern AI Atlas" — pick one (low).
2. vol10 §③ 系统架构 still sparse; §④ family panels thin below lists (low).
3. vol06 canvas ratio 1.308, marginally under the 1.35 portrait floor — invisible in print (cosmetic).
4. Ragged chip-row ends: vol03 family tree, vol13 §⑦ ecosystem (low).

## Final verdict

**GO for series delivery.** All S1–S8 systemic findings, all Round 2 regressions, and all vol01 image-card items are verified fixed. The 14 posters read as one design system at the Apple/Google bar: unified skeleton, restrained color, consistent numbering, clean text fitting, and series devices (legend row, footer band, NEXT teaser) applied uniformly. The four residuals above are polish items for a future pass, not delivery blockers.

---

*Read-only review: no poster or code files were modified. Inspection artifacts were temporary crops under /tmp only.*
