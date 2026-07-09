# Table 2: In-Domain and Out-of-Domain Generalization on BART0
- **Source**: Table 2, Section 5.1
- **Caption**: "In-domain (ID) and out-of-domain (OOD) performance of forgetting forecasting methods on BART0. We split P3-Test into in-domain and out-of-domain tasks and report performance on both splits."

| Method / Split | P3-TestID | P3-TestOOD |
|----------------|-----------|------------|
| Threshold | 60.45 | 46.24 |
| Trainable Logit | 64.15 | 30.61 |
| Representation | **75.11** | **50.12** |
| w/o Prior | 74.19 | 34.85 |

Note: P3-TestID tasks: super_glue-cb, super_glue-rte, super_glue-wsc.fixed, super_glue-copa, super_glue-wic. P3-TestOOD tasks: storycloze, hellaswag, anli, winogrande-xl. Full FT setting used.
