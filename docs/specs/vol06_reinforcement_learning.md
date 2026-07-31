# Vol.06 强化学习 / Reinforcement Learning

- Source image: `assets/reference/volumes/6.强化学习.png`
- Declared volume number in header: **Vol.06** (matches filename number 6 — no discrepancy)
- Aspect: portrait 2:3 (1024×1536 reference)
- Theme note: light background like Vol.04/05 (see §6).

## 1. Header

- Left badge: dark navy `Modern AI Atlas` + pill `Vol.06`.
- Title (zh): **强化学习**
- Subtitle (en): **Reinforcement Learning** (indigo)
- Tagline (zh): **让智能体在与环境的交互中学习最优决策**
- Top-right quote box:
  > 强化学习关注如何学习到最优的行为策略，以最大化长期回报。
  > — Richard S. Sutton
- Far-right header illustration: white humanoid robot with floating RL concept icons.

## 2. Legend row

No top legend row. Bottom-right **图例 (Legend)** panel, 6 chips (icon + zh + en):

状态 (State) · 动作 (Action) · 奖励 (Reward) · 策略 (Policy) · 价值 (Value) · 环境 (Environment)

## 3. Sections (in top-to-bottom order)

### 3.1 强化学习发展时间线 (Timeline)

6 era columns above a navy axis; sketch icons below each era (maze, graph, DQN network labeled `DQN`, AlphaGo Go-board labeled `AlphaGo`, robot arm, gamepad, OpenAI swirl, robot head).

| Era | Years | Bullets |
|-----|-------|---------|
| 早期理论探索 | 1950s–1980s | 最优控制理论 / 动态规划基础 / 试错学习思想 |
| 基础算法形成 | 1990s–2000s | TD学习、Q学习等 / 蒙特卡洛方法 / 策略梯度方法 |
| 深度强化学习萌芽 | 2010–2013 | 深度学习结合RL / DQN (2013) 提出 / 解决高维状态问题 |
| 快速发展与突破 | 2014–2017 | 策略梯度方法进步 / A3C、DDPG、PPO / AlphaGo战胜人类 |
| 广泛应用与扩展 | 2018–2021 | 多智能体强化学习 / 离线强化学习 / 在机器人、游戏等领域落地 |
| 大模型时代的强化学习 | 2022–至今 | 大模型与RL结合 (RLHF等) / 通用智能体探索 / 更高效、稳定、安全的RL |

### 3.2 强化学习核心要素 (Core Elements)

Left vertical list (icon + bold term + zh desc):

- 智能体 (Agent) — 学习并与环境交互的决策者
- 环境 (Environment) — 智能体所处的外部世界
- 状态 (State, s) — 环境在某一时刻的描述
- 动作 (Action, a) — 智能体可执行的行为
- 奖励 (Reward, r) — 环境对智能体行为的反馈
- 策略 (Policy, π) — 从状态到动作的映射
- 价值函数 (Value Function) — 评估状态或状态-动作对的好坏
- 回报 (Return) — 从某时刻起累积的未来奖励
- 折扣因子 (Discount Factor, γ) — 平衡短期与长期回报的权重

### 3.3 强化学习交互流程 (RL Loop)

Center diagram: robot icon labeled 智能体 (Agent) above a globe labeled 环境 (Environment). Circular arrows:

- Down: 动作 Action aₜ
- Up: 状态 State sₜ and 奖励 Reward rₜ
- Feedback label: rₜ₊₁, sₜ₊₁

### 3.4 主要强化学习范式 (Main RL Paradigms)

4 groups, each with algorithm chips (colored pills):

- 值函数方法 (Value-Based) — 学习最优价值函数 Q*(s,a) 或 V*(s) — chips: Q-Learning, DQN, Double DQN
- 策略梯度方法 (Policy-Based) — 直接优化策略参数 θ — chips: REINFORCE, A2C / A3C, PPO
- 演员-评论家方法 (Actor-Critic) — 结合值函数与策略学习 — chips: DDPG, TD3, SAC
- 模型驱动方法 (Model-Based) — 学习环境模型，进行规划 — chips: Dyna-Q, MCTS, MuZero

### 3.5 强化学习问题类型 (Problem Settings)

Right vertical list (icon + title + desc):

- 单智能体 (Single-Agent RL) — 单个智能体与环境交互
- 多智能体 (Multi-Agent RL) — 多个智能体共同学习或竞争
- 离散动作空间 (Discrete Action) — 动作空间是离散集合
- 连续动作空间 (Continuous Action) — 动作空间是连续的实数空间
- 部分可观测 (POMDP) — 智能体无法直接观测完整状态
- 离线强化学习 (Offline RL) — 从已有数据中学习策略
- 安全强化学习 (Safe RL) — 在满足安全约束下学习最优策略

