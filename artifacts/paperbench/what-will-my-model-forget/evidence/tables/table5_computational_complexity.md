# Table 5: Computational Complexity of Forecasting Methods
- **Source**: Table 5, Section 5.3
- **Caption**: "Computational complexity of forecasting methods and obtaining ground truth forgetting by running inference with updated LMs when only fine-tuning the LM head or the entire model (Full FT)."

**Notation**: N_PT = number of upstream pretraining examples (3,600 in experiments); T = max output length; H = feature dimension of sentence representations; V = vocabulary size; F_w(N) = cost of running model inference with N examples.

| Method / Setup | Head Fine-Tuning | Full Fine-Tuning |
|----------------|-----------------|-----------------|
| Threshold | O(N_PT) | O(N_PT) |
| Trainable Logit | O(N_PT · T^2 · (H + V)) | O(N_PT · T^2 · (H + V)) |
| Representation | O(N_PT · H) | O(N_PT · H) |
| Ground Truth | O(N_PT · T · H · V) | O(F_w(N_PT)) |
