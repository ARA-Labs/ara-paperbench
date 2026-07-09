# Related Work

## RW01: Miller et al., 2021 (Accuracy-on-the-Line)
- **DOI**: ICML 2021 Proceedings
- **Type**: baseline
- **Delta**:
  - What changed: LCA-on-the-Line replaces Top-1 ID accuracy with LCA distance as the OOD predictor
  - Why: Top-1 accuracy fails to unify VM and VLM families (two separate linear trends); LCA provides a single unified trend
- **Claims affected**: C01
- **Adopted elements**: The "on-the-line" evaluation framework concept; use of ImageNet as ID reference anchor; same 5 OOD datasets

## RW02: Baek et al., 2022 (Agreement-on-the-Line)
- **DOI**: NeurIPS 2022
- **Type**: baseline
- **Delta**:
  - What changed: LCA-on-the-Line uses a single-model in-distribution metric (no model pairs needed); does not require OOD data or multiple models
  - Why: Agreement-on-the-Line requires computing consensus between model pairs on OOD benchmarks (computationally expensive), fails for cross-modality comparison
- **Claims affected**: C01
- **Adopted elements**: Comparison methodology; Aline-D and Aline-S baselines for MAE comparison

## RW03: Taori et al., 2020 (Effective Robustness)
- **DOI**: NeurIPS 2020
- **Type**: imports
- **Delta**:
  - What changed: LCA provides a better explanation of why VLMs appear to have "high effective robustness" — they simply have lower LCA distance
  - Why: Effective robustness framework lacks a mechanism to explain cross-modal differences
- **Claims affected**: C01
- **Adopted elements**: Concept of effective robustness; motivation for predicting OOD from ID measurements

## RW04: Bertinetto et al., 2020 (Making Better Mistakes)
- **DOI**: CVPR 2020
- **Type**: imports
- **Delta**:
  - What changed: LCA-on-the-Line uses LCA distance as a generalization predictor rather than just an evaluation metric; demonstrates LCA and Top-1 do NOT always align (especially across modalities)
  - Why: Bertinetto et al. established LCA as a quality metric but dismissed it as correlated with Top-1 accuracy
- **Claims affected**: C01, C04
- **Adopted elements**: LCA distance definition; WordNet hierarchy usage; information content formulation; the concept of "making better mistakes"

## RW05: Valmadre, 2022 (Hierarchical classification at multiple operating points)
- **DOI**: arXiv:2210.10929
- **Type**: imports
- **Delta**:
  - What changed: This paper directly uses Valmadre's information content formulation for LCA computation
  - Why: Information content is more robust to tree imbalance than simple tree depth
- **Claims affected**: C01, C02
- **Adopted elements**: Information content node scoring function $I(v) = -\log_2(p(v))$ where $p$ is computed recursively

## RW06: Deng et al., 2009 (ImageNet)
- **DOI**: CVPR 2009
- **Type**: imports
- **Delta**:
  - What changed: LCA-on-the-Line revives the LCA metric from early ImageNet challenge evaluations
  - Why: LCA was used in early ImageNet benchmarking but abandoned as Top-1 became dominant
- **Claims affected**: C01
- **Adopted elements**: ImageNet hierarchy structure; WordNet synset mapping

## RW07: Radford et al., 2021 (CLIP)
- **DOI**: ICML 2021
- **Type**: baseline
- **Delta**:
  - What changed: CLIP models are analyzed through the LCA lens; LCA explains why CLIP generalizes better than VMs
  - Why: CLIP's generalization was previously attributed to data diversity but LCA provides a unified feature-quality explanation
- **Claims affected**: C01, C05
- **Adopted elements**: 7 CLIP model variants included in the 75-model evaluation

## RW08: Cherti et al., 2023 (OpenCLIP Scaling Laws)
- **DOI**: CVPR 2023
- **Type**: baseline
- **Delta**:
  - What changed: 31 OpenCLIP variants included in the 75-model evaluation; confirms that VLMs show higher OOD accuracy than expected from ID accuracy
  - Why: Cherti et al. found VLMs show separate OOD trends from VMs; LCA provides the unified explanation
- **Claims affected**: C01, C02
- **Adopted elements**: OpenCLIP model weights and architecture variants

## RW09: Arjovsky et al., 2019 (Invariant Risk Minimization)
- **DOI**: arXiv:1907.02893
- **Type**: imports
- **Delta**:
  - What changed: LCA provides a practical, interpretable proxy for measuring invariant feature learning
  - Why: IRM requires domain labels and structural assumptions; LCA needs only a class hierarchy
- **Claims affected**: C04
- **Adopted elements**: Conceptual framework: features invariant across environments lead to better OOD generalization; causal/confounding feature distinction

## RW10: Wortsman et al., 2022 (WiSE-FT)
- **DOI**: CVPR 2022
- **Type**: imports
- **Delta**:
  - What changed: Adapts the weight interpolation technique to combine CE-only and CE+soft probes
  - Why: Weight interpolation allows smooth trade-off between ID and OOD performance without OOD data
- **Claims affected**: C03
- **Adopted elements**: Linear weight interpolation: W_interp = alpha*W_1 + (1-alpha)*W_2; selected on ID validation set

## RW11: Fang et al., 2022 (Data diversity in CLIP)
- **DOI**: ICML 2022
- **Type**: bounds
- **Delta**:
  - What changed: LCA offers a model-intrinsic explanation for VLM generalization that complements data diversity perspective
  - Why: Data diversity is hard to measure and doesn't explain differences within CLIP variants
- **Claims affected**: C01
- **Adopted elements**: Motivation for studying VLM vs VM generalization gap

## RW12: Hendrycks et al., 2021 (ImageNet-R/A)
- **DOI**: ICCV 2021
- **Type**: imports
- **Delta**:
  - What changed: ImageNet-R and ImageNet-A are used as key OOD benchmarks in LCA-on-the-Line
  - Why: These datasets represent severe, natural distribution shifts that reveal meaningful generalization differences
- **Claims affected**: C01
- **Adopted elements**: ImageNet-Rendition and ImageNet-Adversarial datasets as OOD evaluation benchmarks
