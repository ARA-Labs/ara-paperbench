---
# Heuristics

## H01: Use k=10 responses as minimum viable sample size
- **Rationale**: Below k ≈ 7–10 responses, performance gains from semantic methods become unstable and may produce random-level accuracy. The paper demonstrates consistent performance at k=10 across all methods.
- **Sensitivity**: high
- **Bounds**: k ≥ 7 (minimum); k=10 used in all main experiments; increasing k beyond 10 expected to improve further
- **Code ref**: [src/execution/semantic_self_consistency.py]
- **Source**: Appendix I.1

## H02: Select featurizer by dataset domain
- **Rationale**: SciBERT produces average distance 45.281 on arithmetic tasks vs. RoBERTa's 48.697; tighter clusters improve weighting discriminability. Using a general featurizer on domain-specific data loses ~3.4 distance units of compactness.
- **Sensitivity**: high
- **Bounds**: Use SciBERT 110M for AQuA-RAT and SVAMP; use RoBERTa 125M for StrategyQA; consider MathBERT for pure math tasks
- **Code ref**: [src/execution/semantic_self_consistency.py]
- **Source**: Appendix G.2, Table 6

## H03: Use temperature=0.8 for standard experiments
- **Rationale**: Temperature=0.8 provides sufficient sampling diversity for self-consistency while avoiding excessive degeneration. The sweet spot for varied-temperature experiments is t ∈ [0.5, 0.9].
- **Sensitivity**: medium
- **Bounds**: Static temperature=0.8 for all main experiments; for varied-temperature, use Set 1: {0.9, 0.8, 0.7, 0.6, 0.5} applied equally across 1/5 of samples each
- **Code ref**: [src/execution/semantic_self_consistency.py]
- **Source**: Appendix J.1, Table 10

## H04: Apply Isolation Forest with n_estimators=200
- **Rationale**: Grid search found n_estimators=200 with contamination=auto and max_samples=auto achieves the best average accuracy (58.56% averaged across all models and datasets) among Isolation Forest configurations.
- **Sensitivity**: medium
- **Bounds**: n_estimators=200; contamination='auto'; max_samples='auto'
- **Code ref**: [src/execution/semantic_self_consistency.py]
- **Source**: Appendix I.2.2

## H05: Set max-new-tokens per dataset
- **Rationale**: Different datasets require different reasoning chain lengths. SVAMP needs only 250 tokens; AQuA-RAT and StrategyQA require longer chains (400 and 450 respectively) to avoid truncation of reasoning.
- **Sensitivity**: medium
- **Bounds**: SVAMP=250; AQuA-RAT=400; StrategyQA=450
- **Code ref**: [src/execution/semantic_self_consistency.py]
- **Source**: Appendix I.4
