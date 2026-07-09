# Environment

- **Python**: Not specified in paper
- **Framework**: PyTorch (version not specified in paper)
- **Hardware**: Not specified in paper (GPU cluster assumed; single-precision and half-precision APGD attacks require significant GPU memory for ViT-L/14 + LLM inference)
- **Key dependencies**:
  - OpenCLIP (for CLIP ViT-L/14 implementation; LLaVA requires OpenCLIP instead of HuggingFace CLIP per reproduction rubric)
  - `open_flamingo` (OpenFlamingo 9B)
  - `transformers` (LLaVA-1.5 7B/13B; Vicuna-7B, MPT-7B)
  - `torch` + `torchvision`
  - `autoattack` (Croce & Hein, 2020) for evaluation
  - ImageNet dataset (training, 2 epochs, 224×224, no labels for FARE)
  - COCO 2014, Flickr30k, VQAv2, TextVQA (LVLM evaluation)
  - CalTech101, StanfordCars, CIFAR10, CIFAR100, DTD, EuroSAT, FGVC Aircrafts, Flowers102, ImageNet-R, ImageNet-Sketch, PCAM, OxfordPets, STL-10 (zero-shot eval)
  - POPE benchmark (COCO validation subset)
  - SQA-I (Science QA, 10k image/question pairs)
- **Random seeds**: Not specified in paper
- **Precision**: Half precision (float16) for initial APGD attacks; single precision (float32) for final APGD attacks and targeted attacks
- **Jailbreak attack params**: 5000 iterations, α = 1/255 (from Qi et al., 2023 attack)
- **Model checkpoints**: Available on GitHub (linked from paper); TeCoA checkpoints from https://github.com/cvlab-columbia/ZSRobust4FoundationModel
