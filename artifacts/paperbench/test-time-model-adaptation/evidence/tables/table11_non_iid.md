---
# Table 11: Non-i.i.d. Scenario Results

**Source**: Table 11, §4.4
**Claims**: C07
**Description**: Accuracy (%) and ECE (%) under mild (i.i.d.) and non-i.i.d. scenarios. ViT-Base (32-bit), ImageNet-C level 5.

| Method | BP? | Mild (i.i.d.) Acc | Mild ECE | Online Label Shifts Acc | Online Label Shifts ECE | Mixed Shifts Acc | Mixed Shifts ECE |
|---|---|---|---|---|---|---|---|
| TENT | Yes | 59.6 | 18.5 | 60.2 | 17.7 | 56.9 | 29.2 |
| SAR | Yes | 62.7 | 7.0 | 60.8 | 7.5 | 61.4 | 14.8 |
| FOA (ours) | No | **66.3** | **3.2** | **62.1** | **6.6** | **62.0** | **4.9** |

Notes:
- Mild (i.i.d.): average over 15 corruptions with shuffled test data (standard protocol)
- Online imbalanced label shift: test data in class order (consecutive samples from each class)
- Mixed shifts: single data stream of 15 randomly mixed corruptions
- FOA shows performance degradation under non-i.i.d. (66.3% → 62.1%/62.0%) but maintains best performance
- All methods show some degradation under non-i.i.d., but FOA's degradation is bounded
