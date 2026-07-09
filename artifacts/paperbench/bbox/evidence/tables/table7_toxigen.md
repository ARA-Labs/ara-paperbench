# Table 7: ToxiGen Toxicity Reduction Results
- **Source**: Table 7, Appendix E
- **Caption**: "Results of adapting Mixtral-8x7B-v0.1 on the ToxiGen dataset. Note: For both metrics presented, lower values indicate better performance."
- **Conditions**: Mixtral-8x7B-v0.1 (temperature=0.7) as base model; deberta-v3-base as BBOX-ADAPTER backbone; 2,000 training samples, 500 test samples from ToxiGen; RoBERTa-based classifier judge (Hartvigsen et al., 2022)

| Adapter | Toxic (%) | Toxic Δ(%) | Toxicity Prob (%) | Toxicity Prob Δ(%) |
|---------|-----------|------------|-------------------|---------------------|
| Base Model (Mixtral-8x7B) | 41.90 | - | 41.02 | - |
| Base + BBOX-ADAPTER | 20.60 | −21.30 | 20.75 | −20.27 |
