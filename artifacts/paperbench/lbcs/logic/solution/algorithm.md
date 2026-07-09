# Algorithm: Lexicographic Bilevel Coreset Selection (LBCS)

## Mathematical Formulation

### Objective Functions
$$f_1(\mathbf{m}) = \frac{1}{n}\sum_{i=1}^n \ell(h(x_i; \theta(\mathbf{m})), y_i) \quad \text{(model performance on full data)}$$

$$f_2(\mathbf{m}) = \|\mathbf{m}\|_0 \quad \text{(coreset size)}$$

### Bilevel Lexicographic Problem
$$\vec{\min}_{\mathbf{m} \in \mathcal{M}} \mathbf{F}(\mathbf{m}) = [f_1(\mathbf{m}), f_2(\mathbf{m})]$$
$$\text{s.t. } \theta(\mathbf{m}) \in \arg\min_\theta L(\mathbf{m}, \theta), \quad L(\mathbf{m},\theta) = \sum_{i=1}^n m_i \ell(h(x_i;\theta), y_i)$$

### Lexicographic Relations
$$\mathbf{F}(\mathbf{m}) \vec{=} \mathbf{F}(\mathbf{m}') \iff f_i(\mathbf{m}) = f_i(\mathbf{m}') \; \forall i \in [2]$$

$$\mathbf{F}(\mathbf{m}) \vec{\prec} \mathbf{F}(\mathbf{m}') \iff \exists i \in [2]: f_i(\mathbf{m}) < f_i(\mathbf{m}') \land (\forall i' < i, f_{i'}(\mathbf{m}) = f_{i'}(\mathbf{m}'))$$

### Optimal Region
$$\mathcal{M}^*_1 = \{\mathbf{m} \in \mathcal{M} : f_1(\mathbf{m}) \leq f^*_1 \cdot (1+\epsilon)\}, \quad f^*_1 = \inf_{\mathbf{m} \in \mathcal{M}} f_1(\mathbf{m})$$
$$\mathcal{M}^*_2 = \{\mathbf{m} \in \mathcal{M}^*_1 : f_2(\mathbf{m}) \leq f^*_2\}, \quad f^*_2 = \inf_{\mathbf{m} \in \mathcal{M}^*_1} f_2(\mathbf{m})$$

### ε-Convergence Theorem (Theorem 2)
Under Conditions 1 (Progressable) and 2 (Stable Moving):
$$P_{t \to \infty}[f_2(\mathbf{m}_t) \leq f^*_2] = 1$$

## Algorithm 1: LBCS

```
Input: network h, dataset D, predefined size k, compromise ε
Initialize: mask m randomly with ‖m‖₀ = k

For t = 1, 2, ..., T:
    1. Inner loop: θ(m) ← argmin_θ L(m, θ)   [train to convergence]
    2. Outer loop: update m using LexiFlow (Algorithm 2)
       - Evaluate f1(m) = (1/n) Σᵢ ℓ(h(xᵢ; θ(m)), yᵢ)
       - Evaluate f2(m) = ‖m‖₀
       - Accept/reject candidate mask via lexicographic comparison

Output: final mask m
```

## Algorithm 2: LexiFlow (Outer Loop)

```
Input: objectives F(·) = [f1(·), f2(·)], compromise ε
Initialize: m0, t' = r = e = 0, δ = δ_init
m* ← m0, H ← {m0}, F_H ← F(m0)

While t = 0, 1, 2, ...:
    Sample u uniformly from unit sphere S
    
    If update(F(m_t + δu), F(m_t), F_H):
        m_{t+1} ← m_t + δu; t' ← t
    Elif update(F(m_t - δu), F(m_t), F_H):
        m_{t+1} ← m_t - δu; t' ← t
    Else:
        m_{t+1} ← m_t; e ← e + 1
    
    H ← H ∪ {m_{t+1}}
    Update F_H (thresholds f̃*₁, f̃*₂)
    
    If e = 2n - 1:
        e ← 0
        δ ← δ · √((t' + 1) / (t + 1))
    
    If δ < δ_lower:   # Random restart
        r ← r + 1
        m_{t+1} ← N(m0, I)
        δ ← δ_init + r

Output: optimal mask m*

Function update(F(m'), F(m), F_H):
    If F(m') ≺_(F_H) F(m) or [F(m') =_(F_H) F(m) and F(m') ≺ F(m)]:
        If F(m') ≺_(F_H) F(m*) or [F(m') =_(F_H) F(m*) and F(m') ≺_l F(m*)]:
            m* ← m'
        Return True
    Return False
```

### Practical Lexicographic Relations (used in Algorithm 2)
$$\mathbf{F}(\mathbf{m}) \vec{=}_{(\mathbf{F}_H)} \mathbf{F}(\mathbf{m}') \iff \forall i: f_i(\mathbf{m}) = f_i(\mathbf{m}') \lor (f_i(\mathbf{m}) \leq \tilde{f}^*_i \land f_i(\mathbf{m}') \leq \tilde{f}^*_i)$$

$$\tilde{f}^*_1 = \hat{f}^*_1 \cdot (1+\epsilon), \quad \tilde{f}^*_2 = \hat{f}^*_2 \quad \text{(computed from history } H\text{)}$$

## Step-by-step Explanation

1. **Initialization**: Start with a random mask m with exactly k ones. This ensures the search starts from a feasible coreset of predefined size.

2. **Inner loop**: Train the proxy network on the current coreset until convergence. This produces θ(m) which is used to evaluate f1.

3. **Mask evaluation**: Compute f1(m) (loss on full dataset with θ(m)) and f2(m) = ‖m‖₀.

4. **LexiFlow outer update**: Perturb the mask along a random direction u (projected to {0,1}^n), evaluate f1 and f2 of the new candidate, accept if it lexicographically dominates the current mask. Update running minimum thresholds.

5. **Step-size adaptation**: Decrease step size when no progress is made for 2n consecutive iterations. Restart randomly if step size falls below δ_lower.

6. **Output**: Return the best-found mask after T iterations.

## Complexity Analysis

- **LBCS**: O(TK) where T = number of outer iterations and K = epochs for one inner-loop training
- **Probabilistic coreset (Zhou et al. 2022)**: O(TKC) where C = number of policy gradient samples (C > 1)
- **LBCS is strictly more efficient** than Probabilistic by a factor of C
