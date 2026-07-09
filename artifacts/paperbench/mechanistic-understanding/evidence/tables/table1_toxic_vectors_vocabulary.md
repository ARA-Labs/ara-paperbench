# Table 1: Top Toxic Vectors Projected onto Vocabulary Space

- **Source**: Table 1, Section 3.2
- **Caption**: "Top toxic vectors projected onto the vocabulary space. WARNING: THESE EXAMPLES ARE HIGHLY OFFENSIVE. We note that SVD.UToxic[2] has a particularly gendered nature. This arises from the dataset and language model we use."

| Vector | Layer | Index | Top Tokens |
|--------|-------|-------|------------|
| WToxic | — | — | c\*nt, f\*ck, a\*\*hole, d\*ck, wh\*re, holes |
| MLP.vToxic | 19 | (unlabeled) | sh\*t, a\*\*, cr\*p, f\*ck, c\*nt, garbage, trash |
| MLP.vToxic | 12 | (unlabeled) | delusional, hypocritical, arrogant, nonsense |
| MLP.vToxic | 18 | 2669 | degener, whining, idiots, stupid, smug |
| MLP.vToxic | 13 | (unlabeled) | losers, filthy, disgr, gad, feces, apes, thous |
| MLP.vToxic | 16 | (unlabeled) | disgrace, shameful, coward, unacceptable |
| MLP.vToxic | 12 | (unlabeled) | f\*ck, sh\*t, piss, hilar, stupidity, poop |
| MLP.vToxic | 19 | 1438 | c\*m, c\*ck, orgasm, missionary, anal |
| SVD.UToxic[0] | — | — | a\*\*, losers, d\*ck, s\*ck, balls, jack, sh\*t |
| SVD.UToxic[1] | — | — | sexually, intercourse, missive, rogens, nude |
| SVD.UToxic[2] | — | — | sex, breasts, girlfriends, vagina, boobs |

**Notes**:
- MLP.vToxic vectors are identified by layer and index where specified in the paper. Several entries show layer only (ambiguous index in original table).
- Tokens are partially censored as in original paper.
- SVD.UToxic[2] has gendered content arising from dataset/model biases.
