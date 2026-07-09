# Related Work

## RW01: Geva et al., 2022
- **DOI**: 10.18653/v1/2022.emnlp-main.3
- **Type**: imports
- **Delta**:
  - What changed: This paper applies Geva et al.'s key-value MLP decomposition framework to identify and intervene on toxic vectors, and to analyze post-DPO residual stream shifts.
  - Why: Provides the mathematical foundation for interpreting MLP blocks as key-value memories and projecting value vectors onto vocabulary space.
- **Claims affected**: C01, C02, C03, C05
- **Adopted elements**: MLP decomposition (Eq. 1–2), vocabulary projection $r_i = Ev_i$, token promotion/suppression framework

## RW02: Rafailov et al., 2023
- **DOI**: arXiv:2305.18290
- **Type**: imports
- **Delta**:
  - What changed: The paper uses DPO as the alignment algorithm to study and applies its loss formulation directly.
  - Why: DPO is widely used and avoids reward model training complexity.
- **Claims affected**: C03, C04, C05, C06
- **Adopted elements**: DPO loss function, pairwise preference data format

## RW03: Dathathri et al., 2019
- **DOI**: arXiv:1912.02164 (ICLR 2020)
- **Type**: imports
- **Delta**:
  - What changed: PPLM is used with WToxic as attribute classifier to generate toxic negative samples for DPO training data.
  - Why: Allows controlled generation of toxic text without manual annotation.
- **Claims affected**: C03 (via data generation)
- **Adopted elements**: PPLM framework $p(y|a) \propto p(y)p(a|y)$, gradient-based activation steering

## RW04: Gehman et al., 2020
- **DOI**: 10.18653/v1/2020.findings-emnlp.301
- **Type**: imports
- **Delta**:
  - What changed: RealToxicityPrompts (challenge subset, 1,199 prompts) used as evaluation dataset.
  - Why: Standard benchmark for evaluating toxic degeneration.
- **Claims affected**: C01, C02, C03, C06 (all evaluation)
- **Adopted elements**: RealToxicityPrompts challenge set, Perspective API toxicity scoring methodology

## RW05: Jain et al., 2023
- **DOI**: arXiv:2311.12786
- **Type**: baseline
- **Delta**:
  - What changed: Jain et al. study fine-tuning on synthetic tasks and find "wrapper" representations at late layers; this paper finds distributed minimal changes from RLHF with KL regularization.
  - Why: Closest prior work on mechanistic analysis of fine-tuning effects.
- **Claims affected**: C03, C04, C05
- **Adopted elements**: Conceptual framing of studying mechanism changes from fine-tuning

## RW06: Wei et al., 2023
- **DOI**: NeurIPS 2023 (openreview.net/forum?id=jA235JGM09)
- **Type**: extends
- **Delta**:
  - What changed: Wei et al. provide empirical hypotheses for why LLMs are jailbroken; this paper provides the first mechanistic explanation.
  - Why: Direct motivation for mechanistic study.
- **Claims affected**: C06
- **Adopted elements**: Framing of jailbreak as a fundamental alignment vulnerability

## RW07: Nostalgebraist, 2020
- **DOI**: https://www.lesswrong.com/posts/AcKRB8wDpdaN6v6ru/interpreting-gpt-the-logit-lens
- **Type**: imports
- **Delta**:
  - What changed: Logit Lens technique applied to visualize layer-wise promotion of toxic tokens.
  - Why: Allows identification of which MLP layers most promote toxic tokens.
- **Claims affected**: C03
- **Adopted elements**: Logit Lens (apply unembedding at intermediate layers)

## RW08: Balestriero et al., 2023
- **DOI**: arXiv:2312.01648
- **Type**: imports
- **Delta**:
  - What changed: MLP activation region visualization concept borrowed and applied to show residual stream shift post-DPO.
  - Why: Provides geometric characterization of LLM hidden spaces.
- **Claims affected**: C05
- **Adopted elements**: Activation region concept $\gamma(k) = \{g | \sigma(k \cdot g) > 0\}$

## RW09: Zou et al., 2023
- **DOI**: arXiv:2307.15043
- **Type**: bounds
- **Delta**:
  - What changed: Demonstrates adversarial attacks that jailbreak aligned LLMs; this paper provides mechanistic explanation for why such attacks work.
  - Why: Empirical evidence motivating mechanistic study.
- **Claims affected**: C06
- **Adopted elements**: Evidence that alignment is easily circumvented

## RW10: Carlini et al., 2023
- **DOI**: NeurIPS 2023 (openreview.net/forum?id=OQQoD8Vc3B)
- **Type**: bounds
- **Delta**:
  - What changed: Shows multimodal models can be jailbroken; motivates need for mechanistic understanding.
  - Why: Broader evidence that alignment is fragile across modalities.
- **Claims affected**: C06
- **Adopted elements**: Evidence that adversarial alignment failures are widespread

## RW11: Yang et al., 2023; Qi et al., 2023
- **DOI**: arXiv:2310.02949; arXiv:2310.03693
- **Type**: baseline
- **Delta**:
  - What changed: Demonstrate fine-tuning with as few as 100 examples can un-align models; this paper provides the mechanistic reason (toxic vectors remain, only offset shifts).
  - Why: Establishes baseline ease of un-alignment for comparison.
- **Claims affected**: C06
- **Adopted elements**: Un-alignment as a feasible attack

## RW12: cjadams et al., 2017
- **DOI**: https://kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge
- **Type**: imports
- **Delta**:
  - What changed: Jigsaw Toxic Comment Classification dataset (561,808 comments) used to train WToxic probe.
  - Why: Standard toxicity classification dataset with binary labels.
- **Claims affected**: C01
- **Adopted elements**: Dataset (561,808 comments, binary toxic/non-toxic labels, 90:10 split)
