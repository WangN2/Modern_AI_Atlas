# Content Accuracy Review — Modern AI Atlas (14 volumes)

**To:** k0 (PM) — route fixes to k2
**From:** k5 (technical / scientific accuracy reviewer)
**Date:** 2026-07-22
**Scope:** All 14 `atlas/vol*/knowledge_graph.json` files, cross-referenced against `docs/specs/*` and `docs/AI圣经_修订版.md` (relation semantics).
**Method:** Full text extraction of every poster-visible string; expert review; targeted web verification (cited inline where used). Read-only audit — no files modified.

**Severity legend:**
- **CRITICAL** — factually wrong (wrong year, wrong attribution, fabricated entity, wrong technical claim)
- **MINOR** — imprecise / internally inconsistent / debatable convention
- **OPTIONAL** — style-level precision

**Confidence legend:** `certain` = verified against primary source or unambiguous expert knowledge; `verify` = strong suspicion, k2 should re-check the cited reference before editing.

**Global convention used in the corrections below:** year = first public release (arXiv/blog/product launch), not the later conference-publication year. This matches the existing convention already used for e.g. BERT (2018, not NAACL 2019) and RT-1 (2022, not CoRL 2023). Where a citation line mentions a later venue year, that is acceptable and should stay.

---

## 0. Rulings on preserved [sic] / [uncertain] items

Per k0's standing rule (correctness beats verbatim fidelity, precedent: "HD Xap" → "HD Map"), my ruling on every flagged item:

| # | Location | Poster print (flag) | Ruling | Correction |
|---|----------|--------------------|--------|------------|
| S1 | vol13 发展里程碑 timeline + `nodes.perceptron.year` | Perceptron **1969** [sic, "as printed per spec"] | **FIX** | **1957** (Rosenblatt, 1957; hardware 1958). 1969 is the Minsky & Papert *Perceptrons* book, not the model. If desired add footnote "1969: Minsky–Papert critique". |
| S2 | vol09 §BEV 表示 | "HD Xap" [sic] | already fixed to "HD Map" | keep |
| S3 | vol01 meta.quote | quote attributed to **图灵 (Turing)** | **FIX** | Fabricated quote. Remove the attribution (keep text unattributed) or replace with a verified Turing quote, e.g. "We can only see a short distance ahead, but we can see plenty there that needs to be done." — Turing, 1950. |
| S4 | vol10 mainline Latent Dynamics chips | `CaITta` [uncertain] · `Fisher` [uncertain] · `MEPO` · `SimMBM` [uncertain] | **FIX (remove/replace)** | None of these are identifiable world-model works (see §vol10 analysis). Replace the four chips with verifiable latent-dynamics / model-based RL works: **SimPLe (2019) · MBPO (2019) · MOPO (2020) · TIA (2020)**. |
| S5 | vol10 mainline Physics chips | `Galileo` · `Phyformer` | **FIX (remove/replace)** | No notable 2024 physics world model named "Galileo" (the only "Galileo" is Wu et al., NeurIPS **2015**, physics-engine + DL) or "Phyformer". Replace with verifiable works: **FNO (2020) · FourCastNet (2022) · Earth-2/CorrDiff (NVIDIA)**. |
| S6 | vol10 §04 roadmap chip | "规划世界任务执行" [sic — likely 现实世界任务执行] | **FIX** | "现实世界任务执行" |
| S7 | vol13 §02 pillar 5 | "环境建解" [sic] | already rendered as "环境建模" | keep |
| S8 | vol13 §04 阶段五 | "社会…协同" [partially illegible] → "社会价值协同" | keep best-read | — |
| S9 | vol13 §06 | "价值?对齐问题" [uncertain] → "价值观对齐" | keep best-read | — |
| S10 | vol13 §03/§04 illegible zh tails | best-read transcriptions | keep best-read | — |
| S11 | vol12 §03 DeepSpeed | "高练加速框架" [sic] → normalized "高效训练加速框架" | keep normalization | — |
| S12 | vol12 §04 张量并行 | "拆分矩阵相乘" [sic] | **FIX** | "拆分矩阵维度（张量切分）" |
| S13 | vol12 §04 column header | "Mixed Precision Overlap Compression" [sic] | **FIX** | "Overlap & Compression（计算通信重叠与压缩）" — mixed precision is a different optimization already listed in its own card |
| S14 | vol12 §04 显存优化 | "优化器状态分配" [uncertain] | **FIX** | "优化器状态分片" (ZeRO-1 = optimizer-state **sharding**) |
| S15 | vol01 insights 1–2 | [uncertain] best-read "智能涌现与突破" / "范式变革智能" | keep (harmless taglines) | — |
| S16 | vol01 §6 card + vol08/vol10 multiple | "GROOT" (poster spelling; spec notes NVIDIA product is GR00T) | **FIX** | **GR00T** everywhere (see vol08/vol10 tables) |
| S17 | vol10 datasets summary | "注：DIOR (2022) 按原图转录 — DIOR 实为遥感数据集" | **FIX (remove entry + note)** | Replace DIOR with a real AD dataset (see vol09 table) |
| S18 | vol07 companies | "Google — … Florence" (as printed, spec flags duplication) | **FIX** | Remove Florence from Google row (it is Microsoft; already correctly listed in the Microsoft row) |
| S19 | vol05 edge note | `gpt_4 → sora` composes (spec itself flags "uncertain") | **FIX** | Change to `converges` or drop; Sora is a diffusion-transformer, not composed from GPT-4 |
| S20 | vol10 §representative models | "Google and DeepMind separate cards — keep as printed" | keep (historically separate brands on poster; harmless) | — |

---

## 1. vol01_ai_evolution

