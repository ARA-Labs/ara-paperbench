# Algorithm

## Mathematical Formulation

### QoE Definition

**S_delay** (Equation 1):
$$S_{\text{delay}} = \sum_{i=1}^{n} (T^{\text{actual}}_i - T^{\text{ideal}}_i)$$

where $T^{\text{actual}}_i$ is the actual consumption timestamp of token $i$, $T^{\text{ideal}}_i$ is the ideal consumption timestamp, and $n$ is total tokens consumed.

**S_whole** (Equation 2):
$$S_{\text{whole}} = \sum_{i=1}^{n} (T^{\text{actual}}_i - T^{\text{ideal}}_{\text{start}})$$

where $T^{\text{ideal}}_{\text{start}}$ is the request submission time. $S_{\text{whole}}$ covers both $S_{\text{delay}}$ and the area below the Actual Consumption Timeline.

**QoE** (Equation 3):
$$\text{QoE} = 1 - \frac{S_{\text{delay}}}{S_{\text{whole}}}$$

Range: QoE ∈ [0, 1]. QoE = 1: perfect. QoE = 0: no tokens delivered.

### QoE Gain (Equation 4):
$$\Delta Q_i = Q_{\text{serve},i}(B) - Q_{\text{wait},i}$$

where $Q_{\text{serve},i}(B)$ is the estimated QoE of request $i$ if served in batch size $B$ for the next $\Delta t$ seconds, and $Q_{\text{wait},i}$ is the estimated QoE if not served for $\Delta t$.

### Scheduling Problem (Equation 5):
$$\max_{x} \sum_{i=1}^{N} (Q_{\text{serve},i}(B) - Q_{\text{wait},i}) \cdot x_i$$

subject to:
$$x_i \in \{0, 1\}, \quad i \in \{1, \ldots, N\}$$
$$\sum_{i=1}^{N} x_i = B$$
$$\sum_{i=1}^{N} l_i x_i \leq M$$

Solved for all $B \in [B_{\min}, B_{\max}]$; the $x$ achieving the maximum across all $B$ is selected.

**Problem hardness**: Weakly NP-Hard (variant of 0/1 knapsack where item values depend on total items selected).

### Priority Score (Equation 6):
$$\pi_i = \frac{Q_{\text{serve},i}(B) - Q_{\text{wait},i}}{l_i}$$

---

## Algorithm 1: Priority-Based Greedy Packing

**Input**: N (number of requests), M (memory capacity), l[N] (context lengths), q[N] (QoE gains), B (target batch size)  
**Output**: x[N] (scheduling decision: 1=serve, 0=wait)  
**Complexity**: O(N log N)

```
for all i in [1, N]:
    p[i] ← q[i] / l[i]           # priority = QoE gain per memory unit

M_current ← 0
N_current ← 0
x[N] ← all zeros

for all i in [1, N] sorted by p[i] descending:
    if M_current + l[i] ≤ M and N_current + 1 ≤ B:
        x[i] ← 1
        M_current ← M_current + l[i]
        N_current ← N_current + 1
    else:
        break

return x
```

Run for all B ∈ [B_min, B_max]; select x* achieving maximum total QoE gain across all B.

---

## Algorithm 2: 3D Dynamic Programming (Optimal, Pseudo-Polynomial)

**Input**: N, M, l[N], q[N], B  
**Output**: x[N]  
**Complexity**: O(M · N²) (pseudo-polynomial; N² from solving for all B ∈ [1, N])

```
Initialize dp[N+1][B+1][M+1] ← -∞
Initialize choice[N+1][B+1][M+1] ← 0
dp[0][0][0] ← 0

for i = 1 to N:
    for b = 0 to min(i, B):
        for m = 0 to M:
            # Option 1: do not serve request i
            if dp[i][b][m] < dp[i-1][b][m]:
                dp[i][b][m] ← dp[i-1][b][m]
                choice[i][b][m] ← 0
            # Option 2: serve request i (if feasible)
            if b ≥ 1 and m ≥ l[i]:
                if dp[i-1][b-1][m-l[i]] + q[i] > dp[i][b][m]:
                    dp[i][b][m] ← dp[i-1][b-1][m-l[i]] + q[i]
                    choice[i][b][m] ← 1

Q_max ← max(dp[N][B][:])
m_current ← index of Q_max in dp[N][B]
b_current ← B
x ← all zeros

for i = N downto 1:
    x[i] ← choice[i][b_current][m_current]
    if x[i] == 1:
        m_current ← m_current - l[i]
        b_current ← b_current - 1

return x[1:]
```

---

## Overhead-Aware Refiner (Algorithm, Informal)

```
Input: greedy decision (A_proposed, P_proposed) sorted by priority
Output: refined decision (A', P')

A' ← {}; P' ← {}

for r_admit in A_proposed (highest priority first):
    find r_preempt ⊆ P_proposed with minimum resources to accommodate r_admit
    overhead ← estimate_latency(preempt r_preempt, admit r_admit)
    delta_t_overhead ← overhead duration
    
    QoE_gain ← Q_serve(r_admit) - Q_wait(r_admit)   # from greedy computation
    QoE_loss ← Σ_{all ongoing r} QoE_loss(r, delta_t_overhead)   # Qwait estimation with Δt=overhead
    
    if QoE_gain > QoE_loss:
        A' ← A' ∪ {r_admit}
        P' ← P' ∪ {r_preempt}
    else:
        break   # no further admissions are profitable

return (A', P')
```

---

## Alternative Objective Functions (Appendix A)

**Max-min QoE** (Equation 7): Item value for request i = `max(Q_min − Q_wait,i, 0)`  
**Maximize requests with perfect QoE** (Equation 8): Item value = `[1(Q_serve,i=1) − 1(Q_wait,i=1)] · 1(Q_current,i=1)`

---

## Token Generation Latency Model

Token generation latency modeled as function of batch size B only, justified by Pearson correlation coefficient of **0.997** between batch size and total context length in a batch (Figure 21, Multi-Round ShareGPT dataset). Eliminates need to track total context length separately.
