# Problem Specification

## Observations

### O1: Fixed coreset size is the standard but limits practitioners
- **Statement**: All prior coreset selection methods fix the coreset size k before selection and optimize only for model performance on the fixed-size subset (Toneva et al. 2019, Paul et al. 2021, Borsos et al. 2020, Zhou et al. 2022).
- **Evidence**: Survey of related work in §1; the bilevel objective in Eq. (3) confirms no optimization of coreset size.
- **Implication**: Practitioners who lack a strong prior on the optimal k must either over-provision (wasting resources) or under-provision (degrading accuracy).

### O2: Minimizing a weighted combination of f1 and f2 fails due to scale mismatch
- **Statement**: Setting the outer objective to (1−λ)f1(m)+λf2(m) causes either f2 dominating (collapsing the coreset) when λ=0.5, or requiring intractable scale calibration when λ<0.5. The gradient norm of f2's term is √n (large), while that of f1 depends on data, network, and task simultaneously.
- **Evidence**: §2.1 gradient analysis (Appendix C.2); Figure 1(c)(d) show f2→0 and f1 remaining large under λ=0.5.
- **Implication**: Simple scalarization cannot capture the strict priority of model performance over coreset size.

### O3: Bilevel coreset selection (without size optimization) leaves coreset size at predefined k
- **Statement**: When the objective is only min f1(m) with inner-loop θ training (Eq. 3), f2(m) converges near the predefined k for all outer iterations.
- **Evidence**: Figure 1(a)(b); Section 2.1; reproduced using Zhou et al. (2022) with k∈{100,150,200,250} on MNIST-S.
- **Implication**: Without explicit size optimization, the coreset size never shrinks, even when smaller subsets could achieve the same performance.

### O4: Model overfitting in coreset selection is an unaddressed risk
- **Statement**: Existing bilevel methods (e.g., Zhou et al. 2022) drive f1(m) to the minimum, which can overfit to training noise and degrade generalization, especially under label corruption or class imbalance.
- **Evidence**: §5.3, Remark 2; Figures 2(a)(b); performance gap widens under 30% and 50% label noise.
- **Implication**: Allowing a controlled performance compromise ε on f1 can reduce overfitting and improve test accuracy.

## Gaps

### G1: No method addresses the RCS problem (minimal coreset size under accuracy constraint)
- **Statement**: No prior work jointly optimizes model accuracy and coreset size with a clear priority structure.
- **Caused by**: O1 — all methods fix k beforehand.
- **Existing attempts**: Borsos et al. (2020), Zhou et al. (2022) — bilevel coreset selection without size minimization.
- **Why they fail**: They optimize only f1(m); f2(m) remains fixed at k (O3).

### G2: Lexicographic multi-objective optimization has not been applied to coreset selection
- **Statement**: While bilevel multi-objective optimization exists (Deb & Sinha 2010), no prior work applies it to coreset selection with a priority structure over objectives.
- **Caused by**: O1, O2 — the community has not recognized the need for priority-based joint optimization.
- **Existing attempts**: Weighted combination (Eq. 4).
- **Why they fail**: Scale mismatch and inability to represent strict lexicographic preferences as weights (Shi et al. 2020) (O2).

## Key Insight

- **Insight**: The two objectives f1(m) (model performance) and f2(m) (coreset size) have a strict lexicographic ordering — f1 must be "good enough" (within ε of its optimum) before f2 is minimized. This ordering can be implemented via a black-box randomized direct search that uses pairwise lexicographic comparisons of masks instead of gradient-based updates, requiring no analytic gradient of the combinatorial mask space.
- **Derived from**: O1, O2, O3 — the failure of existing approaches reveals the need for gradient-free, priority-aware search.
- **Enables**: LBCS: a tractable algorithm that provably converges to the ε-optimal coreset size while maintaining model performance.

## Assumptions

- A1: The dataset D is labeled and i.i.d. sampled from some distribution; cross-entropy loss is appropriate.
- A2: The inner loop can be trained to convergence (or near-convergence) to obtain a reliable θ(m) for evaluating f1(m).
- A3: The progressable condition (Condition 1) holds by construction of the lexicographic update rule.
- A4: The stable moving condition (Condition 2) holds for the LexiFlow randomized search over the mask space.
- A5: The performance compromise ε is non-negative and set by the user (default ε=0.2 in experiments).
