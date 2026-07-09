# Figure 1: Trajectories for Trivial Solutions
- **Source**: Figure 1, Section 2.1
- **Caption**: "Illustrations of phenomena of several trivial solutions discussed in §2.1. The experiment is based on (Zhou et al., 2022). The setup is provided in Appendix C.3. Here, k denotes the predefined coreset size before optimization."
- **Experimental conditions**: MNIST subset (MNIST-S), CNN (two blocks of Conv2d+Dropout+MaxPool+ReLU). Inner loop: SGD, lr=0.1, momentum=0.9, 100 epochs. Outer loop: Adam, lr=2.5, cosine scheduler (following Zhou et al., 2022).

## Subfigure (a): f1(m) vs. outer iterations with Eq. (3) [only f1 in outer loop]

| Iteration | k=100 (approx) | k=150 (approx) | k=200 (approx) | k=250 (approx) |
|-----------|----------------|----------------|----------------|----------------|
| 0 | ≈3.5 | ≈3.5 | ≈3.5 | ≈3.5 |
| ~50 | ≈1.5 | ≈1.2 | ≈1.0 | ≈0.8 |
| ~100 | ≈1.0 | ≈0.9 | ≈0.7 | ≈0.5 |
| converged | ≈0.8 | ≈0.6 | ≈0.5 | ≈0.4 |

**Key finding**: f1(m) decreases effectively and settles at low values for all k; larger k → lower final f1.

## Subfigure (b): f2(m) vs. outer iterations with Eq. (3) [only f1 in outer loop]

| Iteration | k=100 | k=150 | k=200 | k=250 |
|-----------|-------|-------|-------|-------|
| 0 | ≈100 | ≈150 | ≈200 | ≈250 |
| converged | ≈100 | ≈150 | ≈200 | ≈250 |

**Key finding**: f2(m) stays near the predefined k throughout all iterations — coreset size is NOT reduced.

## Subfigure (c): f1(m) vs. outer iterations with Eq. (4) [weighted, λ=0.5]

| Iteration | k=100 (approx) | k=150 (approx) | k=200 (approx) | k=250 (approx) |
|-----------|----------------|----------------|----------------|----------------|
| 0 | ≈3.5 | ≈3.5 | ≈3.5 | ≈3.5 |
| converged | ≈3.0–5.0 | ≈3.0–5.0 | ≈3.0–5.0 | ≈3.0–5.0 |

**Key finding**: f1(m) fails to be minimized effectively under Eq. (4); values remain large.

## Subfigure (d): f2(m) vs. outer iterations with Eq. (4) [weighted, λ=0.5]

| Iteration | k=100 (approx) | k=150 (approx) | k=200 (approx) | k=250 (approx) |
|-----------|----------------|----------------|----------------|----------------|
| 0 | ≈100 | ≈150 | ≈200 | ≈250 |
| converged | ≈5–20 | ≈5–20 | ≈5–20 | ≈5–20 |

**Key finding**: f2(m) collapses dramatically toward near-zero under Eq. (4) with λ=0.5.

**Note**: Exact data point values are read approximately from the figure; marked with ≈ as they are extracted from a line plot rather than a table.
