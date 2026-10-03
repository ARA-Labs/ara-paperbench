# Experiments and proof obligations

These records distinguish paper-reported studies, mathematical checks and the single completed local reproduction. They are declarative; their exact inputs and outputs are in evidence.

## E01: Permutation calibration
- **Verifies**: [C01, C03]
- **Evidence**: [evidence/proofs/calibration.md](../evidence/proofs/calibration.md)
- **Run**: paper theorem and proof
- **Setup**: Examine pooled-data parameter selection under exchangeability.
- **Procedure**: Check that selection and normalization remain invariant under the same permutation group.
- **Metrics**: Conditional permutation rejection-probability bound at the declared null level, and exact invariance under the stated permutation action; no empirical null rejection estimate is supplied.
- **Expected outcome**: Null rejection control under the stated mathematical assumptions.
- **Baselines**: The mathematical fixed-statistic permutation test under identical exchangeability assumptions; no numerical baseline run.
- **Dependencies**: none

## E02: Fusion identity and normalized statistic
- **Verifies**: [C02, C03, C06]
- **Evidence**: [evidence/proofs/fusion.md](../evidence/proofs/fusion.md)
- **Run**: paper definitions and pinned mmdfuse.py
- **Setup**: Use the paper-defined statistic and the separately identified released implementation.
- **Procedure**: Compare the variational identity, normalizer and operation structure without conflating temperatures.
- **Metrics**: Equality of the log-integral exponential and divergence-regularized variational forms at an identical temperature; exact invariance of the concrete pooled normalizer; count of calibration stages.
- **Expected outcome**: The formal identity holds in its stated domain; source mismatches remain explicit.
- **Baselines**: Hard maximum, separately calibrated test aggregation and unnormalized fusion are structural alternatives, not locally measured ablations.
- **Dependencies**: none

## E03: Conditional power and concentration arguments
- **Verifies**: [C04, C05]
- **Evidence**: [evidence/proofs/power.md](../evidence/proofs/power.md)
- **Run**: paper appendices and theorem chain
- **Setup**: Apply every original boundedness, prior, permutation and moment assumption.
- **Procedure**: Trace concentration, coupling and variance results into the stated sufficient-power arguments.
- **Metrics**: The author-stated sufficient separation and type-II error bounds, including divergence and reciprocal-normalizer moment terms; all assumptions and proof dependencies are retained in the linked proof record.
- **Expected outcome**: The proposed guarantees apply only if their assumptions and proofs withstand review.
- **Baselines**: Concentrated versus spread posterior weight under the same kernel prior; these are conditional bound comparisons, not measured power differences.
- **Dependencies**: E01, E02

## E04: Mixture power comparisons
- **Verifies**: [C07]
- **Evidence**: [evidence/figures/figure1.md](../evidence/figures/figure1.md)
- **Run**: https://github.com/antoninschrab/mmdfuse-paper/blob/558e3999db1a2f6e3668b7539b48ef5ee3f09538/experiment_mixture.ipynb
- **Setup**: Use the author-defined mixture and comparison configurations.
- **Procedure**: Compare rejection behavior as the alternative and sample size vary.
- **Metrics**: Author-reported rejection proportions by mixture variance and sample size in Figure 1; whole-method differences are descriptive, with no reported contrast intervals or local mechanism ablation.
- **Expected outcome**: Adaptive collections can respond where a global median scale has low sensitivity.
- **Baselines**: MMD-Median, MMD-Split, MMDAgg, MMDAggInc, ACTT, CTT, ME, SCF, MMD-D and AutoML, with the exact author configurations and rows retained in Figure 1.
- **Dependencies**: none

