# Table 1: Model Performance Corresponds to Mistake Severity
- **Source**: Table 1, Section 4.1
- **Caption**: "Model performance corresponds to mistake severity. Results are measured by LCA ↓ and Top1 ↑, respectively. indicate measurements on a given dataset. We present model comparisons across VMs and VLMs families. In-distribution LCA distance indicate severely shifted OOD performance (ImageNet-S/R/A/O) better than in-distribution (ImageNet) Top1 accuracy (except for ImageNet-v2). Full 75 models evaluation in Table 2."
- **Conditions**: LCA uses information content scoring (D^I_LCA), averaged over misclassified samples; all models evaluated on the same 6 datasets

| Model | ImgN LCA ↓ | ImgN Top1 ↑ | ImgN-v2 Top1 ↑ | ImgN-S Top1 ↑ | ImgN-R Top1 ↑ | ImgN-A Top1 ↑ | ObjNet Top1 ↑ |
|-------|-----------|------------|---------------|--------------|--------------|--------------|--------------|
| ResNet18 | 6.643 | 0.698 | 0.573 | 0.202 | 0.330 | 0.011 | 0.272 |
| ResNet50 | 6.539 | 0.733 | 0.610 | 0.235 | 0.361 | 0.018 | 0.316 |
| CLIP_RN50 | 6.327 | 0.579 | 0.511 | 0.332 | 0.562 | 0.218 | 0.398 |
| CLIP_RN50x4 | 6.166 | 0.641 | 0.573 | 0.415 | 0.681 | 0.384 | 0.504 |
