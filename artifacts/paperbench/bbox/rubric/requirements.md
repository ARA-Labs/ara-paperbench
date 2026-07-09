# Rubric Requirements — bbox
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 279

## Experimental Setup

### R01: The deberta-v3-base model has been implemented for StrategyQ...
- **Rubric ID**: deberta-base-strategyqa
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The deberta-v3-base model has been implemented for StrategyQA with the hyperparameters specified in Appendix H.2.
- **Parent context**: The deberta-v3-base (0.1B) model has been implemented for StrategyQA, GSM8K, and ScienceQA tasks.

### R02: The deberta-v3-base model has been implemented for GSM8K wit...
- **Rubric ID**: deberta-base-gsm8k
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The deberta-v3-base model has been implemented for GSM8K with the hyperparameters specified in Appendix H.2.
- **Parent context**: The deberta-v3-base (0.1B) model has been implemented for StrategyQA, GSM8K, and ScienceQA tasks.

### R03: The deberta-v3-base model has been implemented for ScienceQA...
- **Rubric ID**: deberta-base-scienceqa
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The deberta-v3-base model has been implemented for ScienceQA with the hyperparameters specified in Appendix H.2.
- **Parent context**: The deberta-v3-base (0.1B) model has been implemented for StrategyQA, GSM8K, and ScienceQA tasks.

### R04: The deberta-v3-large model has been implemented for Strategy...
- **Rubric ID**: deberta-large-strategyqa
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The deberta-v3-large model has been implemented for StrategyQA with the hyperparameters specified in Appendix H.2.
- **Parent context**: The deberta-v3-large (0.3B) model has been implemented for StrategyQA, GSM8K, and ScienceQA tasks.

### R05: The deberta-v3-large model has been implemented for GSM8K wi...
- **Rubric ID**: deberta-large-gsm8k
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The deberta-v3-large model has been implemented for GSM8K with the hyperparameters specified in Appendix H.2.
- **Parent context**: The deberta-v3-large (0.3B) model has been implemented for StrategyQA, GSM8K, and ScienceQA tasks.

### R06: The deberta-v3-large model has been implemented for ScienceQ...
- **Rubric ID**: deberta-large-scienceqa
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The deberta-v3-large model has been implemented for ScienceQA with the hyperparameters specified in Appendix H.2.
- **Parent context**: The deberta-v3-large (0.3B) model has been implemented for StrategyQA, GSM8K, and ScienceQA tasks.

### R07: The adapter has been trained using the NCE loss and spectral...
- **Rubric ID**: adapter-training-execution
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The adapter has been trained using the NCE loss and spectral normalization for the specified number of steps.
- **Parent context**: The training process components have been implemented.

### R08: The temperature is set to 1.0 for generation as specified in...
- **Rubric ID**: temperature-setting
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The temperature is set to 1.0 for generation as specified in Appendix H.2.
- **Parent context**: The LLM generation parameters have been configured correctly.

### R09: The maximum generation length is set to 512 as specified in...
- **Rubric ID**: max-length-setting
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The maximum generation length is set to 512 as specified in Appendix H.2.
- **Parent context**: The LLM generation parameters have been configured correctly.

### R10: The model is configured with temperature 1.0 and a maximum l...
- **Rubric ID**: gpt-generation-params
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The model is configured with temperature 1.0 and a maximum length of 512 tokens for generation.
- **Parent context**: The GPT-3.5 Turbo model has been set up for evaluation with the correct configurations.

### R11: The fine-tuning hyperparameters have been configured with nu...
- **Rubric ID**: gpt-finetune-params
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The fine-tuning hyperparameters have been configured with number of epochs set to 5.
- **Parent context**: The GPT-3.5 Turbo model has been set up for evaluation with the correct configurations.

### R12: The model is configured with temperature 1.0 and a maximum l...
- **Rubric ID**: mixtral-generation-params
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The model is configured with temperature 1.0 and a maximum length of 512 tokens for generation.
- **Parent context**: The Mixtral-8x7B model has been set up for evaluation with correct configurations.

### R13: The AdamW optimizer has been configured with learning rate 5...
- **Rubric ID**: optimizer-setup
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The AdamW optimizer has been configured with learning rate 5e-6 and weight decay 0.01.
- **Parent context**: The training loop for the adapter modules has been implemented.

### R14: The training loop has been implemented to process data in ba...
- **Rubric ID**: batch-config
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The training loop has been implemented to process data in batches of size 64 and run for 6000 training steps as specified in Appendix H.2.
- **Parent context**: The training loop for the adapter modules has been implemented.

### R15: The fine-tuning hyperparameters (epochs=3, batch size and le...
- **Rubric ID**: hyperparameter-config
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The fine-tuning hyperparameters (epochs=3, batch size and learning rate as Azure OpenAI service default values) have been configured.
- **Parent context**: The Azure OpenAI fine-tuning service has been set up.

### R16: Code has been written to execute fine-tuning jobs through th...
- **Rubric ID**: azure-sft-implementation
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to execute fine-tuning jobs through the Azure OpenAI API.
- **Parent context**: The fine-tuning process has been executed using Azure service.

### R17: The fine-tuning jobs have been executed successfully for all...
- **Rubric ID**: azure-sft-execution
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The fine-tuning jobs have been executed successfully for all tasks.
- **Parent context**: The fine-tuning process has been executed using Azure service.

### R18: The rank parameter $r$ has been set to 128 for the 0.1B adap...
- **Rubric ID**: lora-rank-small
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The rank parameter $r$ has been set to 128 for the 0.1B adapter comparison.
- **Parent context**: The LoRA hyperparameters have been configured correctly.

### R19: The rank parameter $r$ has been set to 384 for the 0.3B adap...
- **Rubric ID**: lora-rank-large
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The rank parameter $r$ has been set to 384 for the 0.3B adapter comparison.
- **Parent context**: The LoRA hyperparameters have been configured correctly.

### R20: The scaling parameter $\alpha$ has been set to $2r$ (256 and...
- **Rubric ID**: lora-alpha
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The scaling parameter $\alpha$ has been set to $2r$ (256 and 768 respectively) for both adapter versions.
- **Parent context**: The LoRA hyperparameters have been configured correctly.

### R21: The learning rate has been set to 2e-4.
- **Rubric ID**: learning-rate
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The learning rate has been set to 2e-4.
- **Parent context**: The training hyperparameters have been configured correctly.

### R22: The weight decay has been set to 0.001.
- **Rubric ID**: weight-decay
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The weight decay has been set to 0.001.
- **Parent context**: The training hyperparameters have been configured correctly.

### R23: The batch size per GPU has been set to 8.
- **Rubric ID**: batch-size
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The batch size per GPU has been set to 8.
- **Parent context**: The training hyperparameters have been configured correctly.

### R24: The remaining parameters have been configured: LoRA dropout...
- **Rubric ID**: other-params
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The remaining parameters have been configured: LoRA dropout is set to 0.1, number of epochs is set to 3, maximum gradient norm is set to 0.3, optimizer is set to Paged AdamW 32bit, and scheduler is set to Cosine.
- **Parent context**: The training hyperparameters have been configured correctly.

### R25: Code has been written to fine-tune Mixtral-8x7B using LoRA a...
- **Rubric ID**: lora-training-implementation
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune Mixtral-8x7B using LoRA adaptation. The hyperparameters used for fine-tuning, listed in Table 8, include a LoRA dropout of 0.1, 3 epochs, a learning rate of 2e-4, weight decay of 0.001, and a batch size of 8 per GPU.
- **Parent context**: The LoRA fine-tuning process has been executed.

### R26: Mixtral-8x7B using LoRA adaptation has been fine-tuned for 3...
- **Rubric ID**: lora-training-execution
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Mixtral-8x7B using LoRA adaptation has been fine-tuned for 3 epochs.
- **Parent context**: The LoRA fine-tuning process has been executed.

### R27: Gradient clipping with max norm 0.3 has been implemented.
- **Rubric ID**: gradient-clipping
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Gradient clipping with max norm 0.3 has been implemented.
- **Parent context**: The LoRA fine-tuning process has been executed.

### R28: The training process for a dedicated 0.1B adapter on the Str...
- **Rubric ID**: strategyqa-small-adapter
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The training process for a dedicated 0.1B adapter on the StrategyQA dataset has been executed.
- **Parent context**: Task-specific 0.1B adapters have been trained separately for each dataset.

### R29: The training process for a dedicated 0.1B adapter on the GSM...
- **Rubric ID**: gsm8k-small-adapter
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The training process for a dedicated 0.1B adapter on the GSM8K dataset has been executed.
- **Parent context**: Task-specific 0.1B adapters have been trained separately for each dataset.

### R30: The training process for a dedicated 0.1B adapter on the Tru...
- **Rubric ID**: truthfulqa-small-adapter
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The training process for a dedicated 0.1B adapter on the TruthfulQA dataset has been executed.
- **Parent context**: Task-specific 0.1B adapters have been trained separately for each dataset.

### R31: The training process for a dedicated 0.1B adapter on the Sci...
- **Rubric ID**: scienceqa-small-adapter
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The training process for a dedicated 0.1B adapter on the ScienceQA dataset has been executed.
- **Parent context**: Task-specific 0.1B adapters have been trained separately for each dataset.

### R32: The training process for a dedicated 0.3B adapter on the Str...
- **Rubric ID**: strategyqa-large-adapter
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The training process for a dedicated 0.3B adapter on the StrategyQA dataset has been executed.
- **Parent context**: Task-specific 0.3B adapters have been trained separately for each dataset.

### R33: The training process for a dedicated 0.3B adapter on the GSM...
- **Rubric ID**: gsm8k-large-adapter
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The training process for a dedicated 0.3B adapter on the GSM8K dataset has been executed.
- **Parent context**: Task-specific 0.3B adapters have been trained separately for each dataset.

### R34: The training process for a dedicated 0.3B adapter on the Tru...
- **Rubric ID**: truthfulqa-large-adapter
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The training process for a dedicated 0.3B adapter on the TruthfulQA dataset has been executed.
- **Parent context**: Task-specific 0.3B adapters have been trained separately for each dataset.

