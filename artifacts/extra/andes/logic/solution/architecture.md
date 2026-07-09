# Architecture

## System Overview
Andes co-designs the LLM inference server and the application client. The server handles all scheduling and token generation; the client smooths token delivery to users.

```
[User] ←→ [Token Pacer (Client)] ←→ [Server]
                                       ├── Request Tracker
                                       ├── Token-Level Request Scheduler
                                       │     ├── Priority-Based Greedy Packer
                                       │     └── Overhead-Aware Refiner
                                       ├── Executor (LLM Inference Engine)
                                       └── KV Cache
```

## Component: Request Tracker
- **Purpose**: Maintains the complete control state for each active request (waiting or running).
- **Inputs**: Request arrival events (prompt, QoE parameters), token generation events from Executor, preemption/admit decisions from Scheduler.
- **Outputs**: Per-request state to the Scheduler (context length, accumulated QoE state, token timestamps, QoE parameters).
- **State per request**:
  - QoE parameters: target TTFT, user token consumption speed r_user
  - Prompt and partial response text
  - Timestamps of each generated token (T_delivery array)
  - Current context length l_i
  - Current resource usage
  - Current QoE value (recomputed incrementally)
- **Design choices**: Continuously updated on every token generation event; enables real-time QoE gain estimation for scheduler.
- **Code ref**: `src/execution/qoe.py` (QoE computation, RequestState class)

## Component: Token-Level Request Scheduler
- **Purpose**: At each scheduling quantum, decides which requests to admit/resume and which to preempt to maximize aggregate QoE.
- **Inputs**: Full request state from Request Tracker (context lengths, QoE gains, resource usage), token generation latency profile (function of batch size B), preemption overhead profiles.
- **Outputs**: Admit/resume set A', Preempt set P' for the Executor.
- **Subcomponents**:
  1. **Priority-Based Greedy Packer** (§4.2): Assigns priority π_i = (Q_serve,i(B) − Q_wait,i) / l_i, sorts descending, greedily packs requests respecting memory constraint M and batch size B. Run for all B ∈ [B_min, B_max]. O(N log N) per B value.
  2. **Overhead-Aware Refiner** (§4.3): Post-processes the greedy decision, iterates over (admit, preempt) pairs in priority order, estimates net QoE change (gain minus overhead-induced loss on all ongoing requests), prunes pairs with non-positive net QoE.
- **Selective Triggering**: Algorithm only invoked when GPU KV cache occupancy > 90% (memory-bound) or token generation latency exceeds the most stringent user consumption speed requirement (compute-bound).
- **Batch size search space**: B ∈ [B_min, B_max]; B_max = max feasible batch by context length; B_min = largest batch generating tokens faster than most stringent r_user.
- **Design choices**: Approximate greedy over exact DP because greedy is ~20× faster and achieves slightly better real-time QoE. Overhead-aware refiner is critical (ablation in §6.4).
- **Code ref**: `src/execution/scheduler.py`

## Component: Executor
- **Purpose**: Executes LLM inference using continuous batching; generates one token per iteration for each request in the current batch.
- **Inputs**: Admit/preempt decisions from Scheduler, KV cache state.
- **Outputs**: Generated tokens (pushed immediately to client Token Pacer via push-based streaming); updated KV cache.
- **Design choices**: Push-based streaming (not pull) because tokens for a single user are streamed only to that user, and the server needs to deallocate request state quickly to free memory.
- **Interactions**: Reads/writes KV Cache; sends tokens to Token Pacer via server-push streaming.

## Component: KV Cache
- **Purpose**: Stores key-value attention tensors for all tokens in the context of running requests.
- **Inputs**: Requests admitted by Scheduler; preemption events (trigger eviction or swap).
- **Outputs**: KV tensors to Executor during inference; swapped data to/from CPU RAM during preemption.
- **Memory constraint**: Total KV cache entries across all running requests ≤ M (GPU memory capacity).
- **Preemption modes**: Recomputation (drop cache, recompute on resumption) or Swapping (copy GPU↔CPU RAM, restore on resumption). Andes offline-profiles both and selects the faster.
- **Design choices**: Managed by the Scheduler via context length tracking; no modification needed to standard KV cache implementations.

## Component: Token Pacer (Client-Side)
- **Purpose**: Buffers tokens received from the server (potentially in bursts faster than r_user) and delivers them to the user precisely at the Ideal Consumption Timeline rate.
- **Inputs**: Tokens pushed from server; QoE parameters (target TTFT, r_user) set at request submission.
- **Outputs**: Token stream to user at rate r_user aligned to Ideal Consumption Timeline.
- **State**: Buffer of received-but-not-yet-delivered tokens; current pacer size B_pacer(t).
- **Server awareness**: Server monitors pacer buffer state (inferred from token timestamps and consumption speed) and resumes preempted requests before the buffer runs dry.
- **Design choices**: Client-side buffering allows server to preempt more aggressively without the user perceiving pauses. Absorbs generation fluctuations and preemption gaps.
- **Code ref**: `src/execution/token_pacer.py`

## Request Lifecycle
1. User submits request through application client; Token Pacer is initialized with QoE parameters.
2. Request enters server queue; Request Tracker initializes state.
3. Scheduler admits request when resources are available; Executor generates tokens.
4. Server pushes tokens immediately to Token Pacer (push-based streaming).
5. Token Pacer buffers excess tokens; delivers at r_user aligned to Ideal Consumption Timeline.
6. If Scheduler preempts request: KV cache is saved (swap) or dropped (recompute); Token Pacer continues delivering buffered tokens to user.
7. When Scheduler resumes request: KV cache is restored; Executor resumes token generation.
8. Request completes when all output tokens are generated and delivered.
