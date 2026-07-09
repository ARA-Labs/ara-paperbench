"""
BBOX-ADAPTER: Online Adaptation Loop (Algorithm 1)
Implements the iterative sampling and training procedure for self-improvement.

Reference: Sun et al., "BBOX-ADAPTER: Lightweight Adapting for Black-Box LLMs"
ICML 2024. arXiv:2402.08219
"""

import torch
from torch.optim import AdamW
from typing import List, Tuple, Dict, Callable, Optional
from ebm_adapter import EBMAdapter, ranking_nce_loss, sentence_level_beam_search


def select_positive_sample(
    candidates: List[str],
    previous_positive: Optional[str],
    feedback_fn: Callable[[str, List[str]], str],
) -> Tuple[str, List[str]]:
    """
    Update positive and negative sample sets based on feedback (Equations 5, 6).

    Equation (5): y^(t)_{i+} = SEL(y^(t-1)_{i+}, {hat_y_{i,m}}^M_{m=1})
    Equation (6): y^(t)_{i-} = {hat_y_{i,m} | hat_y_{i,m} != y^(t)_{i+}}

    The SEL(·) function selects the best candidate based on:
      - Ground-truth setting: exact match with ground-truth answer
      - AI Feedback setting: GPT-4 evaluation (coherency, reasonability,
                              correctness, format criteria from Appendix G)
      - Combined: ground-truth augmented with AI feedback preferred candidates

    Args:
        candidates: List[str] — M sampled candidates from adapted inference
        previous_positive: Optional[str] — y^(t-1)_{i+} from previous iteration
        feedback_fn: callable(question, candidates) -> best_candidate
                     Implements SEL(·) — selects best answer given feedback signal
    Returns:
        positive: str — selected positive sample y^(t)_{i+}
        negatives: List[str] — remaining candidates as negatives y^(t)_{i-}
    """
    pool = candidates.copy()
    if previous_positive is not None:
        pool = [previous_positive] + candidates

    # SEL(·): select best from pool using ground-truth / human / AI feedback
    positive = feedback_fn("", pool)

    # All non-positive candidates become negatives (Equation 6)
    negatives = [c for c in candidates if c != positive]
    return positive, negatives


