# P3 Dataset CFG–Instruction-Tuned Model Similarity Scores

- **Source**: Table 8, Appendix F
- **Caption**: "Datasets in P3 where Instruction-Tuned models were the most and least similar, in terms of top-p overlap, to CFG models. The count column shows the number of datapoints that were sampled from each dataset to calculate the overlap."
- **Conditions**: Falcon-7b-Base with CFG γ=1.5 vs Falcon-7b-Instruct; top-p=90% vocabulary overlap as similarity metric; 32,902 total P3 samples

## Highest CFG–Instruct Similarity

| P3 Dataset | Mean Top-p Overlap | Std |
|-----------|-------------------|-----|
| SuperGLUE wsc.fixed p is are r score eval | 31.89 | +/-22.06 |
| SciQ Multiple Choice Closed Book | 5.82 | +/-13.27 |
| CosE v1.11 description question option text | 5.70 | +/-9.05 |
| RottenTomatoes Writer Expressed Sentiment | 4.93 | +/-7.45 |
| WinograndeXL fill in the blank | 4.42 | +/-10.51 |
| RottenTomatoes Text Expressed Sentiment | 2.93 | +/-7.98 |
| Quarel: choose between | 2.51 | +/-12.39 |
| SuperGLUE wic GPT 3 prompt score eval | 2.15 | +/-5.94 |
| WinograndeDebiased Replace score eval | 2.02 | +/-24.46 |
| PAWS final context question (no label) | 1.37 | +/-4.81 |

## Lowest CFG–Instruct Similarity

| P3 Dataset | Mean Top-p Overlap | Std |
|-----------|-------------------|-----|
| paws labeled final paraphrase task | -11.71 | +/-11.03 |
| super glue copa more likely | -11.94 | +/-6.38 |
| piqa Does this solution make sense sol2 | -12.22 | +/-9.24 |
| super glue copa cause effect score eval | -12.82 | +/-5.8 |
| rotten tomatoes Sentiment with choices | -13.07 | +/-7.98 |
| super glue copa plausible alternatives score eval | -15.07 | +/-5.69 |
| super glue copa C1 or C2 premise so because | -15.38 | +/-6.43 |
| super glue copa more likely score eval | -16.54 | +/-5.45 |
| cos e v1.11 question option description id | -17.60 | +/-14.06 |
| rotten tomatoes Reviewer Enjoyment Yes No | -18.16 | +/-16.02 |

## Key Finding
CFG and instruction-tuned models agree most on longer, more complex, structured questions (e.g., multiple choice, closed-book QA). They agree least on open-ended, vague, conversational prompts (COPA, open sentiment). Trend: longer prompts → higher CFG/instruction-tuning agreement (Spearman rs=0.05, significant).
