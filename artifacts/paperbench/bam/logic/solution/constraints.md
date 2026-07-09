# Boundary Conditions and Limitations

## Hard Requirements

### R1: Gaussian Variational Family
- **Constraint**: BaM is designed exclusively for Q = {N(μ, Σ) : μ ∈ R^D, Σ ∈ S^D_{++}}. The closed-form solution to ΣUΣ + Σ = V relies on this structure.
- **Implication**: Cannot directly handle multimodal or heavy-tailed approximations. Full covariance requires O(D²) parameters, limiting practical D.
- **Mitigation**: Authors note future work on non-Gaussian variational families.

### R2: Differentiable Log-Target Density
- **Constraint**: The score function s(z) = ∇_z log p(z) must be computable. This requires log p to be differentiable everywhere on R^D.
- **Implication**: Cannot handle discrete latent variables or non-differentiable likelihoods directly.

### R3: Full-Support Target Density
- **Constraint**: Both p(z) > 0 and q(z) > 0 for all z ∈ R^D required for theoretical guarantees (Appendix A conditions).
- **Implication**: Bounded-support distributions require reparameterization.

### R4: Positive Definite Initial Covariance
- **Constraint**: Σ_0 ≻ 0 required for convergence proof (α > 0).
- **Implication**: Initializing with Σ_0 = I satisfies this in practice.

## Known Limitations

### L1: Convergence Proof Only Covers Gaussian Targets and Infinite Batch
- **Statement**: Theorem 3.1 requires p to be Gaussian and B → ∞. For non-Gaussian targets and finite B, convergence is empirically observed but not theoretically guaranteed.
- **Practical impact**: BaM works empirically on non-Gaussian targets, but may require tuning of decaying learning rate schedule λ_t = BD/(t+1).

### L2: Gaussian Approximation Bias for Non-Gaussian Targets
- **Statement**: For highly non-Gaussian targets (e.g., s=1.8 sinh-arcsinh), BaM converges to a higher forward KL divergence than ADVI (Figure 5.2), indicating the Gaussian approximation is limited.
- **Practical impact**: Both BaM and ADVI are limited by the Gaussian family; BaM's advantage is speed, not approximation quality.

### L3: Small Batch Size Fails for High-Dimensional Latent Variables
- **Statement**: For the deep generative model (D=256), BaM with B=10 performs poorly. The batch size should be comparable to D for stable convergence.
- **Rule of thumb**: B should be O(D) or larger for high-dimensional problems.

### L4: Pilot Tuning Required for Deep Generative Models
- **Statement**: BaM with non-Gaussian targets (especially deep generative) requires a pilot run of 100 iterations to select the learning rate λ from a grid search.
- **Practical impact**: Adds overhead; GSM does not require this tuning step.

### L5: Higher Relative SD Error for Hierarchical Models
- **Statement**: For the eight-schools-centered hierarchical model, BaM converges to a larger relative standard deviation error than GSM (Figure E.6), suggesting potential room for better regularization tuning.

### L6: O(D³) Computational Cost per Iteration
- **Statement**: The full-rank covariance update costs O(D³). While manageable for models with O(D²) parameters (which is already assumed), this limits scalability to very large D.
- **Mitigation**: Low-rank solver (Lemma B.3) reduces cost to O(D²B + B³) when B << D.

## Assumptions Made in Derivation

- A1: Empirical score-based divergence D̂_{q_t}(q;p) is a good proxy for D(q;p) when q_t ≈ q (ensured by regularization).
- A2: The quadratic matrix equation ΣUΣ + Σ = V has a unique PD solution (guaranteed by Lemma B.2 when V ≻ 0, U ⪰ 0).
- A3: For the convergence proof, target scores at samples from q_t converge to their expectations via the law of large numbers (B → ∞ limit).
