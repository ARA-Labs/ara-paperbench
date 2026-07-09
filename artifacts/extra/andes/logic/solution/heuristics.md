# Heuristics

## H01: Priority = QoE Gain per Memory Unit (l_i denominator)
- **Rationale**: Dividing QoE gain by context length l_i balances QoE improvement against GPU memory cost. A request with large l_i consuming much memory but small QoE gain should yield to requests with smaller l_i and larger QoE gain. This also means long-context requests are naturally preempted first, freeing enough memory to potentially admit multiple new short-context requests (more efficient than preempting multiple short ones).
- **Sensitivity**: high — the denominator l_i directly controls preemption decisions for memory-heavy requests.
- **Bounds**: π_i > 0 when the request would gain QoE from being served; π_i ≤ 0 when already ahead of ideal timeline (no gain from serving).
- **Code ref**: [src/execution/scheduler.py]
- **Source**: Section 4.2, Equation 6

## H02: Selective Triggering via KV Cache Watermark (90%) and Latency Threshold
- **Rationale**: Under normal load, running the knapsack solver every iteration is unnecessary overhead. Triggering only when the system is resource-constrained (memory occupancy > 90% or token latency exceeds the most stringent r_user) avoids wasted computation while ensuring the scheduler acts exactly when QoE is at risk.
- **Sensitivity**: medium — a lower watermark triggers more frequently (more overhead), a higher watermark risks missing early QoE degradation.
- **Bounds**: Memory watermark set at 90% of KV cache capacity. Latency threshold = 1/r_user_min for the most stringent request.
- **Code ref**: [src/execution/scheduler.py]
- **Source**: Section 4.2, "Selective Triggering"

## H03: Batch Size Search Space Pruning [B_min, B_max]
- **Rationale**: Exploring all B ∈ [1, N] is unnecessary. B_max is set by packing the shortest-context requests until memory M is reached (maximum feasible batch). B_min is set as the largest B that still generates tokens faster than the most stringent user consumption speed — below B_min, TDS > r_user for all requests and serving fewer requests only wastes potential concurrency without QoE benefit.
- **Sensitivity**: medium — incorrect B_min/B_max bounds can exclude the optimal batch size.
- **Bounds**: 1 ≤ B_min ≤ B_max ≤ N; B_max determined by memory capacity; B_min determined by token generation latency profile.
- **Code ref**: [src/execution/scheduler.py]
- **Source**: Section 4.2, "Batch Size Search Space Pruning"

## H04: Overhead-Aware Refiner — Stop When Net QoE Change is Non-Positive
- **Rationale**: The greedy scheduler's admission list is sorted by priority. Once a lower-priority (admit, preempt) pair produces non-positive net QoE (gain < overhead cost), all subsequent pairs in priority order will also fail (since they have lower gain). This allows early termination, making the refiner efficient.
- **Sensitivity**: high — without this stopping criterion, the refiner could admit preemptions that net-degrade QoE.
- **Bounds**: Net QoE threshold = 0. If QoE_gain(r_admit) − QoE_loss_all_ongoing(overhead) ≤ 0, stop.
- **Code ref**: [src/execution/scheduler.py]
- **Source**: Section 4.3, "Balancing QoE Gain and Overhead"

## H05: Token Pacer — Server-Side Buffer Awareness for Preemption Timing
- **Rationale**: The server pushes tokens as they are generated. When a request has accumulated sufficient tokens in the pacer buffer (actual delivery timeline well above ideal), the server can afford to preempt it. The server tracks pacer state via token delivery timestamps and consumption speed, resuming preempted requests before the buffer depletes to zero.
- **Sensitivity**: high — if the server resumes too late, the user experiences a pause (QoE degradation). Too early, and the preemption benefit is lost.
- **Bounds**: Resume request when estimated pacer buffer < safety margin (enough tokens for overhead duration at r_user). Safety margin = preemption/resumption latency × r_user.
- **Code ref**: [src/execution/token_pacer.py]
- **Source**: Section 5, Figure 10
