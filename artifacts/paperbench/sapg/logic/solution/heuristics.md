---
# Heuristics

## H01: Equal on/off-policy data ratio (50/50 split) for leader update
- **Rationale**: Off-policy gradients from follower data are noisier than on-policy gradients. Without subsampling, the larger off-policy dataset drowns out the more reliable on-policy signal. Equal ratio (λ=1 with subsampling so |D'| = |D₁|) balances the contribution of each.
- **Sensitivity**: high
- **Bounds**: Off-policy fraction = 50%; using 100% off-policy data (no subsampling) significantly degrades performance on AllegroHand and ShadowHand; lower off-policy fractions might be too conservative.
- **Code ref**: [src/execution/sapg.py]
- **Source**: §4.3, §6.3 (ablation: "SAPG (high off-policy ratio)")

## H02: KL-threshold-based adaptive learning rate
- **Rationale**: When the KL divergence between updated and old policy exceeds a threshold, the learning rate is reduced to prevent destructive updates. This is especially important with large batch sizes and combined on/off-policy gradients.
- **Sensitivity**: medium
- **Bounds**: KL threshold = 0.016 for all tasks; learning rate = 1e-4 (AllegroKuka) or 5e-4 (ShadowHand/AllegroHand)
- **Code ref**: [src/execution/sapg.py]
- **Source**: Appendix B (Tables 2, 3, 4)

## H03: Task-adaptive entropy coefficient selection
- **Rationale**: Hard exploration tasks (Reorientation, ShadowHand) benefit from follower exploration via entropy bonus. Simpler or more refine-exploit tasks (AllegroHand, Regrasping, Throw) do not benefit and may be hurt by excessive exploration.
- **Sensitivity**: medium
- **Bounds**: σ ∈ {0, 0.003, 0.005}; best σ=0 for AllegroHand/Regrasping/Throw; best σ=0.005 for ShadowHand/Reorientation. Select by grid search over the small set.
- **Code ref**: [src/execution/sapg.py]
- **Source**: §5.2, §6.3

## H04: Latent dimension sized by task complexity
- **Rationale**: More complex tasks (AllegroKuka with LSTM, high DoF, complex object dynamics) require larger hanging parameter vectors to differentiate policy behaviors meaningfully. Simpler tasks need less representational capacity.
- **Sensitivity**: low
- **Bounds**: ϕj ∈ R32 for AllegroKuka tasks (complex, LSTM policy); ϕj ∈ R16 for ShadowHand/AllegroHand (simpler, MLP policy)
- **Code ref**: [src/execution/policy.py]
- **Source**: §4.4

## H05: Gradient norm clipping
- **Rationale**: Combined on/off-policy gradients with importance sampling can exhibit occasional spikes in gradient magnitude. Gradient clipping prevents catastrophic updates.
- **Sensitivity**: low
- **Bounds**: Gradient norm clipped to 1.0 for all tasks.
- **Code ref**: [src/execution/sapg.py]
- **Source**: Appendix B (Tables 2, 3, 4)
