# Table 8: Model Performance Corresponds to Mistake Severity (LCA and ELCA)
- **Source**: Table 8, Appendix D.3
- **Caption**: "Model performance corresponds to mistake severity. LCA ↓ / ELCA ↓ / Top1 ↑ indicate measurements on a given dataset. We present two pairs of model comparisons from the VMs and VLMs families with different generalization abilities. Note that ELCA should not be compared across modalities, as it is sensitive to logit temperature."
- **Conditions**: All metrics measured per dataset; LCA uses information content (D^I_LCA); ELCA uses full softmax distribution weighted by D_LCA; Top1 is classification accuracy

| Model | ImgN LCA | ImgN ELCA | ImgN Top1 | ImgN-v2 LCA | ImgN-v2 ELCA | ImgN-v2 Top1 | ImgN-S LCA | ImgN-S ELCA | ImgN-S Top1 | ImgN-R LCA | ImgN-R ELCA | ImgN-R Top1 | ImgN-A LCA | ImgN-A ELCA | ImgN-A Top1 | ObjNet LCA | ObjNet ELCA | ObjNet Top1 |
|-------|---------|----------|----------|------------|-------------|-------------|-----------|------------|------------|-----------|------------|------------|-----------|------------|------------|----------|-----------|----------|
| ResNet18 | 6.643 | 7.505 | 0.698 | 6.918 | 7.912 | 0.573 | 8.005 | 9.283 | 0.202 | 8.775 | 8.853 | 0.330 | 8.449 | 9.622 | 0.011 | 8.062 | 8.636 | 0.272 |
| ResNet50 | 6.539 | 7.012 | 0.733 | 6.863 | 7.532 | 0.610 | 7.902 | 9.147 | 0.235 | 8.779 | 8.668 | 0.361 | 8.424 | 9.589 | 0.018 | 8.029 | 8.402 | 0.316 |
| CLIP_RN50 | 6.327 | 9.375 | 0.579 | 6.538 | 9.442 | 0.511 | 6.775 | 9.541 | 0.332 | 7.764 | 9.127 | 0.562 | 7.861 | 9.526 | 0.218 | 7.822 | 8.655 | 0.398 |
| CLIP_RN50x4 | 6.166 | 9.473 | 0.641 | 6.383 | 9.525 | 0.573 | 6.407 | 9.518 | 0.415 | 7.435 | 8.982 | 0.681 | 7.496 | 9.388 | 0.384 | 7.729 | 8.354 | 0.504 |