## E05: Perturbed-uniform comparisons
- **Verifies**: []
- **Context**: Comparative background for C08, not direct support for its Galaxy-specific statement.
- **Evidence**: [evidence/figures/figure1.md](../evidence/figures/figure1.md)
- **Run**: https://github.com/antoninschrab/mmdfuse-paper/blob/558e3999db1a2f6e3668b7539b48ef5ee3f09538/experiment_perturbations.ipynb
- **Setup**: Use the author-defined perturbation samplers and baseline settings.
- **Procedure**: Vary perturbation and sample size using the original experiment scripts.
- **Metrics**: Author-reported rejection proportions by perturbation amplitude, dimension and sample size in Figure 1; original arrays are retained, but raw paired outcomes and contrast intervals are unavailable.
- **Expected outcome**: The named methods differ in sensitivity; no universal ranking is presumed.
- **Baselines**: MMD-Median, MMD-Split, MMDAgg, MMDAggInc, ACTT, CTT, ME, SCF, MMD-D and AutoML; use the perturbation-specific rows and settings in Figure 1.
- **Dependencies**: none

## E06: Galaxy comparisons
- **Verifies**: [C08]
- **Evidence**: [evidence/figures/figure1.md](../evidence/figures/figure1.md)
- **Run**: https://github.com/antoninschrab/mmdfuse-paper/blob/558e3999db1a2f6e3668b7539b48ef5ee3f09538/experiment_galaxy.ipynb
- **Setup**: Keep image-specific methods and the longer AutoML variant distinct.
- **Procedure**: Compare the reported corruption and sample-size sweeps without relabeling flattened and image-kernel methods.
- **Metrics**: Author-reported rejection proportions by Galaxy corruption and sample size in Figure 1; the image-kernel MMD-D minus MMD-FUSE contrast identifies the reported exception. Raw paired outcomes and contrast intervals are unavailable.
- **Expected outcome**: Learned image representations can differ from generic kernel rankings.
- **Baselines**: Image-specific MMD-D, MMDAgg, MMDAggInc, ACTT, CTT, SCF, MMD-Median, MMD-Split and the explicitly longer AutoML setting; ME is omitted in the Galaxy plot. Do not substitute synthetic MMD-D settings.
- **Dependencies**: none

## E07: CIFAR image-collection comparison
- **Verifies**: [C10]
- **Evidence**: [evidence/tables/table1.md](../evidence/tables/table1.md)
- **Run**: https://github.com/antoninschrab/mmdfuse-paper/blob/558e3999db1a2f6e3668b7539b48ef5ee3f09538/experiment_cifar.ipynb
- **Setup**: Use the specified image collections and retain the unresolved original outcome provenance.
- **Procedure**: Compare printed table values, released aggregates and source aggregation settings; no local rerun is represented.
- **Metrics**: Printed rejection proportions and exact released aggregate decimals for the CIFAR comparison in Table 1; denominator and averaging-path reconciliation remains incomplete, so no count-based uncertainty is calculated.
- **Expected outcome**: A reported difference does not imply verified raw rejection counts or broader dataset conclusions.
- **Baselines**: All thirteen named Table 1 tests are preserved, including MMDAgg, MMD-D, CTT, MMD-Median, ACTT, ME, AutoML, C2ST-L, C2ST-S, MMD-O, MMDAggInc and SCF alongside MMD-FUSE.
- **Dependencies**: none

## E08: Bandwidth-collection retention
- **Verifies**: [C05, C09]
- **Evidence**: [evidence/figures/figure7.md](../evidence/figures/figure7.md)
- **Run**: https://github.com/antoninschrab/mmdfuse-paper/blob/558e3999db1a2f6e3668b7539b48ef5ee3f09538/experiment_perturbations_vary_kernel.ipynb
- **Setup**: Use the declared perturbed-uniform setting and total-kernel count convention.
- **Procedure**: Inspect the released collection-size sweep and distinguish its data from the invalid saved plotting cell.
- **Metrics**: Descriptive rejection proportions at each total kernel count, and expanded-minus-starting contrasts referenced to the smallest retained collection in Figure 7. Raw cross-count outcomes, verified pairing and inferential noninferiority bounds are absent.
- **Expected outcome**: The retained point estimates describe the sweep; population-power retention remains a hypothesis requiring a prospective margin and valid uncertainty analysis.
- **Baselines**: MMD-FUSE against its own smallest retained collection for retention; MMDAgg is a separate method comparison and does not establish within-method noninferiority.
- **Dependencies**: none

