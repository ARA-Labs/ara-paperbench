# Model Configuration

## ResNet-18
- **Value**: Standard ResNet-18 (He et al., 2016); 11.2M parameters
- **Rationale**: Widely used CL benchmark model for image classification; requires moderate compute/memory on-device.
- **Search range**: N/A — fixed model choice for real testbed evaluation
- **Sensitivity**: low (model architecture is not Venn's novelty)
- **Source**: §5.1 (CL jobs)

## MobileNet-V2
- **Value**: Standard MobileNet-V2 (Sandler et al., 2018); lightweight mobile model
- **Rationale**: Represents a low-resource CL model suitable for less capable edge devices; validates Venn across model complexity range.
- **Search range**: N/A
- **Sensitivity**: low
- **Source**: §5.1 (CL jobs)

## Dataset: FEMNIST
- **Value**: FEMNIST (Federated EMNIST, Cohen et al., 2017); handwritten letter/digit classification; federated split across many users
- **Rationale**: Standard non-IID federated learning benchmark; data partitioned across edge devices naturally.
- **Search range**: N/A
- **Sensitivity**: low
- **Source**: §5.1 (CL jobs), Figure 9

## Job Demand Range
- **Value**: 1,000 – 10,000 device participants per round (production); 100 clients per round (motivation experiment in §2.3)
- **Rationale**: Reflects real-world Google CL deployment scale (Yang et al., 2018).
- **Search range**: Diverse demands sampled from Figure 8b trace for evaluation
- **Sensitivity**: high — job demand strongly affects scheduling delay and contention
- **Source**: §1 (Introduction), §5.1 (CL jobs), Figure 8b

## Hardware Stratification Thresholds
- **Value**: 4 device regions based on normalized CPU score and normalized memory score thresholds (Figure 8a); exact numerical thresholds not stated in paper — stratification is shown visually as four quadrant-like regions in CPU vs. Memory space.
- **Rationale**: Captures real device heterogeneity from AI Benchmark (Ignatov et al., 2019); creates overlapping eligibility sets for contention evaluation.
- **Search range**: Not specified
- **Sensitivity**: medium
- **Source**: §5.1 (Resources), Figure 8a
