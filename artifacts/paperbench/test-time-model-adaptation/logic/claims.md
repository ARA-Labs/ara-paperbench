---
# Claims

## C01: FOA outperforms gradient-based TENT on full-precision ViT without backpropagation
- **Statement**: FOA achieves higher average accuracy and lower ECE than TENT on ImageNet-C (severity 5) using full-precision 32-bit ViT-Base, without performing any backpropagation or modifying model weights.
- **Status**: supported
- **Falsification criteria**: If FOA average accuracy on ImageNet-C (severity 5) with 32-bit ViT-Base is ≤ TENT's 59.6%, or FOA average ECE is ≥ TENT's 18.5%, the claim is falsified.
- **Proof**: [E01, E02]
- **Dependencies**: none
- **Tags**: accuracy, ECE, backpropagation-free, ImageNet-C, ViT-Base

## C02: FOA on 8-bit quantized ViT outperforms TENT on full-precision 32-bit ViT
- **Statement**: FOA applied to an 8-bit PTQ4ViT-quantized ViT-Base achieves higher accuracy (63.5%) on ImageNet-C than gradient-based TENT applied to full-precision 32-bit ViT-Base (59.6%), while using 208 MB vs. 5,165 MB memory.
- **Status**: supported
- **Falsification criteria**: If FOA (8-bit) accuracy on ImageNet-C ≤ 59.6%, or memory usage is not substantially reduced relative to TENT (32-bit).
- **Proof**: [E03]
- **Dependencies**: C01
- **Tags**: quantization, 8-bit, memory efficiency, edge deployment, ImageNet-C

## C03: FOA achieves up to 24× run-time memory reduction vs. TENT
- **Statement**: FOA with 8-bit ViT uses 208 MB at batch size 64 on ImageNet-C, compared to 5,165 MB for TENT with 32-bit ViT — a 24.8× reduction — because FOA requires no gradient buffers or backward computation graph.
- **Status**: supported
- **Falsification criteria**: If FOA (8-bit, BS=64) memory usage is not substantially lower than TENT (32-bit, BS=64) at ≥ 10× ratio.
- **Proof**: [E04]
- **Dependencies**: C02
- **Tags**: memory, efficiency, quantization, run-time, resource-constrained

## C04: CMA-ES with entropy-only fitness is infeasible for TTA
- **Statement**: Replacing SGD with CMA-ES for entropy-based TTA (using either norm layers or prompts as learnable parameters) collapses to near-random accuracy (0.1% for norm layers, 44.9% for prompts), confirming that entropy alone cannot provide stable CMA learning signals.
- **Status**: supported
- **Falsification criteria**: If CMA + prompts + entropy achieves accuracy within 5% of NoAdapt (55.5%) or better, the claim is partially falsified.
- **Proof**: [E05]
- **Dependencies**: none
- **Tags**: CMA-ES, entropy, fitness function, ablation, design choice

## C05: Activation discrepancy fitness enables stable CMA learning in online unsupervised TTA
- **Statement**: The proposed fitness function combining prediction entropy with activation distribution discrepancy (Eq. 5) provides consistent learning signals for CMA, improving accuracy from 55.5% (NoAdapt) to 63.4% using only the activation discrepancy term, and to 66.3% using the full fitness function with activation shifting.
- **Status**: supported
- **Falsification criteria**: If activation discrepancy fitness improves over NoAdapt by < 5% on ImageNet-C average accuracy, or combined fitness + shifting does not achieve best accuracy among all FOA variants.
- **Proof**: [E05, E06]
- **Dependencies**: C04
- **Tags**: fitness function, activation discrepancy, CMA-ES, ablation, stability

## C06: FOA maintains near-original in-distribution accuracy, outperforming gradient-based TTA on source domain
- **Statement**: FOA's in-distribution accuracy on clean ImageNet validation set (85.11%, −0.06% from NoAdapt's 85.17%) is higher than TENT (84.80%, −0.37%), CoTTA (83.91%, −1.26%), and SAR (84.52%, −0.65%).
- **Status**: supported
- **Falsification criteria**: If FOA's in-distribution accuracy drops by more than 1% from NoAdapt (85.17%), or if it is lower than any gradient-based method's in-distribution accuracy.
- **Proof**: [E07]
- **Dependencies**: none
- **Tags**: catastrophic forgetting, in-distribution, source domain, clean accuracy

## C07: FOA outperforms TENT and SAR under non-i.i.d. test scenarios
- **Statement**: Under online imbalanced label distribution shifts and mixed domain shifts on ImageNet-C, FOA (62.1%/6.6% ECE and 62.0%/4.9% ECE) outperforms both TENT (60.2%/17.7% and 56.9%/29.2%) and SAR (60.8%/7.5% and 61.4%/14.8%).
- **Status**: supported
- **Falsification criteria**: If FOA accuracy is lower than SAR or TENT in either non-i.i.d. scenario, or ECE is higher than SAR in both scenarios.
- **Proof**: [E08]
- **Dependencies**: C01
- **Tags**: non-i.i.d., label shift, domain shift, robustness, online adaptation
