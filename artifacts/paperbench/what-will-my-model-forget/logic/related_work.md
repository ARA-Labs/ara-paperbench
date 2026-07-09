# Related Work

## RW01: Toneva et al., 2018
- **DOI**: ICLR 2019 (arXiv:1812.05159)
- **Type**: imports
- **Delta**:
  - What changed: This paper extends the finding that some examples are more forgettable than others by predicting *which specific upstream example* will be forgotten based on the *specific online example* being learned, rather than characterizing global forgettability.
  - Why: To achieve example-pair-level prediction rather than just per-example statistics.
- **Claims affected**: C01, C03
- **Adopted elements**: Concept of "forgettable examples"; motivation for threshold-based forecasting baseline (Eqn. 1)

## RW02: Maini et al., 2022
- **DOI**: NeurIPS 2022
- **Type**: imports
- **Delta**:
  - What changed: "Second-split forgetting" characterizes example difficulty; this paper instead characterizes pair-wise interaction effects.
  - Why: Single-example characterization cannot predict which example causes forgetting of which other.
- **Claims affected**: C03
- **Adopted elements**: The concept of characterizing training examples by forgetting dynamics

## RW03: Aljundi et al., 2019a (MIR)
- **DOI**: NeurIPS 2019
- **Type**: baseline
- **Delta**:
  - What changed: MIR retrieves forgetting examples from a small subset of training data to avoid full inference; this paper trains a separate forecasting model that does not require any PTLM inference.
  - Why: MIR's subset approximation degrades performance at scale (Table 3).
- **Claims affected**: C04, C06
- **Adopted elements**: The core idea that targeted replay reduces forgetting better than random replay

## RW04: Aljundi et al., 2019b (GSS)
- **DOI**: NeurIPS 2019
- **Type**: baseline
- **Delta**:
  - What changed: Gradient-based sample selection (inner products of gradients) is computationally expensive; this paper replaces gradient inner products with inner products of learned low-dimensional representations.
  - Why: TV backward passes for gradient computation are prohibitive for large LMs.
- **Claims affected**: C06
- **Adopted elements**: Motivation for measuring example similarity via inner products

## RW05: Lee et al., 2019 (NTK)
- **DOI**: NeurIPS 2019
- **Type**: imports
- **Delta**:
  - What changed: The paper applies NTK theory to derive the logit-change transfer formula (Eqn. 2) for sequence-to-sequence models.
  - Why: Provides the theoretical justification for using kernel-based approximations to predict logit changes.
- **Claims affected**: C03
- **Adopted elements**: First-order Taylor expansion technique; NTK definition and properties

## RW06: Ramasesh et al., 2020
- **DOI**: ICLR 2021
- **Type**: imports
- **Delta**:
  - What changed: Ramasesh et al. study logit changes in frozen feature models; this paper studies logit-change transfer in fine-tuned instruction-tuned LMs with trainable kernels.
  - Why: The frozen feature assumption does not hold for LoRA or Full FT settings.
- **Claims affected**: C03
- **Adopted elements**: The idea that logit dynamics can explain task interference patterns

## RW07: De Cao et al., 2021 (EDITS)
- **DOI**: EMNLP 2021
- **Type**: baseline
- **Delta**:
  - What changed: EDITS learns meta-gradients for editing; this paper uses standard fine-tuning as the update mechanism, which is model-agnostic.
  - Why: Meta-gradient approaches can reduce forgetting but sacrifice edit success rate in the paper's setup (Appendix A, Table 6).
- **Claims affected**: C04
- **Adopted elements**: Problem framing of model refinement / error fixing

## RW08: Mitchell et al., 2021 (MEND)
- **DOI**: ICLR 2022
- **Type**: baseline
- **Delta**:
  - What changed: MEND learns a meta-model to edit gradients; the paper uses standard fine-tuning + forecasting-guided replay, which achieves better edit success rate at comparable forgetting reduction.
  - Why: MEND's edit success rate is lower than Vanilla FT (93.1% vs. 95.7%) in LoRA setting (Table 6).
- **Claims affected**: C04
- **Adopted elements**: Comparison methodology; establishing that replay-based methods are competitive

## RW09: Yoon et al., 2022 (OCS)
- **DOI**: ICLR 2022
- **Type**: baseline
- **Delta**:
  - What changed: OCS computes coresets as important examples to replay; this paper uses forecasting model predictions (pair-specific) rather than importance-based coreset selection.
  - Why: OCS does not capture online example-specific forgetting interactions (Table 3).
- **Claims affected**: C04
- **Adopted elements**: Coreset-based replay as an alternative baseline

## RW10: Chung et al., 2022 (FLAN-T5)
- **DOI**: arXiv:2210.11416
- **Type**: imports
- **Delta**:
  - What changed: FLAN-T5 is used as the primary experimental model; the paper studies how model refinement affects FLAN-T5's instruction-following abilities.
  - Why: FLAN-T5 is a widely deployed instruction-tuned model that makes real errors.
- **Claims affected**: C01, C03, C04
- **Adopted elements**: FLAN-T5Large and FLAN-T53B model weights; MMLU as evaluation dataset

## RW11: Lin et al., 2022a (BART0)
- **DOI**: NeurIPS 2022
- **Type**: imports
- **Delta**:
  - What changed: BART0 is used as a second experimental model trained exclusively on P3; its controlled training setup enables cleaner evaluation.
  - Why: BART0's single-dataset pretraining allows using P3-Test as a genuinely out-of-pretraining evaluation set.
- **Claims affected**: C01, C03, C04
- **Adopted elements**: BART0Large model weights; P3 dataset splits

## RW12: Novak et al., 2022 (Fast NTK)
- **DOI**: ICML 2022
- **Type**: bounds
- **Delta**:
  - What changed: Establishes that computing NTKs for large LMs is prohibitively expensive; this paper proposes a trainable low-rank approximation to circumvent this.
  - Why: Motivates the departure from exact NTK computation toward the simplified kernel Θ̃.
- **Claims affected**: C06
- **Adopted elements**: Complexity analysis framework; TV backward pass cost characterization
