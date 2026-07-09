# Table 3: Error Prediction of OOD Datasets Across 75 Models
- **Source**: Table 3, Section 4.2
- **Caption**: "Error prediction of OOD datasets across 75 models of diverse settings measured by MAE loss ↓. We mark the best and second best method bold and underline, respectively. Despite ImageNet (ID) accuracy remaining a significant indicator of ImageNet-v2 (OOD) accuracy, the ID LCA serves as a more robust error predictor across the four diverse OOD datasets. Refer to Table 12 for detailed results of VMs-only and VLMs-only."
- **Conditions**: MAE computed from linear regression of ID metric → OOD Top-1 accuracy; 75 models total; min-max scaling for LCA

| Methods | ImgN-v2 ↓ | ImgN-S ↓ | ImgN-R ↓ | ImgN-A ↓ | ObjNet ↓ |
|---------|----------|---------|---------|---------|---------|
| ID Top1 (Miller et al., 2021) | **0.040** | 0.230 | 0.277 | 0.192 | 0.178 |
| AC (Hendrycks & Gimpel, 2017) | 0.043 | 0.124 | 0.113 | 0.324 | 0.127 |
| Aline-D (Baek et al., 2022) | 0.121 | 0.270 | 0.167 | 0.409 | 0.265 |
| Aline-S (Baek et al., 2022) | 0.072 | 0.143 | 0.201 | 0.165 | 0.131 |
| (Ours) ID LCA | 0.162 | **0.093** | _0.114_ | **0.103** | **0.048** |
