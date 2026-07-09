# Figure 21: Total Context Length Distribution Under Different Batch Sizes
- **Source**: Figure 21, Appendix B
- **Caption**: "Total context length distribution under different batch sizes using the Multi-Round ShareGPT dataset."
- **Dataset**: Multi-Round ShareGPT
- **X-axis**: Batch size
- **Y-axis**: Total context length (×10³ tokens)

## Key Scalar Value from Text (Appendix B)

| Metric | Value |
|--------|-------|
| Pearson correlation between batch size and total context length | 0.997 |

## Key Observation (Appendix B)
"It can be seen that batch size and total context length are nearly perfectly correlated, with Pearson correlation coefficient being 0.997. Moreover, with the increase of batch size, the total context length is more predictable as it averages out the variance in individual request context lengths. Therefore, we can drop total context length and estimate token generation latency simply as a function of batch size B."

**Note**: Exact (batch_size, total_context_length) data points are shown as a scatter/distribution plot; numerical values not stated in paper text. The critical result (Pearson r = 0.997) is explicitly stated.
