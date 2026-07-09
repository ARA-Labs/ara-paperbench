# Environment

## Python
- **Version**: 3.10.13

## Framework
- **HuggingFace Transformers**: Used for DeBERTa-v3-base, DeBERTa-v3-large, BERT-base-cased, Mixtral-8×7B model loading and inference
- **HuggingFace PEFT**: Used for LoRA fine-tuning of Mixtral-8×7B (SFT-LoRA baseline)
- **PyTorch**: Not version-specified in paper; required for all model training
- **OpenAI Python SDK**: For gpt-3.5-turbo and davinci-002 API access via Microsoft Azure

## Hardware
- **GPU**: NVIDIA A100-SXM4-80GB
- **GPU Count**: 4× A100-SXM4-80GB (for Mixtral-8×7B LoRA experiments)
- **CPU**: AMD EPYC 7702 64-Core Processor @ 1.50GHz
- **Memory requirements (VRAM)**:
  - deberta-v3-base adapter training: low (< 8 GiB)
  - Mixtral-8×7B inference: ~90 GiB (half-precision)
  - Mixtral-8×7B + LoRA training: ~208 GiB
  - Mixtral-8×7B + BBOX-ADAPTER training: ~105 GiB
  - Mixtral-8×7B inference (any): ~92 GiB

## Key Dependencies
- **HuggingFace Transformers**: model loading, tokenization (deberta-v3, bert-base-cased, Mixtral-8×7B-v0.1)
- **HuggingFace PEFT**: LoRA implementation for SFT-LoRA baseline
- **OpenAI API**: gpt-3.5-turbo, davinci-002 text generation and fine-tuning
- **Microsoft Azure OpenAI API**: Azure-hosted GPT-3.5-turbo fine-tuning service
- **PyTorch**: model training and gradient computation
- **torch.nn.utils.spectral_norm**: spectral normalization for adapter classification head

## Model Checkpoints
- **DeBERTa-v3-base**: `microsoft/deberta-v3-base` (HuggingFace Hub, 86M parameters)
- **DeBERTa-v3-large**: `microsoft/deberta-v3-large` (HuggingFace Hub, 304M parameters)
- **BERT-base-cased**: `bert-base-cased` (HuggingFace Hub, 110M parameters)
- **Mixtral-8×7B**: `mistralai/Mixtral-8x7B-v0.1` (HuggingFace Hub, half-precision)

## Random Seeds
- Not specified in paper

## Code Repository
- GitHub: https://github.com/haotiansun14/BBox-Adapter
