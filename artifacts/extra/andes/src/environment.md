# Environment

- **Python**: Not specified in paper
- **Framework**: vLLM v0.6.1 (Andes implemented as an alternative scheduling policy within vLLM)
- **Hardware**: NVIDIA A100 SXM4 40GB GPUs; AWS p4d.24xlarge instance
  - Phi-3-mini 3.8B: 4 × A100
  - Command R 32B: 8 × A100
  - Phi-3.5-MoE 16×3.8B: 8 × A100
  - Llama 3.1 70B: 8 × A100
- **Parallelism**: Tensor parallelism across GPUs within one instance
- **Key dependencies**:
  - vLLM v0.6.1
  - PyTorch (version not specified in paper)
  - CUDA (version not specified in paper)
- **Random seeds**: Not specified in paper
- **Request trace**: BurstGPT (one-hour slice), arXiv:2401.17644
- **Prefill throughput (measured)**: 5000 tokens/s on 8×A100 for Phi-3.5-MoE 16×3.8B
- **Token generation latency model**: Batch size as sole predictor; offline-profiled per model; Pearson r = 0.997 between batch size and total context length
