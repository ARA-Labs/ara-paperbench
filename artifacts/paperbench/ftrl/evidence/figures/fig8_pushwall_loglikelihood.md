---
# Figure 8: Push-wall Log-likelihood Analysis

**Source**: Figure 8, §5
**Claims**: C01, C02

## Description
Log-likelihood under the fine-tuned policy of trajectories collected using π* on push-wall, i.e., state-action pairs (s, a*) where a* ~ π*(s). Top row: overall push-wall success rates at each checkpoint. Bottom row: 2D PCA projections of the state space, color-coded by log-likelihood values.

## Push-wall Success Rate (Top Row)

| Checkpoint | Success Rate |
|-----------|-------------|
| 0 steps (pre-trained π*) | ~1.0 (100%) |
| 100K steps | ~0.0 (collapsed) |
| 500K steps | ~0.0 (still collapsed) |
| ~4M steps (recovered) | ~0.8 (recovered but different policy) |

## Log-likelihood (Bottom Row — PCA Projections)
- **0 steps**: High log-likelihood (bright colors) uniformly across state space PCA projection
- **100K steps**: High probability assigned to some correct actions in part of state space; overall success rate already collapsed to 0 — "even partial forgetting in the initial stages significantly impacts performance"
- **500K steps**: Log-likelihood values collapse on all expert trajectories; PCA projection shows low values everywhere
- **~4M steps** (recovered): Some regions show recovered log-likelihoods, but values do not reach original levels; fine-tuned agent learned a DIFFERENT policy from π*

## Key Observations
- Rapid collapse: success rate drops to 0 between 0 and 100K steps
- Partial log-likelihood (at 100K) is insufficient to maintain any success — the missing portions matter
- Recovery does not return to original values — irreversible representation change
- This demonstrates that vanilla fine-tuning cannot recover FPC and learns an alternative solution
