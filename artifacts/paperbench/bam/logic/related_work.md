# Related Work

## RW01: Modi et al., 2023
- **DOI**: NeurIPS 2023 (Advances in Neural Information Processing Systems, 36)
- **Type**: extends
- **Delta**:
  - What changed: BaM generalizes GSM by optimizing a proper score-based divergence with KL regularization, instead of solving exact score-matching equations. BaM recovers GSM as the B=1, λ→∞ limiting case.
  - Why: GSM lacks a proper divergence objective, uses ad hoc batch averaging, and diverges on highly non-Gaussian targets.
- **Claims affected**: C03, C04, C05, C06
- **Adopted elements**: Full-covariance Gaussian variational family; iterative score-matching framework; closed-form update structure.

## RW02: Kucukelbir et al., 2017
- **DOI**: Journal of Machine Learning Research (ADVI paper)
- **Type**: baseline
- **Delta**:
  - What changed: BaM replaces stochastic ELBO gradient optimization (ADAM) with closed-form proximal score-based divergence optimization.
  - Why: ELBO gradients have high variance; convergence is sensitive to learning rate; no closed-form updates available.
- **Claims affected**: C05, C06
- **Adopted elements**: Full-covariance Gaussian VI paradigm; reparameterization trick (used in ADVI baseline but not BaM).

## RW03: Asi and Duchi, 2019
- **DOI**: SIAM Journal on Optimization, 29(3):2257-2290
- **Type**: imports
- **Delta**:
  - What changed: BaM adapts stochastic proximal point (SPP) ideas to VI with a KL regularizer (instead of Euclidean distance) and exploits Gaussian family structure for closed-form solutions.
  - Why: SPP methods are stable with respect to learning rate; BaM inherits this robustness (Theorem 3.1 holds for all λ>0).
- **Claims affected**: C02, C04
- **Adopted elements**: SPP framework of minimizing stochastic estimate of objective + regularizer; stability analysis approach.

## RW04: Hyvärinen, 2005
- **DOI**: Journal of Machine Learning Research, 6(4)
- **Type**: imports
- **Delta**:
  - What changed: BaM uses a Cov(q)-weighted variant of score matching (making it affine invariant) rather than the standard Fisher divergence, and applies it to VI rather than density estimation.
  - Why: Standard Fisher divergence is not affine invariant; VI requires dealing with unnormalized targets.
- **Claims affected**: C01
- **Adopted elements**: Score matching principle; connection between score agreement and density estimation.

## RW05: Barp et al., 2019
- **DOI**: NeurIPS 2019 (Advances in Neural Information Processing Systems, 32)
- **Type**: bounds
- **Delta**:
  - What changed: BaM's score-based divergence is a special case of the weighted Fisher divergence with M = Cov(q) (data-dependent weighting), which enables affine invariance.
  - Why: BaM needs M to adapt to the variational distribution for affine invariance; fixed M does not achieve this.
- **Claims affected**: C01
- **Adopted elements**: Weighted Fisher divergence framework; minimum Stein discrepancy perspective.

## RW06: Kingma and Welling, 2014
- **DOI**: ICLR 2014
- **Type**: baseline
- **Delta**:
  - What changed: BaM proposes closed-form updates instead of gradient-based ELBO optimization for Gaussian VI.
  - Why: Gradient-based VI is used in VAE training but is sensitive to hyperparameters and converges slowly for posterior inference.
- **Claims affected**: C05
- **Adopted elements**: Variational autoencoder framework; amortized inference baseline for Section 5.3.

## RW07: Theis and Hoffman, 2015
- **DOI**: ICML 2015
- **Type**: extends
- **Delta**:
  - What changed: BaM uses score-based divergence as its objective and obtains a fully closed-form solution; Theis & Hoffman use ELBO with KL regularizer and alternating coordinate ascent (not closed-form).
  - Why: Linearization in Theis & Hoffman introduces approximation error.
- **Claims affected**: C02, C04
- **Adopted elements**: KL divergence as regularizer in proximal VI; trust-region interpretation.

## RW08: Khan et al., 2015 and 2016
- **DOI**: NeurIPS 2015; UAI 2016
- **Type**: refutes
- **Delta**:
  - What changed: BaM achieves closed-form Gaussian updates without linearizing difficult terms and without requiring additional structural knowledge of the target.
  - Why: Khan et al.'s linearization introduces approximation error; BaM solves the full quadratic exactly.
- **Claims affected**: C02
- **Adopted elements**: KL-proximal variational inference concept; Gaussian variational family.

## RW09: Lambert et al., 2022
- **DOI**: NeurIPS 2022 (Advances in Neural Information Processing Systems, 35)
- **Type**: extends
- **Delta**:
  - What changed: BaM uses KL divergence as regularizer (yielding closed-form solution); Lambert et al. use Wasserstein metric as regularizer (no closed-form solution for proximal step).
  - Why: KL regularizer for Gaussians admits quadratic matrix equation with known closed-form solution.
- **Claims affected**: C02
- **Adopted elements**: Proximal Gaussian VI framework; Wasserstein-inspired motivation.

## RW10: Davis and Drusvyatskiy, 2019
- **DOI**: SIAM Journal on Optimization, 29(1):207-239
- **Type**: imports
- **Delta**:
  - What changed: BaM adapts stochastic model-based minimization to the VI setting with Gaussian family structure.
  - Why: General SPP theory provides theoretical backing for stability; BaM exploits specific structure for closed-form solutions.
- **Claims affected**: C04
- **Adopted elements**: Theoretical convergence framework for stochastic proximal methods.

## RW11: Yu and Zhang, 2023
- **DOI**: ICLR 2023
- **Type**: refutes
- **Delta**:
  - What changed: BaM uses Gaussian family with affine-invariant score-based divergence and closed-form updates; Yu & Zhang use semi-implicit family with Fisher divergence and stochastic gradient.
  - Why: BaM's Gaussian family and affine-invariant divergence enable analytical optimization.
- **Claims affected**: C01, C02
- **Adopted elements**: Score-matching approach to VI.

## RW12: Diao et al., 2023
- **DOI**: ICML 2023
- **Type**: extends
- **Delta**:
  - What changed: BaM uses score-based divergence with KL regularizer (not forward KL with Wasserstein metric as in Diao et al.) but both achieve closed-form Gaussian updates.
  - Why: Different divergence and regularizer choices; BaM recovers GSM as special case.
- **Claims affected**: C02
- **Adopted elements**: Forward-backward Gaussian VI with closed-form proximal steps.
