# Model Configuration

## vision_encoder_architecture
- **Value**: ViT-L/14 (Vision Transformer Large, patch size 14)
- **Rationale**: Used by both OpenFlamingo 9B and LLaVA-1.5 7B/13B as their CLIP vision encoder; enabling single encoder to improve all LVLMs simultaneously
- **Search range**: ViT-B/32 used for hyperparameter ablations only
- **Sensitivity**: high
- **Source**: §4 (Setting), §2

## vision_encoder_source
- **Value**: OpenAI CLIP ViT-L/14 (openai/clip-vit-large-patch14)
- **Rationale**: The exact checkpoint used by LLaVA-1.5 and OpenFlamingo
- **Search range**: N/A
- **Sensitivity**: high
- **Source**: §2, reproduction rubric

## image_resolution
- **Value**: 224×224 pixels
- **Rationale**: ViT-L/14@224 (not ViT-L/14@336) is used, consistent with the checkpoint in LLaVA-1.5 and OpenFlamingo
- **Search range**: N/A
- **Sensitivity**: high
- **Source**: Appendix B.1, reproduction rubric

## embedding_dimension
- **Value**: 1024 (ViT-L/14 output dimension D)
- **Rationale**: Standard ViT-L/14 output dimension; used in FARE loss computation
- **Search range**: N/A
- **Sensitivity**: low
- **Source**: CLIP architecture specification

## text_encoder
- **Value**: CLIP text encoder ψ (OpenAI ViT-L/14 text encoder); frozen throughout FARE fine-tuning
- **Rationale**: Text encoder is not modified by FARE; only image encoder φ is fine-tuned
- **Search range**: N/A
- **Sensitivity**: N/A (frozen)
- **Source**: §3.3

## llava_model
- **Value**: LLaVA-1.5 7B (LLaVA with Vicuna-7B LLM backbone)
- **Rationale**: Primary LVLM evaluation target; uses ViT-L/14 frozen vision encoder
- **Search range**: Also evaluated: LLaVA-1.5 13B (Appendix C.3)
- **Sensitivity**: high
- **Source**: §4

## openflamingo_model
- **Value**: OpenFlamingo 9B (MPT-7B LLM backbone)
- **Rationale**: Second LVLM evaluation target; uses ViT-L/14 frozen vision encoder
- **Search range**: N/A
- **Sensitivity**: high
- **Source**: §4

## llava_vision_encoder_layer
- **Value**: Second-last layer outputs (all tokens) for LLaVA; class token for FARE loss computation
- **Rationale**: LLaVA uses second-last layer, but FARE loss computed on class token is sufficient
- **Search range**: N/A
- **Sensitivity**: medium
- **Source**: Appendix B.1

## vitb32_ablation_model
- **Value**: ViT-B/32 CLIP (used for hyperparameter ablations only, not main paper results)
- **Rationale**: Cheaper to train for ablation studies; results transferred to ViT-L/14
- **Search range**: N/A
- **Sensitivity**: N/A
- **Source**: Appendix B.3
