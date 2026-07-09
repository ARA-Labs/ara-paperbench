# Problem Specification

## Observations

### O1: Alignment algorithms suppress but may not eliminate undesirable capabilities
- **Statement**: RLHF-based alignment algorithms like DPO and PPO can reduce toxic outputs from LLMs, but the mechanisms by which they do so are not understood.
- **Evidence**: Prior work (Wei et al., 2023; Zou et al., 2023; Carlini et al., 2023) shows aligned models are easily jailbroken; empirical evidence without mechanistic explanation.
- **Implication**: Without understanding the mechanism, we cannot predict failure modes or design robust defenses.

### O2: MLP blocks in transformers function as key-value memories
- **Statement**: Geva et al. (2022) demonstrated that MLP blocks in GPT-class models can be decomposed into key-value operations where value vectors promote specific token concepts. GPT2-medium has L=24, d=1024, dmlp=4096.
- **Evidence**: §2, Geva et al. (2022), Equation 1–2 in the paper.
- **Implication**: Individual value vectors are interpretable and can be identified as promoting toxic content.

### O3: Toxicity is represented in identifiable MLP value vectors
- **Statement**: Value vectors with high cosine similarity to a trained toxicity probe (WToxic, 94% validation accuracy) promote toxic tokens when projected onto vocabulary space.
- **Evidence**: Table 1 (§3.2): vectors MLP.v19_770, MLP.v12_771, etc. promote highly offensive token lists. Probe achieves 94% accuracy on Jigsaw validation set.
- **Implication**: Toxicity has a localized, identifiable representation in MLP weights.

### O4: DPO produces minimal weight changes
- **Statement**: After DPO fine-tuning, every parameter in GPT2 vs. GPT2DPO has cosine similarity >0.99 and average norm difference <1e-5 (unembedding layer <1e-3).
- **Evidence**: §5.1.
- **Implication**: DPO does not substantially rewrite any single weight yet still reduces toxicity, suggesting the mechanism is distributed.

### O5: Post-DPO, toxic MLP activations drop
- **Statement**: Using 1,199 challenge prompts from RealToxicityPrompts, mean activations of the top-5 toxic value vectors (MLP.vToxic) drop significantly in GPT2DPO compared to GPT2.
- **Evidence**: Figure 2 (§5.2).
- **Implication**: The model's residual stream no longer enters the activation regions of toxic vectors.

## Gaps

### G1: No mechanistic explanation for alignment or jailbreaks
- **Statement**: Prior work lacked an explanation at the level of model internals for how alignment suppresses behavior and why it is reversible.
- **Caused by**: O1 — empirical jailbreak results exist but no mechanistic account.
- **Existing attempts**: Wei et al. (2023) provide hypotheses backed by empirical studies.
- **Why they fail**: They describe what fails but not the internal mechanism that enables reversion.

### G2: No method to characterize when/how alignment will be undone
- **Statement**: Researchers could not predict vulnerability from model internals alone.
- **Caused by**: O1, O4 — without knowing that toxic vectors persist unchanged, one cannot design targeted defenses.
- **Existing attempts**: Adversarial prompt search (Zou et al., 2023; Wallace et al., 2019).
- **Why they fail**: Empirical attack methods rather than mechanistic understanding.

## Key Insight

- **Insight**: DPO does not delete or overwrite toxic capabilities encoded in MLP value vectors. Instead, it learns a distributed offset across many inactive (negative-activation) value vectors in earlier MLP layers, shifting the residual stream out of the "activation regions" of toxic key vectors. Because most neurons are sparse/inactive (negative GeLU activations), the shift in value vectors (δMLP.v) paradoxically contributes in the opposite direction, yielding the residual stream offset δx that bypasses toxic regions.
- **Derived from**: O2, O3, O4, O5.
- **Enables**: (1) A simple un-alignment attack: scale toxic key vectors by 10× to expand toxic regions back into the path of the shifted residual stream. (2) A conjecture for more robust alignment: eliminate toxic regions rather than bypassing them.

## Assumptions

- A1: GPT2-medium is a sufficiently representative model for studying DPO's toxicity-reduction mechanism.
- A2: The Jigsaw toxicity dataset provides adequate signal for training a probe that captures GPT2's internal toxicity representation.
- A3: RealToxicityPrompts challenge set (1,199 prompts) is representative of prompts that elicit toxic outputs.
- A4: PPLM with WToxic as attribute classifier generates sufficiently toxic negative samples for DPO training.
- A5: Cosine similarity and norm difference are adequate metrics for measuring parameter-level change.
