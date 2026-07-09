# Table 4: Ablation Study on RoBERTa-base
- **Source**: Table 4, Section 5.6
- **Caption**: "Results of ablating salience-based allocation strategy and APT adapter with RoBERTa-base model, with relative training efficiency metrics to fine-tuning."

| Method | SST2 | MNLI | Train Time(⇓) | Train Mem(⇓) |
|--------|------|------|--------------|-------------|
| APT | 94.5 | 86.4 | 592.1% | 70.1% |
| w/o AP | 94.4 | 87.5 | 82.6% | 62.2% |
| w/o salience | 94.3 | 84.7 | 609.8% | 65.0% |
| w/o AT | 93.2 | 84.5 | 684.9% | 64.4% |
| w/o DS | 92.9 | 85.3 | 483.1% | 61.9% |

*Note: All efficiency metrics normalized to full fine-tuning (FT) baseline.*
*Note: w/o AP = no adaptive pruning (only adaptive tuning); inference efficiency same as FT/LoRA for this variant.*
*Note: w/o AT = static LoRA ranks during pruning.*
*Note: w/o DS = no self-distillation, only L_ft objective.*
*Note: w/o salience = uniform pruning allocation instead of salience-based ranking.*
