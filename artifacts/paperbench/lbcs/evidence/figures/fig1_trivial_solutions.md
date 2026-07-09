# Figure 1: Trivial Solution Failure Modes (§2.1)
- **Source**: Figure 1, Section 2.1
- **Caption**: "Illustrations of phenomena of several trivial solutions discussed in §2.1. The experiment is based on (Zhou et al., 2022). The setup is provided in Appendix C.3. Here, k denotes the predefined coreset size before optimization."
- **Conditions**: MNIST-S subset; CNN with two blocks (Conv→Dropout→MaxPool→ReLU); inner loop: SGD lr=0.1, momentum=0.9, 100 epochs; outer loop: Adam lr=2.5, cosine scheduler; k∈{100,150,200,250}.

## Panel (a): f1(m) vs. outer iterations — Equation (3) only (min f1, no size term)
**Axis labels**: x = Iterations of the outer loop; y = f1(m)

| k | Behavior |
|---|---------|
| 100 | f1(m) decreases steadily from ~3.5 toward ~0.5 |
| 150 | f1(m) decreases steadily from ~3.5 toward ~0.5 |
| 200 | f1(m) decreases steadily from ~3.5 toward ~0.5 |
| 250 | f1(m) decreases steadily from ~3.5 toward ~0.5 |

**Key observation**: f1(m) can be effectively minimized (converges below 2.0) for all k values.

## Panel (b): f2(m) vs. outer iterations — Equation (3) only
**Axis labels**: x = Iterations of the outer loop; y = f2(m)

| k | Behavior |
|---|---------|
| 100 | f2(m) remains close to 100 throughout all iterations |
| 150 | f2(m) remains close to 150 throughout all iterations |
| 200 | f2(m) remains close to 200 throughout all iterations |
| 250 | f2(m) remains close to 250 throughout all iterations |

**Key observation**: Without explicit size optimization, f2(m) stays near the predefined k — size is not reduced.

## Panel (c): f1(m) vs. outer iterations — Equation (4) weighted combination (λ=0.5)
**Axis labels**: x = Iterations of the outer loop; y = f1(m)

| k | Behavior |
|---|---------|
| 100 | f1(m) remains large (>5.0) and fails to converge to acceptable values |
| 150 | f1(m) remains large (>5.0) |
| 200 | f1(m) remains large (>5.0) |
| 250 | f1(m) remains large (>5.0) |

**Key observation**: The weighted combination with λ=0.5 prioritizes f2 reduction at the expense of f1 — model performance is not satisfactory.

## Panel (d): f2(m) vs. outer iterations — Equation (4) weighted combination (λ=0.5)
**Axis labels**: x = Iterations of the outer loop; y = f2(m)

| k | Behavior |
|---|---------|
| 100 | f2(m) collapses rapidly toward 0 |
| 150 | f2(m) collapses rapidly toward 0 |
| 200 | f2(m) collapses rapidly toward 0 |
| 250 | f2(m) collapses rapidly toward 0 |

**Key observation**: f2 is minimized too aggressively (collapses to near 0), while f1 (panel c) is not optimized — contradicting the priority structure of RCS.
