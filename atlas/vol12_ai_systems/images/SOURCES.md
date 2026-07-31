# Vol.12 Card Image Sources

All 6 images below are embedded as base64 data URIs into the generated SVG at render time (see `generator/render/images.py`); the SVG stays self-contained and no external requests are made when exporting PDF/PNG.

| File | Card it illustrates | Source URL | What it depicts | License / attribution |
|---|---|---|---|---|
| nvidia_h100.png | 计算底座 → GPU 架构演进 | https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/NVIDIA_H100_%28%E6%9E%81%E5%AE%A2%E6%B9%BEGeekerwan%29_021.png/960px-NVIDIA_H100_%28%E6%9E%81%E5%AE%A2%E6%B9%BEGeekerwan%29_021.png | NVIDIA H100 (Hopper) GPU module being installed into a server chassis — the current flagship AI-training chip (photo by 极客湾 Geekerwan) | Wikimedia Commons — CC BY 3.0 |
| hbm_schematic.png | 计算底座 → 关键硬件组件 | https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/High_Bandwidth_Memory_schematic.svg/960px-High_Bandwidth_Memory_schematic.svg.png | HBM schematic: GPU + DRAM dice + HBM controller die on a silicon interposer with TSVs / μBumps, package substrate and graphics-card PCB | Wikimedia Commons — CC BY-SA 4.0 |
| cuda_thread_hierarchy.png | 并行计算与加速 → CUDA 并行计算平台 | https://upload.wikimedia.org/wikipedia/commons/1/15/Jerarquia_de_fils_d%27execuci%C3%B3_CUDA.png | CUDA thread-execution hierarchy diagram: grid → thread blocks → warps/threads (`intHelloGpu<<<2,5>>>`) | Wikimedia Commons — public domain |
| flashattention_diagram.png | 关键系统组件 → FlashAttention | https://ar5iv.labs.arxiv.org/html/2205.14135/assets/x1.png | FlashAttention (arXiv:2205.14135) figure: IO-aware tiling of Q/K/V blocks between HBM and on-chip SRAM | arXiv paper figure |
| zero_deepspeed.png | 关键系统组件 → DeepSpeed | https://ar5iv.labs.arxiv.org/html/1910.02054/assets/x1.png | ZeRO (Microsoft, arXiv:1910.02054) figure: memory consumption per device — parameters / gradients / optimizer states sharded across data-parallel ranks | arXiv paper figure |
| pagedattention_vllm.png | 关键系统组件 → vLLM | https://ar5iv.labs.arxiv.org/html/2309.06180/assets/x3.png | vLLM / PagedAttention (SOSP'23, arXiv:2309.06180) figure: KV-cache usage vs Orca baselines — vLLM reaches 96.3% cache utilization | arXiv paper figure |
