# Constraints

## Boundary Conditions

### BC1: Frozen Vision Encoder Requirement
- **Constraint**: FARE applies only to LVLMs that use CLIP as a *frozen* vision encoder (not fine-tuned jointly with the LVLM). If the vision encoder is updated during LVLM training, FARE must be applied after the LVLM is fully trained.
- **Affected tasks**: Newer LVLMs that fine-tune the vision encoder may need FARE applied post-training.
- **Workaround**: The paper notes FARE can still be applied after full LVLM training at low extra cost.

### BC2: Perturbation Radius Trade-off
- **Constraint**: Models trained at ε=2/255 (FARE2) provide better clean performance but are not fully robust at ε=4/255. Models trained at ε=4/255 (FARE4) are fully robust at both radii but sacrifice some clean performance.
- **Quantification**: FARE2 mean success rate for targeted attacks at ε=4/255 is 2.0%; FARE4 is 0%.
- **Implication**: For deployments requiring imperceptible-perturbation robustness only, FARE2 is preferred; for higher robustness, FARE4 is needed.

### BC3: Language-Side Robustness Not Addressed
- **Constraint**: FARE only addresses robustness of the visual input modality. Adversarial attacks on the text input of LVLMs are not defended.
- **Scope**: This is explicitly acknowledged as a limitation.

### BC4: CLIP-Based LVLMs Only
- **Constraint**: The method is demonstrated for CLIP-based LVLMs. Other LVLM architectures (not using CLIP as backbone) would require a separate robust encoder.
- **Scope**: OpenFlamingo 9B and LLaVA-1.5 7B/13B are validated; generalization to other CLIP-based models (e.g., BLIP-2, Shikra) is expected but not explicitly measured.

### BC5: ℓ∞ Threat Model
- **Constraint**: FARE is trained and evaluated under the ℓ∞ threat model. Other threat models (ℓ₂, etc.) are not directly addressed.

### BC6: ImageNet Resolution
- **Constraint**: All training is performed at 224×224 image resolution (ImageNet standard). CIFAR10/CIFAR100/STL-10 are evaluated at their native resolution for zero-shot, but training uses only 224×224.

### BC7: Class Token Sufficiency
- **Constraint**: FARE loss is computed using only the class token of the ViT encoder. LLaVA uses second-last layer outputs of all tokens, and OpenFlamingo uses all token outputs. The paper shows (Appendix B.1) that class token is sufficient for good downstream results.

## Known Limitations

- **L1**: TeCoA outperforms FARE on ImageNet-specific clean and robust accuracy (because TeCoA has supervised ImageNet training signal). FARE is not optimal for single-dataset supervised settings.
- **L2**: Jailbreaking attack evaluation is based on one attack method (Qi et al., 2023) and may overestimate robustness. Authors note this is a preliminary evaluation.
- **L3**: The paper does not examine instruction following, explainability, or perception-related tasks.
- **L4**: FARE robustness evaluation does not cover ℓ₁ or ℓ₂ threat models.
- **L5**: Transfer robustness is shown for COCO captioning only; robustness under adaptive white-box attacks directly targeting the fine-tuned encoder is the intended evaluation in main tables.
