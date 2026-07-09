# Heuristics

## H01: Smallest Remaining Demand First (Intra-Group)
- **Rationale**: Within a job group (same eligibility), prioritizing jobs with fewer remaining device needs minimizes average scheduling delay. Analogous to Shortest Remaining Processing Time (SRPT) proven optimal for minimizing average completion time in single-machine scheduling (Garey et al., 1976). Lemma 1 + Appendix C prove this is also globally optimal when combined with the inter-group step.
- **Sensitivity**: low — this is a provably optimal strategy for within-group scheduling.
- **Bounds**: "Remaining resource demand" defaults to current round's unmet demand $D_i$; can optionally use total remaining rounds × demand if future demand is known.
- **Code ref**: [src/execution/venn_scheduler.py]
- **Source**: §4.2.1, Algorithm 1 line 3, Appendix C

## H02: Scarcest Group First (Initial Inter-Group Allocation)
- **Rationale**: Allocating devices to the job group with the fewest eligible devices first prevents resource-rich groups from monopolizing intersection resources and starving resource-scarce groups. This mirrors max-min fairness intuitions but applied to device eligibility rather than bandwidth.
- **Sensitivity**: medium — effectiveness depends on how skewed eligibility distributions are; most impactful when one group is severely resource-constrained.
- **Bounds**: Applied once per scheduling invocation as the initialization step; subsequent cross-group reallocation can override the initial allocation.
- **Code ref**: [src/execution/venn_scheduler.py]
- **Source**: §4.2.2, Algorithm 1 lines 5–9

## H03: Queue-Length-to-Allocated-Resource Ratio for Cross-Group Reallocation
- **Rationale**: When reallocating intersected resources from a scarce group to an abundant group, the ratio $m'_j / |S'_j|$ measures how much scheduling delay improvement can be achieved per device transferred. Transferring resources from a group with lower ratio to one with higher ratio reduces average scheduling delay (proven for two groups in Lemma 2; extended greedily to $n$ groups).
- **Sensitivity**: high — the quality of the $m'$ (affected queue length) estimate directly affects scheduling quality; approximating $m'$ as the group queue length is simpler but may miss cross-group effects.
- **Bounds**: Reallocation stops when the ratio condition fails (Algorithm 1 line 18–19), preventing over-allocation to any single group.
- **Code ref**: [src/execution/venn_scheduler.py]
- **Source**: §4.2.2, Algorithm 1 lines 10–23, Appendix D (Lemma 2)

## H04: Conditional Tier-Based Matching (JCT Reduction Condition)
- **Rationale**: Tier-based matching reduces response time by restricting devices to a homogeneous-capacity tier but increases scheduling delay by factor $V$ (fewer devices to choose from). The condition $1 + c_i > V + c_i g_u$ ensures tier-based matching is applied only when the response time savings outweigh the scheduling delay cost. This avoids worsening JCT under high contention (when scheduling delay dominates).
- **Sensitivity**: high — sensitive to the accuracy of $c_i = T_{\text{resp}} / T_{\text{sched}}$ estimates from previous rounds and to $g_v$ tier speed-up profiles; cold-start jobs (first round) bypass matching entirely.
- **Bounds**: $V$ should be tuned based on resource pool size; Figure 13 shows gains plateau beyond a certain tier count. Randomized tier selection (rather than always best tier) prevents convergence to a subset of devices.
- **Code ref**: [src/execution/venn_scheduler.py]
- **Source**: §4.3, Algorithm 2 lines 6–8, Figure 7, Figure 13

## H05: 24-Hour Eligibility Rate Averaging for Dynamic Supply
- **Rationale**: Device availability follows a diurnal pattern (Figure 2a). Using instantaneous eligibility rates as input to the scheduler leads to oscillating decisions. Averaging over the past 24 hours smooths the signal while preserving the day-level trend, making the scheduler "farsighted" for multi-day CL jobs.
- **Sensitivity**: medium — window length of 24 hours is chosen to match the diurnal period; shorter windows increase variance, longer windows lag behind secular trends.
- **Bounds**: 24-hour window assumed fixed; eligibility history stored in a time-series database queried by the scheduler.
- **Code ref**: [src/execution/venn_scheduler.py]
- **Source**: §4.4 (Dynamic resource supply), Figure 2a
