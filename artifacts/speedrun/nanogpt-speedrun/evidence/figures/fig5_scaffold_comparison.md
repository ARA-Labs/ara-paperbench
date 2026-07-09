---
source: "Figure 5, Section 4.3 of arXiv:2506.22419"
claims_verified: [C07]
---

# Figure 5: Scaffold Comparison

IQM FSR across 5 search scaffolds for each model (L1 hints).

## Data

| Model | Tree | Forest | AIDE | Multi-AIDE | Flat |
|-------|------|--------|------|------------|------|
| o3-mini | 0.38 | 0.40 | 0.41 | 0.43 | 0.39 |
| DeepSeek-R1 | 0.28 | 0.30 | 0.31 | 0.32 | 0.29 |
| Gemini-2.5-Pro | 0.18 | 0.19 | 0.20 | 0.22 | 0.19 |
| Claude-3.7-Sonnet | 0.10 | 0.11 | 0.11 | 0.12 | 0.10 |

## Key Observations

- **Multi-AIDE achieves the highest IQM FSR** for 3 of 4 models
- **Flat search is surprisingly competitive**: Often matches or exceeds Tree and Forest, despite using no iteration
- **AIDE vs. Multi-AIDE**: Multi-AIDE's branching adds ~0.01-0.02 FSR over single-branch AIDE
- **Debug capability (AIDE/Multi-AIDE vs. Tree/Forest)**: Modest advantage from debugging (p_debug=0.5)
- **The benefit of iteration over independent attempts is smaller than expected**: Flat (20 independent shots) is nearly as good as iterative methods, suggesting the optimization landscape is hard to navigate incrementally

## Visualization Type

Grouped bar chart, one group per model, bars for each scaffold. Error bars: bootstrap 95% CI.
