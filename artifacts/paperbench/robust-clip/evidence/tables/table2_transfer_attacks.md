# Table 2: Transfer Attacks
- **Source**: Table 2, Section 4.1
- **Caption**: "We test the transferability of adversarial COCO images (ε = 4/255) across models and report CIDEr scores. Adversarial images from OF-CLIP successfully transfer to LLaVA-CLIP and vice-versa. However, when using robust vision encoders, the transfer attack is no longer successful."
- **Conditions**: Adversarial COCO images generated at ε = 4/255 against OF-CLIP or LLaVA-CLIP; CIDEr score measured on target models with different encoders.

## Target: OF (OpenFlamingo)

| Source | Target: OF CLIP | Target: OF TeCoA2 | Target: OF FARE2 | Target: OF TeCoA4 | Target: OF FARE4 |
|--------|----------------|------------------|-----------------|------------------|-----------------|
| OF-CLIP | 1.1 | 79.0 | 85.5 | 69.9 | 79.9 |
| LLaVA-CLIP | 8.3 | 74.7 | 78.0 | 65.0 | 75.7 |

## Target: LLaVA

| Source | Target: LLaVA CLIP | Target: LLaVA TeCoA2 | Target: LLaVA FARE2 | Target: LLaVA TeCoA4 | Target: LLaVA FARE4 |
|--------|-------------------|---------------------|--------------------|--------------------|---------------------|
| OF-CLIP | 25.5 | 102.5 | 115.9 | 93.5 | 108.8 |
| LLaVA-CLIP | 3.1 | 105.7 | 115.5 | 95.7 | 105.3 |
