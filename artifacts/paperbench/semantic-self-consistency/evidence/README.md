---
# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_semantic_consistency.md](tables/table1_semantic_consistency.md) | Table 1, §5.1 | C01, C02 | Accuracy comparison of CPW and SCW against SC baseline and top-prob across 5 models and 3 datasets, showing delta over SC baseline in parentheses. |
| [tables/table2_outlier_detection.md](tables/table2_outlier_detection.md) | Table 2, §5.2 | C03 | Best and average accuracy of Isolation Forest, KNN, and One-class SVM outlier removal across 5 models and 3 datasets, with values >1% gain over baseline bolded. |
| [tables/table3_seq_length_bleu.md](tables/table3_seq_length_bleu.md) | Table 3, Appendix B | C05, C06 | Average sequence length, average accuracy increase (%), and average BLEU score per model-dataset pair, demonstrating positive length-accuracy correlation but no BLEU-accuracy correlation. |
| [tables/table4_accuracy_deviation.md](tables/table4_accuracy_deviation.md) | Table 4, Appendix B | C01 | Accuracy deviation (%) across models and datasets, quantifying variability in semantic method performance. |
| [tables/table5_varied_temp.md](tables/table5_varied_temp.md) | Table 5, Appendix G.1 | C01 | Comparison of baseline SC, varied-temperature SC with majority vote, and varied-temperature SC with inverse-temperature weighting on SVAMP. |
| [tables/table6_featurizer_distance.md](tables/table6_featurizer_distance.md) | Table 6, Appendix G.2 | C04 | Average inter-embedding distances for RoBERTa, MathBERT, and SciBERT on arithmetic tasks, showing domain-aligned featurizers produce tighter clusters. |
| [tables/table7_kmeans.md](tables/table7_kmeans.md) | Table 7, Appendix G.3/M | — | K-means outlier detection performance with k=2 per model and dataset, showing generally poor results compared to SC baseline. |
| [tables/table8_kmeans_avg.md](tables/table8_kmeans_avg.md) | Table 8, Appendix G.3/M | — | K-means performance averaged over 10 runs showing high volatility and generally below-baseline accuracy. |
| [tables/table9_ngram.md](tables/table9_ngram.md) | Table 9, Appendix H.2 | — | N-gram weighting accuracy (n=2) for Llama 2, Mistral, GPT-3.5 on AQuA-RAT and SVAMP, demonstrating that pure n-gram methods fail. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure2_rouge_n.md](figures/figure2_rouge_n.md) | Figure 2, Appendix H.1 | C06 | Average ROUGE-N scores for Llama 3, GPT-3.5, GPT-4o mini, Mistral, and Llama 2 7B averaged across StrategyQA, AQuA-RAT, and SVAMP, showing GPT-3.5 underperforms on ROUGE despite strong accuracy. |
