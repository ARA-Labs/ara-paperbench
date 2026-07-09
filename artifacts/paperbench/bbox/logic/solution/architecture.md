# System Architecture

## Component Overview

BBOX-ADAPTER consists of three main components operating in two phases (training and inference) within an online adaptation loop.

```
┌─────────────────────────────────────────────────────────────────┐
│                   BBOX-ADAPTER System                           │
│                                                                 │
│  ┌──────────────────────┐    ┌─────────────────────────────┐   │
│  │   Black-Box LLM      │    │  Energy-Based Adapter g_θ   │   │
│  │  (Proposal Generator)│    │  (Scorer/Reranker)          │   │
│  │  pLLM(y|x) — FIXED   │    │  DeBERTa-v3 / BERT — TRAIN  │   │
│  │  API: text-in/out    │    │  Input: (x, y) text pair    │   │
│  │                      │    │  Output: scalar score ∈ ℝ   │   │
│  └──────────────────────┘    └─────────────────────────────┘   │
│           │                              │                      │
│           ▼                              ▼                      │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              Online Adaptation Loop (Algorithm 1)         │  │
│  │  1. Sample M candidates from pθ(y|x) (beam search)        │  │
│  │  2. Select positive y+ via SEL(·) [GT/human/AI]           │  │
│  │  3. Set remaining as negatives y−                         │  │
│  │  4. Compute NCE loss gradient ∇θℓ(θt)                     │  │
│  │  5. Update θt+1 = θt − η∇θℓ(θt)                          │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Components

### 1. Black-Box LLM (Proposal Generator)
- **Purpose**: Generates candidate text outputs for a given input; serves as the base proposal distribution $p_{LLM}(y|x)$.
- **Inputs**: Text prompt $x$ (formatted with few-shot CoT examples)
- **Outputs**: Text completions $\{y_j\}$ (text-only, no probabilities)
- **Implementation**: gpt-3.5-turbo (Azure OpenAI API) or Mixtral-8×7B (HuggingFace); temperature=1.0; max_length=512
- **Interactions**: Called during both training (to generate initial candidates and adaptation samples) and inference (sentence-by-sentence for beam search)
- **Key design choice**: Treated as completely black-box; only text outputs are consumed.

### 2. Energy-Based Adapter $g_\theta$
- **Purpose**: Assigns a scalar energy score to each (input, output) pair; trained to score target-domain text higher than source-domain text.
- **Inputs**: Concatenated (question, answer) text string as a single sequence
- **Outputs**: Scalar score $g_\theta(x, y) \in \mathbb{R}$ (higher = more likely from target domain)
- **Implementation**: 
  - DeBERTa-v3-base (86M, `microsoft/deberta-v3-base`) for StrategyQA, GSM8K, ScienceQA
  - DeBERTa-v3-large (304M, `microsoft/deberta-v3-large`) for StrategyQA, GSM8K, ScienceQA
  - BERT-base-cased (110M, `bert-base-cased`) for TruthfulQA
  - Final classification head: linear layer mapping [CLS] representation to scalar; output dimension = 1
  - Spectral normalization applied to the linear classification head
- **Interactions**: Called at each beam step to score partial hypotheses $s_{1:l}$; updated via NCE gradient during training
- **Key design choice**: Lightweight (0.1B–0.3B) for cost efficiency; uses encoder-only models for discriminative scoring.

### 3. Online Adaptation Loop
- **Purpose**: Iteratively improves the adapter by sampling from its own adapted distribution and refining positive/negative sets.
- **Inputs**: Dataset $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^N$; current adapter parameters $\theta_t$
- **Outputs**: Refined adapter parameters $\theta_{T}$ after $T$ iterations
- **Sub-components**:
  - *Sample collection*: beam search via adapted inference to obtain $M$ candidates per input
  - *Feedback module*: SEL(·) selects best candidate using ground-truth match, human ranking, or GPT-4 AI feedback
  - *Training step*: AdamW optimizer (lr=5e-6, wd=0.01), batch size 64, 6000 total steps per iteration
- **Interactions**: Calls LLM (for new candidates) and adapter (for scoring); updates adapter weights
- **Key design choice**: Dynamic positive set that improves over iterations; negative set always comes from the adapter's own recent outputs (self-improvement).

### 4. Adapted Inference (Sentence-Level Beam Search)
- **Purpose**: At test time, generates the best output by combining LLM proposals with adapter scoring.
- **Inputs**: Question $x$; current adapter $g_{\theta_T}$; beam size $k$; candidates per step $n$
- **Outputs**: Best complete answer $y^*$ according to $g_{\theta_T}$
- **Procedure**: At each sentence step $l$, generate $n$ next-sentence candidates per beam (total $nk$); score all with adapter on partial chain $s_{1:l}$; prune to top-$k$; repeat until stop signal or $L$ steps; return highest-scoring complete answer.
- **Interactions**: Calls LLM API multiple times per question (beam × candidates × steps); calls adapter for scoring
- **Key design choice**: Sentence-level granularity decomposes complex multi-step problems into manageable search steps.

## Data Flow

```
Training:
x_i → [Black-Box LLM (K samples)] → {y_{i,j}} → SEL(·) → y+(0), y-(0)
       ↓ (per iteration t)
       [Adapted Inference pθt] → {ŷ_{i,m}} → SEL(y+(t-1), {ŷ}) → y+(t), y-(t)
       → NCE loss → ∇θℓ(θt) → θt+1

Inference:
x → [Beam Search: LLM proposes, Adapter scores, top-k retained] → y*
```
