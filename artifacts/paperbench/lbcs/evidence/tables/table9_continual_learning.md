# Table 9: Continual Learning Results
- **Source**: Table 9, Appendix E.6
- **Caption**: "Experimental results of continual learning with constructed coresets. 'Noisy PermMNIST' indicates the label-noise version of PermMNIST. The best result in each case is in bold."
- **Experimental conditions**: PermMNIST (10 tasks, fixed random pixel permutations). Memory size: 100. Weight for previous memory: 0.01. Implementation from Borsos et al. (2020). Noisy PermMNIST: 10% symmetric label noise injected into training data.

| Method | PermMNIST | Noisy PermMNIST |
|--------|-----------|-----------------|
| Uniform | 78.1 | 65.0 |
| EL2N | 75.9 | 52.8 |
| GraNd | 77.3 | 61.8 |
| Influential | 78.8 | 64.0 |
| Moderate | 78.4 | 63.9 |
| CCS | 79.4 | 64.6 |
| Probabilistic | 79.3 | 65.5 |
| LBCS | 79.9 | 65.9 |

**Notes**:
- LBCS achieves the best accuracy in both clean and noisy continual learning settings.
- Results use the implementation from Borsos et al. (2020) since Zhou et al. (2022) did not provide code for this.
