# Claims

These are source-attributed claims and hypotheses, not declarations of paper-wide reproduction. “Supported” names the bounded logical/source evidence described in each block; it does not confer artifact admission, independent theory certification or live control validation.

## C01: Pooled invariance permits reuse of all observations
- **Statement**: Permutation-invariant parameter selection can reuse the pooled observations without sacrificing the null calibration of a permutation test.
- **Conditions**: Exchangeability under the null; parameter selection ignores the original sample labels; one fixed statistic rule is applied consistently to the permutation group. This is a mathematical statement, not a local finite-precision calibration result.
- **Sources**: [] — no quantitative values are asserted in this claim block; exact source values reside in its linked evidence.
- **Status**: supported
- **Provenance**: ai-suggested, compiled from the attributed paper/code/run sources
- **Falsification criteria**: A null example satisfying the complete invariance assumptions but exceeding the prescribed rejection level would challenge the claim.
- **Proof**: [E01]
- **Evidence basis**: The paper states and proves the permutation result; no local null experiment was run.
- **Dependencies**: []
- **Tags**: kernel-testing, source-attribution

## C02: Soft fusion has a divergence-regularized interpretation
- **Statement**: A soft maximum over kernel discrepancies corresponds to optimizing kernel weights subject to a divergence penalty from a prior.
- **Conditions**: The variational identity requires the stated integrability conditions and an unrestricted posterior absolutely continuous with respect to its prior. Restricted parametric posterior families are not silently equated with that unrestricted optimization. The temperature must be identified explicitly.
- **Sources**: [] — no quantitative values are asserted in this claim block; exact source values reside in its linked evidence.
- **Status**: supported
- **Provenance**: ai-suggested, compiled from the attributed paper/code/run sources
- **Falsification criteria**: Failure of the variational identity under its stated assumptions, or a statistic not matching it at the same temperature, would contradict the asserted equivalence.
- **Proof**: [E02]
- **Evidence basis**: Definition and dual form in the paper support the identity. The released-code temperature discrepancy is separately documented.
- **Dependencies**: []
- **Tags**: kernel-testing, source-attribution

## C03: A pooled normalizer can be shared across permutations
- **Statement**: A positive pooled permutation-invariant normalizer lets kernel discrepancies share a scale without recomputing the normalizer for each label permutation.
- **Conditions**: The normalizer is finite, positive and invariant for the chosen pooled sample. Degenerate kernels and floating-point equivariance are not certified. A power advantage over unnormalized fusion is not established by this statement.
- **Sources**: [] — no quantitative values are asserted in this claim block; exact source values reside in its linked evidence.
- **Status**: supported
- **Provenance**: ai-suggested, compiled from the attributed paper/code/run sources
- **Falsification criteria**: The conditional reuse implication would require a counterexample satisfying positivity, finiteness and invariance, not an example violating them. For the concrete paper construction, restrict to pooled kernel matrices with a finite positive off-diagonal squared sum and test exact equality under simultaneous row/column permutation. A violation refutes applicability of that construction; degenerate matrices and floating-point tolerances are separate implementation questions.
- **Proof**: [E01, E02]
- **Evidence basis**: The formal normalizer and source construction are inspectable; the paper leaves the normalized-versus-unnormalized power advantage theoretically open.
- **Dependencies**: [C01]
- **Tags**: kernel-testing, source-attribution

## C04: Power bounds charge adaptation through the kernel prior
- **Statement**: The paper proposes sufficient-power guarantees whose adaptation penalty depends on divergence from a fixed kernel prior.
- **Conditions**: All original power-theorem hypotheses apply: bounded kernels, comparable groups, a data-independent prior, a sufficiently rich permutation sample and finite divergence. The normalized theorem additionally needs its reciprocal-normalizer moment condition. Empirical pooled-data priors and the released temperature are not certified by these bounds.
- **Sources**: [] — no quantitative values are asserted in this claim block; exact source values reside in its linked evidence.
- **Status**: hypothesis
- **Provenance**: ai-suggested, compiled from the attributed paper/code/run sources
- **Falsification criteria**: A counterexample satisfying every stated hypothesis but violating the bound, or an invalid proof step that cannot be repaired under those hypotheses, would refute the proposed guarantee.
- **Proof**: [E03]
- **Evidence basis**: Theorems and proof dependencies are retained as author-stated evidence, not independently certified mathematics. Apparent proof-constant typography remains flagged.
- **Dependencies**: []
- **Tags**: kernel-testing, source-attribution

