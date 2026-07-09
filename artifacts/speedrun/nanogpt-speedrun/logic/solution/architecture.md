---
type: architecture
paper: nanogpt-speedrun
---

# Solution Architecture

## Overview

The LLM Speedrunner is a tree-structured experimentation framework where three LLM agent roles collaborate to reproduce training optimizations. The system versions all artifacts (code, hypotheses, results, conversations) in an explicit workspace tree.

## Component Graph

```
┌──────────────┐     hypothesis     ┌──────────────┐     edited code    ┌──────────────┐
│   Ideator    │ ──────────────────→│    Coder     │ ──────────────────→│   Runner     │
│ (proposes    │                    │ (implements  │                    │ (executes on │
│  optimization│                    │  via aider   │                    │  SLURM/GPU)  │
│  hypothesis) │                    │  diff edits) │                    │              │
└──────┬───────┘                    └──────────────┘                    └──────┬───────┘
       │                                                                       │
       │ reads current code                                          results.json
       │ + prior results                                             + train logs
       │ + bug history                                                         │
       │                                                                       ▼
       │                    ┌──────────────────────────────────┐       ┌──────────────┐
       └────────────────────│     Versioned Workspace          │←──────│   Analyst    │
                            │  v_0/ (template)                 │       │ (summarizes  │
                            │  v_1/ (first attempt)            │       │  outcomes,   │
                            │  v_2/ (branched from v_1)        │       │  extracts    │
                            │  ...                             │       │  metrics)    │
                            │  meta.json (tree structure)      │       └──────────────┘
                            │  results.json (metrics)          │
                            │  *_history.jsonl (LLM logs)      │
                            └──────────────┬───────────────────┘
                                           │
                                           ▼
                            ┌──────────────────────────────────┐
                            │     BoN Science Runner           │
                            │  - Branches N hypotheses         │
                            │  - Runs in parallel on SLURM     │
                            │  - Selects best (lowest time,    │
                            │    val_loss ≤ 3.28)              │
                            │  - Repeats for T iterations      │
                            └──────────────────────────────────┘
```

## Components

1. **Ideator** (`core/ideators/base.py`): Reads current code + past results + knowledge hints. Outputs JSON hypothesis with "summary" and "hypothesis" fields. DummyIdeator passes hints through unchanged.

2. **Coder** (`core/coders/aider.py`): Receives hypothesis + task description + bug history. Uses aider library for diff-based code editing of `train_gpt2.py`. AiderCoder wraps the aider chat interface.

3. **Runner** (`core/runners/bon_science_runner.py`): Submits modified training scripts to SLURM cluster via submitit. Manages parallel GPU jobs. Collects results.json and training logs.

4. **Analyst** (`core/prompts/analysis_prompts.py`): LLM-based log summarizer. Extracts val_loss, train_time, n_steps. Generates outcome_summary. Detects bugs.

5. **Versioned Workspace** (`core/workspace.py`): Tree-structured version control. Each version stores code, results, metadata (parent/children/bug_depth), and full LLM conversation histories.

6. **Knowledge Store** (`core/knowledge.py`): Loads hint files from disk at specified abstraction levels. Supports level combinations.

## Interactions

- Ideator → Coder: hypothesis JSON
- Coder → Runner: modified train_gpt2.py
- Runner → Analyst: training logs + results.json
- Analyst → Workspace: outcome_summary + metrics + bug classification
- Workspace → Ideator: current code + result history + bug history (feedback loop)
- BoN Runner orchestrates the outer loop: branch → run → select → repeat
