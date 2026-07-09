# Heuristics

## H01: Scale subtracted vector α to match DPO perplexity
- **Rationale**: Different toxic vectors have different norms; subtracting at full scale can degrade generation quality. Choosing α to approximately match the perplexity of GPT2DPO ensures fair comparison between intervention methods.
- **Sensitivity**: high
- **Bounds**: α is chosen per-vector such that resulting perplexity ≈ 23.34 (GPT2DPO perplexity on Wikitext-2); no fixed range given
- **Code ref**: [src/execution/interventions.py]
- **Source**: §3.3, Table 2

## H02: Select N=128 toxic value vectors for MLP.vToxic
- **Rationale**: 128 vectors provide sufficient coverage of the toxicity subspace. The paper reports "similar results" for other values of N. Too few vectors miss toxicity dimensions; too many dilute the signal.
- **Sensitivity**: low
- **Bounds**: Tested with various values; N=128 used in all reported experiments
- **Code ref**: [src/execution/toxic_vectors.py]
- **Source**: §3.1, footnote 2

## H03: DPO beta=0.1 to balance reward maximization and KL regularization
- **Rationale**: The KL term (controlled by β) prevents drastic weight changes, which is key to the "distributed minimal offset" mechanism. Higher β would constrain learning more strongly; lower β would allow larger weight changes that could remove toxic vectors outright.
- **Sensitivity**: high
- **Bounds**: β=0.1 (fixed); range not reported
- **Code ref**: [src/execution/dpo_training.py]
- **Source**: Appendix D, Table 5

## H04: PPLM gm_scale=0.95 and kl_scale=0.1 for toxic data generation
- **Rationale**: gm_scale controls the geometric mean blending of modified and original distributions; kl_scale prevents PPLM from diverging too far from GPT2. These values balance toxicity of generated negatives with fluency.
- **Sensitivity**: medium
- **Bounds**: gm_scale=0.95, kl_scale=0.1, step_size=0.4, decay=FALSE (all from Table 6)
- **Code ref**: [src/execution/dpo_training.py]
- **Source**: Appendix D, Table 6

## H05: Scale top-7 key vectors by 10× for un-alignment
- **Rationale**: Scaling expands the activation region γ(k_i^ℓ) without touching value vectors or the residual stream. Factor 10× was sufficient to restore toxicity; fewer vectors or smaller scale may not fully overcome the DPO offset.
- **Sensitivity**: medium
- **Bounds**: 7 vectors, 10× scale; both chosen empirically
- **Code ref**: [src/execution/unalignment.py]
- **Source**: §5.3, Table 4
