# System Architecture: Lexicographic Bilevel Coreset Selection (LBCS)

## Component Overview

LBCS consists of three interacting components: the **Inner Loop Trainer**, the **Outer Loop Optimizer (LexiFlow)**, and the **Mask Evaluator**.

```
Dataset D ──────────────────────────────────────────────┐
                                                         │
┌────────────────────────────────────────────────────────┼──────────────────────┐
│  OUTER LOOP (LexiFlow, T iterations)                   │                      │
│                                                         ▼                      │
│   Incumbent mask m* ──► Perturb: m+ = m* ± δu ──► Mask Evaluator            │
│                                                         │                      │
│             ┌───────────────────────────────────────────┘                      │
│             │  f1(m), f2(m)                                                    │
│             ▼                                                                   │
│   Lexicographic Compare (m+, m*, F_H) ──► Update m* if m+ dominates          │
│             │                                                                   │
│             └──────────────► Update history H, thresholds F̃*                 │
│                                                                                 │
│   Dynamic step-size δ, Random restarts if δ < δ_lower                        │
└─────────────────────────────────────────────────────────────────────────────────┘
                                         │
              ┌──────────────────────────┘
              │  Current mask m
              ▼
┌─────────────────────────────────────────┐
│  INNER LOOP (Neural Network Training)   │
│  θ(m) = argmin_θ L(m, θ)              │
│  L(m,θ) = Σ_i m_i ℓ(h(x_i;θ), y_i)  │
│  Optimizer: Adam, lr=0.001            │
└─────────────────────────────────────────┘
              │
              │  θ(m)
              ▼
┌────────────────────────────────────────────────────────────┐
│  MASK EVALUATOR                                             │
│  f1(m) = (1/n) Σ_i ℓ(h(x_i; θ(m)), y_i)  [full data]    │
│  f2(m) = ‖m‖₀                              [coreset size] │
└────────────────────────────────────────────────────────────┘
```

## Components

### Inner Loop Trainer
- **Purpose**: Given a mask m, trains a proxy network θ to convergence on the selected coreset.
- **Inputs**: Binary mask m ∈ {0,1}^n, dataset D, proxy network architecture
- **Outputs**: Trained parameters θ(m)
- **Optimizer**: Adam with lr=0.001 (F-MNIST, SVHN, CIFAR-10); SGD with lr=0.1, momentum=0.9 for the trivial solution experiment (Figure 1)
- **Acceleration**: Pre-train with random mask once, then fine-tune with updated masks; apply model sparsity if needed
- **Interaction**: Called by Mask Evaluator to compute f1(m); re-run at each outer iteration

### Mask Evaluator
- **Purpose**: Given trained θ(m), compute the two optimization objectives.
- **Inputs**: θ(m), full dataset D, mask m
- **Outputs**: Scalar f1(m) (full-data cross-entropy), scalar f2(m) (L0 norm of m)
- **Key design choice**: f1 is evaluated on the *full* dataset (not just the coreset), ensuring the coreset is representative
- **Interaction**: Feeds f1 and f2 to LexiFlow for comparison

### Outer Loop Optimizer (LexiFlow)
- **Purpose**: Iteratively update the incumbent mask m* using lexicographic comparisons over F(m) = [f1(m), f2(m)].
- **Inputs**: Objectives f1, f2; history set H; initial mask m0; step size δ_init; tolerance ε
- **Outputs**: Optimal mask m* after T iterations
- **Algorithm**: Randomized direct search — sample unit-sphere direction u, try m ± δu, accept if lexicographically better than current
- **Features**: Dynamic step-size decay (δ ← δ · √((t'+1)/(t+1))), random restart when δ < δ_lower
- **Interaction**: Uses Mask Evaluator to query f1, f2 for candidate masks; updates history H and thresholds F̃*

### Grouping Trick (Large-Scale Acceleration)
- **Purpose**: Reduce the number of mask variables for large datasets (e.g., ImageNet-1k).
- **Design**: Groups of G=100 examples share the same binary mask entry, reducing the search space from n to n/G dimensions.
- **Interaction**: Applied in outer loop to reduce LexiFlow search dimensionality
- **Used in**: ImageNet-1k experiments (§5.4)

## Key Design Choices

1. **Gradient-free outer loop**: The lexicographic objective is non-differentiable in the mask space; LexiFlow avoids this by using only pairwise comparisons.
2. **Separate proxy and evaluation networks**: The inner-loop proxy network (cheaper architecture) is used to guide coreset selection; a separate (potentially larger) network is trained on the final coreset for evaluation (e.g., ResNet-18 for CIFAR-10).
3. **Full-data evaluation of f1**: Ensures the coreset is validated against the entire training distribution, not just the selected subset.
4. **ε-relaxation of f1**: Prevents the algorithm from getting stuck optimizing f1 to the minimum at the expense of f2 reduction.
