# Model Configurations

## NetHack: 33M LSTM Architecture

### hidden_dim (LSTM)
- **Value**: 1738
- **Rationale**: Determined by Tuyls et al. (2023) scaling law study; scaled from the 6M model used in Hambro et al. (2022)
- **Sensitivity**: high
- **Source**: Table 1, Appendix B.1

### activation_function
- **Value**: relu
- **Rationale**: Standard activation for the MLP components
- **Sensitivity**: low
- **Source**: Table 1, Appendix B.1

### total_parameters
- **Value**: 33M (fine-tuned model); 6M (baseline CDGPT5 model)
- **Source**: Appendix B.1

### architecture_overview
- **Value**: 3 encoders (main screen ResNet + blstats 2-layer MLP + message 2-layer MLP) → concatenate → LSTM (hidden_dim=1738) → policy head + baseline head
- **Source**: Appendix B.1

### main_screen_encoder
- **Value**: Character and color embedding lookup → grid → ResNet (see Tuyls et al. 2023 for details)
- **Source**: Appendix B.1

### blstats_encoder
- **Value**: 2-layer MLP (processes player status: health, hunger, etc.)
- **Source**: Appendix B.1

### message_encoder
- **Value**: 2-layer MLP (processes text notifications/warnings)
- **Source**: Appendix B.1

### action_space
- **Value**: 120 discrete actions
- **Source**: Appendix B.1

### joint_backbone
- **Value**: Actor and critic share encoders + LSTM; separate policy head and baseline head
- **Source**: Appendix B.1

### encoder_frozen_during_finetuning
- **Value**: True (all 3 encoders frozen)
- **Source**: Section B.1 (Fine-tuning subsection)

---

## Montezuma's Revenge: PPO+RND Architecture

### base_architecture
- **Value**: CNN-based architecture from jcwleo/random-network-distillation-pytorch
- **Source**: Appendix B.2

### rnd_output_dim
- **Value**: 512 (both target and prediction networks)
- **Source**: Appendix B.2

### target_network
- **Value**: Randomly initialized and frozen; maps observations to 512-dim vectors
- **Source**: Appendix B.2

### prediction_network
- **Value**: Trained to predict target network outputs; prediction error = intrinsic reward
- **Source**: Appendix B.2

### state_representation
- **Value**: 84×84 grayscale frames, stacked 4 frames (StateStackSize=4)
- **Source**: Table 2, Appendix B.2

---

## RoboticSequence: SAC MLP Architecture

### policy_architecture
- **Value**: 4-layer MLP, 256 neurons per hidden layer, Leaky-ReLU activations, LayerNorm after first layer
- **Source**: Appendix B.3

### critic_architecture
- **Value**: 4-layer MLP, 256 neurons per hidden layer, Leaky-ReLU activations, LayerNorm after first layer
- **Source**: Appendix B.3

### output_heads
- **Value**: Separate output head per stage (4 heads for 4-stage sequence); head selected by stage ID (one-hot encoded)
- **Rationale**: Outperforms adding stage ID to observation vector
- **Source**: Appendix B.3

### observation_space
- **Value**: Robot configuration info (from Meta-World) + stage ID (one-hot) + normalized timestep (t/T)
- **Source**: Appendix B.3

### entropy_coefficient
- **Value**: Auto-tuned (Haarnoja et al., 2018b)
- **Source**: Appendix B.3

### fisher_matrix_clip
- **Value**: min 1e-5 (for EWC)
- **Source**: Rubric (task bea5ee41)

### fisher_matrix_samples
- **Value**: 2560 examples from replay buffer (for EWC Fisher estimation)
- **Source**: Rubric (task 70f0fef8)
