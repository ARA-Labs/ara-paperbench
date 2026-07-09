# Model Configuration

## Model Name
- **Value**: GPT2-medium
- **Rationale**: Widely studied model; mechanistic interpretability tools well-developed for it.
- **Search range**: N/A
- **Sensitivity**: high
- **Source**: §2, §3

## Number of Layers (L)
- **Value**: 24
- **Rationale**: Fixed by GPT2-medium architecture.
- **Search range**: N/A
- **Sensitivity**: N/A
- **Source**: §2

## Hidden Dimension (d)
- **Value**: 1024
- **Rationale**: Fixed by GPT2-medium architecture.
- **Search range**: N/A
- **Sensitivity**: N/A
- **Source**: §2

## MLP Intermediate Dimension (dmlp)
- **Value**: 4096
- **Rationale**: Fixed by GPT2-medium architecture; 4× hidden dimension.
- **Search range**: N/A
- **Sensitivity**: N/A
- **Source**: §2

## MLP Activation Function
- **Value**: GeLU (Gaussian Error Linear Unit)
- **Rationale**: GeLU produces mostly-negative activations for inactive neurons (close to 0), which is mechanistically critical for the antipodal shift explanation.
- **Search range**: N/A
- **Sensitivity**: high (the mechanism relies on GeLU sparsity)
- **Source**: §5.2, Hendrycks & Gimpel (2016)

## Vocabulary Size (|V|)
- **Value**: 50,257 (standard GPT2 BPE vocabulary)
- **Rationale**: Fixed by GPT2 tokenizer.
- **Search range**: N/A
- **Sensitivity**: N/A
- **Source**: Implicit (GPT2-medium standard)

## Number of Toxic Vectors (N)
- **Value**: 128
- **Rationale**: Selected experimentally; similar results obtained with other values.
- **Search range**: Various values tested (not specified); N=128 used in all reported results.
- **Sensitivity**: low
- **Source**: §3.1, footnote 2

## Number of Key Vectors for Un-alignment
- **Value**: 7
- **Rationale**: Minimum number needed to restore toxicity; top-7 by cosine similarity to WToxic.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: §5.3