### R35: The training process for a dedicated 0.3B adapter on the Sci...
- **Rubric ID**: scienceqa-large-adapter
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The training process for a dedicated 0.3B adapter on the ScienceQA dataset has been executed.
- **Parent context**: Task-specific 0.3B adapters have been trained separately for each dataset.

### R36: The adapter has been trained using ground truth data.
- **Rubric ID**: gt-adapter-training
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The adapter has been trained using ground truth data.
- **Parent context**: BBox-Adapter (Ground-Truth) has been evaluated.

### R37: The adapter has been trained using AI feedback.
- **Rubric ID**: ai-adapter-training
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The adapter has been trained using AI feedback.
- **Parent context**: BBox-Adapter (AI Feedback) has been evaluated.

### R38: The adapter has been trained using combined feedback.
- **Rubric ID**: combined-adapter-training
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The adapter has been trained using combined feedback.
- **Parent context**: BBox-Adapter (Combined) has been evaluated.

### R39: The model is configured with temperature 1.0 and a maximum l...
- **Rubric ID**: davinci-generation-params
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The model is configured with temperature 1.0 and a maximum length of 512 tokens for generation as specified in Appendix H.2
- **Parent context**: The davinci-002 model has been set up with the OpenAI API for text generation with the following cap...

### R40: The adapter has been configured to run with beam sizes $k$ =...
- **Rubric ID**: beam-configurations
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The adapter has been configured to run with beam sizes $k$ = 1, 3, and 5.
- **Parent context**: The experiments with different beam sizes have been conducted.

### R41: The online adaptation has been configured to run with $T$ =...
- **Rubric ID**: iteration-configurations
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The online adaptation has been configured to run with $T$ = 0, 1, 2, 3, and 4 iterations.
- **Parent context**: The experiments evaluating the impact of different iteration counts have been implemented and run.

### R42: The training and inference has been executed for each iterat...
- **Rubric ID**: iteration-training
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The training and inference has been executed for each iteration configuration.
- **Parent context**: The experiments evaluating the impact of different iteration counts have been implemented and run.

### R43: Mixtral-8x7B has been loaded in half-precision.
- **Rubric ID**: db39284a-0937-4175-a5b0-f69eb677c2c6
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Mixtral-8x7B has been loaded in half-precision.
- **Parent context**: Mixtral-8x7B, Mixtral-8x7B + LoRA and Mixtral-8x7B + BBox-Adapter have been evaluated on the Strateg...

## Method Implementation

### R44: The bert-base-cased (110M) model has been implemented for Tr...
- **Rubric ID**: bert-base-tasks
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The bert-base-cased (110M) model has been implemented for TruthfulQA with the hyperparameters specified in Appendix H.2.
- **Parent context**: The adapter backbone models have been implemented as specified in Appendix H.2.

