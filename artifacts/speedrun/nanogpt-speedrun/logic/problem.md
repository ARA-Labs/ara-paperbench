---
type: problem
paper: nanogpt-speedrun
---

# Problem

## Observations

- **O1**: GPT-2 (124M) training on FineWeb-Edu 10B tokens takes ~49.5 minutes on 8×H100 GPUs with standard PyTorch setup (AdamW, learned positional embeddings, standard attention).
- **O2**: Human ML engineers have iteratively optimized NanoGPT training through 21 records, reducing wall-clock time to 3.1 minutes (16.1× speedup) while maintaining val_loss ≤ 3.28.
- **O3**: Each record introduces one or a few targeted optimizations — spanning optimizer design (Muon), architecture changes (ReLU², GQA, skip connections), systems-level tricks (FlexAttention, FP8 ops, async all_gather), and training recipe tuning (LR schedules, sequence lengths).
- **O4**: The optimizations are not independent; later records build on and depend on innovations introduced in earlier records (e.g., FlexAttention requires the architecture from Record 5, FP8 requires the distributed setup from Record 6).

## Gaps

- **G1 (Agent Implementation Gap)**: LLM agents can identify correct optimizations (via hints) but cannot implement them in working distributed training code — the bottleneck is not knowledge but systems engineering capability.
- **G2 (Compounding Complexity)**: Each successive optimization adds implementation constraints, making later records exponentially harder — the system becomes increasingly fragile to code changes.

## Key Insight

The NanoGPT speedrun trajectory reveals that training speedup is achieved through **compounding heterogeneous optimizations** across four axes (optimizer, architecture, systems, recipe), where each optimization must be implemented with exact precision in a distributed multi-GPU setting. This creates a natural difficulty ladder where success at level N requires mastery of all preceding levels.

## Assumptions

- 8×H100 80GB GPU hardware with NVLink interconnect
- PyTorch 2.x with torch.compile support
- FineWeb-Edu 10B tokens dataset (fixed)
- Success criterion: val_loss ≤ 3.28 AND train_time < previous record
