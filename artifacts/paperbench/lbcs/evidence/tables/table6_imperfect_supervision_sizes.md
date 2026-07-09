# Table 6: Optimized Coreset Sizes under Imperfect Supervision
- **Source**: Table 6, Appendix E.3
- **Caption**: "Mean and standard deviation of optimized coreset sizes by our method under imperfect supervision."
- **Experimental conditions**: F-MNIST dataset, LeNet model, LBCS with ε=0.2, T=500. Experiments repeated 10 times. 30% and 50% symmetric label noise applied to training set (test set kept clean). Exponential class imbalance ratio 0.01.

| Imperfect supervision setting | k = 1000 | k = 2000 | k = 3000 | k = 4000 |
|-------------------------------|----------|----------|----------|----------|
| With 30% corrupted labels | 951.2±4.9 | 1866.1±8.3 | 2713.7±10.8 | 3675.6±17.0 |
| With 50% corrupted labels | 934.5±5.6 | 1856.5±9.1 | 2708.8±11.2 | 3668.4±14.6 |
| With class-imbalanced data | 988.4±6.7 | 1893.8±10.0 | 2762.7±14.2 | 3757.4±17.8 |

**Notes**:
- All optimized coreset sizes are strictly smaller than the predefined k values.
- Higher noise rates (50% vs 30%) lead to smaller optimized coreset sizes, consistent with the ε-compromise preventing overfitting.
- Class-imbalanced coresets are larger than noise-corrupted coresets (closer to predefined k), suggesting that imbalance is a milder form of imperfect supervision for LBCS.
