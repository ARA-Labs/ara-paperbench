# Table 5: Computational Complexity of Forecasting Methods
- **Source**: Table 5, Section 5.3
- **Caption**: "Computational complexity of forecasting methods and obtaining ground truth forgetting by running inference with updated LMs when only fine-tuning the LM head or the entire model (Full FT)."
- **Notation**: NPT = number of upstream pretraining examples; T = max output length; H = feature dimension; V = vocabulary size; Fw(N) = cost of LM inference on N examples

| Method / Setup | Head | Full FT |
|----------------|------|---------|
| Threshold | O(NPT) | O(NPT) |
| Trainable Logit | O(NPTT²(H + V)) | O(NPTT²(H + V)) |
| Representation | O(NPTH) | O(NPTH) |
| Ground Truth | O(NPTTHV) | O(Fw(N)) |
