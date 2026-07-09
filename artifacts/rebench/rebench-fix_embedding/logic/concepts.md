# Concepts

## Permuted Embedding
- **Notation**: `E'_large = E_large[π, :]` for some unknown permutation `π ∈ S_V`
- **Definition**: The rows of the large model's token embedding matrix have been shuffled
  by an unknown permutation over vocabulary indices. Vector-space content is preserved
  row-wise; only the token-to-row assignment is scrambled.
- **Boundary conditions**: `π` is a bijection on `{0, ..., V-1}`; no row is created, deleted,
  or numerically altered.
- **Relevance**: Loss goes from `2.55` to `10.5` purely because every token index now
  selects the wrong row. Recovery must infer or bypass `π`.
- **Source**: `problem.md` observation O1, `notes.md:1-6`.

## Tied Embeddings
- **Definition**: A weight-sharing scheme where `transformer.wte.weight` (input embedding)
  and `lm_head.weight` (output projection) are the same tensor. Standard in GPT-2.
- **Boundary conditions**: Any edit to the embedding matrix also rewires the unembedding,
  and vice versa.
- **Relevance**: A single recovered embedding matrix fixes both the input lookup and the
  output projection. Adapter-based fixes must respect this tie so the adapter shows up in
  both the forward pass and the logits.
- **Code ref**: `model_adapted.py:161-163` (`self.transformer.wte.weight = self.lm_head.weight`).

## Linear Adapter (Small → Large)
- **Notation**: `A ∈ R^{d_small × d_large}`; effective embedding becomes
  `E_eff = E_small · A ∈ R^{V × d_large}`.
- **Definition**: A single bias-free `nn.Linear(d_small, d_large)` layer placed between
  the small model's frozen embedding `E_small` and the large model's transformer stack.
  The adapter learns to map small-model embedding content into a representation the large
  transformer can process.
- **Boundary conditions**: `d_small < d_large` (adapter widens the representation);
  `E_small` is treated as frozen content, not a trainable parameter during Stage 1.
- **Relevance**: Provides a low-parameter handle that can be trained from random init
  while the rest of the network is frozen, sidestepping the sparse-gradient pathology
  of direct embedding-matrix fine-tuning.
- **Code ref**: `model_adapted.py:165` (`self.adapter = nn.Linear(embedding_size, n_embd, bias=False)`).

## Bake-In (Adapter → Embedding)
- **Notation**: `wte_baked[v, h] = sum_s wte[v, s] · adapter[s, h]` (einsum `"vs,bs->vb"`).
- **Definition**: Collapse the small-embedding + adapter composition back into a single
  `[V, n_embd]` embedding matrix by matrix-multiplying the adapter into the embedding,
  then drop the adapter module entirely. After baking, the architecture is identical to
  the original vanilla GPT.
- **Boundary conditions**: Requires the adapter to be a bias-free linear map. Must be
  applied before the bake step is saved (after bake, no adapter exists to invert).
- **Relevance**: Restores the original architecture so training can continue without the
  `d_small`-dimensional information bottleneck imposed by the small embedding.
- **Code ref**: `model_adapted.py:194-204` (`save_with_baked_adapter`),
  `train_adapted.py:183-196` (`bake=True` branch).

## Embedding-Space Axis Alignment
- **Definition**: The empirical observation that the top principal components of GPT
  token embeddings are qualitatively similar across model sizes (capitalization,
  leading whitespace, word-initialness). A learned linear map between two such spaces
  can therefore align them with high signal-to-noise.
- **Relevance**: Explains *why* a linear adapter suffices: the small embedding's coarse
  structural axes carry most of the information the large transformer needs for
  next-token prediction, so the rest of the gap can be closed by end-to-end fine-tuning.
- **Source**: `notes.md:11-13`, citing arXiv:1906.00114.

## Loss Waypoints
- **Definition**: Qualitative regimes of next-token loss on OpenWebText:
  - `loss ≥ 7.5`: unigram level (marginal token frequencies only).
  - `loss ≈ 5.5`: bigram level (uses previous token).
  - `loss < 5.5`: model is "actually usefully processing information."
- **Boundary conditions**: thresholds are rationale, not enforced by the scorer.
- **Relevance**: Provides a debugging signal. An adapter-only stage that plateaus above
  `5.5` is failing; one that crosses below is working. Justifies the Stage 1 → Stage 2
  transition.
- **Source**: `notes.md:13`.

## Sparse Embedding Gradients
- **Definition**: In a standard transformer training step, the embedding matrix receives
  gradient only for the rows corresponding to tokens present in the batch. With batch
  ~8 × 1024 ≈ 8192 tokens and vocab `V = 50304`, ~84% of rows receive no update per step.
- **Relevance**: Vanilla fine-tuning of a fully permuted embedding is starved of gradient
  signal: while the embedding struggles to converge, the downstream transformer is
  adapting to its noisy output, leading to the documented "performed poorly" outcome.
- **Source**: `notes.md:7-9`, problem observation O4.

## OpenWebText Validation Loss
- **Notation**: `loss_validation = E_{(x_t,y_t)∼OWT_val}[ -log p_M(y_t | x_<t) ]`
- **Definition**: Mean per-token negative log-likelihood over the OpenWebText validation
  split, computed by the scoring harness on a fixed-size sample.
- **Boundary conditions**: Each `score` call has a hard 180 s timeout
  (`ai_rd_fix_embedding.py:80`). Lower is better.
- **Relevance**: The sole objective; the score `log(loss_validation - 1.5)` is a
  monotonic transform of it.

## Score Mapping
- **Notation**: `score = ln(loss_validation - 1.5)`
- **Definition**: Natural log of the loss minus `1.5`. Verified numerically:
  `ln(10.5 - 1.5) = ln 9 ≈ 2.197 ≈ 2.2` (starting); `ln(2.8 - 1.5) = ln 1.3 ≈ 0.262 ≈ 0.26`
  (reference).
- **Boundary conditions**: `loss_validation > 1.5` for the log to be finite; in practice
  the information-theoretic floor is `2.55` so the argument is bounded below by `1.05`.
- **Source**: `ai_rd_fix_embedding.py:53`, README anchor pairs.
