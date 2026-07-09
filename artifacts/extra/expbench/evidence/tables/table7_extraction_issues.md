# Table 7: Extraction Issues Identified and Patched
- **Source**: Table 7, Appendix F
- **Caption**: "Examples of extraction issues identified that were subsequently patched in the final pipeline."
- **Conditions**: Identified during iterative pipeline development before finalization

| Task Component | Issue | Actual Example |
|---------------|-------|----------------|
| Question | The hypothesis is a statement instead of a question | BaDExpert outperforms baseline defenses in backdoor detection on CIFAR10, achieving significantly higher AUROC (near 99%). |
| Question | Conclusion data mentioned in the hypothesis | Specifically, can PDF achieve around 34.64% lower MACs compared to PatchTST and 74.38% lower MACs ...? |
| Masked source | Masked source doesn't exist | "source": ["/workspace/topomlp_setA_r50_w_otransform.py"...] |
| Masked source | Included masked source with wrong path | MuSc has musc.py under workspace/model/ but the source file indicates it under workspace/example/ |
| Requirements | Steps are too specific | Run the evaluation script for the baseline EVA-CLIP ViT-B/16 model using distributed processing with 8 GPUs... |
| Requirements | Asking the agent to use a masked source script | Merge the trained models using the heal_tools.py script (/workspace/opencood/tools/heal_tools.py:115-130) |
| Requirements | Invalid operation | Analyze execution outcomes from Table 4, comparing... |
| Expected outcome | Conclusion not aligned with the paper's findings | N/A |
| Method / Usage Instruction / Agent Instruction | Mentioned specific parts of the paper (tables or figures) | The scripts will log metrics including mean rewards and standard deviations, which can be compared with the reported results in Table 2 of the paper. |
| Method / Usage Instruction / Agent Instruction | Required hyperparameters not given in the agent instruction | Set appropriate model architecture parameters (encoder layers, attention heads, dimensions) |
| Method / Usage Instruction / Agent Instruction | Invalid operations | Collect and analyze performance results from Table 3, ... |
