# Related Work

## RW01: Devlin et al., 2019 (BERT)
- **DOI**: 10.18653/v1/N19-1423
- **Type**: imports
- **Delta**:
  - What changed: BBOX-ADAPTER uses DeBERTa/BERT as an energy scorer (classification head outputting scalar) rather than as a task classifier
  - Why: Pretrained encoders provide rich contextual representations for scoring (question, answer) pairs
- **Claims affected**: C01, C04
- **Adopted elements**: Pretrained DeBERTa-v3-base/large and BERT-base-cased as adapter backbones; [CLS] token representation for scoring

## RW02: Hu et al., 2021 (LoRA)
- **DOI**: arXiv:2106.09685
- **Type**: baseline
- **Delta**:
  - What changed: BBOX-ADAPTER adapts black-box LLMs without accessing parameters; LoRA directly updates rank-decomposed weight matrices inside the white-box model
  - Why: LoRA is inapplicable to black-box APIs; used as white-box upper-bound baseline
- **Claims affected**: C01, C02, C03
- **Adopted elements**: Used as SFT-LoRA baseline with r=128/384, α=2r, for Mixtral-8×7B comparison (Table 6)

## RW03: Gutmann & Hyvarinen, 2010 (NCE)
- **DOI**: JMLR Workshop Proceedings 9
- **Type**: imports
- **Delta**:
  - What changed: BBOX-ADAPTER extends NCE from binary real/noise to a ranking-based objective that pushes target samples above source samples
  - Why: Standard NCE only distinguishes real vs. noise; ranking-based variant better captures the relative quality of candidates
- **Claims affected**: C04
- **Adopted elements**: NCE principle of avoiding intractable partition function; ranking-based variant from Ma & Collins (2018)

## RW04: Ma & Collins, 2018 (Ranking NCE)
- **DOI**: 10.18653/v1/D18-1405
- **Type**: imports
- **Delta**:
  - What changed: Applied to energy-based LLM adaptation with online dynamic positive/negative sampling instead of static corpus
  - Why: Enables domain adaptation via ranking without requiring gold probability labels
- **Claims affected**: C04
- **Adopted elements**: Ranking-based NCE loss formulation (Eq. 2); proof that optimal solution recovers data distribution

## RW05: Du & Mordatch, 2019 (EBM with spectral normalization)
- **DOI**: arXiv:1903.08689
- **Type**: imports
- **Delta**:
  - What changed: BBOX-ADAPTER applies spectral normalization specifically to prevent gradient instability in the NCE-trained adapter
  - Why: Sharp gradients destabilize EBM training; spectral normalization provides Lipschitz control
- **Claims affected**: C04
- **Adopted elements**: Spectral normalization technique; regularization terms $\alpha\mathbb{E}[g_\theta(x,y)^2]$ in loss gradient

## RW06: Peng et al., 2023 (Azure-SFT / GPT-3.5-turbo Fine-Tuning API)
- **DOI**: OpenAI Blog 2023
- **Type**: baseline
- **Delta**:
  - What changed: BBOX-ADAPTER eliminates the need for fine-tuning APIs by training an external lightweight adapter
  - Why: API fine-tuning is opaque (only 3 adjustable hyperparameters), privacy-risky, and costly (31.30× more expensive in training)
- **Claims affected**: C01, C02, C03
- **Adopted elements**: Azure-SFT serves as the primary performance upper bound and cost comparison baseline

## RW07: Huang et al., 2023 (kNN-Adapter)
- **DOI**: arXiv:2302.10879
- **Type**: bounds
- **Delta**:
  - What changed: BBOX-ADAPTER removes the requirement for a domain-specific retrieval datastore and token-probability access
  - Why: kNN-Adapter requires output token probabilities for interpolation (grey-box); unavailable in modern black-box LLMs
- **Claims affected**: C01
- **Adopted elements**: Concept of augmenting LLM generation with an external module

## RW08: Ormazabal et al., 2023 (CombLM)
- **DOI**: 10.18653/v1/2023.emnlp-main.180
- **Type**: bounds
- **Delta**:
  - What changed: BBOX-ADAPTER uses text-level energy scoring instead of logit-level combination; no token probabilities required
  - Why: CombLM interpolates log-probabilities from white-box and black-box models, requiring token probability access
- **Claims affected**: C01
- **Adopted elements**: Concept of combining a small fine-tuned model with a large black-box LLM

## RW09: Liu et al., 2024 (Proxy-Tuning)
- **DOI**: arXiv:2401.08565
- **Type**: bounds
- **Delta**:
  - What changed: BBOX-ADAPTER operates on text outputs only; Proxy-Tuning requires logit-level adjustments using expert/anti-expert token probabilities
  - Why: Logit offsets require probability access; unavailable in black-box APIs
- **Claims affected**: C01
- **Adopted elements**: Concept of using a small model to adjust black-box LLM outputs

## RW10: Sun et al., 2022 (LMaaS)
- **DOI**: ICML 2022
- **Type**: bounds
- **Delta**:
  - What changed: BBOX-ADAPTER trains an energy-based scorer; LMaaS trains a derivative-free optimizer for discrete prompt tuning requiring high-dimensional input/output representations
  - Why: LMaaS still requires gradient information via high-dimensional representations
- **Claims affected**: C01
- **Adopted elements**: Paradigm of adapting LLMs as a service without internal parameter access

## RW11: Wei et al., 2022 (Chain-of-Thought)
- **DOI**: NeurIPS 2022
- **Type**: baseline
- **Delta**:
  - What changed: BBOX-ADAPTER combines CoT prompting with adapter-guided beam search; pure CoT is the non-adapted baseline
  - Why: CoT provides a strong baseline that BBOX-ADAPTER must surpass
- **Claims affected**: C01
- **Adopted elements**: CoT prompts used as the base generation strategy for all experiments; few-shot prompt format

## RW12: Deng et al., 2020 (Residual EBM for Text Generation)
- **DOI**: arXiv:2004.11714
- **Type**: imports
- **Delta**:
  - What changed: BBOX-ADAPTER applies residual EBM to black-box LLM adaptation with online learning; Deng et al. apply it to white-box text generation
  - Why: The residual EBM formulation (Eq. 1) is directly adopted but extended to the black-box setting
- **Claims affected**: C01, C04
- **Adopted elements**: Residual EBM parameterization $p_\theta(y|x) = p_{LLM}(y|x)\exp(g_\theta(x,y))/Z_\theta(x)$
