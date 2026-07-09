# Environment

- **Python**: Not specified in paper
- **Framework**: PyTorch (implied by gradient operations and model APIs)
- **Hardware**: Not specified in paper (GPUs required for training 400M-3B parameter models)
- **Key dependencies**:
  - Transformers (HuggingFace) for BART0, FLAN-T5, FLAN-T5small model loading
  - P3 dataset (Public Pool of Prompts) via PromptSource
  - MMLU dataset from https://people.eecs.berkeley.edu/~hendrycks/data.tar
  - P3 test split from https://github.com/INK-USC/ReCross/blob/main/data/
  - peft (HuggingFace PEFT library) for LoRA implementation
- **Random seeds**: Not specified in paper
- **Code availability**: https://inklab.usc.edu/lm-forgetting-prediction/
