"""
BBOX-ADAPTER Core: Energy-Based Model Adapter for Black-Box LLM Adaptation

This module implements the core algorithm:
1. Energy adapter (g_θ): DeBERTa/BERT classification head outputting scalar energy
2. NCE loss with spectral normalization (L2 regularization)
3. Sentence-level beam search for adapted inference

References:
  - algo/adapter.py, llms/whitebox.py (core implementation)
  - configs/*.yaml (hyperparameters)
  - Paper Sections 3.1, 3.2, 3.3
"""

import torch
import torch.nn as nn
from torch.optim import AdamW
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    get_constant_schedule_with_warmup,
)
from typing import List, Tuple, Dict, Optional


class EnergyAdapter:
    """
    The energy adapter g_θ: (x, y) → scalar energy score.
    
    Uses AutoModelForSequenceClassification with num_labels=1 to output
    a scalar energy value. Higher energy = target domain (positive).
    Lower energy = source domain (negative).
    
    Corresponds to g_θ in Eq. (1): p_θ(y|x) = p_LLM(y|x) * exp(g_θ(x,y)) / Z_θ(x)
    """
    
    def __init__(
        self,
        model_name: str,          # e.g., "microsoft/deberta-v3-base" or "bert-base-cased"
        learning_rate: float,     # 5e-6
        weight_decay: float,      # 0.01
        warmup_steps: int,        # 50 (StrategyQA/GSM8K/ScienceQA), 0 (TruthfulQA)
        l2_reg_coef: float,       # 1.0 (alpha in Eq. 3)
        energy_temp: float,       # 5.0 (temperature scaling for energies)
        gradient_accumulation_steps: int,  # 1 (StrategyQA/TruthfulQA), 3 (GSM8K/ScienceQA)
        add_special_tokens: bool = True,
        truncation_side: str = "left",
    ):
        self.l2_reg_coef = l2_reg_coef
        self.energy_temp = energy_temp
        
        # Tokenizer with left truncation (preserves answer at end of sequence)
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            truncation_side=truncation_side,
        )
        
        # Energy model: sequence classifier with scalar output (num_labels=1)
        # Final linear layer: hidden_size → 1, outputting scalar energy g_θ(x, y)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            trust_remote_code=True,
            num_labels=1,         # KEY: scalar energy output
        )
        self.model.config.pad_token_id = self.tokenizer.eos_token_id
        self.model.config.use_cache = True
        
        # Optimizer: AdamW with weight decay for regularization
        self.optimizer = AdamW(
            self.model.parameters(),
            lr=learning_rate * gradient_accumulation_steps,
            weight_decay=weight_decay,  # 0.01
        )
        
        # Constant LR schedule with warmup (flat after warmup)
        self.lr_scheduler = get_constant_schedule_with_warmup(
            self.optimizer,
            num_warmup_steps=warmup_steps,
        )
    
    def compute_nce_loss(
        self,
        positive_texts: List[str],   # y+ ~ p_data(y|x): target domain samples
        negative_texts: List[str],   # y- ~ p_θ(y|x): LLM-generated source domain samples
    ) -> torch.Tensor:
        """
        Compute the ranking-based NCE loss with spectral normalization (Eq. 3):
        
        ∇_θ ℓ(θ) = ∇_θ {
            -E_{y+~p_data}[g_θ(x,y+)] + α·E[g_θ(x,y+)²]
          + E_{y-~p_θ}[g_θ(x,y-)]   + α·E[g_θ(x,y-)²]
        }
        
        The L2 terms (α·E[g²]) approximate spectral normalization,
        preventing sharp gradients and training instability.
        
        Args:
            positive_texts: List of (question, answer) strings for target domain
            negative_texts: List of (question, answer) strings for source domain
        
        Returns:
            scalar loss tensor for backward()
        """
        all_texts = positive_texts + negative_texts
        # labels: +1 for positive, -1 for negative
        labels = torch.cat([
            torch.ones(len(positive_texts)),
            -torch.ones(len(negative_texts))
        ])
        
        # Tokenize
        inputs = self.tokenizer(
            all_texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            add_special_tokens=True,
        )
        
        # Forward pass → scalar energy per sample: shape (B,)
        outputs = self.model(**inputs)
        output_logits = outputs.get("logits")  # shape: (B, 1)
        
        # Energy = -logit (higher logit → lower energy for positive class)
        # In classification mode: energies = -output_logits.squeeze(-1)
        energies = -output_logits.squeeze(-1)   # shape: (B,)
        
        # Scale energies by temperature
        pos_energy = energies[labels > 0] / self.energy_temp
        neg_energy = energies[labels < 0] / self.energy_temp
        
        # Guard against empty batches
        if pos_energy.shape[0] == 0:
            pos_energy = torch.zeros(1)
        if neg_energy.shape[0] == 0:
            neg_energy = torch.zeros(1)
        
        # NCE contrastive loss: push positive energy up, negative energy down
        ml_loss = pos_energy.mean() - neg_energy.mean()
        
        # L2 spectral normalization proxy (Eq. 3, α term)
        l2_loss = self.l2_reg_coef * energies.square().mean()
        
        loss = ml_loss + l2_loss
        return loss
    
    def get_energy_scores(
        self,
        texts: List[str],            # (question + answer) strings to score
    ) -> torch.Tensor:
        """
        Score candidate texts with the energy adapter g_θ(x, y).
        Higher score = more likely to be target domain.
        
        Used during adapted inference (beam search) to select top-k beams.
        
        Returns:
            1D tensor of shape (len(texts),) with energy scores
        """
        self.model.eval()
        with torch.no_grad():
            inputs = self.tokenizer(
                texts,
                return_tensors="pt",
                padding=True,
                truncation=True,
                add_special_tokens=True,
            )
            outputs = self.model(**inputs)
            output_logits = outputs.get("logits")  # (B, 1)
            # Return raw logit as score (higher = better for beam selection)
            return output_logits.squeeze(-1).detach()
    
    def update_step(self, loss: torch.Tensor, max_grad_norm: float = 1.0):
        """
        Perform one gradient update step (Eq. 7):
        θ_{t+1} = θ_t - η ∇_θ ℓ(θ_t)
        
        Includes gradient clipping (max_norm=1.0) for stability.
        """
        loss.backward()
        torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_grad_norm)
        self.optimizer.step()
        self.lr_scheduler.step()
        self.optimizer.zero_grad()


