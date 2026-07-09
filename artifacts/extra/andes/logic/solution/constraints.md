# Constraints

## Boundary Conditions

### BC1: Memory Constraint
- The sum of context lengths (KV cache entries) for all concurrently served requests must not exceed the GPU's KV cache capacity M: `Σ(l_i · x_i) ≤ M`.
- Batch size is also bounded by memory: B_max is the largest batch achievable before M is exceeded when filling with shortest-context requests.

### BC2: Compute Constraint
- Larger batch size B increases token generation latency. B_min is set as the largest B where all served requests still generate tokens faster than the most stringent user consumption speed r_user_min across all requests.
- If B > some threshold, TDS drops below r_user, causing QoE degradation for served requests.

### BC3: Online Setting — No Future Knowledge
- Andes operates in a fully online setting: request arrival times, input lengths, output lengths, and QoE parameters are not known in advance.
- QoE gain estimation uses a look-ahead window Δt; the best Δt depends on model and workload and requires pre-deployment tuning.

### BC4: QoE = 0 is Worst Case (No Tokens)
- QoE is undefined when S_whole = 0 (no tokens expected). When no tokens are delivered at all, S_delay = S_whole and QoE = 0.
- QoE cannot be computed before any tokens have been consumed.

### BC5: Token Pacer Buffer Depletion
- If the server fails to resume a preempted request before the client-side pacer buffer drains, the user experiences a pause and QoE degrades. The server must track pacer buffer state to avoid this.

### BC6: Cluster-Level Concerns Out of Scope
- Andes's scheduler manages requests within a single vLLM instance. Cluster-level load balancing and fault tolerance are assumed to be handled separately.

### BC7: Preemption Overhead Predictability Assumption
- The overhead-aware refiner assumes preemption overhead is predictable from offline profiles. If hardware or load conditions cause overhead to be highly variable, refiner estimates may be inaccurate.

## Known Limitations

### L1: Output Length Unknown
- Since output lengths are unknown a priori, QoE gain estimation (Q_serve,i(B)) can only project forward by Δt, introducing uncertainty. The choice of Δt affects performance and must be tuned per deployment.

### L2: Single-Instance Scope
- Andes does not address multi-instance load balancing or cross-machine scheduling. It assumes the system receiving requests is a single serving unit.

### L3: Greedy Solver Sub-Optimality
- The greedy solver is an approximation to the NP-Hard knapsack problem. While empirically it matches or exceeds the 3D DP solver due to real-time speed advantages, it does not provide optimality guarantees.

### L4: QoE Parameters Must Be Known at Request Time
- Target TTFT and user consumption speed must be specified at request submission. In real deployments, these may need to be inferred or set via API tiers.

### L5: Preemption Mechanism Availability
- Andes requires the underlying serving system to support continuous batching and at least one preemption mechanism (swapping or recomputation). Systems lacking these cannot integrate Andes's scheduler.

### L6: Context Length as Sole Memory Proxy
- The memory constraint uses context length as the proxy for KV cache size. Actual memory usage also includes model weights and intermediate tensors, which are treated as fixed overhead.
