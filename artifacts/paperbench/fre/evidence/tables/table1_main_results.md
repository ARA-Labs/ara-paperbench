# Table 1: Main Zero-Shot RL Comparison

- **Source**: Table 1, Section 5.2
- **Caption**: "Offline zero-shot RL comparisons on AntMaze, ExORL, and Kitchen. FRE-conditioned policies match or outperform state-of-the-art prior methods on many standard evaluation objectives including goal-reaching, directional movement, and structured locomotion paths. FRE utilizes only 32 examples of (state, reward) pairs during evaluation, while the FB and SF methods require 5120 examples to be consistent with prior work. Results are normalized between 0 and 100."
- **Conditions**: 20 evaluation episodes per seed, 5 seeds; scores normalized [0, 100]; FRE eval K=32 samples; FB/SF eval K=5120 samples; OPAL uses privileged 10-skill online rollouts.
- **Note**: OPAL is a skill discovery method without true zero-shot capabilities; compared against a privileged version with online rollouts selecting best of 10 skills.

| Eval Task | FRE | GC-IQL | GC-BC | OPAL¹ | FB | SF |
|-----------|-----|--------|-------|-------|----|----|
| ant-goal-reaching | 48.8 ± 6 | 0.0 ± 0 | 0.4 ± 2 | 40.0 ± 14 | 12.0 ± 18 | 19.4 ± 12 |
| ant-directional | 55.2 ± 8 | 4.8 ± 14 | 6.5 ± 16 | — | — | 39.4 ± 13 |
| ant-random-simplex | 21.3 ± 4 | 9.7 ± 2 | 8.5 ± 10 | — | — | 27.3 ± 8 |
| ant-path-loop | 67.2 ± 36 | 46.6 ± 40 | 13.6 ± 16 | — | — | 44.4 ± 22 |
| ant-path-edges | 60.0 ± 17 | 23.5 ± 25 | 2.2 ± 5 | — | — | 85.0 ± 10 |
| ant-path-center | 64.4 ± 38 | 70.3 ± 37 | 39.4 ± 27 | — | — | 58.1 ± 36 |
| antmaze-all | 52.8 ± 18.2 | 25.8 ± 19.8 | 11.8 ± 12.6 | — | — | 45.6 ± 17.0 |
| exorl-walker-goals | 94 ± 2 | 58 ± 30 | 100 ± 0 | 92 ± 4 | 52 ± 18 | 88 ± 8 |
| exorl-cheetah-goals | 58 ± 8 | 1 ± 2 | 0 ± 0 | 100 ± 0 | 14 ± 6 | 0 ± 0 |
| exorl-walker-velocity | 34 ± 13 | 64 ± 1 | 38 ± 4 | — | — | 8 ± 0 |
| exorl-cheetah-velocity | 20 ± 2 | 51 ± 3 | 25 ± 3 | — | — | 17 ± 8 |
| exorl-all | 51.5 ± 6.3 | 43.4 ± 9.1 | 40.9 ± 1.9 | — | — | 28.2 ± 4.0 |
| kitchen | 66 ± 3 | 3 ± 6 | 1 ± 1 | 59 ± 4 | 35 ± 9 | 26 ± 16 |
| all | 57 ± 9 | 24 ± 12 | 18 ± 5 | — | — | 33 ± 12 |

¹ OPAL is evaluated with privileged access: 10 skills sampled online per episode, best skill selected.
