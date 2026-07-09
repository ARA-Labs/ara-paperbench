---
# Related Work

## RW01: Schulman et al., 2017 — PPO
- **DOI**: arXiv:1707.06347
- **Type**: baseline
- **Delta**:
  - What changed: SAPG replaces single-policy PPO with multi-policy leader-follower framework with importance-sampled data aggregation.
  - Why: PPO performance saturates at large batch sizes due to IID sampling redundancy.
- **Claims affected**: C01, C02
- **Adopted elements**: Clipped surrogate objective (Eq. 2), KL-threshold-based LR adaptation, minibatch gradient descent, trust-region update philosophy.

## RW02: Petrenko et al., 2023 — DexPBT
- **DOI**: 10.15607/RSS.2023.XIX.037
- **Type**: baseline
- **Delta**:
  - What changed: SAPG uses importance-sampled data aggregation to use ALL collected data; DexPBT only keeps best-policy weights and discards data from worse policies.
  - Why: Data from "worse" policies still contains valuable trajectory information that should not be wasted.
- **Claims affected**: C02, C03, C05
- **Adopted elements**: Multi-policy environment splitting (M groups of N/M environments), task suite selection (AllegroKuka environments), 24,576 environment experimental setup.

## RW03: Li et al., 2023 — PQL (Parallel Q-Learning)
- **DOI**: arXiv (Parallel Q-learning: Scaling off-policy RL under massively parallel simulation)
- **Type**: baseline
- **Delta**:
  - What changed: SAPG is on-policy (PPO-based) while PQL is off-policy (DDPG-based). SAPG achieves higher asymptotic performance on hard tasks; PQL is more sample-efficient early.
  - Why: On-policy methods are better at latching onto high-reward trajectories for hard tasks.
- **Claims affected**: C02
- **Adopted elements**: ShadowHand and AllegroHand task benchmarks, massively parallel simulation setting.

## RW04: Meng et al., 2023 — Off-policy PPO
- **DOI**: 10.1609/aaai.v37i8.26099
- **Type**: imports
- **Delta**:
  - What changed: SAPG uses the off-policy PPO framework to combine data from multiple concurrent policies (not just past versions of one policy).
  - Why: This provides the importance sampling formulation (Eq. 3) that enables stable off-policy updates within PPO's clipped surrogate framework.
- **Claims affected**: C02, C05
- **Adopted elements**: Off-policy importance sampling correction term μ = πi,old/πj (Eq. 3), off-policy clipped surrogate formulation.

## RW05: Degris et al., 2012 — Off-policy Actor-Critic
- **DOI**: arXiv:1205.4839
- **Type**: imports
- **Delta**:
  - What changed: SAPG applies importance sampling in the large-batch GPU setting where diverse concurrent policies make IS beneficial rather than costly.
  - Why: IS was impractical in small-scale settings; at scale it enables data diversity gains.
- **Claims affected**: C05
- **Adopted elements**: Importance sampling framework for using off-policy data in actor-critic updates.

## RW06: Espeholt et al., 2018 — IMPALA
- **DOI**: arXiv:1802.01561
- **Type**: bounds
- **Delta**:
  - What changed: IMPALA distributes data collection across CPU workers; SAPG distributes across GPU environment blocks with concurrent policy optimization rather than asynchronous collection.
  - Why: GPU-driven simulation makes CPU-distributed collection obsolete; the bottleneck is algorithmic (data diversity) not collection throughput.
- **Claims affected**: C01
- **Adopted elements**: Importance-weighted learning with V-trace; concept of using off-policy data from lagged policies.

## RW07: Makoviychuk et al., 2021 — IsaacGym
- **DOI**: arXiv:2108.10470
- **Type**: imports
- **Delta**:
  - What changed: SAPG is built on top of IsaacGym and exploits its massive parallelism specifically.
  - Why: IsaacGym enables 24,576+ parallel environments on a single GPU — the scale at which SAPG's benefits manifest.
- **Claims affected**: C01
- **Adopted elements**: GPU-based physics simulation platform; AllegroKuka task environments.

## RW08: Fakoor et al., 2020 — P3O
- **DOI**: PMLR v115 (UAI 2020)
- **Type**: bounds
- **Delta**:
  - What changed: SAPG extends the policy-on/policy-off optimization idea to concurrent multi-policy systems rather than mixing current and past policy data from a single policy.
  - Why: Concurrent diverse policies provide better coverage than past versions of one policy.
- **Claims affected**: C05
- **Adopted elements**: Framework for combining on-policy and off-policy data in a single update.

## RW09: Konda & Tsitsiklis, 1999 — Actor-Critic Algorithms
- **DOI**: NeurIPS 1999
- **Type**: imports
- **Delta**:
  - What changed: SAPG uses the actor-critic update structure with separate actor and critic losses, extending it to the multi-policy off-policy setting.
  - Why: Actor-critic structure (separate value function + policy) is necessary for advantage estimation in the off-policy correction.
- **Claims affected**: C02
- **Adopted elements**: Actor-critic update framework, advantage function estimation, baseline variance reduction.
