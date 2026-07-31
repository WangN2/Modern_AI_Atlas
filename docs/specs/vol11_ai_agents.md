# Vol.11 智能体 / AI Agents

- Source image: `assets/reference/volumes/11.AI Agents.png`
- Declared volume number in header: **Vol.11** (matches filename number 11 — no discrepancy)
- Aspect: **landscape 3:2 (1536×1024 reference)** — not portrait; flag to k2.

## 1. Header

- Badge (top-left): `Modern AI Atlas` + chip `Vol.11`
- Title: AI Agents 智能体
- Subtitle (zh): 自主感知 · 规划决策 · 工具使用 · 协同合作
- Subtitle (en): Perceive, Plan, Act, and Collaborate in the Real World
- Top-right quote block (with large decorative `“`):
  > AI Agent 是迈向通用人工智能（AGI）的关键一步，它让 AI 从“回答问题”走向“解决问题”。— Yann LeCun
- Top-right artwork: white/blue humanoid robot presenting floating UI panels.

## 2. Legend row

No edge-style legend. Section badges are dark navy squares (01–11). Accent color language: blue/purple = capability & architecture, orange = 行动/反思 (in section 01), red = challenges (10), teal = future trends (11).

## 3. Sections (in top-to-bottom order)

### 01 AI Agent 核心能力 (Core Capabilities)
Circular hub diagram around a central robot icon labeled **AI Agent**, six satellite cards:
- **感知 Perception** — 理解环境与输入 · 多模态感知如状态理解 [reads "多模态感知如 / 状态理解"; likely intended 多模态感知与状态理解 — flag]
- **规划 Planning** — 分解目标 · 选择策略
- **记忆 Memory** — 短期/长期记忆 · 知识检索 · 经验挖掘
- **工具使用 Tool Use** — 调用外部工具 · API / 插件 / 代码 · 扩展能力
- **行动 Action** (orange) — 与环境交互 · 完成任务
- **反思 Reflection** (orange) — 自我评估 · 总结经验 · 持续改进

### 02 智能体工作流程 (Agent Workflow)
Top flow chips: 目标 Goal → 感知 Perceive → 记忆 Retrieve → 规划 Plan → 行动 Act → 观察 Observe → 反思 Reflect (cyclic arrows back).
Middle **记忆 (Memory)** sub-panel with three cards:
- 短期记忆 Short-term — 临时上下文 · 最近交互信息
- 长期记忆 Long-term — 知识库 · 历史经验
- 结构化记忆 Structured — 规则 / 模板 · 知识图谱
Bottom band: **工具 (Tools) / 环境 (Environment)** — 与外部世界持续交互，获取反馈.

### 03 工具使用 (Tool Use)
Seven icon chips: 搜索 Search · 计算器 Calculator · 代码解释器 Code Interpreter · API 调用 API Call · 数据库 Database · 文件读写 File I/O · 更多工具 More…

### 04 MCP (Model Context Protocol) 模型上下文协议
Subtitle: 连接模型与外部世界的标准协议.
Flow: **Host (Agent / App) → MCP Client → MCP Protocol → MCP Server** → fan-out to: 文件系统 · 数据库 · API 服务 · 向量库 · 更多…

### 05 记忆系统 (Memory)
Three cards:
- **短期记忆 Short-term Memory**: 对话上下文 · 最近的交互信息 · 临时记忆
- **长期记忆 Long-term Memory**: 用户画像 · 知识库 · 历史经验
- **结构化记忆 Structured Memory**: 知识图谱 · 向量数据库 · 规则与事实

### 06 规划与推理 (Planning & Reasoning)
Six cards (2 rows × 3):
- 任务分解 Task Decomposition — 将复杂任务分解为可执行的子任务
- 推理链 Chain of Thought — 逐步推理，得出中间结论
- 策略规划 Strategy Planning — 生成执行方案与行动顺序
- 决策 Decision Making — 选择最优行动，平衡风险与收益
- 自我反思 Self-Reflection — 评估结果，改进策略
- 自我修正 Self-Correction — 发现错误，修正并重试