class SentenceBeamSearch:
    """
    Sentence-level beam search for adapted inference (Section 3.3).
    
    The black-box LLM generates candidate next sentences (proposals).
    The adapter scores accumulated chains and selects top-k beams.
    
    pθ(y|x) = exp(g_θ(s_{1:L}, x)) · Π_l p_LLM(s_l | x, s_{1:l-1})
    
    Corresponds to algo/beam_search.py
    """
    
    def __init__(
        self,
        beam_size: int,         # k: number of beams to maintain (default: 3)
        num_candidates: int,    # n: candidates generated per beam per step (default: 10)
        max_length: int,        # L: max reasoning steps (10/15/8/1 by task)
        early_stopping: bool = True,
    ):
        self.beam_size = beam_size
        self.num_candidates = num_candidates
        self.max_length = max_length
        self.early_stopping = early_stopping
    
    def beam_search(
        self,
        question: str,
        llm_generate_fn,        # callable: (prompt) → List[str] (n candidate sentences)
        adapter_score_fn,       # callable: (List[str]) → Tensor (energy scores)
        stop_criterion,         # callable: (str) → bool (True if answer is complete)
        qa_template: str,       # e.g., "Q: <Q>\n\nA: <A>"
    ) -> List[str]:
        """
        Perform sentence-level beam search.
        
        At each step l:
          1. For each of k beams, call LLM to generate n candidate next sentences
          2. Score all n*k candidates (accumulated chains) with adapter
          3. Keep top-k chains by adapter score
          4. Stop if all beams complete or max_length reached
        
        Returns top-k complete answer chains (sorted by energy score, best first).
        """
        # Initialize: one beam with empty answer
        beams: List[str] = [""]
        beam_scores: torch.Tensor = torch.zeros(1)
        
        for step in range(self.max_length):
            all_candidates: List[Tuple[str, float]] = []
            
            for beam_idx, current_chain in enumerate(beams):
                # Check if this beam is already complete
                if step > 0 and stop_criterion(current_chain):
                    all_candidates.append((current_chain, beam_scores[beam_idx].item()))
                    continue
                
                # Generate n candidate next sentences from LLM
                prompt = qa_template.replace("<Q>", question).replace("<A>", current_chain)
                candidate_sentences: List[str] = llm_generate_fn(prompt)
                
                # Accumulate sentences into chains and score with adapter
                for sentence in candidate_sentences:
                    chain = current_chain + ("\n" if current_chain else "") + sentence
                    all_candidates.append((chain, None))  # scores filled below
            
            # Score all unevaluated candidates with adapter
            texts_to_score = [c for c, s in all_candidates if s is None]
            if texts_to_score:
                qa_texts = [qa_template.replace("<Q>", question).replace("<A>", t) for t in texts_to_score]
                scores = adapter_score_fn(qa_texts)
                score_idx = 0
                all_candidates = [
                    (c, scores[score_idx].item() if s is None else s)
                    for score_idx, (c, s) in enumerate(
                        [(c, s) for c, s in all_candidates]
                    )
                ]
            
            # Select top-k beams
            all_candidates.sort(key=lambda x: x[1], reverse=True)
            top_k = all_candidates[:self.beam_size]
            beams = [c for c, _ in top_k]
            beam_scores = torch.tensor([s for _, s in top_k])
            
            # Early stopping: all beams complete
            if self.early_stopping and all(stop_criterion(b) for b in beams):
                break
        
        return beams  # ranked best-first by energy score
