# Table 1: Models and Hardware Configurations
- **Source**: Table 1, Section 6.1
- **Caption**: "Models and hardware configurations."
- **Experimental conditions**: All models evaluated on NVIDIA A100 SXM4 40GB GPUs in one AWS p4d.24xlarge instance with tensor parallelism.

| Model | Architecture | Memory | Hardware |
|-------|-------------|--------|----------|
| Phi-3-mini 3.8B | Dense, MHA | 7 GB | A100×4 |
| Command R 32B | Dense, GQA | 61 GB | A100×8 |
| Phi-3.5-MoE 16×3.8B | MoE, GQA | 80 GB | A100×8 |
| Llama 3.1 70B | Dense, GQA | 132 GB | A100×8 |
