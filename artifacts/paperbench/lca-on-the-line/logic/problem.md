# Problem Specification

## Observations

### O1: VLMs outperform VMs on severely shifted OOD datasets despite lower ID accuracy
- **Statement**: Vision-Language Models (VLMs) trained on LAION with contrastive loss achieve higher OOD Top-1 accuracy on ImageNet-R, ImageNet-S, ImageNet-A, and ObjectNet compared to Vision Models (VMs) with comparable or higher ImageNet ID accuracy. For example, CLIP_RN50 (ID Top1=0.579) achieves 0.218 on ImageNet-A vs ResNet50 (ID Top1=0.733) achieving 0.018.
- **Evidence**: Table 1 (main paper); Figure 1 (left panel shows two divergent linear trends)
- **Implication**: ID Top-1 accuracy is insufficient to explain OOD generalization across different model families.

### O2: Accuracy-on-the-Line (Miller et al., 2021) breaks down across model modalities
- **Statement**: The established linear relationship between ID and OOD accuracy holds within VMs or within VLMs separately, but breaks down when both families are considered together. For severely shifted datasets (ImageNet-S/R/A/ObjectNet), R²(Top1→OOD Top1) ≈ 0.075, 0.020, 0.009, 0.273 respectively (across all 75 models).
- **Evidence**: Table 2, Figure 5 (red line showing two separate trends for VMs vs VLMs)
- **Implication**: A unified metric for cross-modality OOD prediction is needed.

### O3: LCA distance correlates strongly with OOD accuracy across both model families
- **Statement**: In-distribution LCA distance (information content) on ImageNet strongly correlates with OOD Top-1 accuracy across all 75 models on 4/5 OOD datasets: R²(LCA→ImgN-S Top1)=0.816, R²(LCA→ImgN-R Top1)=0.779, R²(LCA→ImgN-A Top1)=0.704, R²(LCA→ObjNet Top1)=0.915. PEA values: 0.903, 0.883, 0.839, 0.956 respectively.
- **Evidence**: Table 2; Figure 1 (right panel showing unified linear trend)
- **Implication**: Semantic severity of mispredictions (LCA distance) is a better proxy for transferable feature learning than top-1 accuracy.

### O4: ImageNet-v2 behaves more like ID than OOD for VMs
- **Statement**: ImageNet-v2 shows R²(Top1→ImgN-v2 Top1)=0.962 (high), while R²(LCA→ImgN-v2 Top1)=0.339 (low), reversing the pattern seen in other OOD datasets.
- **Evidence**: Table 2, Section 4.1, Appendix B
- **Implication**: ImageNet-v2 is a recollection of ImageNet with minimal external intervention; spurious correlations from ImageNet training transfer to ImageNet-v2, inflating VM ID accuracy measures.

## Gaps

### G1: No unified OOD predictor across VM and VLM families
- **Statement**: Existing "X-on-the-Line" methods (Accuracy, Agreement) fail to provide a single linear function that predicts OOD performance for both VMs and VLMs simultaneously.
- **Caused by**: O1, O2
- **Existing attempts**: Accuracy-on-the-Line (Miller et al., 2021); Agreement-on-the-Line (Baek et al., 2022)
- **Why they fail**: VMs trained on ImageNet inflate ID Top-1 through spurious correlations that don't transfer to severely shifted OOD datasets; these methods treat both families separately.

### G2: LCA distance dismissed as redundant with Top-1 accuracy
- **Statement**: Prior work (Deng et al., 2009; Bertinetto et al., 2020) assumed LCA distance follows the same ordering as Top-1 accuracy, making it uninformative. This belief was not tested across different model modalities.
- **Caused by**: O1, O3
- **Existing attempts**: LCA used in early ImageNet challenge evaluations; later abandoned.
- **Why they fail**: The correlation between LCA and Top-1 is weak when mixing VM and VLM families on ID datasets (PEA=0.174 on ImageNet for all 75 models), revealing LCA carries independent information.

### G3: No hierarchy available for arbitrary datasets
- **Statement**: WordNet is only available for ImageNet-like datasets; no principled method existed to construct class taxonomies for arbitrary datasets to enable LCA-based evaluation.
- **Caused by**: O3
- **Existing attempts**: Manual hierarchy construction (iNaturalist, ImageNet)
- **Why they fail**: Labor-intensive, domain-specific, not scalable.

## Key Insight

- **Insight**: A model that consistently makes "better mistakes"—predicting semantically closer classes in the hierarchy when wrong—has learned more transferable (causal) features rather than spurious correlations. The LCA distance on in-distribution data serves as a proxy for this feature quality and is invariant to the training modality (class labels vs. captions), thereby providing a unified cross-modal OOD predictor.
- **Derived from**: O1, O2, O3
- **Enables**: The LCA-on-the-Line framework: a single linear function mapping ID LCA distance to OOD Top-1 accuracy that works for both VMs and VLMs.

## Assumptions

- A1: WordNet hierarchy approximates invariant inter-class relationships that remain stable across ID and OOD environments.
- A2: Models that learn transferable features tend to predict semantically nearby classes when making errors (i.e., lower LCA distance implies better feature alignment with class ontology).
- A3: The "on-the-line" linear relationship generalizes across architectures, training objectives (CE vs. contrastive), and training data distributions (ImageNet class labels vs. LAION captions).
- A4: Class hierarchies (WordNet) serve as a valid approximation of invariant causal relationships between classes across environments, as in invariant risk minimization.
- A5: ImageNet serves as a valid reference anchor dataset for evaluating generalization, even for VLMs not trained on it.
