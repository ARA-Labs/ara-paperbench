# Algorithm

## Mathematical Formulation

### Model Reprogramming Objective (General)
$$\min_{\theta \in \Theta, \omega \in \Omega} \sum_{i=1}^n \ell\left(f_\text{out}\left(f_P\left(f_\text{in}(x_i^T | \theta)\right) | Y^P_\text{sub}, \omega\right), y_i^T\right)$$

### SMM Input Transformation
$$f_\text{in}(x_i | \varphi, \delta) = r(x_i) + \delta \odot f_\text{mask}(r(x_i) | \varphi)$$

where:
- $r : \mathcal{X}^T \to \mathbb{R}^{d_P}$ is bilinear upsampling
- $f_\text{mask} : \mathbb{R}^{d_P} \to \mathbb{R}^{d_P}$ is the CNN mask generator with parameters $\varphi$
- $\delta \in \mathbb{R}^{d_P}$ is the shared learnable pattern
- $\odot$ denotes element-wise (Hadamard) product

### SMM Training Objective
$$\arg\min_{\varphi \in \Phi, \delta \in \mathbb{R}^{d_P}} \mathbb{E}_{(x_i, y_i) \sim D_T}\left[\ell\left(f_\text{out}\left(f_P\left(r(x_i) + \delta \odot f_\text{mask}(r(x_i)|\varphi)\right)\right), y_i\right)\right]$$

### Approximation Error Definition
$$\text{Err}^\text{apx}_D(\mathcal{F}) = \inf_{f \in \mathcal{F}} \mathbb{E}_{(X,Y) \sim D}[\ell(f(X), Y)] - R^*_D$$

where $R^*_D = \int \left(1 - \sup_{y \in \mathcal{Y}} \Pr(y|x)\right) p_X(x)\, dx$ is the Bayes risk.

### Theorem 4.2 (Approximation Error Monotonicity)
If $\mathcal{F}_1 \subseteq \mathcal{F}_2$, then $\text{Err}^\text{apx}_D(\mathcal{F}_1) \geq \text{Err}^\text{apx}_D(\mathcal{F}_2)$.

### Proposition 4.3 (SMM Lower Approximation Error)
$\mathcal{F}_\text{shr}(f'_P) \subseteq \mathcal{F}_\text{smm}(f'_P)$, therefore $\text{Err}^\text{apx}_{D_T}(\mathcal{F}_\text{shr}(f'_P)) \geq \text{Err}^\text{apx}_{D_T}(\mathcal{F}_\text{smm}(f'_P))$.

**Proof sketch**: Any constant mask $M \in \{0,1\}^{d_P}$ can be represented as a CNN output with zero last-layer weights (output = bias $b_\text{last}$, and $b_\text{last} \in \mathbb{R}^{d_P} \supseteq \{0,1\}^{d_P}$).

---

## Algorithm 1: Visual Reprogramming with SMM

```
Input:  Pre-trained model fP
        Loss function ℓ
        Label-mapping function f_out^(j) for iteration j (ILM)
        Target domain training data {(xi, yi)}_{i=1}^n
        Maximum iterations E = 200
        Learning rates α1 (for δ), α2 (for ϕ)

Output: Optimal δ*, ϕ*

Initialize: ϕ ← random; δ ← 0^dP

for j = 1 to E do
  # Step 1: Update ILM label mapping using current fin
  Compute frequency distribution d using Algorithm 2
  Update f_out^(j) using Algorithm 4

  # Step 2: Forward pass with SMM
  for each batch {(xi, yi)} do
    r_i ← bilinear_upsample(xi)          # resize to dP
    m_i ← CNN_fmask(r_i; ϕ)              # mask generator: → H/2^l × W/2^l × 3
    M_i ← patch_wise_interpolate(m_i, l) # upsample: → H × W × 3
    fin_i ← r_i + δ ⊙ M_i               # apply mask
    logits_i ← fP(fin_i)                 # frozen model
    ŷ_i ← f_out^(j)(logits_i)           # label mapping

  # Step 3: Compute loss and update
  L(δ, ϕ) ← (1/n) Σ ℓ(ŷ_i, yi)
  δ ← δ - α1 · ∇_δ L(δ, ϕ)
  ϕ ← ϕ - α2 · ∇_ϕ L(δ, ϕ)
end for

return δ*, ϕ*
```

