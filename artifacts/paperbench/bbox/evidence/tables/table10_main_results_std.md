# Table 10: Main Results with Standard Deviation
- **Source**: Table 10, Appendix I.1
- **Caption**: "Main results of adapting gpt-3.5-turbo on downstream tasks. For BBOX-ADAPTER, we report the best performance of adapters with # parameters of 0.1B and 0.3B. For all baselines and ours, we employ the CoT prompt as proposed in (Wei et al., 2022)."
- **Conditions**: Same as Table 2 but with standard deviations across multiple runs; Azure-SFT has no std reported (single run)

| Adapter | StrategyQA Acc. (%) | GSM8K Acc. (%) | TruthfulQA True+Info (%) | ScienceQA Acc. (%) |
|---------|--------------------|-----------------|--------------------------|--------------------|
| gpt-3.5-turbo (OpenAI, 2022) | 66.59±0.22 | 67.51±1.33 | 77.00±2.97 | 72.90±0.30 |
| Azure-SFT (Peng et al., 2023) | 76.86 | 69.94 | 95.00 | 79.00 |
| BBOX-ADAPTER (Ground-Truth) | 71.62±0.87 | 73.86±0.94 | 79.70±2.19 | 78.53±0.57 |
| BBOX-ADAPTER (AI Feedback) | 69.85±1.09 | 73.50±0.48 | 82.10±3.39 | 78.30±0.50 |
| BBOX-ADAPTER (Combined) | 72.27±1.09 | 74.28±0.45 | 83.60±2.37 | 79.40±0.20 |
