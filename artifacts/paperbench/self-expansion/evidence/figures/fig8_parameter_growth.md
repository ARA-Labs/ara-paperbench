# Figure 8: Added Parameters During Model Deployment on ImageNet-A
- **Source**: Figure 8, Section 4.3 (also Figure 10, Appendix C.2)
- **Caption**: "Analysis on added parameters (in Millions) during model deployment on ImageNet-A."
- **Dataset**: ImageNet-A (20 tasks, 10 classes/task)
- **Axes**: X = number of tasks (1–20); Y = added parameters (M)
- **Series**: L2P (fixed), DualPrompt, CODA-P, SEMA, Expansion by task

## Parameter Growth Data Points (approximate from figure)

| Tasks | L2P Params (M) | DualPrompt Params (M) | CODA-P Params (M) | SEMA Params (M) | Exp-by-Task Params (M) |
|-------|---------------|----------------------|-------------------|-----------------|------------------------|
| 1 | ≈ 0.200 | ≈ 0.10 | ≈ 0.20 | ≈ 0.025 | ≈ 0.10 |
| 5 | ≈ 0.200 | ≈ 0.55 | ≈ 1.00 | ≈ 0.15–0.20 | ≈ 0.48 |
| 9 | ≈ 0.200 | ≈ 0.99 | ≈ 1.80 | ≈ 0.30–0.40 | ≈ 0.86 |
| 10 | ≈ 0.200 | ≈ 1.10 | ≈ 2.00 | ≈ 0.40–0.45 | ≈ 0.95 |
| 15 | ≈ 0.200 | ≈ 1.65 | ≈ 3.00 | ≈ 0.48–0.52 | ≈ 1.43 |
| 20 | ≈ 0.200 | ≈ 2.19 | ≈ 3.99 | ≈ 0.560 | ≈ 1.90 |

**Note**: L2P parameter count is fixed (prompt pool); DualPrompt and CODA-P grow linearly; SEMA grows sub-linearly (concave curve); expansion-by-task grows linearly but at lower rate than CODA-P.
**Key finding at Task 9**: SEMA added more parameters than at other steps (expansion triggered at more layers for a particular task), showing step-wise sub-linear growth.
