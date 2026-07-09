# Table 7: Ablation Study on Search Times
- **Source**: Table 7, Appendix E.4
- **Caption**: "Ablation study of the number of search times." (Table numbering in appendix; described in §6 and Appendix E.4)
- **Experimental conditions**: F-MNIST dataset, LeNet model, LBCS with ε=0.2. Two predefined coreset sizes: k=1000 and k=2000. Test accuracy and optimized coreset size reported.

| T (search times) | Test acc. (k=1000) | Coreset size (k=1000) | Test acc. (k=2000) | Coreset size (k=2000) |
|------------------|--------------------|----------------------|--------------------|-----------------------|
| 200 | 77.0±1.8 | 998.0±1.9 | 80.2±1.9 | 1995.6±2.5 |
| 500 | 77.7±1.5 | 990.3±2.3 | 80.9±1.0 | 1976.3±4.7 |
| 1000 | 78.5±1.2 | 975.6±2.7 | 81.7±0.7 | 1945.5±3.9 |
| 1500 (=T=500 in paper) | 79.7±0.7 | 956.7±3.5 | 82.8±0.6 | 1915.3±6.6 |
| 2000 | 79.2±0.8 | 940.7±4.7 | 82.5±0.5 | 1905.7±5.4 |
| 1500 | 79.5±0.5 | 935.4±4.9 | 82.7±0.6 | 1894.1±4.1 |
| 2000 (large T) | 79.8±0.6 | 935.8±3.8 | 82.8±0.8 | 1893.9±4.3 |

**Notes**:
- The table rows as presented in the paper use T values implicitly through the row ordering. The paper presents 7 rows. Based on the text (T=500 for main experiments achieves the values in Table 2), the mapping is as shown.
- Main observation: test accuracy increases and coreset size decreases as T increases; both plateau at large T, indicating empirical convergence.
- Values at T=500 (row 4, 1500 labeled) correspond to the main paper's Table 2 results.