## C05: Distributed signal can reduce the adaptation penalty
- **Statement**: Signal spread across candidate kernels can reduce the divergence penalty in the paper’s sufficient condition compared with concentrating all weight on one kernel.
- **Conditions**: This is a conditional implication for the bound and a fixed prior, not a monotonicity guarantee for actual test power. The bandwidth-count experiment does not measure posterior divergence.
- **Sources**: [] — no quantitative values are asserted in this claim block; exact source values reside in its linked evidence.
- **Status**: hypothesis
- **Provenance**: ai-suggested, compiled from the attributed paper/code/run sources
- **Falsification criteria**: A violation of the stated divergence implication under the same prior/posterior assumptions would challenge this interpretation; actual monotonic power requires its own controlled experiment.
- **Proof**: [E03, E08]
- **Evidence basis**: The paper’s divergence discussion motivates this consequence; the reported dense-grid experiment is a qualitative complement rather than a proof of it.
- **Dependencies**: [C04]
- **Tags**: kernel-testing, source-attribution

## C06: One statistic avoids a separate multiplicity calibration
- **Statement**: Combining discrepancies into one statistic avoids the additional resampling stage used to calibrate an aggregation of separate tests.
- **Conditions**: This concerns algorithm structure under comparable kernel computation, not universal wall-clock speed. Original runtime defaults, hardware, warmup and the corrupted dimension-panel provenance must remain separate from the local whole-run duration.
- **Sources**: [] — no quantitative values are asserted in this claim block; exact source values reside in its linked evidence.
- **Status**: supported
- **Provenance**: ai-suggested, compiled from the attributed paper/code/run sources
- **Falsification criteria**: An operation-level audit showing the claimed additional multiplicity stage is still required by the defined fused test would refute this structural comparison.
- **Proof**: [E02, E09]
- **Evidence basis**: The source has one permutation-statistic stage; the paper gives the separate complexity comparison. The published runtime RHS is not accepted as dimension-scaling evidence.
- **Dependencies**: [C02]
- **Tags**: kernel-testing, source-attribution

## C07: Global distance scales can miss local mixture differences
- **Statement**: A global median distance can miss the local scale distinguishing well-separated mixture components.
- **Conditions**: The author-reported multimodal benchmark motivates an explanatory hypothesis. Whole-method comparisons do not isolate bandwidth selection or establish its causal role. The local run checks only a released-code aggregate and does not reproduce the baseline comparison.
- **Sources**: [] — no quantitative values are asserted in this claim block; exact source values reside in its linked evidence.
- **Status**: hypothesis
- **Provenance**: ai-suggested, compiled from the attributed paper/code/run sources
- **Falsification criteria**: A prospective mechanism test must hold the discrepancy statistic, normalization, calibration, data draws and permutation schedule fixed while varying only global-median versus prespecified local-scale bandwidth selection. Measure pooled and within-component distances. A simultaneous uncertainty interval excluding any positive local-scale rejection advantage in the named mixture regime would contradict the directional explanation; this isolating experiment has not been run.
- **Proof**: [E04]
- **Evidence basis**: The released mixture arrays establish the author-reported whole-method pattern. They motivate, but do not identify, the proposed bandwidth mechanism.
- **Dependencies**: []
- **Tags**: kernel-testing, source-attribution

## C08: Benchmark competitiveness is not uniform dominance
- **Statement**: In the reported Galaxy sample-size comparison, an image-specific learned kernel can exceed the rejection rate of a generic adaptive kernel collection.
- **Conditions**: Only the paper’s named synthetic and image settings are represented. Image-kernel and flattened-input methods differ; the longer AutoML setting is explicit. Missing raw vectors and unreplicated image experiments limit inference.
- **Sources**: [] — no quantitative values are asserted in this claim block; exact source values reside in its linked evidence.
- **Status**: hypothesis
- **Provenance**: ai-suggested, compiled from the attributed paper/code/run sources
- **Falsification criteria**: For the retained Galaxy sample-size points where image-kernel MMD-D exceeds MMD-FUSE, a source-aligned replication whose simultaneous upper uncertainty bounds for the learned-minus-fused rejection contrasts are all nonpositive would contradict this directional empirical exception. Fix the points, outcome pairing, interval procedure and coverage before new outcomes. No such inferential replication is present.
- **Proof**: [E06]
- **Evidence basis**: The Galaxy sample-size rows show an empirical exception to uniform dominance. The synthetic and CIFAR comparisons are contextual records, not proof of the Galaxy contrast or an inferential ranking.
- **Dependencies**: []
- **Tags**: kernel-testing, source-attribution

