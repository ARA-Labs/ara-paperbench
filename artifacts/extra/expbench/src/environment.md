# Environment

## Python
- **Version**: Not specified in paper (standard ML environment assumed; Python 3.10+ implied by Ubuntu 24.04 Docker base)

## Framework
- **Agent runtime**: Ubuntu 24.04 Docker container
- **LLM APIs**: OpenAI API (o3-mini), Anthropic API (Claude-3.7 Sonnet, Claude-3.5 Haiku), Amazon Bedrock (Nova Pro), DeepSeek API (DeepSeek R1)
- **Judge LLM**: o3-mini-2025-01-01-preview via OpenAI API
- **Extraction LLMs**: o3-mini-2025-01-01-preview + claude-3-7-sonnet-20250219-v1:0

## Hardware
- **Per-agent-run**: 4× NVIDIA A40 GPU
- **Evaluation infrastructure**: Standard HPC/cloud cluster (University of Michigan, Rice, UC Berkeley, Cisco Research)
- **Notable paper-specific requirements**: Some tasks require specialized hardware (e.g., Bag of Tricks: 50× A800 GPUs; Voxel Mamba: 8× A100; Self-playing Adversarial: 32× A100 40GB; Safe RLHF: 8× A800-80GB)

## Key Dependencies
- Docker (Ubuntu 24.04 base image)
- NVIDIA drivers + CUDA (compatible with A40 GPUs)
- PyTorch (version varies by source paper task)
- JAX/Flax (required by some tasks, e.g., JaxMARL)
- k2 / icefall (required by Zipformer ASR task)
- OpenAI Python SDK
- Anthropic Python SDK
- AWS Boto3 (for Amazon Bedrock)
- Git (for repository cloning and diff operations)
- OCR library (for PDF processing in curation pipeline)

## Random Seeds
- Not specified in paper for agent evaluations
- Source papers vary in their seed specifications; ground truth implementations use seeds as specified in original papers

## Dataset Repository
- HuggingFace: https://huggingface.co/datasets/Just-Curieous/EXP-Bench
- GitHub: https://github.com/Just-Curieous/Curie/tree/main/benchmark/exp_bench
- License: Creative Commons Attribution 4.0 (data); MIT (code)
