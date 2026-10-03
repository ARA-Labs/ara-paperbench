# Method and source correspondence

**Source**: paper Definition 1 and section 6; pinned `mmdfuse.py` lines 193–216, individually linked in the [code index](../../src/artifacts.md); [full correspondence audit](../../evidence/source_conflicts.md).

The paper first chooses kernel parameters from the unordered pooled observations. It then evaluates each kernel discrepancy under a common permutation schedule, normalizes using a pooled quantity when required, and combines the discrepancies through a prior-weighted log-sum-exp. The permutation comparison yields the test decision.

For equal group size, write Q=n(n-1), U for unbiased squared MMD and S for the sum of squared off-diagonal pooled-kernel entries. The printed normalizer is Nhat=S/Q. The printed fused normalized statistic is `(1/lambda) log E_prior exp(lambda U/sqrt(Nhat))`. An overall positive scaling does not alter permutation ranks. Changing the coefficient inside the exponential can alter how kernels contribute.

The released implementation is represented separately. Its quadratic-form bracket equals Q U; after division by sqrt(S) and multiplication by sqrt(Q), the default code exponent is Q U/sqrt(Nhat). The paper’s stated experimental exponent is sqrt(Q) U/sqrt(Nhat). The source inspection establishes this distinction, not which code produced the authors’ historical figures. Both use the paper’s distinct-pair convention for diagonal exclusion.

The code selects Gaussian and Laplace bandwidths from pooled distances, with specific zero replacement, order-statistic and discretization conventions. These remain pinned implementation choices; they are not replaced with generic percentile calls. Code, exact configuration and source conflicts are linked through the artifact index and evidence layer.

The paper’s complexity argument distinguishes one permutation-calibration stage from a separate multiple-testing correction stage. The original complexity expressions and theorem statements remain in the source PDF and proof evidence. No new algorithm, correction, model-training API or unreported method is reconstructed here.
