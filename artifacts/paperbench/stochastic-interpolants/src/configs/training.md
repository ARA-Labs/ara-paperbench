# Training Configuration

## Optimizer
- **Value**: Adam
- **Rationale**: Standard optimizer for generative models; adaptive learning rates handle heterogeneous gradient scales in U-Net.
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: paper §Appendix B "We use Adam optimizer (Kingma & Ba, 2014)"

## Learning Rate (Initial)
- **Value**: 2e-4
- **Rationale**: Standard learning rate for U-Net training on ImageNet-scale tasks.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: paper §Appendix B "starting at learning rate 2e-4"

## Learning Rate Scheduler
- **Value**: StepLR; multiplicative factor γ=0.99 every N=1000 steps
- **Rationale**: Gradual decay prevents oscillation around final optimum; 0.99 per 1000 steps is mild.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: paper §Appendix B "StepLR scheduler which scales the learning rate by γ = .99 every N = 1000 steps"

## Weight Decay
- **Value**: 0 (no weight decay)
- **Rationale**: Authors found no benefit from regularization; standard for diffusion/flow model training.
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: paper §Appendix B "We use no weight decay"

## Gradient Norm Clipping
- **Value**: 10,000 (global L2 norm of entire parameter vector)
- **Rationale**: Prevents catastrophic gradient explosions during training; very high threshold mainly catches rare outliers.
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: paper §Appendix B "We clip gradient norms at 10,000 (this is the norm of the entire set of parameters taken as a vector, the default type of norm clipping in PyTorch library)"

## Batch Size
- **Value**: 32 (applies to ALL models: Uncoupled Interpolant inpainting, Dependent Coupling inpainting, Dependent Coupling super-resolution)
- **Rationale**: Not explicitly stated in paper; provided via reproduction rubric.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Not specified in paper text; confirmed by reproduction rubric

## Training Steps
- **Value**: 200,000 gradient steps (applies to ALL models)
- **Rationale**: Not explicitly stated in paper; provided via reproduction rubric.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Not specified in paper text; confirmed by reproduction rubric

## Time Sampling
- **Value**: tᵢ ~ U(0, 1) uniformly per sample per batch
- **Rationale**: Uniform time sampling ensures equal learning signal across all interpolation times.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: paper Algorithm 1 "Draw tᵢ ~ U(0,1)"

## Inpainting Mask Tile Probability
- **Value**: p = 0.3 per tile (64 tiles total per image)
- **Rationale**: Random masking during training provides diverse masking patterns; p=0.3 balances coverage.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: paper §4.1 "each tile is selected to enter the mask with probability p = 0.3"

## Inpainting Interpolant Coefficients
- **Value**: αₜ = t, βₜ = 1-t, γₜ = 0
- **Rationale**: Reversed coefficients ensure unmasked pixels have zero velocity, enabling output masking trick.
- **Search range**: Not applicable
- **Sensitivity**: high
- **Source**: paper §4.1 "we set αₜ = t and βₜ = 1 − t"

## Super-resolution Interpolant Coefficients
- **Value**: αₜ = 1-t, βₜ = t, γₜ = 0
- **Rationale**: Standard linear interpolant from corrupted base to clean target.
- **Search range**: Not applicable
- **Sensitivity**: high
- **Source**: paper §3.3 "If we choose αₜ = 1 − t and βₜ = t, and set γₜ = 0"

## ODE Solver (Inference)
- **Value**: Dopri (Dormand-Prince) adaptive solver from torchdiffeq (Chen, 2018)
- **Rationale**: Adaptive solver automatically adjusts step size; more efficient than fixed-step Euler for smooth flows.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: paper §Appendix B "We use the Dopri solver from the torchdiffeq library"

## Parallelism
- **Value**: PyTorch Lightning Fabric
- **Rationale**: Handles multi-GPU distribution of training.
- **Search range**: Not applicable
- **Sensitivity**: low
- **Source**: paper §Appendix B "We use Pytorch library along with Lightning Fabric to handle parallelism"
