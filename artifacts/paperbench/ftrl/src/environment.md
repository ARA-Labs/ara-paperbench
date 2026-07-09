# Environment

## NetHack
- **Python**: Not specified in paper
- **Framework**: PyTorch; Sample Factory (APPO implementation, Petrenko et al. 2020)
- **NLE (NetHack Learning Environment)**: https://github.com/heiner/nle (Küttler et al., 2020)
- **Hardware**: Single NVIDIA A100 GPU; >500M environment steps per 24 hours
- **Key dependencies**:
  - nle (NetHack Learning Environment)
  - sample-factory (https://github.com/alex-petrenko/sample-factory/)
  - AutoAscend (https://github.com/cdmatters/autoascend/tree/jt-nld)
  - Pre-trained weights: https://drive.google.com/uc?id=1tWxA92qkat7Uee8SKMNsj-BV1K9ENExl
- **Dataset**: NLD-AA (Hambro et al., 2022c) from https://github.com/dungeonsdatasubmission/dungeonsdata-neurips2022; ~8000 Human Monk games used
- **Random seeds**: 5 seeds per method
- **Code**: https://github.com/BartekCupial/finetuning-RL-as-CL

## Montezuma's Revenge
- **Framework**: PyTorch; PPO + RND from jcwleo/random-network-distillation-pytorch
- **ALE (Arcade Learning Environment)**: https://github.com/jcwleo/random-network-distillation-pytorch (Bellemare et al., 2013; Machado et al., 2018)
- **Hardware**: GPU (not further specified in paper)
- **Key dependencies**:
  - Atari/ALE environment
  - PPO+RND implementation: https://github.com/jcwleo/random-network-distillation-pytorch
- **Random seeds**: 5 seeds per method

## RoboticSequence (Meta-World)
- **Framework**: PyTorch; SAC implementation based on Continual World (Wołczyk et al., 2021)
- **Hardware**: 8 CPU cores, 30 GB RAM per experiment; ~48 hours per run; GPU gains marginal for small observations
- **Key dependencies**:
  - Meta-World benchmark (Yu et al., 2020)
  - Continual World codebase (Wołczyk et al., 2021)
- **Random seeds**: 20 seeds per method, 90% confidence intervals
- **Compute**: Over 20,000 experiments run during the research; PLGrid HPC (ACK Cyfronet AGH) used; grant PLG/2023/016286
