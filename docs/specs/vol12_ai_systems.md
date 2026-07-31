# Vol.12 AI 系统 / AI Systems

- Source image: `assets/reference/volumes/12.AI系统.png`
- Declared volume number in header: **Vol.12** (matches filename number 12 — no discrepancy)
- Aspect: **landscape 3:2 (1536×1024 reference)** — not portrait; flag to k2.

## 1. Header

- Badge (top-left): `Modern AI Atlas` + chip `Vol.12`
- Title: AI Systems | AI 系统
- Subtitle (zh): 从芯片到集群：构建高效、可扩展、可推理的大模型系统
- Subtitle (en): From Chips to Clusters: Building Efficient, Scalable and Intelligent AI Systems
- Top-right quote block:
  > 卓越的模型需要卓越的系统来承载，AI 的进步不仅来自算法，更来自系统工程。
  > Great models need great systems. AI breakthroughs come from both algorithms and systems.
  (attribution: none printed)
- Top-right artwork: glowing server rack / AI chip cube with labeled callouts: **Compute · Memory · Storage · System Software · Network**.

## 2. Legend row

No edge-style legend. Section badges are dark navy squares (01–10). Accent colors: green for CUDA/hierarchy diagrams (02), blue for component cards (03), purple for inference (05), red/orange gauges for metrics (08), multicolor chips for trends (09).

## 3. Sections (in top-to-bottom order)

### 01 计算底座 (Compute Foundation)
Three sub-panels:
- **GPU 架构演进 GPU Architecture Evolution** (year list): Fermi 2010 · Kepler 2012 · Maxwell 2014 · Pascal 2016 · Volta 2017 · Turing 2018 · Ampere 2020 · Hopper 2022 · Blackwell 2024+
- **NVIDIA GPU 全栈 NVIDIA GPU Stack** (layered stack, top→bottom): Applications 应用层 · Libraries 库 (CUDA / cuDNN 等) · Runtime 运行时 (CUDA Runtime) · Driver 驱动 (GPU Driver) · Hardware 硬件 (GPU)
- **关键硬件组件 Key Hardware Components** (icon list): GPU 并行计算核心 · HBM 高带宽显存 · NVLink 高速互连 · PCIe 高速总线 · NVSwitch 交换芯片 · CPU 主机处理器 · System Memory 系统内存 · Storage 存储设备

### 02 并行计算与加速 (Parallel Computing & Acceleration)
Three sub-panels:
- **CUDA 并行计算平台 CUDA Parallel Computing Platform**: CUDA Core 计算核心 · Warp 线程束 (32线程) · Block 线程块 · Grid 网格 · Kernel 计算内核
- **线程层级模型 Thread Hierarchy Model** (green diagram): Grid → Block (2D/3D) → Warp (32 threads) → Thread
- **Tensor Core 张量核心**: Mixed Precision 支持 / 矩阵乘加加速 — FP64 · FP32 · TF32 · FP16 / BF16 · INT8 / INT4 (descending precision chips)

### 03 关键系统组件 (Key System Components)
Five cards:
- **FlashAttention 高效注意力计算**: Q K V → On-Chip SRAM diagram; bullets: IO-Aware · 减少 HBM 访问 · 加速 Attention · 节省显存
- **NCCL 高性能通信库**: ring diagram; 多 GPU 通信 · All-Reduce · All-Gather · Reduce-Scatter · Broadcast
- **DeepSpeed 高练加速框架** [sic — poster prints 高练, intended 高效训练加速框架]: ZeRO-1 · ZeRO-2 · ZeRO-3 · ZeRO-Infinity · Pipeline Parallel · Tensor Parallel; bullets: 3D 并行 · 显存优化 · 大模型训练
- **vLLM 高效推理引擎**: PagedAttention · Continuous Batching · KV Cache 管理 · 高吞吐低延迟 · OpenAI 兼容 API
- **Ray 分布式计算框架**: 分布式任务调度 · Actor 模型 · 弹性扩展 · 多语言支持

