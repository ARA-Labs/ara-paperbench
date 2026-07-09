# Algorithm

## Mathematical Formulation

### Optimization Objective (Equation 1)
$$\arg\min_{\Theta_T, M_T} \sum_{x,y \in D} \mathcal{L}(x, y | \Theta_T, M_T)$$
$$\text{s.t.} \quad 1 - \frac{C(\Theta_t, M_t)}{C(\Theta_0, M_0)} \geq \gamma_t, \quad \delta(\Theta_t, M_t, R_t) \leq \Delta_t, \quad \forall t \in \{0,1,\ldots,T\}$$

where $C(\cdot)$ is total parameter count, $\delta(\cdot)$ is tuning parameter count, $\gamma_t$ is per-step sparsity constraint, $\Delta_t$ is per-step tuning budget.

### APT Adapter Forward Pass (Equation 2)
$$H_{apt}(X) = m_o \circ (W + s \cdot W_B W_A) X \circ m_i$$

### Outlier-Aware Salience Score (Equations 4–5)
**Step 1 — Activation-gradient salience:**
$$\tilde{S}(W_{:,j}) = \sum_{(x,y) \in D_t} \left|\frac{\partial \mathcal{L}(x,y|\Theta_t,M_t)}{\partial H_{j,i}}\right| \cdot \sum_{(x,y) \in D_t} |H_{j,i}|$$

**Step 2 — Add kurtosis for outliers:**
$$\hat{S}(W_{:,j}) = \tilde{S}(W_{:,j}) + \text{Kurt}(O_{j,:})^{1/2}, \quad O_{:,j} = W_{:,j} \circ X_{j,:}^T$$

**Step 3 — Exponential moving average update:**
$$\bar{S}^{(t)}(m) \leftarrow \beta \bar{S}^{(t-1)}(m) + (1-\beta)\hat{S}(m), \quad \beta = 0.85$$

### APT Adapter Combined Salience (Equation 9)
$$S(H, i) = \sum\left|\frac{\partial\mathcal{L}}{\partial H(X)_{i,l}} \cdot H(X)_{i,l}\right| + \sum\left|\frac{\partial\mathcal{L}}{\partial W_{i,p}} \cdot W_{i,p}\right| + s \cdot \sum\left|\frac{\partial\mathcal{L}}{\partial W_{B_{i,q}}} \cdot W_{B_{i,q}}\right|$$

### Parameter Count (Equations 10–12, RoBERTa-base example)
$$C_{\text{head}} = 4 \times d_m \times d_m / n_h$$
$$C_{\text{neuron}} = 2 \times d_m$$
$$C_{\text{dimension}} = n_L \times (4d_m + 2n_f)$$

### Binary Search Parameter Count (Equation 14)
Given sorted block list, for index $i$:
$$n_h' = \sum_{j=0}^{i-1} \delta(0, f(b_j)), \quad n_f' = \sum_{j=0}^{i-1} \delta(1, f(b_j)), \quad d_m' = \sum_{j=0}^{i-1} \delta(2, f(b_j))$$
$$C_{\text{top-}i} = (4d_h' \cdot n_h' + 2n_f') \cdot d_m'$$

### Cubic Sparsity Schedule
$$\gamma_t = \gamma_T + (1 - \gamma_T)\left(1 - \frac{t}{T}\right)^3$$

### Adaptive Tuning Rank Update
$$r_{apt}' = \left\lfloor r_{apt} \cdot \frac{\Delta_{t'}}{\Delta_t} \right\rfloor$$

### Self-Distillation Loss (Equations 7)
$$\mathcal{L}_{\text{layer}} = \sum_{i=1}^{4} \text{MSE}\left(\text{Tr}(H_s^{\phi(i)}), H_t^i\right)$$
$$\mathcal{L} = \mu \mathcal{L}_{\text{distill}} + (1-\mu)\mathcal{L}_{\text{ft}}$$

## Pseudocode (Algorithm 1)

```
Algorithm: Adaptive Pruning and Tuning (APT)
Input:
  - f: pre-trained LM with APT adapters inserted
  - D: task dataset
  - T: total training steps (pruning phase)
  - T_adj: set of steps at which parameters are adjusted
  - γ_T: target sparsity
  - Δ_max: maximum tuning budget
  - α = 0.01: mask update rate
  - β = 0.85: EMA decay for salience
  - s = 2: LoRA scaling factor

Pruning Phase (steps t = 1 to T):
  for t = 1 to T:
    1. FORWARD: L ← L(f(Θ_t, D_t))  [with distillation if μ > 0]
    2. CACHE: H̃ ← Σ_{i,j} |H|_{ij}  [batch-sequence summed hidden states]
    3. BACKWARD: ∇_Θ L ← ∂L / ∂Θ_t
    4. SALIENCE: S̃(m_i) ← H̃ · Σ_{i,j} |∇_H L|_{ij}
    5. EMA UPDATE: S̄^(t)(m) ← β·S̄^(t-1)(m) + (1-β)·Ŝ(m)
    6. if t in T_adj:
         COMPUTE γ_t = γ_T + (1-γ_T)·(1 - t/T)^3
         SELECT BLOCKS:
           Sort all blocks by ρ(b) = S̄(b) / C(b) [descending]
           Binary search for top-i blocks satisfying γ_t constraint
         UPDATE MASKS:
           For retained blocks: M^(t) ← min(1, M^(t-1) + α)
           For pruned blocks:   M^(t) ← max(0, M^(t-1) - α)
         ADAPTIVE TUNING:
           Compute I(H_apt) = Σ_{i,j} S(W_{B_{i,j}}) for each adapter
           Sort adapters by I; identify top-half
           For top-half adapters: r_apt' = ⌊r_apt · Δ_{t'}/Δ_t⌋
           Concatenate N(0,σ²) rows to W_A; zeros to W_B
           Reset optimizer state
    7. PARAM UPDATE: Θ_{t+1} ← Θ_t - η·∇_Θ L

Recovery Fine-Tuning Phase (T steps, L_ft only):
  Fine-tune Θ_T with fixed pruned structure using only L_ft

Inference:
  Merge: W_merged ← W + s · W_B W_A
  Remove pruned blocks (mask = 0); return reduced model
```

## Complexity Analysis

- **Salience computation**: O(batch_size × seq_len × hidden_dim) per step — same order as forward pass
- **Block sorting**: O(N log N) where N = total number of blocks (MHA heads + FFN neurons + 1 dimension per layer)
- **Binary search**: O(log N) for mask selection given sorted blocks
- **Rank update**: O(top-half adapters × (d_i + d_o)) for matrix extension — negligible vs forward pass
- **Memory overhead**: Salience computed by summing along batch dimension before multiplying (reduces from O(batch × seq × hidden) to O(seq × hidden))
- **RoBERTa-base block counts**: 12 layers × 12 heads = 144 head blocks; 12 × 3072 = 36,864 neuron blocks; 1 dimension block
