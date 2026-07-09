---
type: model_config
paper: nanogpt-speedrun
---

# Model Configuration

## Target Model: GPT-2 124M (Optimized)

| Property | Baseline (Record 1) | Final (Record 21) |
|----------|---------------------|-------------------|
| Parameters | 124M | ~110M (after layer removal + GQA) |
| Layers | 12 | 7 |
| Heads | 12 | 6 (GQA: 3 KV heads) |
| Head dim | 64 | 128 |
| Vocab | 50257 | 50304 |
| Position | Learned | RoPE (half-truncated) |
| Activation | GELU | ReLU² |
| Norm | LayerNorm | RMSNorm |
| Embedding | Tied | Untied + value token embeddings |
| Skip | None | U-Net encoder-decoder |
| Precision | FP32/FP16 mixed | bfloat16 + FP8 head |

## Agent Models Evaluated

| Model | Provider | Notes |
|-------|----------|-------|
| DeepSeek R1 | DeepSeek | Reasoning-focused |
| o3-mini | OpenAI | Compact reasoning model |
| Gemini 2.5 | Google | Multimodal, long context |
| Claude 3.7 Sonnet | Anthropic | Extended thinking |
