---
# Benchmark C2ST: All Conditional Distributions

- **Source**: Figure 4b, Section 4.1
- **Caption**: "C2ST between arbitrary Simformer-conditional distributions and their ground truth" for Tree, HMM, Two Moons, SLCP tasks.
- **Conditions**: VESDE; 100 randomly selected conditional distributions per task; MCMC ground truth via HMC (5000 steps) for Tree/HMM, slice+MHMCMC for Two Moons/SLCP. 6-layer Simformer.

**Note**: Values are approximate (≈) extracted from Figure 4b. Paper does not provide a numerical table.

| Task | Method | 10³ sims C2ST | 10⁴ sims C2ST | 10⁵ sims C2ST |
|------|--------|---------------|---------------|---------------|
| Tree | Simformer (dense) | ≈0.80 | ≈0.65 | ≈0.58 |
| Tree | Simformer (undirected) | ≈0.78 | ≈0.62 | ≈0.56 |
| Tree | Simformer (directed) | ≈0.75 | ≈0.60 | ≈0.55 |
| HMM | Simformer (dense) | ≈0.85 | ≈0.70 | ≈0.60 |
| HMM | Simformer (undirected) | ≈0.80 | ≈0.65 | ≈0.58 |
| HMM | Simformer (directed) | ≈0.75 | ≈0.62 | ≈0.56 |
| Two Moons | Simformer (dense) | ≈0.78 | ≈0.62 | ≈0.55 |
| Two Moons | Simformer (undirected) | ≈0.78 | ≈0.62 | ≈0.55 |
| Two Moons | Simformer (directed) | ≈0.78 | ≈0.62 | ≈0.55 |
| SLCP | Simformer (dense) | ≈0.85 | ≈0.70 | ≈0.58 |
| SLCP | Simformer (undirected) | ≈0.80 | ≈0.65 | ≈0.56 |
| SLCP | Simformer (directed) | ≈0.75 | ≈0.62 | ≈0.55 |

**Key finding from paper text**: "Despite the complexity of these tasks, Simformer was able to accurately model all conditionals across all tasks." All Simformer models achieve C2ST below 0.7 at 10⁵ simulations across all tasks.
