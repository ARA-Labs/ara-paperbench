"""
BBOX-ADAPTER: Sentence-Level Beam Search Inference

Implements the adapted inference process (§3.3) using sentence-level beam search.
The black-box LLM generates candidate sentences; the adapter scores and selects top-k beams.

Grounded in algo/beam_search.py (Beam_Search class).
"""

import torch
from typing import Callable, Optional


class SentenceLevelBeamSearch:
    """
    Sentence-level beam search for adapted inference from an EBM-based adapter.

    Factorization (§3.3, eq. after Eq. 1):
        p_θ(s^{1:L}|x) = exp(g_θ(s^{1:L}, x)) * ∏_l p_LLM(s^l|x, s^{1:l-1})

    At each step l:
        1. Generate n candidate sentences from p_LLM for each of k beams
        2. Score all nk candidate chains with adapter g_θ
        3. Keep top-k chains with highest adapter scores

    Args:
        beam_size: Number of beams k to maintain. Default=3. Source: configs/*.yaml
        num_candidates: Candidates n generated per beam per step. Default=10. Source: configs/*.yaml
        max_length: Maximum sentence-level steps L. Task-specific (15/8/10/1). Source: configs/*.yaml
        early_stopping: Stop when all beams emit stop signal. Source: configs/*.yaml
        thought_generator: Callable(current_string) → {"text": list[str], "scores": Tensor}
                           Combines LLM generation + adapter scoring
        stop_criterion: Callable(beam_string) → bool; True if beam has terminated
        qa_template: Template string with <Q> and <A> placeholders. Source: configs/*.yaml
    """

    def __init__(
        self,
        beam_size: int,           # k; default=3. Source: configs/*.yaml beam_size
        num_candidates: int,      # n; default=10. Source: configs/*.yaml num_candidates
        max_length: int,          # L; task-specific (15/8/10/1). Source: configs/*.yaml max_length
        early_stopping: bool,     # Source: configs/*.yaml early_stopping
        thought_generator: Callable,
        stop_criterion: Optional[Callable] = None,
        qa_template: str = "Q: <Q>\n\nA: <A>",
    ):
        self.beam_size = beam_size
        self.num_candidates = num_candidates
        self.max_length = max_length
        self.early_stopping = early_stopping
        self.thought_generator = thought_generator
        self.stop_criterion = stop_criterion
        self.qa_template = qa_template

        # State
        self.step = 0
        self.sequences = {}        # hash(text) → text
        self.scores = torch.zeros(beam_size)
        self.beams = -torch.ones((beam_size, max_length), dtype=torch.long)

    def beam_step(self) -> str:
        """
        Execute one beam search step:
        1. For each active beam, generate n candidates from the LLM
        2. Score all nk candidates with the adapter
        3. Select top-k beams by cumulative adapter score

        Returns:
            '<CONTINUE>', '<EARLY_STOP>', or '<SKIP>' (on API failure)
        """
        current_strings = self._get_beam_strings(return_with_init=True)
        bs = 1 if self.step == 0 else self.beam_size

        next_ids = torch.zeros(bs * self.num_candidates, dtype=torch.long)
        next_scores = torch.zeros(bs * self.num_candidates)
        which_beam = -torch.ones(bs * self.num_candidates, dtype=torch.long)

        for i in range(bs):
            candidates = self._get_candidates(current_strings[i], self.scores[i])
            if candidates == '<SKIP>':
                return '<SKIP>'

            next_ids[i * self.num_candidates:(i + 1) * self.num_candidates] = candidates['seq_ids']
            next_scores[i * self.num_candidates:(i + 1) * self.num_candidates] = candidates['scores']
            which_beam[i * self.num_candidates:(i + 1) * self.num_candidates] = i

        # Select top-k beams by adapter score
        top_scores, top_indices = next_scores.topk(self.beam_size, sorted=True)
        beam_ids = which_beam[top_indices]

        self.beams = self.beams[beam_ids, :]
        self.beams[:, self.step] = next_ids[top_indices]
        self.scores = top_scores
        self.step += 1

        # Check early stopping: all beams ended with stop token
        if self.early_stopping and all(
            sid in [hash(''), hash('.')] for sid in self.beams[:, self.step - 1]
        ):
            return '<EARLY_STOP>'
        return '<CONTINUE>'

    def __call__(self, return_with_init: bool = False) -> Optional[list]:
        """
        Run full beam search for up to max_length steps.

        Returns:
            List of beam strings (best first by adapter score), or None on failure.
            If return_with_init=False: returns only the answer portions.
        """
        for _ in range(self.max_length):
            flag = self.beam_step()
            if flag == '<EARLY_STOP>':
                break
            if flag == '<SKIP>':
                return None

        return self._get_beam_strings(return_with_init=return_with_init)

    def _get_candidates(self, current_string: str, current_score: float) -> dict:
        """
        Generate n candidates for a beam, or extend a terminated beam.
        If beam has already stopped, propagate its score without generating.
        """
        if self.stop_criterion is None or not self.stop_criterion(current_string) or self.step == 0:
            res = self.thought_generator(current_string)
            if res == '<SKIP>':
                return '<SKIP>'
            seq_ids = self._add_sequences(res['text'])
            return {'seq_ids': seq_ids, 'scores': res['scores']}
        else:
            # Beam terminated: propagate current score
            seq_ids = hash('') * torch.ones(self.num_candidates)
            scores = current_score * torch.ones(self.num_candidates)
            scores[1:] = -float('inf')
            return {'seq_ids': seq_ids, 'scores': scores}

    def _add_sequences(self, texts: list) -> torch.Tensor:
        """Register new text sequences; return their hash IDs."""
        ids = torch.zeros(self.num_candidates, dtype=torch.long)
        for i, text in enumerate(texts):
            key = hash(text)
            self.sequences[key] = text
            ids[i] = key
        return ids

    def _get_beam_strings(self, return_with_init: bool = True) -> list:
        """Reconstruct full strings from beam IDs."""
        if self.step == 0:
            q = self.sequences.get('init_seq', '')
            return [self.qa_template.replace('<Q>', q).replace('<A>', '')]
        # Reconstruct answer portion from stored sequence hashes
        answer_parts = [
            '\n'.join(
                self.sequences.get(int(self.beams[b, s].item()), '')
                for s in range(self.step)
            )
            for b in range(self.beam_size)
        ]
        if return_with_init:
            q = self.sequences.get('init_seq', '')
            return [
                self.qa_template.replace('<Q>', q).replace('<A>', f"{ans}\n")
                for ans in answer_parts
            ]
        return answer_parts


def single_step_inference(
    llm_generator: Callable,       # LLM_API.get_response() wrapper
    adapter_scorer: Callable,      # get_scores_from_texts()
    question: str,
    num_candidates: int = 10,      # K; Source: configs/*.yaml num_candidates
    prompt: str = "",
) -> str:
    """
    Single-step inference variant (simplified, lower cost).
    The LLM generates K complete answers in one API call; the adapter selects the best.

    Cost: ~6.27x less inference cost than full beam search (Table 4).

    Args:
        llm_generator: Generates K text candidates in one call
        adapter_scorer: Scores a list of texts, returns Tensor of scores
        question: Input question string
        num_candidates: K candidates to generate
        prompt: Few-shot prompt prefix

    Returns:
        Best candidate string selected by adapter score
    """
    full_prompt = f"{prompt}\n{question}".strip()
    candidates = llm_generator(full_prompt, n=num_candidates)

    if not candidates or candidates == '<SKIP>':
        return ""

    scores = adapter_scorer(candidates)
    best_idx = int(scores.argmax())
    return candidates[best_idx]