| Location | Current text | Issue | Recommended correction | Severity | Confidence |
|---|---|---|---|---|---|
| meta.quote / quote_by | "人工智能是人类有史以来最伟大的创造……" —— 图灵 | Fabricated quote attributed to Turing (poster error, S3) | Remove attribution, or use verified Turing 1950 quote | CRITICAL | certain |
| §1 card "1989 Backprop" + `nodes.backprop.year` | 1989 | Backprop popularized by Rumelhart, Hinton & Williams, **Nature 1986**; vol13 correctly uses 1986 | 1986 | CRITICAL | certain |
| §2 card "2001 LSTM" + `nodes.lstm.year` | 2001 | LSTM is Hochreiter & Schmidhuber, **1997** (Neural Computation) | 1997 | CRITICAL | certain |
| §2 card "2008 深度学习复兴" + `nodes.dl_revival.year` | 2008 | Conventional revival year is **2006** (Hinton/Salakhutdinov DBN, Science); vol13 uses 2006 | 2006 (unify with vol13) | MINOR | certain |
| §5 card "2023 Stable Diffusion" + `nodes.stable_diffusion.year` | card year 2023, citation "(2022.8发布)" | Internally contradictory; SD released **Aug 2022**; vol02/vol05 correctly use 2022 | 2022 | CRITICAL | certain |
| §5 card "2022 RLHF" | citation "Deep RL from Human Preferences (NeurIPS 2017)（应用于大模型对齐）" | Card OK; citation already explains — fine as is | keep | OPTIONAL | certain |
| §6 card "VLA / OpenVLA — Qwen-VLA / π0" | "Qwen-VLA" | No official Alibaba model named "Qwen-VLA" (only unofficial community fine-tunes of Qwen2-VL) | Replace with a verifiable VLA, e.g. "RT-2 / π0" or "Octo / π0" | CRITICAL | verify |
| §6 card "Embodied AI — GROOT / Isaac" | GROOT | NVIDIA product is **GR00T** (Project GR00T, GTC 2024) | GR00T / Isaac | CRITICAL | certain |
| §6 card "World Model — V-JEPA2 / Cosmos", year 2024 | 2024 | V-JEPA 2 released **June 2025**; NVIDIA Cosmos announced **CES Jan 2025** ([CES 2025 coverage](https://www.robotics247.com/article/ces_2025_nvidia_launches_cosmos_world_foundation_model_expands_omniverse)) | year 2025 (or pick one 2024-era example, e.g. Genie 2) | CRITICAL | certain |
| nodes.sam / card "SAM / DINOv2" | card node points to `sam` only | DINOv2 node exists but unlinked from the card | minor data hygiene; add dinov2 link | OPTIONAL | certain |
| edges: `resnet → stable_diffusion` composes | composes | SD's U-Net uses ResNet blocks — acceptable | keep | OPTIONAL | certain |

## 2. vol01b_foundations_of_ai

Mostly clean (conceptual content, few dated claims).

| Location | Current text | Issue | Recommended correction | Severity | Confidence |
|---|---|---|---|---|---|
| §"AI 主要应用领域" → 机器人与自动化 items | last item "问答系统" | Copy-paste artifact — QA is not a robotics sub-task (also appears, legitimately, under NLP/KG) | Replace with e.g. "抓取操作" or "人机协作" | MINOR | certain |
| 关键人物 → Herbert Simon | "诺贝尔奖得主" | Correct (1978 Nobel Economics) | keep | — | certain |
| 范式演进 → 连接主义 "1980s-2000s" | era label | Connectionism's first wave is 1950s–60s (Perceptron); 1980s is the backprop revival | "1980s-2010s" or add note; low priority | OPTIONAL | certain |
| edge `vector_representation → deep_learning_paradigm` converges | converges | Fine | keep | — | certain |

## 3. vol02_transformer_empire

| Location | Current text | Issue | Recommended correction | Severity | Confidence |
|---|---|---|---|---|---|
| Decoder 架构 card | "2022 GPT-4" + `nodes.gpt4.year` 2022 | GPT-4 released **March 2023** (correct in vol01/vol03/vol05) | 2023 | CRITICAL | certain |
| Encoder 架构 card | "2022 MPNet" + `nodes.mpnet.year` 2022 | MPNet is **2020** (arXiv Apr 2020, NeurIPS 2020) | 2020 | CRITICAL | certain |
| ViT 家族 card | "2022 DINO" + `nodes.dino.year` 2022 | DINO is **2021** (arXiv Apr 2021, ICCV 2021); vol07 correctly uses 2021 | 2021 | CRITICAL | certain |
| 生成模型家族 card | "2023 DiT (Peebles & Xie)" + node 2023 | DiT arXiv **Dec 2022** (ICCV 2023). Spec already notes "paper is 2022/ICCV 2023". Also "Peebles & Xie" are authors; org = UC Berkeley / NYU | year 2022 (arXiv-first convention); org → "UC Berkeley / NYU" | MINOR | certain |
| 多模态融合家族 card | "2023 LLaVA (UC Berkeley)" | LLaVA is **UW–Madison + Microsoft Research** (+ Columbia) ([arXiv 2304.08485](https://arxiv.org/pdf/2304.08485)) | org → "UW–Madison & Microsoft" | CRITICAL | certain (verified) |
| 多模态融合家族 card + `nodes.qwen_vl.year` | 2024 | Qwen-VL released **Sep 2023** (arXiv 2023) | 2023 | CRITICAL | certain |
| Encoder 架构 card | "2023 E5 / GTE / BGE" | E5 is 2022; GTE/BGE 2023 | "(2022–2023)" | MINOR | certain |
| Encoder-Decoder card | "2023+ GLM / Baichuan / Yi…" | GLM dates to 2021 (GLM-130B 2022) | keep 2023+ as "family prominence" or note GLM (2021) | OPTIONAL | certain |
| 产业影响 → 开源生态 | "VLLM" | casing | "vLLM" | OPTIONAL | certain |
| Key Papers | BERT venue "NAACL 2019" under year 2018 | Acceptable (arXiv year + venue year) | keep | OPTIONAL | certain |
| edges | all | Consistent with semantics (bert↔roberta converges ✓, vit→swin converges ✓, clip→llava composes ✓) | keep | — | certain |

## 4. vol03_llm_era

| Location | Current text | Issue | Recommended correction | Severity | Confidence |
|---|---|---|---|---|---|
| 生态图谱 → Mistral row pills + `nodes.mixtral.label` | "Mistral 8x7B" / "Mistral 8x22B" | The MoE models are **Mixtral** 8x7B / Mixtral 8x22B | "Mixtral 8x7B" / "Mixtral 8x22B" | CRITICAL | certain |
| 生态图谱 → OpenAI row | "GPT-4o / GPT-5?" | GPT-5 released **Aug 2025**; "?" is now stale | "GPT-4o / GPT-5" | MINOR | certain |
| `nodes.mixtral.year` 2023 | covers 8x7B (Dec 2023) and 8x22B (Apr 2024) | split or use "2023–2024" | MINOR | certain |
| edge `claude3 → constitutional_ai` composes | direction inverted | Constitutional AI (2022) is the *training method* used to build Claude — component → composite convention elsewhere (ppo→rlhf) means it should be `constitutional_ai → claude2/3` | reverse edge to `constitutional_ai → claude3` | MINOR | certain |
| edge `palm2 → gemini1` inherits | inherits | Gemini is a new model family (merged Brain+DeepMind), not a direct PaLM 2 descendant | `converges` | MINOR | certain |
| edges `rlhf ↔ dpo` (both directions) | duplicated reciprocal converges | converges is undirected — keep one edge only (see Systemic #3) | delete one | MINOR | certain |
| Timeline milestone 2021 Codex "12B参数" | 12B | Correct (Codex = fine-tuned 12B GPT-3) | keep | — | certain |

## 5. vol04_multimodal_ai

| Location | Current text | Issue | Recommended correction | Severity | Confidence |
|---|---|---|---|---|---|
| meta.callout | "…… —— Fei-Fei Li" | Fabricated quote attribution | Remove attribution (see Systemic #1) | CRITICAL | certain |
| Timeline milestone | "2020 CLIP (OpenAI)" | CLIP released **Jan 2021** (paper Feb 2021); this volume's own milestone-models card and every other volume use 2021 | 2021 | CRITICAL | certain |
| Timeline milestone | "2016 Google Audio-Visual Speech" | Google's AV speech-separation work ("Looking to Listen at the Cocktail Party") is **2018** | 2018 | CRITICAL | verify |
| Timeline milestone | "1997 IBM Multimedia Search" | QBIC dates to ~1993–95; "IBM Multimedia Search 1997" not clearly identifiable | verify or drop year / use "1990s QBIC" | MINOR | verify |
| 里程碑模型 card + `nodes.vqa.year` | "2014 VQA" | VQA (Antol et al.) is **2015** (arXiv May 2015, ICCV 2015) | 2015 | CRITICAL | certain |
| 里程碑模型 card + `nodes.show_and_tell.year` | "2016 Show and Tell" | Show and Tell (Vinyals et al.) is **CVPR 2015** (arXiv Nov 2014) | 2015 | CRITICAL | certain |
| 里程碑模型 card + nodes vilbert/uniter | "2018 ViLBERT / UNITER" | ViLBERT = **2019** (arXiv Aug 2019, NeurIPS 2019); UNITER = **2019** (arXiv Sep 2019, ECCV 2020) | 2019 (both) | CRITICAL | certain |
| `nodes.llava.year` | 2024 | LLaVA is **2023** (arXiv Apr 2023, NeurIPS 2023) | 2023 | CRITICAL | certain (verified) |
| `nodes.internvl.year` | 2024 | InternVL 1.0 = Dec 2023 (CVPR 2024) — borderline; acceptable as 2024 | keep or 2023 | OPTIONAL | certain |
| 重要数据集 → WebVid | type "图像+文本", "100万视频" | WebVid is **video-text** (WebVid-2M ≈ 2.5M / WebVid-10M ≈ 10.7M) | type "视频+文本"; count "~1000万 (WebVid-10M)" | CRITICAL | certain |
| 重要数据集 → VQA v2 | "21万问答" | VQA v2 has **~1.1M questions over ~204K images** | "~110万问答 / 20万图像" | CRITICAL | certain |
| 重要数据集 → Multimodal CoT | "~100万样本" | Multimodal-CoT is built on **ScienceQA = 21,208 examples** ([LLaVA paper, ScienceQA description](https://arxiv.org/pdf/2304.08485)) | "~2.1万样本 (ScienceQA)" | CRITICAL | certain (verified) |
| 重要数据集 → COCO | "33万图像" | Correct (~328K) | keep | — | certain |
| 生态图谱 → 数据层 | "VawCaps" | Not an identifiable dataset (no "VAWCaps" in the literature) | Replace with e.g. "Visual Genome" or "COCO Captions" | CRITICAL | verify |
| edges | gpt_4v↔gemini, gemini↔claude_3, llava↔internvl, internvl↔qwen_vl, llava↔qwen_vl — each present in **both** directions | duplicated reciprocal converges edges | keep one direction per pair (Systemic #3) | MINOR | certain |

## 6. vol05_generative_ai

| Location | Current text | Issue | Recommended correction | Severity | Confidence |
|---|---|---|---|---|---|
| meta.callout | "…… —— Sam Altman" | Fabricated quote attribution | Remove attribution (Systemic #1) | CRITICAL | certain |
| 技术基础 → VAE desc | "解码器 p(z\|a)" | Math typo: decoder models **p(x\|z)** | "p(x\|z)" | MINOR | certain |
| 技术基础 → 流匹配模型 examples | "如: Imagen, Flow Matching" | **Imagen is a cascaded diffusion model**, not flow matching | Examples → "SD3, Flux (Rectified Flow)" | CRITICAL | certain |
| edge `gpt_4 → sora` composes | composes (spec flags uncertain) | Sora = diffusion transformer; not composed from GPT-4 | change to `converges` (or drop) | MINOR | certain |
| 主流生成式模型类型 → LLM examples | "GPT-4, Llama 3, Claude 3, PaLM 2" | fine | keep | — | certain |
| nodes rbm/dbn year 2006 | 2006 | OK (Hinton era; Smolensky 1986 is the original RBM — could footnote) | keep | OPTIONAL | certain |
| edges vae↔gan, bert↔gpt_series, bert↔t5, midjourney↔sd, pika↔midjourney, dreamfusion↔magic3d↔point_e | reciprocal duplicated converges | dedupe (Systemic #3) | MINOR | certain |

## 7. vol06_reinforcement_learning

Largely accurate (algorithm dates all check out: TD 1988, Q-learning 1992, REINFORCE 1992, Dyna-Q 1990, MCTS 2006, DQN 2013, DDPG 2015, TRPO 2015, A3C 2016, PPO 2017, TD3/SAC 2018, MuZero 2019/20).

| Location | Current text | Issue | Recommended correction | Severity | Confidence |
|---|---|---|---|---|---|
| meta.callout | "…… —— Richard S. Sutton" | Close paraphrase of Sutton & Barto's definition, but not a verbatim quote | Keep text; change attribution to "—— Sutton & Barto（释义）" or drop | MINOR | certain |
| `nodes.rlhf.year` 2022 | 2022 | Christiano et al. is 2017; 2022 = LLM alignment application. Same convention as vol01 | keep 2022 + add note "(2017 提出)" | OPTIONAL | certain |
| edge `dqn → alphago` converges | converges | AlphaGo used policy/value nets + MCTS, not DQN — converges is the right type | keep | — | certain |
| edges td3↔sac | reciprocal duplicated converges | dedupe | MINOR | certain |

## 8. vol07_computer_vision

| Location | Current text | Issue | Recommended correction | Severity | Confidence |
|---|---|---|---|---|---|
| meta.callout | "…… — Fei-Fei Li" | Fabricated quote attribution | Remove attribution (Systemic #1) | CRITICAL | certain |
| 代表公司与开源项目 → Google row | "SigLIP, ViT, PaLI, **Florence**" | **Florence is Microsoft** (also correctly listed in the Microsoft row); spec flags this | Remove Florence from Google row | CRITICAL | certain |
| 语义分割 lineage + `nodes.deeplab_v1.year` | "DeepLab v1 (2017)" | DeepLab v1 is **ICLR 2015** (v2 = TPAMI 2017, which is the likely confusion) | 2015 | CRITICAL | certain |
| 自监督 lineage + `nodes.ibot.year` | "iBOT (2023)" | iBOT = arXiv Nov 2021, **ICLR 2022** | 2022 | CRITICAL | certain |
| 自监督 lineage + `nodes.swav.year` | "SwAV (2021)" | SwAV = **NeurIPS 2020** | 2020 | MINOR | certain |
| 经典数据集 → COCO | "20万图像" | COCO has **~33万 (328K)** images; vol04 correctly says 33万 | "33万图像" | CRITICAL | certain |
| 经典数据集 → Pascal Context | "17万图像" | Pascal-Context annotates VOC2010: ~10K train / ~20K total images | "约2万图像" | CRITICAL | certain |
| 经典数据集 → PASCAL VOC | "2万图像" | VOC2012 trainval ≈ 11.5K; across all years ~27K — defensible | keep or "约1.2万 (VOC2007+2012)" | OPTIONAL | certain |
| ViT 家族 card | DINO 2021 ✓ (correct here, wrong in vol02) | cross-volume inconsistency — fix vol02 | see vol02 | MINOR | certain |
| Microsoft row | "Florence, U-Former" | Uformer (MSRA, CVPR 2022) exists but is an image-restoration model; possibly meant "Uniformer" | verify intent; low impact | OPTIONAL | verify |
| edges alexnet↔googlenet, beit↔mae, ssd↔yolo, detr↔faster_rcnn, simclr↔moco, moco↔byol, simsiam↔byol, simsiam↔swav | reciprocal duplicated converges | dedupe (Systemic #3) | MINOR | certain |
| edge `mae → sam_encoder` inherits | inherits | SAM's ViT-H encoder is MAE-pretrained — correct | keep | — | certain |

## 9. vol08_embodied_ai

| Location | Current text | Issue | Recommended correction | Severity | Confidence |
|---|---|---|---|---|---|
| meta.callout | "…… — Yann LeCun" | Fabricated quote attribution | Remove attribution (Systemic #1) | CRITICAL | certain |
| 代表模型 + `nodes.groot` | "GROOT (NVIDIA, 2024)" / label "GROOT" | Product is **GR00T** (Project GR00T, announced GTC March 2024) | GR00T (label, label_en; year 2024 OK) | CRITICAL | certain |
| 代表模型 + `nodes.openvla.year` | "OpenVLA (2023)" | OpenVLA is **2024** ([arXiv 2406.09246, CoRL 2024](https://arxiv.org/abs/2406.09246)) | 2024 | CRITICAL | certain (verified) |
| 代表模型 | "EmbodiedGPT (MS, 2023)" | EmbodiedGPT is **CUHK / Shanghai AI Lab / HKU** (Mu et al., [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/4ec43957eda1126ad4887995d05fae3b-Abstract-Conference.html)), not Microsoft | org → "CUHK & Shanghai AI Lab" | CRITICAL | certain (verified) |
| 代表模型 | "Qwen-VLA (阿里, 2024)" | No official Alibaba "Qwen-VLA" (unofficial community fine-tunes only) | Replace with verifiable 2024 VLA (e.g. "Octo (UC Berkeley, 2024)") or drop | CRITICAL | verify |
| 关键数据集 | "Bridge Data (Google)" | BridgeData is **UC Berkeley** (RAIL; WidowX arm) ([BridgeData V2, arXiv 2308.12952](https://arxiv.org/html/2308.12952v3)) | "Bridge Data (UC Berkeley)" | CRITICAL | certain (verified) |
| `nodes.gemini_robotics.year` | 2024 | Gemini Robotics announced **March 2025** | 2025 | MINOR | certain |
| edge `world_model → dreamer` inherits | direction | Dreamer (2019/20) precedes the generic "World Model (2024)" node; either reverse (`dreamer → world_model`) or drop | reverse or drop | MINOR | certain |
| edge `bridge_data → rt_1` composes | composes | RT-1 was trained on Everyday Robots data; BridgeData feeds RT-1-X/OpenVLA — retarget to openvla or drop | retarget to `bridge_data → openvla` | MINOR | certain |
| edges pi_0↔rt_2, pi_0↔groot, world_model↔jepa | reciprocal duplicated converges | dedupe | MINOR | certain |
| `nodes.dreamer.year` 2020 | 2020 | vol10 uses 2019 — unify (Systemic #2) | 2019 or 2020, consistently | MINOR | certain |

## 10. vol09_autonomous_driving

| Location | Current text | Issue | Recommended correction | Severity | Confidence |
|---|---|---|---|---|---|
| meta.callout | "…… —— Kai-Fu Lee" | Fabricated quote attribution | Remove attribution (Systemic #1) | CRITICAL | certain |
| 发展时间线 §1 (1980s–1990s) | items include "DARPA 自动驾驶挑战赛" | DARPA Grand Challenges were **2004/2005** (Urban Challenge 2007); the node itself correctly says 2004 | Move item to §2 (2000–2010) | CRITICAL | certain |
| 关键数据集 | "DIOR (2022)" + summary note "按原图转录 — DIOR 实为遥感数据集" | DIOR is a **remote-sensing** object-detection dataset ([arXiv 1909.00133](https://arxiv.org/pdf/1909.00133v1.pdf)) — does not belong in an AD dataset list; year also wrong (2019/2020) | Replace with e.g. "Cityscapes (2016)" or "ApolloScape (2018)"; delete the note | CRITICAL | certain (verified) |
| 关键数据集 + `nodes.argoverse2.year` | "Argoverse 2 (2019)" | Argoverse **1** is 2019 (CVPR); Argoverse 2 = [NeurIPS D&B 2021](https://github.com/argoverse/av2-api-sf) paper, released 2022–2023 | "Argoverse 2 (2021)" | CRITICAL | certain (verified) |
| 关键数据集 + `nodes.bdd100k.year` | "BDD100K (2020)" | BDD100K released **2018** (arXiv May 2018) | 2018 | CRITICAL | certain |
| 关键数据集 + `nodes.lyft_l5.year` | "Lyft Level 5 (2020)" | Lyft L5 dataset released **July 2019** | 2019 | MINOR | certain |
| 关键数据集 + `nodes.pandaset.year` | "PandaSet (2021)" | PandaSet released **2020** (scale.com, early 2020) | 2020 | MINOR | verify |
| 关键数据集 + `nodes.openlane.year` | "OpenLane (2023)" | OpenLane = **CVPR 2022** (PersFormer) | 2022 | MINOR | certain |
| 代表性算法 → 分割 (Segmentation) | list includes "BEVFormer" | BEVFormer is **BEV 3D perception/detection**, not segmentation | Move to 检测 (Detection) group or a "BEV 感知" group | MINOR | certain |
| `nodes.hivt.year` | 2021 | HiVT = **CVPR 2022** | 2022 | MINOR | certain |
| `nodes.drivegpt4.year` | 2024 | DriveGPT4 = arXiv **Sep 2023** | 2023 | MINOR | certain |
| `nodes.nio_pilot.year` | 2020 | NIO Pilot shipped **June 2019** (NIO OS 2.0) | 2019 | OPTIONAL | verify |
| `nodes.deeplab_family.year` | 2016 | DeepLab v1 = 2015 (see vol07); family span | 2015 | OPTIONAL | certain |

## 11. vol10_world_models (highest error density)

| Location | Current text | Issue | Recommended correction | Severity | Confidence |
|---|---|---|---|---|---|
| meta.callout | "…… —— Yann LeCun" | Fabricated quote attribution (LeCun's actual framing is the JEPA position paper, 2022) | Remove attribution, or cite "A Path Towards Autonomous Machine Intelligence, LeCun 2022" | CRITICAL | certain |
| Timeline milestone 2 | "2000 Kalman Filter / Particle Filter" | Kalman filter = **1960**; particle filter = **1993–96** | "1960s–1990s Kalman / Particle Filter" | CRITICAL | certain |
| Timeline milestone 3 | "2013 Model Predictive Control — 广泛应用" | MPC originates in the **1970s–80s** (Richalet 1978; DMC 1980) | "1970s–80s MPC 提出与工业应用" | CRITICAL | certain |
| Timeline milestone 4 | "2017 PlaNet" | PlaNet (Hafner et al.) = arXiv **Nov 2018**, ICML **2019**; the volume's own node says 2019 | 2019 (or 2018 arXiv) | CRITICAL | certain |
| 发展史 / models card / Meta list | "JEPA (2022) · I-JEPA (2022) · V-JEPA (2023) · V-JEPA2 (2024)" | I-JEPA = **Jan 2023** ([CVPR 2023](https://arxiv.org/html/2605.15618v1)); V-JEPA = **Feb 2024**; V-JEPA 2 = **June 2025** ([github.com/facebookresearch/vjepa2](https://github.com/facebookresearch/vjepa2)) | I-JEPA 2023 / V-JEPA 2024 / V-JEPA2 2025 (JEPA concept 2022 OK) | CRITICAL | certain (verified) |
| 发展史 milestone 9 + models card + Google list | "2023 DreamerV3 / **Genie**", "Genie (2023) 可交互生成**3D**世界" | Genie = arXiv **Feb 2024**, ICML 2024 ([arXiv 2402.15391](https://arxiv.org/abs/2402.15391)); it generates playable **2D** environments — 3D is Genie 2 (Dec 2024) | year 2024; "可交互生成2D世界（Genie 2 扩展至 3D）" | CRITICAL | certain (verified) |
| models card 物理世界模型 + nodes | "Cosmos (2024)" | NVIDIA Cosmos announced **CES January 2025** ([CES 2025 coverage](https://www.robotics247.com/article/ces_2025_nvidia_launches_cosmos_world_foundation_model_expands_omniverse)) | 2025 | CRITICAL | certain (verified) |
| models card / chips / nodes `groot` | "GROOT" (×4 occurrences incl. mainline) | **GR00T** | GR00T | CRITICAL | certain |
| DeepMind card | "MuZero (2020) **无模型RL突破**"; milestone "无模型+模型融合突破" | MuZero is **model-based** RL — it *learns* a model without being given the rules; calling it "无模型突破" is exactly backwards | "MuZero (2020) 学习隐式模型的 model-based RL 突破" | CRITICAL | certain |
| 关键数据集 | "BridgeData — 自动驾驶场景数据集" | BridgeData is a **robot manipulation** dataset (UC Berkeley, WidowX arm) — nothing to do with autonomous driving | "机器人操作数据集 (UC Berkeley)" | CRITICAL | certain (verified) |
| mainline Latent Dynamics chips | "CaITta · Fisher · MEPO · SimMBM" (S4) | Unidentifiable works — almost certainly GPT-print artifacts | Replace with "SimPLe · MBPO · MOPO · TIA" | CRITICAL | certain (not real as printed) / verify (mapping) |
| mainline Physics chips + nodes `galileo` | "Galileo · Phyformer" (S5) | No such 2024 physics world models ("Galileo" = NeurIPS 2015 physics-engine paper) | Replace with "FNO · FourCastNet · Earth-2"; delete node galileo or repurpose | CRITICAL | verify |
| mainline Embodied chips + nodes `rt2_wm`, `openvla_wm` | "OpenVLA WM · RT-2-WM" | Neither exists as a named model (RT-2 and OpenVLA are VLA policies, not world models) | Replace with verifiable embodied-WM works, e.g. "UniPi (2023) · SuSIE (2023) · π0.5 (2025)"; delete/repurpose nodes | CRITICAL | verify |
| footer | `footer.quote_zh` contains **English** text ("The next generation of AI will not only understand the world…") | Field/content mismatch — English string in the zh field | Move to `quote_en`; supply a zh translation for `quote_zh` | CRITICAL | certain |
| mainline Video chips | "Sora (Research)" | OK | keep | — | certain |
| 代表模型 → Tesla | "Occupancy World Model (2024)" | Defensible (Tesla AI Day 2022 occupancy networks; 2024 WM framing) | keep | OPTIONAL | verify |
| nodes `muzero.year` 2020 vs vol06 2019 | 2020 | MuZero arXiv Nov 2019 / Nature Dec 2020 — unify across volumes | pick one (suggest 2020, Nature) | MINOR | certain |
| nodes `mpc.year` 2013 | 2013 | see milestone fix | 1980 | MINOR | certain |

## 12. vol11_ai_agents

Largely clean (framework dates correct: LangChain/LlamaIndex 2022, AutoGPT/BabyAGI/CAMEL/MetaGPT 2023, AG2 2024, MCP 2024).

| Location | Current text | Issue | Recommended correction | Severity | Confidence |
|---|---|---|---|---|---|
| meta.callout | "…… —— Yann LeCun" | Fabricated quote attribution | Remove attribution (Systemic #1) | CRITICAL | certain |
| 代表性框架 | "AG2" | AG2 = renamed AutoGen; listing AG2 alone may confuse | keep (label_en already says "AG2 (AutoGen 系列)") | OPTIONAL | certain |
| edge `camel → ag2` converges | converges | Both are multi-agent frameworks — fine | keep | — | certain |

## 13. vol12_ai_systems

Hardware timeline fully verified correct (Fermi 2010 → Blackwell 2024; CUDA 2007; cuDNN 2014; Tensor Core 2017; NVLink 2016; NVSwitch 2018; FlashAttention 2022; ZeRO/DeepSpeed 2020; Megatron-LM 2019; vLLM/PagedAttention 2023; SGLang 2024).

| Location | Current text | Issue | Recommended correction | Severity | Confidence |
|---|---|---|---|---|---|
| §04 张量并行 bullet | "拆分矩阵相乘" [sic] (S12) | Should be splitting matrix **dimensions** (tensor sharding) | "拆分矩阵维度（张量切分）" | MINOR | certain |
| §04 column header | "Mixed Precision Overlap Compression" [sic] (S13) | Conflates three distinct optimizations; mixed precision already has its own card | "Overlap & Compression（计算通信重叠与压缩）" | MINOR | certain |
| §04 显存优化 bullet | "优化器状态分配" [uncertain] (S14) | ZeRO-1 = optimizer-state **sharding** (分片), not allocation (分配) | "优化器状态分片" | MINOR | certain |
| `nodes.pytorch.year` 2016 | 2016 | PyTorch announced Jan 2017 (initial release late 2016) | keep 2016 or 2017 | OPTIONAL | certain |
| `nodes.speculative_decoding.year` 2023 | 2023 | OK (Leviathan et al. Feb 2023; blockwise parallel decoding 2018 is the earlier root) | keep | OPTIONAL | certain |

## 14. vol13_towards_agi

| Location | Current text | Issue | Recommended correction | Severity | Confidence |
|---|---|---|---|---|---|
| 发展里程碑 + `nodes.perceptron.year` | "1969 感知机 Perceptron" [sic] (S1) | Perceptron = **Rosenblatt 1957** (Cornell; Mark I hardware 1958). 1969 = Minsky & Papert's critique book | 1957 | CRITICAL | certain |
| §04 阶段三 bullet | "规划世界任务执行" [sic] (S6) | garbled print | "现实世界任务执行" | MINOR | certain |
| §02 pillar Scaling Law bullets | "参数规模 **Data Scale**" | zh/en mismatch — 参数规模 = Parameter Scale (Data Scale = 数据规模) | "参数规模 Parameter Scale · 数据规模 Data Scale · 算力规模 Compute Scale" | MINOR | certain |
| 里程碑 | Backprop 1986 ✓ / DL revival 2006 ✓ / Deep Blue 1997 ✓ / GPT-3 2020 ✓ / ChatGPT 2022 ✓ | correct — use these as the canonical values for vol01 unification | — | — | certain |
| AGI 生态全景 → 训练与框架 | "Microsoft" pill among frameworks | Microsoft is a company, DeepSpeed is its framework (already listed) | drop "Microsoft" pill | OPTIONAL | certain |
| edges | perception→cognitive→agentic→general→superintelligence chain inherits | fine for a roadmap | keep | — | certain |

---

## 2. Systemic issues

1. **Fabricated quote attributions (8 volumes, CRITICAL).** GPT-generated posters invented inspirational quotes and attached real people's names: vol01 图灵, vol04 Fei-Fei Li, vol05 Sam Altman, vol07 Fei-Fei Li, vol08 Yann LeCun, vol09 Kai-Fu Lee, vol10 Yann LeCun, vol11 Yann LeCun. None of these are verifiable quotes. For a publication-quality atlas this is the single most embarrassing failure mode. **Recommendation: strip every attribution (keep the sentence as unattributed banner text), or replace with verified quotes.** vol06's Sutton callout is a legitimate paraphrase — keep with "（释义）" marker.
2. **Date-convention inconsistencies across volumes.** Same entity, different years: Backprop 1989 (vol01) vs 1986 (vol13); DL revival 2008 (vol01) vs 2006 (vol13); DINO 2022 (vol02) vs 2021 (vol07); Dreamer 2020 (vol08) vs 2019 (vol10); MuZero 2019 (vol06) vs 2020 (vol10); CLIP 2020 (vol04 timeline) vs 2021 (everywhere else); Stable Diffusion 2023 (vol01) vs 2022 (vol02/vol05). **Recommendation: adopt "first public release (arXiv/blog/launch)" as the single convention** — it is already the de-facto convention for BERT (2018), RT-1 (2022), etc. Canonical values: Backprop 1986, DL revival 2006, DINO 2021, Dreamer 2019, MuZero 2020 (Nature; or 2019 arXiv — pick one), CLIP 2021, SD 2022.
3. **Duplicated reciprocal `converges` edges (vol03, vol04, vol05, vol07, vol08).** Pairs like `dpo → rlhf` + `rlhf → dpo`, `gemini → gpt_4v` + `gpt_4v → gemini` render the same dashed edge twice. `converges` is undirected by the project semantics (↗ 虚线：趋同). **Recommendation: k2 dedupe — for every {A,B} converges pair keep exactly one edge.** ~20 duplicate edges across 5 volumes.
4. **"GROOT" misprint propagated across 3 volumes (vol01 §6, vol08, vol10 incl. mainline chips and node ids' labels).** Fix all occurrences to **GR00T** (node ids may stay `groot`; only labels change).
5. **Hallucinated model names from the GPT reference posters survived transcription.** "CaITta / Fisher / MEPO / SimMBM" (vol10), "Galileo / Phyformer" as 2024 physics WMs (vol10), "RT-2-WM / OpenVLA WM" (vol10), "Qwen-VLA" as an official Alibaba model (vol01/vol08), "VawCaps" (vol04). These need k5-level verification each time a new poster is transcribed — recommend adding a "fabrication check" step to the spec→JSON workflow.
6. **Field-language mismatches.** vol10 `footer.quote_zh` holds English text; vol13 "参数规模 Data Scale" zh/en gloss mismatch; vol02 "Peebles & Xie" in an org field. Low effort to fix, high polish value.
7. **vol10 is the weakest volume by far** (14 CRITICAL findings) — its timeline, landscape chips, and dataset cards all need rework; consider a full content revision pass rather than point fixes.

---

## 3. Verification log (web-checked in this review)

- LLaVA = UW–Madison + Microsoft Research (+ Columbia): [arXiv 2304.08485](https://arxiv.org/pdf/2304.08485)
- OpenVLA = 2024: [arXiv 2406.09246 / CoRL 2024](https://arxiv.org/abs/2406.09246)
- Genie = Feb 2024, ICML 2024, playable **2D** environments; Genie 2 = Dec 2024, 3D: [arXiv 2402.15391](https://arxiv.org/abs/2402.15391), [world-models.io/model-record](https://world-models.io/en/models/genie-1/)
- V-JEPA = Feb 2024; V-JEPA 2 = June 2025: [github.com/facebookresearch/vjepa2](https://github.com/facebookresearch/vjepa2); I-JEPA = CVPR 2023 (Assran et al.)
- BridgeData = UC Berkeley robot-manipulation dataset (WidowX): [arXiv 2308.12952](https://arxiv.org/html/2308.12952v3), [The Robot Report](https://www.therobotreport.com/berkeley-released-bridgedata-v2-dataset-for-robot-learning-at-scale/)
- EmbodiedGPT = Mu et al., NeurIPS 2023 (CUHK / Shanghai AI Lab / HKU): [NeurIPS 2023 proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/4ec43957eda1126ad4887995d05fae3b-Abstract-Conference.html)
- DIOR = remote-sensing detection benchmark, 23,463 images, arXiv Sep 2019: [arXiv 1909.00133](https://arxiv.org/pdf/1909.00133v1.pdf)
- Argoverse 2 = NeurIPS D&B 2021 (release 2022–23); Argoverse 1 = CVPR 2019: [argoverse/av2-api citation](https://github.com/argoverse/av2-api-sf)
- Multimodal-CoT = ScienceQA, 21,208 examples: [LLaVA paper / ScienceQA](https://arxiv.org/pdf/2304.08485)
- NVIDIA Cosmos = CES, January 2025: [robotics247 CES 2025](https://www.robotics247.com/article/ces_2025_nvidia_launches_cosmos_world_foundation_model_expands_omniverse)
- "Galileo" physics model = NeurIPS **2015** (Wu et al.), not a 2024 world model: [papers.nips.cc/paper/5780](https://papers.nips.cc/paper/5780-galileo-perceiving-physical-object-properties-by-integrating-a-physics-engine-with-deep-learning)

All other findings come from stable expert knowledge (paper years, architectures, dataset sizes) and are marked `certain` only where unambiguous.

---

## 4. Top 10 corrections (ranked)

1. **Strip fabricated quote attributions in 8 volumes** (Turing / LeCun ×3 / Fei-Fei Li ×2 / Altman / Kai-Fu Lee) — reputational risk for a publication-quality atlas.
2. **vol13: Perceptron 1969 → 1957** (node + milestone; overturn the [sic] preservation per k0's correctness rule).
3. **"GROOT" → "GR00T"** everywhere (vol01, vol08, vol10).
4. **vol10 JEPA family dates**: I-JEPA 2022→2023, V-JEPA 2023→2024, V-JEPA2 2024→2025 (and the vol01 "World Model 2024" card referencing V-JEPA2/Cosmos → 2025).
5. **vol01: LSTM 2001 → 1997; Backprop 1989 → 1986; Stable Diffusion 2023 → 2022.**
6. **vol02: GPT-4 2022 → 2023; MPNet 2022 → 2020; DINO 2022 → 2021; LLaVA org "UC Berkeley" → "UW–Madison & Microsoft".**
7. **vol10: Genie 2023 → 2024 and "3D世界" → 2D; PlaNet milestone 2017 → 2019; MuZero "无模型RL突破" → model-based RL 突破; Cosmos 2024 → 2025.**
8. **vol10: BridgeData desc "自动驾驶场景数据集" → "机器人操作数据集 (UC Berkeley)"; vol08 "Bridge Data (Google)" → "(UC Berkeley)".**
9. **vol07: remove Florence from Google row (it's Microsoft); COCO 20万→33万; Pascal Context 17万→约2万; DeepLab v1 2017→2015.**
10. **vol09: remove DIOR from the AD dataset list (replace with Cityscapes 2016 / ApolloScape 2018); Argoverse 2 (2019) → (2021); move "DARPA 挑战赛" from the 1980s–90s era to 2000–2010.**

(Runner-up cluster: vol10 hallucinated chips CaITta/Fisher/MEPO/SimMBM + Galileo/Phyformer + RT-2-WM/OpenVLA WM; vol08 OpenVLA 2023→2024 + EmbodiedGPT "MS"→CUHK/Shanghai AI Lab; vol03 "Mistral 8x…" → "Mixtral 8x…"; vol04 dataset-size errors VQA v2 / Multimodal-CoT / WebVid.)

---

## 5. Applied status (k2, 2026-07-22)

All 14 `atlas/*/knowledge_graph.json` files edited in place; all 14 volumes rebuild cleanly
(SVG; PNG spot-builds for vol01/vol07/vol10/vol13); `tests/test_bands_layout.py` 6/6 pass;
no reciprocal `converges` duplicates remain in any volume (script-verified).

### Applied — CRITICAL (58 findings, all applied or resolved)

- **Fabricated quotes (Systemic #1, 8 volumes)** — attributions stripped, sentences kept as
  unattributed banner text: vol01 `meta.quote_by` `"图灵"` → `""`; vol04 `—— Fei-Fei Li`;
  vol05 `—— Sam Altman`; vol07 `— Fei-Fei Li`; vol08 `— Yann LeCun`; vol09 `—— Kai-Fu Lee`;
  vol10 `—— Yann LeCun`; vol11 `—— Yann LeCun`. vol06 kept with `—— Sutton & Barto（释义）`
  per the report's paraphrase ruling. No new attributions invented.
- **vol01**: Backprop 1989→1986 (card + node); LSTM 2001→1997 (card + node);
  Stable Diffusion 2023→2022 (card + node, resolves the internal citation contradiction);
  World Model card + node 2024→2025; `GROOT` → `GR00T` (card title_en + node label).
- **vol02**: GPT-4 2022→2023; MPNet 2022→2020; DINO 2022→2021; DiT 2023→2022 with org
  `Peebles & Xie` → `UC Berkeley / NYU`; LLaVA org `UC Berkeley` → `UW–Madison & Microsoft`;
  Qwen-VL 2024→2023 (card + node).
- **vol03**: pills `Mistral 8x7B/8x22B` → `Mixtral 8x7B/8x22B`; `nodes.mixtral.label` likewise.
- **vol04**: CLIP timeline 2020→2021; Google AV Speech 2016→2018 (verified: arXiv 1804.03619,
  2018); IBM milestone → `1993 IBM QBIC` (verified: QBIC SPIE 1993) — node `label_en`/`year`
  updated to match; VQA 2014→2015; Show and Tell 2016→2015; ViLBERT/UNITER 2018→2019
  (cards + all nodes); `nodes.llava.year` 2024→2023; WebVid → `视频+文本`, `~1000万视频
  (WebVid-10M)`; VQA v2 → `~110万问答 / 20万图像`; Multimodal CoT → `~2.1万样本 (ScienceQA)`;
  `VawCaps` → `Visual Genome` (verified: no such dataset; likely a garbled "WavCaps", which
  is an *audio* captioning set and would not fit the row).
- **vol05**: flow-matching examples `Imagen, Flow Matching` → `SD3, Flux (Rectified Flow)`.
- **vol07**: Florence removed from Google row (stays in the Microsoft row); DeepLab v1
  2017→2015 (pill + node); iBOT 2023→2022 (pill + node); COCO 20万→33万图像;
  Pascal Context 17万→约2万图像.
- **vol08**: GR00T (card title + node label/label_en; id stays `groot`); OpenVLA 2023→2024
  (card + node); EmbodiedGPT `(MS, 2023)` → `(CUHK & 上海AI Lab, 2023)`;
  Bridge Data `(Google)` → `(UC Berkeley)`.
- **vol09**: DARPA 挑战赛 moved from the 1980s–1990s era card to 2000–2010 (its node year 2004
  was already correct); DIOR removed → `Cityscapes (2016)`, transcription note deleted
  (`summary` emptied; layout/renderer skip empty summaries safely); Argoverse 2 (2019)→(2021)
  (card + node); BDD100K (2020)→(2018) (card + node).
- **vol10 (all 14)**: Kalman milestone `2000` → `1960s–1990s Kalman / Particle Filter`
  (node → 1960); MPC `2013` → `1970s–80s …提出与工业应用` (node → 1980); PlaNet milestone
  2017→2019; JEPA family I-JEPA 2022→2023 / V-JEPA 2023→2024 / V-JEPA2 2024→2025 (family card,
  Meta list card, all three nodes); Genie 2023→2024 + `可交互生成3D世界` → `可交互生成2D世界`
  (milestone year widened to `2023–2024`; Genie 2 keeps the 3D claim); Cosmos 2024→2025
  (both family cards, NVIDIA card, node; final milestone widened to `2024–2025`);
  `GROOT` → `GR00T` ×4; MuZero `无模型RL突破` / `无模型+模型融合突破` →
  `学习隐式模型的 model-based RL 突破` (card + milestone); BridgeData desc →
  `机器人操作数据集 (UC Berkeley)`; mainline latent chips `CaITta·Fisher·MEPO·SimMBM` →
  `SimPLe·MBPO·MOPO·TIA`; physics chips `Galileo·Phyformer` → `FNO·FourCastNet·Earth-2`;
  embodied chips `OpenVLA WM`/`RT-2-WM` → `UniPi`/`SuSIE`; footer English text moved
  `quote_zh` → `quote_en`, new zh translation supplied for `quote_zh`.
- **vol13**: Perceptron 1969→1957 (milestone chip + node; overturns S1 [sic] preservation
  per the correctness rule; `editorial_notes` entry updated to record the fix).

### Applied — MINOR (all `certain` items)

- vol01 DL revival 2008→2006 (card + node, unified with vol13).
- vol01b 机器人与自动化 item `问答系统` → `人机协作`.
- vol02 `E5 / GTE / BGE` year → `2022–2023`; `VLLM` → `vLLM` (OPTIONAL, trivial).
- vol03 `GPT-5?` → `GPT-5`; edge `claude3→constitutional_ai` reversed to
  `constitutional_ai→claude3`; `palm2→gemini1` inherits→converges.
- vol05 VAE decoder `p(z|a)` → `p(x|z)`; edge `gpt_4→sora` composes→converges (S19).
- vol06 MuZero node 2019→2020 (unified with vol10 per the Nature-year suggestion).
- vol07 SwAV 2021→2020 (pill + node).
- vol08 `nodes.gemini_robotics.year` 2024→2025; `world_model→dreamer` reversed to
  `dreamer→world_model`; `bridge_data→rt_1` retargeted to `bridge_data→openvla`;
  `nodes.dreamer.year` 2020→2019 (unified with vol10).
- vol09 Lyft Level 5 (2020)→(2019); PandaSet (2021)→(2020) — **verified**: Hesai/Scale AI,
  2020; OpenLane (2023)→(2022); HiVT node 2021→2022; DriveGPT4 node 2024→2023;
  BEVFormer moved 分割 → 检测 group; NIO Pilot node 2020→2019 (OPTIONAL — **verified**:
  NIO OS 2.0.0 push, 2019-06-10).
- vol10 `nodes.mpc.year` → 1980 (with the milestone fix).
- vol12 S12/S13/S14: `拆分矩阵相乘` → `拆分矩阵维度（张量切分）`;
  `Mixed Precision Overlap Compression` → `Overlap & Compression（计算通信重叠与压缩）`;
  `优化器状态分配` → `优化器状态分片` (`editorial_notes` updated to match).
- vol13 S6 `规划世界任务执行` → `现实世界任务执行`; Scaling Law gloss
  `参数规模 Data Scale` → `参数规模 Parameter Scale`; `Microsoft` pill dropped from
  训练与框架 (OPTIONAL, trivial).
- **Systemic #3 dedupe** — 27 reciprocal `converges` duplicates removed: vol03 rlhf↔dpo (1);
  vol04 6 pairs (incl. vilbert↔uniter, one more than the report listed); vol05 8 pairs
  (incl. pika↔runway_gen3, also not listed); vol06 td3↔sac (1); vol07 8 pairs;
  vol08 3 pairs. One edge per unordered pair kept (first occurrence in file order).

### Adapted (verify items where the check changed the recommended fix)

- **"Qwen-VLA" (vol01 §6, vol08)** — k5 flagged "no official Alibaba Qwen-VLA" (`verify`).
  Re-check shows Alibaba's Qwen team shipped an **official Qwen-VLA in May 2026**
  (arXiv 2605.30280, github.com/QwenLM/Qwen-VLA), predating this review. Resolution: keep the
  model name; fix the wrong year instead — vol08 card/node `Qwen-VLA (阿里, 2024)` →
  `(阿里, 2026)`; vol01 card (no year printed, era card spans 2024–Now) unchanged.
- **vol10 physics node `galileo` / embodied nodes `openvla_wm`, `rt2_wm`** — repurposed rather
  than deleted (ids kept so edges stay valid): `galileo` → FNO (2020); `openvla_wm` → UniPi
  (2023); `rt2_wm` → SuSIE (2023). The VIMA→SuSIE→UniPi→π0 `converges` chain stays coherent.

### Skipped (with reason)

- **vol03 `nodes.mixtral.year` → "2023–2024"** — `year` is an integer consumed by the layout
  x-axis; a range string would break the schema. Left as 2023 (8x7B release year).
- **vol13 Scaling Law three-bullet rewrite** — applied the zh/en gloss fix only; adding a
  third bullet (`数据规模 Data Scale`) changes item counts ahead of the planned layout round.
- **vol07 `U-Former` (OPTIONAL, verify)** — verified it exists (Uformer, MSRA, CVPR 2022) but
  is image-restoration; intent (vs `UniFormer`) genuinely ambiguous → left as-is.
- **OPTIONAL "keep" items** (per the report's own keep rulings): vol01 RLHF citation, vol01
  SAM/DINOv2 card link, vol01b 连接主义 era label, vol02 GLM `2023+`, vol04 InternVL 2024,
  vol06 RLHF 2022 note, vol09 `deeplab_family` 2016, vol10 Tesla Occupancy WM 2024,
  vol12 PyTorch 2016 / speculative decoding 2023, vol02 BERT venue line.

### Verification evidence (this round)

- vol01/07/10/13 PNG spot-checks (downscaled JPEGs + crops): corrected chips render and fit —
  vol01 §6 `GR00T / Isaac`, 2025 World Model card; vol10 timeline (`1960s–1990s Kalman /
  Particle Filter`, `1970s–80s MPC`, 2019 PlaNet, MuZero model-based fix, `2024–2025` band),
  JEPA family 2022/2023/2024/2025, mainline chips (`SimPLe·MBPO·MOPO·TIA`,
  `…FNO·FourCastNet·Earth-2…`, `UniPi·PI0·SuSIE…`), bilingual footer quote; vol07 SwAV (2020),
  iBOT (2022), COCO 33万, Google row without Florence; vol13 milestone `1957 感知机`,
  `参数规模 Parameter Scale`. No date-chip or label overflow observed.
- vol13 rebuilt again after the Microsoft-pill drop; full test suite re-run: 6/6.

### Remaining for k0

1. vol03 Mixtral year needs a schema decision (integer vs range) before it can show 2023–2024.
2. vol07 Microsoft-row `U-Former` vs `UniFormer` — needs an editorial decision on intent.
3. vol10 remains the weakest volume; per k5 §2.7 it deserves a full content revision pass
   (e.g. `Newton`, `Wayve WM`, `RDT-1B` rows were not individually re-verified in this round).
4. The vol01 §1 era range still prints `1950-1989` (era boundary, not the Backprop year);
   optional cosmetic alignment with the 1986 fix.
