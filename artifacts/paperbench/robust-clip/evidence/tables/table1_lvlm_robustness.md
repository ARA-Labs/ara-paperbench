# Table 1: Robustness of Large Vision-Language Models with Different CLIP Models
- **Source**: Table 1, Section 4.1
- **Caption**: "(Robust) performance of OpenFlamingo and LLaVA for two image captioning and visual question answering tasks. In the last column we show for each CLIP-model the average w.r.t. respective evaluation metrics, with the increase/decrease relative to the respective TeCoA model."
- **Conditions**: 500 randomly sampled images for adversarial evaluations; all available samples for clean evaluations. CIDEr score for captioning (COCO, Flickr30k); VQA accuracy for VQAv2, TextVQA. ℓ∞ perturbations at ε = 2/255 and ε = 4/255.

## OpenFlamingo 9B (OF-9B)

| VLM | Vision encoder | COCO clean | COCO 2/255 | COCO 4/255 | Flickr30k clean | Flickr30k 2/255 | Flickr30k 4/255 | TextVQA clean | TextVQA 2/255 | TextVQA 4/255 | VQAv2 clean | VQAv2 2/255 | VQAv2 4/255 | Avg clean | Avg 2/255 | Avg 4/255 |
|-----|----------------|-----------|-----------|-----------|----------------|----------------|----------------|--------------|--------------|--------------|------------|------------|------------|-----------|-----------|-----------|
| OF-9B | CLIP | 79.7 | 1.5 | 1.1 | 60.1 | 0.7 | 0.4 | 23.8 | 0.0 | 0.0 | 48.5 | 1.8 | 0.0 | 53.0 | 1.0 | 0.4 |
| OF-9B | TeCoA2 | 73.5 | 31.6 | 21.2 | 49.5 | 14.1 | 9.5 | 16.6 | 3.5 | 2.1 | 46.2 | 23.5 | 20.5 | 46.4 | 17.9 | 13.3 |
| OF-9B | FARE2 | 79.1 | 34.2 | 19.5 | 57.7 | 16.4 | 8.9 | 21.6 | 4.1 | 1.9 | 47.0 | 24.0 | 17.2 | 51.4 ↑5.0 | 19.7 ↑1.8 | 11.9 ↓1.4 |
| OF-9B | TeCoA4 | 66.9 | 28.5 | 21.6 | 40.9 | 12.0 | 10.3 | 15.4 | 2.1 | 1.8 | 44.8 | 23.6 | 21.3 | 41.9 | 16.5 | 13.7 |
| OF-9B | FARE4 | 74.1 | 30.9 | 22.8 | 51.4 | 15.7 | 10.5 | 18.6 | 3.4 | 2.9 | 46.1 | 23.6 | 21.0 | 47.5 ↑5.6 | 18.4 ↑1.9 | 14.3 ↑0.6 |

## LLaVA 1.5-7B

| VLM | Vision encoder | COCO clean | COCO 2/255 | COCO 4/255 | Flickr30k clean | Flickr30k 2/255 | Flickr30k 4/255 | TextVQA clean | TextVQA 2/255 | TextVQA 4/255 | VQAv2 clean | VQAv2 2/255 | VQAv2 4/255 | Avg clean | Avg 2/255 | Avg 4/255 |
|-----|----------------|-----------|-----------|-----------|----------------|----------------|----------------|--------------|--------------|--------------|------------|------------|------------|-----------|-----------|-----------|
| LLaVA 1.5-7B | CLIP | 115.5 | 4.0 | 3.1 | 77.5 | 1.6 | 1.0 | 37.1 | 0.5 | 0.0 | 74.5 | 2.9 | 0.0 | 76.2 | 2.25 | 1.0 |
| LLaVA 1.5-7B | TeCoA2 | 98.4 | 44.2 | 30.3 | 57.1 | 23.2 | 15.3 | 24.1 | 12.1 | 8.8 | 66.9 | 33.8 | 21.8 | 61.6 | 28.3 | 19.0 |
| LLaVA 1.5-7B | FARE2 | 109.9 | 53.6 | 31.0 | 71.1 | 29.5 | 17.5 | 31.9 | 14.7 | 9.1 | 71.7 | 34.9 | 23.0 | 71.1 ↑9.5 | 33.2 ↑4.9 | 20.1 ↑1.1 |
| LLaVA 1.5-7B | TeCoA4 | 88.3 | 50.9 | 35.3 | 48.6 | 27.9 | 19.5 | 20.7 | 12.6 | 9.3 | 63.2 | 41.0 | 31.7 | 55.2 | 33.1 | 24.0 |
| LLaVA 1.5-7B | FARE4 | 102.4 | 57.1 | 40.9 | 61.6 | 31.4 | 22.8 | 27.6 | 15.8 | 10.9 | 68.3 | 40.7 | 30.5 | 65.0 ↑9.8 | 36.2 ↑3.1 | 26.3 ↑2.3 |
