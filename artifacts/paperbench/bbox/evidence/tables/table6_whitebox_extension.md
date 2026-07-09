# Table 6: White-Box Extension — Mixtral-8×7B on StrategyQA
- **Source**: Table 6, Section 4.7
- **Caption**: "Accuracy (%) and GPU memory usage on adapting Mixtral-8×7B to the StrategyQA dataset. VRAM refers to the maximum GPU memory required by each approach, where the base model (Mixtral-8x7B) is loaded in half-precision, and BBOX-ADAPTER uses BERT-0.1B as the backend."
- **Conditions**: Mixtral-8×7B loaded in half-precision (fp16); StrategyQA test set (229 samples); SFT-LoRA r=128 (0.1B) and r=384 (0.3B); BBOX-ADAPTER uses BERT-0.1B backend; 4× NVIDIA A100-SXM4-80GB

| Adapter | Acc.(%) 0.1B | Acc.(%) 0.3B | Training VRAM (GiB) | Inference VRAM (GiB) |
|---------|-------------|-------------|---------------------|----------------------|
| Base Model (Mixtral-8x7B) | 59.91 | — | — | 90 |
| Base + LoRA (Hu et al., 2021) | 73.80 | 75.98 | 208 | 92 |
| Base + BBOX-ADAPTER | 66.08 | 65.26 | 105 | 92 |

**Note**: The paper's Table 6 has columns Acc.(%) and VRAM (GiB) with sub-columns 0.1B and 0.3B for Acc., and Training/Inference for VRAM. The base model has no 0.3B entry (listed as "-"). VRAM for base model inference is approximately 90 GiB (half-precision Mixtral-8×7B).
