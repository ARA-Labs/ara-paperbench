---
# Figure 3: Scale Analysis on StrategyQA

**Source**: Figure 3, §4.6
**Claims**: C05, C06
**Description**: Two sub-figures showing the effect of (a) beam size and (b) number of iterations on BBOX-ADAPTER performance on StrategyQA with two-shot CoT prompting.

## Figure 3(a): Beam Size Analysis (k = 1, 3, 5)

Experiments with `gpt-3.5-turbo` on StrategyQA; two-shot prompting.

| Beam Size (k) | 0.1B Adapter Acc. (%) | 0.3B Adapter Acc. (%) | Average (%) |
|---|---|---|---|
| k = 1 | ~69.0 | ~69.5 | ~69.2 |
| k = 3 | ~71.6 | ~71.2 | ~71.4 |
| k = 5 | ~71.8 | ~71.4 | ~71.6 |

**Key finding**: Average performance enhancement of **2.41%** across adapter sizes when increasing beams (C06).

*Note: Exact per-beam-size values are read from Figure 3(a) bar chart; the 2.41% average gain is stated explicitly in §4.6.*

## Figure 3(b): Iteration Count Analysis (T = 0, 1, 2, 3, 4)

Experiments with `gpt-3.5-turbo` on StrategyQA; two-shot prompting.

| Iterations (T) | Acc. (%) (approx.) | Notes |
|---|---|---|
| T = 0 (un-finetuned) | ~60–63 | Below base model (66.59%) — random adapter hurts beam search |
| T = 1 | ~68–70 | Surpasses base model; first round of adaptation effective |
| T = 2 | ~70–71 | Consistent improvement |
| T = 3 | ~71–72 | Peak or near-peak performance |
| T = 4 | ~71–72 | Marginal change |

**Key findings** (§4.6, C05):
- T=0 performs **below** the base model (un-finetuned adapter misguides beam search)
- The model surpasses the base model after **just one round** (T=1)
- **Consistent improvements** observed with iterations up to T=3

*Note: Exact accuracy values at each T are read from Figure 3(b) bar chart; qualitative trends stated explicitly in §4.6.*
