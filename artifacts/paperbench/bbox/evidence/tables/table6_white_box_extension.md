# Table 6: White-Box Extension — Mixtral-8×7B Adaptation
- **Source**: Table 6, Section 4.7
- **Caption**: "Accuracy (%) and GPU memory usage on adapting Mixtral-8×7B to the StrategyQA dataset. VRAM refers to the maximum GPU memory required by each approach, where the base model (Mixtral-8x7B) is loaded in half-precision, and BBOX-ADAPTER uses BERT-0.1B as the backend."
- **Conditions**: Mixtral-8x7B-v0.1 in half-precision (float16); StrategyQA; BBOX-ADAPTER uses deberta-v3-base (0.1B) as noted in text (Table caption says "BERT-0.1B"); LoRA r=128 (0.1B), r=384 (0.3B), α=2r

| Adapter | Acc. 0.1B (%) | Acc. 0.3B (%) | Training VRAM (GiB) | Inference VRAM (GiB) |
|---------|---------------|---------------|---------------------|----------------------|
| Base Model (Mixtral-8x7B) | 59.91 | — | — | 90 |
| Base + LoRA | 73.80 | 75.98 | 208 | 92 |
| Base + BBOX-ADAPTER | 66.08 | 65.26 | 105 | 92 |

**Note**: LoRA training uses 4× A100 GPUs (208 GiB total); BBOX-ADAPTER training uses less VRAM (105 GiB) because only the small adapter is trained while Mixtral parameters are frozen.