### 07 多智能体协作 (Multi-Agent Collaboration)
Subtitle: 多个智能体协同完成复杂任务. Five arrow-linked mode cards:
协作式 Collaboration（共同完成任务）→ 辩论式 Debate（通过辩论达成最优决策）→ 分工式 Division of Labor（专业分工协作）→ 竞争式 Competition（相互竞争提升表现）→ 管理者-工人 Manager-Worker（分层管理执行）

### 08 代表性框架 / 平台 (Frameworks / Platforms)
Eight logo chips: **AutoGPT · BabyAGI · LangChain · LlamaIndex · OpenAI Assistants API · MetaGPT · CAMEL · AG2**

### 09 AI Agent 全景架构 (AI Agent Architecture Overview)
Five-column end-to-end diagram:
- **输入 (Input)**: 文本 Text · 图像 Images · 语音 Speech · 视频 Video · 传感器 Sensors · 结构化数据 Structured Data
- **感知 (Perception)**: 多模态理解 Multimodal Understanding · 状态估计 State Estimation · 意图识别 Intent Recognition · 信息抽取 Information Extraction
- **智能体大脑 (Agent Brain)** (highlighted blue panel):
  - 记忆系统 (Memory): 短期记忆 Short-term Memory · 长期记忆 Long-term Memory · 知识库 Knowledge Base
  - 规划与推理 (Planning & Reasoning): 任务分解 Task Decomposition · 推理链 Chain of Thought · 策略规划 Strategy Planning
  - 决策与行动 (Decision & Action): 决策选择 Decision Making · 行动生成 Action Generation · 执行反馈 Execution Feedback
- **工具与环境 (Tools & Environment)**: 内置工具 Built-in Tools（搜索 Search · 计算 Calculator · 代码 Code · 数据库 Database）· 外部工具 External Tools（API / 服务 · 插件 / 组件 · 物理设备）
- **输出 (Output)**: 文本回复 Text Response · 执行结果 Execution Result · 图像生成 Image Generation · 行动控制 Action Control · 报告 / 可视化 Report / Visualization

### 10 当前挑战 (Challenges) — red accent
Ten items (2 rows × 5):
- 可靠性不足 Reliability — 幻觉与错误
- 可解释性不足 Interpretability — 决策过程难理解
- 记忆局限 Memory Limitation — 长期记忆困难
- 任务泛化不足 Generalization — 跨领域泛化难
- 安全与对齐 Safety & Alignment — 价值观对齐难
- 工具依赖性 Tool Dependency — 工具质量影响大
- 环境不确定性 Env Uncertainty — 现实环境复杂
- 多轮交互难 Multi-turn Difficulty — 上下文丢失
- 成本与延迟 Cost & Latency — 资源消耗高
- 协作冲突 Collaboration Conflict — 多智能体冲突

### 11 未来趋势 (Future Trends) — teal accent
Nine icon chips: 更强的推理能力 Stronger Reasoning · 更长的上下文记忆 Longer Context Memory · 更自主的任务执行 Autonomous Execution · 更安全可靠的智能体 Safe & Reliable Agents · 具身智能体 Embodied Agents · 端到端学习 End-to-End Learning · 多模态理解与生成 Multimodal Understanding · 人机协作增强 Human-AI Collaboration · 通向 AGI 的关键路径 Key Path to AGI

## 4. Bottom band(s)

Bottom-right dark navy **总结 (Summary)** card (with glowing "AI" cube artwork):
> AI Agents 将大模型的智能与外部世界连接起来，通过感知、记忆、规划、工具使用、行动和反思，实现从“回答问题”到“解决问题”的跨越。未来，AI Agents 将是 AGI 的重要基石。

No NEXT-volume teaser. Sections 10/11 occupy the bottom-left; the summary card is bottom-right.

## 5. Graph content (for knowledge graph nodes/edges)

