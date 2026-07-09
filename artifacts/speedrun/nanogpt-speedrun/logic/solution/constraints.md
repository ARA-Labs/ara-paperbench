---
type: constraints
paper: nanogpt-speedrun
---

# Constraints

## Hardware Constraints
- Fixed 8×H100 80GB with NVLink interconnect
- All optimizations must work within this hardware envelope
- FP8 operations (Records 18-20) require H100-specific tensor cores
- Memory budget: 80GB per GPU, ~40GB available after model + optimizer states

## Software Constraints
- PyTorch 2.x required (torch.compile, FlexAttention)
- CUDA 12.5+ for FlexAttention block masking
- Python 3.10+ for type hints and match statements used in codebase
- NCCL for distributed communication

## Evaluation Constraints
- Success criterion: val_loss ≤ 3.28 on FineWeb-Edu 10B validation split
- Wall-clock time measured end-to-end including data loading, compilation, checkpointing
- Single run (no ensembling or multi-run selection)

## Agent Benchmark Constraints
- Maximum 20 iterations per search strategy per record
- Agent can only modify `train_gpt2.py` (single-file constraint)
- Agent cannot access the internet or external resources beyond provided hints
- SLURM timeout: 2× the target record's training time

## Generalization Constraints
- All optimizations validated only at GPT-2 124M scale
- FineWeb-Edu 10B is the only training dataset
- Transfer to larger models (1B+) or different architectures (Mamba, SSM) is untested
- Some optimizations (FP8, FlexAttention) are hardware-generation-specific