### 04 大模型训练优化 (Training Optimization Stack)
Grid of 12 mini-cards (4 × 3), verbatim:
- 并行策略 Parallelism: Data Parallel · Tensor Parallel · Pipeline Parallel
- 数据并行 Data Parallel: 多卡计算不同数据 · 线性加速
- 张量并行 Tensor Parallel: 拆分矩阵相乘 [sic, likely 拆分矩阵维度] · 加速大矩阵计算
- 流水线并行 Pipeline Parallel: 分阶段计算流水线 · 提高硬件利用率
- 显存优化 Memory Optimization: 优化器状态分配 [uncertain] · 梯度分片 · 零冗余分片 [uncertain]
- ZeRO 显存优化: 优化器状态分片 · 梯度分片 · 参数分片
- Offload 卸载优化: CPU Offload · NVMe Offload
- Activation Checkpoint 激活检查点: 减少激活显存 · 计算换显存
- 计算优化 Computation Optimization: FP16 / BF16 · 提升吞吐
- Mixed Precision Overlap Compression [sic — poster header, likely intended 通信重叠 Overlap Communication]: Overlap 计算与通信 · 压缩通信量 [uncertain] · 降低通信延迟
- 通信压缩 Gradient Compression: 减少通信数据量 · 降低带宽压力
- 拓扑感知通信 Topology-Aware: 感知网络拓扑 · 优化通信路径

### 05 大模型推理优化 (Inference Optimization Stack)
Four cards + center banner:
- Continuous Batching 连续批处理: 动态加入请求 · 提高吞吐率
- PagedAttention 分页注意力: KV Cache 分页管理 · 减少碎片
- KV Cache 管理 缓存优化: Cache 复用 · Cache 压缩 · Cache Offload
- Speculative Decoding 推测解码: Draft Model 生成 · 验证后输出 · 加速推理速度
- Center banner: **vLLM / SGLang / TensorRT-LLM** — 高吞吐 · 低延迟 · 高并发 · 低显存

### 06 分布式系统与调度 (Distributed Systems & Orchestration)
Five cards:
- Kubernetes 容器编排: 自动化部署 · 弹性伸缩 · 资源管理
- Ray 分布式计算: 任务调度 · Actor 模型 · 大规模并行
- Slurm 集群调度: 作业调度 · 资源分配 · 队列管理
- etcd 分布式存储: 配置管理 · 服务发现 · 一致性存储
- Prometheus 监控告警: 指标监控 · 告警通知 · 可视化

### 07 AI 系统技术栈全景图 (AI Systems Technology Stack Panorama)
Seven-column arrow flow (layer name + items):
- **应用层 Applications**: Chatbot · Copilot · 推荐系统 · 多模态应用 · 智能体 Agent
- **模型层 Models**: LLM · 多模态模型 · 扩散模型 · 语音模型 · 视觉模型
- **训练框架 Training Frameworks**: PyTorch · TensorFlow · JAX · Megatron-LM · DeepSpeed
- **系统软件 System Software**: CUDA · cuDNN · NCCL · FlashAttention · vLLM / SGLang
- **资源管理 Resource Management**: Kubernetes · Ray · Slurm · Docker · Prometheus
- **硬件层 Hardware**: NVIDIA GPU · CPU · HBM Memory · NVLink / NVSwitch · Storage / SSD
- **基础设施 Infrastructure**: 数据中心 Data Center · 网络 Network · 电力 Power · Cooling

### 08 AI 系统性能指标 (Key Performance Metrics)
Four gauge cards (top): TFLOPS / PFLOPS 计算性能 · GPU 利用率 GPU Utilization · 显存带宽 Memory Bandwidth · 网络带宽 Network Bandwidth
Four icon cards (bottom): 吞吐量 (Tokens/s) Throughput · 延迟 (ms/Token) Latency · 并发请求数 Concurrency · 成本 ($/1M Tokens) Cost Efficiency

### 09 发展趋势 (Trends & Future)
Six icon chips: 更大规模 Scaling Up · 更高效率 Efficiency First · 推理优先 Inference First · 软硬协同 HW-SW Co-design · 开放生态 Open Ecosystem · 可持续性 Sustainability

### 10 总结 (Summary) — dark navy panel, bottom-right
> AI 系统是大模型能力的放大器，优秀的系统让先进的模型真正落地。
> AI systems are the force multiplier of model capability. Great systems turn advanced models into real-world impact.

Right side: glowing layered-stack diagram with callouts (top→bottom): Applications · Models · System Software · Resource Management · Hardware · Infrastructure.

## 4. Bottom band(s)

Section 10 doubles as the bottom band. No NEXT-volume teaser.

## 5. Graph content (for knowledge graph nodes/edges)