## Algorithm 2: Frequency Distribution Computation

```
Input:  Target training set {(xi^T, yi^T)}_{i=1}^n
        Current fin(·|θ), pre-trained model fP

Output: Frequency distribution matrix d ∈ Z^{|YP|×|YT|}

d ← 0^{|YP|×|YT|}
for i = 1...n do
  ŷ_i^P ← fP(fin(xi^T | θ))
  d[ŷ_i^P, yi^T] ← d[ŷ_i^P, yi^T] + 1
end for
return d
```

## Algorithm 4 (ILM): Iterative Label Mapping

```
Input:  YP, YT, training set, fP, total iterations E, lr α

Output: f_out^Ilm,(j) for iteration j

for j = 1...E do
  # Compute frequency distribution with current fin(·|θ^(j))
  d ← Algorithm2(training set, fin(·|θ^(j)))
  
  # Greedily assign source labels to target labels
  YP_sub ← ∅
  f_out^(j) ← 0
  while |YP_sub| < |YT| do
    (yP*, yT*) ← argmax_{yP, yT} d[yP, yT]
    YP_sub ← YP_sub ∪ {yP*}
    f_out^(j)(yP*) ← yT*
    d[yP*, :] ← 0    # prevent duplicate source assignment
    d[:, yT*] ← 0    # prevent duplicate target assignment
  end while
  
  # Train fin for epoch j
  θ^(j+1) ← θ^(j) - α · ∇_θ (1/n) Σ ℓ(f_out^(j)(fP(fin(xi|θ^(j)))), yi)
end for
```

## CNN Mask Generator Architecture

### ResNet-18/50 (5-layer, l=3 MaxPool layers)
```
Input: 224×224×3
Layer 1: Conv(3→8, k=3, p=1, s=1) → BN → ReLU → MaxPool(2×2, s=2)
         Output: 112×112×8
Layer 2: Conv(8→16, k=3, p=1, s=1) → BN → ReLU → MaxPool(2×2, s=2)
         Output: 56×56×16
Layer 3: Conv(16→32, k=3, p=1, s=1) → BN → ReLU → MaxPool(2×2, s=2)
         Output: 28×28×32
Layer 4: Conv(32→64, k=3, p=1, s=1) → BN → ReLU
         Output: 28×28×64
Layer 5: Conv(64→3, k=3, p=1, s=1)
         Output: 28×28×3  [= 224/8 × 224/8 × 3]
Total parameters: 26,499
```

### ViT-B32 (6-layer, l=3 MaxPool layers)
```
Input: 384×384×3
Layer 1: Conv(3→8, k=3, p=1, s=1) → BN → ReLU → MaxPool(2×2, s=2)
         Output: 192×192×8
Layer 2: Conv(8→16, k=3, p=1, s=1) → BN → ReLU → MaxPool(2×2, s=2)
         Output: 96×96×16
Layer 3: Conv(16→32, k=3, p=1, s=1) → BN → ReLU → MaxPool(2×2, s=2)
         Output: 48×48×32
Layer 4: Conv(32→64, k=3, p=1, s=1) → BN → ReLU
         Output: 48×48×64
Layer 5: Conv(64→128, k=3, p=1, s=1) → BN → ReLU
         Output: 48×48×128
Layer 6: Conv(128→3, k=3, p=1, s=1)
         Output: 48×48×3  [= 384/8 × 384/8 × 3]
Total parameters: 102,339
```

## Patch-wise Interpolation

**Input**: Mask of shape $\lfloor H/2^l \rfloor \times \lfloor W/2^l \rfloor \times C$

**Output**: Mask of shape $H \times W \times C$

**Operation**: For each pixel $(i, j)$ in the low-resolution mask, copy its value to the corresponding $2^l \times 2^l$ patch in the output. For pixels near the boundary where the patch extends beyond $H$ or $W$, mirror the nearest available patch value.

**Complexity**: $O(H \cdot W \cdot C)$ copy operations, no arithmetic, no backpropagation required.

**Size formula**: Output size per channel: $\left\lfloor \frac{H}{2^l} \right\rfloor \times \left\lfloor \frac{W}{2^l} \right\rfloor$. Each pixel is expanded to $2^l \times 2^l$.
