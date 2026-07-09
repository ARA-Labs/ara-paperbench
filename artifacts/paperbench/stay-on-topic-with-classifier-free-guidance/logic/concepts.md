---
# Key Concepts

## Classifier-Free Guidance (CFG)
- **Notation**: $\hat{P}_\theta(w_i | w_{j<i}, c) \propto P_\theta(w_i | w_{j<i}, c)^\gamma \cdot P_\theta(w_i | w_{j<i})^{\gamma-1}$
- **Definition**: An inference-time technique that upweights conditional generation relative to unconditional generation in logit space. At each decoding step i, the guided log-probability is: $\log \hat{P}_\theta(w_i | w_{j<i}, c) = \log P_\theta(w_i | w_{j<i}) + \gamma \left( \log P_\theta(w_i | w_{j<i}, c) - \log P_\theta(w_i | w_{j<i}) \right)$
- **Boundary conditions**: γ=0 reduces to unconditional generation; γ=1 reduces to standard conditional generation; γ>1 overemphasizes conditioning, improving adherence at the cost of diversity. Optimal γ is task-dependent.
- **Related concepts**: Guidance Strength, Unconditional Distribution, Negative Prompting, Logit Distribution

## Guidance Strength (γ)
- **Notation**: $\gamma \in \mathbb{R}_{\geq 0}$
- **Definition**: A scalar hyperparameter controlling how strongly the model's generation is steered toward the conditioning prompt c. Higher values increase prompt adherence; excessively high values degrade quality.
- **Boundary conditions**: γ=1 is the baseline (no guidance effect beyond standard conditional generation). For zero-shot benchmarks γ=1.5 is used. For CoT tasks γ∈{1.0, 1.1, 1.25, 1.5, 1.75, 2.0}. For assistant prompts γ∈{1,2,3,4,5,6}. Optimal γ varies per task.
- **Related concepts**: Classifier-Free Guidance, Negative Prompting

## Unconditional Distribution
- **Notation**: $P_\theta(w_i | w_{j<i})$ (without conditioning prefix $c$)
- **Definition**: The probability distribution over next tokens when the model is prompted only with the last token of the original prompt (rather than the full prompt). This approximates the marginalized distribution and serves as the reference in CFG arithmetic.
- **Boundary conditions**: In autoregressive LMs, dropping the prefix c is a natural operation (unlike diffusion models which require conditioning dropout training). The paper starts the unconditional distribution from the last token of the initial prompt.
- **Related concepts**: Classifier-Free Guidance, Guidance Strength

## Negative Prompting
- **Notation**: $\bar{c}$ (negative conditioning); $c$ (positive/target conditioning)
- **Definition**: An extension of CFG where instead of using the marginal P(w) as the reference, a specified "negative" prompt $\bar{c}$ is used as the reference: $\log \hat{P}_\theta = \log P_\theta(w|\bar{c}) + \gamma(\log P_\theta(w|c) - \log P_\theta(w|\bar{c}))$. This emphasizes the difference between the target and negative prompts.
- **Boundary conditions**: Applied in chatbot settings where $\bar{c}$ is the model's default system prompt and $c$ is the user-modified system prompt. Reduces to standard CFG when $\bar{c} = \emptyset$.
- **Related concepts**: Classifier-Free Guidance, Guidance Strength

## Chain-of-Thought (CoT) Prompting
- **Notation**: $p(w_{cot}, w_a | w_p)$ where $w_{cot} = w_{p+1}...w_{c-1}$ (reasoning chain) and $w_a$ is the answer
- **Definition**: A prompting strategy where the model generates intermediate reasoning steps before producing a final answer. In this paper, CFG is applied only to upweight the initial prompt $w_p$, not the CoT chain $w_{cot}$.
- **Boundary conditions**: CFG upweights only $w_p$ (the task prompt), not $w_{cot}$ or $w_a$. Low γ (≤1.5) improves valid-answer rate; high γ (>1.5) maintains low invalid rate but degrades accuracy.
- **Related concepts**: Classifier-Free Guidance, Guidance Strength

## pass@k (HumanEval Metric)
- **Notation**: $\text{pass@}k$
- **Definition**: For HumanEval code generation: k code samples are generated per problem; a problem is considered solved if any sample passes the unit tests; the total fraction of problems solved is reported. Defined per [16] (Chen et al.).
- **Boundary conditions**: Evaluated for k=1, 10, 100. CFG improves pass@1 at low γ but hurts pass@100, as CFG reduces diversity (exploration) while improving precision.
- **Related concepts**: Classifier-Free Guidance, Guidance Strength

## Logit Distribution
- **Notation**: $\text{logits}_i = \log P_\theta(w_i | w_{j<i}, c)$ (unnormalized log-probabilities)
- **Definition**: The raw log-probability outputs of the final linear layer of the language model before softmax normalization. CFG operates directly in this space, making it architecture-agnostic (avoids network editing).
- **Boundary conditions**: The logit space has a linear relationship with the last hidden layer. The semantic structure of logits (confirmed by word/sentence embedding research [51, 60]) makes logit-space arithmetic meaningful.
- **Related concepts**: Classifier-Free Guidance, Sampling Entropy, Unconditional Distribution

## Sampling Entropy
- **Notation**: $H(p) = -\sum_k p_k \log p_k$
- **Definition**: The Shannon entropy of the token probability distribution at each decoding step. Measures how concentrated or spread-out the model's prediction is over the vocabulary.
- **Boundary conditions**: CFG reduces mean entropy from 5.4 (vanilla) to 4.7 (CFG γ=1.5), comparable to instruction-tuned model entropy. However, the specific tokens upweighted differ from instruction tuning (top-p overlap < 30%).
- **Related concepts**: Logit Distribution, Classifier-Free Guidance, Negative Prompting
