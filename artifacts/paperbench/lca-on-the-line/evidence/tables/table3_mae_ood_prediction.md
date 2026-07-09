---
# Table 3: Error Prediction of OOD Datasets Measured by MAE (75 Models)
- **Source**: Table 3, Section 4.2
- **Caption**: "Error prediction of OOD datasets across 75 models of diverse settings measured by MAE loss ↓. We mark the best and second best method bold and underline, respectively. Despite ImageNet (ID) accuracy remaining a significant indicator of ImageNet-v2 (OOD) accuracy, the ID LCA serves as a more robust error predictor across the four diverse OOD datasets."
- **Conditions**: 75 models (36 VMs + 39 VLMs); min-max scaling applied (not probit transform); lower MAE = better prediction

| Methods | ImgN-v2 MAE ↓ | ImgN-S MAE ↓ | ImgN-R MAE ↓ | ImgN-A MAE ↓ | ObjNet MAE ↓ |
|---------|--------------|-------------|-------------|-------------|-------------|
| ID Top1 (Miller et al., 2021) | **0.040** | 0.230 | 0.277 | 0.192 | 0.178 |
| AC (Hendrycks & Gimpel, 2017) | 0.043 | 0.124 | 0.113 | 0.324 | 0.127 |
| Aline-D (Baek et al., 2022) | 0.121 | 0.270 | 0.167 | 0.409 | 0.265 |
| Aline-S (Baek et al., 2022) | 0.072 | 0.143 | 0.201 | 0.165 | 0.131 |
| (Ours) ID LCA | 0.162 | **0.093** | **0.114** | **0.103** | **0.048** |
