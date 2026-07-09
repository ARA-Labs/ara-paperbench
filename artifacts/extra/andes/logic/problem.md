# Problem Specification

## Observations

### O1: Token generation speed vastly exceeds user consumption speed
- **Statement**: Under real BurstGPT traces, vLLM's average token delivery speed (TDS) is 11.2 tokens/s, while human reading speed is 4.8 tokens/s and listening speed is 3.3 tokens/s. TDS exceeds any reasonable user consumption speed even under severe load surges.
- **Evidence**: Figure 4b; Section 2.2; Figure 2 demographic data
- **Implication**: Compute is wasted over-generating tokens that users cannot consume, creating slack that could be redirected to reduce TTFT for other users.

### O2: FCFS scheduling causes severe head-of-line blocking and TTFT inflation
- **Statement**: On a one-hour BurstGPT trace with vLLM serving Phi-3.5-MoE 16×3.8B on 8×A100 GPUs, average TTFT is 10.4 seconds, far exceeding the 1.3s web-page patience threshold recommended by Google.
- **Evidence**: Section 2.2; Figure 3; Figure 4a
- **Implication**: FCFS causes queuing delay during load surges; users abandon sessions before receiving any tokens.

### O3: GPU memory is underutilized during non-surge periods
- **Statement**: vLLM's GPU memory utilization fluctuates significantly and remains underutilized during normal load even while building long queues during surges (Figure 3).
- **Evidence**: Figure 3 (GPU Mem. Util. row)
- **Implication**: The system lacks a mechanism to pre-emptively use idle memory to serve waiting requests at token granularity.

### O4: Existing metrics miss mid-stream pauses and cascading delays
- **Statement**: TTFT captures only the first token; average/P90/P99 TPOT can miss long pauses in the middle of generation (Figure 5d) where both TTFT and last-token latency appear normal.
- **Evidence**: Section 3.1; Figure 5d
- **Implication**: A metric spanning the full token consumption timeline is needed.

### O5: Conversational AI drives >60% of LLM applications and is growing rapidly
- **Statement**: Conversational AI drives over 60% of LLM-backed applications; ChatGPT has 300 million weekly active users.
- **Evidence**: Section 1; citations [14], [13]
- **Implication**: Poor user experience at this scale has enormous business impact.

## Gaps

### G1: No QoE metric for text streaming services exists
- **Statement**: There is no formal, end-to-end QoE definition tailored to text streaming that captures TTFT, streaming pace, pauses, and cascading delays simultaneously.
- **Caused by**: O4
- **Existing attempts**: TTFT, average/P90/P99 TPOT, token generation throughput
- **Why they fail**: They measure subsets of the timeline or server-centric aggregates, missing middle pauses (Figure 5d) and cascading effects of early delays.

### G2: Existing schedulers cannot exploit the TDS–consumption-speed gap
- **Statement**: Existing LLM serving systems (vLLM, Sarathi-Serve, Orca) use FCFS and have no mechanism to preempt at token granularity based on user consumption state.
- **Caused by**: O1, O2, O3
- **Existing attempts**: Iteration-level batching (Orca), PagedAttention (vLLM), chunked-prefill (Sarathi-Serve)
- **Why they fail**: Optimized for throughput/latency, not user-facing QoE; FCFS cannot redistribute compute to requests most in need.

### G3: Preemption overhead is unaccounted for in scheduling decisions
- **Statement**: Naive token-level preemption (recomputation or KV-cache swapping) introduces hundreds of milliseconds to seconds of overhead. Without overhead awareness, excessive preemptions degrade aggregate QoE.
- **Caused by**: G2
- **Existing attempts**: None specifically address preemption overhead balancing for QoE.
- **Why they fail**: Scheduling decisions are made without estimating cumulative overhead impact on all ongoing requests.

## Key Insight
- **Insight**: Because servers generate tokens faster than users can consume them, there exists a "slack buffer" in each request's token delivery timeline. This slack can be exploited by a preemptive token-level scheduler to serve new or higher-priority requests without affecting the consuming user's perceived experience, as long as the pacer buffer does not run dry.
- **Derived from**: O1, O2, O3
- **Enables**: Token-level preemptive scheduling that maximizes QoE across all users, plus a client-side token pacer that absorbs generation bursts to maintain smooth delivery.

## Assumptions
- A1: Users consume tokens at a fixed reading/listening speed that is known or estimable per request.
- A2: Token generation latency is a predictable function of batch size (Pearson r = 0.997 between batch size and total context length).
- A3: Preemption overhead (recomputation or KV-cache swapping) is offline-profilable and sufficiently stable to be used for runtime estimation.
- A4: The server is the primary bottleneck; network conditions are not the dominant source of text streaming degradation.
- A5: Request output lengths are not known in advance; scheduling decisions are made online.
