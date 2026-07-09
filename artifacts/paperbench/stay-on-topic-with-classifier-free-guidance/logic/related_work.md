---
# Related Work

## RW01: Ho & Salimans, 2021 (Original CFG)
- **DOI**: NeurIPS 2021 Workshop on Deep Generative Models and Downstream Applications
- **Type**: imports
- **Delta**:
  - What changed: Original CFG was applied to diffusion models with conditioning dropout training; this paper applies CFG to autoregressive LMs without any training changes
  - Why: Autoregressive LMs naturally support unconditional generation; no conditioning dropout needed
- **Claims affected**: C01, C02, C03, C04, C05
- **Adopted elements**: Core CFG formula (Eq. 2/3); guidance strength γ interpretation; negative prompting concept

## RW02: Dhariwal & Nichol, 2021 (Classifier Guidance)
- **DOI**: NeurIPS 2021 (Advances in NIP, 34:8780–8794)
- **Type**: imports
- **Delta**:
  - What changed: Classifier guidance requires separate classifier Pφ(c|x); CFG eliminates the auxiliary classifier by using the model itself
  - Why: Avoids the computational overhead and need for a separate trained classifier
- **Claims affected**: C01, C05
- **Adopted elements**: Observation that γ>1 overemphasizes conditioning, trading diversity for quality; γ parameter definition

## RW03: Dathathri et al., 2019 (PPLM)
- **DOI**: arXiv:1912.02164
- **Type**: baseline
- **Delta**:
  - What changed: PPLM uses Bayes rule to factorize controlled distribution with gradient-based hidden state modification; CFG operates purely in logit space
  - Why: Logit-space operation is architecture-agnostic and avoids gradient computation at inference time
- **Claims affected**: C01, C04
- **Adopted elements**: Conceptual framework of inference-time controlled generation without retraining

## RW04: Li et al., 2022 (Contrastive Decoding)
- **DOI**: arXiv:2210.15097
- **Type**: baseline
- **Delta**:
  - What changed: Contrastive decoding uses two different models (expert fs and weak fw): fs(x|y) − fw(x|y); CFG uses a single model with and without prompt
  - Why: Single-model approach avoids need for a second model; CFG is more practical
- **Claims affected**: C01, C02
- **Adopted elements**: Vector arithmetic in logit space; idea of subtracting a weaker/less-informed distribution

## RW05: Wei et al., 2022 (Chain-of-Thought Prompting)
- **DOI**: NeurIPS 2022 (volume 35, pp. 24824–24837)
- **Type**: extends
- **Delta**:
  - What changed: CoT was shown to improve reasoning; this paper shows CFG further improves CoT validity rate and accuracy at low γ
  - Why: CFG helps keep CoT chains on-track, reducing drift from the task prompt
- **Claims affected**: C03
- **Adopted elements**: CoT prompting methodology; few-shot prompt structure for reasoning tasks

## RW06: Wang et al., 2023 (Self-Consistency CoT)
- **DOI**: ICLR 2023
- **Type**: extends
- **Delta**:
  - What changed: Self-consistency uses majority voting over multiple CoT paths; this paper adds CFG to the CoT generation step within this framework
  - Why: CFG improves individual chain quality, which compounds with self-consistency's ensemble benefit
- **Claims affected**: C03
- **Adopted elements**: Few-shot prompt format for GSM8K and AQuA; parsing settings

## RW07: Yang & Klein, 2021 (FUDGE)
- **DOI**: arXiv:2104.05218
- **Type**: baseline
- **Delta**:
  - What changed: FUDGE uses a future discriminator (auxiliary classifier) to guide generation; CFG uses the model's own conditional vs unconditional distributions
  - Why: CFG requires no auxiliary model; FUDGE requires training a discriminator per attribute
- **Claims affected**: C01, C04
- **Adopted elements**: Controlled generation evaluation methodology (toxicity, sentiment)

## RW08: Nijkamp et al., 2023 (CodeGen)
- **DOI**: ICLR 2023
- **Type**: baseline
- **Delta**:
  - What changed: CodeGen is evaluated without CFG; this paper applies CFG to CodeGen for HumanEval
  - Why: Code generation represents a formal-language distribution distinct from natural language, testing CFG robustness
- **Claims affected**: C04
- **Adopted elements**: CodeGen-350M/2B/6B-mono model checkpoints; HumanEval evaluation framework

## RW09: Touvron et al., 2023 (LLaMA)
- **DOI**: arXiv:2302.13971
- **Type**: baseline
- **Delta**:
  - What changed: LLaMA evaluated at γ=1 (vanilla); this paper shows LLaMA-7B with CFG (γ=1.5) achieves new SOTA on Lambada
  - Why: LLaMA-7B is a strong open-source baseline; demonstrating CFG improvement on it is significant
- **Claims affected**: C01, C02
- **Adopted elements**: LLaMA 7B/13B/30B/65B model checkpoints; TriviaQA evaluation uses substring match per LLaMA methodology

## RW10: Biderman et al., 2023 (Pythia)
- **DOI**: arXiv (2023)
- **Type**: baseline
- **Delta**:
  - What changed: Pythia provides a controlled model family for scaling analysis; CFG is applied across all sizes
  - Why: Pythia's consistent training setup makes it ideal for studying CFG's effect across model scales
- **Claims affected**: C01, C02
- **Adopted elements**: Pythia 160M/410M/1B/1.4B/2.8B/6.9B/12B checkpoints; EleutherAI LM Evaluation Harness
