# Figure 21: Total Context Length Distribution vs Batch Size
- **Source**: Figure 21, Appendix B
- **Caption**: "Total context length distribution under different batch sizes using the Multi-Round ShareGPT dataset."
- **Axis labels**: x-axis = Batch Size; y-axis = Total context length ×10³.
- **Dataset**: Multi-Round ShareGPT
- **Purpose**: Justifies modeling token generation latency as a function of batch size B only (dropping total context length as a separate variable).

## Key Extracted Values

| Metric | Value | Source |
|--------|-------|--------|
| Pearson correlation coefficient (batch size vs total context length) | 0.997 | Appendix B text |
| Observation | Batch size and total context length are "nearly perfectly correlated" | Appendix B text |
| Effect of larger batch size on variance | Variance in total context length decreases (averages out individual variance) | Appendix B text |
| Conclusion | Token generation latency can be modeled as f(B) alone | Appendix B text |

*Note: Exact data points from the scatter plot are not numerically tabulated in the paper text; only the Pearson r = 0.997 statistic and directional observations are explicitly stated.*
