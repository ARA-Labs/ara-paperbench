# Table 11: Comparing Ensemble Attack to Schlarmann & Hein (2023)
- **Source**: Table 11, Appendix B.7
- **Caption**: "The two types of attack are compared for the non-robust CLIP and our most robust FARE4 vision encoders with OpenFlamingo-9B. Across both perturbation strengths and for both captioning (COCO) and question answering (VQAv2) tasks our 'Ensemble' attack is much better while being significantly faster."
- **Conditions**: OpenFlamingo 9B; CLIP and FARE4 vision encoders; 200 samples from COCO and VQAv2 respectively; CIDEr for COCO, VQA accuracy for VQAv2; runtime averaged over all settings.

| Attack | Source | Runtime | COCO CLIP 2/255 | COCO CLIP 4/255 | COCO FARE4 2/255 | COCO FARE4 4/255 | VQAv2 CLIP 2/255 | VQAv2 CLIP 4/255 | VQAv2 FARE4 2/255 | VQAv2 FARE4 4/255 |
|--------|--------|---------|----------------|----------------|-----------------|-----------------|-----------------|-----------------|------------------|------------------|
| Single-precision | Schlarmann & Hein (2023) | 5h 8m | 5.7 | 2.9 | 67.9 | 55.6 | 6.9 | 6.5 | 38.0 | 29.8 |
| Ensemble | ours | 0h 40m | 1.3 | 1.1 | 30.4 | 21.7 | 4.6 | 4.1 | 26.3 | 21.4 |
