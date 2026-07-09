---
# Figure 7: PCA Reconstruction Error — State Diversity Analysis
- **Source**: Figure 7, §6.4
- **Caption**: "Curves comparing reconstruction error for states visited during training using top-k PCA components for SAPG (Ours), PPO and a randomly initialized policy"

## Axis Information
- **X-axis**: Number of PCA components k (range approximately 1 to 56–66)
- **Y-axis**: PCA reconstruction error (decreasing as k increases)
- **Methods**: SAPG (Ours), PPO, Random policy

## Metric Definition
Reconstruction error = ||X - X̂_k||^2 where X̂_k is the projection of state batch X onto the top-k PCA components. Higher error for a given k means the data varies along more dimensions (more diverse).

## Qualitative Findings (from §6.4 and figure description)

### Findings from paper text:
- "The rate of decrease in reconstruction error with an increase in components is the slowest for our method [SAPG]" — SAPG requires more components to explain the same variance
- SAPG has the highest reconstruction error for most values of k, indicating highest state diversity
- Random policy behavior: From paper text variations, exact ordering differs by task (see note)

### Two Tasks Reported (from rubric — separate PCA plots):
- **Task 1** (AllegroKuka-type, k range ≈1–66):
  - For k < 6: PPO has smallest error, random policy has highest error
  - For k > 6: SAPG has highest reconstruction error
  - For k > 25: All methods converge to similar error
  - PPO has smallest error for first few components (more structured/less diverse)
  - Random policy initially highest (uniformly random), SAPG overtakes as k grows

- **Task 2** (ShadowHand/AllegroHand-type, k range ≈1–56):
  - SAPG: highest reconstruction error for most k values
  - PPO: middle range
  - Random policy: smallest reconstruction error for most k (less structured state distribution)
  - All methods converge when k > 25

**Note**: Exact (s,a,r) data points for PCA curves are not provided in the paper text; the above are qualitative descriptions and approximate ranges from §6.4.
