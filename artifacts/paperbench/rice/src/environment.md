# Environment

## Python
- **Version**: Not specified in paper

## Framework
- **Primary**: PyTorch (Paszke et al., 2019)
- **MuJoCo RL**: Stable-Baselines3 (Raffin et al., 2021)
- **Malware RL**: Tianshou (Weng et al., 2022)
- **Autonomous Driving**: DI-drive (drive Contributors, 2021)
- **JSRL Baseline**: https://github.com/steventango/jumpstart-rl
- **StateMask Baseline**: https://github.com/nuwuxian/RL-state_mask

## Hardware
- **GPU type**: NVIDIA A100
- **GPU count**: 8
- **Memory**: Not specified in paper

## Key Dependencies
| Package | Version |
|---------|---------|
| PyTorch | Not specified |
| Stable-Baselines3 | Not specified |
| Tianshou | Not specified |
| MuJoCo | Compatible with Hopper-v3, Walker2d-v3, Reacher-v2, HalfCheetah-v3 |
| MetaDrive | Macro-v1 environment |
| CAGE Challenge 2 | https://github.com/cage-challenge/cage-challenge-2 |
| Selfish Mining | https://github.com/roibarzur/pto-selfish-mining |
| Malware RL | https://github.com/bfilar/malware_rl |

## Source Code
- **RICE**: https://github.com/chengzelei/RICE

## Random Seeds
- **Number of seeds**: 3 per experiment
- **Specific seed values**: Not specified in paper

## Environment Reset Mechanism
- Based on Ecoffet et al. (2019) Go-Explore state restoration
- Requires simulator-based environment supporting arbitrary state reset
- Incompatible with non-deterministic stochastic environments without goal-conditioning
