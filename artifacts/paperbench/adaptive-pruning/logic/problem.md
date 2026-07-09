# Problem Specification

## Observations

### O1: LM Fine-Tuning Is Memory-Intensive
- **Statement**: A 13B LLaMA model costs approximately 100 GB memory for fine-tuning and approximately 30 GB for inference with float16 datatype.
- **Evidence**: Introduction, §1
- **Implication**: Large-scale LM fine-tuning is inaccessible on consumer-level hardware (typically ≤24 GB VRAM).

### O2: PEFT Reduces Training Memory But Not Inference Cost
- **Statement**: Methods like LoRA reduce training memory by tuning only low-rank decomposed layers, but the LM size remains the same or increases after fine-tuning, leaving inference cost unchanged. LoRA also takes longer to converge than full fine-tuning (Ding et al., 2023).
- **Evidence**: §1, Table 1
- **Implication**: PEFT alone cannot satisfy use cases that require fast inference or low inference memory.

### O3: Structured Pruning Improves Inference But Worsens Training
- **Statement**: Structured pruning (removing MHA heads, FFN neurons, model hidden dimensions) improves inference efficiency but typically requires knowledge distillation, causing higher training memory and longer convergence time than PEFT alone.
- **Evidence**: §1, Table 1; CoFi (Prune+Distill) costs 168.5% training memory vs 100% for FT in Table 2.
- **Implication**: Pruning alone cannot satisfy use cases with limited training resources.

### O4: Naive Combination of PEFT and Pruning Fails
- **Statement**: Combining structured pruning with LoRA (e.g., LoRA+Prune) causes noticeable performance loss and extra training costs (6534.6% relative training time in Table 2) because static tuning parameters cannot adapt to the changing parameter space during pruning.
- **Evidence**: §1, §2.3, Table 2; Zhao et al., 2023 (CPET paper)
- **Implication**: A new paradigm is needed that co-adapts tuning and pruning decisions.

### O5: Outlier Parameters Are Disproportionately Important
- **Statement**: Block outlier parameters play a crucial role in task-specific capabilities, as shown by quantization methods (Dettmers et al., 2022; Lin et al., 2023). Averaging salience at the block level loses this signal.
- **Evidence**: §4.2 (outlier discussion); ablation showing w/o kurtosis drops LLaMA2-7B avg from 50.0 to 38.1 (Table 5).
- **Implication**: Salience scoring must account for outlier distributions, not just mean magnitudes.

### O6: Early Pruning Does Not Substantially Hurt Performance
- **Statement**: Removing parameters irrelevant to the fine-tuning task in the early training stage improves training and inference efficiency without substantially hurting model accuracy (Frankle et al., 2021; Shen et al., 2022a; Zhang et al., 2023c).
- **Evidence**: §1 motivation; APT ablation results (Table 4) showing APT maintains 98% accuracy at 60% sparsity.
- **Implication**: Pruning schedule should be front-loaded to maximize training efficiency.

## Gaps

### G1: No Method Simultaneously Improves Training AND Inference Efficiency
- **Statement**: Existing PEFT methods (LoRA, AdaLoRA) improve training efficiency but not inference; existing pruning methods (CoFi, BMP) improve inference but worsen training; no prior method achieves both simultaneously.
- **Caused by**: O2, O3
- **Existing attempts**: SPA (Hedegaard et al., 2022), LRP (Zhang et al., 2023a), CPET (Zhao et al., 2023)
- **Why they fail**: Static tuning parameters cannot compensate for dynamic parameter removal; combining pruning and static LoRA loses performance (Table 2: LoRA+Prune reaches only 84.0/93.0 on MNLI/SST2 vs 87.6/94.8 FT).

### G2: Salience Scoring in PEFT Settings Is Inaccurate
- **Statement**: Standard weight-gradient salience is inapplicable to frozen parameters in PEFT settings; activation-gradient products are needed instead. Existing structured pruning methods with LoRA (LRP) use only tuning block salience, missing the frozen weight contribution.
- **Caused by**: O2, O5
- **Existing attempts**: Movement pruning (Sanh et al., 2020), LRP (Zhang et al., 2023a)
- **Why they fail**: Frozen gradients are unreachable; using only tuning parameter salience gives sub-optimal pruning decisions.

### G3: Knowledge Distillation Is Prohibitively Expensive for Resource-Constrained Settings
- **Statement**: Standard distillation requires a fully trained teacher model on the GPU alongside the student, roughly doubling training memory and time (FT teacher costs 111.8% memory and 7.9% training speed relative to FT; Table 10).
- **Caused by**: O3
- **Existing attempts**: CoFi (Xia et al., 2022) distillation
- **Why they fail**: Separate teacher models are too large for consumer GPUs; LLMPruner costs ~80 GB for LLaMA 7B pruning.

## Key Insight

- **Insight**: Pruning and tuning decisions can be made jointly and adaptively using the same lightweight salience signal computed from activations and their gradients (available even for frozen parameters). By sharing frozen parameters between teacher and student and dynamically growing adapter ranks only in salient layers, one can simultaneously reduce the parameter space (improving training AND inference efficiency) while recovering lost accuracy — all within a single training run without separate teacher pre-training.
- **Derived from**: O2, O3, O5, O6
- **Enables**: A unified APT adapter architecture where binary pruning masks and dynamic LoRA ranks are co-optimized using a shared outlier-aware salience score and a cubic pruning schedule.

## Assumptions

- A1: Pre-trained LM parameters contain general knowledge, but their importance to downstream tasks varies — allowing task-irrelevant parameters to be removed early without catastrophic forgetting.
- A2: Task-specific skills reside in a subset of LM parameters (Wang et al., 2022a; Panigrahi et al., 2023), so selectively adding tuning parameters in important layers suffices for performance recovery.
- A3: Structured pruning (heads, neurons, hidden dim) is preferred over unstructured pruning for hardware-agnostic inference speedup.
- A4: Hardware is Ampere-architecture GPU; dimensions divisible by 8 (FP16) or 16 (Int8) yield realistic speedups.
- A5: The frozen pre-trained weights are not updated during fine-tuning; only adapter parameters (W_A, W_B) and pruning masks are trained.