This poster is more concept/architecture oriented than model-history oriented; nodes are mostly concepts/frameworks.

Nodes (id / zh / en / year / kind):
- `autogpt` — AutoGPT / AutoGPT / 2023 / model (framework)
- `babyagi` — BabyAGI / BabyAGI / 2023 / model (framework)
- `langchain` — LangChain / LangChain / 2022 / industry (framework)
- `llamaindex` — LlamaIndex / LlamaIndex / 2022 / industry (framework)
- `openai_assistants_api` — OpenAI Assistants API / Assistants API / 2023 / industry
- `metagpt` — MetaGPT / MetaGPT / 2023 / model (framework)
- `camel` — CAMEL / CAMEL / 2023 / model (framework)
- `ag2` — AG2 / AG2 (AutoGen 系列) / 2024 / model (framework)
- `mcp` — 模型上下文协议 / Model Context Protocol / 2024 / concept (protocol)
- `react_loop` — 感知-规划-行动-反思循环 / Perceive–Plan–Act–Reflect Loop / 2023 / concept
- `chain_of_thought` — 推理链 / Chain of Thought / 2022 / paper (concept on poster)
- `task_decomposition` — 任务分解 / Task Decomposition / — / concept
- `self_reflection` — 自我反思与修正 / Self-Reflection & Self-Correction / — / concept
- `memory_systems` — 记忆系统 / Memory Systems (short/long/structured) / — / concept
- `tool_use` — 工具使用 / Tool Use / — / concept
- `multi_agent_collaboration` — 多智能体协作 / Multi-Agent Collaboration / — / concept
- `manager_worker` — 管理者-工人模式 / Manager-Worker Pattern / — / concept
- `embodied_agents` — 具身智能体 / Embodied Agents / 2025 / concept
- `agent_to_agi` — 通向 AGI 的关键路径 / Key Path to AGI / — / concept

Edges:
- `langchain` → `autogpt` (converges — same era agent scaffolding; independent projects)
- `autogpt` → `babyagi` (converges — poster groups as peers)
- `camel` → `metagpt` (converges — multi-agent role-play frameworks)
- `metagpt` → `manager_worker` (composes — MetaGPT implements role division); `multi_agent_collaboration` → `manager_worker` (composes)
- `chain_of_thought` → `task_decomposition` (converges); `chain_of_thought` → `self_reflection` (converges)
- `mcp` → `tool_use` (composes — protocol standardizes tool/environment connection)
- `react_loop` → `memory_systems`, `react_loop` → `tool_use` (composes — loop integrates capabilities)
- `autogpt` → `ag2` (converges); `camel` → `ag2` (converges — AG2/AutoGen multi-agent lineage is independent)
- `embodied_agents` → `agent_to_agi` (converges); `multi_agent_collaboration` → `agent_to_agi` (converges)
- `memory_systems` → `react_loop` (composes)

(k2 note: years for concept nodes are not printed on the poster; the ones above are inferred — mark `year` as null or omit for pure concepts if schema allows.)

## 6. Style notes

- Same light series style: off-white background, white cards, light-blue borders, navy numbered badges (01–11).
- Header uses large black `AI Agents` + zh 智能体; blue en subtitle line; violet `Vol.11` chip.
- Section 01 uses a circular radial layout with a 3D robot mascot at the center; satellite cards have colored icon chips (blue/purple for 感知/规划/记忆, orange for 行动/反思, violet for 工具使用).
- Section 04 MCP flow uses pill-shaped nodes with arrows; right fan-out list has small file/db icons.
- Section 09 "Agent Brain" is a visually emphasized inner panel (light blue fill) nested inside the architecture diagram — k2 should reproduce this nested-panel hierarchy.
- Challenges (10) red icons; Future trends (11) teal icons.
- Bottom-right summary card is dark navy with cyan glow artwork; body text white zh.
- Landscape 1536×1024, roughly: top band (header + 01/02/03), second band (04 + 05/06/07), third band (08/09 + start of 10), bottom band (10 cont. / 11 / summary).
