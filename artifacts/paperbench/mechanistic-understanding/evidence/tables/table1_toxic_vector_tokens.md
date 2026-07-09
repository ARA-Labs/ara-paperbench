# Table 1: Top Toxic Vectors Projected onto the Vocabulary Space

- **Source**: Table 1, Section 3.2
- **Caption**: "Top toxic vectors projected onto the vocabulary space. WARNING: THESE EXAMPLES ARE HIGHLY OFFENSIVE. We note that SVD.UToxic[2] has a particularly gendered nature. This arises from the dataset and language model we use."
- **Note**: Offensive tokens are partially censored as in the original paper.

| VECTOR | TOP TOKENS |
|--------|------------|
| WToxic | c*nt, f*ck, a**hole, d*ck, wh*re, holes |
| MLP.v19 (index unspecified in row 1) | sh*t, a**, cr*p, f*ck, c*nt, garbage, trash |
| MLP.v12 (index unspecified in row 2) | delusional, hypocritical, arrogant, nonsense |
| MLP.v18 (index 2669) | degener, whining, idiots, stupid, smug |
| MLP.v13 (index unspecified in row 4) | losers, filthy, disgr, gad, feces, apes, thous |
| MLP.v16 (index unspecified in row 5) | disgrace, shameful, coward, unacceptable |
| MLP.v12 (index unspecified in row 6) | f*ck, sh*t, piss, hilar, stupidity, poop |
| MLP.v19 (index 1438) | c*m, c*ck, orgasm, missionary, anal |
| SVD.UToxic[0] | a**, losers, d*ck, s*ck, balls, jack, sh*t |
| SVD.UToxic[1] | sexually, intercourse, missive, rogens, nude |
| SVD.UToxic[2] | sex, breasts, girlfriends, vagina, boobs |

**Notes**:
- The paper shows MLP layer and neuron index for some rows: MLP.v18[2669] and MLP.v19[1438] are explicitly identified.
- MLP.v19_770 is identified in Figure 2 and Section 5.2 as "one of the most toxic vectors" (highest cosine similarity with WToxic), but the corresponding row in Table 1 is MLP.v19 row 1 (sh*t, a**, ...).
- Row ordering in Table 1 corresponds to descending cosine similarity with WToxic.
