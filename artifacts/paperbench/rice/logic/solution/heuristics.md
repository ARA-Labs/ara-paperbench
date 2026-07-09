# Heuristics

## H01: Set Reset Probability p to 0.25–0.5
- **Rationale**: Exclusively using critical states (p=1) causes overfitting; exclusively using default states (p=0) recovers vanilla PPO fine-tuning. A mixed distribution prevents overfitting while still leveraging critical state information. The range [0.25, 0.5] provides the best empirical trade-off across all tested environments.
- **Sensitivity**: medium
- **Bounds**: p ∈ {0, 0.25, 0.5, 0.75, 1.0} tested; p=0.25 optimal for Hopper, Walker2d, Selfish Mining, Auto Driving; p=0.5 optimal for Reacher, HalfCheetah, CAGE, Malware.
- **Code ref**: [src/execution/rice_refine.py]
- **Source**: Section 4.3, Appendix C.3, Figure 7

## H02: Set RND Weight λ to 0.01 for Most Environments
- **Rationale**: Any λ > 0 significantly improves performance over λ = 0. The exact value has low sensitivity. λ = 0.01 provides the best performance in all environments except Selfish Mining.
- **Sensitivity**: low
- **Bounds**: λ ∈ {0, 0.001, 0.01, 0.1} tested; λ=0.001 for Hopper/Reacher/Selfish Mining; λ=0.01 for all others.
- **Code ref**: [src/execution/rice_refine.py]
- **Source**: Section 4.3, Appendix C.3, Figure 8, Table 3

## H03: Set Blinding Bonus α to 0.0001 (Low Sensitivity)
- **Rationale**: α prevents the trivial solution (mask never blinds). Fidelity score is insensitive to α across the range tested. Using 0.0001 is conservative and avoids distorting the task reward signal.
- **Sensitivity**: low
- **Bounds**: α ∈ {0.01, 0.001, 0.0001} tested; all yield comparable fidelity. Default: α = 0.0001 for all environments.
- **Code ref**: [src/execution/mask_network.py]
- **Source**: Section 4.3, Appendix C.3, Figure 9, Table 3

## H04: Use Vanilla PPO (Not Primal-Dual) for Mask Network Training
- **Rationale**: By Theorem 3.3, the mask network objective can be simplified from min|η(π)−η(π̄)| to max η(π̄), enabling standard PPO. This eliminates the need to estimate discounted returns under both target and perturbed policies, reducing computation by ~16.8% on average.
- **Sensitivity**: high (choice of optimizer determines theoretical validity)
- **Bounds**: Only PPO is theoretically justified here; other optimizers not validated.
- **Code ref**: [src/execution/mask_network.py]
- **Source**: Section 3.3, Theorem 3.3, Table 4

## H05: Normalize RND Bonus Per Episode
- **Rationale**: Raw RND prediction errors have varying magnitudes across environments. Normalization ensures the exploration bonus remains proportional to the task reward regardless of state space dimensionality.
- **Sensitivity**: medium
- **Bounds**: Normalization should not collapse the bonus to zero before genuine exploration has occurred.
- **Code ref**: [src/execution/rice_refine.py]
- **Source**: Section 3.3 (Algorithm 2), Burda et al. (2018)