## C09: A denser kernel collection can retain power
- **Statement**: Adding bandwidths can retain power once useful scales are represented in the particular reported perturbation experiment.
- **Conditions**: Retention means noninferiority to the starting collection, not approximate constancy. The reported perturbed-uniform sweep supplies descriptive aggregates only; no inferential retention margin, verified cross-count outcome pairing or simultaneous uncertainty analysis is available. The count convention is resolved, but the saved plotting cell remains syntactically invalid.
- **Sources**: [] — no quantitative values are asserted in this claim block; exact source values reside in its linked evidence.
- **Status**: hypothesis
- **Provenance**: ai-suggested, compiled from the attributed paper/code/run sources
- **Falsification criteria**: Before any new retention test, identify the starting collection and expansion range, justify an acceptable loss margin independently of the observed curve, and fix valid outcome denominators, pairing and a simultaneous uncertainty rule. An upper bound for an expanded-minus-starting power contrast lying below the negative margin would refute noninferiority for that expansion. Improvement does not refute retention. Without those prospective choices this hypothesis is not an executable acceptance criterion.
- **Proof**: [E08]
- **Evidence basis**: The released proportions describe the observed sweep and resolve total versus per-family counts. They do not establish population-power noninferiority; missing raw outcomes and uncertainty remain unresolved.
- **Dependencies**: []
- **Tags**: kernel-testing, source-attribution

## C10: An image-collection comparison can detect distribution shift
- **Statement**: The reported image-collection test detects a difference between the specified image collections under its selected protocol.
- **Conditions**: Only the named image collections, preprocessing and reported test configurations. Original raw outcome vectors and exact denominator reconciliation are unavailable; there is no new local image-data evidence.
- **Sources**: [] — no quantitative values are asserted in this claim block; exact source values reside in its linked evidence.
- **Status**: hypothesis
- **Provenance**: ai-suggested, compiled from the attributed paper/code/run sources
- **Falsification criteria**: First reconcile the source averaging path, valid outcome denominators, preprocessing and image collections. A prospective source-aligned test must compare rejection probability with its declared null level using a prespecified uncertainty rule; an upper bound no greater than that level would contradict the claimed excess rejection. A demonstrated data/protocol mismatch would instead invalidate the attribution. No count-based precision is inferred from the current aggregate decimals.
- **Proof**: [E07]
- **Evidence basis**: The printed table and released aggregate strings are distinct evidence records; rounded values are not promoted into independently verified counts.
- **Dependencies**: []
- **Tags**: kernel-testing, source-attribution

## C11: Aggregate agreement does not establish formula alignment
- **Statement**: Agreement with an aggregate result can coexist with a mismatch between executed code and a stated mathematical statistic.
- **Conditions**: The verified released-code reproduction and the equal-group-size algebra documented here establish one bounded counterexample to treating agreement as identity. They do not reconstruct the authors’ original execution history or choose a future protocol.
- **Sources**: [] — no quantitative values are asserted in this claim block; exact source values reside in its linked evidence.
- **Status**: supported
- **Provenance**: ai-suggested, compiled from the attributed paper/code/run sources
- **Falsification criteria**: A source-aligned derivation showing equivalence at the same temperature up to a common positive scale, or invalidation of the documented aggregate match, would undermine this counterexample.
- **Proof**: [E10, E11]
- **Evidence basis**: The completed local output matches the released aggregate, while the implemented exponent differs from the paper-stated experimental exponent. Both are retained; issue #281 remains open.
- **Dependencies**: []
- **Tags**: kernel-testing, source-attribution

## C12: Attributed experimental target T-MF1
- **Statement**: T-MF1 evaluates robustness of the author-reported mixture-cell rejection proportion under the registered released-code seed and within-group row-order interventions.
- **Status**: hypothesis
- **Provenance**: ai-suggested derived experimental target, explicitly approved in the joint admission plan
- **Sources**: [E10] and author experiment_mixture.ipynb cell 6 first position; exact target and measured outcomes are in evidence/admission/report.json.
- **Falsification criteria**: The finite-family treatment mean falls outside the frozen engineering band after the matched label control passes. A failed control yields inconclusive.
- **Proof**: [E12]
- **Dependencies**: []
- **Tags**: experimental-target, released-code, T-MF1
- **Conditions**: Only the registered finite families under the released-code protocol; no baseline-method or paper-temperature comparison, no bootstrap and no external dataset. The verdict concerns the preregistered finite two-treatment mean, not every seed or unrestricted robustness.
- **Evidence basis**: Completed method-bound repository operations, complete per-repetition outcomes, satisfied protected label controls and independent copied public replay.
