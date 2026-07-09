# Table 6 (Appendix E.3): Optimized Coreset Sizes Under Imperfect Supervision
- **Source**: Appendix Table 6, Appendix E.3
- **Caption**: "Mean and standard deviation of optimized coreset sizes by our method under imperfect supervision."
- **Conditions**: F-MNIST with imperfect supervision; LeNet proxy + LeNet evaluation; ε=0.2; T=500; k∈{1000,2000,3000,4000}.

| Imperfect supervision condition | k=1000 | k=2000 | k=3000 | k=4000 |
|--------------------------------|--------|--------|--------|--------|
| With 30% corrupted labels | 951.2±4.9 | 1866.1±8.3 | 2713.7±10.8 | 3675.6±17.0 |
| With 50% corrupted labels | 934.5±5.6 | 1856.5±9.1 | 2708.8±11.2 | 3668.4±14.6 |
| With class-imbalanced data | 988.4±6.7 | 1893.8±10.0 | 2762.7±14.2 | 3757.4±17.8 |
