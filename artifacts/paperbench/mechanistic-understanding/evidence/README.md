# Evidence Index

## Tables

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [tables/table1_toxic_vector_tokens.md](tables/table1_toxic_vector_tokens.md) | Table 1, §3.2 | C01 | Top promoted tokens (censored) for each toxic vector (W_Toxic, MLP.vToxic layers/indices, SVD.UToxic[0-2]), showing that each vector encodes a distinct toxicity dimension. |
| [tables/table2_intervention_results.md](tables/table2_intervention_results.md) | Table 2, §3.3, §5 | C02, C03 | Toxicity score, perplexity, and F1 for GPT2 (No Op), three subtraction interventions, and DPO—demonstrating DPO achieves the best toxicity reduction with minimal quality loss. |
| [tables/table3_generation_examples.md](tables/table3_generation_examples.md) | Table 3, §3.3 | C02, C03 | Top-5 next token predictions and full continuations for three toxic prompts under GPT2, GPT2−MLP.v19, and GPT2DPO—showing shift from toxic to neutral top token after intervention/DPO. |
| [tables/table4_unalignment_results.md](tables/table4_unalignment_results.md) | Table 4, §5.3 | C06 | Toxicity, perplexity, and F1 for GPT2DPO, un-aligned model (7 key vectors scaled 10×), and original GPT2—demonstrating trivial reversal of DPO alignment. |
| [tables/table5_dpo_hyperparameters.md](tables/table5_dpo_hyperparameters.md) | Table 5, Appendix D | — | DPO training hyperparameters including learning rate, optimizer, batch size, gradient norm, and beta. |
| [tables/table6_pplm_hyperparameters.md](tables/table6_pplm_hyperparameters.md) | Table 6, Appendix D | — | PPLM data generation hyperparameters including step size, gm_scale, kl_scale, and decay. |

## Figures

| File | Source | Claims | Description |
|------|--------|--------|-------------|
| [figures/figure1_logit_lens.md](figures/figure1_logit_lens.md) | Figure 1, §4 | C03 | Mean probability of token "sh*t" at each intermediate layer for GPT2 and GPT2DPO across 295 prompts—showing that MLP layers drive toxic token promotion and DPO suppresses it. |
| [figures/figure2_mean_activations.md](figures/figure2_mean_activations.md) | Figure 2, §5.2 | C03, C05 | Bar chart of mean activations for the top-5 MLP.vToxic vectors in GPT2 vs. GPT2DPO—demonstrating the drop in activation after DPO for each toxic vector. |
| [figures/figure4_residual_shift.md](figures/figure4_residual_shift.md) | Figure 4, §5.2 | C03, C05 | 2D scatter of layer-19 residual streams projected onto (mean shift direction, principal component), colored by MLP.v19_770 activation level, showing consistent linear shift from GPT2 to GPT2DPO and drop in activations. |
| [figures/figure5_cosine_similarity.md](figures/figure5_cosine_similarity.md) | Figure 5, §5.2 | C05 | Distribution of cosine similarities between δMLP.v and δx at each layer (layers 0–18), alongside mean activation distributions—showing antipodal relationship grows as layers approach layer 19. |
