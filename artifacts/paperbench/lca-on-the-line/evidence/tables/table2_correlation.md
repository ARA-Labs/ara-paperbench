# Table 2: Correlation Measurement by R² and PEA
- **Source**: Table 2, Section 4.1
- **Caption**: "Correlation measurement by R² and PEA of ID LCA/Top1 with OOD Top1/Top5 across 75 models (36 VMs and 39 VLMs) as shown in Figure 5. We demonstrate that LCA has a strong correlation with OOD performance on all listed datasets (except ImageNet-v2). We take the absolute value of all correlations for simplicity. Full table containing results of VMs-only and VLMs-only in Table 11. Measurements from the KEN and SPE show a similar trend as seen in Section F."
- **Conditions**: 75 models (36 VMs + 39 VLMs); ID dataset = ImageNet; min-max scaling applied to LCA

| Element | OOD | ImgN-v2 R² | ImgN-v2 PEA | ImgN-S R² | ImgN-S PEA | ImgN-R R² | ImgN-R PEA | ImgN-A R² | ImgN-A PEA | ObjNet R² | ObjNet PEA |
|---------|-----|------------|------------|----------|----------|----------|----------|----------|----------|----------|----------|
| Top1 | Top1 | 0.962 | 0.980 | 0.075 | 0.275 | 0.020 | 0.140 | 0.009 | 0.094 | 0.273 | 0.522 |
| LCA | Top1 | 0.339 | 0.582 | 0.816 | 0.903 | 0.779 | 0.883 | 0.704 | 0.839 | 0.915 | 0.956 |
| Top1 | Top5 | 0.889 | 0.943 | 0.052 | 0.229 | 0.004 | 0.060 | 0.013 | 0.115 | 0.262 | 0.512 |
| LCA | Top5 | 0.445 | 0.667 | 0.811 | 0.901 | 0.738 | 0.859 | 0.799 | 0.894 | 0.924 | 0.961 |
