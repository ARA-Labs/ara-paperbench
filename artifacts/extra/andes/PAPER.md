---
title: "Andes: Defining and Enhancing Quality-of-Experience in LLM-Based Text Streaming Services"
authors: ["Jiachen Liu", "Jae-Won Chung", "Zhiyu Wu", "Fan Lai", "Myungjin Lee", "Mosharaf Chowdhury"]
year: 2024
venue: "arXiv"
doi: "arXiv:2404.16283v2"
ara_version: "1.0"
domain: "LLM serving, systems"
keywords: ["LLM serving", "Quality-of-Experience", "text streaming", "preemptive scheduling", "token-level scheduling", "KV cache", "conversational AI", "QoE", "knapsack scheduling", "token pacer"]
claims_summary:
  - "QoE (as defined by Andes) better captures user experience than TTFT/TPOT/throughput for text streaming services"
  - "Andes's priority-based QoE-aware token-level preemptive scheduler improves average QoE by up to 4.7× vs vLLM under burst load"
  - "Andes saves up to 61% GPU resources while maintaining the same high QoE (≥0.95)"
  - "97% of Andes-served requests achieve QoE ≥ 0.95 on real-world BurstGPT traces vs 75% for vLLM"
  - "The overhead-aware refiner is essential; without it, excessive preemptions degrade QoE"
abstract: "Large language models (LLMs) are now at the core of conversational AI services such as real-time translation and chatbots, which provide live user interaction by incrementally streaming text to the user. However, existing LLM serving systems fail to provide good user experience because their optimization metrics are not always aligned with user experience. In this paper, we first introduce and define the notion of Quality-of-Experience (QoE) for text streaming services by considering each user's end-to-end interaction timeline. Based on this, we propose Andes, a QoE-aware LLM serving system that enhances user experience by ensuring that users receive the first token promptly and subsequent tokens at a smooth, digestible pace, even during surge periods. This is enabled by Andes's preemptive request scheduler that dynamically prioritizes requests at the token granularity based on each request's expected QoE gain and GPU resource usage. Our evaluations demonstrate that, compared to state-of-the-art LLM serving systems, Andes improves the average QoE by up to 4.7× given the same GPU resource, or saves up to 61% GPU resources while maintaining the same high QoE."
---

# Andes: Defining and Enhancing Quality-of-Experience in LLM-Based Text Streaming Services

## Overview

Andes identifies that existing LLM serving systems optimize for server-centric metrics (throughput, average TTFT, P90/P99 TPOT) that are misaligned with actual user experience in text streaming services. The paper introduces a formal QoE definition that measures how closely a user's actual token consumption timeline follows their ideal consumption timeline, capturing cascading delays and pauses that TTFT/TPOT metrics miss.

Built on this QoE definition, Andes co-designs a server-side token-level preemptive request scheduler and a client-side token pacer. The scheduler formulates request selection as a variant of the knapsack problem (QoE gain per unit GPU memory) and solves it with an efficient O(N log N) greedy algorithm augmented by an overhead-aware refiner that prevents excessive preemption from degrading aggregate QoE. The token pacer buffers excess tokens on the client and smoothly delivers them at the user's reading/listening speed, absorbing generation bursts. Together these achieve up to 4.7× QoE improvement and up to 61% GPU savings compared to vLLM on real-world and synthetic bursty workloads.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight |
| [claims.md](logic/claims.md) | 8 falsifiable claims (C01–C08) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 6 verification plans (E01–E06) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: server (scheduler, tracker, executor, KV cache) + client (token pacer) |
| [solution/algorithm.md](logic/solution/algorithm.md) | Priority-based greedy packing (O(N log N)) + 3D DP baseline (O(MN²)) |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 5 convergence/scheduling tricks |
| [related_work.md](logic/related_work.md) | 12 typed dependencies |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/qoe.py](src/execution/qoe.py) | QoE metric computation (S_delay, S_whole, QoE) and Request Tracker state | C01 |
| [execution/scheduler.py](src/execution/scheduler.py) | Priority-based greedy packing + overhead-aware refiner | C02, C03, C05 |
| [execution/token_pacer.py](src/execution/token_pacer.py) | Client-side token pacer buffering and ideal-timeline delivery | C01, C02 |
| [configs/training.md](src/configs/training.md) | Serving/scheduling parameters with rationale | — |
| [configs/model.md](src/configs/model.md) | Model and hardware configurations | — |
| [environment.md](src/environment.md) | Hardware, deps, seeds | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG (nested YAML) |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 2 tables + 10 figures |
