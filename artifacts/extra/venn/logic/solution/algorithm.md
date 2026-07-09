# Algorithm

## Mathematical Formulation

### Problem: Intersection Resource Scheduling (IRS)

**Variables:**
- $J = \{J_1, \ldots, J_m\}$: set of $m$ CL jobs
- $D = \{D_1, \ldots, D_m\}$: resource demands (number of devices per round)
- $S = S_1 \cup \cdots \cup S_n$: device pool partitioned into eligibility subsets
- $f(J_i) = S_k$: maps job $J_i$ to its eligible device subset
- $e_{ij} \in \{0,1\}$: eligibility matrix ($e_{ij}=1$ iff device $i$ is eligible for job $j$)
- $x_{ij} \in \{0,1\}$: assignment ($x_{ij}=1$ iff device $i$ is assigned to job $j$)
- Devices arrive at times $t_1, t_2, \ldots, t_q$

**ILP Constraints (Appendix B):**
$$\sum_{j=1}^{m} x_{ij} \leq 1, \quad \forall i \in [1,q] \quad \text{(each device assigned to at most one job)}$$
$$\sum_{j=1}^{m} x_{ij} \cdot e_{ij} \leq 1, \quad \forall i \in [1,q] \quad \text{(eligibility respected)}$$
$$\sum_{i=0}^{q} x_{ij} = D_j, \quad \forall j \in [1,m] \quad \text{(demand satisfied)}$$

**Objective (minimize average scheduling delay):**
$$\min \sum_{j=1}^{m} T_j, \quad T_j = \max_i (x_{ij} \cdot t_i)$$

This is NP-hard (reduces to integer multi-commodity flow, Even et al., 1975).

### Tier-Based Matching Condition

Apply tier-based matching to job $J_i$ if and only if:
$$1 + c_i > V + c_i \cdot g_u$$
where $c_i = T_{\text{resp}} / T_{\text{sched}}$, $V$ is the number of tiers, and $g_u = t_u / t_0$ is the speed-up factor for tier $u$ (95th-percentile response time ratio).

### Starvation Prevention

Fair-share JCT: $T_i = M \cdot sd_i$

Adjusted demand: $d'_i = d_i \cdot \left(\frac{t_i}{T_i}\right)^\varepsilon$

Adjusted group queue length: $q'_j = q_j \cdot \left(\frac{\sum_{J_i \in G_j} T_i}{\sum_{J_i \in G_j} t_i}\right)^\varepsilon$

## Pseudocode

### Algorithm 1: Intersection Resource Scheduling (Venn-Sched)

```
Input: Job Groups G = {G1, ..., Gn}, Devices S

// Step 1: Sort within each job group by ascending remaining demand
for Gj in G:
    sort Ji ∈ Gj by Di in ascending order

// Step 2: Generate initial allocation (scarcest group first)
S = union of all Sj
sort Gj by |Sj| in ascending order  // scarcest group first
for Gj in G:
    S'j = S ∩ Sj
    S = S \ S'j  // remove allocated devices

// Step 3: Greedily reallocate intersected resources
sort Gj by |Sj| in descending order  // most abundant group first
for Gj in G:
    if |S'j| > 0:
        for Gk in G where |Sk| < |Sj| and Sk ∩ Sj ≠ ∅:
            m'j, m'k = get-queue-len()
            if m'j / |S'j| > m'k / |S'k|:
                S'j = S'j ∪ (Sj ∩ Sk)
                S'k = S'k - S'j
            else:
                break

Return {Gj[0], S'j} for all j  // first job in each group + its allocated devices
```

### Algorithm 2: Device Matching (Venn-Match)

```
Input: Jobs Ji, Devices S'j from Venn-Sched(G, S)

// Partition devices into V tiers by hardware capability
S = {S1, S2, ..., SV}  // evenly partition by hardware score

// Compute speed-up factors from profiling
gv = tv / t0 for v in [1, V]  // 95th-percentile response time ratio

Function Venn-Match(Job Ji, Resource S'j):
    ci = T_response / T_schedule  // from previous round profile

    // Randomly select a tier
    u = randint(0, V)

    // Apply tier-based matching only if it reduces JCT
    if V + gu * ci < ci + 1:
        S'j = S'j ∩ Su  // restrict to tier u devices
    
    Return {Ji, S'j}
```

## Step-by-Step Explanation

**Algorithm 1:**
1. **Intra-group sort**: Within each group, smallest-remaining-demand jobs go first. This is proven optimal for average scheduling delay within a group (analogous to Shortest Remaining Processing Time).
2. **Initial allocation**: Allocate resources starting from the group with the fewest eligible devices (scarcest). This ensures scarce-resource groups get first pick, preventing starvation of high-demand-diversity jobs.
3. **Cross-group reallocation**: For groups with abundant resources, check if acquiring intersected resources from scarcer groups reduces average scheduling delay. The ratio $m'_j / |S'_j|$ measures the "pressure" (affected jobs per allocated device). If the requesting group has higher pressure than the donor group, reallocation helps average JCT.

**Algorithm 2:**
1. Tier partitioning groups devices by hardware score into V equal buckets.
2. Speed-up profiling uses 95th-percentile tail latency to represent response collection time per tier.
3. The condition gates tier assignment: tier-based matching increases scheduling delay by factor $V$ but reduces response time by factor $g$. It is applied only when the net effect is a JCT reduction.
4. Randomized tier selection (vs. always picking the best tier) ensures each job sees device diversity across rounds, avoiding model bias toward data from high-end devices.

## Complexity Analysis
- **Algorithm 1**: $\max(O(m \log m), O(n^2))$ where $m$ = number of jobs, $n$ = number of job groups
  - $O(m \log m)$: sorting jobs within groups
  - $O(n^2)$: pairwise comparison of job groups in cross-group reallocation
- **Algorithm 2**: $O(V)$ per job (tier profiling and assignment)
- **Overall**: Linear in the number of jobs (per scheduling event), scalable to 1000+ jobs with sub-millisecond latency (Figure 10)
