---
# Problem Specification

## Observations

### O1: LLMs underperform on reasoning tasks
- **Statement**: Despite strong general performance, LLMs achieve suboptimal accuracy in mathematics, commonsense, and complex algorithmic reasoning.
- **Evidence**: Hendrycks et al. (2021) MATH dataset results; discussed in §1.
- **Implication**: Reasoning tasks require targeted methods beyond standard generation.

### O2: Self-consistency (majority vote) improves reasoning accuracy
- **Statement**: Sampling n rationales with chain-of-thought prompting and taking a majority vote over final answers reliably improves accuracy over single-sample greedy decoding.
- **Evidence**: Wang et al. (2023) self-consistency paper [33]; Table 1 SC baseline vs. Top prob sample results throughout the paper.
- **Implication**: Ensembling multiple reasoning paths is beneficial, but aggregation is currently only over final answers.

### O3: Standard self-consistency ignores reasoning-path semantics
- **Statement**: Existing self-consistency aggregates only final answer tokens; the full reasoning path (chain-of-thought) contains semantic information not exploited in voting.
- **Evidence**: Described in §1 and Figure 1; motivation for semantic weighting.
- **Implication**: A semantic re-ranking step could shift weight toward more consistent reasoning paths.

### O4: Models frequently apply correct reasoning but conclude incorrectly
- **Statement**: LLMs often produce correct intermediate reasoning steps but arrive at an incorrect final answer (arithmetic errors, hallucinations).
- **Evidence**: Stated explicitly in Figure 1 caption: "Our assumption is that language models often apply the correct reasoning but lack the ability to conclude to the correct result."
- **Implication**: Filtering or down-weighting incorrect final answers based on their reasoning paths could recover the correct answer.

### O5: Embedding quality correlates with task domain alignment
- **Statement**: Fine-tuned BERT variants (SciBERT, MathBERT) produce tighter embedding clusters on mathematical reasoning tasks (avg distance 45.281 and 45.892 respectively) compared to general RoBERTa (avg distance 48.697).
- **Evidence**: Table 6, Appendix G.2.
- **Implication**: Featurizer selection is critical; domain-mismatched featurizers reduce clustering quality.

## Gaps

### G1: Semantic information in reasoning paths is discarded
- **Statement**: Self-consistency disregards all step-by-step reasoning content when voting on answers; only the final token(s) matter.
- **Caused by**: O2, O3
- **Existing attempts**: Chain-of-thought prompting generates reasoning paths but does not use them for aggregation.
- **Why they fail**: The aggregation step reduces each rationale to its final answer, losing semantic similarity signals.

### G2: No mechanism to filter hallucinated or degenerate outputs before voting
- **Statement**: Outliers (hallucinated rationales, degenerate outputs) pollute the majority vote and may flip the decision.
- **Caused by**: O2, O4
- **Existing attempts**: Self-improvement methods (Huang et al., 2022); importance weighting (Jiang et al., 2024) require additional pre-training.
- **Why they fail**: Pre-training steps add significant compute; no lightweight post-generation filter exists.

### G3: Majority vote performance degrades with small sample sizes
- **Statement**: With k < 7–10 responses, self-consistency gains diminish and can produce random results.
- **Caused by**: O2
- **Existing attempts**: Increasing k, but this increases generation cost linearly.
- **Why they fail**: Cannot reduce k without a smarter aggregation to compensate.

## Key Insight

- **Insight**: The semantic consistency of reasoning paths in embedding space encodes correctness signals — embeddings that cluster tightly around the centroid (CPW) or show high mutual cosine similarity (SCW) correspond to more reliable responses. Separately, embeddings that lie far from the cloud (outliers) correspond to degenerate reasoning.
- **Derived from**: O3, O4, O5
- **Enables**: A lightweight, post-generation weighting/filtering step that re-ranks candidate answers using embedding geometry, without any additional training.

## Assumptions

- A1: Correct reasoning paths are semantically more similar to each other than to incorrect/hallucinated paths in embedding space.
- A2: A suitable domain-aligned featurizer (e.g., SciBERT for math) is available.
- A3: k ≥ 7–10 samples are generated per question (minimum for stable performance).
- A4: Chain-of-thought prompting is used, producing sufficiently long reasoning sequences.
- A5: The correct answer exists in at least one of the k sampled responses (self-consistency precondition).
