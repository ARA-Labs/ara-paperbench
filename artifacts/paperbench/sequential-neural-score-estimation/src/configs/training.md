# Training Configuration

## Optimizer
- **Value**: Adam (Kingma & Ba, 2015)
- **Rationale**: Standard adaptive optimizer; robust across tasks without per-task tuning.
- **Search range**: Not specified in paper.
- **Sensitivity**: low
- **Source**: Section 5.1, Appendix E.3.2

## Learning Rate
- **Value**: 1 × 10⁻⁴
- **Rationale**: Standard learning rate for Adam with neural score networks; not tuned per task.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Section 5.1, Appendix E.3.2

## Batch Size (Non-Sequential, Budget ≤ 10000)
- **Value**: 50
- **Rationale**: Small datasets require small batches to cycle through training data.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.2

## Batch Size (Sequential, Budget ≤ 10000)
- **Value**: 200
- **Rationale**: Accumulated dataset across rounds is larger, supporting larger batch size.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.2

## Batch Size (Budget = 100000, All Methods)
- **Value**: 500
- **Rationale**: Large dataset supports large batch.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.2

## Validation Split
- **Value**: 15% of dataset held out
- **Rationale**: Standard held-out fraction; re-computed per round in sequential experiments as 15% of all available simulations sampled uniformly at random.
- **Search range**: Not specified in paper.
- **Sensitivity**: low
- **Source**: Section 5.1, Appendix E.3.2

## Early Stopping Patience
- **Value**: 1000 training steps without validation loss improvement
- **Rationale**: Return the network giving the lowest validation loss. Prevents overfitting.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.2

## Maximum Training Iterations
- **Value**: 3000 (both sequential and non-sequential experiments)
- **Rationale**: Caps training time; early stopping usually triggers before this.
- **Search range**: Not specified in paper.
- **Sensitivity**: low
- **Source**: Appendix E.3.2

## Number of Rounds (Sequential, Benchmarks)
- **Value**: R = 10
- **Rationale**: Standard for sequential SBI; budget divided equally M = N/R per round.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.3

## Number of Rounds (Pyloric Experiment)
- **Value**: 9 rounds; 30000 initial simulations + 20000 per subsequent round
- **Rationale**: Adapts to the Pyloric problem's large valid-sample scarcity; first round larger to establish a reasonable initial posterior.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Section 5.3

## C2ST Sample Count
- **Value**: 10000 samples from approximate posterior; 10000 from true posterior
- **Rationale**: Standard for sbibm C2ST evaluation.
- **Search range**: Not applicable.
- **Sensitivity**: low
- **Source**: Appendix E.3.2 (implied by sbibm default)

## HPR Estimation Sample Count (TSNPSE)
- **Value**: 20000 posterior samples per round
- **Rationale**: Large sample for reliable empirical HPR estimation.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.3

## HPR Truncation Threshold (TSNPSE)
- **Value**: ε = 5 × 10⁻⁴ (log-probability rejection threshold is the ε-th quantile of posterior log-densities)
- **Rationale**: Retains 99.95% of posterior mass, making the correctness assumption (Proposition 3.1) approximately valid.
- **Search range**: Not specified in paper.
- **Sensitivity**: medium
- **Source**: Appendix E.3.3

## ODE Solver
- **Value**: RK45 (off-the-shelf)
- **Rationale**: Standard adaptive step-size ODE solver; good accuracy-efficiency tradeoff.
- **Search range**: Not specified in paper.
- **Sensitivity**: low
- **Source**: Appendix E.3.3
