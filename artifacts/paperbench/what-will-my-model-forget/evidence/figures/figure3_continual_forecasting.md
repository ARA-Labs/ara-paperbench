# Figure 3: Forecasting Performance in Continual Model Refinement
- **Source**: Figure 3, Section 5.1
- **Caption**: "F1, Precision, and Recall of representation-based (Rep), threshold-based (Thres), and trainable logit-based forecasting models averaged up to a given time step (in x-axis) when continually refining the LM. For all forecasting methods, recall drops over time (as more examples being forgotten), while precision remains stable. Representation-based forecasting achieves best F1 and precision at the end of the sequence."

**Experimental conditions**: FLAN-T5Large, Full FT, MMLU dataset as D_R; continual stream of sequential error fixes; running averages plotted.

## Panel (a): F1 vs. Time Step
Approximate data points (running averages; x-axis = normalized time step 0–1):

| Time Step | Rep F1 | Thres F1 | Logit F1 |
|-----------|--------|----------|----------|
| ~0.0 (early) | ≈0.55 | ≈0.52 | ≈0.52 |
| ~0.3 | ≈0.48 | ≈0.43 | ≈0.40 |
| ~0.5 | ≈0.42 | ≈0.38 | ≈0.35 |
| ~0.7 | ≈0.38 | ≈0.34 | ≈0.33 |
| ~1.0 (end) | ≈0.35 | ≈0.30 | ≈0.28 |

**Key finding**: Rep achieves highest running F1 at all time steps.

## Panel (b): Precision vs. Time Step
Approximate data points:

| Time Step | Rep Precision | Thres Precision | Logit Precision |
|-----------|--------------|-----------------|-----------------|
| ~0.0 | ≈0.50 | ≈0.52 | ≈0.48 |
| ~0.3 | ≈0.56 | ≈0.52 | ≈0.52 |
| ~0.5 | ≈0.58 | ≈0.54 | ≈0.53 |
| ~1.0 (end) | ≈0.58 | ≈0.55 | ≈0.53 |

**Key finding**: Precision is relatively stable or slightly increasing for all methods; Rep achieves highest precision.

## Panel (c): Recall vs. Time Step
Approximate data points:

| Time Step | Rep Recall | Thres Recall | Logit Recall |
|-----------|-----------|--------------|--------------|
| ~0.0 | ≈0.60 | ≈0.52 | ≈0.58 |
| ~0.3 | ≈0.43 | ≈0.38 | ≈0.35 |
| ~0.5 | ≈0.38 | ≈0.30 | ≈0.28 |
| ~1.0 (end) | ≈0.28 | ≈0.26 | ≈0.22 |

**Key finding**: Recall drops significantly over time for all methods as more examples are forgotten; Rep maintains the highest recall throughout.

**Note**: Exact values not readable from line plots; ≈ denotes estimated readings from Figure 3 in the paper.
