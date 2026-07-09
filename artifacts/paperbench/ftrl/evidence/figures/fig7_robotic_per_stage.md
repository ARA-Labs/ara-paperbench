---
# Figure 7: RoboticSequence Per-Stage Success Rates

**Source**: Figure 7, §5
**Claims**: C01, C02, C03, C05

## Description
Success rate for each of the four sub-tasks in RoboticSequence throughout fine-tuning. Pre-trained π* was trained on peg-unplug-side and push-wall (FAR); hammer and push are CLOSE (new) tasks.

## Stage: hammer (CLOSE — new task)

| Method | Within 1e6 steps | Final |
|--------|-----------------|-------|
| Fine-tuning + BC | >90% | maintained |
| Fine-tuning + EM | >90% | maintained |
| Fine-tuning + EWC | >90% | maintained |
| Vanilla fine-tuning | >90% | maintained |
| Training from scratch | >90% | maintained |
| Pre-trained π* (frozen) | ~0% | ~0% (no knowledge of CLOSE) |

## Stage: push (CLOSE — new task)

| Method | At end of training | Notes |
|--------|-------------------|-------|
| Fine-tuning + BC | >80% | Learns faster than scratch |
| Fine-tuning + EM | >80% | Learns faster than scratch |
| Fine-tuning + EWC | >80% | Learns faster than scratch |
| Vanilla fine-tuning | >80% | Learns faster than scratch |
| Training from scratch | >80% | Slowest convergence |
| Pre-trained π* (frozen) | ~0% | No knowledge of CLOSE |

## Stage: peg-unplug-side (FAR — pre-trained)

| Method | At 1e6 steps | Final | Notes |
|--------|-------------|-------|-------|
| Pre-trained π* (frozen) | ~100% | ~100% | Static reference |
| Fine-tuning + BC | >90% | >90% | Never drops below 90% |
| Fine-tuning + EM | <20% | ~90% | Temporary drop then recovery |
| Fine-tuning + EWC | <65% | ~90% | Temporary drop then recovery |
| Vanilla fine-tuning | severe drop | lower than KR | Slow recovery |

## Stage: push-wall (FAR — pre-trained)

| Method | At 1e6 steps | At ~4e6 steps | Final | Notes |
|--------|-------------|--------------|-------|-------|
| Pre-trained π* (frozen) | ~100% | ~100% | ~100% | Static reference |
| Fine-tuning + BC | >90% | >90% | >90% | Never drops below 90% |
| Fine-tuning + EM | <10% | ~85% | ~85% | Temporary drop then recovery |
| Fine-tuning + EWC | <50% | ~60% | ~60% | Temporary drop; limited recovery |
| Vanilla fine-tuning | ~0% (catastrophic) | >80% (recovered) | ~60% | Drops to 0%, slow recovery |

## Key Insight
- BC prevents forgetting on FAR stages throughout training (remains >90%)
- EM and EWC allow temporary drops but recover
- Vanilla fine-tuning shows severe and slow-recovering forgetting on FAR stages
