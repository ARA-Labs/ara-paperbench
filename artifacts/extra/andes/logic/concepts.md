# Concepts

## Quality-of-Experience (QoE)
- **Notation**: `QoE = 1 - S_delay / S_whole`
- **Definition**: A scalar in [0, 1] measuring how closely a user's Actual Consumption Timeline follows their Ideal Consumption Timeline. `S_delay = Σᵢ(T_actual_i − T_ideal_i)` for all consumed tokens i=1..n, summing the area between the Actual and Ideal consumption timelines. `S_whole` covers `S_delay` plus the area below the Actual Consumption Timeline, always ≥ S_delay. QoE = 1 denotes perfect experience (no delays); QoE = 0 denotes worst experience (no tokens delivered).
- **Boundary conditions**: Defined only when at least one token has been delivered. QoE can be computed for queued, running, or finished requests. Delivering tokens earlier than ideal does NOT improve QoE (capped at the user's consumption speed). Delivers only worsen QoE monotonically.
- **Related concepts**: Ideal Consumption Timeline, Actual Consumption Timeline, Token Delivery Delay, Time-to-First-Token (TTFT), Token Delivery Speed (TDS)

## Ideal Consumption Timeline (T_ideal)
- **Notation**: `T_ideal_i = T_target_TTFT + (i-1) / r_user`
- **Definition**: The timeline along which a user expects to receive tokens: the i-th token should arrive at the TTFT target plus `(i-1)` token intervals at the user's consumption speed `r_user` (tokens/s). The slope of the line equals the user's reading or listening speed.
- **Boundary conditions**: Fixed per request once QoE parameters (target TTFT, consumption speed) are set at request submission. Does not change based on server state.
- **Related concepts**: QoE, Actual Consumption Timeline, Token Delivery Speed (TDS), Token Pacer

## Actual Consumption Timeline (T_actual)
- **Notation**: `T_actual_i`
- **Definition**: The timestamp at which the user actually consumes the i-th token. Equals `max(T_delivery_i, T_actual_{i-1} + 1/r_user)`, where `T_delivery_i` is when the token arrives. When delivery is ahead of schedule, T_actual follows the ideal; when delivery falls behind, T_actual lags, creating cascading delays on all subsequent tokens.
- **Boundary conditions**: Always ≥ T_ideal_i when any delay has occurred (cascading). Equals T_ideal when delivery is ahead of schedule.
- **Related concepts**: Ideal Consumption Timeline, QoE, Token Delivery Delay

## Token Delivery Speed (TDS)
- **Notation**: `TDS` (tokens/s)
- **Definition**: The rate at which the server generates and pushes tokens to the client for a given request. Determined by the token generation latency, which is a function of batch size B. Generating TDS > r_user does not improve QoE but creates slack that can be exploited for preemption.
- **Boundary conditions**: TDS > r_user is wasteful for QoE of that request but enables preemption slack. TDS < r_user degrades QoE. Modeled as a function of batch size B only (Pearson r = 0.997 between batch size and total context length).
- **Related concepts**: Ideal Consumption Timeline, QoE, Token Pacer, Batch Size B

## Priority Score (π_i)
- **Notation**: `π_i = (Q_serve,i(B) − Q_wait,i) / l_i`
- **Definition**: The scheduling priority of request i, defined as its expected QoE gain if served (at batch size B) divided by its context length l_i. Q_serve,i(B) is the estimated QoE of request i if served in a batch of size B for the next Δt seconds; Q_wait,i is the estimated QoE if not served for Δt seconds. Dividing by l_i penalizes memory-heavy requests, implementing a QoE-per-memory-unit heuristic.
- **Boundary conditions**: Priority is dynamic: increases as a request waits (growing QoE gain from waiting), decreases as context length grows (auto-deprioritization after sufficient tokens are buffered). Prevents starvation.
- **Related concepts**: QoE, Greedy Knapsack Scheduling, Overhead-Aware Refiner, Batch Size B

## Token Pacer
- **Notation**: Client-side buffer of size `B_pacer(t)` tokens
- **Definition**: A client-side component that receives tokens from the server via push-based streaming (potentially faster than consumption speed), buffers them, and delivers them to the user precisely at the user's Ideal Consumption Timeline rate r_user. Absorbs server-side generation bursts and pauses (during preemption) to provide smooth delivery.
- **Boundary conditions**: If the pacer buffer drains to zero (no tokens buffered and server not generating), the user experiences a pause and QoE degrades. The server monitors pacer state and resumes preempted requests before the buffer runs out.
- **Related concepts**: Ideal Consumption Timeline, Token Delivery Speed (TDS), QoE, Push-Based Streaming

## Cyclic Burst Load Pattern
- **Notation**: Characterized by intensity r (ratio of burst to average request rate) and duration d (fraction of time in burst phase)
- **Definition**: A synthetic request arrival pattern alternating between burst and non-burst phases following a Poisson process. Default parameters: intensity = 2×, duration = 35% of cycle. The average request rate equals system throughput under no burstiness to prevent indefinite queue growth. Models real BurstGPT behavior (≈3 bursts/hour, ≈7 min avg duration, ≈2× higher rate during bursts).
- **Boundary conditions**: Valid when intensity > 1 and 0 < duration < 1. At intensity = 1 there is no burst. At duration = 1 the system is permanently overloaded.
- **Related concepts**: BurstGPT, Head-of-Line Blocking, QoE

## KV Cache Context Length (l_i)
- **Notation**: `l_i` (tokens)
- **Definition**: The total number of tokens (prompt + generated so far) occupying KV cache entries in GPU memory for request i. Each token in a request's context consumes one KV cache entry. Acts as the "weight" in the knapsack formulation; the memory constraint requires Σ(l_i · x_i) ≤ M.
- **Boundary conditions**: Grows over time as more tokens are generated, automatically increasing the memory cost and decreasing priority. GPU memory M bounds total feasible context.
- **Related concepts**: Priority Score, Greedy Knapsack Scheduling, Batch Size B, Memory Constraint M

## Overhead-Aware Refiner
- **Notation**: Refines scheduling decision (A, P) → (A', P') where A' ⊆ A, P' ⊆ P
- **Definition**: A post-processing step that iterates over the admission list A (sorted by priority descending) from the greedy scheduler and checks whether admitting request r_admit by preempting request r_preempt produces net positive QoE change. For each candidate admission, it estimates: QoE gain of admission − QoE loss of overhead on all ongoing requests. Stops when net QoE change becomes non-positive.
- **Boundary conditions**: Operates after the greedy scheduler produces an initial decision. Preemption overhead (recomputation or KV-swap latency) is estimated from offline profiles. Becomes critical at high burst durations where many preemptions would otherwise be triggered.
- **Related concepts**: Priority Score, Token-Level Request Scheduler, Preemption Mechanisms

## Preemption Mechanisms
- **Notation**: Recomputation (drop KV cache, recompute on resumption) or Swapping (move KV cache GPU↔CPU)
- **Definition**: Two mechanisms for pausing a running request. Recomputation: drop the KV cache on preemption (zero preemption cost), recompute from scratch on resumption (overhead ≈ one prefill). Swapping: copy KV cache to CPU RAM on preemption and back on resumption (overhead proportional to KV cache size). Andes offline-profiles both and selects the faster per context length.
- **Boundary conditions**: Overhead ranges from hundreds of milliseconds to seconds. Both mechanisms interrupt the entire token generation pipeline for all requests in the current batch. Overhead is predictable and stable enough for runtime estimation.
- **Related concepts**: Overhead-Aware Refiner, KV Cache Context Length, Token-Level Request Scheduler
