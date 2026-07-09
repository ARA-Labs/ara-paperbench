---
# Table 1: Comparison of LLM Adaptation Methods

**Source**: Table 1, §2 (Categorization of LLM Adaptation)
**Claims**: C01
**Description**: Categorization of LLM adaptation methods by five accessibility axes.

✓ = feature present (without requirement) / ✗ = feature absent (requires access)

| Methods | w/o Model Parameters | w/o High-Dim Representation | w/o Token Probabilities | w/o Retrieval Corpus | w/ Smaller Adapter |
|---|---|---|---|---|---|
| **White-Box LLM Fine-Tuning** | | | | | |
| Fine-Tuning (Devlin et al., 2019) | ✗ | ✗ | ✗ | ✓ | ✗ |
| Instruction-Tuning (Wei et al., 2021) | ✗ | ✗ | ✗ | ✓ | ✗ |
| Continual Pre-Training (Gururangan et al., 2020) | ✗ | ✗ | ✗ | ✓ | ✗ |
| Adapter (Houlsby et al., 2019) | ✗ | ✗ | ✗ | ✓ | ✓ |
| Prefix-Tuning (Liu et al., 2022) | ✗ | ✗ | ✗ | ✓ | ✓ |
| LoRA (Hu et al., 2021) | ✗ | ✗ | ✗ | ✓ | ✓ |
| **Grey-Box LLM Adaptation** | | | | | |
| LMaaS (Sun et al., 2022) | ✓ | ✗ | ✗ | ✓ | ✓ |
| kNN-Adapter (Huang et al., 2023) | ✓ | ✓ | ✗ | ✗ | ✓ |
| CombLM (Ormazabal et al., 2023) | ✓ | ✓ | ✗ | ✓ | ✓ |
| IPA (Lu et al., 2023) | ✓ | ✓ | ✗ | ✓ | ✓ |
| Proxy-Tuning (Liu et al., 2024) | ✓ | ✓ | ✗ | ✓ | ✓ |
| **Black-Box LLM Adaptation** | | | | | |
| **BBOX-ADAPTER (Ours)** | ✓ | ✓ | ✓ | ✓ | ✓ |
