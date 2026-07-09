# Figure 18: Knapsack Solver Comparison (Greedy vs 3D DP)
- **Source**: Figure 18, Section 6.4
- **Caption**: "Different knapsack solver."
- **Axis labels**: Left panel: x-axis = Duration (%); y-axis = Avg QoE. Right panel: x-axis = Intensity (r); y-axis = Avg QoE.
- **Model**: Llama 3.1 70B, 8×A100
- **Dataset**: Multi-Round ShareGPT
- **Systems**: vLLM, Andes w/ Greedy (Algorithm 1), Andes w/ DP (Algorithm 2)

## Key Extracted Values

| Metric | Value | Source |
|--------|-------|--------|
| Greedy solver speedup over 3D DP | ≈ 20× | Section 6.4 text |
| Greedy vs DP QoE at longer burst durations | Greedy achieves slightly better QoE | Section 6.4 text |
| Greedy vs DP QoE at higher burst intensities | Greedy achieves slightly better QoE | Section 6.4 text |
| Reason greedy outperforms DP | Faster per-decision enables more frequent scheduling | Section 6.4 text |

*Note: Exact per-configuration QoE values are not numerically tabulated in the paper text.*
