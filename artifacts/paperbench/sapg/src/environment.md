---
# Environment

## Python
- **Python**: Not specified in paper; compatible with IsaacGym requirements (typically Python 3.7+)

## Framework
- **Deep Learning**: PyTorch (version not specified in paper)
- **Simulator**: IsaacGym (GPU-accelerated physics simulation)
- **Physics Engine**: PhysX (underlying IsaacGym), MuJoCo 3.0 mentioned as alternative GPU simulator

## Hardware
- **GPU**: Single GPU per experiment (type not specified; must support IsaacGym — typically NVIDIA A100 or similar)
- **Memory**: Not specified in paper
- **Training duration**: ~48–60 hours per experiment on a single GPU
- **Total transitions**: ~2×10¹⁰ per experiment

## Key Dependencies
- IsaacGymEnvs (for AllegroKuka, ShadowHand, AllegroHand environments)
- PyTorch (version not specified)
- ELU activation: Clevert et al. [4] implementation available in PyTorch nn.ELU

## Parallel Environments
- **N**: 24,576 parallel environments (default for all main experiments)
- **Environments per policy block**: 24,576 / 6 = 4,096

## Random Seeds
- **Number of seeds**: 5 seeds per experiment
- **Seed values**: Not specified in paper

## Compute Budget
- **Per run**: ~48–60 hours on single GPU
- **Note**: Different experiments run on different machines; wall-clock time is not directly comparable across methods. Comparison is based on number of environment steps.

## Task Environments
- **Hard tasks**: AllegroKuka Regrasping, Throw, Reorientation, Two Arms Reorientation (from IsaacGymEnvs/DexPBT)
- **Easy tasks**: ShadowHand, AllegroHand (from IsaacGymEnvs)
