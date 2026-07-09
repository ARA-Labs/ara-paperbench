# Concepts

## Forward-pass primitive set
The closed list of operators permitted between input tokens and output logits. The set excludes division, exponentiation, softmax, layer-norm, GELU, mean, and `where`. See `logic/problem.md` for the exhaustive list.

## Bigram prior (BiBigram)
A fixed lookup table of forward and backward token-bigram log-odds, computed once over a 50257*200 token slice of OpenWebText (`measure_unigram_loss.py:17`). At inference, the previous and next tokens are looked up via `tensor[index]`; the two log-odds tensors are averaged. Provides a strong baseline (loss 5.83) without any neural training. The mask token's row is replaced with the unigram distribution to handle masked-neighbour cases (`tao_solution.py:54-59`).

The `BiBigramMLM` class precomputes `log(p / (1-p))` (a "log-odds" rather than log-prob) **outside** the forward pass, so the forward only does indexing, addition, and a multiplication by 0.5.

## Convolutional MLM
A residual stack of 1D convolutions over the token dimension. The kernel-size-7 conv is implemented via `torch.nn.functional.pad` (allowed: it is non-numerical when constants are passed) plus `torch.as_strided` plus `torch.einsum` to sidestep `torch.nn.Conv1d`, which is not on the allow-list (`tao_solution.py:206-236`). Each block has an up-projection (`hidden * expansion` channels), a ReLU, and a down-projection, added residually.

## Inverse-stds normalisation trick
Standard normalisation needs `1/std`. Instead, the model stores a buffer `inverse_stds` of length `num_layers` and **multiplies** by it inside forward. The buffer is updated **outside** the forward pass via `update_inverse_stds()`, which divides by the running standard deviation collected during forward. This implements LayerNorm-like scale stabilisation while keeping the forward division-free (`tao_solution.py:199-203, 263, 280, 293-297`). The update uses an EMA with weight 0.99.

## Composite model: ConvMLMWithBiBigrams
The shipped model adds a learnable scalar `bigram_multiplier` (initialised to 1.0) to combine the conv-MLM logits with frozen bigram-prior logits: `logits = conv_logits + bigram_logits * bigram_multiplier`. The bigram pathway is wrapped in `torch.no_grad()` so its weights are not updated (`tao_solution.py:357-359`). Final reported loss: 4.6 (score 1.13).

## Hidden trick: training-loop division
The single use of division is `1 / torch.tensor(self.last_residual_scales)` inside `update_inverse_stds()` (`tao_solution.py:201-203, 295-297, 365-367`), which the author labels in a comment as "this division is allowed as long as it isn't called during inference, eg not called between receiving input and returning output". This is the linchpin that lets the solution use a normalisation analogue.

## Score formula and reference asymptote
`score = log(loss - 1.5)`. The 1.5 offset acts as a soft asymptote: as loss approaches 1.5 (well below GPT-2-small's typical eval loss), the score diverges to `-∞`. Halving the loss-above-asymptote roughly subtracts `log(2) ≈ 0.69` from the score.

## OpenWebText with GPT-2 tokenisation
The training and validation corpora are GPT-2-tokenised OpenWebText (vocab 50257, mask token 50256). Sequences are 128 tokens; 15% of positions per batch are replaced with the mask token in `get_batch()` (`tao_train.py:50-68`).

## n-gram statistics file format
- `unigrams.pt`: shape `(vocab_size,)`, smoothed token frequencies.
- `bigrams_forward.pt`: shape `(vocab_size, vocab_size)`, P(next | prev).
- `bigrams_backward.pt`: shape `(vocab_size, vocab_size)`, P(prev | next).
All three are saved by `measure_unigram_loss.py` (lines 41, 86) and loaded by the model classes via `torch.load`.
