# Table 4: FRE Reward Subset Ablation on AntMaze

- **Source**: Table 4, Appendix D
- **Caption**: "Full results comparing FRE agents trained on different subsets of random reward functions in AntMaze."
- **Conditions**: All agents trained on antmaze-large-diverse-v2 with identical training budgets; FRE-all receives 1/3 as many samples of each reward type as single-family agents. Scores normalized [0, 100]; mean ± std over 5 seeds, 20 episodes each.

| Eval Task | FRE-all | FRE-goals | FRE-lin | FRE-mlp | FRE-lin-mlp | FRE-goal-mlp | FRE-goal-lin |
|-----------|---------|-----------|---------|---------|-------------|--------------|--------------|
| goal-reaching | 48.8 ± 6 | 66.0 ± 4 | 6.0 ± 1 | 24.0 ± 6 | 8.0 ± 4 | 52.0 ± 6 | 54.0 ± 12 |
| directional | 55.2 ± 8 | 6.6 ± 13 | 55.5 ± 6 | −6.6 ± 14 | 47.9 ± 6 | 5.1 ± 25 | 67.1 ± 5 |
| random-simplex | 21.3 ± 4 | 23.5 ± 6 | 14.4 ± 3 | 18.5 ± 6 | 14.8 ± 4 | 19.7 ± 5 | 10.7 ± 3 |
| path-all | 63.8 ± 10 | 8.3 ± 11 | 50.5 ± 9 | 65.4 ± 5 | 58.5 ± 7 | 58.6 ± 23 | 55.8 ± 8 |
| total | 47.3 ± 7 | 26.1 ± 8 | 31.6 ± 5 | 25.3 ± 8 | 32.3 ± 5 | 33.8 ± 15 | 46.9 ± 7 |