## E09: Runtime and operation-count comparison
- **Verifies**: [C06]
- **Evidence**: [evidence/figures/figure8.md](../evidence/figures/figure8.md)
- **Run**: https://github.com/antoninschrab/mmdfuse-paper/blob/558e3999db1a2f6e3668b7539b48ef5ee3f09538/experiment_runtimes.ipynb
- **Setup**: Retain original hardware, warmup and per-method defaults; keep whole-run timing separate.
- **Procedure**: Inspect the source runtime arrays and the plotting provenance for both axes.
- **Metrics**: Author-reported mean and standard deviation of warmed per-test runtime in seconds, plus structural resampling-stage counts. Figure 8 retains separate sample-size and dimension arrays and the published RHS plotting defect.
- **Expected outcome**: The extra calibration stage has a structural cost; the published dimension panel cannot establish its intended trend.
- **Baselines**: The eleven named runtime methods in Figure 8, especially MMDAgg for the extra-calibration comparison; preserve each method default and distinguish warmed timings from local whole-run duration.
- **Dependencies**: none

## E10: Local implementation reproduction
- **Verifies**: [C11]
- **Evidence**: [evidence/results/local_run.md](../evidence/results/local_run.md)
- **Run**: src/execution/p1_mixture_point.py
- **Setup**: Use the immutable local protocol and unchanged author implementation.
- **Procedure**: Verify complete outcomes, source identities, process completion and the released aggregate comparison.
- **Metrics**: Complete binary rejection count, repetition coverage, aggregate agreement with the frozen interval, elapsed whole-container seconds, exit status, source/driver/protocol hashes and retained environment identities; exact values are in the local-run evidence.
- **Expected outcome**: The implementation point can reproduce without settling the paper-defined statistic.
- **Baselines**: The preregistered released MMD-FUSE notebook aggregate only. No independent method, null control or paper-formula execution was run.
- **Dependencies**: none

## E11: Paper and code correspondence audit
- **Verifies**: [C11]
- **Evidence**: [evidence/source_conflicts.md](../evidence/source_conflicts.md)
- **Run**: paper definition, pinned source and recorded algebra
- **Setup**: Keep mathematical notation, released code and run provenance independently attributed.
- **Procedure**: Derive the equal-group-size exponent and inspect source/plotting conflicts without correcting or rerunning them.
- **Metrics**: Symbolic equality or mismatch of paper and executed exponents for equal group sizes at the same declared temperature; source identity and plotting-variable correspondence. No statistical estimate is involved.
- **Expected outcome**: A documented non-equivalence blocks silent source substitution in future testing.
- **Baselines**: The paper-defined statistic and separately pinned released implementation; neither is silently substituted for the other.
- **Dependencies**: none

## E12: Registration target T-MF1
- **Verifies**: [C12]
- **Procedure**: Frozen released-code mixture n=m=500,d=2,sigma2=1.3, 200 repetitions and 2000 permutations per test; registered parent seed or within-group row ordering; diagnostic pooled label permutation.
- **Metrics**: rejection_proportion
- **Evidence**: [admission report](../evidence/admission/report.json) and [public closure](../evidence/admission/public-runs.zip)
- **Baselines**: Author-reported released-code value; no competing-method or paper-temperature comparison.
- **Run**: Frozen released driver in the captured public execution profile; generator families and all attempts are in the public closure.
- **Setup**: Same released implementation, generated mixture inputs and finite seed/row-order interventions; reference/control roles fixed before dispatch.
- **Expected outcome**: Treatment mean stays in the original engineering band while label permutation removes separation signal; a failed control blocks a target verdict.
