---
# Table 11: Performance Under Non-I.I.D. Scenarios
- **Source**: Table 11, Section 4.4
- **Caption**: "Effectiveness of FOA under non-i.i.d. scenarios. Results obtained on ViT and ImageNet-C (level 5). For mild (i.i.d.) and online imbalanced label shift scenarios, we report the average result over 15 corruptions. For mixed shifts, the performance is evaluated on a single data stream consisting of 15 mixed corruptions."
- **Conditions**: ViT-Base (full precision, 32-bit); batch size 64; ImageNet-C severity level 5

| Method | BP? | Mild (i.i.d.) Acc. | Mild ECE | Online Label Shifts Acc. | Online Label Shifts ECE | Mixed Shifts Acc. | Mixed Shifts ECE |
|--------|-----|-------------------|----------|--------------------------|------------------------|-------------------|-----------------|
| TENT | ✓ | 59.6 | 18.5 | 60.2 | 17.7 | 56.9 | 29.2 |
| SAR | ✓ | 62.7 | 7.0 | 60.8 | 7.5 | 61.4 | 14.8 |
| FOA (ours) | ✗ | 66.3 | 3.2 | 62.1 | 6.6 | 62.0 | 4.9 |

**Notes**:
- Online imbalanced label shift: test data arrives in class order (class-sequential stream)
- Mixed domain shift: single stream of 15 randomly interleaved corruption types
- FOA maintains best accuracy and lowest ECE in both non-i.i.d. scenarios
- All methods show some degradation under non-i.i.d. vs. i.i.d. conditions
- FOA's ECE under mixed shifts (4.9%) remains substantially lower than TENT (29.2%) and SAR (14.8%)
