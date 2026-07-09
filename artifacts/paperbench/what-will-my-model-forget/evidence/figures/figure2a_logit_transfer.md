# Figure 2(a): Logit Change Transfer Example
- **Source**: Figure 2(a), Section 3.2
- **Caption**: "Transfer of logit changes of first output tokens on an upstream pretraining example ⟨xj, yj⟩ when fixing prediction errors of an online learning example ⟨xi, yi⟩. After fixing the error, the logit scores of the tokens 'not' and 'duplicates' in ⟨xi, yi⟩ changes significantly, despite that their token probabilities after normalization are both close to 0. The logit change has no effect on the prediction of ⟨xi, yi⟩; however, the predictions of the upstream pretraining example ⟨xj, yj⟩ flips as the logit change partially transfers to ⟨xj, yj⟩."
- **Conditions**: FLAN-T5 model; fine-tuning on a single online example about public relations (MCQ)

## Online Learning Example (xi): 
"Which of these is NOT a type of research that could be used for the purposes of evaluation? (A)Media content analysis (B) Survey (C) Behavior study (D) Media Release"
- Original incorrect prediction: Media Release
- Target correct prediction: Behavior study

## Upstream Example (xj):
"How can you lose weight quickly? / How do I lose weight in a short time? / Pick one: These questions are 'duplicates' or 'not duplicates'."
- Original correct prediction: Duplicates
- Prediction after fine-tuning: Not duplicates (incorrect — FORGOTTEN)

## Logit Values Table

### Online Learning Example xi
| Token | Logit Before | Logit After | Change |
|-------|-------------|-------------|--------|
| Behavior | -2.56 | -1.72 | +0.84 ↑ |
| Media | -2.03 | -2.18 | -0.15 ↓ |
| Not | -6.05 | -9.43 | **-3.38 ↓** |
| Duplicates | -6.24 | -10.02 | **-3.78 ↓** |

### Upstream Pretraining Example xj
| Token | Logit Before | Logit After | Change |
|-------|-------------|-------------|--------|
| Not | -2.30 | -2.56 | -0.26 ↓ |
| Duplicates | -2.23 | -2.63 | -0.40 ↓ |

Note: Tokens "not" and "duplicates" have negligible probability in xi (far below top predictions) but their large logit decrease transfers to xj where they ARE the top-2 candidates, causing the prediction of xj to flip from "Duplicates" (correct) to "Not duplicates" (incorrect).
