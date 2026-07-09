# Environment

- **Python**: Not specified in paper
- **Framework**: Not specified in paper (PyTorch implied by transformer/neural network usage)
- **Hardware**: Not specified in paper
- **Key dependencies**:
  - D4RL (Fu et al., 2020): antmaze-large-diverse-v2, kitchen-complete-v0 datasets and environments
  - ExORL (Yarats et al., 2022): cheetah RND, walker RND datasets; custom DMControl tasks from https://github.com/denisyarats/exorl/tree/main/custom_dmc_tasks
  - DeepMind Control Suite (Tassa et al., 2018): Walker and Cheetah base environments
  - D4RL Ant Maze environment: https://github.com/Farama-Foundation/D4RL
  - D4RL Kitchen environment: https://github.com/Farama-Foundation/D4RL
  - FB/SF baseline code: https://github.com/facebookresearch/controllable_agent
  - FRE project code: https://github.com/kvfrans/fre
- **Random seeds**: 5 seeds used for all experiments; specific seed values not specified in paper
- **Batch size**: Listed in Appendix A Table 3 but value not explicitly provided in paper text
