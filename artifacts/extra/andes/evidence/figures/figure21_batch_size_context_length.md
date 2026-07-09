# Figure 21: Batch Size vs. Total Context Length Distribution
- **Source**: Figure 21, Appendix B
- **Caption**: "Total context length distribution under different batch sizes using the Multi-Round ShareGPT dataset."
- **Axis labels**: X-axis: Batch Size; Y-axis: Total context length (×10³)
- **Conditions**: Multi-Round ShareGPT dataset; distribution shown as scatter/box plot of total context lengths per batch size.

## Key Quantitative Finding

| Statistic | Value |
|-----------|-------|
| Pearson correlation coefficient (batch size vs. total context length) | 0.997 |

## Qualitative Observation
- Total context length and batch size are nearly perfectly correlated (r = 0.997).
- As batch size increases, total context length is more predictable (variance decreases because per-request lengths average out).
- This justifies modeling token generation latency as a function of batch size B alone, dropping the total context length variable.

**Note**: The distribution plot shows boxes (likely median + IQR) for each batch size. Exact per-batch-size median and IQR values are not tabulated in the paper text. The Pearson r = 0.997 is the explicitly stated value.
