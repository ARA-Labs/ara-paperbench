# Heuristics

## H01: Spectral normalization on the energy model
- **Rationale**: Energy-based models (EBMs) trained with NCE can produce arbitrarily sharp gradients, causing training instability and divergence. Spectral normalization controls the Lipschitz constant of $g_\theta$, ensuring gradient magnitudes remain bounded.
- **Sensitivity**: high
- **Bounds**: Applied to the final linear classification layer of the adapter; spectral norm is constrained to ≤1 by normalizing by the largest singular value at each step.
- **Code ref**: [src/execution/ebm_adapter.py]
- **Source**: §3.2; Du & Mordatch (2019)

## H02: Beam size k=3 as default
- **Rationale**: k=3 balances exploration (more candidate chains retain better solutions) against API cost (each step requires k×n LLM calls). Increasing to k=5 yields +2.41% average accuracy gain over k=1 but increases inference cost proportionally.
- **Sensitivity**: medium
- **Bounds**: k ∈ {1, 3, 5} evaluated; k=3 is the default. Single-step variant uses k=1 effectively.
- **Code ref**: [src/execution/ebm_adapter.py]
- **Source**: §4.6, Figure 3(a)

## H03: Learning rate η=5e-6 for AdamW
- **Rationale**: Very small learning rate prevents catastrophic forgetting of pretrained DeBERTa/BERT representations while allowing fine-tuning on the task-specific NCE objective. Larger learning rates destabilize the energy function.
- **Sensitivity**: high
- **Bounds**: Set to 5e-6; weight decay 0.01; AdamW optimizer.
- **Code ref**: [src/execution/ebm_adapter.py]
- **Source**: Appendix H.2

## H04: Temperature=1.0 for LLM proposal generation
- **Rationale**: Temperature 1.0 maintains diversity in generated candidates, which is essential for effective beam search and for obtaining varied negative samples. Temperature 0 (greedy) would collapse all beams to the same output, defeating the purpose.
- **Sensitivity**: medium
- **Bounds**: Temperature=1.0 for all LLM generation during adaptation and inference. Temperature=0 is used only for Azure-SFT evaluation to reduce variance.
- **Code ref**: [src/execution/online_adaptation.py]
- **Source**: Appendix H.2

## H05: Online iteration count T=3 as sweet spot
- **Rationale**: Performance improves from T=0 (worse than base) through T=1,2,3 with diminishing returns by T=4. Three iterations provide sufficient self-improvement without excessive LLM API costs from iterative sampling.
- **Sensitivity**: medium
- **Bounds**: T ∈ {0,1,2,3,4} evaluated on StrategyQA. Performance plateau observed around T=3. T=0 adapter actually hurts performance (misguided beam search).
- **Code ref**: [src/execution/online_adaptation.py]
- **Source**: §4.6, Figure 3(b)

## H06: Training steps=6000 and batch size=64
- **Rationale**: 6000 steps at batch size 64 is sufficient to converge the adapter on datasets of 229–7473 training samples. The NCE loss with dynamic positive/negative sets requires more steps than standard supervised fine-tuning to fully converge.
- **Sensitivity**: low
- **Bounds**: 6000 steps default; batch size 64; max generation length 512 tokens.
- **Code ref**: [src/configs/training.md, src/execution/ebm_adapter.py]
- **Source**: Appendix H.2