Nodes (id / zh / en / year / kind):
- `gpu_fermi`…`gpu_blackwell` — GPU 架构节点: Fermi 2010, Kepler 2012, Maxwell 2014, Pascal 2016, Volta 2017, Turing 2018, Ampere 2020, Hopper 2022, Blackwell 2024 — kind: industry (hardware)
- `cuda` — CUDA 平台 / CUDA / 2007 / industry (platform)
- `cudnn` — cuDNN / cuDNN / 2014 / industry
- `tensor_core` — Tensor Core / Tensor Core / 2017 / industry (hardware feature)
- `hbm` — HBM 高带宽显存 / HBM / 2015 / industry (hardware)
- `nvlink` — NVLink / NVLink / 2016 / industry
- `nvswitch` — NVSwitch / NVSwitch / 2018 / industry
- `nccl` — NCCL / NCCL / 2015 / industry (library)
- `flashattention` — FlashAttention / FlashAttention / 2022 / paper
- `deepspeed` — DeepSpeed / DeepSpeed / 2020 / industry (framework)
- `zero` — ZeRO 优化 / ZeRO (1/2/3/Infinity) / 2020 / paper
- `megatron_lm` — Megatron-LM / Megatron-LM / 2019 / model (framework)
- `vllm` — vLLM / vLLM / 2023 / industry (engine)
- `pagedattention` — PagedAttention / PagedAttention / 2023 / paper
- `continuous_batching` — 连续批处理 / Continuous Batching / 2022 / concept
- `speculative_decoding` — 推测解码 / Speculative Decoding / 2023 / concept
- `kv_cache` — KV Cache 管理 / KV Cache Management / — / concept
- `sglang` — SGLang / SGLang / 2024 / industry (engine)
- `tensorrt_llm` — TensorRT-LLM / TensorRT-LLM / 2023 / industry (engine)
- `ray` — Ray / Ray / 2018 / industry (framework)
- `kubernetes` — Kubernetes / Kubernetes / 2014 / industry
- `slurm` — Slurm / Slurm / 2002 / industry
- `etcd` — etcd / etcd / 2013 / industry
- `prometheus` — Prometheus / Prometheus / 2012 / industry
- `pytorch` / `tensorflow` / `jax` — 训练框架 / 2016/2015/2018 / industry
- `mixed_precision` — 混合精度训练 / Mixed Precision (FP16/BF16/TF32) / 2017 / concept
- `activation_checkpoint` — 激活检查点 / Activation Checkpointing / 2016 / concept
- `cpu_nvme_offload` — 卸载优化 / CPU/NVMe Offload / 2021 / concept
- `gradient_compression` — 通信压缩 / Gradient Compression / 2018 / concept
- `topology_aware_comm` — 拓扑感知通信 / Topology-Aware Communication / — / concept

Edges:
- `gpu_fermi` → `gpu_kepler` → … → `gpu_blackwell` (inherits — generational line, NVIDIA same-vendor evolution)
- `gpu_volta` → `tensor_core` (composes — Tensor Cores introduced with Volta); `tensor_core` → `mixed_precision` (composes)
- `cuda` → `cudnn` (inherits — same vendor stack); `cuda` → `nccl` (composes)
- `flashattention` → `vllm` (composes — fused attention used in inference engines); `flashattention` → `sglang` (composes); `flashattention` → `tensorrt_llm` (composes)
- `pagedattention` → `vllm` (composes — core technique of vLLM); `continuous_batching` → `vllm` (composes); `kv_cache` → `pagedattention` (inherits conceptually)
- `zero` → `deepspeed` (composes — ZeRO implemented in DeepSpeed); `megatron_lm` → `deepspeed` (converges — parallel-training frameworks later merged efforts)
- `speculative_decoding` → `vllm` (converges — decoding optimization adopted by engines); `speculative_decoding` → `tensorrt_llm` (converges)
- `ray` → `kubernetes` (converges — orchestration layers); `slurm` → `kubernetes` (converges)
- `vllm` → `sglang` (converges); `vllm` → `tensorrt_llm` (converges)
- `nvlink` → `nvswitch` (inherits); `hbm` → `gpu_hopper` (composes)
- `activation_checkpoint` → `zero` (converges — memory-saving techniques); `gradient_compression` → `topology_aware_comm` (converges)

## 6. Style notes

- Same light series style as vols 9–11: off-white background, white cards, navy numbered badges (01–10).
- Header: black `AI Systems` + `| AI 系统`; bilingual subtitle; violet `Vol.12` chip; top-right 3D server illustration with callout labels.
- Section 02 thread-hierarchy diagram uses green blocks (Grid/Block/Warp/Thread) — keep green accent (#22A06B-ish).
- Section 03 DeepSpeed header contains a printed typo (`高练加速框架`) — k2 may normalize to 高效训练加速框架 or keep verbatim; flag in JSON.
- Section 08 gauges are semicircular dials in red/orange with needle icons; bottom metrics use flat line icons.
- Section 10 summary is a dark navy panel with cyan-glow 3D layered stack; callout labels in white.
- Landscape 1536×1024, three main bands: top (01/02/03), middle (04/05 + 08), bottom (06/09 + 07 + 10). Section 07 panorama is a wide 7-column arrow strip.