### R45: The adapter accepts input text pairs (x,y) and processes the...
- **Rubric ID**: adapter-inputs
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The adapter accepts input text pairs (x,y) and processes them through the DeBERTa encoder.
- **Parent context**: The joint model parameterization $p_{\theta}(y|x) = \exp(g_{\theta}(s_{1:L},x))\prod_l p_{LLM}(s_l|x...

### R46: The adapter outputs a scalar score $g_{\theta}(x,y)$ represe...
- **Rubric ID**: adapter-outputs
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The adapter outputs a scalar score $g_{\theta}(x,y)$ representing the energy value for the input pair.
- **Parent context**: The joint model parameterization $p_{\theta}(y|x) = \exp(g_{\theta}(s_{1:L},x))\prod_l p_{LLM}(s_l|x...

### R47: The positive sample terms $-\mathbb{E}_{y^+ \sim p_{data}(y|...
- **Rubric ID**: positive-terms
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The positive sample terms $-\mathbb{E}_{y^+ \sim p_{data}(y|x)}[g_\theta(x,y^+)] + \alpha\mathbb{E}[g_\theta(x,y^+)^2]$ have been implemented.
- **Parent context**: The NCE loss components have been implemented.

### R48: The negative sample terms $\mathbb{E}_{y^- \sim p_\theta(y|x...
- **Rubric ID**: negative-terms
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The negative sample terms $\mathbb{E}_{y^- \sim p_\theta(y|x)}[g_\theta(x,y^-)] + \alpha\mathbb{E}[g_\theta(x,y^-)^2]$ have been implemented.
- **Parent context**: The NCE loss components have been implemented.

### R49: The NCE loss has been implemented according to Equation (3)...
- **Rubric ID**: loss-computation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The NCE loss has been implemented according to Equation (3) in the paper, which includes: $\nabla_{\theta}\ell(\theta) = \nabla_{\theta}\{-\mathbb{E}_{y+\sim p_{data}(y|x)}[g_{\theta}(x,y+)] + \alpha\mathbb{E}[g_{\theta}(x,y+)^2] + \mathbb{E}_{y-\sim p_{\theta}(y|x)}[g_{\theta}(x,y-)] + \alpha\mathbb{E}[g_{\theta}(x,y-)^2]\}$, incorporating both positive and negative sample terms with regularization.
- **Parent context**: The training process components have been implemented.

### R50: The gradient updates $\nabla_{\theta} \mathcal{L}_{NCE}$ hav...
- **Rubric ID**: gradient-updates
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The gradient updates $\nabla_{\theta} \mathcal{L}_{NCE}$ have been implemented with $\eta=5e-6$ as specified in Appendix H.2.
- **Parent context**: The training process components have been implemented.

### R51: Spectral normalization has been applied to the energy model...
- **Rubric ID**: spectral-normalization
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Spectral normalization has been applied to the energy model $g_{\theta}$ to increase gradient stability.
- **Parent context**: The training process components have been implemented.

### R52: The decomposition of complete solution $y$ into sentence-lev...
- **Rubric ID**: sequence-decomposition
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The decomposition of complete solution $y$ into sentence-level sequences $[s_1, s_2, ..., s_L]$ has been implemented.
- **Parent context**: The sentence-level factorization of the adapted inference process has been implemented.

### R53: The autoregressive scoring of sequences using both LLM proba...
- **Rubric ID**: autoregressive-scoring
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The autoregressive scoring of sequences using both LLM probabilities and adapter scores has been implemented.
- **Parent context**: The sentence-level factorization of the adapted inference process has been implemented.

### R54: The generation of $M$ samples per beam at each step $l$ base...
- **Rubric ID**: candidate-generation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The generation of $M$ samples per beam at each step $l$ based on $p_{LLM}(s_l|x,s_{1:l-1})$ has been implemented.
- **Parent context**: The beam management system for tracking and updating candidate solutions has been implemented.

### R55: The scoring of $nk$ candidate chains using the adapter $g_\t...
- **Rubric ID**: beam-scoring
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The scoring of $nk$ candidate chains using the adapter $g_\theta(s_{1:l},x)$ has been implemented.
- **Parent context**: The beam management system for tracking and updating candidate solutions has been implemented.

### R56: The selection of top-k beams based on adapter scores has bee...
- **Rubric ID**: beam-pruning
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The selection of top-k beams based on adapter scores has been implemented.
- **Parent context**: The beam management system for tracking and updating candidate solutions has been implemented.

### R57: The checking for either reaching $L$ iterations or encounter...
- **Rubric ID**: termination-check
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The checking for either reaching $L$ iterations or encountering stop signals has been implemented.
- **Parent context**: The stopping criteria and final selection process have been implemented.

### R58: The selection of the highest-scoring complete solution from...
- **Rubric ID**: final-selection
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The selection of the highest-scoring complete solution from the $k$ final candidates has been implemented.
- **Parent context**: The stopping criteria and final selection process have been implemented.

### R59: The base model generates a set of complete answers in a sing...
- **Rubric ID**: single-step-generation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The base model generates a set of complete answers in a single step.
- **Parent context**: The single-step adapter variant has been implemented.

### R60: The adapter selects the best answer from the candidates as t...
- **Rubric ID**: single-step-selection
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The adapter selects the best answer from the candidates as the final response.
- **Parent context**: The single-step adapter variant has been implemented.

### R61: The base model generates multiple solution paths using beam...
- **Rubric ID**: full-step-generation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The base model generates multiple solution paths using beam search.
- **Parent context**: The full-step adapter variant with beam search has been implemented.

### R62: The adapter scores and selects the top-$k$ paths at each ste...
- **Rubric ID**: full-step-selection
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The adapter scores and selects the top-$k$ paths at each step, maintaining a beam size of $k=3$ by default as specified in the paper.
- **Parent context**: The full-step adapter variant with beam search has been implemented.

### R63: Code has been written to properly format and send prompts to...
- **Rubric ID**: prompt-handling
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to properly format and send prompts to the LLM API.
- **Parent context**: The LLM can generate text completions given input prompts.

### R64: Code has been written to parse completion responses from the...
- **Rubric ID**: completion-handling
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to parse completion responses from the LLM API.
- **Parent context**: The LLM can generate text completions given input prompts.

### R65: Code has been written such that the LLM can generate candida...
- **Rubric ID**: proposal-generation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written such that the LLM can generate candidate proposals for the adapter to score.
- **Parent context**: The LLM outputs can be used as proposals in the adapter framework.

### R66: Code has been written such that the LLM is treated as a blac...
- **Rubric ID**: black-box-usage
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written such that the LLM is treated as a black box without accessing internal parameters or probabilities.
- **Parent context**: The LLM outputs can be used as proposals in the adapter framework.

### R67: Random initialization of adapter parameters $\theta_0$ has b...
- **Rubric ID**: random-init
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Random initialization of adapter parameters $\theta_0$ has been implemented.
- **Parent context**: The initialization steps of Algorithm 1 have been implemented.

### R68: Initial sampling of $K$ responses for each input query has b...
- **Rubric ID**: initial-sampling
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Initial sampling of $K$ responses for each input query has been implemented: ${y_{i,j}}^K_{j=1} \sim p_{LLM}(y|x_i)$.
- **Parent context**: The initialization steps of Algorithm 1 have been implemented.

### R69: When ground truth data is available, positive samples are ta...
- **Rubric ID**: ground-truth-selection
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When ground truth data is available, positive samples are taken from ground truth solutions while negative samples are generated using an adapter with random parameters.
- **Parent context**: Initial positive/negative sample selection has been implemented with the appropriate method based on...

### R70: When ground truth data is unavailable, positive samples are...
- **Rubric ID**: ai-feedback-selection
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When ground truth data is unavailable, positive samples are selected based on AI feedback (using GPT-4) from generated candidates, while remaining candidates serve as negative samples.
- **Parent context**: Initial positive/negative sample selection has been implemented with the appropriate method based on...

### R71: Sampling $M$ candidates from adapted inference has been impl...
- **Rubric ID**: eq4-implementation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Sampling $M$ candidates from adapted inference has been implemented as described in Equation 4 i.e., ${\hat{y}_{i,m}}^M_{m=1} \sim p_{\theta_t}(y|x_i)$
- **Parent context**: The main adaptation loop from Algorithm 1 has been implemented.

### R72: The update of positive samples has been implemented as descr...
- **Rubric ID**: eq5-implementation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The update of positive samples has been implemented as described in Equation 5 i.e., $y^{(t)}_{i+} = \text{SEL}(y^{(t-1)}_{i+}, {\hat{y}_{i,m}}^M_{m=1})$
- **Parent context**: The main adaptation loop from Algorithm 1 has been implemented.

### R73: The update of negative samples has been implemented as descr...
- **Rubric ID**: eq6-implementation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The update of negative samples has been implemented as described in Equation 6 i.e., $y^{(t)}_{i-} = {\hat{y}_{i,m} | \hat{y}_{i,m} \neq y^{(t)}_{i+}}^M_{m=1}$
- **Parent context**: The main adaptation loop from Algorithm 1 has been implemented.

### R74: The computation of the loss gradient has been implemented as...
- **Rubric ID**: eq3-implementation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The computation of the loss gradient has been implemented as described in Equation 3 i.e., $\nabla_\theta \ell(\theta_t)$ using $y^{(t)}_{i+}$ and $y^{(t)}_{i-}$
- **Parent context**: The main adaptation loop from Algorithm 1 has been implemented.

### R75: The parameter update has been implemented as described in Eq...
- **Rubric ID**: eq7-implementation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The parameter update has been implemented as described in Equation 7 i.e., $\theta_{t+1} = \theta_t - \eta \nabla_\theta \ell(\theta_t)$
- **Parent context**: The main adaptation loop from Algorithm 1 has been implemented.

### R76: The final layer has been modified to a classification head w...
- **Rubric ID**: classification-head
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The final layer has been modified to a classification head with an output dimension of 1 to ensure the adapter outputs a scalar score value.
- **Parent context**: The deberta-v3-base model has been properly loaded and configured.

### R77: The final layer has been modified to a classification head w...
- **Rubric ID**: classification-head-large
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The final layer has been modified to a classification head with an output dimension of 1 to ensure the adapter outputs a scalar score value.
- **Parent context**: The deberta-v3-large model has been properly loaded and configured.

### R78: The final layer has been modified to a classification head w...
- **Rubric ID**: classification-head-bert
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The final layer has been modified to a classification head with an output dimension of 1 to ensure the adapter outputs a scalar score value.
- **Parent context**: The bert-base-cased model has been properly loaded and configured.

### R79: The two-shot prompt for StrategyQA has been implemented as s...
- **Rubric ID**: ab87b0ff-7caf-4678-89f5-8341600cebe9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The two-shot prompt for StrategyQA has been implemented as specified in Appendix J.
- **Parent context**: The Chain-of-Thought using GPT-3.5 Turbo baseline has been implemented.

### R80: The four-shot prompt from Chain-of-Thought Hub has been impl...
- **Rubric ID**: d865c8bb-b7e2-4908-94cf-d1f854319112
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The four-shot prompt from Chain-of-Thought Hub has been implemented for GSM8K, as specified in Appendix J.
- **Parent context**: The Chain-of-Thought using GPT-3.5 Turbo baseline has been implemented.

### R81: The one-shot prompt for ScienceQA has been implemented as sp...
- **Rubric ID**: 86dd3099-e471-46fc-bd98-b49e899ba498
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The one-shot prompt for ScienceQA has been implemented as specified in Appendix J.
- **Parent context**: The Chain-of-Thought using GPT-3.5 Turbo baseline has been implemented.

### R82: The training pipeline using masked word supervision has been...
- **Rubric ID**: mlm-training
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The training pipeline using masked word supervision has been implemented.
- **Parent context**: The MLM baseline has been implemented.

### R83: The inference process using masked word probability scoring...
- **Rubric ID**: mlm-inference
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The inference process using masked word probability scoring has been implemented.
- **Parent context**: The MLM baseline has been implemented.

## Dataset and Model Acquisition

### R84: Code has been written to download the GSM8K questions and st...
- **Rubric ID**: gsm8k-download-code
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been written to download the GSM8K questions and step-by-step solutions.
- **Parent context**: The GSM8K dataset has been downloaded and split into train and test splits, as described in Appendix...

### R85: The GSM8K questions and step-by-step solutions have been dow...
- **Rubric ID**: gsm8k-download-exec
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The GSM8K questions and step-by-step solutions have been downloaded.
- **Parent context**: The GSM8K dataset has been downloaded and split into train and test splits, as described in Appendix...

### R86: Code has been written to download the StrategyQA questions a...
- **Rubric ID**: strategyqa-download-code
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been written to download the StrategyQA questions and reasoning steps.
- **Parent context**: The StrategyQA dataset has been downloaded and split into train and test splits, as described in App...

### R87: The StrategyQA questions and reasoning steps have been downl...
- **Rubric ID**: strategyqa-download-exec
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The StrategyQA questions and reasoning steps have been downloaded.
- **Parent context**: The StrategyQA dataset has been downloaded and split into train and test splits, as described in App...

### R88: Code has been written to download the TruthfulQA questions.
- **Rubric ID**: truthfulqa-download-code
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been written to download the TruthfulQA questions.
- **Parent context**: The TruthfulQA dataset has been downloaded and split into train and test splits, as described in App...

### R89: The TruthfulQA questions have been downloaded.
- **Rubric ID**: truthfulqa-download-exec
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The TruthfulQA questions have been downloaded.
- **Parent context**: The TruthfulQA dataset has been downloaded and split into train and test splits, as described in App...

### R90: Code has been written to download the non-image ScienceQA qu...
- **Rubric ID**: scienceqa-download-code
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been written to download the non-image ScienceQA questions.
- **Parent context**: The ScienceQA dataset has been downloaded and split into train and test splits, as described in Appe...

### R91: The non-image ScienceQA questions have been downloaded.
- **Rubric ID**: scienceqa-download-exec
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The non-image ScienceQA questions have been downloaded.
- **Parent context**: The ScienceQA dataset has been downloaded and split into train and test splits, as described in Appe...

### R92: The mixtral-8x7B-v0.1 model has been loaded from HuggingFace...
- **Rubric ID**: mixtral-model-loading
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The mixtral-8x7B-v0.1 model has been loaded from HuggingFace in half-precision.
- **Parent context**: The Mixtral-8x7B model has been set up for evaluation with correct configurations.

### R93: Code has been written to load and initialize the deberta-v3-...
- **Rubric ID**: model-loading
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been written to load and initialize the deberta-v3-base model (86M) with correct model weights.
- **Parent context**: The deberta-v3-base model has been properly loaded and configured.

### R94: Code has been written to load and initialize the deberta-v3-...
- **Rubric ID**: model-loading-large
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been written to load and initialize the deberta-v3-large model (304M) with correct model weights.
- **Parent context**: The deberta-v3-large model has been properly loaded and configured.

### R95: Code has been written to load the weights of the bert-base-c...
- **Rubric ID**: model-loading-bert
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been written to load the weights of the bert-base-cased (110M) model.
- **Parent context**: The bert-base-cased model has been properly loaded and configured.

## Data Processing & Preparation

### R96: Code has been written to split the GSM8K dataset into 7473 t...
- **Rubric ID**: gsm8k-split-code
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to split the GSM8K dataset into 7473 training and 1319 test samples.
- **Parent context**: The GSM8K dataset has been downloaded and split into train and test splits, as described in Appendix...

### R97: The GSM8K dataset has been split into 7473 training and 1319...
- **Rubric ID**: gsm8k-split-exec
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The GSM8K dataset has been split into 7473 training and 1319 test samples.
- **Parent context**: The GSM8K dataset has been downloaded and split into train and test splits, as described in Appendix...

### R98: Code has been written to split the StrategyQA dataset into 2...
- **Rubric ID**: strategyqa-split-code
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to split the StrategyQA dataset into 2059 training and 229 test samples.
- **Parent context**: The StrategyQA dataset has been downloaded and split into train and test splits, as described in App...

### R99: The StrategyQA dataset has been split into 2059 training and...
- **Rubric ID**: strategyqa-split-exec
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The StrategyQA dataset has been split into 2059 training and 229 test samples.
- **Parent context**: The StrategyQA dataset has been downloaded and split into train and test splits, as described in App...

### R100: Code has been written to randomly sample 100 questions for t...
- **Rubric ID**: truthfulqa-split-code
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to randomly sample 100 questions for the test set and use the remaining 717 samples for training.
- **Parent context**: The TruthfulQA dataset has been downloaded and split into train and test splits, as described in App...

### R101: The TruthfulQA dataset has been split into 717 training and...
- **Rubric ID**: truthfulqa-split-exec
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The TruthfulQA dataset has been split into 717 training and 100 test samples.
- **Parent context**: The TruthfulQA dataset has been downloaded and split into train and test splits, as described in App...

### R102: Code has been written to randomly select 2000 questions for...
- **Rubric ID**: scienceqa-split-code
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to randomly select 2000 questions for training and 500 for testing from the original splits.
- **Parent context**: The ScienceQA dataset has been downloaded and split into train and test splits, as described in Appe...

### R103: The ScienceQA dataset has been split into 2000 training and...
- **Rubric ID**: scienceqa-split-exec
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The ScienceQA dataset has been split into 2000 training and 500 test samples.
- **Parent context**: The ScienceQA dataset has been downloaded and split into train and test splits, as described in Appe...

### R104: The training data has been formatted according to Azure fine...
- **Rubric ID**: data-formatting
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The training data has been formatted according to Azure fine-tuning API requirements.
- **Parent context**: The Azure OpenAI fine-tuning service has been set up.

## Environment & Infrastructure Setup

### R105: API access has been set up for text generation using GPT-3.5...
- **Rubric ID**: azure-api-setup
- **Category**: Code Development / Environment & Infrastructure Setup
- **Weight**: 1
- **Requirement**: API access has been set up for text generation using GPT-3.5 Turbo, supporting the following features: (1) prompt-based text generation, (2) adjustable sampling temperature, and (3) control over maximum output length.
- **Parent context**: The GPT-3.5 Turbo model has been set up for evaluation with the correct configurations.

### R106: API access has been configured to enable text generation usi...
- **Rubric ID**: davinci-api-setup
- **Category**: Code Development / Environment & Infrastructure Setup
- **Weight**: 1
- **Requirement**: API access has been configured to enable text generation using davinci-002
- **Parent context**: The davinci-002 model has been set up with the OpenAI API for text generation with the following cap...

## Evaluation, Metrics & Benchmarking

### R107: Code has been written to query the model on TruthfulQA sampl...
- **Rubric ID**: bert-inference-check
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to query the model on TruthfulQA samples.
- **Parent context**: The bert-base-cased model has been set up to be evaluated on TruthfulQA.

### R108: The Chain-of-Thought baseline has been evaluated on the test...
- **Rubric ID**: cot-execution
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Chain-of-Thought baseline has been evaluated on the test splits of all datasets using GPT-3.5 Turbo.
- **Parent context**: The GPT-3.5 Turbo with Chain-of-Thought baseline has been evaluated.

### R109: The accuracy of the base GPT-3.5 Turbo model on the Strategy...
- **Rubric ID**: cot-strategyqa-accuracy
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy of the base GPT-3.5 Turbo model on the StrategyQA dataset has been calculated.
- **Parent context**: The metrics for the base GPT-3.5 Turbo model have been calculated on all datasets (StrategyQA, GSM, ...

### R110: The accuracy of the base GPT-3.5 Turbo model on the GSM8K da...
- **Rubric ID**: cot-gsm8k-accuracy
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy of the base GPT-3.5 Turbo model on the GSM8K dataset has been calculated.
- **Parent context**: The metrics for the base GPT-3.5 Turbo model have been calculated on all datasets (StrategyQA, GSM, ...

### R111: The True+Info metric of the base GPT-3.5 Turbo model on the...
- **Rubric ID**: cot-truthfulqa-accuracy
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The True+Info metric of the base GPT-3.5 Turbo model on the TruthfulQA dataset has been calculated.
- **Parent context**: The metrics for the base GPT-3.5 Turbo model have been calculated on all datasets (StrategyQA, GSM, ...

### R112: The accuracy of the base GPT-3.5 Turbo model on the ScienceQ...
- **Rubric ID**: cot-scienceqa-accuracy
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy of the base GPT-3.5 Turbo model on the ScienceQA dataset has been calculated.
- **Parent context**: The metrics for the base GPT-3.5 Turbo model have been calculated on all datasets (StrategyQA, GSM, ...

### R113: The Azure-SFT fine-tuned model has been evaluated on the Str...
- **Rubric ID**: 2c90777a-b539-4e37-8108-b7a62a741a9e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Azure-SFT fine-tuned model has been evaluated on the StrategyQA test split.
- **Parent context**: The Azure-SFT fine-tuned model has been evaluated on the test splits of all datasets.

### R114: The Azure-SFT fine-tuned model has been evaluated on the GSM...
- **Rubric ID**: c6f6c8d9-e975-4cad-91df-08df536f0d0a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Azure-SFT fine-tuned model has been evaluated on the GSM8K test split.
- **Parent context**: The Azure-SFT fine-tuned model has been evaluated on the test splits of all datasets.

### R115: The Azure-SFT fine-tuned model has been evaluated on the Tru...
- **Rubric ID**: 9a21233a-43e3-4bee-ae5f-11cea32568f6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Azure-SFT fine-tuned model has been evaluated on the TruthfulQA test split.
- **Parent context**: The Azure-SFT fine-tuned model has been evaluated on the test splits of all datasets.

### R116: The Azure-SFT fine-tuned model has been evaluated on the Sci...
- **Rubric ID**: 02f77608-6c71-4e6a-aeb3-82f7017eaf00
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Azure-SFT fine-tuned model has been evaluated on the ScienceQA test split.
- **Parent context**: The Azure-SFT fine-tuned model has been evaluated on the test splits of all datasets.

### R117: The accuracy metrics for Azure-SFT and base model have been...
- **Rubric ID**: sft-strategyqa-calculation
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy metrics for Azure-SFT and base model have been calculated on StrategyQA dataset.
- **Parent context**: The metrics for Azure-SFT and base model have been calculated on all datasets (StrategyQA, GSM8K, Tr...

### R118: The accuracy metrics for Azure-SFT and base model have been...
- **Rubric ID**: sft-gsm8k-calculation
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy metrics for Azure-SFT and base model have been calculated on GSM8K dataset.
- **Parent context**: The metrics for Azure-SFT and base model have been calculated on all datasets (StrategyQA, GSM8K, Tr...

### R119: The True + Info metrics for Azure-SFT and base model have be...
- **Rubric ID**: sft-truthfulqa-calculation
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The True + Info metrics for Azure-SFT and base model have been calculated on TruthfulQA dataset.
- **Parent context**: The metrics for Azure-SFT and base model have been calculated on all datasets (StrategyQA, GSM8K, Tr...

### R120: The accuracy metrics for Azure-SFT and base model have been...
- **Rubric ID**: sft-scienceqa-calculation
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy metrics for Azure-SFT and base model have been calculated on ScienceQA dataset.
- **Parent context**: The metrics for Azure-SFT and base model have been calculated on all datasets (StrategyQA, GSM8K, Tr...

### R121: Code has been written to compare adapter sizes and select th...
- **Rubric ID**: performance-comparison-code
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compare adapter sizes and select the best performer.
- **Parent context**: The best performing adapter size has been selected for each dataset based on validation performance.

### R122: The performance comparison has been run and best performers...
- **Rubric ID**: performance-comparison-exec
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The performance comparison has been run and best performers selected.
- **Parent context**: The best performing adapter size has been selected for each dataset based on validation performance.

### R123: The ground truth adapter has been evaluated on the test spli...
- **Rubric ID**: gt-evaluation
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The ground truth adapter has been evaluated on the test splits of all datasets.
- **Parent context**: BBox-Adapter (Ground-Truth) has been evaluated.

### R124: The accuracy has been computed for StrategyQA.
- **Rubric ID**: gt-acc-sqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy has been computed for StrategyQA.
- **Parent context**: The performance metrics have been computed for StrategyQA, GSM8K, ScienceQA, and TruthfulQA.

### R125: The accuracy has been computed for GSM8K.
- **Rubric ID**: gt-acc-gsm8k
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy has been computed for GSM8K.
- **Parent context**: The performance metrics have been computed for StrategyQA, GSM8K, ScienceQA, and TruthfulQA.

### R126: The accuracy has been computed for ScienceQA.
- **Rubric ID**: gt-acc-scienceqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy has been computed for ScienceQA.
- **Parent context**: The performance metrics have been computed for StrategyQA, GSM8K, ScienceQA, and TruthfulQA.

### R127: The True+Info metric has been computed for TruthfulQA.
- **Rubric ID**: gt-acc-truthfulqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The True+Info metric has been computed for TruthfulQA.
- **Parent context**: The performance metrics have been computed for StrategyQA, GSM8K, ScienceQA, and TruthfulQA.

### R128: The AI feedback adapter has been evaluated on the test split...
- **Rubric ID**: ai-evaluation
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The AI feedback adapter has been evaluated on the test splits of all datasets.
- **Parent context**: BBox-Adapter (AI Feedback) has been evaluated.

### R129: The accuracy has been computed for StrategyQA.
- **Rubric ID**: gt-acc-strategyqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy has been computed for StrategyQA.
- **Parent context**: The metrics have been computed for StrategyQA, GSM8K, TruthfulQA, and ScienceQA.

### R130: The accuracy has been computed for GSM8K.
- **Rubric ID**: gt-acc-gsm8k
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy has been computed for GSM8K.
- **Parent context**: The metrics have been computed for StrategyQA, GSM8K, TruthfulQA, and ScienceQA.

### R131: The True+Info metric has been computed for TruthfulQA.
- **Rubric ID**: gt-acc-truthfulqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The True+Info metric has been computed for TruthfulQA.
- **Parent context**: The metrics have been computed for StrategyQA, GSM8K, TruthfulQA, and ScienceQA.

### R132: The accuracy has been computed for ScienceQA.
- **Rubric ID**: gt-acc-scienceqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy has been computed for ScienceQA.
- **Parent context**: The metrics have been computed for StrategyQA, GSM8K, TruthfulQA, and ScienceQA.

### R133: The combined feedback adapter has been evaluated on the test...
- **Rubric ID**: combined-evaluation
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The combined feedback adapter has been evaluated on the test splits of all datasets.
- **Parent context**: BBox-Adapter (Combined) has been evaluated.

### R134: The True+Info metric has been computed for StrategyQA.
- **Rubric ID**: combined-strategyqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The True+Info metric has been computed for StrategyQA.
- **Parent context**: The performance metrics have been computed for StrategyQA, TruthfulQA, GSM8K, and ScienceQA.

### R135: The True+Info metric has been computed for TruthfulQA.
- **Rubric ID**: combined-truthfulqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The True+Info metric has been computed for TruthfulQA.
- **Parent context**: The performance metrics have been computed for StrategyQA, TruthfulQA, GSM8K, and ScienceQA.

### R136: The True+Info metric has been computed for GSM8K.
- **Rubric ID**: combined-gsm8k
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The True+Info metric has been computed for GSM8K.
- **Parent context**: The performance metrics have been computed for StrategyQA, TruthfulQA, GSM8K, and ScienceQA.

### R137: The True+Info metric has been computed for ScienceQA.
- **Rubric ID**: combined-scienceqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The True+Info metric has been computed for ScienceQA.
- **Parent context**: The performance metrics have been computed for StrategyQA, TruthfulQA, GSM8K, and ScienceQA.

### R138: The baseline model achieves an accuracy of ~66.59% on Strate...
- **Rubric ID**: baseline-strategyqa
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline model achieves an accuracy of ~66.59% on StrategyQA.
- **Parent context**: The baseline performance matches the performance reported in Table 2.

### R139: The baseline model achieves an accuracy of ~67.51% on GSM8K.
- **Rubric ID**: baseline-gsm8k
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline model achieves an accuracy of ~67.51% on GSM8K.
- **Parent context**: The baseline performance matches the performance reported in Table 2.

### R140: The baseline model achieves an accuracy of ~72.90% on Scienc...
- **Rubric ID**: baseline-truthfulqa
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline model achieves an accuracy of ~72.90% on ScienceQA.
- **Parent context**: The baseline performance matches the performance reported in Table 2.

### R141: The baseline model achieves a True + Info score of ~77.00% o...
- **Rubric ID**: baseline-scienceqa
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline model achieves a True + Info score of ~77.00% on TruthfulQA.
- **Parent context**: The baseline performance matches the performance reported in Table 2.

### R142: The Azure-SFT model achieves an improvement of ~10.27% over...
- **Rubric ID**: sft-strategyqa-gain
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Azure-SFT model achieves an improvement of ~10.27% over the baseline model on StrategyQA.
- **Parent context**: The Azure-SFT improvements match those reported in Table 2.

### R143: The Azure-SFT model achieves an improvement of ~2.43% over t...
- **Rubric ID**: sft-gsm8k-gain
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Azure-SFT model achieves an improvement of ~2.43% over the baseline model on GSM8K.
- **Parent context**: The Azure-SFT improvements match those reported in Table 2.

### R144: The Azure-SFT model achieves an improvement of ~6.10% over t...
- **Rubric ID**: sft-truthfulqa-gain
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Azure-SFT model achieves an improvement of ~6.10% over the baseline model on ScienceQA.
- **Parent context**: The Azure-SFT improvements match those reported in Table 2.

### R145: The Azure-SFT model achieves an improvement of ~18.00% over...
- **Rubric ID**: sft-scienceqa-gain
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Azure-SFT model achieves an improvement of ~18.00% over the baseline model on TruthfulQA.
- **Parent context**: The Azure-SFT improvements match those reported in Table 2.

### R146: The Ground-Truth adapter achieves an improvement of ~5.03% o...
- **Rubric ID**: gt-strategyqa-gain
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Ground-Truth adapter achieves an improvement of ~5.03% on StrategyQA.
- **Parent context**: The Ground-Truth adapter improvements match those reported in Table 2.

### R147: The Ground-Truth adapter achieves an improvement of ~6.35% o...
- **Rubric ID**: gt-gsm8k-gain
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Ground-Truth adapter achieves an improvement of ~6.35% on GSM8K.
- **Parent context**: The Ground-Truth adapter improvements match those reported in Table 2.

### R148: The Ground-Truth adapter achieves an improvement of ~2.70% o...
- **Rubric ID**: gt-truthfulqa-gain
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Ground-Truth adapter achieves an improvement of ~2.70% on TruthfulQA.
- **Parent context**: The Ground-Truth adapter improvements match those reported in Table 2.

### R149: The Ground-Truth adapter achieves an improvement of ~5.63% o...
- **Rubric ID**: gt-scienceqa-gain
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Ground-Truth adapter achieves an improvement of ~5.63% on ScienceQA.
- **Parent context**: The Ground-Truth adapter improvements match those reported in Table 2.

### R150: The AI feedback adapter achieves an improvement of ~3.26% on...
- **Rubric ID**: ai-feedback-strategyqa-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The AI feedback adapter achieves an improvement of ~3.26% on StrategyQA.
- **Parent context**: The performance improvements for AI feedback match those reported in Table 2.

### R151: The AI feedback adapter achieves an improvement of ~5.99% on...
- **Rubric ID**: ai-feedback-gsm8k-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The AI feedback adapter achieves an improvement of ~5.99% on GSM8K.
- **Parent context**: The performance improvements for AI feedback match those reported in Table 2.

### R152: The AI feedback adapter achieves an improvement of ~5.40% on...
- **Rubric ID**: ai-feedback-scienceqa-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The AI feedback adapter achieves an improvement of ~5.40% on ScienceQA.
- **Parent context**: The performance improvements for AI feedback match those reported in Table 2.

### R153: The AI feedback adapter achieves an improvement of ~5.10% on...
- **Rubric ID**: ai-feedback-truthfulqa-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The AI feedback adapter achieves an improvement of ~5.10% on TruthfulQA.
- **Parent context**: The performance improvements for AI feedback match those reported in Table 2.

### R154: The Combined adapter achieves an improvement of ~5.68% on St...
- **Rubric ID**: combined-strategyqa-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Combined adapter achieves an improvement of ~5.68% on StrategyQA.
- **Parent context**: The performance improvements for combined feedback match those reported in Table 2.

### R155: The Combined adapter achieves an improvement of ~6.77% on GS...
- **Rubric ID**: combined-gsm8k-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Combined adapter achieves an improvement of ~6.77% on GSM8K.
- **Parent context**: The performance improvements for combined feedback match those reported in Table 2.

### R156: The Combined adapter achieves an improvement of ~6.50% on Sc...
- **Rubric ID**: combined-scienceqa-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Combined adapter achieves an improvement of ~6.50% on ScienceQA.
- **Parent context**: The performance improvements for combined feedback match those reported in Table 2.

### R157: The Combined adapter achieves an improvement of ~6.60% on Tr...
- **Rubric ID**: combined-truthfulqa-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Combined adapter achieves an improvement of ~6.60% on TruthfulQA.
- **Parent context**: The performance improvements for combined feedback match those reported in Table 2.

### R158: The accuracy of base davinci-002 on StrategyQA has been calc...
- **Rubric ID**: base-davinci-strategyqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy of base davinci-002 on StrategyQA has been calculated.
- **Parent context**: The performance metrics for base davinci-002 have been calculated.

### R159: The accuracy of base davinci-002 on GSM8K has been calculate...
- **Rubric ID**: base-davinci-gsm8k
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy of base davinci-002 on GSM8K has been calculated.
- **Parent context**: The performance metrics for base davinci-002 have been calculated.

### R160: The True+Info metric of base davinci-002 on TruthfulQA has b...
- **Rubric ID**: base-davinci-truthfulqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The True+Info metric of base davinci-002 on TruthfulQA has been calculated.
- **Parent context**: The performance metrics for base davinci-002 have been calculated.

### R161: The accuracy of adapted davinci-002 on StrategyQA has been c...
- **Rubric ID**: adapted-davinci-strategyqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy of adapted davinci-002 on StrategyQA has been calculated.
- **Parent context**: The performance metrics for adapted davinci-002 have been calculated.

### R162: The accuracy of adapted davinci-002 on GSM8K has been calcul...
- **Rubric ID**: adapted-davinci-gsm8k
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy of adapted davinci-002 on GSM8K has been calculated.
- **Parent context**: The performance metrics for adapted davinci-002 have been calculated.

### R163: The True+Info metric of adapted davinci-002 on TruthfulQA ha...
- **Rubric ID**: adapted-davinci-truthfulqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The True+Info metric of adapted davinci-002 on TruthfulQA has been calculated.
- **Parent context**: The performance metrics for adapted davinci-002 have been calculated.

### R164: The adapted davinci-002 achieves an improvement of ~15.42% o...
- **Rubric ID**: davinci-strategyqa-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The adapted davinci-002 achieves an improvement of ~15.42% on StrategyQA.
- **Parent context**: The performance improvements of adapted davinci-002 over base davinci-002 match those reported in Ta...

### R165: The adapted davinci-002 achieves an improvement of ~0.12% on...
- **Rubric ID**: davinci-gsm8k-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The adapted davinci-002 achieves an improvement of ~0.12% on GSM8K.
- **Parent context**: The performance improvements of adapted davinci-002 over base davinci-002 match those reported in Ta...

### R166: The adapted davinci-002 achieves an improvement of ~5.00% on...
- **Rubric ID**: davinci-truthfulqa-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The adapted davinci-002 achieves an improvement of ~5.00% on TruthfulQA.
- **Parent context**: The performance improvements of adapted davinci-002 over base davinci-002 match those reported in Ta...

### R167: The adapted davinci-002 achieves an average improvement of ~...
- **Rubric ID**: davinci-average-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The adapted davinci-002 achieves an average improvement of ~6.85% across all datasets.
- **Parent context**: The performance improvements of adapted davinci-002 over base davinci-002 match those reported in Ta...

### R168: Mixtral-8x7B has been evaluated on the StrategyQA test set,...
- **Rubric ID**: baseline-inference-mixtral
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B has been evaluated on the StrategyQA test set, with the accuracy computed and saved.
- **Parent context**: The baseline evaluation of Mixtral-8x7B has been conducted.

### R169: The baseline performance metrics have been calculated.
- **Rubric ID**: baseline-metrics
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline performance metrics have been calculated.
- **Parent context**: The baseline evaluation of Mixtral-8x7B has been conducted.

### R170: The inference with the adapted Mixtral-8x7B has been execute...
- **Rubric ID**: adapted-inference-mixtral
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The inference with the adapted Mixtral-8x7B has been executed.
- **Parent context**: The plug-and-play evaluation using the GPT-3.5 Turbo trained adapter has been conducted on Mixtral-8...

### R171: The accuracy of base Mixtral-8x7B on StrategyQA has been cal...
- **Rubric ID**: base-mixtral-strategyqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy of base Mixtral-8x7B on StrategyQA has been calculated.
- **Parent context**: Performance metrics for the base Mixtral-8x7B model have been calculated.

### R172: The accuracy of base Mixtral-8x7B on GSM8K has been calculat...
- **Rubric ID**: base-mixtral-gsm8k
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy of base Mixtral-8x7B on GSM8K has been calculated.
- **Parent context**: Performance metrics for the base Mixtral-8x7B model have been calculated.

### R173: The True+Info metric of base Mixtral-8x7B on TruthfulQA has...
- **Rubric ID**: base-mixtral-truthfulqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The True+Info metric of base Mixtral-8x7B on TruthfulQA has been calculated.
- **Parent context**: Performance metrics for the base Mixtral-8x7B model have been calculated.

### R174: The accuracy of adapted Mixtral-8x7B on StrategyQA has been...
- **Rubric ID**: adapted-mixtral-strategyqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy of adapted Mixtral-8x7B on StrategyQA has been calculated.
- **Parent context**: Performance metrics for the adapted Mixtral-8x7B model have been calculated.

### R175: The accuracy of adapted Mixtral-8x7B on GSM8K has been calcu...
- **Rubric ID**: adapted-mixtral-gsm8k
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy of adapted Mixtral-8x7B on GSM8K has been calculated.
- **Parent context**: Performance metrics for the adapted Mixtral-8x7B model have been calculated.

### R176: The True+Info metric of adapted Mixtral-8x7B on TruthfulQA h...
- **Rubric ID**: adapted-mixtral-truthfulqa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The True+Info metric of adapted Mixtral-8x7B on TruthfulQA has been calculated.
- **Parent context**: Performance metrics for the adapted Mixtral-8x7B model have been calculated.

### R177: The adapted Mixtral-8x7B achieves an improvement of ~4.06% o...
- **Rubric ID**: mixtral-strategyqa-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The adapted Mixtral-8x7B achieves an improvement of ~4.06% on StrategyQA.
- **Parent context**: The performance improvements over base Mixtral-8x7B match those reported in Table 3.

### R178: The adapted Mixtral-8x7B achieves an improvement of ~0.15% o...
- **Rubric ID**: mixtral-gsm8k-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The adapted Mixtral-8x7B achieves an improvement of ~0.15% on GSM8K.
- **Parent context**: The performance improvements over base Mixtral-8x7B match those reported in Table 3.

### R179: The adapted Mixtral-8x7B achieves an improvement of ~9.30% o...
- **Rubric ID**: mixtral-truthfulqa-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The adapted Mixtral-8x7B achieves an improvement of ~9.30% on TruthfulQA.
- **Parent context**: The performance improvements over base Mixtral-8x7B match those reported in Table 3.

### R180: The adapted Mixtral-8x7B achieves an average improvement of...
- **Rubric ID**: mixtral-average-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The adapted Mixtral-8x7B achieves an average improvement of ~4.50% across all datasets.
- **Parent context**: The performance improvements over base Mixtral-8x7B match those reported in Table 3.

### R181: The inference has been executed for each beam size configura...
- **Rubric ID**: beam-inference
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The inference has been executed for each beam size configuration.
- **Parent context**: The experiments with different beam sizes have been conducted.

### R182: The performance changes across beam sizes ($k$ = 1, 3, 5) ha...
- **Rubric ID**: performance-tracking-beam
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The performance changes across beam sizes ($k$ = 1, 3, 5) have been tracked and calculated.
- **Parent context**: The results evaluating the impact of beam size match those reported in Figure 3(a).

### R183: The results show that increasing the number of beams contrib...
- **Rubric ID**: beam-size-trends
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The results show that increasing the number of beams contributes to an average performance enhancement of ~2.41% across different adapter sizes (0.1B and 0.3B).
- **Parent context**: The results evaluating the impact of beam size match those reported in Figure 3(a).

### R184: Code has been written to compute and save the performance ch...
- **Rubric ID**: performance-tracking-129838129
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the performance changes across iteration counts.
- **Parent context**: The experiments evaluating the impact of different iteration counts have been implemented and run.

### R185: The performance changes across iteration counts have been co...
- **Rubric ID**: performance-tracking
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The performance changes across iteration counts have been computed and saved.
- **Parent context**: The experiments evaluating the impact of different iteration counts have been implemented and run.

### R186: The results show that the un-finetuned adapter ($T=0$) perfo...
- **Rubric ID**: initial-performance-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The results show that the un-finetuned adapter ($T=0$) performs worse than the base model.
- **Parent context**: The results evaluating the impact of iteration count match those reported in Figure 3(b).

### R187: The results show that the adapted LLM surpasses the performa...
- **Rubric ID**: adaptation-improvement-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The results show that the adapted LLM surpasses the performance of the base model after one round of adaptation.
- **Parent context**: The results evaluating the impact of iteration count match those reported in Figure 3(b).

### R188: The results show that consistent improvements are observed w...
- **Rubric ID**: subsequent-iterations-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The results show that consistent improvements are observed with iterations up to $T=3$.
- **Parent context**: The results evaluating the impact of iteration count match those reported in Figure 3(b).

### R189: Code has been written to compute and save the training cost...
- **Rubric ID**: azure-sft-strategyqa-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the training cost ($) for StrategyQA.
- **Parent context**: The training costs ($) have been computed and saved for each dataset.

### R190: Code has been written to compute and save the training cost...
- **Rubric ID**: azure-sft-gsm8k-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the training cost ($) for GSM8K.
- **Parent context**: The training costs ($) have been computed and saved for each dataset.

### R191: Code has been written to compute and save the training cost...
- **Rubric ID**: azure-sft-truthfulqa-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the training cost ($) for TruthfulQA.
- **Parent context**: The training costs ($) have been computed and saved for each dataset.

### R192: Code has been written to compute and save the inference cost...
- **Rubric ID**: azure-sft-strategyqa-inf-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the inference cost ($/1k questions) for StrategyQA.
- **Parent context**: The inference costs ($/1k questions) have been computed and saved for each dataset.

### R193: Code has been written to compute and save the inference cost...
- **Rubric ID**: azure-sft-gsm8k-inf-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the inference cost ($/1k questions) for GSM8K.
- **Parent context**: The inference costs ($/1k questions) have been computed and saved for each dataset.

### R194: Code has been written to compute and save the inference cost...
- **Rubric ID**: azure-sft-truthfulqa-inf-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the inference cost ($/1k questions) for TruthfulQA.
- **Parent context**: The inference costs ($/1k questions) have been computed and saved for each dataset.

### R195: Code has been written to compute and save the inference cost...
- **Rubric ID**: azure-sft-scienceqa-inf-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the inference cost ($/1k questions) for ScienceQA.
- **Parent context**: The inference costs ($/1k questions) have been computed and saved for each dataset.

### R196: Code has been written to compute and save the cost ($) of co...
- **Rubric ID**: azure-sft-strategyqa-eval-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the cost ($) of computing accuracy for StrategyQA.
- **Parent context**: The evaluation costs ($) for computing accuracy have been computed and saved for each dataset.

### R197: Code has been written to compute and save the cost ($) of co...
- **Rubric ID**: azure-sft-gsm8k-eval-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the cost ($) of computing accuracy for GSM8K.
- **Parent context**: The evaluation costs ($) for computing accuracy have been computed and saved for each dataset.

### R198: Code has been written to compute and save the cost ($) of co...
- **Rubric ID**: azure-sft-truthfulqa-eval-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the cost ($) of computing True+Info scores for TruthfulQA.
- **Parent context**: The evaluation costs ($) for computing accuracy have been computed and saved for each dataset.

### R199: Code has been written to compute and save the cost ($) of co...
- **Rubric ID**: azure-sft-scienceqa-eval-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the cost ($) of computing accuracy for ScienceQA.
- **Parent context**: The evaluation costs ($) for computing accuracy have been computed and saved for each dataset.

### R200: Code has been written to compute and save the training cost...
- **Rubric ID**: adapter-scienceqa-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the training cost ($) for ScienceQA.
- **Parent context**: The training costs ($) have been computed and saved for each dataset.

### R201: Code has been written to compute and save the inference cost...
- **Rubric ID**: adapter-strategyqa-inf-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the inference cost ($/1k questions) for StrategyQA.
- **Parent context**: The inference costs ($/1k questions) have been computed and saved for each dataset.

### R202: Code has been written to compute and save the inference cost...
- **Rubric ID**: adapter-gsm8k-inf-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the inference cost ($/1k questions) for GSM8K.
- **Parent context**: The inference costs ($/1k questions) have been computed and saved for each dataset.

### R203: Code has been written to compute and save the inference cost...
- **Rubric ID**: adapter-truthfulqa-inf-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the inference cost ($/1k questions) for TruthfulQA.
- **Parent context**: The inference costs ($/1k questions) have been computed and saved for each dataset.

### R204: Code has been written to compute and save the inference cost...
- **Rubric ID**: adapter-scienceqa-inf-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the inference cost ($/1k questions) for ScienceQA.
- **Parent context**: The inference costs ($/1k questions) have been computed and saved for each dataset.

### R205: Code has been written to compute and save the cost ($) of co...
- **Rubric ID**: adapter-strategyqa-eval-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the cost ($) of computing accuracy for StrategyQA.
- **Parent context**: The evaluation costs ($) for computing accuracy have been computed and saved for each dataset.

### R206: Code has been written to compute and save the cost ($) of co...
- **Rubric ID**: adapter-gsm8k-eval-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the cost ($) of computing accuracy for GSM8K.
- **Parent context**: The evaluation costs ($) for computing accuracy have been computed and saved for each dataset.

### R207: Code has been written to compute and save the cost ($) of co...
- **Rubric ID**: adapter-truthfulqa-eval-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the cost ($) of computing True+Info scores for TruthfulQA.
- **Parent context**: The evaluation costs ($) for computing accuracy have been computed and saved for each dataset.

### R208: Code has been written to compute and save the cost ($) of co...
- **Rubric ID**: adapter-scienceqa-eval-cost
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the cost ($) of computing accuracy for ScienceQA.
- **Parent context**: The evaluation costs ($) for computing accuracy have been computed and saved for each dataset.

### R209: Code has been written to compute and save the API costs duri...
- **Rubric ID**: full-step-scienceqa-inf-tracking
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the API costs during full-step ScienceQA inference.
- **Parent context**: The inference cost ($/1k questions) for ScienceQA has been computed and saved.

### R210: Code has been written to compute and save API costs during m...
- **Rubric ID**: full-step-truthfulqa-eval-tracking
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save API costs during metric computation for TruthfulQA.
- **Parent context**: The cost ($) of computing performance metrics for TruthfulQA has been computed and saved.

### R211: Code has been written to compute and save API costs during a...
- **Rubric ID**: full-step-scienceqa-eval-tracking
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save API costs during accuracy computation for ScienceQA.
- **Parent context**: The cost ($) of computing accuracy for ScienceQA has been computed and saved.

### R212: The results show that BBOX-ADAPTER reduces training costs by...
- **Rubric ID**: training-reduction-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The results show that BBOX-ADAPTER reduces training costs by ~31.30x compared to Azure-SFT.
- **Parent context**: The cost efficiency trends match those presented in Table 4.

### R213: The results show that BBOX-ADAPTER reduces inference costs b...
- **Rubric ID**: inference-reduction-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The results show that BBOX-ADAPTER reduces inference costs by ~1.84x compared to Azure-SFT.
- **Parent context**: The cost efficiency trends match those presented in Table 4.

### R214: The results show that the single-step variant reduces infere...
- **Rubric ID**: single-step-trend-4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The results show that the single-step variant reduces inference costs by ~6.27x compared to Azure-SFT.
- **Parent context**: The cost efficiency trends match those presented in Table 4.

### R215: The results show that BBOX-ADAPTER achieves these cost reduc...
- **Rubric ID**: training-efficiency-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The results show that BBOX-ADAPTER achieves these cost reductions while maintaining competitive performance (within ~4% of Azure-SFT).
- **Parent context**: The cost efficiency trends match those presented in Table 4.

### R216: The results show that the single-step variant reduces infere...
- **Rubric ID**: single-step-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The results show that the single-step variant reduces inference costs by ~6.27x compared to Azure-SFT.
- **Parent context**: The cost efficiency trends match those presented in Table 4.

### R217: The results show that the single-step variant achieves ~3.45...
- **Rubric ID**: performance-tradeoff-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The results show that the single-step variant achieves ~3.45% improvement over the base model despite lower cost, compared to the full-step's ~5.90% improvement.
- **Parent context**: The cost efficiency trends match those presented in Table 4.

### R218: The accuracy metrics for both 0.1B and 0.3B adapters have be...
- **Rubric ID**: size-performance-calculation
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy metrics for both 0.1B and 0.3B adapters have been calculated.
- **Parent context**: The results match those presented in Table 5.

### R219: The results show that the MLM-based adapter achieves 61.52%...
- **Rubric ID**: mlm-size-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The results show that the MLM-based adapter achieves 61.52% (0.1B) and 60.41% (0.3B) accuracy on StrategyQA.
- **Parent context**: The results match those presented in Table 5.

### R220: The results show that the NCE-based adapter achieves 71.62%...
- **Rubric ID**: nce-size-trend
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The results show that the NCE-based adapter achieves 71.62% (0.1B) and 71.18% (0.3B) accuracy on StrategyQA, showing consistent improvement of ~10% over MLM regardless of adapter size.
- **Parent context**: The results match those presented in Table 5.

### R221: Mixtral-8x7B on 0.1B parameters has been evaluated on the St...
- **Rubric ID**: baseline-inference-plug
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B on 0.1B parameters has been evaluated on the StrategyQA test set, with the accuracy computed and saved.
- **Parent context**: Mixtral-8x7B has been evaluated on the StrategyQA test set with its accuracy and VRAM computed and s...

### R222: Mixtral-8x7B on 0.3B parameters has been evaluated on the St...
- **Rubric ID**: 748c5996-02da-4ef5-a9e2-09aa848218f0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B on 0.3B parameters has been evaluated on the StrategyQA test set, with the accuracy computed and saved.
- **Parent context**: Mixtral-8x7B has been evaluated on the StrategyQA test set with its accuracy and VRAM computed and s...

### R223: Mixtral-8x7B has been evaluated on the StrategyQA test set,...
- **Rubric ID**: baseline-metrics-plug
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B has been evaluated on the StrategyQA test set, with the VRAM computed and saved.
- **Parent context**: Mixtral-8x7B has been evaluated on the StrategyQA test set with its accuracy and VRAM computed and s...

### R224: Mixtral-8x7B with LoRA adaptation on 0.1B parameters has bee...
- **Rubric ID**: adapted-inference-wb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B with LoRA adaptation on 0.1B parameters has been evaluated on the StrategyQA test set, with the accuracy computed and saved.
- **Parent context**: Mixtral-8x7B + LoRA has been evaluated on the StrategyQA test set with its accuracy and VRAM compute...

### R225: Mixtral-8x7B with LoRA adaptation on 0.3B parameters has bee...
- **Rubric ID**: e2171d3f-ab95-4daf-9f47-2439503f7ed0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B with LoRA adaptation on 0.3B parameters has been evaluated on the StrategyQA test set, with the accuracy computed and saved.
- **Parent context**: Mixtral-8x7B + LoRA has been evaluated on the StrategyQA test set with its accuracy and VRAM compute...

### R226: Mixtral-8x7B with LoRA adaptation on 0.1B parameters has bee...
- **Rubric ID**: performance-comparison-whitebox
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B with LoRA adaptation on 0.1B parameters has been evaluated on the StrategyQA test set, with the VRAM computed and saved.
- **Parent context**: Mixtral-8x7B + LoRA has been evaluated on the StrategyQA test set with its accuracy and VRAM compute...

### R227: Mixtral-8x7B with BBox-Adapter adaptation on 0.1B parameters...
- **Rubric ID**: 21c168ee-c5a1-4b10-be7a-bdd84f9be988
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B with BBox-Adapter adaptation on 0.1B parameters has been evaluated on the StrategyQA test set, with the accuracy computed and saved.
- **Parent context**: Mixtral-8x7B + BBox-Adapter has been evaluated on the StrategyQA test set with its accuracy and VRAM...

### R228: Mixtral-8x7B with BBox-Adapter adaptation on 0.3B parameters...
- **Rubric ID**: eaefd25e-575f-4c06-a2b1-6f61f4496e25
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B with BBox-Adapter adaptation on 0.3B parameters has been evaluated on the StrategyQA test set, with the accuracy computed and saved.
- **Parent context**: Mixtral-8x7B + BBox-Adapter has been evaluated on the StrategyQA test set with its accuracy and VRAM...

### R229: Mixtral-8x7B with BBox-Adapter adaptation has been evaluated...
- **Rubric ID**: b2407631-327e-4e5d-9a6d-579cb1ddad2e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B with BBox-Adapter adaptation has been evaluated on the StrategyQA test set using the 0.1B parameter model, with the VRAM computed and saved.
- **Parent context**: Mixtral-8x7B + BBox-Adapter has been evaluated on the StrategyQA test set with its accuracy and VRAM...

### R230: Mixtral-8x7B achieves an accuracy of 59.91% on the StrategyQ...
- **Rubric ID**: base-memory
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B achieves an accuracy of 59.91% on the StrategyQA test set.
- **Parent context**: The results match those presented in Table 6.

### R231: Mixtral-8x7B + LoRA on 0.1B parameters achieves an accuracy...
- **Rubric ID**: lora-memory
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B + LoRA on 0.1B parameters achieves an accuracy of 73.80% on the StrategyQA test set.
- **Parent context**: The results match those presented in Table 6.

### R232: Mixtral-8x7B + LoRA on 0.3B parameters achieves an accuracy...
- **Rubric ID**: 4ab94afb-e410-4732-9b88-96815e66e4eb
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B + LoRA on 0.3B parameters achieves an accuracy of 73.80% on the StrategyQA test set.
- **Parent context**: The results match those presented in Table 6.

### R233: Mixtral-8x7B + LoRA takes up 92GB of VRAM during inference-t...
- **Rubric ID**: 2eca0f28-5595-4957-857b-98208d886c3c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B + LoRA takes up 92GB of VRAM during inference-time the StrategyQA test set.
- **Parent context**: The results match those presented in Table 6.

### R234: Mixtral-8x7B + Bbox-Adapter achieves an accuracy of 66.08% o...
- **Rubric ID**: 100a78df-af5a-410c-a8c1-6eea2331c3ee
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B + Bbox-Adapter achieves an accuracy of 66.08% on the StrategyQA test set with the 0.1B parameter setting.
- **Parent context**: The results match those presented in Table 6.

### R235: Mixtral-8x7B + Bbox-Adapter achieves an accuracy of 65.26% o...
- **Rubric ID**: 504b46df-0b53-4f37-aa64-556b9cf108df
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Mixtral-8x7B + Bbox-Adapter achieves an accuracy of 65.26% on the StrategyQA test set with the 0.3B parameter setting.
- **Parent context**: The results match those presented in Table 6.

## Logging, Analysis & Presentation

### R236: Code has been implemented to compute and save the training l...
- **Rubric ID**: 7e2f154e-02a3-43a6-bf8e-2bfb5cc3711e
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been implemented to compute and save the training loss curves for the StrategyQA fine-tuning process, following the specifications in Appendix H.2.
- **Parent context**: Code has been written to save the training loss curves during Azure-SFT fine-tuning for the Strategy...

### R237: Code has been implemented to compute and save the training l...
- **Rubric ID**: 357edc2c-417b-49ff-b3fd-59af7134f147
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been implemented to compute and save the training loss curves for the TruthfulQA fine-tuning process, following the specifications in Appendix H.2.
- **Parent context**: Code has been written to save the training loss curves during Azure-SFT fine-tuning for the Strategy...

### R238: Code has been implemented to compute and save the training l...
- **Rubric ID**: c4d72598-0892-4d1a-98a7-9fa92fe0fbd7
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been implemented to compute and save the training loss curves for the ScienceQA fine-tuning process, following the specifications in Appendix H.2.
- **Parent context**: Code has been written to save the training loss curves during Azure-SFT fine-tuning for the Strategy...

### R239: Training loss curves have been saved for StrategyQA fine-tun...
- **Rubric ID**: strategyqa-loss-curves
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Training loss curves have been saved for StrategyQA fine-tuning.
- **Parent context**: The training loss curves have been generated and saved.

### R240: Training loss curves have been saved for TruthfulQA fine-tun...
- **Rubric ID**: truthfulqa-loss-curves
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Training loss curves have been saved for TruthfulQA fine-tuning.
- **Parent context**: The training loss curves have been generated and saved.

### R241: Training loss curves have been saved for ScienceQA fine-tuni...
- **Rubric ID**: scienceqa-loss-curves
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Training loss curves have been saved for ScienceQA fine-tuning.
- **Parent context**: The training loss curves have been generated and saved.

### R242: Code has been written to compute and save the training cost...
- **Rubric ID**: azure-sft-scienceqa-cost
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the training cost ($) for ScienceQA.
- **Parent context**: The training costs ($) have been computed and saved for each dataset.

### R243: Code has been written to compute and save the training cost...
- **Rubric ID**: adapter-strategyqa-cost
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the training cost ($) for StrategyQA.
- **Parent context**: The training costs ($) have been computed and saved for each dataset.

### R244: Code has been written to compute and save the training cost...
- **Rubric ID**: adapter-gsm8k-cost
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the training cost ($) for GSM8K.
- **Parent context**: The training costs ($) have been computed and saved for each dataset.

### R245: Code has been written to compute and save the training cost...
- **Rubric ID**: adapter-truthfulqa-cost
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the training cost ($) for TruthfulQA.
- **Parent context**: The training costs ($) have been computed and saved for each dataset.

### R246: Code has been written to track and log the API costs during...
- **Rubric ID**: single-step-strategyqa-inf-tracking
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to track and log the API costs during single-step StrategyQA inference.
- **Parent context**: The inference cost ($/1k questions) for StrategyQA have been computed and saved.

### R247: Code has been written to calculate the cost per 1000 questio...
- **Rubric ID**: single-step-strategyqa-inf-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the cost per 1000 questions from the logged API usage.
- **Parent context**: The inference cost ($/1k questions) for StrategyQA have been computed and saved.

### R248: Code has been written to track and log the API costs during...
- **Rubric ID**: single-step-gsm8k-inf-tracking
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to track and log the API costs during single-step GSM8K inference.
- **Parent context**: The inference cost ($/1k questions) for GSM8K have been computed and saved.

### R249: Code has been written to calculate the cost per 1000 questio...
- **Rubric ID**: single-step-gsm8k-inf-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the cost per 1000 questions from the logged API usage.
- **Parent context**: The inference cost ($/1k questions) for GSM8K have been computed and saved.

### R250: Code has been written to track and log the API costs during...
- **Rubric ID**: single-step-truthfulqa-inf-tracking
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to track and log the API costs during single-step TruthfulQA inference.
- **Parent context**: The inference cost ($/1k questions) for TruthfulQA has been computed and saved.

### R251: Code has been written to calculate the cost per 1000 questio...
- **Rubric ID**: single-step-truthfulqa-inf-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the cost per 1000 questions from the logged API usage.
- **Parent context**: The inference cost ($/1k questions) for TruthfulQA has been computed and saved.

### R252: Code has been written to track and log the API costs during...
- **Rubric ID**: single-step-scienceqa-inf-tracking
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to track and log the API costs during single-step ScienceQA inference.
- **Parent context**: The inference cost ($/1k questions) for ScienceQA has been computed and saved.

### R253: Code has been written to calculate the cost per 1000 questio...
- **Rubric ID**: single-step-scienceqa-inf-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the cost per 1000 questions from the logged API usage.
- **Parent context**: The inference cost ($/1k questions) for ScienceQA has been computed and saved.

### R254: Code has been written to track and log API costs during accu...
- **Rubric ID**: single-step-strategyqa-eval-tracking
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to track and log API costs during accuracy computation for StrategyQA.
- **Parent context**: The cost ($) of computing accuracy for StrategyQA has been computed and saved.

### R255: Code has been written to calculate the total evaluation cost...
- **Rubric ID**: single-step-strategyqa-eval-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the total evaluation cost from the logged API usage.
- **Parent context**: The cost ($) of computing accuracy for StrategyQA has been computed and saved.

### R256: Code has been written to track and log API costs during accu...
- **Rubric ID**: single-step-gsm8k-eval-tracking
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to track and log API costs during accuracy computation for GSM8K.
- **Parent context**: The cost ($) of computing accuracy for GSM8K has been computed and saved.

### R257: Code has been written to calculate the total evaluation cost...
- **Rubric ID**: single-step-gsm8k-eval-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the total evaluation cost from the logged API usage.
- **Parent context**: The cost ($) of computing accuracy for GSM8K has been computed and saved.

### R258: Code has been written to track and log API costs during True...
- **Rubric ID**: single-step-truthfulqa-eval-tracking
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to track and log API costs during True+Info computation for TruthfulQA.
- **Parent context**: The cost ($) of computing True+Info scores for TruthfulQA has been computed and saved.

### R259: Code has been written to calculate the total evaluation cost...
- **Rubric ID**: single-step-truthfulqa-eval-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the total evaluation cost from the logged API usage.
- **Parent context**: The cost ($) of computing True+Info scores for TruthfulQA has been computed and saved.

### R260: Code has been written to track and log API costs during accu...
- **Rubric ID**: single-step-scienceqa-eval-tracking
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to track and log API costs during accuracy computation for ScienceQA.
- **Parent context**: The cost ($) of computing accuracy for ScienceQA has been computed and saved.

### R261: Code has been written to calculate the total evaluation cost...
- **Rubric ID**: single-step-scienceqa-eval-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the total evaluation cost from the logged API usage.
- **Parent context**: The cost ($) of computing accuracy for ScienceQA has been computed and saved.

### R262: Code has been written to track and log the API costs during...
- **Rubric ID**: full-step-strategyqa-inf-tracking
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to track and log the API costs during full-step StrategyQA inference.
- **Parent context**: The inference cost ($/1k questions) for StrategyQA has been computed and saved.

### R263: Code has been written to calculate the cost per 1000 questio...
- **Rubric ID**: full-step-strategyqa-inf-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the cost per 1000 questions from the logged API usage.
- **Parent context**: The inference cost ($/1k questions) for StrategyQA has been computed and saved.

### R264: Code has been written to track and log the API costs during...
- **Rubric ID**: full-step-gsm8k-inf-tracking
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to track and log the API costs during full-step GSM8K inference.
- **Parent context**: The inference cost ($/1k questions) for GSM8K has been computed and saved.

### R265: Code has been written to calculate the cost per 1000 questio...
- **Rubric ID**: full-step-gsm8k-inf-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the cost per 1000 questions from the logged API usage.
- **Parent context**: The inference cost ($/1k questions) for GSM8K has been computed and saved.

### R266: Code has been written to track and log the API costs during...
- **Rubric ID**: full-step-truthfulqa-inf-tracking
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to track and log the API costs during full-step TruthfulQA inference.
- **Parent context**: The inference cost ($/1k questions) for TruthfulQA has been computed and saved.

### R267: Code has been written to calculate the cost per 1000 questio...
- **Rubric ID**: full-step-truthfulqa-inf-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the cost per 1000 questions from the logged API usage.
- **Parent context**: The inference cost ($/1k questions) for TruthfulQA has been computed and saved.

### R268: Code has been written to calculate the cost per 1000 questio...
- **Rubric ID**: full-step-scienceqa-inf-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the cost per 1000 questions from the logged API usage.
- **Parent context**: The inference cost ($/1k questions) for ScienceQA has been computed and saved.

### R269: Code has been written to track and log API costs during accu...
- **Rubric ID**: full-step-strategyqa-eval-tracking
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to track and log API costs during accuracy computation for StrategyQA.
- **Parent context**: The cost ($) of computing accuracy for StrategyQA has been computed and saved.

### R270: Code has been written to calculate the total evaluation cost...
- **Rubric ID**: full-step-strategyqa-eval-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the total evaluation cost from the logged API usage.
- **Parent context**: The cost ($) of computing accuracy for StrategyQA has been computed and saved.

### R271: Code has been written to track and log API costs during accu...
- **Rubric ID**: full-step-gsm8k-eval-tracking
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to track and log API costs during accuracy computation for GSM8K.
- **Parent context**: The cost ($) of computing accuracy for GSM8K has been computed and saved.

### R272: Code has been written to calculate the total evaluation cost...
- **Rubric ID**: full-step-gsm8k-eval-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the total evaluation cost from the logged API usage.
- **Parent context**: The cost ($) of computing accuracy for GSM8K has been computed and saved.

### R273: Code has been written to calculate the total evaluation cost...
- **Rubric ID**: full-step-truthfulqa-eval-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the total evaluation cost from the logged API usage.
- **Parent context**: The cost ($) of computing performance metrics for TruthfulQA has been computed and saved.

### R274: Code has been written to calculate the total evaluation cost...
- **Rubric ID**: full-step-scienceqa-eval-calculation
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the total evaluation cost from the logged API usage.
- **Parent context**: The cost ($) of computing accuracy for ScienceQA has been computed and saved.

### R275: The results show that the full-step variant reduces inferenc...
- **Rubric ID**: full-step-trend
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The results show that the full-step variant reduces inference costs by ~1.84x compared to Azure-SFT.
- **Parent context**: The cost efficiency trends match those presented in Table 4.

### R276: Mixtral-8x7B takes up 90GB of VRAM during inference-time the...
- **Rubric ID**: adapter-memory
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Mixtral-8x7B takes up 90GB of VRAM during inference-time the StrategyQA test set.
- **Parent context**: The results match those presented in Table 6.

### R277: Mixtral-8x7B + LoRA takes up 208GB of VRAM during train-time...
- **Rubric ID**: 7c3f6fb5-590f-4e65-afcb-8e15c590287f
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Mixtral-8x7B + LoRA takes up 208GB of VRAM during train-time the StrategyQA test set.
- **Parent context**: The results match those presented in Table 6.

### R278: Mixtral-8x7B + Bbox-Adapter takes up 105GB of VRAM during tr...
- **Rubric ID**: 2067127d-80e8-4b1c-93a6-54aa352e7607
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Mixtral-8x7B + Bbox-Adapter takes up 105GB of VRAM during train-time the StrategyQA test set.
- **Parent context**: The results match those presented in Table 6.

### R279: Mixtral-8x7B + Bbox-Adapter takes up 92GB of VRAM during inf...
- **Rubric ID**: 52c38b9d-ce30-4d86-b7dc-90f31cf3ebb8
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Mixtral-8x7B + Bbox-Adapter takes up 92GB of VRAM during inference-time the StrategyQA test set.
- **Parent context**: The results match those presented in Table 6.
