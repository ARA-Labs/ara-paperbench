# Figure 3: Sequential Refinement — F1, Precision, Recall Over Time
- **Source**: Figure 3, Section 5.1
- **Caption**: "F1, Precision, and Recall of representation-based (Rep), threshold-based (Thres), and trainable logit-based forecasting models averaged up to a given time step (in x-axis) when continually refining the LM. For all forecasting methods, recall drops over time (as more examples being forgotten), while precision remains stable. Representation-based forecasting achieves best F1 and precision at the end of the sequence."
- **Conditions**: FLAN-T5Large Full FT on MMLU; values are running averages up to each time step

## Axis Labels
- X-axis: Time step (sequential position in the stream)
- Y-axis: Running average metric value

## Figure 3(a) — F1 (FLAN-T5Large Full FT)

| Approximate Time Step | Rep (F1) | Thres (F1) | Logit (F1) |
|----------------------|----------|------------|------------|
| Early (~0.1) | ≈0.50 | ≈0.50 | ≈0.45 |
| Middle (~0.5) | ≈0.45 | ≈0.42 | ≈0.38 |
| End (~1.0) | ≈0.40 | ≈0.37 | ≈0.33 |

Note: All values approximate from figure. Rep achieves consistently highest F1. Y-axis range approximately 0.3–0.6.

## Figure 3(b) — Precision (FLAN-T5Large Full FT)

| Approximate Time Step | Rep (Prec) | Thres (Prec) | Logit (Prec) |
|----------------------|------------|--------------|--------------|
| Early (~0.1) | ≈0.45 | ≈0.42 | ≈0.38 |
| Middle (~0.5) | ≈0.48 | ≈0.44 | ≈0.40 |
| End (~1.0) | ≈0.50 | ≈0.44 | ≈0.40 |

Note: Precision is approximately stable or slightly increasing over time. Rep achieves highest precision. Y-axis range approximately 0.4–0.6.

## Figure 3(c) — Recall (FLAN-T5Large Full FT)

| Approximate Time Step | Rep (Rec) | Thres (Rec) | Logit (Rec) |
|----------------------|-----------|-------------|-------------|
| Early (~0.1) | ≈0.70 | ≈0.65 | ≈0.55 |
| Middle (~0.5) | ≈0.55 | ≈0.45 | ≈0.40 |
| End (~1.0) | ≈0.35 | ≈0.30 | ≈0.28 |

Note: Recall drops over time as more examples are forgotten (the positive class grows). All three methods show declining recall. Y-axis range approximately 0.25–0.75.