### 3.6 马尔可夫决策过程 (MDP)

Panel with formulas:

- 强化学习通常建模为MDP: ⟨S, A, P, R, γ⟩
- S: 状态空间　A: 动作空间
- P: 状态转移概率 P(s′|s,a)
- R: 奖励函数 R(s,a,s′)
- γ ∈ [0,1): 折扣因子
- 目标: 找到最优策略 π*，最大化期望回报 J(π) = E[ Σ_{t=0}^{∞} γᵗ rₜ ]

### 3.7 贝尔曼方程 (Bellman Equation)

- 状态价值函数: V^π(s) = E_π[r + γV^π(s′)|s]
- 动作价值函数: Q^π(s,a) = E_π[r + γQ^π(s′,a′)|s,a]
- 最优贝尔曼方程:
  - V*(s) = max_a Σ_{s′,r} P(s′,r|s,a)[r + γV*(s′)]
  - Q*(s,a) = Σ_{s′,r} P(s′,r|s,a)[r + γ max_{a′} Q*(s′,a′)]

### 3.8 探索与利用 (Exploration vs Exploitation)

- 探索: 尝试未知动作，获取更多信息
- 利用: 选择当前最优动作，获得最大回报
- Balance-scale diagram: 探索 (Exploration) ⚖ 利用 (Exploitation)
- 常见方法: ε-贪心策略、Softmax策略、UCB、熵正则化等

### 3.9 价值函数与策略的关系

Two boxes with arrows (policy-iteration loop):

- 价值函数指导策略改进: 评估 (Evaluation) 估计 V^π 或 Q^π → 改进 (Improvement) 更新策略 π ← π′
- 策略改进提升价值函数: 更好的策略 π′ 带来更高的期望回报

### 3.10 经典算法对比 (Algorithm Comparison)

Table, headers: 算法 | 类型 | 特点 | 优点 | 缺点

| 算法 | 类型 | 特点 | 优点 | 缺点 |
|------|------|------|------|------|
| Q-Learning | 值函数 | 基于表格的Q学习 | 简单、收敛性好 | 高维状态空间不适用 |
| DQN | 值函数 | 深度神经网络近似Q函数 | 能处理高维输入 | 样本效率低、易过估计 |
| REINFORCE | 策略梯度 | 纯策略梯度方法 | 实现简单 | 方差大、收敛慢 |
| PPO | 策略梯度 | 剪切策略梯度优化 | 稳定性好、易实现 | 需调参 |
| DDPG | 演员-评论家 | 确定性策略梯度 | 适用于连续动作 | 对超参敏感 |
| SAC | 演员-评论家 | 最大熵强化学习 | 样本效率高、稳定 | 计算复杂度较高 |

### 3.11 强化学习应用领域 (Applications)

9 icon tiles (zh + en): 游戏AI (Game AI) · 机器人控制 (Robotics) · 自动驾驶 (Self-Driving) · 推荐系统 (Recommender) · 金融交易 (Finance) · 资源分配 (Resource Allocation) · 医疗决策 (Medical Decision) · 工业控制 (Industrial Control) · 实验设计 (Experiment Design) · (`…` tile)

### 3.12 挑战与未来方向 (Challenges & Future Directions)

**主要挑战 (Challenges)** — 5 red icon items: 样本效率低 · 训练不稳定 · 探索难度大 · 安全性问题 · 可解释性不足

**未来方向 (Future Directions)** — 5 green icon items: 高效探索方法 · 离线强化学习 · 多模态与大模型融合 · 通用智能体 · 安全与对齐强化学习

### 3.13 重要数据集与基准 (Benchmarks & Environments)

Two groups:

- 仿真环境: Atari (游戏) · MuJoCo (机器人) · OpenAI Gym (经典控制) · PyBullet (机器人仿真)
- 真实场景数据集: D4RL (离线RL) · RoboSuite (机器人操作) · Meta-World (机器人操作) · RL Unplugged (教育)

### 3.14 强化学习学习路径 (Learning Roadmap)

5-step horizontal arrow flow, then a dashed return arrow labeled 持续迭代与复盘:

1. 基础知识 — 概率论、线性代数、最优化
2. 理解核心概念 — MDP、回报、价值函数等
3. 掌握经典算法 — Q-Learning、策略梯度等
4. 实践与调参 — 环境选择、超参优化
5. 深入研究前沿 — 最新算法、应用落地

## 4. Bottom band(s)

- Dark navy gradient banner (cityscape + robot at laptop), bilingual quote:
  > 强化学习让智能体在与环境的不断交互中学习最优行为，是迈向通用人工智能的重要基石。
  > Reinforcement Learning empowers agents to learn optimal behaviors through interaction, laying a crucial foundation towards Artificial General Intelligence.
