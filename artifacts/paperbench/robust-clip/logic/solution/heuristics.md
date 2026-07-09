# Heuristics

## H01: Use Class Token Only for FARE Loss Computation
- **Rationale**: LLaVA and OpenFlamingo use all token outputs from ViT, but early experiments showed that computing FARE loss on the class token alone is sufficient to achieve good downstream LVLM performance. Using all tokens requires more memory and compute without yielding improvements.
- **Sensitivity**: medium
- **Bounds**: Applicable to ViT-based encoders; may not generalize to non-ViT architectures. Loss on class token ⊆ information needed for all-token downstream tasks.
- **Code ref**: [src/execution/fare_training.py]
- **Source**: Appendix B.1

## H02: Short Fine-Tuning with Many PGD Steps (10 steps × 2 epochs)
- **Rationale**: In long adversarial training (300 epochs), 2–3 PGD steps suffice. In short fine-tuning, more steps compensate for fewer epochs. 10 steps with 2 epochs achieves non-trivial robustness while costing only 0.2% of original CLIP training.
- **Sensitivity**: medium
- **Bounds**: 10 PGD steps, 2 epochs, step size 1/255. Fewer steps (e.g., 2) with short fine-tuning leads to weaker robustness.
- **Code ref**: [src/execution/fare_training.py]
- **Source**: §4 (Setting), Appendix B.1, B.3

## H03: Small Learning Rate (1e-5) for Better Zero-Shot Generalization
- **Rationale**: Larger LR (1e-4) yields better ImageNet robustness (+5% on average) but hurts zero-shot generalization on non-ImageNet datasets by -4.2% clean accuracy. Since FARE's goal is to preserve generalization, the smaller LR is preferred.
- **Sensitivity**: high
- **Bounds**: Tested values: {1e-5, 1e-4}; 1e-5 chosen. Weight decay {1e-3, 1e-4}: no impact observed; 1e-4 chosen.
- **Code ref**: [src/execution/fare_training.py]
- **Source**: Appendix B.3, Table 8

## H04: Cosine LR Schedule with Linear Warmup to 7% of Total Steps
- **Rationale**: Standard practice for transformer fine-tuning. Warmup to peak LR at 7% of training steps prevents instability at the start of fine-tuning.
- **Sensitivity**: low
- **Bounds**: Peak LR = 1e-5; warmup fraction = 7% of total training steps. Cosine decay applied after warmup.
- **Code ref**: [src/execution/fare_training.py]
- **Source**: Appendix B.1

## H05: ε=2/255 Training for Clean-Performance-Prioritized Use Cases
- **Rationale**: ε=2/255 provides non-trivial robustness at both test radii while maintaining clean performance very close to the original CLIP. For ε=2/255 testing it is comparable to ε=4/255-trained models; for ε=4/255 testing it is slightly less robust but has better clean accuracy.
- **Sensitivity**: high
- **Bounds**: FARE2 achieves 0% attack success at ε=2/255; 2.0% mean at ε=4/255. FARE4 achieves 0% at both.
- **Code ref**: [src/execution/fare_training.py]
- **Source**: §4 (Controlling the clean vs robust accuracy trade-off), Table 3

## H06: Squared ℓ₂ Norm (Not ℓ₁) for FARE Loss
- **Rationale**: Squared ℓ₂ connects naturally to cosine similarity via the identity ||u/||u||₂ - v/||v||₂||²₂ = 2 - 2cos(u,v), and preserves non-normalized embeddings (which LVLMs use). ℓ₁ loss leads to sparse residuals with no clear motivation in this setting.
- **Sensitivity**: low
- **Bounds**: Ablation (Table 9) shows ℓ₁ and ℓ₂ give comparable results (e.g., 48.6/33.7/21.9 vs 48.6/33.9/21.9 on avg. zero-shot clean/2/4), so choice is not critical.
- **Code ref**: [src/execution/fare_training.py]
- **Source**: §3.3, Appendix B.4, Table 9
