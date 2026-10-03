# Concepts

## Two-sample level and power
- **Notation**: see the source formalization
- **Definition**: A test distinguishes equality of two sampling distributions; level limits null rejection and power describes rejection under an alternative.
- **Boundary conditions**: Exchangeability and the stated sampling design matter; an alternative power point is not a null control.
- **Related concepts**: kernel prior, permutation statistic, source correspondence

## Squared maximum mean discrepancy
- **Notation**: see the source formalization
- **Definition**: The squared RKHS distance between distribution mean embeddings; the paper uses an unbiased two-sample estimator.
- **Boundary conditions**: Characteristic kernels identify distribution equality; finite-sample power may favor a restricted representation.
- **Related concepts**: kernel prior, permutation statistic, source correspondence

## Unordered pooled sample
- **Notation**: see the source formalization
- **Definition**: A combined observation collection considered independently of original sample labels.
- **Boundary conditions**: Parameter learning must obey the required permutation invariance, including any randomness.
- **Related concepts**: kernel prior, permutation statistic, source correspondence

## Permutation quantile
- **Notation**: see the source formalization
- **Definition**: A reference distribution formed by applying a common statistic to group actions on the observations.
- **Boundary conditions**: The identity/original statistic and Monte Carlo permutation convention must be preserved.
- **Related concepts**: kernel prior, permutation statistic, source correspondence

## Kernel prior and posterior
- **Notation**: see the source formalization
- **Definition**: A prior weights a candidate kernel family; an optimized posterior trades discrepancies against divergence from that prior.
- **Boundary conditions**: The power theorems use fixed priors; empirical pooled-data priors have a different scope.
- **Related concepts**: kernel prior, permutation statistic, source correspondence

## Donsker–Varadhan duality
- **Notation**: see the source formalization
- **Definition**: A log exponential moment equals a divergence-penalized optimization over admissible distributions.
- **Boundary conditions**: Integrability and the admissible posterior class cannot be silently changed.
- **Related concepts**: kernel prior, permutation statistic, source correspondence

## Fused statistic
- **Notation**: see the source formalization
- **Definition**: A log-sum-exp combination of kernel discrepancies at an identified temperature.
- **Boundary conditions**: An outside positive scaling and an inside temperature change have different effects on permutation rankings.
- **Related concepts**: kernel prior, permutation statistic, source correspondence

## Pooled normalizer
- **Notation**: see the source formalization
- **Definition**: A permutation-invariant squared-kernel quantity used to normalize discrepancies.
- **Boundary conditions**: It must be positive and finite; mathematical and finite-precision properties are distinct.
- **Related concepts**: kernel prior, permutation statistic, source correspondence

## Mean kernel
- **Notation**: see the source formalization
- **Definition**: A kernel averaged over a kernel distribution.
- **Boundary conditions**: The paper’s rational-quadratic example and restricted-family argument retain their own assumptions.
- **Related concepts**: kernel prior, permutation statistic, source correspondence

## Adaptation penalty
- **Notation**: see the source formalization
- **Definition**: A divergence term measuring the cost of moving from a prior toward useful kernels.
- **Boundary conditions**: It describes a sufficient-bound tradeoff rather than a universal empirical monotonicity law.
- **Related concepts**: kernel prior, permutation statistic, source correspondence

## U-statistic and chaos bounds
- **Notation**: see the source formalization
- **Definition**: The paper uses coupling, moment-generating-function and bounded-difference arguments to control test statistics.
- **Boundary conditions**: Full theorem constants and hypotheses remain source-attributed and not independently certified.
- **Related concepts**: kernel prior, permutation statistic, source correspondence
