# Table 14: Effect of EMA in Back-to-Source Activation Shifting
- **Source**: Table 14, Appendix C
- **Caption**: "Effects of exponential moving average (EMA) (Eqn. (9)) in our Back-to-Source Activation (Act.) Shifting scheme. For Act. Shifting w/o EMA, we directly utilize the batch statistics µN(Xt) to calculate the shifting direction dt in Eqn. (8). We report the average results over 15 corruptions on ImageNet-C (severity level 5) with ViT-Base."
- **Model**: ViT-Base, full precision 32-bit
- **Dataset**: ImageNet-C severity 5, average over 15 corruptions

| Metric | Method | NoAdapt | BS=1 | BS=2 | BS=4 | BS=8 | BS=16 | BS=32 | BS=64 |
|--------|--------|---------|------|------|------|------|-------|-------|-------|
| Acc. (%, ↑) | Act. Shifting w/o EMA | 55.5 | 0.1 | 56.9 | 58.4 | 58.8 | 59.0 | 59.1 | 59.1 |
| Acc. (%, ↑) | Act. Shifting with EMA (Ours) | 55.5 | 59.0 | 59.1 | 59.1 | 59.1 | 59.1 | 59.1 | 59.2 |
| ECE (%, ↓) | Act. Shifting w/o EMA | 10.5 | 0.0 | 52.4 | 37.5 | 24.5 | 18.0 | 15.1 | 13.8 |
| ECE (%, ↓) | Act. Shifting with EMA (Ours) | 10.5 | 12.7 | 12.7 | 12.7 | 12.7 | 12.7 | 12.7 | 12.7 |
