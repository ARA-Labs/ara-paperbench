---
# Figures 10–11: AppleRetrieval Toy Example

**Source**: Figures 10–11, Appendix A.2
**Claims**: C01, C02, C06

## Description
Results from APPLERETRIEVAL: a 1D gridworld where the agent must go right to collect an apple (Phase 1, CLOSE) then return home (Phase 2, FAR). Policy: σ(w·o + b) with observation o = -c in Phase 1, o = +c in Phase 2. Pre-trained on Phase 2 only.

## Figure 10: Forgetting vs Distance M (3 subplots)

### Left: Phase 2 Forgetting vs M
- **X-axis**: Training steps
- **Y-axis**: Phase 2 success rate
- **Key**: Larger M → more forgetting; small M (apple nearby) → minimal forgetting; large M (apple far) → catastrophic forgetting

### Center: Overall Success Rate vs M
- **X-axis**: Training steps
- **Y-axis**: Overall task success rate
- **Key**: Larger M → overall performance collapses; small M → agent succeeds

### Right: Phase 2 Probability Early in Training (log scale x-axis)
- **Key**: As M increases, probability of reaching Phase 2 in early training decreases exponentially
- **Note**: x-scale changes for this panel

## Figure 11: Impact of c Parameter (M=30 fixed, 3 subplots)

### Left: Forgetting vs c
- **Key**: Smaller c → greater forgetting of Phase 2; c controls |b|/|w| ratio in learned policy

### Center: Overall Success Rate vs c
- **Key**: Smaller c → lower success rate

### Right: Weight difference (w, b) early in fine-tuning
- **Key**: Lower c encourages pre-trained model to use high |b|/|w| ratio → bias dominates → same bias update affects both phases → greater interference

## Theoretical Insight
If pre-trained policy relies mostly on weight w (|w| >> |b|): minimal interference between phases.
If pre-trained policy relies mostly on bias b (|b| >> |w|): same bias update changes output in both phases → high forgetting.
