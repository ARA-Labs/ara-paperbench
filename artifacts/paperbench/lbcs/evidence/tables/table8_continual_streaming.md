# Tables 9–10 (Appendix E.6–E.7): Continual Learning and Streaming
- **Source**: Appendix Tables 9 and 10, Appendix E.6–E.7
- **Caption (Table 9)**: "Experimental results of continual learning with constructed coresets. 'Noisy PermMNIST' indicates the label-noise version of PermMNIST. The best result in each case is in bold."
- **Caption (Table 10)**: "Experimental results of streaming with constructed coresets. 'Noisy PermMNIST' indicates the label-noise version of PermMNIST. The best result in each case is in bold."
- **Conditions**: PermMNIST (10 tasks, pixel permutation); memory size=100; weight for previous memory=0.01; 10% symmetric label noise for noisy version. Streaming: batch size=125, slots=0.0005, Adam step=0.0005, 40 gradient steps per batch; implementation follows Borsos et al. (2020).

## Table 9: Continual Learning (PermMNIST)

| Method | PermMNIST | Noisy PermMNIST |
|--------|-----------|----------------|
| Uniform | 78.1 | 65.0 |
| EL2N | 75.9 | 52.8 |
| GraNd | 77.3 | 61.8 |
| Influential | 78.8 | 64.0 |
| Moderate | 78.4 | 63.9 |
| CCS | 79.4 | 64.6 |
| Probabilistic | 79.3 | 65.5 |
| **LBCS (ours)** | **79.9** | **65.9** |

## Table 10: Streaming (PermMNIST)

| Method | PermMNIST | Noisy PermMNIST |
|--------|-----------|----------------|
| Uniform | 69.0 | 59.4 |
| EL2N | 70.2 | 58.4 |
| GraNd | 71.7 | 63.3 |
| Influential | 70.9 | 62.4 |
| Moderate | 68.0 | 60.0 |
| CCS | 71.7 | 65.3 |
| Probabilistic | 72.1 | 64.6 |
| **LBCS (ours)** | **73.2** | **66.1** |
