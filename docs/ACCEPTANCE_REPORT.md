# Acceptance Report — Modern AI Atlas Poster Regeneration (14 Volumes)

- Reviewer: **k4** (final cross-check, read-only)
- Date: 2026-07-30
- Scope: `export/vol*.png` (14 posters, code-generated SVG → PNG, full-res ~10k–15k px wide) cross-checked against `assets/reference/volumes/*.png` and `docs/specs/vol*.md`
- Method: full-view comparison at 1536 px + 2–4 full-resolution crops per volume (dense bands, formulas, tables, key labels). Checks: theme family, section presence/order, header/quote/legend/footer bands, tofu boxes, truncation, overflow/overlap.

## Verdict Table

| # | Volume | Export | Verdict |
|---|--------|--------|---------|
| 1 | vol01 AI 编年史 / AI Evolution | `vol01_ai_evolution.png` | ✅ PASS |
| 2 | vol01b 人工智能基础 / Foundations of AI | `vol01b_foundations_of_ai.png` | ❌ **FAIL** |
| 3 | vol02 Transformer 帝国 / Transformer Empire | `vol02_transformer_empire.png` | ❌ **FAIL** |
| 4 | vol03 大语言模型时代 / The LLM Era | `vol03_llm_era.png` | ⚠️ PASS-with-notes |
| 5 | vol04 多模态 AI / Multimodal AI | `vol04_multimodal_ai.png` | ⚠️ PASS-with-notes |
| 6 | vol05 生成式 AI / Generative AI | `vol05_generative_ai.png` | ✅ PASS |
| 7 | vol06 强化学习 / Reinforcement Learning | `vol06_reinforcement_learning.png` | ⚠️ PASS-with-notes |
| 8 | vol07 计算机视觉 / Computer Vision | `vol07_computer_vision.png` | ✅ PASS |
| 9 | vol08 具身智能 / Embodied AI | `vol08_embodied_ai.png` | ✅ PASS |
| 10 | vol09 自动驾驶 / Autonomous Driving | `vol09_autonomous_driving.png` | ✅ PASS |
| 11 | vol10 世界模型 / World Models | `vol10_world_models.png` | ⚠️ PASS-with-notes |
| 12 | vol11 智能体 / AI Agents | `vol11_ai_agents.png` | ⚠️ PASS-with-notes |
| 13 | vol12 AI 系统 / AI Systems | `vol12_ai_systems.png` | ✅ PASS |
| 14 | vol13 迈向 AGI / Towards AGI | `vol13_towards_agi.png` | ✅ PASS |

**Result: 8 PASS, 4 PASS-with-notes, 2 FAIL (vol01b, vol02).**

---

## FAIL Details

### FAIL 1 — vol01b `vol01b_foundations_of_ai.png`

**Section: AI 能力层次 (Capability Hierarchy) — pyramid is vertically inverted.**

- What is wrong: the export renders the 5-tier pyramid as (top→bottom) **感知 (Perceive) → 理解 (Understand) → 推理 (Reason) → 决策 (Decide) → 创造 (Create)**, with the widest tier (创造) at the bottom. The reference and spec define bottom→top = 感知 → 理解 → 推理 → 决策 → 创造, i.e. 感知 (basic) is the wide base and 创造 is the apex. The export also keeps the axis label **高阶能力 at the top / 基础能力 at the bottom**, so the printed pyramid directly contradicts its own axis: Perceive — a basic capability — sits at the top next to 高阶能力, and Create sits at the bottom next to 基础能力. This is a semantic content error, not a style deviation.
- Suggested fix: reverse the tier order so 感知 (Perceive) is the bottom (widest) tier and 创造 (Create) is the apex, matching the reference and the 基础能力→高阶能力 axis. Also check the green→orange gradient direction afterwards (reference: green base → orange/red apex).

**Section: AI 学科分支地图 (Discipline Map) — cards overlap and hide content.**

- What is wrong (verified at full resolution):
  - The **认知科学 (Cognitive Science)** card is drawn on top of the **语言学 (Linguistics)** card: the Linguistics title is partially covered ("…guistics" visible) and its first two bullets (自然语言理解 / 语义与语法) are hidden — only fragments ("解", "法") peek out.
  - The **统计学 (Statistics)** card overlaps the same Linguistics card from above, and its own lower bullets (假设检验 / 回归分析) are hidden behind the Linguistics card — only 数据建模 is visible.
  - The **哲学 (Philosophy)** card overlaps the **计算机科学 (Computer Science)** card, hiding two of its three bullets (计算理论 / 编程语言); only 算法与数据结构 is visible.
