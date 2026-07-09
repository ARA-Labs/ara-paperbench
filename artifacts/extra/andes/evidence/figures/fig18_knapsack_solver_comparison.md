# Figure 18: Different Knapsack Solver Comparison
- **Source**: Figure 18, Section 6.4
- **Caption**: "Different knapsack solver."
- **Model**: Llama 3.1 70B; Multi-Round ShareGPT dataset
- **Systems**: vLLM, Andes with Greedy solver (Algorithm 1), Andes with 3D DP solver (Algorithm 2)
- **X-axes**: Burst duration (%) [left panel]; Burst intensity (right panel)
- **Y-axis**: Average QoE

## Key Scalar Values from Text (§6.4)

| Metric | Value |
|--------|-------|
| Greedy solver speedup vs. 3D DP | ≈20× faster |

## Qualitative Observations (§6.4)
- "Andes outperforms the exact 3D DP solver because its greedy solver is more suitable for real-time decision making, being ~20× faster while still delivering high-quality approximate solutions."
- Greedy achieves slightly better average QoE under longer burst durations or higher burst intensities
- Both Andes variants significantly outperform vLLM

**Note**: Exact per-data-point QoE values are shown in Figure 18 as line plots; numerical values not stated in paper text.
