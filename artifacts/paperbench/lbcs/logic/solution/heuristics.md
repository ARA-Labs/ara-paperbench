# Heuristics and Implementation Tricks

## H01: Pre-train then fine-tune for inner-loop acceleration
- **Rationale**: Training the inner-loop proxy network from scratch at every outer iteration is expensive. Since nearby masks produce similar coresets, starting from a pre-trained checkpoint and fine-tuning for a few epochs significantly reduces inner-loop cost.
- **Sensitivity**: medium — the quality of fine-tuning approximation affects f1(m) evaluation accuracy, but empirically the approach works well.
- **Bounds**: Pre-training should use a representative initialization (e.g., random mask with ‖m‖₀ = k). Fine-tuning duration should be long enough for meaningful convergence but short enough to save computation.
- **Code ref**: [src/execution/lbcs.py]
- **Source**: §3.2 ("To speed up the inner loop, we can first train a model with random masks and then finetune it with other different masks")

## H02: Model sparsity for inner-loop speedup
- **Rationale**: Applying model sparsity (e.g., pruning) to the proxy network during inner-loop training makes it smaller and faster to train, reducing the per-iteration cost of LBCS.
- **Sensitivity**: low to medium — depends on the level of sparsity applied; high sparsity may reduce f1 evaluation quality.
- **Bounds**: Sparsity level should be tuned to maintain reasonable f1(m) correlation with the dense model.
- **Code ref**: [src/execution/lbcs.py]
- **Source**: §3.2 ("Also, we can employ model sparsity and make the trained model smaller for faster training")

## H03: Group-based mask search for large datasets
- **Rationale**: For datasets like ImageNet-1k (n ≈ 1.28M), searching over n binary variables is intractable. Grouping G=100 consecutive examples to share one mask variable reduces the search space to n/G dimensions.
- **Sensitivity**: high — G determines the granularity of coreset size reduction. Larger G enables faster search but coarser size control.
- **Bounds**: G=100 used for ImageNet-1k. Smaller G gives finer granularity at higher cost. The same grouping trick is applied to the Probabilistic baseline for fair comparison.
- **Code ref**: [src/execution/lbcs.py]
- **Source**: §3.2 ("the mask search space can be narrowed by treating several examples as a group"); §5.4

## H04: Voluntary performance compromise ε to reduce overfitting
- **Rationale**: Driving f1(m) to the exact minimum overfits the coreset selection to training noise. Allowing a fractional relaxation ε (default 0.2) prevents this, improving generalization especially under noisy or imbalanced labels.
- **Sensitivity**: medium — too small ε makes size reduction slow; too large ε may allow poor-accuracy coresets.
- **Bounds**: ε ∈ [0.2, 0.4] tested in §5.1; ε=0.2 used for all main experiments (§5.2). Larger ε leads to smaller average f2(m) and larger average f1(m) across repeated runs.
- **Code ref**: [src/execution/lbcs.py]
- **Source**: §3.2 (Remark 2), §5.1

## H05: Dynamic step-size and random restart in LexiFlow
- **Rationale**: Fixed step-size search gets stuck in local optima. Reducing the step size when no progress is made for 2n consecutive iterations, and restarting randomly when the step size falls below a threshold, helps escape local optima and explore globally.
- **Sensitivity**: high — δ_init and δ_lower need to be calibrated for the mask space scale.
- **Bounds**: Step-size update rule: δ ← δ · √((t'+1)/(t+1)) after 2n consecutive failed updates. Restart: δ ← δ_init + r (increment by restart count). Specific values of δ_init and δ_lower not specified in the paper; inherited from LexiFlow (Zhang et al. 2023b).
- **Code ref**: [src/execution/lbcs.py]
- **Source**: §3.2 ("To free the algorithm from local optima and manual configuration of the step size, LexiFlow includes restart and dynamic step size techniques"); Appendix A
