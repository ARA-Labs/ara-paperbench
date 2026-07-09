# Constraints and Boundary Conditions

## Working Conditions

### W1: Class-Incremental Learning with Known Task Boundaries
- SEMA's task-oriented expansion assumes task boundaries are observable during training.
- The expansion decision (at most one adapter per layer per task) is tied to task granularity.
- **Violation impact**: Without task boundaries (online CL), the expansion could occur too frequently (per sample) or require a different trigger mechanism.

### W2: Frozen Pre-Trained ViT Backbone
- All ViT parameters must remain frozen. Only adapters, RDs, and routers are learnable.
- The method relies on the PTM providing stable, generalizable intermediate representations.
- **Violation impact**: Fine-tuning the ViT causes catastrophic forgetting and invalidates the RD-based distribution estimation.

### W3: Last 3 Transformer Layers for Expansion (Default)
- By default, only transformer layers 10, 11, 12 (0-indexed) of ViT-B/16 are eligible for expansion.
- Earlier layers exhibit similar representations across tasks and tend not to trigger expansion.
- **Violation impact**: Allowing expansion in early layers increases adapter count without proportional accuracy gains; restricting to <2 layers reduces plasticity.

### W4: At Most One Adapter Per Layer Per Task
- Expansion is task-oriented: a maximum of one adapter is added per eligible layer per task.
- This is consistent with the CIL setting where each task represents a coherent distribution.
- **Violation impact**: Multiple expansions per task would cause redundancy and training instability.

### W5: No Memory Rehearsal
- SEMA operates without any stored experience replay buffer.
- Forgetting is mitigated by freezing trained modules and using the router for knowledge reuse.
- **Violation impact**: Adding rehearsal would violate the design premise but would likely further improve performance.

## Known Limitations

### L1: Online CL Not Supported
- The current design requires task boundaries for the task-oriented expansion.
- Fully online CL (intra-task diversity) would require a continuously adaptive expansion trigger.

### L2: RD-Based Detection Relies on Task Distribution Homogeneity
- The z-score statistic assumes that reconstruction errors within a task are relatively homogeneous.
- Tasks with very high intra-task diversity may cause inconsistent expansion signals.

### L3: Single Expansion Per Layer Per Task
- For a task that spans very diverse sub-distributions, a single adapter per layer may be insufficient.
- The paper acknowledges this as a limitation and suggests future work on fully online dynamic expansion.

### L4: Router Forgetting Not Fully Eliminated
- While existing router columns are frozen when a new column is added, the softmax normalization means the distribution of weights over all adapters shifts as new columns are added.
- This can cause mild forgetting in the router (acknowledged in §3.4).

### L5: RD Dimensions Fixed at 128
- The hidden dimension of the autoencoder encoder is fixed at 128 (Fig. 13 ablation shows robustness over 16, 32, 64, 128 but this is the default used).
- Choosing a much smaller hidden dimension may reduce RD capacity.

## Hyperparameter Sensitivity

| Hyperparameter | Sensitivity | Safe Range |
|---|---|---|
| Expansion threshold τ | Low (for ImageNet-A) to Medium (VTAB) | 1.0–2.0 for ImageNet-A; 1.0–6.0 for VTAB |
| Number of expansion layers | Medium | 2–4 last layers |
| Adapter hidden dim r | Low | 16–48 (per ablations in §4.3) |
| RD hidden dim | Low | 16–128 (Fig. 13) |
| Learning rates | Medium | adapter LR=0.005, RD LR=0.01 (cosine annealing) |
