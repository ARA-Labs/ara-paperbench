# Model Configuration

## Architecture
- **Value**: U-Net from Ho et al. (2020b) / luciddrains's `denoising-diffusion-pytorch`
- **Rationale**: Proven architecture for image generation with multi-scale feature processing; supports class conditioning.
- **Search range**: Not applicable
- **Sensitivity**: high
- **Source**: paper §Appendix B "we use the U-net from (Ho et al., 2020b) as implemented in lucidrain's denoising-diffusion-pytorch repository"

## dim (Base Channel Dimension)
- **Value**: 256
- **Rationale**: Large channel count provides sufficient model capacity for ImageNet-scale generation.
- **Search range**: Not specified; no default for this architecture variant.
- **Sensitivity**: high
- **Source**: paper §Appendix B "Dim (channels): 256"

## dim_mults (Channel Multipliers per Resolution)
- **Value**: (1, 1, 2, 3, 4)
- **Rationale**: Provides gradual channel expansion with two stages at base resolution (1,1), enabling strong local feature extraction before upsampling.
- **Search range**: Default in luciddrains repo is (1, 2, 4, 8)
- **Sensitivity**: high
- **Source**: paper §Appendix B "Dim Mults: (1,1,2,3,4)"

## resnet_block_groups
- **Value**: 8
- **Rationale**: Group normalization with 8 groups is standard; balances between layer norm and batch norm behavior.
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: paper §Appendix B "Resnet block groups: 8"

## learned_sinusoidal_cond
- **Value**: True
- **Rationale**: Learnable sinusoidal time embedding allows the model to adapt its temporal encoding to the training data.
- **Search range**: Default in luciddrains repo is False
- **Sensitivity**: medium
- **Source**: paper §Appendix B "Learned Sinusoidal Cond: True"

## learned_sinusoidal_dim
- **Value**: 32
- **Rationale**: 32-dimensional learned sinusoidal embedding provides sufficient expressiveness for time conditioning.
- **Search range**: Default in luciddrains repo is 16
- **Sensitivity**: low
- **Source**: paper §Appendix B "Learned Sinusoidal Dim: 32"

## attn_dim_head
- **Value**: 64
- **Rationale**: 64-dimensional attention heads balance computational cost and expressiveness.
- **Search range**: Default in luciddrains repo is 32
- **Sensitivity**: medium
- **Source**: paper §Appendix B "Attention Dim Head: 64"

## attn_heads
- **Value**: 4
- **Rationale**: 4 attention heads for multi-head attention; matches default.
- **Search range**: Default in luciddrains repo is 4
- **Sensitivity**: medium
- **Source**: paper §Appendix B "Attention Heads: 4"

## random_fourier_features
- **Value**: False
- **Rationale**: Learnable sinusoidal conditioning is used instead; random Fourier features are not needed.
- **Search range**: Default in luciddrains repo is False
- **Sensitivity**: low
- **Source**: paper §Appendix B "Random Fourier Features: False"

## Input Channels (Inpainting)
- **Value**: C_image + C_mask (3 image channels + 1 mask channel, plus class embedding)
- **Rationale**: Mask ξ is appended to the input as extra channels for spatial conditioning.
- **Search range**: Not applicable
- **Sensitivity**: high
- **Source**: §4.1 "ξ is given to the model as appended channels of the image x"

## Input Channels (Super-resolution)
- **Value**: C_image + C_lowres (3 high-res channels + 3 low-res channels concatenated)
- **Rationale**: Low-resolution guidance ξ=U(D(x₁)) is appended along channel dimension at each U-Net input.
- **Search range**: Not applicable
- **Sensitivity**: high
- **Source**: Appendix B "we follow (Ho et al., 2022a) and append upsampled low-resolution images to the input xₜ"

## Output Channels
- **Value**: C_image = 3 (only image channels; conditioning channels not predicted)
- **Rationale**: Model predicts velocity only for the image pixels; conditioning (mask, low-res, class) is input-only.
- **Search range**: Not applicable
- **Sensitivity**: high
- **Source**: §4.1 "The approximate velocity field only acts on the image, not the additional class channel"
