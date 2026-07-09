# Related Work

## RW01: Kwon et al., 2023 (vLLM)
- **DOI**: SOSP 2023
- **Type**: baseline
- **Delta**:
  - What changed: Andes adds QoE-aware token-level preemptive scheduling on top of vLLM's continuous batching and PagedAttention.
  - Why: vLLM uses FCFS scheduling which causes head-of-line blocking and QoE degradation.
- **Claims affected**: C02, C03, C04, C07, C08
- **Adopted elements**: Continuous batching, PagedAttention KV cache management, preemption mechanisms (recomputation/swapping). Andes implemented as an alternative scheduler within vLLM v0.6.1.

## RW02: Agrawal et al., 2024 (Sarathi-Serve)
- **DOI**: OSDI 2024
- **Type**: baseline
- **Delta**:
  - What changed: Andes uses QoE-aware priority scheduling; Sarathi-Serve uses chunked prefill with FCFS.
  - Why: Sarathi-Serve optimizes throughput-latency tradeoff but not QoE; chunked prefill can interfere with prefill stage and increase TTFT.
- **Claims affected**: C02, C03, C08
- **Adopted elements**: Preemption overhead predictability insight; preemption mechanism characterization.

## RW03: Yu et al., 2022 (Orca)
- **DOI**: OSDI 2022
- **Type**: imports
- **Delta**:
  - What changed: Andes adds token-level preemptive scheduling; Orca introduced iteration-level batching.
  - Why: Iteration-level batching is a prerequisite for token-level control.
- **Claims affected**: C02
- **Adopted elements**: Iteration-level (continuous) batching paradigm.

## RW04: Patel et al., 2024 (Splitwise)
- **DOI**: ISCA 2024
- **Type**: baseline
- **Delta**:
  - What changed: Splitwise optimizes prefill/decode separation; Andes focuses on QoE-aware scheduling without changing the prefill/decode split.
  - Why: Splitwise uses FCFS and does not optimize for user-facing QoE.
- **Claims affected**: C08
- **Adopted elements**: None directly.

## RW05: Zhong et al., 2024 (DistServe)
- **DOI**: OSDI 2024
- **Type**: baseline
- **Delta**:
  - What changed: DistServe disaggregates prefill and decoding; Andes is orthogonal, focusing on scheduling within a serving instance.
  - Why: DistServe optimizes goodput but not user QoE.
- **Claims affected**: C08
- **Adopted elements**: None directly.

## RW06: Wu et al., 2024 (LoongServe)
- **DOI**: SOSP 2024
- **Type**: baseline
- **Delta**:
  - What changed: LoongServe targets long-context sequences with elastic sequence parallelism; Andes targets QoE-aware scheduling for text streaming.
  - Why: Different optimization objective; LoongServe uses FCFS.
- **Claims affected**: C08
- **Adopted elements**: None directly.

## RW07: Sheng et al., 2024 (VTC — Fairness in LLM Serving)
- **DOI**: OSDI 2024
- **Type**: bounds
- **Delta**:
  - What changed: VTC proposes non-preemptive fairness-based scheduling; Andes uses preemptive QoE-based scheduling.
  - Why: Fairness ≠ QoE; VTC does not account for user consumption speed or TTFT targets.
- **Claims affected**: C02
- **Adopted elements**: Insight that request scheduling beyond FCFS is valuable.

## RW08: Sun et al., 2024 (Llumnix)
- **DOI**: OSDI 2024
- **Type**: bounds
- **Delta**:
  - What changed: Llumnix proposes cluster-wide live migration for load balancing; Andes operates within a single instance.
  - Why: Complementary scope; Andes assumes cluster-level load balancing is handled externally.
- **Claims affected**: C08
- **Adopted elements**: Cluster-level concerns explicitly excluded from Andes scope.

## RW09: Liu et al., 2024 (CacheGen)
- **DOI**: SIGCOMM 2024
- **Type**: bounds
- **Delta**:
  - What changed: CacheGen streams KV cache entries incrementally; Andes focuses on token generation scheduling.
  - Why: Orthogonal optimization; CacheGen addresses KV reuse, Andes addresses scheduling policy.
- **Claims affected**: none directly
- **Adopted elements**: None.

## RW10: Wang et al., 2024 (BurstGPT)
- **DOI**: arXiv:2401.17644
- **Type**: imports
- **Delta**:
  - What changed: BurstGPT provides real-world LLM serving traces; Andes uses these traces for evaluation.
  - Why: Realistic workload characterization; validates that burst patterns (3/hour, 7 min avg, 2× rate) are realistic.
- **Claims affected**: C04, C07
- **Adopted elements**: One-hour trace slice for end-to-end evaluation; burst statistics for cyclic burst load pattern design.

## RW11: Kellerer et al., 2004 (Knapsack Problems)
- **DOI**: Springer Berlin Heidelberg, 2004
- **Type**: imports
- **Delta**:
  - What changed: Andes uses a variant of the 0/1 knapsack problem where item values depend on total items selected (batch size B); solves with greedy approximation.
  - Why: Standard knapsack is NP-Hard; the B-dependent variant is harder but still tractable via greedy.
- **Claims affected**: C02, C06
- **Adopted elements**: Knapsack problem formulation; weak NP-hardness result; pseudo-polynomial DP solution concept.

## RW12: Video Streaming QoE (Dobrian et al. 2011, Jiang et al. 2016, et al.)
- **DOI**: SIGCOMM 2011, NSDI 2016, NSDI 2017, NSDI 2021
- **Type**: imports
- **Delta**:
  - What changed: Andes adapts QoE concepts from video streaming (startup time, buffering) to text streaming (TTFT, token consumption pacing). Key differences: video is network-constrained; text is GPU compute/memory constrained. Video QoE factors (bitrate, buffering ratio) differ from text QoE factors.
  - Why: Text streaming has unique QoE challenges not addressed by video streaming literature.
- **Claims affected**: C01
- **Adopted elements**: QoE as an optimization objective; inspiration for startup delay and buffering concepts.
