# Source conflicts and newly resolved questions

Paths prefixed `official/` refer to the immutable upstream repository, linked individually in [the code index](../src/artifacts.md). Formula-crop filenames below resolve in this evidence directory.

**Source**: paper Definition 1/section 6; immutable author sources; prior source-inspection report.

## 5. Source discrepancies, missing verification, and later source-choice decisions

### 5.1 Demonstrated algebraic mismatch: printed temperature versus pinned implementation

Relevant exact visual sources:

- `definition1-normalizer-page6.png`: PDF page6, crop `(105,530,510,690)` PDF points, 220dpi. The normalizer is `Nhat_k = S/[n(n-1)]`, with `S = sum_{i != j} K_ij^2`, and exponent `lambda * U / sqrt(Nhat_k)`, where `U` is unbiased squared MMD.
- `experiment-lambda-page8.png`: PDF page8, crop `(105,390,510,480)` PDF points, 220dpi. §6 explicitly states `lambda = sqrt(n(n-1))` for MMD-FUSE-N.
- `official/mmdfuse.py:193` sets `unscaled_std = jnp.sqrt(jnp.sum(K**2))`, after diagonal zeroing at line191. Lines199–212 form the quadratic expression and multiply by `jnp.sqrt(n * (n - 1))`. Line216 feeds it to `logsumexp(lambda_multiplier * M, axis=0, b=1 / N)`.

Diagonal check: p3 defines the subscript notation `[n]_2` as ordered pairs of distinct indices, unlike Cartesian `[n]^2`. Definition1 uses `[n+m]_2`, so its normalizer excludes diagonals just as code line191 does. This was verified visually in `distinct-pairs-definition-page3.png` (p3, crop `(105,412,510,452)`, 220dpi). Thus the algebra below uses the same off-diagonal sum; no additional diagonal-normalization discrepancy is asserted.

For equal sizes `m=n=s`, let `A=sum K_XX`, `D=sum K_YY` (diagonals zero), `C=sum K_XY` (one rectangular block), and `Q=s(s-1)`. For the original assignment (and identically for each permuted assignment), the three quadratic forms in the source are:

```
V10' K V10 = A
V01' K V01 = D
V11' K V11 = A + D - 2C
U = (A+D)/[s(s-1)] - 2C/s^2
```

The source coefficients from lines199–209 reduce to:

```
(A / s) + (D / s) + ((s-1)/s)*(A+D-2C)
= A + D - 2*(s-1)*C/s
= Q * U.
```

Consequently line211–212's row of `M` is:

```
M_code = (Q*U)/sqrt(S) * sqrt(Q)
       = Q*U / sqrt(Nhat).
```

The effective exponent at `lambda_multiplier=1` is therefore `Q*U/sqrt(Nhat)`. In contrast the paper's stated experimental exponent is `sqrt(Q)*U/sqrt(Nhat) = Q*U/sqrt(S)`. Their ratio inside the exponent is `sqrt(Q)`, provided the term is nonzero. At the executed sample size, `Q=500*499=249500` (a derived input quantity, not measured output).

This distinction cannot be dismissed as the omitted common outside factor `1/lambda`: multiplying the final statistic by a positive common constant preserves permutation ranks, but changing the coefficient *inside* log-sum-exp changes the relative contribution of kernels and need not preserve ranks. The docstring at `mmdfuse.py:54–55` and the code comment at195 also say lambda is proportional to `sqrt(n(n-1))`; they do not explain the extra factor in the implemented algebra. This is a source-level method-fidelity discrepancy, not evidence that the unchanged author-code rerun failed.

**Later decision:** for a broader executable method description, preserve the paper formula and author implementation separately, and ask which protocol is intended for future testing. The present frozen run is of the pinned author's implementation and notebook, and must remain so. Do not patch its source, retroactively change the protocol, or state that matching the author output proves execution of the printed temperature. Root independently checked the printed normalizer/temperature and the extra exponent factor; this preflight still leaves any future source-choice or artifact-admission decision separate.

### 5.2 Demonstrated implementation detail omitted from paper: bandwidth quantiles

The paper §6/A.2 describes a uniform discretization between half the fifth percentile and twice the ninety-fifth percentile of pooled distances. The code takes the upper triangle including the diagonal (`mmdfuse.py:180`), replaces zero distances by the median (`:172–174`), uses floor-index order statistics (`:175–176`), then `linspace` (`:177`). This is more specific than the prose; exact equality to any generic percentile implementation is not established. It remains permutation invariant for this pooled construction. This is an implementation convention to disclose, not proof of failed calibration. On degenerate all-identical inputs the zero-median path offers no explicit epsilon safeguard; no such degenerate input was run here and no generic robustness claim is justified.

### 5.3 Demonstrated plotting-source contradiction: Figure8 RHS

`figures.ipynb` cell14, “Plot0”, loads sample-size arrays into `time_mean`, `time_std`, `time_mean_autotst`, `time_std_autotst`. “Plot1” loads dimension means into variables `power` and `power_autotst`, but calls `errorbar` with the unchanged sample-size `time_mean`/`time_std` and AutoML counterparts. It does not load dimension standard deviations. The PDF's right-panel curves visibly duplicate the left-panel shape/magnitude pattern (ME drops its last point), consistent with this code. This demonstrates that the supplied plotting cell does not implement its claimed dimension-results provenance. The original PDF generation process is not independently reconstructed, so say “consistent with” rather than claiming a proved byte-identical generation chain.

