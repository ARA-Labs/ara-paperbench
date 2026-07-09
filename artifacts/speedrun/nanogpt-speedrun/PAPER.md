---
title: "An LLM Agent for Speedrunning NanoGPT Training"
authors:
  - Banghua Zhu
  - Zhaoning Wang
  - Jiantao Jiao
  - Michael I. Jordan
venue: "Facebook Research / UC Berkeley, 2025"
ara_version: "1.1"
source_repo: "https://github.com/facebookresearch/llm-speedrunner"
claims_summary:
  - "C01: Human-authored optimizations compress GPT-2 training from 49 min to 3 min (16x) through 21 incremental records"
  - "C02: No frontier LLM agent can reproduce even a single record-to-record optimization, even with pseudocode hints"
  - "C03: The Muon optimizer is the single largest contributor to speedup (49→23 min, 53% reduction)"
  - "C04: FlexAttention with document-aware masking enables 64K context at minimal overhead"
  - "C05: Architectural innovations (ReLU², skip connections, GQA) compound multiplicatively with optimizer gains"
  - "C06: The agent failure mode is implementation, not ideation — agents know what to do but cannot code it"
  - "C07: Tree-structured search (BoN) outperforms linear search for agent-driven optimization"
abstract: >
  We present a benchmark and analysis of LLM agent capability for speedrunning
  NanoGPT training on 8×H100 GPUs. The NanoGPT Speedrun comprises 21
  human-authored records, each introducing a specific optimization that
  incrementally reduces GPT-2 (124M) training time from 49.5 minutes to 3.1
  minutes while maintaining val_loss ≤ 3.28 on FineWeb-Edu 10B tokens. We
  develop a tree-structured experimentation framework where LLM agents (Ideator
  + Coder + Analyst) attempt to reproduce each optimization given hints at four
  abstraction levels. Our finding: no frontier model (DeepSeek R1, o3-mini,
  Gemini 2.5, Claude 3.7 Sonnet) succeeds even with pseudocode-level hints,
  revealing a fundamental gap between LLM ideation and systems-level implementation.

layers:
  logic: "logic/"
  src: "src/"
  trace: "trace/"
  evidence: "evidence/"
---

# NanoGPT Speedrun — ARA Manifest

## Layer Index

| Layer | Path | Description |
|-------|------|-------------|
| Cognitive | `logic/` | Problem framing, claims, concepts, solution architecture |
| Physical | `src/` | Key optimization code, agent framework code, configs, environment |
| Trace | `trace/` | 21-record exploration tree capturing full optimization trajectory |
| Evidence | `evidence/` | Speedrun progression data, agent evaluation results, figures |

## Detailed File Index

### Cognitive Layer (`logic/`)

| File | Description |
|------|-------------|
| `logic/problem.md` | Observations, gaps, key insight, assumptions |
| `logic/claims.md` | 10 falsifiable claims (C01-C10) with proof and falsification criteria |
| `logic/concepts.md` | Ontology: Muon, FlexAttention, BoN search, Newton-Schulz, hint levels, gap recovered |
| `logic/experiments.md` | 7 experiment plans (E01-E07) covering all evaluation ablations |
| `logic/related_work.md` | 10 dependency-typed related work entries |
| `logic/solution/algorithm.md` | BoN search algorithm, Muon optimizer pseudocode, Newton-Schulz iteration |
| `logic/solution/architecture.md` | Agent scaffold: Ideator-Coder-Runner-Analyst pipeline with versioned workspace |
| `logic/solution/constraints.md` | Hardware, software, evaluation, agent benchmark, and generalization constraints |
| `logic/solution/heuristics.md` | 10 design heuristics (H01-H10) with sensitivity and provenance |

### Physical Layer (`src/`)

| File | Description |
|------|-------------|
| `src/environment.md` | Hardware (8xH100), software (PyTorch 2.5+), dataset, agent dependencies, seeds |
| `src/configs/model.md` | GPT-2 124M baseline vs. final architecture comparison; agent model table |
| `src/configs/training.md` | Full optimizer, training recipe, and agent benchmark hyperparameters |
| `src/configs/task_config.md` | Scoring details (FSR formula), 19 record transitions, hint levels, in/out-of-bounds rules |
| `src/execution/muon_optimizer.py` | Muon optimizer: Newton-Schulz orthogonalization + Nesterov momentum |
| `src/execution/flex_attention.py` | FlexAttention with document-aware causal masking and sliding window |
| `src/execution/unet_skip.py` | U-Net encoder-decoder skip connections for transformers |
| `src/execution/bon_runner.py` | Best-of-N search runner with 5 scaffold variants (Algorithm 1) |
| `src/execution/workspace.py` | Versioned workspace tree manager for agent search |
| `src/execution/knowledge.py` | Knowledge/hint store for multi-level hint loading |

### Evidence Layer (`evidence/`)

| File | Description |
|------|-------------|
| `evidence/tables/table1_speedrun_progression.md` | All 21 records: timing, val_loss, key optimization, phase |
| `evidence/tables/table2_scaffold_configs.md` | 5 scaffold configurations with rationale |
| `evidence/tables/table3_main_fsr_results.md` | Main FSR results: 4 models x 5 scaffolds x 6 hint regimes |
| `evidence/tables/table4_cumulative_degradation.md` | Cumulative vs. non-cumulative FSR over chained transitions |
| `evidence/tables/table5_external_knowledge.md` | FlexAttention external docs impact on Record 12 FSR |
| `evidence/tables/table6_per_record_fsr.md` | Per-record FSR by model showing difficulty scaling |
| `evidence/figures/fig1_timeline.md` | Speedrun timeline (training time vs. record) |
| `evidence/figures/fig3_fsr_distributions.md` | FSR distributions per model and hint level |
| `evidence/figures/fig4_hint_ablation.md` | Hint-level ablation (FSR vs. hint detail) |
| `evidence/figures/fig5_scaffold_comparison.md` | Scaffold comparison (IQM FSR per scaffold) |
| `evidence/figures/fig6_per_record_fsr.md` | FSR vs. record index (difficulty scaling) |
| `evidence/figures/fig7_cumulative_degradation.md` | Cumulative FSR degradation visualization |
| `evidence/figures/fig8_search_dynamics.md` | Search tree dynamics (node-type fractions over steps) |
| `evidence/figures/fig9_code_similarity.md` | Code embedding similarity vs. FSR scatter |
