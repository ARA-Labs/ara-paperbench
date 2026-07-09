# Environment

## Hardware (per `manifest.yaml:10-17`)
- **GPU**: 2 × H100 (80 GB each)
- **CPU**: 26 cores
- **RAM**: 200 GB

## Software (per `requirements.txt`)
- `torch~=2.4.1`
- `transformers~=4.44.2`
- `tiktoken~=0.7.0`
- `replicate~=0.32.1`
- `datasets~=2.21.0`
- `numpy<2.0`
- `tqdm~=4.66.5`
- `wandb<0.18.0`
- `metr.task_protected_scoring@v0.2.1` (from `git+https://github.com/METR/task-protected-scoring.git@v0.2.1`)

## External services
- **Replicate API** for `llama-3-8b-instruct` judge calls. Authenticated via
  `REPLICATE_API_TOKEN` (`ai_rd_nanogpt_chat_rl.py:20`); accessed only through
  the protected `/home/agent/evaluation.py` wrapper.

## Random seeds
- Not explicitly fixed in the official solution. `torch.randint`
  (`rl_finetune_best_of_n.py:176`) and the multinomial sampler in
  `model.GPT.generate` (`model.py:359-360`) both rely on PyTorch's default
  CUDA RNG state.

## Filesystem layout (in container)
- `/home/agent/solution/` — agent-modifiable directory containing
  `model.py`, the training script, and saved checkpoints.
- `/home/agent/finetuned_model` — canonical submission path.
- `/home/agent/prompts.jsonl` — Alpaca prompts.
- `/home/agent/evaluation.py` — protected judge wrapper.
- `/home/agent/score.py` — protected held-out scorer.
- `/home/agent/padding_text.txt` — front-padding tokens used by
  `generate_strings_autobatch` (`model.py:377`).
