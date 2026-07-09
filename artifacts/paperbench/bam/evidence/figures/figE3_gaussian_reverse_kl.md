# Figure E.3: Gaussian Targets — Reverse KL Divergence
- **Source**: Figure E.3, Appendix E.3
- **Caption**: "Gaussian targets of increasing dimension. Solid curves indicate the mean over 10 runs (transparent curves). ADVI, Score, Fisher, and GSM use batch size of 2. The batch size for BaM is given in the legend."

## Experimental Conditions
- Same setup as Figure 5.1 (Section 5.1)
- Metric: Reverse KL divergence KL(q_t; p) vs. number of gradient evaluations
- Configurations:
  - D=4: BaM-5, BaM-2; D=16: BaM-15, BaM-2; D=64: BaM-40, BaM-2; D=256: BaM-150, BaM-2
  - ADVI, Score, Fisher, GSM all at B=2

## Qualitative Findings (from paper text)
- "We observe largely the same conclusions as with the forward KL divergence presented in Section 5."
- BaM with large batch size converges orders of magnitude faster in gradient evaluations
- GSM competitive with BaM at B=2; BaM at larger B outperforms
- Gradient-based methods (ADVI, Score, Fisher) similar to each other

Note: Reverse KL results corroborate forward KL findings; consistent story across both directions.
