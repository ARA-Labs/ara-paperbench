# Constraints and Limitations

## Boundary Conditions

### BC1: Centralized Scheduler Assumption
- **Description**: Venn requires a centralized server that all devices check in to and that has global visibility of all active CL jobs. This is analogous to the centralized designs of Meta (Huba et al., 2022) but differs from Apple's client-driven design (Paulik et al., 2021).
- **When it holds**: Cloud-managed CL deployments (Google, Meta production systems).
- **When it fails**: Fully decentralized CL where there is no central coordinator.

### BC2: Synchronous CL Assumption (Primary Focus)
- **Description**: The paper primarily evaluates synchronous CL where each round requires at least 80% of target participants to respond within a 5–15 min deadline. Scheduling decisions depend on "remaining resource demand."
- **When it holds**: Standard synchronous federated learning (Yang et al., 2018; Bonawitz et al., 2019).
- **When it fails**: Asynchronous CL where participation windows overlap. The paper notes asynchronous CL is compatible with Venn's scheduling decisions (which depend only on remaining resource demand, not submission timing), but does not evaluate it.

### BC3: Discrete Eligibility Categories
- **Description**: The evaluation stratifies devices into 4 discrete categories (General, Compute-Rich, Memory-Rich, High-Performance) based on CPU/memory thresholds. The IRS formulation assumes discrete job groups.
- **When it holds**: When hardware requirements create natural thresholds.
- **When it fails**: Continuous or high-dimensional device eligibility spaces (e.g., fine-grained numerical thresholds on dozens of features).

### BC4: Tier-Based Matching Requires Historical Profile Data
- **Description**: Algorithm 2 requires per-tier response time profiles from previous rounds ($g_v = t_v / t_0$). First-round jobs skip tier-based matching.
- **When it holds**: Multi-round CL jobs that have completed at least one round.
- **When it fails**: Single-round jobs or first-round of any new CL job (cold start).

### BC5: Log-Normal Response Time Distribution
- **Description**: Venn models device response time as log-normally distributed and uses the 95th percentile as tail latency for tier speed-up computation.
- **When it holds**: Consistent with empirical CL deployment data (Wang et al., 2023).
- **When it fails**: Highly bimodal or heavy-tailed response distributions beyond log-normal.

## Known Limitations

### L1: Scheduling Optimality Guarantee is Limited to Two Job Groups
- **Description**: Lemma 2 proves optimality of Venn's inter-group scheduling only for the two-group case. For $n > 2$ groups, Venn applies a greedy pairwise comparison that is not proven globally optimal.
- **Impact**: Near-optimal in practice (as shown by simulation results) but no formal bound for general $n$.

### L2: Starvation Prevention Trades JCT for Fairness
- **Description**: Enabling starvation prevention (any $\varepsilon > 0$) reduces average JCT improvement. At $\varepsilon=2$, 69% of jobs meet fair-share JCT, but average JCT speedup decreases compared to $\varepsilon=0$.
- **Impact**: Operators must tune $\varepsilon$ based on their JCT vs. fairness tradeoff requirements.

### L3: Device Fault Tolerance Delegated to CL Jobs
- **Description**: Venn does not handle device dropouts during training. This responsibility is delegated to individual CL jobs (e.g., overcommit decisions).
- **Impact**: If a CL job's fault tolerance policy is suboptimal, Venn's assignments may not translate to completed rounds.

### L4: No Cross-Round Global Optimization
- **Description**: Venn optimizes per-round scheduling independently. It does not jointly optimize JCT across multiple rounds of the same job (e.g., no lookahead for future device availability).
- **Impact**: Multi-round efficiency is approximated by using 24-hour averaged eligibility rates, not exact future predictions.

### L5: Evaluation Scale
- **Description**: Simulation uses up to 50 jobs; real testbed uses 20 jobs. Production CL systems may handle hundreds of concurrent jobs.
- **Impact**: $O(n^2)$ inter-group complexity may become a bottleneck if the number of distinct eligibility categories grows very large.