def online_adaptation(
    dataset: List[Tuple[str, str]],
    llm_generate_fn: Callable[[str, int], List[str]],
    feedback_fn: Callable[[str, List[str]], str],
    adapter: EBMAdapter,
    num_iterations: int = 3,
    learning_rate: float = 5e-6,
    weight_decay: float = 0.01,
    batch_size: int = 64,
    num_training_steps: int = 6000,
    beam_size: int = 3,
    num_candidates: int = 3,
    alpha: float = 1.0,
) -> EBMAdapter:
    """
    Algorithm 1: BBOX-ADAPTER Online Adaptation.

    Iteratively samples from adapted inference, updates positive/negative sets
    using feedback, and trains the adapter with ranking-based NCE loss.

    Key equations:
      Initialization: y^(0)_{i+} = SEL({y_{i,j}}^K_{j=1})
      Sampling (Eq. 4): {hat_y_{i,m}}^M ~ p_theta_t(y|x_i)
      Positive update (Eq. 5): y^(t)_{i+} = SEL(y^(t-1)_{i+}, {hat_y_{i,m}})
      Negative update (Eq. 6): y^(t)_{i-} = {hat_y | hat_y != y^(t)_{i+}}
      Gradient (Eq. 3): nabla_theta l(theta_t) [NCE + spectral norm regularization]
      Update (Eq. 7): theta_{t+1} = theta_t - eta * nabla_theta l(theta_t)

    Args:
        dataset: List[(question, ground_truth)] — D = {(x_i, y_i)}
        llm_generate_fn: callable(prompt, n) -> List[str] — black-box LLM API wrapper
        feedback_fn: callable(question, candidates) -> str — SEL(·) implementation
                     (ground-truth match, human ranking, or AI/GPT-4 feedback)
        adapter: EBMAdapter — initialized adapter (theta_0)
        num_iterations: int T — number of online adaptation rounds (default: 3)
        learning_rate: float eta — AdamW learning rate (default: 5e-6)
        weight_decay: float — AdamW weight decay (default: 0.01)
        batch_size: int — training batch size (default: 64)
        num_training_steps: int — total gradient steps per iteration (default: 6000)
        beam_size: int M — beam size for adapted inference sampling (default: 3)
        num_candidates: int — candidates per beam at each step (default: 3)
        alpha: float — spectral normalization regularization weight (default: 1.0)

    Returns:
        adapter: EBMAdapter — fine-tuned adapter theta_T
    """
    optimizer = AdamW(adapter.parameters(), lr=learning_rate, weight_decay=weight_decay)

    # --- Initialization Phase ---
    # For each input, sample K initial candidates and select initial positives/negatives
    positive_sets: Dict[int, str] = {}
    negative_sets: Dict[int, List[str]] = {}

    print("Initializing positive and negative sample sets...")
    for i, (question, _) in enumerate(dataset):
        # Sample K=beam_size*num_candidates initial responses from unadapted LLM
        initial_candidates = llm_generate_fn(question, n=beam_size * num_candidates)

        # SEL(·): select best initial positive via feedback
        positive = feedback_fn(question, initial_candidates)
        negatives = [c for c in initial_candidates if c != positive]

        positive_sets[i] = positive
        negative_sets[i] = negatives if negatives else initial_candidates[:1]

    # --- Main Adaptation Loop ---
    for t in range(num_iterations):
        print(f"Online adaptation iteration {t+1}/{num_iterations}")

        # Step 1: Sample M candidates from current adapted inference p_theta_t
        new_candidates: Dict[int, List[str]] = {}
        for i, (question, _) in enumerate(dataset):
            # Equation (4): {hat_y_{i,m}}^M ~ p_theta_t(y|x_i)
            sampled = []
            for _ in range(beam_size):
                candidate = sentence_level_beam_search(
                    question=question,
                    llm_generate_fn=llm_generate_fn,
                    adapter=adapter,
                    beam_size=beam_size,
                    candidates_per_beam=num_candidates,
                )
                sampled.append(candidate)
            new_candidates[i] = sampled

        # Step 2 & 3: Update positive and negative sets using feedback
        for i, (question, _) in enumerate(dataset):
            # Equation (5): y^(t)_{i+} = SEL(y^(t-1)_{i+}, {hat_y_{i,m}})
            pool = [positive_sets[i]] + new_candidates[i]
            new_positive = feedback_fn(question, pool)

            # Equation (6): y^(t)_{i-} = {hat_y | hat_y != y^(t)_{i+}}
            new_negatives = [c for c in new_candidates[i] if c != new_positive]

            positive_sets[i] = new_positive
            negative_sets[i] = new_negatives if new_negatives else [positive_sets[i]]

        # Step 4 & 5: Train adapter with NCE loss (Equations 3, 7)
        adapter.train()
        all_positives = [(i, q, positive_sets[i]) for i, (q, _) in enumerate(dataset)]
        all_negatives = [(i, q, n) for i, (q, _) in enumerate(dataset)
                         for n in negative_sets[i]]

        step = 0
        while step < num_training_steps:
            # Sample a batch of positive and negative pairs
            import random
            batch_pos = random.sample(all_positives, min(batch_size // 2, len(all_positives)))
            batch_neg = random.sample(all_negatives, min(batch_size // 2, len(all_negatives)))

            pos_texts = [f"{q} {p}" for _, q, p in batch_pos]
            neg_texts = [f"{q} {n}" for _, q, n in batch_neg]

            # Compute NCE loss (Equation 3)
            loss = ranking_nce_loss(adapter, pos_texts, neg_texts, alpha=alpha)

            # Gradient update (Equation 7): theta_{t+1} = theta_t - eta * nabla_theta l
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            step += 1
            if step % 1000 == 0:
                print(f"  Step {step}/{num_training_steps}, Loss: {loss.item():.4f}")

        adapter.eval()
        print(f"  Iteration {t+1} complete.")

    return adapter