- Suggested fix: increase the radial spacing of the 8 branch cards around the center (or shrink card size / stagger radii) so no card covers another card's title or bullets.

**Minor note (not part of the FAIL):** the 典型 AI 系统工作流程 panel compresses the 6-step flow to the bottom of a tall mostly-empty panel; the 表示范式演进 arrow strip was pulled into its own band. Cosmetic only.

---

### FAIL 2 — vol02 `vol02_transformer_empire.png`

**Section: 跨领域融合 (fusion band) — center core label is clipped; connector arrows dangle.**

- What is wrong (verified at full resolution):
  - The central glowing circle's label reads **"统一的 / Transforme"** — the word *Transformer* is clipped to "Transforme" (missing the final "r"), and the entire second label line **表示空间** is missing. Spec/reference label: `统一的 Transformer 表示空间`. This is truncation/overflow on a key label — an explicit check item.
  - The six modality chips (文本/图像/视频/语音/3D/时间序列) send convergence arrows that terminate at a point floating in empty space to the **left** of the core circle instead of connecting into it.
  - The **理解** capability chip shows ghosted/duplicated glyphs (text appears printed twice with a slight offset).
  - The band as a whole has a large dead area between the chips and the core (layout balance issue).
- Suggested fix: enlarge the core circle (or shrink the label font / wrap to three lines: 统一的 / Transformer / 表示空间); anchor the six convergence arrows to the core's left edge; re-render the 理解 chip text once.

**Everything else in vol02 verified good:** header/quote/legend, 为什么是 Transformer + hero + key papers, all 8 architecture-family panels (Encoder/Decoder/Enc-Dec/Attention modules/variants/ViT/Diffusion/Multimodal — full row contents, footers, year chips), innovation timeline (8 nodes), industry/changes/future row, footer quote, NEXT Vol.03 teaser.

---

## Per-Volume Notes

### 1. vol01 — PASS
Dark navy theme, correct per-era accents (blue/green/orange/blue/purple/teal); 6 era bands with 时代特征 + 6 cards + right panel each; legend row; bottom main-line timeline (6 glowing nodes + 时间轴/核心驱动力 chips); 历史启示 row; closing quote 未来已来，唯变不变。; NEXT Vol.02 teaser; footer line. Text crops show crisp CJK, no tofu, no truncation. Minor: the 论文 citation line wraps mid-word ("Computing Machinery and Int elligence (1950)") — acceptable wrapping, not truncation.

### 2. vol01b — FAIL (see FAIL Details above)
Light theme, badge header, ribbon banner, and all other sections (timeline, 核心概念 wheel + Agent strip, 关键人物, 范式演进, 知识表示 6 cards, 应用领域 8 cards, 基础理论支撑, 关键推动因素, bottom-left legend, footer quote) verified present and correct.

### 3. vol02 — FAIL (see FAIL Details above)

### 4. vol03 — PASS-with-notes
Landscape, light theme; 11-card timeline + rocket; Model Family Tree (3 rails, all rows complete and legible); decoder-only architecture stack; next-token table; SFT→RM→RLHF flow; 6 emergent-ability chips; Scaling 3 cards; S-curve with stage callouts; 6 application cards; 5 tech-stack rows; 6 risk cards; 5 foundations; Road-to-AGI 6 chevrons + 迈向AGI的星辰大海 caption; footer. **Note:** Road-to-AGI chevron labels are white text on light blue/purple chevrons — low contrast vs the reference's dark-text steps; legible at full res but worth darkening.

### 5. vol04 — PASS-with-notes
Light lavender theme; all 11 spec sections present in order (6 era columns, 6 milestone nodes, modalities list, 2×2 paradigms, 5-column evolution path, 理解/生成 pills, tech foundations, 6-node capability wheel, 7 milestone models, 12 application tiles, datasets table, challenges/opportunities, 6 future trends, 4-column ecosystem incl. "VawCaps" [sic] kept, legend, closing banner). **Notes:** (a) the 演进路径 columns omit the reference's colored mini-diagrams (text only) — schematic simplification; (b) the 图例 sits bottom-left while the reference has it bottom-right.

