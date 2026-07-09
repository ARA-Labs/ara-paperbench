---
# Algorithm

## Mathematical Formulation

### Standard CFG for Diffusion Models
Given conditional model $P_\theta(x|c)$ and unconditional $P_\theta(x)$:
$$\hat{P}(x|c) \propto P_\theta(x|c)^\gamma \cdot P_\theta(x)^{1-\gamma}$$

In noise-prediction form (Eq. 3):
$$\log \hat{P}_\theta(\epsilon_t | x_{t+1}, c) = \gamma \log P_\theta(\epsilon_t | x_{t+1}, c) - (\gamma - 1) \log P_\theta(\epsilon_t | x_{t+1})$$

### CFG for Autoregressive Language Models (Eq. 7)
For token $w_i$ given context $w_{j<i}$ and prompt $c$:
$$\log \hat{P}_\theta(w_i | w_{j<i}, c) = \log P_\theta(w_i | w_{j<i}) + \gamma \left( \log P_\theta(w_i | w_{j<i}, c) - \log P_\theta(w_i | w_{j<i}) \right)$$

This arises from the factorization (Eq. 6):
$$\hat{P}_\theta(w|c) \propto \frac{P_\theta(w|c)^\gamma}{P_\theta(w)^{\gamma-1}} = \prod_i \frac{P_\theta(w_i | w_{j<i}, c)^\gamma}{P_\theta(w_i | w_{j<i})^{\gamma-1}}$$

### Negative Prompting Extension (Eq. 5 adapted to LMs)
With negative prompt $\bar{c}$:
$$\log \hat{P}_\theta(w_i | w_{j<i}, c, \bar{c}) = \log P_\theta(w_i | w_{j<i}, \bar{c}) + \gamma \left( \log P_\theta(w_i | w_{j<i}, c) - \log P_\theta(w_i | w_{j<i}, \bar{c}) \right)$$

### Token Upweighting Visualization
The token importance score at step $t$ is:
$$\Delta_t(w) = \log P_\theta(w_t | w_{<t}, c) - \log P_\theta(w_T | \hat{w})$$

Ranking vocabulary by $\Delta_t$ shows which tokens are encouraged (top) vs discouraged (bottom) by CFG at each step.

## Pseudocode

```python
def cfg_decode(model, prompt_tokens, gamma, max_new_tokens,
               negative_prompt_tokens=None, temperature=1.0):
    """
    Classifier-Free Guidance decoding for autoregressive LMs.
    
    Args:
        model: Autoregressive LM with logits output
        prompt_tokens: Tokenized prompt [seq_len]
        gamma: Guidance strength (γ); 1.0 = no guidance
        max_new_tokens: Number of tokens to generate
        negative_prompt_tokens: If None, use last prompt token as uncond prefix
        temperature: Sampling temperature
    
    Returns:
        generated_tokens: List of generated token ids
    """
    context = list(prompt_tokens)
    
    # Unconditional prefix: last prompt token (or negative prompt)
    if negative_prompt_tokens is None:
        uncond_prefix = [prompt_tokens[-1]]  # last token of prompt
    else:
        uncond_prefix = list(negative_prompt_tokens)
    
    generated = []
    for step in range(max_new_tokens):
        # Forward pass 1: Conditional (full prompt + generated so far)
        cond_input = context + generated
        logits_cond = model(cond_input)[-1]  # [vocab_size], last position
        
        # Forward pass 2: Unconditional (uncond prefix + generated so far)
        uncond_input = uncond_prefix + generated
        logits_uncond = model(uncond_input)[-1]  # [vocab_size], last position
        
        # CFG combination (Equation 7)
        logits_cfg = logits_uncond + gamma * (logits_cond - logits_uncond)
        
        # Sample next token
        logits_cfg = logits_cfg / temperature
        probs = softmax(logits_cfg)
        next_token = sample(probs)
        generated.append(next_token)
        
        if is_eos(next_token):
            break
    
    return generated
```

## Step-by-Step Explanation

1. **Initialize**: Start with the tokenized prompt $c$ as the conditional context.
2. **Set unconditional prefix**: Use the last token of the prompt as the unconditional prefix (approximates dropping $c$). For negative prompting, replace with the tokenized negative prompt $\bar{c}$.
3. **For each new token**:
   a. Run forward pass on `[prompt] + [generated_so_far]` → `logits_cond`
   b. Run forward pass on `[uncond_prefix] + [generated_so_far]` → `logits_uncond`
   c. Compute CFG logits: `logits_cfg = logits_uncond + γ * (logits_cond - logits_uncond)`
   d. Apply temperature; sample next token from softmax of `logits_cfg`
4. **Append** the sampled token to `generated`; continue until max_new_tokens or EOS.

## Complexity Analysis

- **Time per token**: 2× forward passes vs 1× for vanilla decoding → roughly 2× inference latency
- **Memory**: No additional model parameters; KV-cache needed for two sequences simultaneously → slightly higher memory than vanilla
- **Training cost**: 0 additional training compute (inference-only method)
- **FLOPs**: Approximately 2× inference FLOPs per token compared to vanilla; empirically shown to be equivalent to running a 2× larger model without CFG (for 5/9 benchmarks, ANCOVA p>0.01)
