# Figure 7

**Source**: Figure 7 of the [paper](../paper.pdf), as identified in the inspection text below.

**Caption**: Power as the bandwidth collection becomes denser. (paraphrase; original caption is preserved in the source PDF).

**Screenshot**: [figure7.png](figure7.png)

**Figure type**: quantitative_plot

**Extraction method**: digitized_estimate

**Reading confidence**: medium

**Axes**: The quantitative panels use linear axes; qualitative image panels have no numeric axes.

## Visual description

Type quantitative_plot. Linear x kernel count, ticks 10,200,400,600,800,1000; linear y Power 0–1. MMD-FUSE red solid circles and MMDAgg blue dashed squares. Eight visible points, including two unlabeled intermediate x positions near ≈50 and ≈100. Approximate FUSE values are about ≈0.94 at first point, ≈0.90 at the next two, then ≈0.92–0.93 over the remainder; MMDAgg stays ≈0.72–0.75. The plotted point estimates occupy a narrow range; FUSE is descriptively higher in this experiment. This does not establish inferential retention. These are visual estimates, not recovered arrays.

Appendix A.4 states six one-dimensional perturbations, amplitude0.5, m=n=500, number of Gaussian/Laplace kernels from10 to1000. Whether this reported count denotes total kernels or per-family bandwidth settings was resolved from the subsequently obtained generator and x-axis array, as recorded below; do not silently equate it with default `number_bandwidths=10` (20 kernels). Caption exactly “Power experiment with perturbed uniform samples while varying the number of kernels.” Method digitized_estimate plus exact labels, confidence medium for point values, high for trend. `figures.ipynb` cell18 references `perturbations_vary_k.npy` and its x-axis array; now retained as decoded arrays and immutable source pointers. The cell's syntax error is discussed below.

## Exact released aggregates

The newly inspected generator notebook confirms that the displayed axis counts total kernels: each per-family bandwidth count is multiplied by two before saving. The plotting-cell syntax defect remains; these arrays are not a new run.

| Total kernels | MMD-FUSE | MMDAgg |
| --- | --- | --- |
| 10 | 0.9399999976158142 | 0.7450000047683716 |
| 50 | 0.9049999713897705 | 0.7299999594688416 |
| 100 | 0.8999999761581421 | 0.7400000095367432 |
| 200 | 0.9199999570846558 | 0.73499995470047 |
| 400 | 0.9199999570846558 | 0.7149999737739563 |
| 600 | 0.9300000071525574 | 0.7199999690055847 |
| 800 | 0.9300000071525574 | 0.73499995470047 |
| 1000 | 0.9149999618530273 | 0.7400000095367432 |

## Trend summary
The released point estimates span a narrow range in this named setting. They are descriptive evidence only: no noninferiority margin, verified cross-count outcome pairing or simultaneous uncertainty analysis is available. Raw binary outcomes are not reconstructed from floating proportions. A future retention analysis must fix its starting collection, expansion range, acceptable loss and uncertainty procedure before new outcomes; improvement is compatible with retention. The corrected count interpretation resolves a preflight uncertainty; it does not repair or rerun the stale plotting cell.