- No NEXT Vol.XX teaser, no summary stats row.

## 5. Graph content (for knowledge graph nodes/edges)

### Nodes

| id | zh label | en label | year | kind |
|----|----------|----------|------|------|
| dynamic_programming | 动态规划 | Dynamic Programming (Bellman) | 1957 | concept |
| mdp | 马尔可夫决策过程 | Markov Decision Process | 1957 | concept |
| monte_carlo_rl | 蒙特卡洛方法 | Monte Carlo Methods | 1980 | concept |
| td_learning | 时序差分学习 | TD Learning | 1988 | milestone |
| q_learning | Q学习 | Q-Learning | 1992 | milestone |
| policy_gradient | 策略梯度 | Policy Gradient | 1992 | concept |
| reinforce | REINFORCE | REINFORCE | 1992 | paper |
| dyna_q | Dyna-Q | Dyna-Q | 1990 | model |
| mcts | 蒙特卡洛树搜索 | MCTS | 2006 | concept |
| dqn | 深度Q网络 | DQN | 2013 | milestone |
| double_dqn | Double DQN | Double DQN | 2015 | paper |
| ddpg | 确定性策略梯度 | DDPG | 2015 | paper |
| a3c | 异步演员-评论家 | A3C / A2C | 2016 | paper |
| trpo | 信赖域策略优化 | TRPO | 2015 | paper |
| ppo | 近端策略优化 | PPO | 2017 | milestone |
| td3 | 孪生延迟DDPG | TD3 | 2018 | paper |
| sac | 柔性演员-评论家 | SAC | 2018 | paper |
| alphago | AlphaGo | AlphaGo | 2016 | milestone |
| alphago_zero | AlphaGo Zero | AlphaGo Zero | 2017 | model |
| muzero | MuZero | MuZero | 2019 | model |
| offline_rl | 离线强化学习 | Offline RL | 2020 | concept |
| safe_rl | 安全强化学习 | Safe RL | 2021 | concept |
| multi_agent_rl | 多智能体强化学习 | Multi-Agent RL | 2018 | concept |
| rlhf | 人类反馈强化学习 | RLHF | 2022 | milestone |
| decision_transformer | 决策Transformer | Decision Transformer | 2021 | paper |

### Suggested edges

- `dynamic_programming → q_learning` — **inherits** (Bellman optimality lineage)
- `td_learning → q_learning` — **inherits** (Q-learning is an off-policy TD method)
- `q_learning → dqn` — **inherits** (DQN = Q-learning + deep function approximation)
- `dqn → double_dqn` — **inherits**
- `policy_gradient → reinforce` — **inherits**
- `reinforce → a3c` — **inherits** (actor-critic extension)
- `a3c → ppo` — **converges** (PPO descends from TRPO line; A3C is parallel — per AI圣经 anti-beautification rule, avoid drawing A3C → PPO as direct descent; PPO ← TRPO would be inherits)
- `trpo → ppo` — **inherits**
- `policy_gradient → ddpg → td3` — **inherits** (deterministic PG lineage)
- `ddpg → sac` — **converges** (SAC is maximum-entropy actor-critic, parallel to TD3)
- `td3 ↔ sac` — **converges**
- `dyna_q → muzero` — **converges** (both model-based, very different mechanisms)
- `mcts → alphago` — **composes** (AlphaGo = MCTS + deep value/policy networks)
- `dqn → alphago` — **converges** (same DeepMind deep-RL program, different mechanisms)
- `alphago → alphago_zero → muzero` — **inherits**
- `q_learning → offline_rl` — **converges** (offline RL reuses value-based ideas; not a descendant)
- `ppo → rlhf` — **composes** (AI圣经 note: RLHF is RL applied to LLM alignment; it also inherits the SFT paradigm — do NOT draw RLHF as "next generation of RL")
- `transformer → decision_transformer` — **composes** (cross-volume edge, optional)

## 6. Style notes

- Same light theme as Vol.04/05: off-white lavender background, dark navy titles, indigo accents, white cards.
- Math panels (3.6/3.7) render formulas in a serif/italic style inside light cards with a small left border accent.
- Paradigm chips (3.4) are colored pills: value-based = indigo outline, policy-based = green, actor-critic = orange, model-based = red/pink (approx — colors distinguish groups).
- Applications/challenges tiles follow the shared 12/5-icon grid language of Vol.04/05; challenges red, future green.
- Learning-roadmap steps are numbered rounded rectangles joined by arrows; the dashed 持续迭代与复盘 loop curves underneath.
- Bottom banner: dark navy gradient, city skyline, robot-at-laptop illustration; bilingual quote (zh white, en light blue).