**Later decision:** preserve the published Figure8 verbatim and flag its RHS; do not treat the RHS as independently grounded dimension-scaling evidence. A corrected plot would be a derived/corrected figure requiring the original dimension arrays and experiment source, separately attributed. No correction or author contact was performed.

### 5.4 CIFAR rounded power versus unverified denominator

The paper Table1 reports FUSE0.937, and p10 explicitly interprets that as937 out of1000. Retained plotting cell16 instead prints FUSE`0.9366197`, MMDAggInc`0.28077313`, AutoML`0.5438067`, and MMD-Median`0.67800003`. These round to the printed table precision but do not, by themselves, establish the exact counts/denominators described in the paper. For example, `0.9366197` is not ordinary floating roundoff of937/1000; a different original denominator or averaging path is possible. Neither is supplied, and none should be inferred from decimal arithmetic. This is a demonstrated difference in source strings plus missing provenance, not proof of a particular hidden denominator or fabricated result.

Cell16's own `mmd_split`0.25100002 is also not Table1's MMD-O0.316. The main text explicitly distinguishes its own splitting implementation from Liu et al.'s MMD-O, so this is a explained method distinction, not a contradiction. Some Table1 baselines have no retained numeric output in supplied files.

**Later decision:** use exact paper table strings as *paper-reported* evidence; keep notebook outputs in a separate source evidence record; do not turn rounded table values into verified counts. Exact reconciliation requires original CIFAR experiment code, raw/aggregated results and averaging logic. It is unrelated to the executed Gaussian-mixture point.

### 5.5 Demonstrated stale/invalid plotting cell

`figures.ipynb` cell18 contains `plt.ylim(-0.05, 1.05n)`. A nonexecuting AST parse confirms `SyntaxError: invalid decimal literal` at source-cell line26. Retained output nevertheless includes a plotted figure. Thus saved output cannot have been generated by executing exactly the present source cell. This does not erase the published Figure7 visual evidence; it blocks a claim that all supplied plotting source runs unchanged. A future repair would be a separately recorded adapter/change, not an unmarked edit of upstream bytes. No repair was made.

### 5.6 Other boundaries needing clarification, not overstated contradictions

- Galaxy AutoML: Figure1 plotting cell3 uses `galaxy_vary_n_autotst_3min.npy` for the size panel while AppendixA.2 states a one-minute default. The filename suggests a three-minute variant but is not proof of actual time used. Missing generator code/records prevent a definitive runtime-setting claim.
- Kernel counts: default code means ten bandwidths *per family*, twenty kernels. Fig7 labels “Number of kernels” and text also mentions bandwidth counts; absent array/generator source leaves total-versus-per-family semantics unresolved. Do not call these the same count without checking.
- Power theory: Theorems2/3 assume a data-independent prior; empirical priors use pooled-data bandwidths. Calibration permits the latter, but the given sufficient-power theorem does not automatically do so. This is an explicit theorem scope boundary, not an inconsistency in calibration.
- Constant-temperature concentration: Theorem5's explicit upper restriction on normalized lambda is smaller than the empirical lambda choice even at the paper's printed scaling. Asymptotic `lambda ≍ n` hides constants; do not claim the explicit finite constants certify this execution.
- Mathematical typography: AppendixC's displayed Theorem7/its proof appear to differ by a factor16, and AppendixB's supremum over a Gamma posterior family is not self-evidently equivalent to the unrestricted DV supremum. These are flags for later mathematical review, not audited theorem refutations. Full compilation should preserve what the paper says and the uncertainty rather than silently rewriting proofs.
- Environment: paper reports Threadripper/GPU hardware; completed candidate used Xeon CPU and a minimal locked environment. Notebook-value agreement does not establish hardware-independent determinism or comparable paper test runtime.
- README notebook names: plural `experiments_mixture.ipynb` link differs from actual supplied singular `experiment_mixture.ipynb`. Cite the verified real file. Remaining referenced paths are missing from this selected snapshot, not proven absent upstream.


## Additional compilation inputs
The full pinned code/configuration inventory and all small released aggregate arrays were fetched without raw datasets. They resolve the kernel-count convention: the generator saves twice the per-family bandwidth count. They also confirm the Galaxy size-panel AutoML call explicitly uses `time=3 * 60`; its longer setting is documented rather than inferred from its filename. The CIFAR generator declares K=10 and N=100, and the released aggregate files match the retained notebook strings; the missing raw outcome vector still prevents independent count reconciliation. The dimension-runtime arrays now provide independently inspectable source values, but the published plotting code still uses the wrong arrays for its RHS. A zero ME entry at the largest dimension is an explicitly skipped case, not a zero-duration run.

Both paper-defined and released-code statistics remain attributed. No source was corrected, no new scientific trial was run, and no source-authority answer has been received. Issue #281 remains open. The earlier preflight's missing-input statements describe that earlier ten-file snapshot; the facts above supersede only those specific missing-input uncertainties.

## Galaxy saved-grid limit
The current three-minute generator cell lists six sample sizes, whereas the saved three-minute result array used by the plot has five entries. The plotting axis also has five entries. Thus the source confirms an explicit longer-time code path, but does not establish that the saved file was generated by the exact current cell. The artifact preserves the plotted five-point arrays and makes no raw-run provenance claim.
