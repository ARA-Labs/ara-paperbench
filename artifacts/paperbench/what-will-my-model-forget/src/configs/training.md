# Training Configuration

## Model Refinement Hyperparameters

### Number of Gradient Steps (Single Error)
- **Value**: 30 steps for LoRA/Full FT; 100 steps for LM head only
- **Rationale**: Sufficient to achieve >95% edit success rate; few-shot fine-tuning is standard for model refinement
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Section 4.1, "Hyperparameters"

### Learning Rate — BART0Large (Single Error Fix)
- **Value**: 10^-5 for Full FT and LoRA; 10^-3 for head-only
- **Rationale**: Tuned to maximize edit success rate on mispredicted examples
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Section 4.1, "Hyperparameters"

### Learning Rate — FLAN-T5Large (Single Error Fix)
- **Value**: 10^-4 for Full FT and LoRA; 10^-4 for head-only
- **Rationale**: FLAN-T5 requires higher LR than BART0 due to different scale/initialization
- **Search range**: 1e-4, 1e-5, 2e-6 tested (Appendix D.1)
- **Sensitivity**: high
- **Source**: Section 4.1, "Hyperparameters"; Appendix D.1, Table 9

### Learning Rate — Sequential Error Fixing (BART0Large)
- **Value**: 10^-6
- **Rationale**: Lower LR needed when fixing multiple errors sequentially to avoid compounding forgetting
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Section 4.1, "Hyperparameters"

### Learning Rate — Sequential Error Fixing (FLAN-T5)
- **Value**: 10^-5
- **Rationale**: Same rationale as BART0 sequential; higher than BART0 due to model scale
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Section 4.1, "Hyperparameters"

### Replay Mini-Batch Size (BART0Large and FLAN-T5Large)
- **Value**: 8 examples per mini-batch, every 10 training steps
- **Rationale**: Sparse replay avoids over-tuning on replayed examples; 3 replay batches over 30 steps
- **Search range**: 3, 6, 9, 15 batches tested (Appendix D.2, Table 10)
- **Sensitivity**: medium
- **Source**: Section 4.2, "Model Refinement"

### Replay Mini-Batch Size (FLAN-T53B)
- **Value**: 4 examples per mini-batch, every 5 training steps
- **Rationale**: Smaller batch size per replay due to model size constraints
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Section 4.2, "Model Refinement"

### DR Train/Test Split
- **Value**: 60% train, 40% test (random split)
- **Rationale**: Standard split to evaluate generalization of forecasting models
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Rubric specification (inferred from setup description)

## Forecasting Model Training Hyperparameters

### LM Backbone Learning Rate
- **Value**: 10^-5
- **Rationale**: Fine-tune the backbone PTLM at lower LR to preserve pretrained representations
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Appendix B, "Training Details of the Forecasting Models"

### MLP Head Learning Rate
- **Value**: 10^-4
- **Rationale**: Higher LR for the freshly initialized MLP layers
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Appendix B, "Training Details of the Forecasting Models"

### Max Training Steps
- **Value**: 100,000 steps
- **Rationale**: Sufficient convergence for the forecasting model
- **Search range**: Not specified
- **Sensitivity**: low
- **Source**: Appendix B, "Training Details of the Forecasting Models"

### Mini-Batch Composition
- **Value**: 8 positive pairs + 8 negative pairs per mini-batch (batch size = 16 total)
- **Rationale**: Balanced sampling from positive/negative pairs within each batch ensures the model sees sufficient positive examples despite class imbalance
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Appendix B, "Training Details of the Forecasting Models"

### Positive Pair Weight
- **Value**: α = 0.1 (weight assigned to positive pairs in the loss)
- **Rationale**: Compensates for the 1-10% positive class rate; ensures positive examples contribute meaningfully to the loss
- **Search range**: Not specified
- **Sensitivity**: high
- **Source**: Appendix B, "Training Details of the Forecasting Models"

### LoRA Application
- **Value**: Applied to query (Q) and value (V) matrices in all self-attention layers; NOT applied to key (K) matrices
- **Rationale**: Standard LoRA configuration; Q and V capture content-dependent interactions
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: Rubric specification (multiple task entries specify "LoRA was applied to the query and value (but not key) matrices in all self-attention layers")
