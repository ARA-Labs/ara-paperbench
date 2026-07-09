# Claims

## C01: SEMA Achieves State-of-the-Art Rehearsal-Free CIL Accuracy
- **Statement**: SEMA with ViT-B/16-IN1K achieves higher or equal average accuracy (A_N) than all compared PTM-based CL methods (FT Adapter, L2P, DualPrompt, CODA-P, SimpleCIL, ADAM, InfLoRA) on CIFAR-100, ImageNet-R (5/10/20-task), ImageNet-A, and VTAB without experience replay.
- **Status**: supported
- **Falsification criteria**: Any compared baseline achieves higher A_N than SEMA (91.37%) on CIFAR-100 under identical experimental conditions (ViT-B/16-IN1K backbone, same data split).
- **Proof**: [E01]
- **Dependencies**: none
- **Tags**: accuracy, CIL, ViT, state-of-the-art

## C02: SEMA Expands Parameters at a Sub-Linear Rate
- **Statement**: The total number of added parameters in SEMA grows sub-linearly with the number of tasks, whereas methods like CODA-P and DualPrompt grow linearly. SEMA adds fewer total parameters than task-specific expansion at equivalent or better accuracy.
- **Status**: supported
- **Falsification criteria**: SEMA's parameter count vs. task index forms a linear or super-linear curve on ImageNet-A (20 tasks), OR SEMA uses more parameters than "Expansion by Task" on any dataset.
- **Proof**: [E02]
- **Dependencies**: C03
- **Tags**: efficiency, sub-linear, parameters, expansion

## C03: On-Demand Self-Expansion Outperforms Static and Per-Task Expansion Strategies
- **Statement**: SEMA's z-score-triggered expansion outperforms: (a) no expansion (single adapter), (b) average weighting without learned router, (c) random weighting, (d) top-1 hard selection, and (e) random hard selection on ImageNet-A and VTAB.
- **Status**: supported
- **Falsification criteria**: Any ablation variant (No Exp., Avg. W., Rand. W., Top-1 Sel., Rand. Sel.) achieves equal or higher A_N and Ā than full SEMA on both ImageNet-A and VTAB simultaneously.
- **Proof**: [E03]
- **Dependencies**: none
- **Tags**: ablation, expansion, routing, MoE

## C04: The SEMA Framework Generalises Across Functional Adapter Types
- **Statement**: Replacing the default Adapter [9] with LoRA [30] or Convpass [34] in the SEMA framework yields performance within 2% A_N on ImageNet-A and VTAB, demonstrating adapter-agnosticism.
- **Status**: supported
- **Falsification criteria**: LoRA or Convpass SEMA variant achieves A_N more than 2% below Adapter SEMA on either ImageNet-A or VTAB.
- **Proof**: [E04]
- **Dependencies**: C01
- **Tags**: adapter variants, generality, LoRA, Convpass
