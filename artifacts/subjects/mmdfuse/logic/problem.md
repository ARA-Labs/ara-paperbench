# Problem

## Observations
- Kernel-test power depends on the scale and representation used to compare samples. The reported mixture plots motivate the hypothesis that a pooled global distance can be poorly matched to within-component differences; whole-method comparisons do not isolate that mechanism. Source: Figure 1 and the released mixture arrays.
- Parameter selection using held-out observations sacrifices information, while repeating expensive selection for every permutation can be costly. Source: paper introduction and pooled-invariance argument.
- The completed implementation reproduction agrees with its released aggregate while its effective temperature differs from the printed experimental setting. Source: local run and correspondence audit.

## Gaps
- Select useful kernels while retaining valid permutation calibration.
- Combine several useful scales without a separate multiple-testing calibration stage.
- Keep reported empirical behavior, proof assumptions and executable source identity distinct.

## Key insight
The paper separates permutation-invariant parameter selection from divergence-regularized fusion of kernel discrepancies. Both use the pooled observations, but their mathematical assumptions must be checked independently from the released implementation.

## Assumptions
Exchangeability under the null, a common permutation-statistic rule, finite integrable quantities, appropriate prior restrictions for the power results, and source-specific execution provenance. These assumptions do not establish candidate admission or the project’s control gate.
