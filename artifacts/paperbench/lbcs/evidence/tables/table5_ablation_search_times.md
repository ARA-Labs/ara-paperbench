# Table 7 (Appendix E.4): Ablation on Search Times
- **Source**: Appendix Table 7 (referenced as Table in §6 "Ablation on Search Times"), Appendix E.4
- **Caption**: "Ablation study of the number of search times." (search time T = number of outer loop iterations)
- **Conditions**: F-MNIST; LeNet proxy + LeNet evaluation; Adam lr=0.001; ε=0.2; k∈{1000,2000}; NVIDIA GTX3090.

| T | k=1000 Test acc. | k=1000 Coreset size (ours) | k=2000 Test acc. | k=2000 Coreset size (ours) |
|---|-----------------|---------------------------|-----------------|---------------------------|
| 100 | 77.0±1.8 | 998.0±1.9 | 80.2±1.9 | 1995.6±2.5 |
| 200 | 77.7±1.5 | 990.3±2.3 | 80.9±1.0 | 1976.3±4.7 |
| 300 | 78.5±1.2 | 975.6±2.7 | 81.7±0.7 | 1945.5±3.9 |
| 500 | 79.7±0.7 | 956.7±3.5 | 82.8±0.6 | 1915.3±6.6 |
| 800 | 79.2±0.8 | 940.7±4.7 | 82.5±0.5 | 1905.7±5.4 |
| 1500 | 79.5±0.5 | 935.4±4.9 | 82.7±0.6 | 1894.1±4.1 |
| 2000 | 79.8±0.6 | 935.8±3.8 | 82.8±0.8 | 1893.9±4.3 |
