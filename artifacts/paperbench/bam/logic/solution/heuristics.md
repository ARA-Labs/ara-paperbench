# Convergence Tricks and Heuristics

## H01: Constant learning rate for Gaussian targets
- **Rationale**: For Gaussian targets, the optimal regularization is independent of iteration since the problem structure is fixed. Theorem 3.1 guarantees convergence for any fixed λ > 0, so a constant schedule suffices and simplifies tuning.
- **Sensitivity**: low
- **Bounds**: λ_t = BD; typical values: B=2 → λ=8 (D=4), B=5 → λ=20 (D=4), B=150 → λ=38400 (D=256). Convergence rate improves with larger λ up to a point (β decreases with ||ε_0||).
- **Code ref**: [src/execution/bam.py]
- **Source**: Section 5.1, Appendix E.3

## H02: Decaying learning rate for non-Gaussian targets
- **Rationale**: For non-Gaussian targets, a constant λ_t tends not to converge; decay is needed to allow the algorithm to stabilize around a fixed point. λ_t = BD/(t+1) was found to converge faster than other schedules (λ_t = BD/√(t+1) or λ_t = BD).
- **Sensitivity**: medium
- **Bounds**: λ_t = BD/(t+1); alternative schedules tested: BD, BD/√(t+1), BD/(t+1). BD/(t+1) preferred for non-Gaussian targets and posteriordb.
- **Code ref**: [src/execution/bam.py]
- **Source**: Section 5.1-5.2, Appendix E.4 (Figure E.5)

## H03: Batch size proportional to dimension for deep generative models
- **Rationale**: For D=256 latent space, B=10 is insufficient; the covariance matrix U has effective rank B, so B should be at least O(D) to capture full covariance structure. B=300 ≈ D yields stable convergence.
- **Sensitivity**: high
- **Bounds**: B should be comparable to D. For D=256: B=10 fails, B=100 borderline, B=300 works. Rule: B ≥ D/2 to D for high-dimensional problems.
- **Code ref**: [src/execution/bam.py]
- **Source**: Section 5.3, Figure 5.4

## H04: Pilot run for learning rate selection in deep generative models
- **Rationale**: The optimal λ depends on batch size and problem structure in ways difficult to predict analytically for complex non-Gaussian targets. A 100-iteration pilot with candidate λ values enables data-driven selection.
- **Sensitivity**: medium
- **Bounds**: For B=10: λ searched over {0.01, 0.1, 0.2, 10}, selected λ=0.1. For B=100: λ searched over {2, 20, 50, 100, 200}, selected λ=50. For B=300: λ searched over {1000, 5000, 7500, 10000}, selected λ=7500. ADVI: best learning rate consistently ℓ=0.02 from search {0.001, 0.01, 0.02, 0.05}.
- **Code ref**: [src/execution/bam.py, src/execution/advi.py]
- **Source**: Appendix E.6

## H05: Initialize variational distribution at standard Gaussian
- **Rationale**: All experiments initialize at Σ_0 = I (identity covariance), μ_0 ~ Uniform[0, 0.1] or μ_0 = 0. This ensures Σ_0 ≻ 0 (required by convergence theory) and provides a neutral starting point. For deep generative model: initialize at N(0, I).
- **Sensitivity**: low
- **Bounds**: Σ_0 must be positive definite. Convergence rate depends on α = min_eigenvalue(Σ*^{-1/2}Σ_0 Σ*^{-1/2}); initializing at I works well in practice. β degrades when initial mean is far from target (large ||ε_0||).
- **Code ref**: [src/execution/bam.py]
- **Source**: Section 3.2, Appendix E.3, E.5, E.6
