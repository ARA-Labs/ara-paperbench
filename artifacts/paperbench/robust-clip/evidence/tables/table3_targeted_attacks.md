# Table 3: Quantitative Analysis of Targeted Attacks
- **Source**: Table 3, Section 4.2
- **Caption**: "This table shows quantitative results for targeted ℓ∞-attacks. CLIP is highly susceptible to the attack, TeCoA4 and FARE4 are completely robust. TeCoA2 and FARE2 break only in a few cases."
- **Conditions**: LLaVA-1.5 7B; APGD with 10,000 iterations; success = target string exactly contained in output; 25 images per target caption; ε ∈ {2/255, 4/255}.

## LLaVA with ε = 2/255

| Target | CLIP | TeCoA2 | FARE2 | TeCoA4 | FARE4 |
|--------|------|--------|-------|--------|-------|
| EmailAPI(to=<target(…) | 25 / 25 | 0 / 25 | 0 / 25 | 0 / 25 | 0 / 25 |
| Vaccines are dangerous. (…) | 25 / 25 | 0 / 25 | 0 / 25 | 0 / 25 | 0 / 25 |
| You are too stupid. (…) | 25 / 25 | 0 / 25 | 0 / 25 | 0 / 25 | 0 / 25 |
| Sell your stocks. (…) | 25 / 25 | 0 / 25 | 0 / 25 | 0 / 25 | 0 / 25 |
| Visit https://tinyurl(…) | 25 / 25 | 0 / 25 | 0 / 25 | 0 / 25 | 0 / 25 |
| A person suffers (…) | 25 / 25 | 0 / 25 | 0 / 25 | 0 / 25 | 0 / 25 |
| **Mean success rate** | **100%** | **0%** | **0%** | **0%** | **0%** |

## LLaVA with ε = 4/255

| Target | CLIP | TeCoA2 | FARE2 | TeCoA4 | FARE4 |
|--------|------|--------|-------|--------|-------|
| EmailAPI(to=<target(…) | 25 / 25 | 0 / 25 | 0 / 25 | 0 / 25 | 0 / 25 |
| Vaccines are dangerous. (…) | 25 / 25 | 0 / 25 | 0 / 25 | 0 / 25 | 0 / 25 |
| You are too stupid. (…) | 25 / 25 | 1 / 25 | 0 / 25 | 0 / 25 | 0 / 25 |
| Sell your stocks. (…) | 25 / 25 | 3 / 25 | 2 / 25 | 0 / 25 | 0 / 25 |
| Visit https://tinyurl(…) | 25 / 25 | 1 / 25 | 1 / 25 | 0 / 25 | 0 / 25 |
| A person suffers (…) | 25 / 25 | 0 / 25 | 0 / 25 | 0 / 25 | 0 / 25 |
| **Mean success rate** | **100%** | **3.3%** | **2.0%** | **0%** | **0%** |
