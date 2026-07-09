# Related Work

## RW01: Hu et al., 2022 (LoRA)
- **DOI**: OpenReview ICLR 2022
- **Type**: imports
- **Delta**:
  - What changed: APT extends LoRA with dynamic rank adjustment and binary pruning masks; LoRA uses fixed ranks and shapes
  - Why: LoRA alone does not reduce inference cost or adapt tuning allocation to task importance
- **Claims affected**: C01, C02, C05
- **Adopted elements**: Low-rank decomposition W_A, W_B; scaling factor s; zero W_B initialization; weight merging at inference

## RW02: Xia et al., 2022 (CoFi)
- **DOI**: 10.18653/v1/2022.acl-long.107
- **Type**: baseline
- **Delta**:
  - What changed: APT replaces CoFi's L0 regularization with salience-based mask learning and replaces its separate teacher model with self-distillation
  - Why: CoFi requires full fine-tuning memory for teacher (168.5% of FT); APT's self-distillation uses only 70.1%
- **Claims affected**: C03
- **Adopted elements**: Layer-wise distillation objective structure (L_layer, L_pred); random intermediate layer mapping from RAIL-KD; cubic scheduling concept

## RW03: Zhang et al., 2023b (AdaLoRA)
- **DOI**: arXiv:2303.10512 (ICLR 2023)
- **Type**: bounds
- **Delta**:
  - What changed: APT grows ranks in top-half adapters based on salience; AdaLoRA reduces ranks based on SVD importance. APT also co-optimizes pruning masks
  - Why: AdaLoRA improves training efficiency but does not reduce inference cost (model size unchanged)
- **Claims affected**: C05
- **Adopted elements**: EMA salience scoring (β = 0.85 from AdaLoRA's formulation)

## RW04: Kwon et al., 2022 (Mask Tuning / MT)
- **DOI**: NeurIPS 2022
- **Type**: baseline
- **Delta**:
  - What changed: APT prunes during training via adaptive salience; MT prunes post-training via Fisher information
  - Why: Post-training pruning requires a fully fine-tuned model as initialization; APT does not
- **Claims affected**: C02
- **Adopted elements**: Used as the pruning component in the LoRA+Prune baseline

## RW05: Ma et al., 2023 (LLMPruner)
- **DOI**: arXiv:2305.11627
- **Type**: baseline
- **Delta**:
  - What changed: APT performs task-specific structured pruning with outlier-aware salience; LLMPruner performs task-agnostic block/channel pruning
  - Why: Task-agnostic pruning cannot achieve on-par performance with task-specific pruning; LLMPruner costs ~80GB for LLaMA 7B
- **Claims affected**: C06, C07
- **Adopted elements**: LLaMA pruning evaluation protocol on Alpaca + Open LLM Leaderboard

## RW06: Sanh et al., 2020 (Movement Pruning / MvP)
- **DOI**: NeurIPS 2020
- **Type**: imports
- **Delta**:
  - What changed: APT uses activation-gradient product (proxy for weight-gradient) and adds kurtosis; movement pruning uses weight-gradient magnitude only for unstructured pruning
  - Why: Weight gradients unavailable for frozen parameters in PEFT settings; block-level averaging loses outlier signal
- **Claims affected**: C04
- **Adopted elements**: Weight-gradient salience concept (Equation 3 in APT paper)

## RW07: Zhao et al., 2023 (CPET)
- **DOI**: arXiv:2307.07705
- **Type**: refutes
- **Delta**:
  - What changed: CPET shows that combining structured pruning with LoRA causes notable performance loss; APT overcomes this via adaptive pruning and tuning
  - Why: Static LoRA cannot compensate for dynamic parameter removal during structured pruning
- **Claims affected**: C01, C02
- **Adopted elements**: Identification of the failure mode motivating APT's design

## RW08: Zhang et al., 2023a (LRP — Pruning meets Low-Rank PEFT)
- **DOI**: arXiv:2305.18403
- **Type**: baseline
- **Delta**:
  - What changed: APT uses combined frozen + tuning weight salience; LRP uses only tuning block salience for pruning decisions
  - Why: Only using tuning block salience leads to sub-optimal pruning results for frozen parameters
- **Claims affected**: C04
- **Adopted elements**: Concept of combining structured pruning with PEFT adapters

## RW09: Hedegaard et al., 2022 (SPA — Structured Pruning Adapters)
- **DOI**: 2022
- **Type**: baseline
- **Delta**:
  - What changed: APT uses outlier-aware salience and self-distillation; SPA combines structured pruning with Compacter
  - Why: SPA suffers substantial performance loss; APT achieves near-FT performance
- **Claims affected**: C01
- **Adopted elements**: Motivation for combining structured pruning with adapters

## RW10: Dettmers et al., 2022 (GPT3.int8())
- **DOI**: NeurIPS 2022
- **Type**: imports
- **Delta**:
  - What changed: APT borrows the insight that outlier parameters play a crucial role in LM capabilities
  - Why: Motivates the kurtosis term in APT's salience scoring
- **Claims affected**: C04
- **Adopted elements**: Outlier parameter importance insight

## RW11: Haidar et al., 2022 (RAIL-KD)
- **DOI**: 10.18653/v1/2022.findings-naacl.103
- **Type**: imports
- **Delta**:
  - What changed: APT adopts the block-wise random teacher layer sampling strategy from RAIL-KD for self-distillation
  - Why: Reduces distillation cost while maintaining layer coverage
- **Claims affected**: C03
- **Adopted elements**: Random intermediate layer mapping for knowledge distillation (4 layers, quarter-sliced)

## RW12: Shen et al., 2022b (Latency-Saliency Knapsack)
- **DOI**: NeurIPS 2022
- **Type**: imports
- **Delta**:
  - What changed: APT adapts the latency-saliency knapsack framing but simplifies it to a binary search over salience density
  - Why: Full knapsack is computationally expensive; binary search over monotone parameter count function is O(log N)
- **Claims affected**: C02
- **Adopted elements**: Salience density (salience / parameter count) as the block ranking criterion
