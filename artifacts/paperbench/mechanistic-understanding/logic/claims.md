# Claims

## C01: Toxicity is encoded in identifiable MLP value vectors in GPT2-medium
- **Statement**: Value vectors in GPT2-medium's MLP blocks that have high cosine similarity with a linearly-trained toxicity probe (WToxic) promote toxic tokens when projected onto vocabulary space, and these vectors span a toxicity subspace recoverable via SVD.
- **Status**: supported
- **Falsification criteria**: If no value vector has cosine similarity with WToxic above a random baseline, or if subtracting such vectors does not reduce toxicity, the claim is refuted.
- **Proof**: [E01, E02]
- **Dependencies**: none
- **Tags**: MLP value vectors, toxic probe, SVD, vocabulary projection, mechanistic interpretability

## C02: Subtracting toxic vectors from the residual stream reduces toxicity while preserving language quality
- **Statement**: Subtracting WToxic, MLP.v19, or SVD.UToxic[0] from the residual stream at the last layer during generation reduces toxicity scores relative to the baseline GPT2, while maintaining comparable F1 and slightly increased but controlled perplexity.
- **Status**: supported
- **Falsification criteria**: If subtraction does not reduce toxicity score (Perspective API) below GPT2 baseline, or if perplexity increases more than observed for DPO, the claim is refuted.
- **Proof**: [E02]
- **Dependencies**: C01
- **Tags**: intervention, residual stream, toxicity reduction, perplexity, F1

## C03: DPO does not remove toxic MLP vectors but learns a distributed residual-stream offset that bypasses them
- **Statement**: After DPO fine-tuning, MLP.kToxic and MLP.vToxic are unchanged (cosine similarity >0.99); instead, GPT2DPO learns a distributed offset δx distributed across many value vectors in earlier MLP layers that shifts the residual stream out of the activation regions of toxic key vectors.
- **Status**: supported
- **Falsification criteria**: If toxic value vectors show cosine similarity <0.99 with their pre-DPO counterparts, or if residual streams in GPT2DPO still pass through toxic activation regions, the claim is refuted.
- **Proof**: [E03, E04]
- **Dependencies**: C01
- **Tags**: DPO, bypass, residual stream offset, toxic regions, distributed learning

## C04: Every DPO weight change is minimal, with cosine similarity >0.99 and norm difference <1e-5
- **Statement**: Every parameter (token embeddings, MLP blocks, attention heads) in GPT2 and GPT2DPO has pairwise cosine similarity greater than 0.99 and average norm difference less than 1e-5; the unembedding layer is the sole exception with norm difference less than 1e-3.
- **Status**: supported
- **Falsification criteria**: Any parameter with cosine similarity ≤0.99 or norm difference ≥1e-5 (or ≥1e-3 for unembedding) would refute this claim.
- **Proof**: [E03]
- **Dependencies**: none
- **Tags**: parameter analysis, cosine similarity, norm difference, DPO, minimal change

## C05: The residual stream shift arises from sparse inactive neurons whose sign-flipped contributions accumulate in the δx direction
- **Statement**: Because GPT2 uses GeLU activations and MLP neurons are predominantly inactive (negative activations) for RealToxicityPrompts inputs, the DPO-induced shift in value vectors (δMLP.v) is multiplied by small negative scalars, flipping direction, and collectively pushing the residual stream into the antipodal direction δx that avoids toxic regions.
- **Status**: supported
- **Falsification criteria**: If the majority of value-vector activations are positive, or if δMLP.v and δx are not predominantly negatively correlated as layers approach the toxic layer, the claim is refuted.
- **Proof**: [E04]
- **Dependencies**: C03, C04
- **Tags**: GeLU, sparse neurons, antipodal shift, δx, mechanistic explanation

## C06: DPO alignment can be trivially reversed by scaling toxic key vectors by 10×
- **Statement**: Scaling as few as 7 MLP key vectors with highest cosine similarity to WToxic by a factor of 10 is sufficient to expand their activation regions, causing the DPO-shifted residual stream to re-enter toxic regions, restoring toxicity to near-baseline GPT2 levels while leaving perplexity and F1 unchanged.
- **Status**: supported
- **Falsification criteria**: If scaling 7 key vectors by 10× does not restore toxicity to near GPT2 baseline, or if perplexity is substantially degraded, the claim is refuted.
- **Proof**: [E05]
- **Dependencies**: C03, C05
- **Tags**: un-alignment, jailbreak, key vector scaling, activation region, robustness
