# Constraints

## Boundary Conditions

### BC1: GPT2-medium Specificity
- **Condition**: All experiments use GPT2-medium (L=24, d=1024, dmlp=4096, GeLU activations). The antipodal shift mechanism specifically relies on GeLU's sparsity (mostly-negative activations for inactive neurons). Models with different activation functions (e.g., ReLU, SiLU) may exhibit different patterns.
- **Implication**: The bypass mechanism may not generalize identically to larger models (GPT-3, LLaMA) without replication.

### BC2: GeLU Activation Sparsity Required
- **Condition**: The antipodal δMLP.v / δx relationship (C05) depends on MLP neurons being predominantly inactive (negative activations) for the specific prompts evaluated. This is empirically true for RealToxicityPrompts with GPT2 (as shown in Figure 5), but may not hold universally.
- **Implication**: For prompts where many neurons are active, the distributed bypass mechanism would be less effective or absent.

### BC3: Toxicity Probe Dataset Bias
- **Condition**: WToxic is trained on the Jigsaw Toxic Comment Classification dataset, which has gendered biases (noted: SVD.UToxic[2] has a "particularly gendered nature"). The probe captures dataset-specific toxicity definitions.
- **Implication**: Different toxicity definitions or datasets could yield different toxic vectors and different DPO training dynamics.

### BC4: N=128 Toxic Vectors
- **Condition**: The set MLP.vToxic is defined as the top-128 value vectors by cosine similarity with WToxic. The paper notes "similar results" for different values of N, but does not specify the range tested.
- **Implication**: Very small N may miss important toxic vectors; very large N may include non-toxic vectors.

### BC5: Un-alignment Requires Only 7 Key Vectors
- **Condition**: The un-alignment attack selects the top-7 MLP.kToxic vectors. This was sufficient to restore toxicity to GPT2 levels, but the minimum number was not ablated.
- **Implication**: The exact number 7 is specific to this model and dataset; generalization requires empirical verification.

### BC6: Training Convergence at ~6,000 Pairs
- **Condition**: DPO training with patience=10 on validation loss converges after approximately 6,000 sample pairs out of 24,576 total. Training may require more pairs for other models or toxicity domains.
- **Implication**: Dataset size of 24,576 provides substantial headroom; the effective training set is much smaller.

## Known Limitations

### L1: Single Model, Single Behavior
The paper studies only GPT2-medium and only toxicity. Generalization to other models (LLaMA, GPT-3) and other undesirable behaviors (bias, harmful instruction following) is not demonstrated.

### L2: Evaluation with Automated Toxicity Scorer
Toxicity is measured with Perspective API, an automated tool that may not perfectly capture human judgments about toxicity. Results may differ with human evaluation.

### L3: Simplified PPLM Data Generation
Using PPLM with a linear classifier as attribute controller may not produce the most natural or diverse toxic samples. More sophisticated data generation could affect DPO training dynamics.

### L4: No Comparison with PPO
The paper focuses exclusively on DPO. Whether the same bypass mechanism applies to PPO-based alignment is hypothesized but not demonstrated.

### L5: Jailbreak Generalization Not Tested
While the paper provides a mechanistic explanation for why jailbreaks are possible, it does not demonstrate that the identified un-alignment method works as a black-box jailbreak (it requires white-box access to key vectors).
