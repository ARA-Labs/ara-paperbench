# Model Configuration Parameters

## phi_3_mini_3_8b
- **Architecture**: Dense, Multi-Head Attention (MHA)
- **Parameters**: 3.8B
- **Memory**: 7 GB (model weights)
- **Hardware**: 4 × NVIDIA A100 SXM4 40GB
- **Parallelism**: Tensor parallelism
- **Source**: Table 1, Section 6.1

## command_r_32b
- **Architecture**: Dense, Grouped-Query Attention (GQA)
- **Parameters**: 32B
- **Memory**: 61 GB (model weights)
- **Hardware**: 8 × NVIDIA A100 SXM4 40GB
- **Parallelism**: Tensor parallelism
- **Source**: Table 1, Section 6.1

## phi_3_5_moe_16x3_8b
- **Architecture**: Mixture-of-Experts (MoE), Grouped-Query Attention (GQA)
- **Parameters**: 16×3.8B (MoE)
- **Memory**: 80 GB (model weights)
- **Hardware**: 8 × NVIDIA A100 SXM4 40GB
- **Parallelism**: Tensor parallelism
- **Source**: Table 1, Section 6.1

## llama_3_1_70b
- **Architecture**: Dense, Grouped-Query Attention (GQA)
- **Parameters**: 70B
- **Memory**: 132 GB (model weights)
- **Hardware**: 8 × NVIDIA A100 SXM4 40GB (requires NVLink or equivalent for 132GB > single GPU)
- **Parallelism**: Tensor parallelism
- **Source**: Table 1, Section 6.1

## dataset_multi_round_sharegpt
- **Input length**: Mean = 3171 tokens, Std = 7943 tokens
- **Output length**: Not separately specified in paper (multi-round conversational)
- **Source**: Table 2, Section 6.1

## dataset_arxiv_summarization
- **Input length**: Mean = 17855 tokens, Std = 11401 tokens
- **Output length**: Not specified in paper
- **Source**: Table 2, Section 6.1

## dataset_coding_challenges
- **Input length**: Mean = 1552 tokens, Std = 5423 tokens
- **Output length**: Mean = 21293 tokens, Std = Not specified in paper
- **Source**: Table 2, Section 6.1
