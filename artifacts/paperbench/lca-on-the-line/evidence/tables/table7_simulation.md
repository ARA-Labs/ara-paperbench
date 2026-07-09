# Table 7: Observation from Simulation Data with 100 Trials
- **Source**: Table 7, Appendix C
- **Caption**: "Observation from simulation data with 100 trials. The average ID test accuracy error (i.e. top 1 error) ID_Top1_Error ↓, ID test LCA distance ID_LCA_Distance ↓, and OOD test accuracy error OOD_Top1_Error ↓ for generalizable 'good' prediction model f and non-generalizable 'bad' prediction model g over 100 independent trials. Specifically, we design the data generation process as described in (1), and f is 'good' as it learns to rely on the transferable causal features supported by hierarchy; while g is 'bad' as it instead relies on the non-transferable confounding features not supported by hierarchy. In this example, ID LCA distance is a better indicator of OOD performance than ID Top1 accuracy, and model f display better generalization to OOD dataset despite lower ID Top 1 accuracy."
- **Conditions**: 4-class Gaussian mixture dataset; 10,000 samples per trial; 100 independent trials; logistic regression models; x1=causal feature (hierarchy-aligned), x2=confounding feature (non-hierarchy), x3=noise

| Model | ID Top1 Error ↓ | ID LCA Distance ↓ | OOD Top1 Error ↓ |
|-------|----------------|------------------|----------------|
| g (w. confounding feature x2) | 0.1423 | 2.000 | 0.7503 |
| f (w. transferable feature x1) | 0.3287 | 1.005 | 0.3197 |
| Diff (g - f) | +0.1864 | -0.995 | -0.4306 |
