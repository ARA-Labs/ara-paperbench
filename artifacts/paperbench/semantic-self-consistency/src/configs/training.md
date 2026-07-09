---
# Training / Inference Configuration

## k (number of samples)
- **Value**: 10
- **Rationale**: Minimum stable sample size for consistent performance. Below 7–10, gains become unstable (Appendix I.1).
- **Search range**: Tested with various k; k=10 used as default unless stated otherwise
- **Sensitivity**: high
- **Source**: Appendix I.1

## temperature
- **Value**: 0.8 (static for all main experiments)
- **Rationale**: Provides sufficient diversity for self-consistency while avoiding excessive degeneration. Sweet spot for varied-temperature experiments is t ∈ [0.5, 0.9].
- **Search range**: 0.1–0.9 tested in varied-temperature experiments (Appendix J.1, N)
- **Sensitivity**: medium
- **Source**: Appendix J.1

## top-p
- **Value**: 1
- **Rationale**: No nucleus sampling restriction; full vocabulary considered. Default for OpenAI API.
- **Search range**: Not varied
- **Sensitivity**: low
- **Source**: Appendix I.3

## top-k
- **Value**: 50
- **Rationale**: Limits vocabulary to top-50 tokens per step, reducing degenerate outputs.
- **Search range**: Not varied
- **Sensitivity**: low
- **Source**: Appendix I.3

## sampling
- **Value**: true
- **Rationale**: Stochastic sampling required for self-consistency diversity.
- **Search range**: Not varied (greedy used only for Top-prob baseline)
- **Sensitivity**: high
- **Source**: Appendix I.3

## max-new-tokens (SVAMP)
- **Value**: 250
- **Rationale**: SVAMP problems are relatively concise; 250 tokens sufficient for full solution.
- **Search range**: Not varied per dataset
- **Sensitivity**: medium
- **Source**: Appendix I.4

## max-new-tokens (AQuA-RAT)
- **Value**: 400
- **Rationale**: AQuA-RAT multi-step arithmetic requires longer reasoning chains.
- **Search range**: Not varied
- **Sensitivity**: medium
- **Source**: Appendix I.4

## max-new-tokens (StrategyQA)
- **Value**: 450
- **Rationale**: StrategyQA requires extended strategic reasoning chains; truncation would harm quality.
- **Search range**: Not varied
- **Sensitivity**: medium
- **Source**: Appendix I.4

## KNN n_neighbors
- **Value**: 5
- **Rationale**: Best-performing configuration in grid search for outlier detection; averaged accuracy 56.18%.
- **Search range**: Varied in grid search (Appendix I.2.1)
- **Sensitivity**: medium
- **Source**: Appendix I.2.1

## KNN threshold
- **Value**: 90% (retains 90% of distribution, filters top 10% by distance)
- **Rationale**: Removes the most extreme outliers while retaining enough samples for majority vote.
- **Search range**: Not specified beyond this configuration
- **Sensitivity**: medium
- **Source**: Appendix I.2.1

## KNN algorithm
- **Value**: ball_tree
- **Rationale**: Best-performing algorithm variant in grid search
- **Search range**: Varied in grid search
- **Sensitivity**: low
- **Source**: Appendix I.2.1

## KNN metric
- **Value**: euclidean (minkowski with p=2)
- **Rationale**: Standard Euclidean distance for embedding space nearest-neighbor search
- **Search range**: Not varied
- **Sensitivity**: low
- **Source**: Appendix I.2.1

## Isolation Forest n_estimators
- **Value**: 200
- **Rationale**: Best-performing configuration; averaged accuracy 58.56% across all models and datasets.
- **Search range**: Varied in grid search (Appendix I.2.2)
- **Sensitivity**: medium
- **Source**: Appendix I.2.2

## Isolation Forest contamination
- **Value**: auto
- **Rationale**: Uses sklearn default threshold from original paper definition.
- **Search range**: Varied in grid search
- **Sensitivity**: medium
- **Source**: Appendix I.2.2

## Isolation Forest max_samples
- **Value**: auto (min(256, n_samples))
- **Rationale**: sklearn default; balances computation and coverage.
- **Search range**: Varied in grid search
- **Sensitivity**: low
- **Source**: Appendix I.2.2

## One-class SVM kernel
- **Value**: linear
- **Rationale**: Best-performing kernel in grid search; averaged accuracy 55.17%.
- **Search range**: Varied in grid search (Appendix I.2.3)
- **Sensitivity**: medium
- **Source**: Appendix I.2.3

## One-class SVM nu
- **Value**: 0.01
- **Rationale**: Very low nu ensures only extreme outliers are flagged.
- **Search range**: Varied in grid search
- **Sensitivity**: high
- **Source**: Appendix I.2.3

## One-class SVM gamma
- **Value**: scale
- **Rationale**: sklearn default scale setting for gamma.
- **Search range**: Varied in grid search
- **Sensitivity**: medium
- **Source**: Appendix I.2.3
