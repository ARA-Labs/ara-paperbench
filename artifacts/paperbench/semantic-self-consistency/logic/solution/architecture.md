---
# System Architecture

## Overview

Semantic Self-Consistency extends the 3-step self-consistency pipeline with a 4th step: semantic re-weighting or filtering of reasoning paths before majority voting. The system has two main subsystems: (1) the Generator subsystem and (2) the Featurizer + Weighting/Filtering subsystem.

## Component Graph

```
[Input Question]
      |
      v
[Generator] ──────────────────────────────────────────────────
  Purpose: Produce k chain-of-thought reasoning responses       |
  Input: Few-shot prompt + question                             |
  Output: k reasoning paths r_1, ..., r_k                      |
  Models: GPT-3.5, GPT-4o mini, Llama 2 7B, Llama 3 8B,       |
          Mistral 7B                                            |
  Params: k=10, temperature=0.8, top-p=1, top-k=50             |
  max-new-tokens: SVAMP=250, AQuA-RAT=400, StrategyQA=450      |
      |                                                         |
      v                                                         |
[Answer Parser]                                                 |
  Purpose: Extract final answer token(s) from each response     |
  Input: r_i (full response string)                            |
  Output: a_i (answer string)                                  |
  Method: Extract string after "The answer is"; strip           |
          whitespace, fullstops, parentheses                    |
      |                                                         |
      |─────────────────────────────────────────────────────────
      |
      v
[Featurizer]
  Purpose: Convert each reasoning path to embedding vector
  Input: r_i (full reasoning path text)
  Output: e_i ∈ R^d (CLS token embedding)
  Models: SciBERT 110M (AQuA-RAT, SVAMP)
          RoBERTa 125M (StrategyQA)
      |
      v
[Semantic Weighting / Filtering Module]  ← Three alternatives:
  ┌─────────────────────────────────────────────────────────┐
  │ CPW Branch:                                             │
  │   Compute centroid of {e_1,...,e_k}                     │
  │   Compute normalized distances to centroid              │
  │   Assign inverse-proportional weights                   │
  │   Sum weights per unique answer                         │
  └─────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────┐
  │ SCW Branch:                                             │
  │   Compute pairwise cosine similarities                  │
  │   Aggregate similarity scores per embedding             │
  │   Sum scores per unique answer                          │
  └─────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────┐
  │ Outlier Removal Branch:                                 │
  │   Fit anomaly detector (IF, KNN, or SVM) on {e_i}       │
  │   Identify and remove outlier embeddings                │
  │   → Subset {r_j} without outliers                       │
  └─────────────────────────────────────────────────────────┘
      |
      v
[Majority Vote / Answer Selection]
  Purpose: Select final answer from weighted or filtered pool
  Input: (answer, weight) pairs or filtered answer set
  Output: Final predicted answer
  Method (CPW/SCW): argmax of summed weights/scores by answer
  Method (Outlier): majority vote over retained responses
```

## Design Notes

1. **Separation of featurizer from generator**: The featurizer operates only on reasoning paths, not on the model's probability distribution, enabling plug-and-play replacement.
2. **CLS token as representation**: The full reasoning path is represented by the single [CLS] token embedding, capturing the holistic semantic content without sentence-level decomposition.
3. **No retraining required**: All weighting and filtering is applied post-generation using off-the-shelf models. No gradient updates.
4. **Modular outlier removal**: The three outlier methods (IF, KNN, SVM) all feed into the same majority-vote step, making them interchangeable.
5. **Domain-specific featurizer selection**: SciBERT for mathematical reasoning tasks; RoBERTa for commonsense reasoning.
