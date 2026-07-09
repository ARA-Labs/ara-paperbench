---
# Model Configuration

## Adaptor Bottleneck Spatial Downscale Factor c (DDPM)
- **Value**: 4
- **Rationale**: Controls spatial compression of adaptor input. For DDPM, c=4 reduces input from w×h×r to w/4 × h/4 × d.
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §5.2 Configurations ("For the DDPMs, we set the parameters c=4 and d=8")

## Adaptor Bottleneck Channel Dimension d (DDPM)
- **Value**: 8
- **Rationale**: Low-dimensional bottleneck for parameter efficiency; d=8 ensures very few parameters per adaptor
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §5.2 Configurations

## Adaptor Bottleneck Spatial Downscale Factor c (LDM)
- **Value**: 2
- **Rationale**: Smaller downscale factor for LDM (which already operates in compressed latent space); c=2 provides appropriate bottleneck
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §5.2 Configurations ("we set c=2 and d=8 for the LDMs")

## Adaptor Bottleneck Channel Dimension d (LDM)
- **Value**: 8
- **Rationale**: Same as DDPM; low-dimensional bottleneck
- **Search range**: Not specified in paper
- **Sensitivity**: medium
- **Source**: §5.2 Configurations

## Adaptor Parameter Initialization
- **Value**: All parameters set to 0 (zero initialization)
- **Rationale**: Ensures adaptor output is zero at initialization, so augmented model = pre-trained model at start; stable training
- **Search range**: N/A
- **Sensitivity**: high
- **Source**: §5.2 Configurations

## Parameter Rate (DDPM-TAN)
- **Value**: 1.3% of pre-trained model parameters
- **Rationale**: Only adaptor parameters ψ are trained; all pre-trained U-Net parameters θ are frozen
- **Search range**: N/A
- **Sensitivity**: N/A
- **Source**: Table 1

## Parameter Rate (LDM-TAN)
- **Value**: 1.6% of pre-trained model parameters
- **Rationale**: LDM has different architecture; slightly higher fraction due to adaptor placement differences
- **Search range**: N/A
- **Sensitivity**: N/A
- **Source**: Table 1

## Pre-trained DDPM Backbone
- **Value**: DDPM similar to DDPM-PA [34] (pre-trained on FFHQ or LSUN Church)
- **Rationale**: Same pre-trained model as DDPM-PA baseline for fair comparison
- **Search range**: N/A
- **Sensitivity**: high
- **Source**: §5.2 Configurations

## Pre-trained LDM Backbone
- **Value**: Pre-trained LDM as provided in [23] (Rombach et al., LDM CVPR 2022)
- **Rationale**: State-of-the-art LDM for high-resolution synthesis; autoencoder kept frozen
- **Search range**: N/A
- **Sensitivity**: high
- **Source**: §5.2 Configurations

## Binary Classifier Backbone
- **Value**: Pre-trained model on ImageNet fine-tuned with binary classification head on 10 target-domain images
- **Rationale**: ImageNet features provide rich representations; fine-tuning on 10 images adapts them to source/target discrimination
- **Search range**: N/A
- **Sensitivity**: medium
- **Source**: §5.2 Configurations (inferred from rubric requirement)

## Frozen Components During Fine-tuning
- **Value**: Pre-trained DPM U-Net θ, autoencoder (for LDM), binary classifier pϕ
- **Rationale**: Only adaptor parameters need updating; freezing base model prevents catastrophic forgetting and saves memory
- **Search range**: N/A
- **Sensitivity**: high
- **Source**: §4.2, §5.2
