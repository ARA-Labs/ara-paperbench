---
type: algorithm
paper: nanogpt-speedrun
---

# Algorithm

## BoN Science Runner (Main Loop)

```
Input: workspace W (with template v_0), hint_level L, branch_factor N, iterations T, debug_prob p
Output: best version v* with lowest train_time where val_loss ≤ 3.28

1. Initialize: best_version ← v_0
2. For t = 1 to T:
   a. candidates ← []
   b. For i = 1 to N:
      - If random() < p AND exists buggy descendant of best_version:
          base ← most recent buggy version (for debugging)
      - Else:
          base ← best_version
      - hypothesis ← Ideator.generate(base.code, base.results, base.history, hints[L])
      - new_code ← Coder.edit(base.code, hypothesis, base.bug_history)
      - v_new ← Workspace.create_version(parent=base, code=new_code, hypothesis=hypothesis)
      - Submit v_new to SLURM: torchrun --nproc_per_node=8 train_gpt2.py
      - candidates.append(v_new)
   c. Wait for all SLURM jobs to complete
   d. For each v in candidates:
      - results ← parse_results(v.logs)
      - v.metrics ← {val_loss, train_time, n_steps}
      - v.outcome_summary ← Analyst.summarize(v.logs)
      - v.bug_depth ← 0 if results.valid else base.bug_depth + 1
   e. valid_candidates ← [v for v in candidates if v.val_loss ≤ 3.28]
   f. If valid_candidates:
      best_version ← argmin(v.train_time for v in valid_candidates)
3. Return best_version
```

## Muon Optimizer (Core Optimization, Record 3)

```
Input: model parameters θ, learning rates (lr_muon, lr_adam), momentum β
Output: updated parameters θ'

1. Partition parameters:
   - θ_2d ← {p ∈ θ : p.ndim ≥ 2}    # weight matrices
   - θ_1d ← {p ∈ θ : p.ndim < 2}     # biases, norms, embeddings

2. For θ_2d (OrthogonalNesterov):
   a. g ← ∇L(θ_2d)                    # gradient
   b. g ← g / max(1, ‖g‖_F / max_grad_norm)  # clip
   c. buf ← β * buf + g               # momentum buffer
   d. g_nesterov ← g + β * buf        # Nesterov lookahead
   e. G ← newton_schulz_5(g_nesterov) # orthogonalize via Newton-Schulz
   f. θ_2d ← θ_2d - lr_muon * G

3. For θ_1d (AdamW):
   Standard AdamW update with lr_adam

4. Return θ = θ_2d ∪ θ_1d
```

## Newton-Schulz Orthogonalization

```
Input: matrix G ∈ R^{m×n}, steps=5
Output: orthogonalized G̃ ≈ G(G^T G)^{-1/2}

1. G ← G / (‖G‖_F + eps)             # normalize to spectral norm < 1.86
2. Coefficients: a=3.4445, b=-4.7750, c=2.0315  # cubic convergence
3. For k = 1 to steps:
   A ← G @ G^T
   G ← a*G + b*(A @ G) + c*(A @ A @ G)
4. Return G
```

## Complexity

- **Per-iteration (BoN)**: O(N × T_train) GPU-hours, where T_train is the current training time and N is branch factor.
- **Total benchmark**: 20 records × 5 strategies × 4 models × multiple hint levels × 20 iterations × N branches.
- **Muon overhead vs AdamW**: Newton-Schulz adds ~5% compute per optimizer step (5 matrix multiplications per parameter group).
