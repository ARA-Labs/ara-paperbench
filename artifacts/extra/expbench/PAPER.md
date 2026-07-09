---
title: "EXP-Bench: Can AI Conduct AI Research Experiments?"
authors:
  - Patrick Tser Jern Kon
  - Jiachen Liu
  - Xinyi Zhu
  - Qiuyi Ding
  - Jingjia Peng
  - Jiarong Xing
  - Yibo Huang
  - Yiming Qiu
  - Jayanth Srinivasa
  - Myungjin Lee
  - Mosharaf Chowdhury
  - Matei Zaharia
  - Ang Chen
year: 2025
venue: "arXiv preprint (under review)"
doi: "arXiv:2505.24785"
ara_version: "1.0"
domain: "AI Research Automation / Benchmarking"
keywords:
  - AI research automation
  - benchmark
  - end-to-end experimentation
  - LLM agents
  - code generation
  - experimental design
  - reproducibility
  - OpenHands
  - conjunctive evaluation
  - semi-automated curation
claims_summary:
  - "Leading AI agents score 20–35% on individual experiment phases but only 0.5% on complete, executable end-to-end experiments"
  - "The most prevalent failure mode is missing essential implementation components (39.71%), followed by environment/dependency configuration errors (29.38%)"
  - "Conjunctive evaluation metrics collapse average agent scores from ~20.6% (monitor-only) to 0.2% (all criteria including execution), revealing brittleness hidden by partial scoring"
abstract: "Automating AI research holds immense potential for accelerating scientific progress, yet current AI agents struggle with the complexities of rigorous, end-to-end experimentation. We introduce EXP-Bench, a novel benchmark designed to systematically evaluate AI agents on complete research experiments sourced from influential AI publications. Given a research question and incomplete starter code, EXP-Bench challenges AI agents to formulate hypotheses, design and implement experimental procedures, execute them, and analyze results. To enable the creation of such intricate and authentic tasks with high-fidelity, we design a semi-autonomous pipeline to extract and structure crucial experimental details from these research papers and their associated open-source code. With the pipeline, EXP-Bench curated 461 AI research tasks from 51 top-tier AI research papers. Evaluations of leading AI agents, such as OpenHands and IterativeAgent on EXP-Bench demonstrate partial capabilities: while scores on individual experimental aspects such as design or implementation correctness reach 20–35%, the success rate for complete, executable experiments was a mere 0.5%. By identifying these bottlenecks and providing realistic step-by-step experiment procedures, EXP-Bench serves as a vital tool for future AI agents to improve their ability to conduct AI research experiments."
---

# EXP-Bench: Can AI Conduct AI Research Experiments?

## Overview

EXP-Bench is a benchmark that evaluates AI agents on complete, end-to-end AI research experiments extracted from 51 peer-reviewed publications (NeurIPS 2024 and ICLR 2024). Each task provides an agent with a research question, a high-level method description, and starter code with masked implementation files. The agent must design the experiment, implement the required code modifications, execute them, and derive a conclusion — all without accessing the original paper.

The benchmark comprises 461 research tasks (12,737 individually gradable subtasks) spanning diverse AI subfields including deep learning, reinforcement learning, computer vision, generative models, and optimization. A semi-automated curation pipeline (multi-modal extraction + execution-based validation) produces high-fidelity ground truth for design variables, code diffs, and conclusions. Evaluation of leading agents (OpenHands, IterativeAgent) with multiple LLM backbones reveals that partial-phase scores reach 20–35% but the complete end-to-end success rate is just 0.5%, exposing fundamental bottlenecks in hypothesis operationalization, implementation completeness, and environment reproducibility.

## Layer Index

### Cognitive Layer (`/logic`)
| File | Description |
|------|-------------|
| [problem.md](logic/problem.md) | Observations → gaps → key insight driving benchmark design |
| [claims.md](logic/claims.md) | 6 falsifiable claims (C01–C06) |
| [concepts.md](logic/concepts.md) | 10 key terms with formal definitions |
| [experiments.md](logic/experiments.md) | 5 verification plans (E01–E05) |
| [solution/architecture.md](logic/solution/architecture.md) | System design: 3-stage curation pipeline + 4-metric evaluation framework |
| [solution/algorithm.md](logic/solution/algorithm.md) | Multi-pass extraction algorithm + conjunctive scoring |
| [solution/constraints.md](logic/solution/constraints.md) | Boundary conditions and known limitations |
| [solution/heuristics.md](logic/solution/heuristics.md) | 5 pipeline and evaluation heuristics |
| [related_work.md](logic/related_work.md) | 12 typed dependencies (RW01–RW12) |

### Physical Layer (`/src`)
| File | Description | Claims |
|------|-------------|--------|
| [execution/curation_pipeline.py](src/execution/curation_pipeline.py) | Semi-automated task extraction and validation pipeline stub | C01, C02 |
| [execution/evaluation_judge.py](src/execution/evaluation_judge.py) | LLM-as-a-judge conjunctive evaluation framework stub | C03, C04, C05, C06 |
| [configs/training.md](src/configs/training.md) | Evaluation agent run parameters (timeout, GPU allocation, containers) | — |
| [configs/model.md](src/configs/model.md) | LLM judge and backbone model configurations | — |
| [environment.md](src/environment.md) | Hardware, dependencies, and containerization specs | — |

### Exploration Graph (`/trace`)
| File | Description |
|------|-------------|
| [exploration_tree.yaml](trace/exploration_tree.yaml) | 12-node research DAG tracing benchmark design decisions |

### Evidence (`/evidence`)
| File | Description |
|------|-------------|
| [README.md](evidence/README.md) | Full index of 9 tables + 3 quantitative figures |
| [tables/table1_main_results.md](evidence/tables/table1_main_results.md) | Average benchmark scores across all 461 tasks for 7 agent configurations |
| [tables/table2_failure_patterns.md](evidence/tables/table2_failure_patterns.md) | Simplified failure type prevalence across all four experiment phases |
| [tables/table3_category_results.md](evidence/tables/table3_category_results.md) | Per-category scores for select agent-model pairs |
| [tables/table4_iclr_papers.md](evidence/tables/table4_iclr_papers.md) | Full list of ICLR 2024 source papers with metadata |
| [tables/table5_neurips_papers.md](evidence/tables/table5_neurips_papers.md) | Full list of NeurIPS 2024 source papers with metadata |
| [tables/table6_full_category_results.md](evidence/tables/table6_full_category_results.md) | Complete per-category benchmark scores across all agents |
| [tables/table7_extraction_issues.md](evidence/tables/table7_extraction_issues.md) | Examples of extraction issues identified and patched in the pipeline |
| [tables/table8_extended_failure_patterns.md](evidence/tables/table8_extended_failure_patterns.md) | Extended failure type analysis with 361 unique categories |
| [tables/table9_cost_time.md](evidence/tables/table9_cost_time.md) | Full cost–time summary statistics across all agents |
| [figures/fig6b_conjunctive_metrics.md](evidence/figures/fig6b_conjunctive_metrics.md) | Progressive conjunctive metric strictness vs. average agent score |
| [figures/fig5_metric_stability.md](evidence/figures/fig5_metric_stability.md) | Metric variance comparison: individual vs. conjunctive scoring |
| [figures/fig6a_cost_time.md](evidence/figures/fig6a_cost_time.md) | Average cost vs. average time per task across agent configurations |
