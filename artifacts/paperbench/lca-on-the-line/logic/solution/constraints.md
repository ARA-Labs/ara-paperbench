# Boundary Conditions and Limitations

## BC01: LCA ineffective for visually similar OOD datasets
- **Condition**: LCA distance is NOT a reliable OOD predictor for datasets with minimal visual shift from the ID dataset.
- **Affected dataset**: ImageNet-v2 (recollection of ImageNet)
- **Reason**: VMs inflate ID accuracy on ImageNet-v2 because spurious correlations from ImageNet training transfer successfully to this collection (minimal external intervention). This disrupts the unbiased linear relationship that LCA establishes on truly shifted datasets.
- **Evidence**: R²(LCA→ImgN-v2 Top1)=0.339 vs R²(Top1→ImgN-v2 Top1)=0.962 (Table 2)
- **Workaround**: Use ID Top-1 accuracy for ImageNet-v2 style datasets; use LCA for severely shifted datasets.

## BC02: ELCA not comparable across model modalities
- **Condition**: ELCA distance should NOT be used to compare VMs and VLMs.
- **Reason**: ELCA is sensitive to logit temperature calibration. VLMs typically output logits with different temperature characteristics than VMs trained with cross-entropy on class labels.
- **Evidence**: Stated explicitly in paper (Table 8 note)

## BC03: LCA weaker discriminator for datasets with few classes
- **Condition**: LCA distance has reduced discriminative power when the dataset has a small number of classes (e.g., CIFAR-10 with 10 classes).
- **Reason**: With few classes, the semantic distance space is compressed and fewer hierarchy levels exist, reducing variation in LCA distances across models.
- **Evidence**: Stated in Limitations section

## BC04: Adversarial LCA models theoretically possible
- **Condition**: A model could achieve low LCA distance with zero Top-1 accuracy (adversarially designed to always predict the semantically nearest wrong class).
- **Reason**: The relationship between LCA and Top-1 is correlational, not causal.
- **Evidence**: Discussed in Appendix B ("Is it Possible for a Semantically-Aware (Low LCA) Model to Have Low Top 1 Accuracy?")

## BC05: K-means hierarchy quality depends on source model
- **Condition**: Latent hierarchies constructed from VMs produce lower-quality soft labels than those from VLMs.
- **Reason**: VLMs have more regularized feature spaces over class centroids (as suggested by their lower LCA distance), so their feature clustering better approximates the WordNet semantic structure.
- **Evidence**: Table 6 shows OpenCLIP(vit-l-14) produces better soft labels than MnasNet or ResNet-18

## BC06: Linear probing does not represent full fine-tuning
- **Condition**: Results in Table 5/6 are for linear probes (frozen backbone + trained linear head), not for full model fine-tuning.
- **Reason**: The paper does not report end-to-end training with the LCA loss, only linear probing experiments.
- **Scope**: The "pro-OOD" setting allows slight ID accuracy drops to achieve larger OOD gains.

## BC07: LCA assumes ID data as reference anchor
- **Condition**: The framework uses ImageNet as a fixed reference anchor, even for VLMs not trained on ImageNet.
- **Reason**: To ensure fair comparison, all models are evaluated on the same ID dataset regardless of their training data.
- **Evidence**: Section 4 explicitly notes that "ID" and "OOD" are not model-specific in this context.

## Known Limitations (from paper)
- No theoretical justification for the LCA-on-the-Line framework
- Future work: causal discovery on ImageNet to construct causal class graphs
- LCA is not an effective indicator for datasets visually similar to ID data
