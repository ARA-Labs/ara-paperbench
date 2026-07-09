# Model Configuration

## θ_t Embedding Network: Depth
- **Value**: 3 fully connected layers
- **Rationale**: Shallow but wide network sufficient for embedding fixed-dimensional inputs.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.2

## θ_t Embedding Network: Width
- **Value**: 256 hidden units per layer
- **Rationale**: Standard width for SBI score networks; not tuned per task.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.2

## θ_t Embedding Network: Output Dimension
- **Value**: max(30, 4 × d) where d = dim(θ)
- **Rationale**: Scales embedding size with parameter dimensionality; minimum 30 for low-d problems.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.2

## x Embedding Network: Depth
- **Value**: 3 fully connected layers
- **Rationale**: Symmetric to θ_t embedding.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.2

## x Embedding Network: Width
- **Value**: 256 hidden units per layer
- **Rationale**: Same as θ_t network.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.2

## x Embedding Network: Output Dimension
- **Value**: max(30, 4 × p) where p = dim(x)
- **Rationale**: Scales with observation dimensionality.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.2

## t Sinusoidal Embedding: Output Dimension
- **Value**: 64 dimensions
- **Rationale**: Fixed-size sinusoidal embedding inspired by transformer positional encoding (Vaswani et al., 2017).
- **Search range**: Not specified in paper.
- **Sensitivity**: low
- **Source**: Appendix E.3.2

## t Sinusoidal Embedding: Formula
- **Value**: `(t_emb)_i = sin(t / 10000^{(i-1)/31})` if i ≤ 32, else `cos(t / 10000^{((i-32)-1)/31})`
- **Rationale**: Captures time at multiple scales; avoids learning time representation from scratch.
- **Search range**: Not applicable.
- **Sensitivity**: low
- **Source**: Appendix E.3.2, Eq. (138)

## Score Network: Depth
- **Value**: 3 fully connected layers
- **Rationale**: Symmetric to embedding networks; concatenated input fed through final MLP.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.2

## Score Network: Width
- **Value**: 256 hidden units per layer
- **Rationale**: Fixed across all experiments; robust without per-task tuning.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.2

## Score Network: Output Dimension
- **Value**: d (same as parameter dimension)
- **Rationale**: Score function ∇_θ log p(θ|x) has the same dimension as θ.
- **Search range**: Not applicable.
- **Sensitivity**: N/A
- **Source**: Appendix E.3.2

## Activation Function
- **Value**: SiLU (Sigmoid Linear Unit) for all MLP layers
- **Rationale**: Smooth, non-monotonic activation shown to work well for score networks.
- **Search range**: Not specified in paper.
- **Sensitivity**: low
- **Source**: Section 5.1, Appendix E.3.2

## Standardisation
- **Value**: Both θ_t and x standardised by subtracting empirical mean and dividing by empirical std before input to embedding networks.
- **Rationale**: Improves training stability; scales vary widely across tasks.
- **Search range**: Not applicable.
- **Sensitivity**: medium
- **Source**: Appendix E.3.3

## VE SDE: σ_min (2D tasks: SIR, Two Moons)
- **Value**: 0.01
- **Rationale**: Low-dimensional posteriors can be narrow; small σ_min avoids over-smoothing.
- **Search range**: Not specified in paper.
- **Sensitivity**: high
- **Source**: Appendix E.3.1

## VE SDE: σ_min (all other tasks)
- **Value**: 0.05
- **Rationale**: Higher-dimensional tasks are more tolerant of larger minimum noise.
- **Search range**: Not specified in paper.
- **Sensitivity**: high
- **Source**: Appendix E.3.1

## VE SDE: σ_max
- **Value**: Maximum pairwise Euclidean distance among all training data points (θ-space only); for sequential methods, computed using first-round training data.
- **Rationale**: Ensures the forward process covers the full data range (Technique 1 of Song & Ermon, 2020).
- **Search range**: Data-dependent; not tuned manually.
- **Sensitivity**: high
- **Source**: Appendix E.3.1

## VP SDE: β_min
- **Value**: 0.1
- **Rationale**: Following Song & Ermon (2020); ensures slow initial noise addition.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.1

## VP SDE: β_max
- **Value**: 11.0
- **Rationale**: Following Song & Ermon (2020); ensures sufficient noise at t=1 for Gaussian reference.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.1

## Time Interval
- **Value**: (0, 1] for both VE and VP SDE
- **Rationale**: Normalised time interval; T=1 for both SDE types.
- **Search range**: Not applicable.
- **Sensitivity**: low
- **Source**: Appendix E.3.1
