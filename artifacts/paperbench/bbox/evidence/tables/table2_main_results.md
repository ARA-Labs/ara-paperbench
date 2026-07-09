# Table 2: Main Results on GPT-3.5-turbo Downstream Task Adaptation
- **Source**: Table 2, Section 4.2
- **Caption**: "Main results of adapting gpt-3.5-turbo on downstream tasks. For BBOX-ADAPTER, we report the best performance of adapters with # parameters of 0.1B and 0.3B. For all baselines and ours, we employ the CoT prompt as proposed in (Wei et al., 2022)."
- **Conditions**: gpt-3.5-turbo base model; Azure-SFT (3 epochs via Azure OpenAI API); BBOX-ADAPTER variants (0.1B/0.3B adapter, beam size 3, T iterations); test sets per dataset

| Adapter | StrategyQA Acc. (%) | StrategyQA Δ(%) | GSM8K Acc. (%) | GSM8K Δ(%) | TruthfulQA True+Info (%) | TruthfulQA Δ(%) | ScienceQA Acc. (%) | ScienceQA Δ(%) |
|---------|--------------------|-----------------|-----------------|-----------|--------------------------|-----------------|--------------------|-----------------|
| gpt-3.5-turbo (OpenAI, 2022) | 66.59 | - | 67.51 | - | 77.00 | - | 72.90 | - |
| Azure-SFT (Peng et al., 2023) | 76.86 | +10.27 | 69.94 | +2.43 | 95.00 | +18.00 | 79.00 | +6.10 |
| BBOX-ADAPTER (Ground-Truth) | 71.62 | +5.03 | 73.86 | +6.35 | 79.70 | +2.70 | 78.53 | +5.63 |
| BBOX-ADAPTER (AI Feedback) | 69.85 | +3.26 | 73.50 | +5.99 | 82.10 | +5.10 | 78.30 | +5.40 |
| BBOX-ADAPTER (Combined) | 72.27 | +5.68 | 74.28 | +6.77 | 83.60 | +6.60 | 79.40 | +6.50 |
