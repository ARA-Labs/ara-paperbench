---
# Figures 7 & 8: State Space Diversity Analysis

## Figure 7: PCA Reconstruction Error

- **Source**: Figure 7, Section 6.4
- **Caption**: "Curves comparing reconstruction error for states visited during training using top-k PCA components for SAPG (Ours), PPO and a randomly initialized policy"
- **X-axis**: Number of PCA components k
- **Y-axis**: Reconstruction error (variance unexplained)
- **Curves**: SAPG (Ours), PPO, Random policy
- **Interpretation**: Lower reconstruction error for same k = lower intrinsic dimensionality = less diverse states

### Key Finding (per paper §6.4):
"We find that the rate of decrease in reconstruction error with an increase in components is the slowest for our method [SAPG]."

SAPG has the highest reconstruction error for most component counts, indicating states span more principal components (higher intrinsic dimensionality).

### PCA Reconstruction Error — Relative Rankings by Task

| Task | k range | Highest error (most diverse) | Intermediate | Lowest error (least diverse) | Convergence point |
|------|---------|------------------------------|--------------|------------------------------|-------------------|
| Allegro Kuka Reorientation | 1–66 | SAPG (k < ≈25) | PPO | Random policy | k ≈ 25 |
| Allegro Kuka Regrasping | 1–56 | SAPG (k > ≈6); Random (k ≤ ≈6) | PPO | PPO (first few k) | k ≈ 25 |
| Allegro Kuka Throw | 1–56 | SAPG (most k) | PPO | Random policy (k < ≈25) | k ≈ 25 |

Note: Exact data point values not provided in paper; above are qualitative descriptions from §6.4 and figure visual descriptions.

---

## Figure 8: MLP Reconstruction Error

- **Source**: Figure 8, Section 6.4
- **Caption**: "Curves comparing reconstruction error for states visited during training using MLPs with varying hidden layer dimensions for SAPG (Ours), PPO and a randomly initialized policy"
- **X-axis**: Hidden layer dimension (8 to 64 neurons; 2-layer feedforward network)
- **Y-axis**: Training reconstruction error (L2 loss for input reconstruction)
- **Curves**: SAPG (Ours), PPO, Random policy
- **Interpretation**: Higher training error = harder to compress state distribution = more diverse

### Network Architecture (per §6.4 and reproduction rubric):
- Two-layer feedforward autoencoder
- Hidden layer sizes vary from 8 to 64 neurons
- Activation: ReLU
- Optimizer: Adam
- Loss: L2 reconstruction error

### Key Finding (per paper §6.4):
"We find that training error is consistently higher for our method compared to PPO across different hidden layer sizes."

### Allegro Kuka Reorientation (Fig 8, panel 1)
- SAPG and PPO: Similar reconstruction errors, both significantly higher than random policy
- Random policy: Much lower reconstruction error (less diverse state distribution)
- Trend: All methods show decreasing error with larger hidden layers; SAPG and PPO remain above random

### Allegro Kuka Regrasping (Fig 8, panel 2)
- SAPG and PPO: Similar high reconstruction errors
- Random policy: Much lower reconstruction error
- Indicates both trained policies explore diverse states relative to random

### Allegro Kuka Throw (Fig 8, panel 3)
- SAPG and PPO: Similar high reconstruction errors
- Random policy: Much lower reconstruction error
- Same pattern as other tasks

Note: Exact numeric data points not provided in paper; values are approximate descriptions from §6.4 and figure captions.
