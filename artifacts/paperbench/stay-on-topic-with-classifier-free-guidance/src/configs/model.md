---
# Model Configurations

## GPT-2 Family
- **Models**: GPT-2 small, GPT-2 medium, GPT-2 large, GPT-2 xl
- **Source**: Radford et al. 2019 [62]; OpenAI; HuggingFace `gpt2`, `gpt2-medium`, `gpt2-large`, `gpt2-xl`
- **Architecture**: Decoder-only transformer
- **Used in**: Section 3.1 (zero-shot benchmarks), Appendix D.2 (GPT-J exploratory code), Appendix E.1 (generation samples)
- **Note**: Not specified in paper — exact parameter counts not listed in main text

## Pythia Family
- **Models**: Pythia-160M, 410M, 1B, 1.4B, 2.8B, 6.9B, 12B
- **Source**: Biderman et al. 2023 [11]; EleutherAI; HuggingFace `EleutherAI/pythia-{size}`
- **Architecture**: Decoder-only transformer; consistent training methodology across sizes
- **Used in**: Section 3.1 (zero-shot benchmarks)
- **Evaluation**: EleutherAI LM Evaluation Harness

## LLaMA Family
- **Models**: LLaMA-7B, 13B, 30B, 65B
- **Source**: Touvron et al. 2023 [78]; Meta AI; HuggingFace `huggyllama/llama-{size}`
- **Architecture**: Decoder-only transformer with RoPE positional embeddings
- **Used in**: Section 3.1 (zero-shot benchmarks)
- **Note**: TriviaQA uses substring match (not exact match) per LLaMA evaluation methodology

## CodeGen Family
- **Models**: CodeGen-350M-mono, CodeGen-2B-mono, CodeGen-6B-mono
- **Source**: Nijkamp et al. 2023 [54]; Salesforce; HuggingFace `Salesforce/codegen-{size}-mono`
- **Architecture**: Decoder-only transformer specialized for Python code generation
- **Used in**: Section 3.3 (HumanEval), Appendix D.2
- **Note**: CodeGen-16B-mono omitted due to compute constraints

## WizardLM-30B
- **Model**: WizardLM-30B
- **Source**: Xu et al. 2023 [83]; HuggingFace `WizardLM/WizardLM-30B-V1.0`
- **Architecture**: Instruction-tuned LLaMA variant
- **Used in**: Section 3.2 (CoT experiments on GSM8K)

## Guanaco-65B
- **Model**: Guanaco-65B
- **Source**: Dettmers et al. 2023 [25] (QLoRA); HuggingFace `timdettmers/guanaco-65b-merged`
- **Architecture**: QLoRA fine-tuned LLaMA-65B
- **Used in**: Section 3.2 (CoT experiments on GSM8K and AQuA)

## GPT4All-J v1.3-jazzy
- **Model**: GPT4All-J v1.3-jazzy
- **Source**: Anand et al. 2023 [3]; nomic-ai/gpt4all
- **Architecture**: GPT-J variant fine-tuned on instruction data
- **Used in**: Section 3.4 (chatbot / human evaluation)

## Falcon-7b-Base and Falcon-7b-Instruct
- **Models**: Falcon-7b-Base, Falcon-7b-Instruct
- **Source**: Almazrouei et al. 2023 [2]; HuggingFace `tiiuae/falcon-7b`, `tiiuae/falcon-7b-instruct`
- **Architecture**: Decoder-only transformer with multi-query attention
- **Used in**: Section 5 (entropy analysis, instruction-tuning comparison)

## GPT-J-6B
- **Model**: GPT-J-6B
- **Source**: Wang & Komatsuzaki 2021 [79]; EleutherAI; HuggingFace `EleutherAI/gpt-j-6b`
- **Architecture**: Decoder-only transformer (6B parameters)
- **Used in**: Appendix D.2 (exploratory code generation)

## Translation Models
- **Models**: Bloom-3B (multilingual, 49 languages), RedPajama-Incite-Base-3B (English), mT0 (prompt-tuned seq2seq)
- **Source**: Scao et al. 2022 [72]; Together.xyz; Sanh et al. [52]; HuggingFace
- **Used in**: Appendix D.1 (machine translation on WMT14 fr-en)
