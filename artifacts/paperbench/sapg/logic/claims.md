---
# Claims

## C01: PPO performance saturates with increasing parallel environments
- **Statement**: Increasing the number of parallel environments beyond a certain threshold (approximately 25,000) yields no further improvement in PPO's asymptotic performance, due to redundant IID samples from a shared Gaussian policy.
- **Status**: supported
- **Falsification criteria**: A plot of PPO asymptotic performance vs. batch size that shows monotonically increasing performance up to 100,000 environments would refute this claim.
- **Proof**: [E01]
- **Dependencies**: none
- **Tags**: PPO, batch-size scaling, data redundancy, IID sampling, performance saturation

## C02: SAPG achieves significantly higher asymptotic performance than PPO, DexPBT, and PQL on hard dexterous manipulation tasks
- **Statement**: On the AllegroKuka task suite (Regrasping, Throw, Reorientation, Two Arms Reorientation) evaluated after 2×10¹⁰ environment steps, SAPG achieves 12–66% higher success rates than DexPBT and near-zero improvements over PPO and PQL which fail entirely on hard tasks.
- **Status**: supported
- **Falsification criteria**: DexPBT or PPO matching SAPG's success counts at 2e10 samples would refute this. Any method achieving ≥35 successes on Reorientation with λ_ent=0 would refute the entropy benefit claim.
- **Proof**: [E02, E03]
- **Dependencies**: C01
- **Tags**: asymptotic performance, dexterous manipulation, AllegroKuka, hard tasks, SAPG vs baselines

## C03: Leader-follower aggregation outperforms symmetric aggregation for maintaining policy diversity
- **Statement**: The asymmetric leader-follower scheme (only leader receives off-policy data) consistently outperforms the symmetric scheme (each policy updated with all others' data) because symmetric aggregation causes policy convergence, eliminating data diversity.
- **Status**: supported
- **Falsification criteria**: Symmetric SAPG matching or exceeding leader-follower SAPG on ≥3 of 5 tasks would refute this claim.
- **Proof**: [E04]
- **Dependencies**: C01, C02
- **Tags**: leader-follower, symmetric aggregation, policy diversity, ablation

## C04: SAPG explores a more diverse state space than PPO during training
- **Statement**: States visited by SAPG during training have higher intrinsic dimensionality (higher PCA reconstruction error for the same number of components) and are harder to compress with small autoencoders (higher MLP reconstruction error) compared to states visited by PPO.
- **Status**: supported
- **Falsification criteria**: PCA or MLP reconstruction error being equal or lower for SAPG vs PPO across the measured range of components/hidden-layer sizes would refute this claim.
- **Proof**: [E05]
- **Dependencies**: C01
- **Tags**: exploration diversity, state coverage, PCA, MLP reconstruction, data diversity

## C05: Off-policy data from followers is essential for SAPG's performance gains
- **Statement**: Removing the off-policy update (running multiple policies independently without aggregation) significantly degrades performance compared to full SAPG on most tasks; the off-policy component is not merely decorative.
- **Status**: supported
- **Falsification criteria**: The no-off-policy ablation matching full SAPG performance on ≥3 tasks would refute this.
- **Proof**: [E04]
- **Dependencies**: C02
- **Tags**: off-policy correction, importance sampling, ablation, data aggregation

## C06: Entropy regularization of followers improves performance on harder exploration tasks
- **Statement**: Adding an entropy loss (H(π(a|s))) to follower policies with coefficient σ = 0.005 improves SAPG performance on the AllegroKuka Reorientation task (up to 16.5% over σ=0) but provides marginal or negative benefit on simpler tasks (AllegroHand, Regrasping, Throw).
- **Status**: supported
- **Falsification criteria**: σ=0 matching σ=0.005 on Reorientation, or σ=0.005 outperforming σ=0 on AllegroHand and Throw would refute the selective benefit claim.
- **Proof**: [E04, E06]
- **Dependencies**: C02, C03
- **Tags**: entropy regularization, exploration, diversity, hyperparameter sensitivity, follower policy