### 6. vol05 — PASS
All sections present: 6-era timeline, 6 core concepts, 6 model-type cards, 5-step generative process, 5 tech foundations with inline ASCII diagrams, 4 architecture mini-diagrams (Transformer/Enc-Dec/U-Net/fusion — present), 9 application tiles + 更多领域 row, 8-row datasets table, 4 evaluation-metric groups, 6 challenges, 6 future trends, 4-column ecosystem, 9-chip legend, bilingual closing banner. "beta-VAE" substitution accepted. No text defects found in crops.

### 7. vol06 — PASS-with-notes
All sections present: 6-era timeline, 9 core elements, RL loop, 4 paradigm groups with correct chips, 7 problem settings, MDP + Bellman formula panels (font-safe substitutions "gamma/pi/sum_t" — accepted), exploration/exploitation, value-policy loop, 6-row algorithm table, 9 applications + more, 5+5 challenges/future, benchmarks (sim + real), 5-step learning roadmap + 持续迭代 label, legend, bilingual banner. **Notes:** (a) the circular RL interaction loop is rendered as a linear chevron flow (智能体→动作→环境→反馈) — content preserved, diagram simplified; (b) legend bottom-left vs spec's bottom-right.

### 8. vol07 — PASS
Numbered sections 1–15 all present: 8-era timeline, 4-stage paradigm flow, 4-layer landscape, CNN tree (9 trunk + 5 side branches), ViT family (10 entries), 8 foundation models, detection lineage (3 groups), segmentation lineage (3 groups), SSL routes (3 groups, DINO/DINOv2 split as printed), 8 application domains, 10-row datasets table, 8-row benchmarks table, 11 key papers, companies & frameworks, 7 future trends, bilingual banner. Full-res crops of the family trees and tables are crisp; no tofu, no truncation. Highest density volume — holds up.

### 9. vol08 — PASS
Numbered sections 1–13 all present: 8-era timeline, 4-layer architecture, 8-row tech-stack table, 12 sensor chips, brain-model pipeline (8 stages) + 8 representative models ("pi0" for π0 — accepted substitution; "GROOT" kept as printed per spec), 6 embodiment forms + 6 core capabilities, data/training 3 groups, 10 challenges, 7 future trends, 15 companies, 9 datasets, 9-node evolutionary roadmap + capability strip, 8-step learning roadmap, bilingual banner. No text defects in crops.

### 10. vol09 — PASS
All 12 numbered sections (4 intentionally skipped per spec) present: 7-era timeline, architecture (6 sensors + 5 pipeline cards), 5-stage roadmap, perception panorama (4 stages, **"HD Xap" [sic] kept as printed**), 5 algorithm columns (BEVFormer under 分割 as printed), 10 company cards, 10 datasets with a clarifying footnote on the DIOR [sic] entry, 5 metric groups, 7 red challenges, 6 future trends, 6 application chips, 7-node learning roadmap, bilingual footer with car placeholder. No text defects.

### 11. vol10 — PASS-with-notes
Landscape; sections 01–13 (with the printed numbering quirk: datasets = 12 left of 10/11) all present: 11-node timeline, 8-chip tech roadmap, system architecture pipeline, 4-color family tree (A green/B purple/C red/D maroon, all rows legible), 4-row paradigm table, 7 org cards, 10 challenges, 8 applications, 9 datasets, learning path + evolutionary roadmap, 6-item future trends, World Model Landscape band (6 neon columns; spec-flagged [uncertain] strings CaITta/Fisher/MEPO/SimMBM kept), en closing quote. **Note:** the Landscape band's six columns are bottom-anchored inside a tall dark band, leaving a large empty dark area above — cosmetic rebalance suggested.

### 12. vol11 — PASS-with-notes
Landscape; sections 01–11 all present: 6-satellite capability hub (orange 行动/反思 accents correct; "多模态感知如状态理解" kept per spec flag), 7-step workflow + memory sub-panel + tools/env band, 7 tool chips, MCP flow + server fan-out, 3 memory cards, 6 planning cards, 8 framework chips, 5 multi-agent modes, 5-column architecture overview with nested Agent Brain panel (memory/planning/decision sub-lists complete), 10 red challenges, 9 teal future chips, dark summary band. **Note:** sections 07 (多智能体协作) and 08 (框架/平台) are visually swapped relative to the reference order; the printed numerals still make the order unambiguous.

