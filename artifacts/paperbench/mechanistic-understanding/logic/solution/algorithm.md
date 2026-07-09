# Algorithm

## 1. Toxicity Probe Training

**Objective**: Train $W_\text{Toxic} \in \mathbb{R}^d$ to classify toxic vs. non-toxic text.

$$P(\text{Toxic} | \bar{x}^{L-1}) = \text{softmax}(W_\text{Toxic} \bar{x}^{L-1})$$

where $\bar{x}^{L-1} = \frac{1}{T}\sum_{t=0}^{T-1} x_t^{L-1}$ is the mean residual stream at the last layer.

**Pseudocode**:
```
Input: Jigsaw dataset {(comment_i, label_i)}, GPT2-medium
Output: W_Toxic ∈ R^d

for each (comment, label) in training set:
    tokens = tokenize(comment)
    x^{L-1}_t for all t = GPT2_forward(tokens)  # all layer outputs
    x_bar = mean(x^{L-1}, axis=time)
    logits = softmax(W_Toxic @ x_bar)
    loss = cross_entropy(logits, label)
    W_Toxic = W_Toxic - lr * grad(loss, W_Toxic)
```

## 2. Toxic Vector Extraction

**Objective**: Find value vectors that promote toxicity.

$$\text{MLP.v}_\text{Toxic} = \text{top-}N \{v_i^\ell : \forall \ell \in [0,L), i \in [0, d_\text{mlp})\}, \quad \text{ranked by } \cos(v_i^\ell, W_\text{Toxic})$$

$$\text{SVD.U}_\text{Toxic} = \text{svd}(\text{stack}(\text{MLP.v}_\text{Toxic}))[0]$$

## 3. MLP Decomposition (Geva et al., 2022)

The MLP output decomposes into $d_\text{mlp}$ sub-updates:

$$\text{MLP}^\ell(x^\ell) = \sum_{i=1}^{d_\text{mlp}} \underbrace{\sigma(x^\ell \cdot k_i^\ell)}_{m_i^\ell} v_i^\ell$$

Influence on token $w$ probability:

$$P(w | x^\ell + m_i^\ell v_i^\ell, E) \propto \exp(e_w \cdot x^\ell) \cdot \exp(e_w \cdot m_i^\ell v_i^\ell)$$

When $e_w \cdot m_i^\ell v_i^\ell > 0$: token $w$ probability increases; when $< 0$: decreases.

## 4. DPO Fine-tuning

$$\mathcal{L}_\text{DPO} = -\mathbb{E}\left[\log \sigma\left(\beta \log \frac{\pi_\theta(y^+|w)}{\pi_\text{ref}(y^+|w)} - \beta \log \frac{\pi_\theta(y^-|w)}{\pi_\text{ref}(y^-|w)}\right)\right]$$

- $y^+$: non-toxic continuation (greedy GPT2 on Wikitext-2 prompt)
- $y^-$: toxic continuation (PPLM-generated using WToxic)
- $\beta = 0.1$, lr = 1e-6, optimizer = RMSProp, batch size = 4, max_grad_norm = 10

## 5. Residual Stream Intervention

During generation, subtract toxic vector from last layer:

$$x^{L-1} \leftarrow x^{L-1} - \alpha \cdot W$$

where $W \in \{\text{WToxic}, \text{MLP.v19}, \text{SVD.U}_\text{Toxic}[0]\}$ and $\alpha$ is chosen to match GPT2DPO perplexity.

## 6. Activation Region and Residual Shift

MLP activation region:
$$\gamma(k_i^\ell) := \{g \mid g \in \mathbb{R}^d,\ \sigma(k_i^\ell \cdot g) > 0\}$$

Residual stream shift:
$$\delta^{\ell\text{mid}} = x_\text{DPO}^{\ell\text{mid}} - x_\text{GPT2}^{\ell\text{mid}}$$

Cosine similarity between value vector shifts and residual shift:
$$\forall j < \ell,\ \forall i < d_\text{mlp}: \cos(\delta^{\ell\text{mid}}, \delta^j_{\text{MLP.v}_i})$$

**Key result**: $\delta_{\text{MLP.v}}$ and $\delta_x$ are antipodal (high negative cosine similarity), because:
- Most neurons are inactive (negative GeLU activation near 0)
- $m_i \approx -\epsilon$ (small negative), so $m_i \cdot \delta v_i$ flips direction: contributes to $+\delta_x$

## 7. Un-alignment Attack

$$k_i^\ell \leftarrow \lambda \cdot k_i^\ell \quad \forall (k_i^\ell, v_i^\ell) \in \text{top-}7\ \text{MLP.k}_\text{Toxic}$$

where $\lambda = 10$. This expands $\gamma(k_i^\ell)$, causing DPO's shifted residual stream to re-enter toxic regions.

**Complexity**: $O(7 \cdot d)$ — trivial weight modification, no retraining.

## 8. PPLM Data Generation

$$p(y|a) \propto p(y) \cdot p(a|y)$$

PPLM uses gradient of $\log p(a|y)$ w.r.t. activations to steer generation:
$$\tilde{H}_t = H_t + \Delta H_t, \quad \Delta H_t \propto \nabla_{H_t} \log p_c(a|x)$$

Parameters: step_size=0.4, decay=FALSE, gm_scale=0.95, kl_scale=0.1.
