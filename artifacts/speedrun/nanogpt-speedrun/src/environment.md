---
type: environment
paper: nanogpt-speedrun
---

# Environment

## Hardware
- **GPUs**: 8× NVIDIA H100 80GB SXM5 with NVLink
- **Interconnect**: NVLink 4.0 (900 GB/s bidirectional)
- **CPU**: AMD EPYC 9654 (or equivalent)
- **RAM**: 512GB+ DDR5

## Software
- **Python**: 3.10+
- **PyTorch**: 2.5+ (required for FlexAttention, torch.compile)
- **CUDA**: 12.5+
- **NCCL**: 2.20+
- **torchrun**: distributed launcher (`--nproc_per_node=8`)

## Dataset
- **Training**: FineWeb-Edu 10B tokens (HuggingFace)
- **Format**: Pre-tokenized with GPT-2 tokenizer, stored as `data.jsonl`
- **Validation**: Same distribution, separate split
- **URL**: https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu

## Agent Framework Dependencies
- **aider**: 0.40+ (diff-based code editing)
- **submitit**: SLURM job submission
- **hydra-core**: Configuration management
- **litellm**: Multi-model LLM API client

## Seeds
- Training seeds vary per record (not fixed across records)
- Agent evaluation uses fixed seeds per (model, record, strategy) tuple
