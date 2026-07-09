# Table 12: StanfordCars — Ineffective VR Case

- **Source**: Table 12, Appendix D.4
- **Caption**: "An Ineffective Case of Input Reprogramming - StanfordCars (Mean % ± Std %)"
- **Conditions**: StanfordCars dataset (196 classes of cars for fine-grained recognition); same training setup as Table 1; ILM output mapping
- **Note**: All methods fail (<10% accuracy) on this fine-grained recognition task requiring subtle appearance differences

| METHOD | RESNET-18 | RESNET-50 | VIT-B32 |
|--------|-----------|-----------|---------|
| PAD | 4.5 ±0.1 | 4.7 ±0.2 | 4.7 ±0.6 |
| NARROW | 3.6 ±0.1 | 4.7 ±0.1 | 7.7 ±0.2 |
| MEDIUM | 3.6 ±0.1 | 4.7 ±0.2 | 8.3 ±0.3 |
| FULL | 3.4 ±0.1 | 4.6 ±0.1 | 5.0 ±0.0 |
| OURS (SMM) | 2.9 ±0.2 | 3.0 ±0.6 | 4.8 ±0.9 |
