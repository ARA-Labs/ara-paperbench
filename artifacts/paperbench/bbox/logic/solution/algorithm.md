# Algorithm

## Mathematical Formulation

### EBM Parameterization
The adapted model distribution:

$$p_\theta(y|x) = \frac{p_{LLM}(y|x)\exp(g_\theta(x,y))}{Z_\theta(x)}$$

where $Z_\theta(x) = \int p_{LLM}(y|x)\exp(g_\theta(x,y))dy$ is intractable.

### Ranking-Based NCE Objective
Minimize KL divergence between parameterized posterior and data-to-noise ratio:

$$\min_\theta \ell(\theta) = \max_\theta \mathbb{E}_{p_{data}(x)}\left[g_\theta(x) - \log\sum_{k}\exp(g_\theta(x_k))\right] \quad (2)$$

Optimal solution: $p_\theta(x) := p_{LLM}(x)\exp(g_\theta(x)) = p_{data}(x)$

### NCE Loss Gradient (with Spectral Normalization)
$$\nabla_\theta\ell(\theta) = \nabla_\theta\left\{-\mathbb{E}_{y^+\sim p_{data}(y|x)}[g_\theta(x,y^+)] + \alpha\mathbb{E}[g_\theta(x,y^+)^2] + \mathbb{E}_{y^-\sim p_\theta(y|x)}[g_\theta(x,y^-)] + \alpha\mathbb{E}[g_\theta(x,y^-)^2]\right\} \quad (3)$$

### Adapted Inference
$$p_\theta(y|x) = p_\theta(s_{1:L}|x) = \exp(g_\theta(s_{1:L},x))\prod_l p_{LLM}(s_l|x,s_{1:l-1}) \quad (4)$$

### Online Sampling
$$\{\hat{y}_{i,m}\}_{m=1}^M \sim p_{\theta_t}(y|x_i) \quad (4)$$

$$y^{(t)}_{i+} = \text{SEL}(y^{(t-1)}_{i+}, \{\hat{y}_{i,m}\}_{m=1}^M) \quad (5)$$

$$y^{(t)}_{i-} = \{\hat{y}_{i,m} | \hat{y}_{i,m} \neq y^{(t)}_{i+}\}_{m=1}^M \quad (6)$$

$$\theta_{t+1} = \theta_t - \eta\nabla_\theta\ell(\theta_t) \quad (7)$$

---

## Pseudocode

### Algorithm 1: BBOX-ADAPTER Online Adaptation

```
Input:
  D = {(x_i, y_i)}_{i=1}^N  — SFT dataset
  p_LLM                       — unadapted black-box LLM (fixed)
  T                           — number of iterations
  η = 5e-6                    — learning rate
  M (= beam_size = 3)         — number of beams / candidates sampled per step
  K                           — initial candidates per query

Initialize:
  θ_0 ← random initialization

# --- Initialization Phase ---
For each i = 1..N:
  Sample K candidates: {y_{i,j}}_{j=1}^K ~ p_LLM(y|x_i)
  y^(0)_{i+} = SEL({y_{i,j}}, feedback=ground_truth_or_AI)
  y^(0)_{i-} = {y_{i,j} | j ≠ argmax}

# --- Iterative Adaptation ---
For t = 0..T-1:
  For each i = 1..N:
    # Step 1: Sample from adapted inference
    {ŷ_{i,m}}_{m=1}^M ~ p_θt(y|x_i)  [via beam search, Eq.4]
    
    # Step 2: Update positive samples
    y^(t)_{i+} = SEL(y^(t-1)_{i+}, {ŷ_{i,m}})  [Eq.5]
    
    # Step 3: Update negative samples
    y^(t)_{i-} = {ŷ_{i,m} | ŷ_{i,m} ≠ y^(t)_{i+}}  [Eq.6]
  
  # Step 4: Compute NCE gradient
  ∇_θ ℓ(θ_t) using y^(t)_{i+} and y^(t)_{i-} via Eq.3
  
  # Step 5: Update adapter
  θ_{t+1} = θ_t - η * ∇_θ ℓ(θ_t)  [Eq.7, AdamW, batch=64, steps=6000]

Output: θ_T (fine-tuned adapter)
```

### Adapted Inference (Sentence-Level Beam Search)

```
Input: x, adapter g_θ, beam_size k=3, candidates_per_beam n
Output: best answer y*

Initialize beams: B = [("", 0.0)]  # (partial_sequence, score)

While not all beams terminated:
  candidates = []
  For each beam b in B:
    # Sample n next sentences from LLM
    For j = 1..n:
      s_new ~ p_LLM(s_l | x, b.prefix)
      candidates.append((b.prefix + s_new, g_θ(x, b.prefix + s_new)))
  
  # Prune to top-k by adapter score
  B = top_k(candidates, k=k, key=score)
  
  # Check stop signals (e.g., "####" terminator, L steps reached)

Return: argmax_{b in B} g_θ(x, b.sequence)
```

## Complexity Analysis

- **Training**: $O(T \cdot N \cdot M \cdot C_{LLM} + T \cdot N \cdot C_{adapter})$ where $C_{LLM}$ is the cost of one LLM API call and $C_{adapter}$ is one adapter forward-backward pass. Adapter training dominates at 6000 steps with batch size 64.
- **Inference (single-step)**: $O(n \cdot C_{LLM} + n \cdot C_{adapter})$ per question — one round of LLM proposals + adapter scoring.
- **Inference (full-step)**: $O(L \cdot n \cdot k \cdot C_{LLM} + L \cdot n \cdot k \cdot C_{adapter})$ per question — scales with sentence count $L$ and beam size $k$.
- **Adapter size**: 86M–304M parameters; significantly smaller than the black-box LLM.
