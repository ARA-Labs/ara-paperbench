# Table 6: Performance Comparison When Using Different Explanation Methods
- **Source**: Table 6, Appendix C.3
- **Caption**: "Performance comparison when using different explanation methods across four MuJoCo tasks."
- **Setup**: Fixed refining method = RICE (Ours); varied explanation method
- **Metric**: Final reward (mean ± std over 3 seeds); higher is better for Hopper, Walker2d, HalfCheetah; less negative is better for Reacher.

| Task | Random Explanation | Integrated Gradients | AIRS | Ours |
|------|--------------------|----------------------|------|------|
| Hopper | 3648.98 (39.06) | 3653.24 (14.23) | 3654.49 (8.12) | 3663.91 (20.98) |
| Walker2d | 3969.64 (6.38) | 3972.15 (4.77) | 3976.35 (2.40) | 3982.79 (3.15) |
| Reacher | -3.11 (0.42) | -2.99 (0.31) | -2.89 (0.19) | -2.66 (0.03) |
| HalfCheetah | 2132.01 (0.76) | 2132.81 (0.83) | 2133.98 (2.52) | 2138.89 (3.22) |
