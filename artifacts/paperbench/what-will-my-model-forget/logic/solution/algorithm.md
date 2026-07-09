# Algorithm

## Mathematical Formulation

### Problem Setup
Let $f_0$ be the base pretrained LM with parameters $\theta_0$. Given an online learning example $\langle x_i, y_i \rangle$ with $f_0(x_i) \neq y_i$, the updated model is $f_i$ obtained via $K$ gradient steps starting from $f_0$.

**Exact Match score**: $\text{EM}_{D,f} = |\{\langle x,y\rangle \in D \mid f(x) = y\}| / |D|$

**Forecasting task**: Binary classification $g: \langle x_i, y_i\rangle, \langle x_j, y_j\rangle \mapsto z_{ij} \in \{0,1\}$ where $z_{ij}=1$ iff $x_j$ is forgotten upon learning $x_i$.

### Logit-Change Transfer Derivation (Eqn. 2)

From the first-order Taylor expansion after one gradient step with learning rate $\eta$:

$$\theta_i - \theta_0 = -\eta \nabla_\theta \hat{f}_0(x_i) \nabla_{\hat{f}_0(x_i)} \mathcal{L}(x_i, y_i)$$

The logit change of any example $x_j$:

$$\Delta\hat{f}_i(x_j) = -\eta \Theta(x_j, x_i) \mathcal{L}(x_i, y_i)$$

where $\Theta(x_j, x_i) = \nabla_\theta \hat{f}_0(x_j) \nabla_\theta \hat{f}_0(x_i)^T \in \mathbb{R}^{TV \times TV}$.

Combining the logit changes of $x_j$ and $x_i$:

$$\hat{f}_i(x_j) - \hat{f}_0(x_j) = \Theta(x_j, x_i)\Theta^{-1}(x_i, x_i)\left[\hat{f}_i(x_i) - \hat{f}_0(x_i)\right] \tag{Eqn. 2}$$

### Trainable Kernel Approximation

Replace the full NTK with a trainable low-rank approximation:

$$\tilde{\Theta}(x_j, x_i) = h(x_j, y_j) h(x_i, y_i)^T \in \mathbb{R}^{T \times T}$$

Predicted updated logits of $x_j$:

$$\hat{f}_i(x_j) = \tilde{\Theta}(x_j, x_i)\left[\hat{f}_i(x_i) - \hat{f}_0(x_i)\right] + \hat{f}_0(x_j)$$

**Margin loss** (Eqn. 3):

$$\mathcal{L}(\langle x_i, y_i\rangle, \langle x_j, y_j\rangle, z_{ij}) = \max\left(0,\ 1 + (-1)^{z_{ij}} \left(\max_{v \neq y_j} \hat{f}_i(x_j)[v] - \hat{f}_i(x_j)[y_j]\right)\right)$$

### Representation-Based Forecasting (Eqn. 4)

$$g(\langle x_i, y_i\rangle, \langle x_j, y_j\rangle) = \sigma\left(h(x_j, y_j) h(x_i, y_i)^T + b_j\right)$$

where $h: (x,y) \mapsto \mathbb{R}^d$ averages token representations, and the frequency prior is:

$$b_j = \log\frac{|\{⟨x_i,y_i⟩ \in D^{\text{train}}_R \mid z_{ij}=1\}|}{|D^{\text{train}}_R|} - \log\frac{|\{⟨x_i,y_i⟩ \in D^{\text{train}}_R \mid z_{ij}=0\}|}{|D^{\text{train}}_R|}$$

Optimized with binary cross-entropy loss.

## Pseudocode

### Algorithm 1: Train Logit-Based Forecasting Model

