---
# System Architecture

## Overview

CFG for language models is implemented as a **decoding wrapper** that intercepts the token generation loop of any autoregressive language model. It requires two forward passes per token: one with the full prompt (conditional) and one with a truncated prompt (unconditional). The logits from both passes are combined using the CFG formula before sampling.

## Components

### 1. Language Model (LM)
- **Purpose**: Provides conditional logits P(wᵢ|w<ᵢ, c) and unconditional logits P(wᵢ|w<ᵢ) at each step
- **Inputs**: Token sequences (with and without prompt prefix)
- **Outputs**: Logit tensors of shape [vocab_size]
- **Design choice**: Any decoder-only transformer (GPT-2, Pythia, LLaMA, CodeGen, etc.) works without modification; no training changes required
- **Interaction**: Queried twice per decoding step

### 2. CFG Logit Combiner
- **Purpose**: Combines conditional and unconditional logits using the CFG formula (Eq. 7)
- **Inputs**: `logits_cond` [vocab_size], `logits_uncond` [vocab_size], scalar γ
- **Outputs**: `logits_cfg` [vocab_size] = `logits_uncond + γ * (logits_cond - logits_uncond)`
- **Design choice**: Logit space (pre-softmax) is used because it has linear relationship with last hidden layer and is architecture-agnostic; avoids network editing [9]
- **Interaction**: Receives outputs from LM; sends combined logits to sampler

### 3. Unconditional Prefix Constructor
- **Purpose**: Constructs the "unconditional" input by truncating the prompt to only the last token
- **Inputs**: Full prompt token sequence [seq_len]
- **Outputs**: Truncated prefix [1] (last token of prompt)
- **Design choice**: Starting from the last prompt token (rather than a special BOS token) naturally uses the model's in-distribution behavior; aligns with how the model was trained
- **Interaction**: Provides input to the LM's second (unconditional) forward pass

### 4. Negative Prompt Manager (Optional)
- **Purpose**: Replaces the unconditional prefix with a "negative prompt" for more granular control
- **Inputs**: Negative prompt token sequence $\bar{c}$ (e.g., default system prompt)
- **Outputs**: Negative-conditioned logits P(wᵢ|w<ᵢ, $\bar{c}$)
- **Design choice**: Used in chatbot settings; the default system prompt is the natural "negative" to contrast against a user-modified system prompt
- **Interaction**: Replaces the unconditional LM pass; feeds into CFG Logit Combiner

### 5. Token Sampler
- **Purpose**: Samples the next token from the CFG-adjusted logit distribution
- **Inputs**: `logits_cfg` [vocab_size], temperature parameter, top-p nucleus
- **Outputs**: Next token wᵢ
- **Design choice**: Any standard sampling strategy (greedy, temperature, nucleus) is compatible; CFG adjusts the distribution before sampling
- **Interaction**: Receives combined logits; outputs token to append to running context

## Component Graph

```
Prompt (c) ──────────────────────┐
                                 ▼
                         ┌─────────────┐
                         │  LM Forward │ → logits_cond
                         │ (full prompt)│
                         └─────────────┘
                                 ↓
Last prompt token ──────────────────────┐
(or negative prompt c̄)                 ▼
                         ┌─────────────┐
                         │  LM Forward │ → logits_uncond
                         │(uncond/neg) │
                         └─────────────┘
                                 ↓
                         ┌─────────────────┐
                         │ CFG Combiner    │
                         │ logits_uncond + │ → logits_cfg
                         │ γ*(cond-uncond) │
                         └─────────────────┘
                                 ↓
                         ┌─────────────┐
                         │   Sampler   │ → next token wᵢ
                         └─────────────┘
```

## Design Rationale

1. **Logit space vs hidden space**: CFG is applied in logit space (not hidden states) to be architecture-agnostic and avoid network editing.
2. **No training required**: Unlike diffusion CFG which needs conditioning dropout, LM CFG works out-of-the-box.
3. **Last-token unconditional**: Starting the unconditional forward pass from the last prompt token (not a start token) was found to work well in practice.
4. **Negative prompting extension**: The unconditional pass can be replaced with any negative prompt, enabling fine-grained control over what aspects are emphasized.

## Code Reference
- Core implementation: [src/execution/cfg_decoding.py](../../src/execution/cfg_decoding.py)
