# Environment

Source: `metr-re-bench/ai_rd_triton_cumsum/README.md`, `requirements.txt`, task instructions

## Hardware
- GPU: NVIDIA H100 80GB (from task instructions: "nvidia gpu", H100 80GB confirmed in RE-Bench paper arXiv:2411.15114 Appendix C)
- HBM3 bandwidth: ~3.35 TB/s (RE-Bench paper Appendix C — not in task README)
- SM count: 132 (RE-Bench paper Appendix C — not in task README)

## Software
- Triton: 2.3.1
- PyTorch: CUDA-enabled (version from task environment)
- Python: 3.x

## Task Environment
- Agent working directory: `/home/agent/solution/`
- Solution file: `solution.py` (must export `prefix_sum` function)
- Scoring harness runs separately (outside agent environment)

## Randomness
- Scoring input: `torch.randint(-10, 10, (100_000_000,), dtype=torch.int32)`
- Seed: `torch.manual_seed(int.from_bytes(os.urandom(8), "big"))` — fresh random seed
  each score call to prevent memorization attacks
