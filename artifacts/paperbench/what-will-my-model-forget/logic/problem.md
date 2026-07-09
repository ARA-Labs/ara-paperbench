# Problem Specification

## Observations

### O1: Model Refinement Causes Catastrophic Forgetting
- **Statement**: Fine-tuning a pretrained LM on even a single incorrectly predicted example (30 gradient steps) causes massive forgetting of upstream pretraining data. BART0Large shows 8.0–9.3% EM Drop Ratio; FLAN-T5Large shows 0.15–3.3% EM Drop Ratio depending on tuning strategy.
- **Evidence**: Table 3 (Vanilla FT rows), Table 4 (Vanilla FT rows)
- **Implication**: Naive model refinement is impractical for deployment due to uncontrolled forgetting of previously learned knowledge.

### O2: Random Replay Provides Partial Relief but High Variance
- **Statement**: Randomly replaying 8 upstream examples every 10 gradient steps reduces EM Drop on BART0Large from 9.274% to 5.769% (Full FT) and on FLAN-T53B from 4.384% to 1.910% (LoRA), but this is still substantially higher than replaying ground-truth forgotten examples.
- **Evidence**: Table 3 (Vanilla FT vs. Replay w/ Random rows)
- **Implication**: Random replay wastes compute on examples that would not be forgotten anyway; targeted replay should be significantly more efficient.

### O3: Logit Changes Transfer Between Examples
- **Statement**: After fine-tuning on an online learning example ⟨xi, yi⟩, the change in logit score Δf̂i(xi) for tokens in xi numerically transfers to the logit change Δf̂i(xj) for an upstream example xj, even when the two examples appear semantically unrelated (e.g., a public-relations question causing forgetting of a paraphrase-detection example).
- **Evidence**: Figure 2(a) — logit scores for tokens "not" and "duplicates" in xi change by −3.38 and −3.78; corresponding tokens in xj change by −0.26 and −0.40
- **Implication**: Forgetting has a mechanistic explanation rooted in gradient dynamics, enabling principled prediction.

### O4: Positive Examples Are a Small Minority
- **Statement**: Forgotten upstream pretraining examples constitute only 1%–10% of all upstream examples D̂PT, creating a severe class-imbalance problem for forecasting.
- **Evidence**: Section 4.2 ("Compared Methods"), Section 3.3 ("Training" in Appendix B)
- **Implication**: Forecasting models must explicitly handle class imbalance (e.g., via frequency prior or positive-pair weighting).

### O5: Ground-Truth Forgetting Identification is Computationally Expensive
- **Statement**: Obtaining ground-truth forgotten examples requires running full inference over all |D̂PT| pretraining examples with the updated model fi for every single error fixed, costing O(Fw(N)) FLOPs (9.04×10^14 FLOPs for 3,600 upstream examples under full FT).
- **Evidence**: Table 5, Table 8
- **Implication**: A forecasting model that avoids PTLM inference at prediction time is essential for practical deployment.

## Gaps

### G1: No Interpretable Framework for Understanding Example-Level Forgetting Interactions
- **Statement**: Existing work characterizes *which* examples tend to be forgotten (Toneva et al., 2018; Maini et al., 2022) but does not explain *why* learning one example causes forgetting of another.
- **Caused by**: O3 — the logit-change transfer phenomenon was previously uncharacterized.
- **Existing attempts**: Ramasesh et al. (2020) analytically study logit changes in frozen-feature models; Evron et al. (2022) analyze forgetting in linear models.
- **Why they fail**: These analyses do not apply to large-scale instruction-tuned encoder-decoder LMs and do not yield computationally efficient forecasting models.

### G2: No Computationally Efficient Forgetting Forecasting Method
- **Statement**: Inner-product-of-gradients methods (Lopez-Paz & Ranzato, 2017; Aljundi et al., 2019b) are theoretically sound but require TV backward passes to compute the full NTK, costing O(NPTTHV) even for head-only tuning.
- **Caused by**: O5 — ground-truth computation is intractable at scale.
- **Existing attempts**: MIR (Aljundi et al., 2019a) approximates forgetting by evaluating on a small subset of upstream data.
- **Why they fail**: MIR's subset approximation clearly degrades performance compared to ground-truth forgetting replay (Table 3).

### G3: Random Replay Lacks Controllability and Interpretability
- **Statement**: Practitioners cannot predict which examples will be affected by a model update, making debugging and auditability difficult.
- **Caused by**: O1, O2 — forgetting is severe and random replay does not explain what is being preserved.
- **Existing attempts**: OCS (Yoon et al., 2022) selects coresets from upstream data.
- **Why they fail**: OCS does not capture example-level interactions between the new online example and upstream examples.

## Key Insight

- **Insight**: The change in pre-softmax logit scores of an online-learned example (after one gradient step) is linearly related to the logit change in any upstream example through the Neural Tangent Kernel: Δf̂i(xj) ≈ Θ(xj, xi)Θ⁻¹(xi, xi) · Δf̂i(xi). This relationship can be *approximated* by a trainable low-rank kernel h(xj,yj)h(xi,yi)^T, enabling efficient forecasting without computing the full NTK.
- **Derived from**: O3 (logit-change transfer), with NTK theory providing the formal justification.
- **Enables**: Two forecasting approaches: (1) a partially interpretable logit-based model that predicts logit changes, and (2) a black-box representation-based model that learns a similarity function over example encodings.

## Assumptions

- A1: The pretrained LM f0 is an instruction-tuned seq2seq model (encoder-decoder) that performs multiple NLP tasks using a unified prompt format.
- A2: Model refinement involves a small number of gradient steps on a single online example (≤100 steps), so first-order Taylor expansion of logit changes is approximately valid.
- A3: The upstream pretraining data D_PT is accessible for replay (white-box access to training data).
- A4: The positive/negative structure of forgetting is sufficiently consistent across different online examples to be learnable by a forecasting model trained on D^Train_R.
