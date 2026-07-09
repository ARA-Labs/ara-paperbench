# Related Work

## RW01: Papamakarios & Murray, 2016 (SNPE-A)
- **DOI**: NeurIPS 2016 proceedings
- **Type**: baseline
- **Delta**:
  - What changed: NPSE replaces normalizing flow posterior estimator with conditional score-based diffusion model; TSNPSE analogises SNPE-A's post-hoc SIR correction as SNPSE-A.
  - Why: Avoid architectural restrictions of normalizing flows; do not require importance weight corrections.
- **Claims affected**: C01, C02
- **Adopted elements**: Sequential training concept; proposal prior idea; SIR correction (adapted as SNPSE-A).

## RW02: Lueckmann et al., 2017 (SNPE-B)
- **DOI**: NeurIPS 2017 proceedings
- **Type**: baseline
- **Delta**:
  - What changed: NPSE avoids the high-variance importance-weighted loss of SNPE-B; SNPSE-B is the score-based analogue.
  - Why: Importance weights in DSM loss are high-variance and lead to unstable training.
- **Claims affected**: C03
- **Adopted elements**: Importance-weighted objective concept (adapted as SNPSE-B).

## RW03: Greenberg et al., 2019 (SNPE-C / APT)
- **DOI**: ICML 2019 proceedings
- **Type**: baseline
- **Delta**:
  - What changed: SNPSE-C is the score-based analogue of SNPE-C; TSNPSE avoids the score-space correction that SNPSE-C requires.
  - Why: Score-based correction requires additional approximations that degrade performance.
- **Claims affected**: C02, C03
- **Adopted elements**: Automatic posterior transformation concept (partially adapted as SNPSE-C).

## RW04: Deistler et al., 2022a (TSNPE)
- **DOI**: NeurIPS 2022 proceedings
- **Type**: baseline
- **Delta**:
  - What changed: TSNPSE replaces normalizing flow with conditional score network; retains the truncated proposal idea.
  - Why: Diffusion models are more flexible than discrete normalizing flows; CNFs may give more accurate inference on hard tasks.
- **Claims affected**: C02, C04
- **Adopted elements**: Truncated prior proposal; HPR estimation procedure; pre-rejection hypercube heuristic; Pyloric experimental setup.

## RW05: Song et al., 2021 (Score-Based Generative Modelling via SDEs)
- **DOI**: ICLR 2021 (arXiv:2011.13456)
- **Type**: imports
- **Delta**:
  - What changed: Applied to the conditional posterior estimation problem in SBI rather than unconditional generation.
  - Why: Score-based diffusion provides a flexible, training-stable alternative to normalizing flows.
- **Claims affected**: C01, C02, C05
- **Adopted elements**: SDE framework; VE/VP SDE definitions; probability flow ODE; denoising score matching; sinusoidal embeddings.

## RW06: Batzolis et al., 2021 (Conditional Score-Based Diffusion)
- **DOI**: arXiv:2111.13606
- **Type**: imports
- **Delta**:
  - What changed: Applied conditional score diffusion to SBI where the likelihood is intractable.
  - Why: Standard conditional diffusion assumes known or tractable likelihood.
- **Claims affected**: C01
- **Adopted elements**: Conditional DSM objective derivation; equivalence proof between J^SM_post and J^DSM_post.

## RW07: Geffner et al., 2023 (Compositional Score Modeling for SBI)
- **DOI**: ICML 2023 proceedings
- **Type**: extends
- **Delta**:
  - What changed: Geffner et al. focus on multi-observation SBI using compositional scores; this paper introduces sequential variants.
  - Why: Different scope — sequential vs. multi-observation generalisation.
- **Claims affected**: C01
- **Adopted elements**: Motivation for applying diffusion models to SBI; comparison basis.

## RW08: Dax et al., 2023 (FMPE — Flow Matching)
- **DOI**: NeurIPS 2023 proceedings
- **Type**: extends
- **Delta**:
  - What changed: NPSE using the deterministic probability flow ODE is a special case of FMPE; TSNPSE provides a sequential variant which FMPE lacks.
  - Why: FMPE is amortised only; sequential variant is needed for simulation efficiency.
- **Claims affected**: C01, C02
- **Adopted elements**: CNF perspective; comparison in Appendix F.

## RW09: Papamakarios et al., 2019 (SNLE)
- **DOI**: AISTATS 2019 proceedings
- **Type**: baseline
- **Delta**:
  - What changed: NPSE targets the posterior score directly rather than learning an approximate likelihood for MCMC.
  - Why: SNLE requires MCMC for sampling, which is costly for complex posteriors.
- **Claims affected**: C01
- **Adopted elements**: Sequential SBI framework; benchmark comparison.

## RW10: Durkan et al., 2020 (SNRE)
- **DOI**: ICML 2020 proceedings
- **Type**: baseline
- **Delta**:
  - What changed: NPSE does not require binary classification / ratio estimation.
  - Why: Ratio estimation is an indirect approach; direct score estimation is more principled.
- **Claims affected**: C01
- **Adopted elements**: Sequential SBI framework.

## RW11: Lueckmann et al., 2021 (sbibm benchmark)
- **DOI**: AISTATS 2021 proceedings
- **Type**: bounds
- **Delta**:
  - What changed: Uses sbibm as evaluation framework; benchmark tasks and C2ST metric defined there.
  - Why: Standard evaluation protocol for fair comparison.
- **Claims affected**: C01, C02, C03
- **Adopted elements**: 8 benchmark tasks; C2ST metric; sbibm toolkit for baselines.

## RW12: Benton et al., 2024 (Error Bounds for Flow Matching)
- **DOI**: Transactions on Machine Learning Research, 2024
- **Type**: imports
- **Delta**:
  - What changed: Theorem A.3 adapts Benton et al. Theorem 6 to the conditional posterior score estimation setting.
  - Why: Provides theoretical grounding for NPSE's approximation error.
- **Claims affected**: C01
- **Adopted elements**: Wasserstein-2 error bound framework; assumptions A1–A4.

## RW13: Glöckler et al., 2022 (SNVI)
- **DOI**: ICLR 2022 proceedings
- **Type**: baseline
- **Delta**:
  - What changed: TSNPSE compared directly against SNVI on Pyloric problem.
  - Why: SNVI is a competitive recent method for the Pyloric neuroscience experiment.
- **Claims affected**: C04
- **Adopted elements**: Pyloric experimental setup; comparison metric (% valid summary statistics).

## RW14: Hyvarinen, 2005 (Score Matching)
- **DOI**: JMLR 6:695-709, 2005
- **Type**: imports
- **Delta**:
  - What changed: Uses denoising score matching (Vincent 2011; Song et al., 2020) rather than explicit score matching.
  - Why: Denoising score matching is tractable without requiring density normalisation.
- **Claims affected**: C01
- **Adopted elements**: Score matching principle as the foundation of the DSM objective.
