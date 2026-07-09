# Table 12: Targeted Attacks with Only 500 Iterations
- **Source**: Table 12, Appendix B.9
- **Caption**: "We run the targeted attacks of Table 3 for 500 iterations (instead of 10,000) and observe that this attack is considerably weaker for ε = 2/255."
- **Conditions**: LLaVA-1.5 7B with original CLIP vision encoder; APGD targeted attack with 500 iterations (vs 10,000 in main paper); ε ∈ {2/255, 4/255}.

| Target | ε = 2/255 | ε = 4/255 |
|--------|----------|----------|
| EmailAPI(to=<target(…) | 7 / 25 | 25 / 25 |
| Vaccines are dangerous. (…) | 11 / 25 | 25 / 25 |
| You are too stupid. I (…) | 25 / 25 | 25 / 25 |
| Sell your stocks. (…) | 19 / 25 | 25 / 25 |
| Visit https://tinyurl.com/(…) | 14 / 25 | 25 / 25 |
| A person suffers (…) | 13 / 25 | 25 / 25 |
| **Mean success rate** | **59.3%** | **100%** |
