# Experiments

## E01: Toxic Vector Extraction and Vocabulary Projection
- **Verifies**: C01
- **Setup**:
  - Model: GPT2-medium (L=24, d=1024, dmlp=4096)
  - Hardware: Not specified in paper
  - Dataset: Jigsaw toxic comment classification dataset (561,808 comments, 90:10 train/validation split)
  - System: Linear probe WToxic trained on averaged last-layer residual stream
- **Procedure**:
  1. Load GPT2-medium; extract residual streams at last layer (L-1) for all Jigsaw comments, averaged across timesteps.
  2. Train linear probe WToxic ∈ R^d via softmax(WToxic * x̄^{L-1}) on 90% training split; evaluate on 10% validation split.
  3. Record classification accuracy on validation split.
  4. Compute cosine similarity of all 24×4096 MLP value vectors with WToxic; select top N=128 as MLP.vToxic, with corresponding MLP.kToxic.
  5. Stack MLP.vToxic into 128×d matrix; apply SVD to obtain left singular vectors SVD.UToxic[0], [1], [2].
  6. Project each toxic vector (WToxic, sampled MLP.vToxic, SVD.UToxic[0–2]) onto vocabulary space via r = E*v; inspect top-ranked tokens.
- **Metrics**: Probe validation accuracy; cosine similarity distribution; top-5 promoted tokens per vector
- **Expected outcome**:
  - Probe achieves high validation accuracy (around 94%)
  - Selected MLP.vToxic vectors promote offensive/toxic tokens in vocabulary space
  - SVD.UToxic vectors capture distinct dimensions of toxicity (profanity, insults, sexual content)
- **Baselines**: none
- **Dependencies**: none

## E02: Residual Stream Intervention (Toxicity Suppression)
- **Verifies**: C02
- **Setup**:
  - Model: GPT2-medium (pre-DPO)
  - Hardware: Not specified in paper
  - Dataset: RealToxicityPrompts challenge subset (1,199 prompts); Wikitext-2 for perplexity; 2,000 Wikipedia sentences for F1
  - System: Subtract toxic vector from last-layer residual stream during forward pass
- **Procedure**:
  1. Load GPT2-medium.
  2. For each toxicity vector W ∈ {WToxic, MLP.v19_770, SVD.UToxic[0]}, apply intervention: x^{L-1} ← x^{L-1} - α * W during generation.
  3. Select scalar α such that resulting perplexity on Wikitext-2 is comparable to post-DPO model.
  4. Generate continuations for all 1,199 RealToxicityPrompts challenge prompts; score with Perspective API.
  5. Compute perplexity on Wikitext-2 dataset.
  6. Use 2,000 Wikipedia sentences as prompts; compute F1 as harmonic mean of precision (fraction of generated tokens in ground-truth continuation) and recall (fraction of ground-truth tokens in generated output).
  7. Record examples of top-k token predictions and continuations before/after intervention.
- **Metrics**: Toxicity score (Perspective API, 0–1), perplexity on Wikitext-2, F1 on Wikipedia continuations
- **Expected outcome**:
  - Subtracting any of the three vectors reduces toxicity score below GPT2 baseline
  - DPO achieves the greatest toxicity reduction
  - Perplexity increases slightly above GPT2 baseline but remains close to DPO perplexity
  - F1 remains near GPT2 baseline (no significant degradation)
  - Top-1 predicted token shifts from toxic to non-toxic after intervention
- **Baselines**: GPT2 No Op (no intervention)
- **Dependencies**: E01

## E03: Parameter Distance Analysis (Pre vs. Post DPO)
- **Verifies**: C03, C04
- **Setup**:
  - Model: GPT2-medium and GPT2DPO (fine-tuned with DPO)
  - Hardware: Not specified in paper
  - Dataset: Not applicable (parameter comparison)
  - System: Compare all model parameter tensors pairwise
- **Procedure**:
  1. Load GPT2 and GPT2DPO.
  2. For each matching parameter tensor (token embeddings, MLP blocks at all 24 layers, attention heads, unembedding), compute pairwise cosine similarity.
  3. Compute average norm difference ||θ_GPT2 - θ_DPO||.
  4. Specifically verify MLP.kToxic and MLP.vToxic vectors show same minimal change.
  5. Report cosine similarity and norm differences across all components.
- **Metrics**: Per-tensor cosine similarity; per-tensor average norm difference
- **Expected outcome**:
  - All parameters show cosine similarity greater than 0.99
  - All parameters show average norm difference less than 1e-5, except unembedding layer (less than 1e-3)
  - MLP.kToxic and MLP.vToxic included in the minimal-change finding
- **Baselines**: none
- **Dependencies**: E01 (to identify which vectors are MLP.kToxic/MLP.vToxic)

