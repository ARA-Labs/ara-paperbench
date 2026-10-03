# Figure 3

**Source**: Figure 3 of the [paper](../paper.pdf), as identified in the inspection text below.

**Caption**: One-dimensional perturbed-uniform densities across amplitudes. (paraphrase; original caption is preserved in the source PDF).

**Screenshot**: [figure3.png](figure3.png)

**Figure type**: quantitative_plot

**Extraction method**: digitized_estimate

**Reading confidence**: medium

**Axes**: The quantitative panels use linear axes; qualitative image panels have no numeric axes.

## Visual description

Type quantitative_plot, deterministic density illustration. Linear x on [0,1]; linear y density displayed [0,2]; six labeled amplitudes 0,0.1,0.2,0.3,0.4,0.5. Two positive and two negative lobes about baseline density 1, with larger amplitudes moving farther from 1. Visually largest-amplitude maxima ≈1.5 and minima ≈0.5. Caption identifies two perturbations and varying amplitudes. `figures.ipynb` cell 11 imports missing `sampler_perturbations.f_theta`, uses 300 grid positions and seed 1; the loop reuses variable `s` originally set as smoothness, so exact function semantics require the missing source before declaring a discrepancy. Method digitized_estimate/visual_description; confidence high for labels and medium for extrema. No empirical power is shown.

| Amplitude label | Visual density range |
| --- | --- |
| 0 | 1 baseline |
| 0.5 | ≈0.5 to ≈1.5 |

## Trend summary
The perturbation grows around the common baseline; no statistical test power is represented here.
