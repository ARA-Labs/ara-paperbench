# Table 10: Streaming Results
- **Source**: Table 10, Appendix E.7
- **Caption**: "Experimental results of streaming with constructed coresets. 'Noisy PermMNIST' indicates the label-noise version of PermMNIST. The best result in each case is in bold."
- **Experimental conditions**: PermMNIST streamed in batches of 125. Replay memory size: 100, number of slots: 0.0005. Networks trained for 40 gradient descent steps per batch using Adam with step size 0.0005. Implementation from Borsos et al. (2020).

| Method | PermMNIST | Noisy PermMNIST |
|--------|-----------|-----------------|
| Uniform | 69.0 | 59.4 |
| EL2N | 70.2 | 58.4 |
| GraNd | 71.7 | 63.3 |
| Influential | 70.9 | 62.4 |
| Moderate | 68.0 | 60.0 |
| CCS | 71.7 | 65.3 |
| Probabilistic | 72.1 | 64.6 |
| LBCS | 73.2 | 66.1 |

**Notes**:
- LBCS achieves the best accuracy in both clean and noisy streaming settings.
- Results differ from those reported in Zhou et al. (2022) because that work did not provide streaming code; the Borsos et al. (2020) implementation is used.
