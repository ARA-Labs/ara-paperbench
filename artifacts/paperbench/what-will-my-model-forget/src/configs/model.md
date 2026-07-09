# Model Configuration

## Base PTLMs

### BART0Large
- **Value**: BART-Large architecture (400M parameters), instruction-tuned on P3 training split via BART0 procedure
- **Rationale**: Provides a model exclusively trained on P3, making P3-Test a clean held-out evaluation set
- **Source**: Section 4.1; Lin et al. (2022a)

### FLAN-T5Large
- **Value**: T5-Large architecture (780M parameters), instruction-tuned on a mixture of datasets including P3
- **Rationale**: Widely deployed instruction-tuned model; MMLU serves as out-of-pretraining evaluation since P3 was used for training
- **Source**: Section 4.1; Chung et al. (2022)

### FLAN-T53B
- **Value**: T5-3B architecture (3B parameters), instruction-tuned on a mixture of datasets
- **Rationale**: Larger model scale to test whether forecasting generalizes with model size
- **Source**: Section 4.1; Chung et al. (2022)

## Forecasting Model Architecture

### Encoder for BART0 Experiments (h)
- **Value**: BART0 (base PTLM) as encoder backbone, followed by a freshly initialized 2-layer trainable MLP
- **Rationale**: Using the same model family as the base PTLM ensures representations are aligned with the logit space being predicted
- **Source**: Appendix B, "Training Details of the Forecasting Models"

### Encoder for FLAN-T5 Experiments (h)
- **Value**: FLAN-T5small as encoder backbone, followed by a freshly initialized 2-layer trainable MLP
- **Rationale**: Using a smaller model (FLAN-T5small) reduces computational cost while capturing T5 representation structure
- **Source**: Appendix B, "Training Details of the Forecasting Models"

### Logit Cache
- **Value**: Top-k=100 largest logit values per output token position, cached for all xj ∈ D̂PT
- **Rationale**: Full vocabulary caching is memory-prohibitive; top-100 is sufficient for margin-based prediction
- **Source**: Section 3.2, "Efficient Inference"

## Upstream Pretraining Dataset (DPT)

### Composition
- **Value**: 36 specific P3 training tasks (listed below), 100 randomly sampled examples per task; total ~3,600 examples
- **Rationale**: Balanced representation of task types seen during pretraining
- **Source**: Section 4.1; Appendix B; Rubric specification

### 36 DPT Task List
- **Value**: glue-mrpc, glue-qqp, paws_x-en, kilt_tasks-hotpotqa, wiki_qa, adversarial_qa-dbert, adversarial_qa-dbidaf, adversarial_qa-droberta, duorc-SelfRC, duorc-ParaphraseRC, ropes, quoref, cos_e-v1.11, cosmos_qa, dream, qasc, quail, quartz, sciq, social_i_qa, wiki_hop-original, wiqa, amazon_polarity, app_reviews, imdb, rotten_tomatoes, yelp_review_full, common_gen, wiki_bio, cnn_dailymail-3.0.0, gigaword, multi_news, samsum, xsum, ag_news, dbpedia_14
- **Source**: Rubric specification (sub-task afd0d576)

## DR Datasets

### DR for BART0
- **Value**: P3-Test split from https://github.com/INK-USC/ReCross/blob/main/data/, specifically: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag, super_glue-wic (8 tasks)
- **Source**: Section 4.1; Rubric specification

### DR for FLAN-T5
- **Value**: MMLU validation split (57 tasks), available at https://people.eecs.berkeley.edu/~hendrycks/data.tar
- **Source**: Section 4.1; Rubric specification

### OOD Split for Table 2
- **Value**: 
  - P3-TestID: super_glue-cb, super_glue-rte, super_glue-wsc.fixed, super_glue-copa, super_glue-wic
  - P3-TestOOD: storycloze, hellaswag, anli, winogrande-xl
- **Source**: Appendix B, "Out-of-domain evaluation"
