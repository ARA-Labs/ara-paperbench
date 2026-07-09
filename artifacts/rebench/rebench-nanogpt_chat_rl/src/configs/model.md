# Model Configuration

`gpt2-xl` loaded via `GPT.from_pretrained("gpt2-xl")`
(`model.py:249-329`). Configuration overrides applied during load
(`model.py:266-278`):

| Parameter | Value | Notes | File:line |
|-----------|-------|-------|-----------|
| `n_layer` | 48 | gpt2-xl size class | `model.py:270` |
| `n_head` | 25 | gpt2-xl size class | `model.py:270` |
| `n_embd` | 1600 | gpt2-xl size class | `model.py:270` |
| `vocab_size` | 50257 | forced for GPT-2 checkpoints | `model.py:273-274` |
| `block_size` | 1024 | forced for GPT-2 checkpoints | `model.py:277` |
| `bias` | True | forced for GPT-2 checkpoints | `model.py:278` |
| `dropout` | 0.0 (default) | overridable but not overridden in the solution | `model.py:151, 280-282` |
| `kv_cache` | False (default) | toggled to True only inside `generate` | `model.py:155, 340` |

## Tied weights

`self.transformer.wte.weight = self.lm_head.weight` (`model.py:179-181`) — the
input token embedding and the output projection share the same `nn.Parameter`.
Any modification to `wte.weight` is also a modification to `lm_head.weight`
and vice versa.

## Reference model parameters (used by the scorer, not the agent)

The scorer compares the student against two reference models, both loaded
through the same `GPT.from_pretrained` path:

| Reference | n_layer | n_head | n_embd | vocab_size | Source |
|-----------|---------|--------|--------|-----------|--------|
| `gpt2-xl` | 48 | 25 | 1600 | 50257 | `model.py:270, 274` |
| `vicgalle/gpt2-alpaca` | 12 | 12 | 768 | 50260 | `model.py:271, 276` |

The reference model outputs are pre-computed at task setup time and copied from
`assets/{model}.jsonl` into the protected scoring directory
(`ai_rd_nanogpt_chat_rl.py:134-138`); the agent never invokes them at run time.

## Save / load format

`GPT.save(path)` writes `{"config": GPTConfig, "model_state_dict": dict}` via
`torch.save` (`model.py:444-445`). `GPT.from_saved_model(path)` reads the same
dict (`model.py:437-442`). Submitted artefact must conform to this format.
