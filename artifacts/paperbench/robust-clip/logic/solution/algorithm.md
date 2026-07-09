# Algorithm

## Mathematical Formulation

### FARE Fine-Tuning Objective

**FARE Loss** (Equation 3):
$$\mathcal{L}_{\text{FARE}}(\phi, x) = \max_{\|z - x\|_\infty \leq \varepsilon} \|\phi(z) - \phi_{\text{Org}}(x)\|_2^2$$

**Outer minimization**:
$$\phi_{\text{FT}} = \arg\min_\phi \frac{1}{n} \sum_{i=1}^n \mathcal{L}_{\text{FARE}}(\phi, x_i)$$

where $(x_i)_{i=1}^n$ is the training set (ImageNet images, **no labels used**).

### TeCoA Baseline Objective (Equation 1, 2)

$$\mathcal{L}_{\text{TeCoA}}(y, f(\phi, x)) = -\log\frac{e^{f_y(\phi,x)}}{\sum_{k=1}^K e^{f_k(\phi,x)}}$$

where $f_k(\phi, x) = \cos(\phi(x), \psi(t_k))$.

$$\phi_{\text{FT}} = \arg\min_\phi \frac{1}{n}\sum_{i=1}^n \max_{\|z-x_i\|_\infty \leq \varepsilon} \mathcal{L}_{\text{TeCoA}}(y_i, f(\phi, z))$$

### Theorem 3.1 (Embedding Preservation)

For original embedding $\phi_{\text{Org}}$, fine-tuned $\phi_{\text{FT}}$, and text encoder $\psi$:
$$|\cos(\phi_{\text{FT}}(x), \psi(t)) - \cos(\phi_{\text{Org}}(x), \psi(t))| \leq \min\left(\frac{1}{\|\phi_{\text{Org}}(x)\|_2}, \frac{1}{\|\phi_{\text{FT}}(x)\|_2}\right) \|\phi_{\text{FT}}(x) - \phi_{\text{Org}}(x)\|_2$$

**Proof sketch**: Follows from adding/subtracting $\phi_{\text{Org}}(x)/\|\phi_{\text{FT}}(x)\|_2$ in the norm, applying triangle inequality and reverse triangle inequality $|\|u\|_2 - \|v\|_2| \leq \|u-v\|_2$.

### Adversarial Classification Formulation (Zero-Shot)

Given class prompts $t_k$ = "A photo of \<class k\>", classifier logit:
$$f_k(\phi, x) = \cos(\phi(x), \psi(t_k)) = \left\langle \frac{\phi(x)}{\|\phi(x)\|_2}, \frac{\psi(t_k)}{\|\psi(t_k)\|_2} \right\rangle$$

Adversarial example $z$ satisfies:
$$\arg\max_k f_k(\phi, z) \neq y, \quad \|z - x\|_\infty \leq \varepsilon, \quad z \in \mathcal{I}$$

## Pseudocode

### FARE Fine-Tuning

```
Algorithm: FARE Fine-Tuning
Input: Training images {x_i}, original encoder φ_Org (frozen),
       ε (perturbation radius), T_pgd (PGD steps), α (PGD step size),
       η (learning rate), epochs
Output: Fine-tuned encoder φ_FT

1. Initialize φ_FT ← φ_Org
2. For epoch = 1, ..., epochs:
   For each mini-batch B = {x_i}:
     a. For each x_i ∈ B:
        // PGD Inner Maximization
        δ_0 ~ Uniform(-ε, ε)^d  (random initialization)
        For t = 1, ..., T_pgd:
          g_t = ∇_δ ||φ_FT(x_i + δ_{t-1}) - φ_Org(x_i)||²₂
          // Momentum PGD
          m_t = 0.9 * m_{t-1} + g_t / ||g_t||₁
          δ_t = δ_{t-1} + α * sign(m_t)
          δ_t = clip(δ_t, -ε, ε)
          δ_t = clip(x_i + δ_t, 0, 1) - x_i  // project to image domain
        z_i = x_i + δ_{T_pgd}
     b. Compute FARE loss:
        L = (1/|B|) Σ_{x_i ∈ B} ||φ_FT(z_i) - φ_Org(x_i)||²₂
     c. Update: φ_FT ← AdamW_step(φ_FT, ∇_φ L, η, β₁=0.9, β₂=0.95, wd=1e-4)
3. Return φ_FT
```

### FARE Zero-Shot Inference
```
Algorithm: Robust Zero-Shot Classification
Input: Image x, fine-tuned encoder φ_FT, text encoder ψ (frozen),
       class names {c_1, ..., c_K}, prompt templates
Output: Predicted class label

1. For k = 1, ..., K:
   t_k = "A photo of " + c_k
   e_k = average over templates: ψ(template(c_k))
   e_k = e_k / ||e_k||₂
2. v = φ_FT(x) / ||φ_FT(x)||₂
3. Return argmax_k <v, e_k>
```

## Complexity Analysis

- **Training cost**: 2 epochs × (1.28M ImageNet images / 128 batch size) × 10 PGD steps × 2 forward-backward passes ≈ 0.2% of original CLIP training (32 epochs × 400M images).
- **Per-iteration cost**: Each training step requires T_pgd + 1 = 11 forward passes through φ_FT and 1 forward pass through φ_Org per image.
- **Memory**: Only φ_FT gradients stored; φ_Org is frozen inference-only. Class token only used (reduces memory vs. all tokens).
- **Inference cost**: Zero overhead compared to original CLIP (identical architecture; only weights differ).