### 13. vol12 — PASS
Landscape; sections 01–10 all present: compute foundation (9-gen GPU list, 5-layer stack, 8 hardware components), CUDA/Tensor Core panels, 5 system-component cards (DeepSpeed typo normalized to 高效训练加速框架 — spec-allowed), 12-card training-optimization grid ([sic] strings kept: "Mixed Precision Overlap Compression", "拆分矩阵相乘", "零冗余分片"), 4+1 inference optimization, 5 distributed-systems cards, 7-layer panorama, 8 metric chips (gauges → flat chips, accepted schematic substitution), 6 trends, dark summary with layer chain and full bilingual quote (header en-quote shortened per accepted deviation).

### 14. vol13 — PASS
Landscape (near-square tall canvas — accepted deviation); sections 01–08 all present: 6-era chevron strip + 10 milestones (1969 Perceptron as printed) + 3-row capability/scale trend, 8 pillar cards + formula bar + safety strip, 5-stage next-decade roadmap (bilingual), 5-stage AGI roadmap with **阶段三 correctly highlighted orange** ("规划世界任务执行" [sic] kept), embodied/world-model 4-node loop, 8 challenge cards, 持续迭代 strip, 7-row ecosystem panorama, dark grand-summary band (6 satellite chips), full quote in footer (header en-quote shortened per accepted deviation). No text defects in crops.

---

## Cross-Cutting Observations (non-blocking)

1. **Legend placement drift (vol04, vol06):** the bottom 图例 panel is placed bottom-left in the exports; references have it bottom-right (vol04 spec §2, vol06 spec §2). Content identical.
2. **Schematic substitutions are consistent and acceptable** across all volumes: photos/logos → flat icon chips or placeholder boxes; π → "pi"/"pi0"; ⊕ → "＋"; → in formulas → ASCII arrows. No tofu boxes were found anywhere.
3. **Whitespace balance:** vol01b workflow panel, vol02 fusion band, vol10 landscape band each leave a large empty region inside a tall band — cosmetic, but worth a layout pass.
4. **Spec-flagged [sic]/[uncertain] strings** were kept as printed in every case checked (vol04 VawCaps, vol09 HD Xap + DIOR footnote, vol10 CaITta/Fisher/MEPO/SimMBM, vol12 training-grid headers, vol13 规划世界任务执行). One normalized case (vol12 DeepSpeed 高练→高效训练) is explicitly allowed by the spec.
5. **Known accepted deviations confirmed:** taller-than-2:3 canvases (vol04/07/08/09), vol13 near-square, vol12/13 shortened header en-quotes with full quotes in the footer.

## Required Actions Before Final Acceptance

1. **vol01b:** flip the 能力层次 pyramid tier order (感知 base → 创造 apex); fix Discipline Map card overlaps (语言学/统计学/计算机科学 bullets currently hidden).
2. **vol02:** repair the fusion band — unclip the core label (统一的 Transformer 表示空间), anchor convergence arrows to the core, fix the ghosted 理解 chip text.

Both fixes are localized to a single panel per volume; the remaining 12 volumes need no changes.

---

## Fix Round (post-review)

All findings were addressed by k2 and re-verified by k0 spot-check:

- **vol01b FAIL → PASS**: pyramid tier order corrected (感知 base → 创造 apex, gradient and axis labels now consistent); radial discipline map re-laid-out for n≥7 (left/right/top/bottom columns) — zero card overlap, all bullets legible.
- **vol02 FAIL → PASS**: fusion band core label complete (统一的 / Transformer / 表示空间); six convergence arrows anchored to the core edge; 理解 chip ghosting eliminated (connectors drawn under chips).
- **Notes resolved**: vol03 chevron label contrast (label_color option); vol11 section order 05→11 sequential; vol10 drivers-only mainline centered.
- **Deferred**: vol04/vol06 legend horizontal alignment (no payload option; non-blocking).

Regression after fixes: tests 6/6 pass; all 14 volumes rebuilt in SVG/PDF/PNG; unchanged volumes' SVG output provably identical.
