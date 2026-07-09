# Problem Specification

## Observations

### O1: PTM-Based CL Methods Are Limited by Fixed Adapter/Prompt Pools
- **Statement**: Most PTM-based CL methods (L2P, DualPrompt, ADAM, RanPAC) use a fixed, pre-defined set of prompts or adapters shared by all tasks. To avoid forgetting, they restrict parameter updates to the first task or apply regularization.
- **Evidence**: Survey in §2 citing [51, 73, 74, 90]; L2P uses 0.123M parameters (fixed) across all tasks (Table 6).
- **Implication**: The fixed capacity constrains the model's ability to adapt to diverse or long task sequences.

### O2: Task-Specific Expansion Causes Linear Parameter Growth
- **Statement**: Methods that expand PTMs with task-specific adapters or prompts (CODA-P, DualPrompt, EASE) add modules at every new task, leading to parameter count that grows linearly with the number of tasks.
- **Evidence**: Table 6 — DualPrompt adds 1.022M params for CIFAR-100 (10 tasks), CODA-P adds 3.917M. Figure 8 shows linear growth for DualPrompt and CODA-P vs sub-linear for SEMA.
- **Implication**: Linear growth is storage-inefficient and impairs knowledge sharing across tasks.

### O3: Knowledge Transfer Is Impaired by Task-Specific Isolation
- **Statement**: When adapters are task-specific, samples that share features across tasks (e.g., cat vs. dog) cannot benefit from the previously learned representations.
- **Evidence**: Table 5 — SEMA with fewer parameters (0.617M) outperforms "Expansion by Task" (1.904M) on ImageNet-R (74.53% vs 74.08%).
- **Implication**: Naive expansion fails to exploit cross-task similarities.

### O4: Distribution Shift Is Layer-Specific in Transformers
- **Statement**: Feature distribution shifts across tasks manifest differently at different transformer layers; earlier layers exhibit more generic representations while later layers encode more task-specific patterns.
- **Evidence**: Figure 7 — allowing expansion in layers 9-12 improves over layers 11-12 only; earlier layers (9-10) trigger fewer expansions.
- **Implication**: Expansion must be decided per-layer, not globally.

## Gaps

### G1: No Existing Method Achieves On-Demand Sub-Linear Expansion
- **Statement**: No existing PTM-based CL method simultaneously achieves: (a) automatic per-layer expansion, (b) sub-linear parameter growth, and (c) competitive accuracy.
- **Caused by**: O1, O2, O3
- **Existing attempts**: Task-specific expansion (EASE [92], CODA-P [68]); fixed pools (L2P [74], ADAM [90])
- **Why they fail**: Fixed pools lack plasticity; task-specific expansion wastes parameters and hinders reuse.

### G2: No Reliable Distribution Shift Detector at Intermediate Layers
- **Statement**: Existing CL methods lack a mechanism to reliably detect whether intermediate-layer representations of a new task fall within the distribution of previously-seen tasks.
- **Caused by**: O4
- **Existing attempts**: Using batch statistics of modular networks [55], task ID oracles, prototype distances
- **Why they fail**: Batch-level statistics are unreliable for individual samples; task IDs are often unavailable; prototypes operate only on final-layer features.

## Key Insight
- **Insight**: A lightweight autoencoder (representation descriptor) can be trained jointly with each functional adapter to capture the local feature distribution at that specific layer. Its reconstruction error, normalized to a z-score using running statistics from a 500-sample buffer, provides a reliable per-sample novelty signal that is robust to scale and perturbation differences across tasks.
- **Derived from**: O2, O4
- **Enables**: Layer-wise, on-demand adapter expansion that is automatically triggered only when genuinely novel feature patterns are detected — enabling sub-linear growth and knowledge reuse.

## Assumptions
- A1: The pre-trained ViT (frozen) provides a stable and transferable feature extractor for downstream CL tasks.
- A2: Task boundaries are known during training (class-incremental learning setting with task-oriented expansion).
- A3: Autoencoder reconstruction error is a reliable proxy for distribution novelty at each transformer layer.
- A4: A single additional adapter per layer per task is sufficient granularity for the on-demand expansion.
- A5: The last 3 transformer layers (layers 10, 11, 12 for ViT-B/16) contain the most task-discriminative representations and are the primary targets for expansion.