## E04: Residual Stream Bypass Analysis
- **Verifies**: C03, C05
- **Setup**:
  - Model: GPT2-medium and GPT2DPO
  - Hardware: Not specified in paper
  - Dataset: RealToxicityPrompts challenge subset (1,199 prompts); generate 20 tokens per prompt
  - System: Measure MLP activations and residual stream shifts layer by layer
- **Procedure**:
  1. For each of the 1,199 RealToxicityPrompts challenge prompts, generate 20 tokens with both GPT2 and GPT2DPO.
  2. Record mean activations m_i = σ(x^ℓ · k_i^ℓ) for the top-5 MLP.vToxic vectors across all generated tokens.
  3. At each layer ℓ (after attention, before MLP), record residual stream x^{ℓmid} for both models.
  4. Compute δ^{ℓmid} = x_{DPO}^{ℓmid} - x_{GPT2}^{ℓmid}; compute mean shift δ̄^ℓ_x.
  5. For each preceding layer j < ℓ and each value vector i, compute cosine similarity cos(δ^{ℓmid}, δ^j_MLP.v_i).
  6. Project residual streams at layer 19 onto (δ̄^{19}_x, main principal component) to visualize shift and activation status.
  7. Plot proportion of value vectors at each layer with various cosine similarity scores and mean activations.
- **Metrics**: Mean activation per toxic vector; cosine similarity cos(δMLP.v, δx); residual stream 2D projections
- **Expected outcome**:
  - Mean activations of MLP.vToxic drop substantially in GPT2DPO vs. GPT2
  - Residual streams in GPT2DPO show consistent linear shift away from toxic activation regions
  - δMLP.v has predominantly negative cosine similarity with δx (antipodal relationship)
  - Most value vector activations are negative (due to GeLU sparsity), explaining sign flip
  - As layers approach toxic layer 19, the proportion of value vectors with negative cosine similarity to δx increases
- **Baselines**: GPT2 (no DPO)
- **Dependencies**: E01, E03

## E05: Un-alignment via Key Vector Scaling
- **Verifies**: C06
- **Setup**:
  - Model: GPT2DPO (DPO fine-tuned)
  - Hardware: Not specified in paper
  - Dataset: RealToxicityPrompts challenge subset (1,199 prompts); Wikitext-2; 2,000 Wikipedia sentences
  - System: Scale toxic key vectors by 10× in GPT2DPO
- **Procedure**:
  1. Load GPT2DPO.
  2. Identify the 7 MLP key vectors with highest cosine similarity to WToxic (top-7 from MLP.kToxic).
  3. Scale each selected key vector by factor 10×.
  4. Generate continuations for 1,199 RealToxicityPrompts challenge prompts; score with Perspective API.
  5. Compute perplexity on Wikitext-2; compute F1 on 2,000 Wikipedia sentence completions.
  6. Compare toxicity, perplexity, and F1 to GPT2DPO baseline and original GPT2.
- **Metrics**: Toxicity (Perspective API), perplexity (Wikitext-2), F1 (Wikipedia continuations)
- **Expected outcome**:
  - Toxicity reverts to near-original GPT2 levels after scaling 7 key vectors
  - Perplexity remains near GPT2DPO level (unlike residual stream interventions)
  - F1 remains near GPT2DPO level
  - Un-alignment is achieved with minimal impact on language quality
- **Baselines**: GPT2DPO (before un-alignment), GPT2 (original)
- **Dependencies**: E01, E03

## E06: Logit Lens Analysis of Toxic Token Promotion
- **Verifies**: C03
- **Setup**:
  - Model: GPT2-medium and GPT2DPO
  - Hardware: Not specified in paper
  - Dataset: 295 prompts from RealToxicityPrompts that cause GPT2 to output "sh*t" as the next token
  - System: Apply unembedding layer at each intermediate layer
- **Procedure**:
  1. Filter RealToxicityPrompts to identify 295 prompts for which GPT2 assigns highest probability to "sh*t" as next token.
  2. For both GPT2 and GPT2DPO, run forward pass and at each intermediate layer ℓ (including ℓmid after attention but before MLP), apply unembedding layer U to x^ℓ.
  3. Compute probability of "sh*t" token at each intermediate layer.
  4. Average over all 295 prompts to get mean probability per layer.
  5. Identify which layers (particularly MLP layers) show the largest spike in "sh*t" probability.
- **Metrics**: Mean probability of token "sh*t" per intermediate layer
- **Expected outcome**:
  - "sh*t" probability is near zero for layers 1–16 in GPT2
  - Probability spikes at specific MLP layers in GPT2 (shaded regions corresponding to MLP layers 17–23)
  - GPT2DPO shows consistently lower probability of "sh*t" than GPT2 at all layers
  - Maximum probability in GPT2DPO is substantially below that of GPT2
- **Baselines**: GPT2 (no DPO)
- **Dependencies**: E01
