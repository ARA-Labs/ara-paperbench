# Related Work

## RW01: Zhou et al., 2022 (Probabilistic Bilevel Coreset Selection)
- **DOI**: ICML 2022, pp. 27287–27302
- **Type**: baseline
- **Delta**:
  - What changed: LBCS replaces probabilistic reparameterization and policy gradient estimation with lexicographic black-box search; adds explicit coreset size minimization.
  - Why: Policy gradient (C samples per step) is more expensive; weighted combination of f1, f2 fails due to scale mismatch (§2.1).
- **Claims affected**: C01, C02, C03
- **Adopted elements**: Bilevel optimization framework; inner-loop loss L(m,θ); f1 evaluation on full data.

## RW02: Borsos et al., 2020 (Coresets via Bilevel Optimization)
- **DOI**: NeurIPS 2020, pp. 14879–14890
- **Type**: baseline
- **Delta**:
  - What changed: LBCS uses a more efficient black-box search (no per-example cost growth); adds lexicographic size minimization.
  - Why: Borsos et al. cost increases rapidly with coreset size per new example, making it intractable at larger scales.
- **Claims affected**: C01
- **Adopted elements**: Bilevel coreset selection paradigm; coreset mask formulation.

## RW03: Zhang et al., 2023b (LexiFlow — Targeted Hyperparameter Optimization with Lexicographic Preferences)
- **DOI**: ICLR 2023
- **Type**: imports
- **Delta**:
  - What changed: LBCS adapts LexiFlow to the coreset selection setting by removing optional input targets and adjusting the compromise from absolute to relative value.
  - Why: LexiFlow provides a ready-made lexicographic black-box optimizer with convergence guarantees.
- **Claims affected**: C01, C02, C03
- **Adopted elements**: LexiFlow algorithm (Algorithm 2), practical lexicographic relations, dynamic step-size and restart mechanisms.

## RW04: Paul et al., 2021 (EL2N and GraNd)
- **DOI**: NeurIPS 2021, pp. 20596–20607
- **Type**: baseline
- **Delta**:
  - What changed: LBCS does not use per-sample scoring; instead it uses bilevel optimization for joint performance-size optimization.
  - Why: Score-based methods fix coreset size and do not minimize it.
- **Claims affected**: C01
- **Adopted elements**: None; used as baselines.

## RW05: Xia et al., 2023 (Moderate Coreset)
- **DOI**: ICLR 2023
- **Type**: baseline
- **Delta**:
  - What changed: LBCS does not use class-center distance scoring; LBCS+Moderate variant initializes with Moderate and then runs LBCS refinement.
  - Why: Moderate selects examples near class center median, a complementary initialization strategy.
- **Claims affected**: C01, C02
- **Adopted elements**: Moderate coreset as initialization for LBCS+Moderate variant.

## RW06: Zheng et al., 2023 (CCS — Coverage-Centric Coreset Selection)
- **DOI**: ICLR 2023
- **Type**: baseline
- **Delta**:
  - What changed: CCS uses a coverage-based one-shot selection; LBCS iteratively optimizes via bilevel framework.
  - Why: CCS does not minimize coreset size.
- **Claims affected**: C01
- **Adopted elements**: None; used as baseline.

## RW07: Yang et al., 2023 (Influential Coreset / Dataset Pruning)
- **DOI**: ICLR 2023
- **Type**: baseline
- **Delta**:
  - What changed: Influential uses generalization influence function scores; LBCS uses bilevel optimization without explicit per-sample scoring.
  - Why: Influential scores are fixed after scoring; cannot minimize size jointly with performance.
- **Claims affected**: C01
- **Adopted elements**: None; used as baseline.

## RW08: Fishburn, 1975 (Axioms for Lexicographic Preferences)
- **DOI**: The Review of Economic Studies, 42(3):415–419
- **Type**: imports
- **Delta**:
  - What changed: LBCS applies lexicographic preference theory from economics to machine learning coreset selection.
  - Why: Provides formal justification for priority-ordered objectives.
- **Claims affected**: C03
- **Adopted elements**: Lexicographic relation definitions and reflexivity/transitivity properties.

## RW09: Dolan et al., 2003 (Local Convergence of Pattern Search)
- **DOI**: SIAM Journal on Optimization, 14(2):567–583
- **Type**: bounds
- **Delta**:
  - What changed: Condition 2 (Stable Moving) in LBCS is a standard assumption from local randomized search convergence theory.
  - Why: Provides the theoretical basis for the ε-convergence proof.
- **Claims affected**: C03
- **Adopted elements**: Stable moving condition structure used in convergence proof (Appendix B).

## RW10: Solis & Wets, 1981 (Minimization by Random Search Techniques)
- **DOI**: Mathematics of Operations Research, 6(1):19–30
- **Type**: bounds
- **Delta**:
  - What changed: The convergence analysis of LBCS follows the style of Solis & Wets randomized search analysis.
  - Why: Provides probabilistic convergence framework for randomized direct search.
- **Claims affected**: C03
- **Adopted elements**: Framework for probabilistic convergence of randomized search.