```
Input: D^train_R, DPT, f0, max_steps T
Output: Trained encoding function h: R^T → R^{T×H}

Initialize h (PTLM + 2-layer MLP)
for step in 1..T:
    (xi, yi) ← sample(D^train_R)
    (xj, yj) ← sample(DPT)
    
    # Get logits from base model
    f̂0_xi ← f0.logits(xi)
    f̂0_xj ← f0.logits(xj)
    
    # Fine-tune copy of f0 on (xi, yi)
    fi ← FineTune(f0, (xi, yi), K_steps, lr)
    f̂i_xi ← fi.logits(xi)
    f̂i_xj ← fi.logits(xj)
    
    # Ground truth forgetting
    zij ← 1 if fi(xj) ≠ yj else 0
    
    # Compute trainable kernel
    Θ̃ ← h(xj, yj) @ h(xi, yi).T  # [T × T]
    
    # Predict updated logits of xj
    f̂i_xj_pred ← Θ̃ @ (f̂i_xi - f̂0_xi) + f̂0_xj
    
    # Margin loss (Eqn. 3)
    loss ← max(0, 1 + (-1)^zij * (max_{v≠yj} f̂i_xj_pred[v] - f̂i_xj_pred[yj]))
    loss.backward(); optimizer.step()
```

### Algorithm 2: Inference with Logit-Based Forecasting

```
Input: (xi, yi) ∈ D^Test_R, DPT, f0, trained h, cached h(xj,yj) for xj ∈ DPT
Output: Predicted ẑij for all (xj, yj) ∈ DPT

h_xi ← h(xi, yi)
f̂0_xi ← f0.logits(xi)
fi ← FineTune(f0, (xi, yi), K_steps, lr)
f̂i_xi ← fi.logits(xi)
Δlogit_xi ← f̂i_xi - f̂0_xi

for (xj, yj) ∈ DPT:
    h_xj ← cached h(xj, yj)  # pre-computed
    Θ̃ ← h_xj @ h_xi.T
    f̂i_xj_pred ← Θ̃ @ Δlogit_xi + f̂0_xj  # cached f̂0_xj
    ẑij ← 1 if argmax(f̂i_xj_pred) ≠ yj else 0
```

### Algorithm 3: Train Representation-Based Forecasting Model

```
Input: D^train_R, DPT, f0, max_steps T, positive weight α=0.1
Output: Trained h: R^T → R^d

Initialize h (PTLM + 2-layer MLP)
Compute frequency priors bj for all (xj,yj) ∈ DPT

while not converged:
    # Sample balanced mini-batch: 8 positive + 8 negative pairs
    batch ← SamplePairs(D^train_R, DPT, n_pos=8, n_neg=8)
    
    for ((xi,yi), (xj,yj), zij) in batch:
        h_xi ← h(xi, yi)  # averaged token reps
        h_xj ← h(xj, yj)
        p̃ij ← σ(h_xj · h_xi + bj)
        
        weight ← α if zij==1 else 1.0
        loss += weight * BCE(p̃ij, zij)
    
    loss.backward(); optimizer.step()
```

### Algorithm 4: Inference with Representation-Based Forecasting

```
Input: (xi, yi) ∈ D^Test_R, DPT, trained h, cached h(xj,yj), cached bj
Output: Predicted ẑij for all (xj, yj) ∈ DPT

h_xi ← h(xi, yi)

for (xj, yj) ∈ DPT:
    h_xj ← cached h(xj, yj)
    p̃ij ← σ(h_xj · h_xi + bj)
    ẑij ← 1 if p̃ij > 0.5 else 0
```

## Complexity Analysis

| Method | Inference Complexity | Notes |
|--------|---------------------|-------|
| Threshold | $O(N_{PT})$ | Look up pre-counted forgetting frequencies |
| Fixed Logit | $O(N_{PT} T^2 (H+V))$ | Kernel computation + logit prediction |
| Trainable Logit | $O(N_{PT} T^2 (H+V))$ | Same as fixed logit |
| Representation | $O(N_{PT} H)$ | Inner product of $d$-dim vectors |
| GT (Head-only) | $O(N_{PT} T H V)$ | Full inference with updated LM |
| GT (Full FT) | $O(F_w(N_{PT}))$ | Full LM forward passes with all updated params |

Where $N_{PT}$ = number of upstream examples, $T$ = max output length, $H$ = hidden dim, $V$ = vocab size.
