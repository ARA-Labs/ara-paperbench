# System Architecture

## Overview

EXP-Bench consists of two interconnected systems: (1) the **Dataset Curation Pipeline** that produces the benchmark tasks, and (2) the **Evaluation Framework** that scores agent outputs. Both systems interact with external components (papers, repositories, LLM APIs, Docker environments).

---

## Component Graph

```
[Source Papers (PDF)]  ──────────────────────────┐
[GitHub Repositories] ──────────────────────────┤
                                                  ▼
                            ┌─────────────────────────────────────┐
                            │   Stage 1: Source Selection         │
                            │   - Citation count filter           │
                            │   - GitHub stars/forks filter       │
                            │   - Conference filter (NeurIPS,     │
                            │     ICLR 2024)                      │
                            └─────────────────┬───────────────────┘
                                              │
                            ┌─────────────────▼───────────────────┐
                            │   Stage 2.1: Multi-Modal Extraction  │
                            │   - OCR + multimodal LLM indexing   │
                            │   - 2-pass RAG querying             │
                            │   - Subsection-level semantic        │
                            │     classification                  │
                            │   - Full-paper re-querying          │
                            │   Output: (Q, M, D_gt, C_gt)       │
                            └─────────────────┬───────────────────┘
                                              │
                            ┌─────────────────▼───────────────────┐
                            │   Stage 2.2: Implementation          │
                            │   Extraction Agent                   │
                            │   - Tool-augmented (PDF, terminal,  │
                            │     web) codebase search            │
                            │   - Goal-conditioned repo search    │
                            │   - AST tracing → step-by-step      │
                            │     requirements (Δ_gt)             │
                            └─────────────────┬───────────────────┘
                                              │
                            ┌─────────────────▼───────────────────┐
                            │   Stage 3: Verification              │
                            │   - Containerized execution          │
                            │   - Output vs. expected comparison  │
                            │   - Human lightweight review         │
                            │   - File masking (git scripted)     │
                            └─────────────────┬───────────────────┘
                                              │
                            ┌─────────────────▼───────────────────┐
                            │         EXP-Bench Dataset            │
                            │   461 tasks × (Q, M, R_masked, G)  │
                            └─────────────────┬───────────────────┘
                                              │
               ┌──────────────────────────────▼──────────────────────────────┐
               │                      Agent Interface                         │
               │   Input: (Q, M, R_masked, credentials, 40-min timeout)      │
               │   Agent types: OpenHands, IterativeAgent                    │
               │   Hardware: Ubuntu 24.04 Docker + 4× NVIDIA A40            │
               └───┬──────────────────────────────────────────────┬──────────┘
                   │                                              │
       ┌───────────▼────────────┐                    ┌───────────▼──────────┐
       │   Agent Output         │                    │   Agent Logs         │
       │   - Exp. design text  │                    │   - Stderr/stdout    │
       │   - Git diff (Δ_agent)│                    │   - Action traces    │
       │   - Conclusion text   │                    └───────────┬──────────┘
       └───────────┬────────────┘                               │
                   │                                ┌───────────▼──────────┐
                   │                                │   Monitor (o3-mini)  │
                   │                                │   - Paper access?    │
                   │                                │   - Git ops?         │
                   │                                │   - Faked data?      │
                   │                                │   Output: M ∈ {0,1} │
                   │                                └───────────┬──────────┘
                   │                                            │ (if M=1)
       ┌───────────▼────────────────────────────────────────────▼──────────┐
       │                    LLM Judge (o3-mini)                             │
       │   - Design Eval: D_agent vs D_gt → score D ∈ [0,100]            │
       │   - Conclusion Eval: C_agent vs C_gt → correct/incorrect          │
       │   - Implementation Eval: Δ_agent vs Δ_gt → score I ∈ [0,100]   │
       │   (Chunked input handling for long diffs/logs)                    │
       └───────────┬────────────────────────────────────────────┬──────────┘
                   │                                            │
       ┌───────────▼────────────┐                  ┌───────────▼──────────┐
       │  Code Execution        │                  │   Score Aggregation  │
       │  Validator             │                  │   D, I, C, E, I·E,  │
       │  - Apply Δ_agent       │─────────────────▶│   All✓, All·E✓      │
       │  - Run in clean Docker │                  └──────────────────────┘
       │  - Output: E ∈ {0,1}  │
       └────────────────────────┘
```

---

## Component Descriptions

### Source Selection Filter
- **Purpose**: Identify high-quality, reproducible candidate papers
- **Inputs**: Conference proceedings (NeurIPS 2024, ICLR 2024), GitHub metadata
- **Outputs**: Filtered list of (paper, repository) pairs
- **Key design choices**: Citation count + GitHub stars/forks as proxy for impact and reproducibility; both criteria applied conjunctively

### Multi-Modal Extraction (Stage 2.1)
- **Purpose**: Extract structured research task components from paper text
- **Inputs**: PDF (with OCR + multimodal indexing), extracted tables/figures
- **Outputs**: Research question $Q$, high-level method $M$, expected outcome / conclusion ground truth $C_{gt}$, design variables $D_{gt}$
- **Key design choices**: Two-pass RAG to handle information scattered across sections; subsection-level prompting to reduce context noise; full-paper re-querying for setup details in appendices

### Implementation Extraction Agent (Stage 2.2)
- **Purpose**: Locate and validate the code implementation corresponding to the extracted research task
- **Inputs**: Complete codebase + extracted task $(Q, M, C_{gt})$; tool access (PDF reader, terminal, web browser)
- **Outputs**: List of required scripts, high-level usage instructions, step-by-step implementation requirements (from AST tracing), additional hyperparameters from config files/READMEs
- **Key design choices**: Goal-conditioned search reduces problem to finding implementation matching specified methodology; iterative refinement if execution fails

### Verification and Refinement (Stage 3)
- **Purpose**: Ensure tasks are executable and correct
- **Inputs**: Candidate task + implementation
- **Outputs**: Verified task with masked files added to dataset
- **Key design choices**: Containerized execution in clean environment; human review limited to lightweight consistency check (~20 min/paper after pipeline finalization)

### Monitor
- **Purpose**: Integrity check to detect shortcutting behaviors
- **Inputs**: Agent action logs
- **Outputs**: Binary pass/fail + explanation string
- **Key design choices**: LLM-based (o3-mini); checks three specific disallowed behaviors; automatic discard of failed traces before execution

### LLM Judge
- **Purpose**: Score design, implementation, and conclusion correctness
- **Inputs**: Agent outputs + ground truth; chunked for long inputs
- **Outputs**: D ∈ [0,100], I ∈ [0,100], C ∈ {correct, incorrect}
- **Key design choices**: Chunked processing for long diffs/logs; multi-step prompting separating monitor, design/conclusion, and implementation evaluations

### Code Execution Validator
- **Purpose**: Verify that agent code modifications are actually executable
- **Inputs**: Agent git diff + clean repository clone
- **Outputs**: E ∈ {0,1}
- **Key design choices**: Run in identical containerized environment to agent; provides ground truth for executability independent of LLM judge
