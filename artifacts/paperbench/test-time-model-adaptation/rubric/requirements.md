# Rubric Requirements — test-time-model-adaptation
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 163

## Method Implementation

### R01: Code has been implemented such that a ViT-Base model pre-tra...
- **Rubric ID**: vit-base
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that a ViT-Base model pre-trained on ImageNet-1K can be loaded into memory using the timm repository
- **Parent context**: The required model architectures and pretrained weights are obtained

### R02: Code has been implemented such that a ResNet-50 model pre-tr...
- **Rubric ID**: resnet50
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that a ResNet-50 model pre-trained on ImageNet-1K can be loaded into memory
- **Parent context**: The required model architectures and pretrained weights are obtained

### R03: Quantized 8-bit and 6-bit ViT-Base models are created using...
- **Rubric ID**: quantized-models
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: Quantized 8-bit and 6-bit ViT-Base models are created using PTQ4ViT, using 32 randomly selected training samples from the ImageNet-1K training set as training data
- **Parent context**: The required model architectures and pretrained weights are obtained

### R04: The LAME baseline is implemented from https://github.com/fiv...
- **Rubric ID**: lame-implementation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The LAME baseline is implemented from https://github.com/fiveai/LAME
- **Parent context**: The gradient-free baseline methods are implemented correctly

### R05: The T3A baseline is implemented from https://github.com/mats...
- **Rubric ID**: t3a-implementation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The T3A baseline is implemented from https://github.com/matsuolab/T3A
- **Parent context**: The gradient-free baseline methods are implemented correctly

### R06: The TENT baseline is implemented from https://github.com/Deq...
- **Rubric ID**: tent-implementation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The TENT baseline is implemented from https://github.com/DequanWang/tent
- **Parent context**: The gradient-based baseline methods are implemented correctly

### R07: The CoTTA baseline is implemented from https://github.com/qi...
- **Rubric ID**: cotta-implementation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The CoTTA baseline is implemented from https://github.com/qinenergy/cotta
- **Parent context**: The gradient-based baseline methods are implemented correctly

### R08: The SAR baseline is implemented from https://github.com/mr-e...
- **Rubric ID**: sar-implementation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The SAR baseline is implemented from https://github.com/mr-eggplant/SAR
- **Parent context**: The gradient-based baseline methods are implemented correctly

### R09: In COTTA, for images below the threshold, 32 augmentations a...
- **Rubric ID**: e03e23d6-98c1-476c-90df-280bc268b90f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In COTTA, for images below the threshold, 32 augmentations are used, including color jitter, random affine, Gaussian blur, random horizontal flip, and Gaussian noise
- **Parent context**: The CoTTA hyperparameters are setup

### R10: A mechanism is implemented to calculate and store the source...
- **Rubric ID**: new-uuid-source-stats
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: A mechanism is implemented to calculate and store the source domain statistics (mean and standard deviation) of the N-th layer's CLS token features, computed over a set of source training samples.
- **Parent context**: The CMA-based prompt adaptation module is implemented

### R11: The input prompt mechanism is implemented to add learnable p...
- **Rubric ID**: prompt-insertion
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The input prompt mechanism is implemented to add learnable prompts to the inputs following the required arrangement: [CLS token, learnable prompts, patch embeddings].
- **Parent context**: The CMA-based prompt adaptation module is implemented

### R12: Given a population size K, the t-th prompt $p^{(t)}_k$ is sa...
- **Rubric ID**: 8cc7f4ee-e809-4b43-81cd-f6e34bef05de
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Given a population size K, the t-th prompt $p^{(t)}_k$ is sampled K times i.i.d. (k=1,...,K) via $p^{(t)}_k \sim m^{(t)} + \tau^{(t)} \mathcal{N}(0, \sigma^{(t)})$, where $m^{(t)}$ is the mean vector, $\tau^{(t)}$ is the step size, and $\sigma^{(t)}$ is the covariance matrix at iteration t.
- **Parent context**: The CMA evolution strategy optimizer is implemented with population sampling and parameter updates a...

### R13: Each prompt p^{(t)}_k is concatenated with the embeddings of...
- **Rubric ID**: 6fce355f-d43f-467d-b7ba-c324ff4cb17d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Each prompt p^{(t)}_k is concatenated with the embeddings of test batch X_t as input to the model, producing fitness values v_k. These K fitness values are then used to update the parameters via the CMA algorithm.
- **Parent context**: The CMA evolution strategy optimizer is implemented with population sampling and parameter updates a...

### R14: A mechanism is implemented to calculate and store the source...
- **Rubric ID**: source-statistics
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: A mechanism is implemented to calculate and store the source domain statistics (mean and standard deviation) of the N-th layer's CLS token features, computed over a set of source training samples.
- **Parent context**: The back-to-source activation shifting mechanism is implemented

### R15: For each batch of elements $X_t$, the mean of the elements i...
- **Rubric ID**: dfa8753b-5321-4f0f-b455-40f12edf0e41
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each batch of elements $X_t$, the mean of the elements is computed as $\mu_N(X_t)$.
- **Parent context**: The activation shifting mechanism with dynamic direction updates using exponential moving averages i...

### R16: For each batch of elements $X_t$, an update is made as $\mu_...
- **Rubric ID**: 6ae1951a-9046-4c4f-8b80-2dced089f876
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each batch of elements $X_t$, an update is made as $\mu_N(t) = \alpha * \mu_N(X_t) + (1 - \alpha) * \mu_N(t-1)$, where $\alpha$ is a configurable hyperparameter.
- **Parent context**: The activation shifting mechanism with dynamic direction updates using exponential moving averages i...

### R17: The shifting direction $d_t$ is set to $\mu^S_N - \mu_N(t)$,...
- **Rubric ID**: 37a2aa82-25db-467c-ac20-52110ea68af0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The shifting direction $d_t$ is set to $\mu^S_N - \mu_N(t)$, where $\mu^S_N$ is the mean of the $N$-th final layer CLS feature calculated over source in-distribution samples $\mathcal{D}_S$.
- **Parent context**: The activation shifting mechanism with dynamic direction updates using exponential moving averages i...

### R18: To shift the output of the OOD data points from the t-th bat...
- **Rubric ID**: 88178132-a2d9-4804-9516-b5e9d31d1a49
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: To shift the output of the OOD data points from the t-th batch to match the in-distribution domain, $\gamma * d_t$ is added to the $N$-th layer's CLS feature $e^0_N$, where gamma is a configurable hyperparameter.
- **Parent context**: The activation shifting mechanism with dynamic direction updates using exponential moving averages i...

### R19: The activation shifting moving average muN(0) is correctly i...
- **Rubric ID**: activation-shifting-initialization
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The activation shifting moving average muN(0) is correctly initialized using the statistics of the first batch muN(X1).
- **Parent context**: The back-to-source activation shifting mechanism is implemented

### R20: Two storage mechanisms are implemented for interval-based up...
- **Rubric ID**: 715c6377-fa52-4f44-8ed9-313bb0a8b630
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Two storage mechanisms are implemented for interval-based updates: FOA-I V1 stores CLS token features between updates, while FOA-I V2 stores original input images between updates.
- **Parent context**: FOA-I's interval-based update strategy for single sample processing is implemented correctly.

### R21: After every I samples, CMA optimization is performed using a...
- **Rubric ID**: interval-update
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: After every I samples, CMA optimization is performed using all stored samples as a batch, followed by deleting all I stored samples.
- **Parent context**: FOA-I's interval-based update strategy for single sample processing is implemented correctly.

### R22: Model inference is correctly performed all the samples via a...
- **Rubric ID**: forward-pass
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Model inference is correctly performed all the samples via a forward pass.
- **Parent context**: FOA-I's interval-based update strategy for single sample processing is implemented correctly.

### R23: Quantizing models to 8 bits reduces memory usage.
- **Rubric ID**: 57793664-3d52-444d-b5aa-023b4a4ad271
- **Category**: Result Analysis / Method Implementation
- **Weight**: 1
- **Requirement**: Quantizing models to 8 bits reduces memory usage.
- **Parent context**: The memory usage results are consistent with Table 7.

### R24: Code is implemented to allow training only the normalization...
- **Rubric ID**: norm-layer-training
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code is implemented to allow training only the normalization layer parameters of ViT-Base while keeping other parameters frozen
- **Parent context**: Support for selectively training different components of ViT-Base is implemented

### R25: Code is implemented to allow training only the input prompt...
- **Rubric ID**: prompt-training
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code is implemented to allow training only the input prompt parameters while keeping the ViT-Base model parameters frozen
- **Parent context**: Support for selectively training different components of ViT-Base is implemented

### R26: SGD optimizer is implemented with momentum of 0.9 and config...
- **Rubric ID**: sgd-implementation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: SGD optimizer is implemented with momentum of 0.9 and configurable learning rate
- **Parent context**: Different optimizer implementations are developed

### R27: CMA optimizer is implemented with configurable population si...
- **Rubric ID**: cma-implementation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: CMA optimizer is implemented with configurable population size and step size
- **Parent context**: Different optimizer implementations are developed

### R28: Entropy minimization loss is implemented for test-time adapt...
- **Rubric ID**: entropy-loss
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Entropy minimization loss is implemented for test-time adaptation
- **Parent context**: Different loss function implementations are developed

### R29: The fitness function from Equation 5 combining entropy and a...
- **Rubric ID**: fitness-loss
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The fitness function from Equation 5 combining entropy and activation discrepancy is implemented
- **Parent context**: Different loss function implementations are developed

### R30: Using prompts with CMA and the devised fitness function achi...
- **Rubric ID**: prompt-effectiveness
- **Category**: Result Analysis / Method Implementation
- **Weight**: 1
- **Requirement**: Using prompts with CMA and the devised fitness function achieves effective performance.
- **Parent context**: The results are consistent with Table 9 showing the effects of different design choices.

### R31: A new learnable 7x7 Conv layer is implemented with the same...
- **Rubric ID**: resnet-prompt-layer
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: A new learnable 7x7 Conv layer is implemented with the same number of input and output channels as the input image (3).
- **Parent context**: The prompt mechanism for ResNet-50 is implemented correctly by using a learnable 7x7 Conv layer to g...

### R32: The Conv layer weights are initialized with uniform initiali...
- **Rubric ID**: resnet-prompt-init
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The Conv layer weights are initialized with uniform initialization, similar to ViT prompts.
- **Parent context**: The prompt mechanism for ResNet-50 is implemented correctly by using a learnable 7x7 Conv layer to g...

### R33: The prompt output is element-wise added to the input image b...
- **Rubric ID**: resnet-prompt-addition
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The prompt output is element-wise added to the input image before being passed to the ResNet model.
- **Parent context**: The prompt mechanism for ResNet-50 is implemented correctly by using a learnable 7x7 Conv layer to g...

### R34: BN Adapt is implemented to update batch normalization statis...
- **Rubric ID**: resnet-bn-setup
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: BN Adapt is implemented to update batch normalization statistics using test time samples with batch size 64.
- **Parent context**: The baseline methods (NoAdapt, BN Adapt) are evaluated on ResNet-50 on ImageNet-C Gaussian noise lev...

### R35: N_p=3 learnable prompt embeddings are created with the same...
- **Rubric ID**: mamba-prompt-creation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: N_p=3 learnable prompt embeddings are created with the same dimension as patch embeddings and initialized with uniform initialization.
- **Parent context**: The prompt mechanism for VisionMamba is implemented correctly by concatenating learnable input promp...

### R36: The prompts are concatenated at the beginning of the sequenc...
- **Rubric ID**: mamba-prompt-concat
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The prompts are concatenated at the beginning of the sequence of patch embeddings, before being passed to the VisionMamba blocks.
- **Parent context**: The prompt mechanism for VisionMamba is implemented correctly by concatenating learnable input promp...

### R37: The attention masks and position embeddings are adjusted to...
- **Rubric ID**: mamba-mask-handling
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The attention masks and position embeddings are adjusted to account for the additional prompt tokens.
- **Parent context**: The prompt mechanism for VisionMamba is implemented correctly by concatenating learnable input promp...

## Dataset and Model Acquisition

### R38: Code has been implemented such that a VisionMamba model pre-...
- **Rubric ID**: visionmamba
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been implemented such that a VisionMamba model pre-trained on ImageNet-1K can be loaded into memory
- **Parent context**: The required model architectures and pretrained weights are obtained

### R39: The ImageNet-1K dataset is obtained.
- **Rubric ID**: 07ab27df-589c-4896-b667-93ca6e0c7a05
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The ImageNet-1K dataset is obtained.
- **Parent context**: All required datasets for evaluating out-of-distribution generalization are available

### R40: The ImageNet-C dataset is obtained, which contains corrupted...
- **Rubric ID**: e66011b0-67aa-4e40-8b89-028c61e5cd61
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The ImageNet-C dataset is obtained, which contains corrupted images in 15 types and 5 severity levels for each type.
- **Parent context**: All required datasets for evaluating out-of-distribution generalization are available

### R41: The ImageNet-R dataset containing artistic renditions of 200...
- **Rubric ID**: imagenet-r
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The ImageNet-R dataset containing artistic renditions of 200 ImageNet classes is obtained
- **Parent context**: All required datasets for evaluating out-of-distribution generalization are available

### R42: The ImageNet-V2 matched frequency subset dataset is obtained
- **Rubric ID**: imagenet-v2
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The ImageNet-V2 matched frequency subset dataset is obtained
- **Parent context**: All required datasets for evaluating out-of-distribution generalization are available

### R43: The ImageNet-Sketch dataset containing black and white sketc...
- **Rubric ID**: imagenet-sketch
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The ImageNet-Sketch dataset containing black and white sketches is obtained
- **Parent context**: All required datasets for evaluating out-of-distribution generalization are available

### R44: The original ImageNet validation set is loaded without any c...
- **Rubric ID**: f6b90573-15df-4859-85f3-2e816bcdf969
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original ImageNet validation set is loaded without any corruptions or modifications.
- **Parent context**: The in-distribution performance comparison is reproduced.

## Experimental Setup

### R45: LAME uses a batch size of 64
- **Rubric ID**: 656e67f1-0777-4e04-a5e7-1bc55e1eae7c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: LAME uses a batch size of 64
- **Parent context**: The LAME hyperparameters are setup

### R46: For the kNN affinity matrix in LAME, $k=5$
- **Rubric ID**: 537a4b4a-345d-47b5-9146-ecce04342a68
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For the kNN affinity matrix in LAME, $k=5$
- **Parent context**: The LAME hyperparameters are setup

### R47: T3A uses a batch size of 64
- **Rubric ID**: 955216ec-c8dd-4734-8409-c8d8c1082670
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: T3A uses a batch size of 64
- **Parent context**: The T3A hyperparameters are setup

### R48: In T3A, the number of supports to restore $M$ is set to 20
- **Rubric ID**: 12e08875-9130-45b4-9a69-94178bcd8294
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In T3A, the number of supports to restore $M$ is set to 20
- **Parent context**: The T3A hyperparameters are setup

### R49: TENT uses a batch size of 64
- **Rubric ID**: caabc6a0-056f-4bd6-9994-b48c645ee976
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: TENT uses a batch size of 64
- **Parent context**: The TENT hyperparameters are setup

### R50: TENT uses SGD as the update rule
- **Rubric ID**: 4402b969-ad0c-401b-b475-2574749898bb
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: TENT uses SGD as the update rule
- **Parent context**: The TENT hyperparameters are setup

### R51: TENT uses a momentum of 0.9
- **Rubric ID**: ccc0dd8a-31c6-490d-aa37-4f7c642edf7a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: TENT uses a momentum of 0.9
- **Parent context**: The TENT hyperparameters are setup

### R52: TENT uses a learning rate of 0.001
- **Rubric ID**: df17b005-f142-47e8-9286-1efa94d7905d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: TENT uses a learning rate of 0.001
- **Parent context**: The TENT hyperparameters are setup

### R53: In CoTTA, SGD is used as the optimizer
- **Rubric ID**: 134750d0-e559-457a-a05c-b19d25330492
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In CoTTA, SGD is used as the optimizer
- **Parent context**: The CoTTA hyperparameters are setup

### R54: In CoTTA, momentum=0.9 is used
- **Rubric ID**: 0c456209-b018-4be2-a9c7-8f37c7054ad3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In CoTTA, momentum=0.9 is used
- **Parent context**: The CoTTA hyperparameters are setup

### R55: In CoTTA, a learning rate of 0.05 is used
- **Rubric ID**: 80160b60-f7b2-403b-aa54-d91dd652fcf0
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In CoTTA, a learning rate of 0.05 is used
- **Parent context**: The CoTTA hyperparameters are setup

### R56: In CoTTA, a batch size of 64 is used
- **Rubric ID**: 476efd2f-57c6-4b5d-9f14-390af179b353
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In CoTTA, a batch size of 64 is used
- **Parent context**: The CoTTA hyperparameters are setup

### R57: In COTTA, the augmentation threshold $p_{th}$ is set to 0.1
- **Rubric ID**: 4f065829-610e-4af4-91dd-816dec9ae57e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In COTTA, the augmentation threshold $p_{th}$ is set to 0.1
- **Parent context**: The CoTTA hyperparameters are setup

### R58: In COTTA, the restoration probability is set to 0.01, and th...
- **Rubric ID**: c3ed3ffe-bc19-4615-88da-b6f38d8b34d0
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In COTTA, the restoration probability is set to 0.01, and the EMA factor $\\alpha$ for teacher update is set to 0.999
- **Parent context**: The CoTTA hyperparameters are setup

### R59: SAR uses SGD as its optimizer
- **Rubric ID**: 2500492e-6bf8-415b-9e8c-e492bcea9f2d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: SAR uses SGD as its optimizer
- **Parent context**: The SAR hyperparameters are setup

### R60: SAR uses momentum=0.9
- **Rubric ID**: 891b9f8e-9a71-41d8-8498-db75c554f37b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: SAR uses momentum=0.9
- **Parent context**: The SAR hyperparameters are setup

### R61: SAR uses a learning rate of 0.001
- **Rubric ID**: fb2c9926-ef49-465d-8794-5201caa9c15c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: SAR uses a learning rate of 0.001
- **Parent context**: The SAR hyperparameters are setup

### R62: SAR uses a batch size of 64
- **Rubric ID**: a643ce62-16f3-49aa-84c5-5f55ffd03b1e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: SAR uses a batch size of 64
- **Parent context**: The SAR hyperparameters are setup

### R63: In SAR the entropy threshold is $E_0$ is set to $0.4\\times\...
- **Rubric ID**: 95ba7d30-f4d7-4a15-befd-9fc6b3db57ce
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In SAR the entropy threshold is $E_0$ is set to $0.4\\times\\ln C$, where $C$ is the number of task classes
- **Parent context**: The SAR hyperparameters are setup

### R64: In SAR the trainable parameters are the affine parameters of...
- **Rubric ID**: 87cca796-5257-46d8-bcca-2234287aa96b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In SAR the trainable parameters are the affine parameters of the layer normalization modules from blocks1 to blocks8 for ViT-Base
- **Parent context**: The SAR hyperparameters are setup

### R65: The number of prompt embeddings N_p is set to 3.
- **Rubric ID**: 96fe6dab-b94c-4b65-b226-685b2b030530
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The number of prompt embeddings N_p is set to 3.
- **Parent context**: The default hyperparameters for FOA are set correctly.

### R66: Prompts are initialized uniformly.
- **Rubric ID**: 0c2acf08-070a-4f66-8c39-cd6ba26c141b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Prompts are initialized uniformly.
- **Parent context**: The default hyperparameters for FOA are set correctly.

### R67: The batch size (BS) is set to 64.
- **Rubric ID**: c33f98df-8d41-434b-9c27-ce71f7e6d6d1
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The batch size (BS) is set to 64.
- **Parent context**: The default hyperparameters for FOA are set correctly.

### R68: The population size K is set to 28.
- **Rubric ID**: bc867c99-9d7f-4d50-9af6-b46ede203b16
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The population size K is set to 28.
- **Parent context**: The default hyperparameters for FOA are set correctly.

### R69: Lambda is set to 0.4 on ImageNet-C/V2/Sketch
- **Rubric ID**: 69c93e10-4535-477d-84d3-63ce712405e3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Lambda is set to 0.4 on ImageNet-C/V2/Sketch
- **Parent context**: The default hyperparameters for FOA are set correctly.

### R70: Lambda is set to 0.2 on ImageNet-R
- **Rubric ID**: 03d22003-456f-4288-8d22-25a829efdd54
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Lambda is set to 0.2 on ImageNet-R
- **Parent context**: The default hyperparameters for FOA are set correctly.

### R71: For activation shifting, alpha is set to 0.1.
- **Rubric ID**: 7bf85e71-77f0-4f81-836e-03d5d56a9a29
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For activation shifting, alpha is set to 0.1.
- **Parent context**: The default hyperparameters for FOA are set correctly.

### R72: The step size gamma for activation shifting is set to 1.0.
- **Rubric ID**: 38ece210-c07a-4f8d-baf7-7e99a3a203f3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The step size gamma for activation shifting is set to 1.0.
- **Parent context**: The default hyperparameters for FOA are set correctly.

### R73: The model precision is set to 32-bits by default unless othe...
- **Rubric ID**: new-uuid-1
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The model precision is set to 32-bits by default unless otherwise specified.
- **Parent context**: The default hyperparameters for FOA are set correctly.

### R74: FOA is trained for all subsets of the following three compon...
- **Rubric ID**: 44021325-7929-45e0-9900-ca2bce85a5ea
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: FOA is trained for all subsets of the following three components on ImageNet-C: 1) The entropy term in the fitness function, 2) The activation discrepepancy term in the fitness function, 3) Use of activation shifting.
- **Parent context**: The effect of components in FOA is analyzed.

### R75: FOA is trained with population sizes K equal to 2, 3, ..., 2...
- **Rubric ID**: 7cf9ca07-63b7-4610-a7ff-358919edba7e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: FOA is trained with population sizes K equal to 2, 3, ..., 28, on the Gaussian corrputed samples from ImageNet-C.
- **Parent context**: The effect of the population size in FOA is studied.

### R76: FOA is trained with N_p values equal to 1, 2, ..., 10, on th...
- **Rubric ID**: 6f98319e-5966-4e93-835f-d5a9db8cb021
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: FOA is trained with N_p values equal to 1, 2, ..., 10, on the Gaussian corrputed samples from ImageNet-C.
- **Parent context**: The effect of the number of prompt embeddings N_p in FOA is studied.

### R77: FOA is trained with Q values equal to 16, 32, 64, 100, 200,...
- **Rubric ID**: 126f14d6-a8c6-4877-9cd0-06a6a87c2d05
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: FOA is trained with Q values equal to 16, 32, 64, 100, 200, 400, 800, 1600, where Q is the number of source training samples used for calculating the source statistics, on the Gaussian corrupted samples from ImageNet-C.
- **Parent context**: The effect of the number of samples Q for source training statistics is analyzed.

### R78: FOA-I is trained and evaluated with intervals I = {4, 8, 16,...
- **Rubric ID**: intervals-tested
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: FOA-I is trained and evaluated with intervals I = {4, 8, 16, 32, 64} as shown in Table 6.
- **Parent context**: FOA-I is evaluated with different interval values I on ImageNet-C (Gaussian noise level 5).

### R79: The model is trained with different optimizers (SGD vs CMA)...
- **Rubric ID**: optimizer-experiments
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The model is trained with different optimizers (SGD vs CMA) and the accuracy scores and ECE scores are computed
- **Parent context**: The experiments varying model components, optimizers and loss functions are run on ImageNet-C (Gauss...

### R80: The model is trained with different loss functions (entropy...
- **Rubric ID**: loss-experiments
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The model is trained with different loss functions (entropy vs fitness from equation 5) and the accuracy scores and ECE scores are computed
- **Parent context**: The experiments varying model components, optimizers and loss functions are run on ImageNet-C (Gauss...

### R81: Direct replacement of SGD with CMA for entropy-based TTA is...
- **Rubric ID**: cma-entropy-failure
- **Category**: Result Analysis / Experimental Setup
- **Weight**: 1
- **Requirement**: Direct replacement of SGD with CMA for entropy-based TTA is shown to be infeasible (accuracy degrading to a smaller percentage on the order of 0.1%).
- **Parent context**: The results are consistent with Table 9 showing the effects of different design choices.

### R82: NoAdapt, TENT, CoTTA, SAR, and FOA are evaluated with consis...
- **Rubric ID**: 3e77debc-d638-49c8-9597-56ee903b95b2
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: NoAdapt, TENT, CoTTA, SAR, and FOA are evaluated with consistent batch size 64 and using exactly the same validation samples.
- **Parent context**: The in-distribution performance comparison is reproduced.

## Evaluation, Metrics & Benchmarking

### R83: For each $x \in X_t$, the term $\sum_{c \in C} -\hat{y}_c \l...
- **Rubric ID**: dd2b0167-77fd-443c-9b1f-2421bf88de11
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each $x \in X_t$, the term $\sum_{c \in C} -\hat{y}_c \log \hat{y}_c$ is computed, where $X_t$ is the current batch of test samples, $C$ is the set of all classes, and $\hat{y}_c$ is the predicted probability for class c
- **Parent context**: The entropy term is computed correctly, as $\sum_{x \in X_t} \sum_{c \in C} -\hat{y}_c \log \hat{y}_...

### R84: The above expression ($\sum_{c \in C} -\hat{y}_c \log \hat{y...
- **Rubric ID**: 94f30003-f275-41a4-b76c-6fdd51721246
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The above expression ($\sum_{c \in C} -\hat{y}_c \log \hat{y}_c$) is summed over all $x \in X_t$.
- **Parent context**: The entropy term is computed correctly, as $\sum_{x \in X_t} \sum_{c \in C} -\hat{y}_c \log \hat{y}_...

### R85: The difference in means is computed correctly, as the sum ov...
- **Rubric ID**: cdd126eb-86a2-4c3a-91f1-b217bff9456c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The difference in means is computed correctly, as the sum over $x \in X_t$ of $\lambda * ||\mu_i(X_t) - \mu_i^S|| _2$.
- **Parent context**: The fitness function combining prediction entropy and activation distribution discrepancy is impleme...

### R86: The difference in standard deviations is computed correctly,...
- **Rubric ID**: 4c1b3e06-ded8-4fb0-866a-0f09af607afe
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The difference in standard deviations is computed correctly, as the sum over $x \in X_t$ of $||\sigma_i(X_t) - \sigma_i^S||_2$.
- **Parent context**: The fitness function combining prediction entropy and activation distribution discrepancy is impleme...

### R87: The total fitness value is computed correctly by summing all...
- **Rubric ID**: new-uuid-fitness-sum
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The total fitness value is computed correctly by summing all components: the entropy term over X_t and all activation discrepancy terms (means and standard deviations).
- **Parent context**: The fitness function combining prediction entropy and activation distribution discrepancy is impleme...

### R88: Classification accuracy on OOD examples is implemented corre...
- **Rubric ID**: 45191ae5-2021-4571-bb5c-bc45bbd054db
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Classification accuracy on OOD examples is implemented correctly.
- **Parent context**: The evaluation metrics are implemented correctly.

### R89: ECE (expected calibration error), the difference between pre...
- **Rubric ID**: 3487990e-09b6-40b7-9b48-c3321e67898c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: ECE (expected calibration error), the difference between predicted probabilities and actual outcomes in a probabilistic model, is implemented correctly.
- **Parent context**: The evaluation metrics are implemented correctly.

### R90: The accuracies on all 15 corruptions are calculated for the...
- **Rubric ID**: a3892035-d300-4c89-a761-ace7829f33b6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracies on all 15 corruptions are calculated for the baseline methods (NoAdapt, LAME, T3A).
- **Parent context**: The baseline methods (NoAdapt, LAME, T3A) are evaluated on ImageNet-C.

### R91: The ECE scores on all 15 corruptions are calculated for the...
- **Rubric ID**: 09a51455-c656-404b-be52-09999f529fb7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The ECE scores on all 15 corruptions are calculated for the baseline methods (NoAdapt, LAME, T3A).
- **Parent context**: The baseline methods (NoAdapt, LAME, T3A) are evaluated on ImageNet-C.

### R92: The accuracies on all 15 corruptions are calculated for the...
- **Rubric ID**: dd10692c-8196-4073-9555-db4b3034d405
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracies on all 15 corruptions are calculated for the gradient-based methods (TENT, CoTTA, SAR) and FOA.
- **Parent context**: The gradient-based methods (TENT, CoTTA, SAR) and FOA are evaluated on ImageNet-C.

### R93: The ECE scores on all 15 corruptions are calculated for the...
- **Rubric ID**: 413cecbd-59a4-451c-a60c-fad885bf33b5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The ECE scores on all 15 corruptions are calculated for the gradient-based methods (TENT, CoTTA, SAR) and FOA.
- **Parent context**: The gradient-based methods (TENT, CoTTA, SAR) and FOA are evaluated on ImageNet-C.

### R94: FOA has a higher average accuracy score than all other metho...
- **Rubric ID**: 806d13f1-ace2-4a29-b746-97659030f487
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA has a higher average accuracy score than all other methods.
- **Parent context**: The trends of the training methods of ImageNet-C are consistent with those in Section 4.1.

### R95: FOA has a lower average ECE score than all other methods.
- **Rubric ID**: f49179f6-5d63-4117-abbd-2ef7c0325499
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA has a lower average ECE score than all other methods.
- **Parent context**: The trends of the training methods of ImageNet-C are consistent with those in Section 4.1.

### R96: LAME and T3A perform around the same or worse than NoAdapt b...
- **Rubric ID**: 14e863e3-c953-424b-b059-aa126b261f88
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: LAME and T3A perform around the same or worse than NoAdapt both on average accuracy and on average ECE.
- **Parent context**: The trends of the training methods of ImageNet-C are consistent with those in Section 4.1.

### R97: TENT, CoTTA, and SAR have higher average accuracy than the g...
- **Rubric ID**: e358b89e-c75f-448b-812f-734fca9e69d4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: TENT, CoTTA, and SAR have higher average accuracy than the gradient-free methods (LAME and T3A).
- **Parent context**: The trends of the training methods of ImageNet-C are consistent with those in Section 4.1.

### R98: Compared to SAR, the average accuracy of FOA is 2-6% higher.
- **Rubric ID**: e008e8e1-0d6e-4411-8f46-69b07656d430
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Compared to SAR, the average accuracy of FOA is 2-6% higher.
- **Parent context**: The trends of the training methods of ImageNet-C are consistent with those in Section 4.1.

### R99: Compared to SAR, the average ECE of FOA is 2-6% lower.
- **Rubric ID**: 564653b0-70a0-4143-9d2d-5eb90ed2a833
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Compared to SAR, the average ECE of FOA is 2-6% lower.
- **Parent context**: The trends of the training methods of ImageNet-C are consistent with those in Section 4.1.

### R100: FOA's ECE score is more than 10% lower than that of TENT.
- **Rubric ID**: fa981c83-ca1a-4122-bce2-2a5045cf3b13
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA's ECE score is more than 10% lower than that of TENT.
- **Parent context**: The trends of the training methods of ImageNet-C are consistent with those in Section 4.1.

### R101: The accuracies on all 3 benchmarks are calculated for the ba...
- **Rubric ID**: 91f4fde3-cb9a-4899-9689-1ec0456c4d40
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracies on all 3 benchmarks are calculated for the baseline methods (NoAdapt, LAME, T3A).
- **Parent context**: The baseline methods (NoAdapt, LAME, T3A) are evaluated on ImageNet-R, ImageNet-V2, and ImageNet-Ske...

### R102: The ECE scores on all 3 benchmarks are calculated for the ba...
- **Rubric ID**: 76d49374-1496-4dc3-970d-0c2890bca42f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The ECE scores on all 3 benchmarks are calculated for the baseline methods (NoAdapt, LAME, T3A).
- **Parent context**: The baseline methods (NoAdapt, LAME, T3A) are evaluated on ImageNet-R, ImageNet-V2, and ImageNet-Ske...

### R103: The accuracies on all 3 benchmarks are calculated for the gr...
- **Rubric ID**: b384d1f5-f600-4714-ae40-1e0e6d6ee276
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracies on all 3 benchmarks are calculated for the gradient-based methods (TENT, CoTTA, SAR).
- **Parent context**: The gradient-based methods (TENT, CoTTA, SAR) are evaluated on ImageNet-R, ImageNet-V2, and ImageNet...

### R104: The ECE scores on all 3 benchmarks are calculated for the gr...
- **Rubric ID**: e337c8f0-f757-41a8-95bd-d4d4972ea034
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The ECE scores on all 3 benchmarks are calculated for the gradient-based methods (TENT, CoTTA, SAR).
- **Parent context**: The gradient-based methods (TENT, CoTTA, SAR) are evaluated on ImageNet-R, ImageNet-V2, and ImageNet...

### R105: The average accuracy value of FOA is comparable or higher th...
- **Rubric ID**: 0ee5fada-d3a1-4e18-a711-af8189c0c0c2
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy value of FOA is comparable or higher than the average accuracy values of the other methods.
- **Parent context**: The trends of the training methods on ImageNet-R, ImageNet-V2, and ImageNet-Sketch are consistent wi...

### R106: The average ECE value of FOA is comparable or lower than the...
- **Rubric ID**: 6613dcf6-8941-42bb-a969-c03179a75d93
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average ECE value of FOA is comparable or lower than the average ECE values of the other methods.
- **Parent context**: The trends of the training methods on ImageNet-R, ImageNet-V2, and ImageNet-Sketch are consistent wi...

### R107: The accuracies on all 15 corruptions are calculated for the...
- **Rubric ID**: 8bit-accuracy
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracies on all 15 corruptions are calculated for the methods (NoAdapt, T3A, and FOA) using 8-bit quantized ViT
- **Parent context**: The NoAdapt baseline, T3A, and FOA are evaluated using 8-bit quantized ViT on ImageNet-C as in Table...

### R108: The ECE scores on all 15 corruptions are calculated for the...
- **Rubric ID**: 8bit-ece
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The ECE scores on all 15 corruptions are calculated for the methods (NoAdapt, T3A, and FOA) using 8-bit quantized ViT
- **Parent context**: The NoAdapt baseline, T3A, and FOA are evaluated using 8-bit quantized ViT on ImageNet-C as in Table...

### R109: The accuracies on all 15 corruptions are calculated for the...
- **Rubric ID**: 6bit-accuracy
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracies on all 15 corruptions are calculated for the methods (NoAdapt, T3A, and FOA) using 6-bit quantized ViT
- **Parent context**: The NoAdapt baseline, T3A, and FOA are evaluated using 6-bit quantized ViT on ImageNet-C as in Table...

### R110: The ECE scores on all 15 corruptions are calculated for the...
- **Rubric ID**: 6bit-ece
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The ECE scores on all 15 corruptions are calculated for the methods (NoAdapt, T3A, and FOA) using 6-bit quantized ViT
- **Parent context**: The NoAdapt baseline, T3A, and FOA are evaluated using 6-bit quantized ViT on ImageNet-C as in Table...

### R111: FOA outperforms T3A significantly in both accuracy and ECE s...
- **Rubric ID**: foa-t3a-comparison
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA outperforms T3A significantly in both accuracy and ECE scores on both 8-bit and 6-bit models
- **Parent context**: The results of quantized model experiments match the trends reported in Section 4.2

### R112: FOA with 8-bit ViT achieves better accuracy than TENT with 3...
- **Rubric ID**: foa-8bit-tent-32bit
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA with 8-bit ViT achieves better accuracy than TENT with 32-bit ViT (with a > 2% improvement).
- **Parent context**: The results of quantized model experiments match the trends reported in Section 4.2

### R113: The average accuracy and ECE score is computed over all 15 c...
- **Rubric ID**: c6a02904-c8bf-4d68-901e-b68c2b7c39d2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy and ECE score is computed over all 15 corruptions of ImageNet-C on all the runs of FOA.
- **Parent context**: The effect of components in FOA is analyzed.

### R114: CMA with Entropy fitness performs poorer than NoAdapt.
- **Rubric ID**: 8c734773-1093-4409-b402-dc31bd03d82b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: CMA with Entropy fitness performs poorer than NoAdapt.
- **Parent context**: The trends when using different components is consistent with the trends in Section 4.3.

### R115: Using Activation Discrepancy fitness causes a > 5 % increase...
- **Rubric ID**: 4c40bfda-0437-4354-bef3-6a903d6ee43d
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using Activation Discrepancy fitness causes a > 5 % increase in accuracy compared to NoAdapt.
- **Parent context**: The trends when using different components is consistent with the trends in Section 4.3.

### R116: Using only activation shifting causes a > 2 % increase in ac...
- **Rubric ID**: 60c1e713-4492-4558-a5f1-c38655056b52
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using only activation shifting causes a > 2 % increase in accuracy compared to NoAdapt
- **Parent context**: The trends when using different components is consistent with the trends in Section 4.3.

### R117: When combining all three components, the accuracy is compara...
- **Rubric ID**: ec71c4f7-a73b-4dd5-a35e-0f7b336b9a79
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When combining all three components, the accuracy is comparable to or higher than all other component combinations
- **Parent context**: The trends when using different components is consistent with the trends in Section 4.3.

### R118: When combining all three components, the ECE score is compar...
- **Rubric ID**: f0373fea-4f62-4d85-831d-e968cdf0e13b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When combining all three components, the ECE score is comparable to or lower than all other component combinations.
- **Parent context**: The trends when using different components is consistent with the trends in Section 4.3.

### R119: The accuracy and ECE values are computed for the above value...
- **Rubric ID**: ee156450-cd1a-4863-996d-00b569b899da
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy and ECE values are computed for the above values of K, both on FOA and on NoAdapt, on the Gaussian noise corrupted samples from ImageNet-C (severity level 5).
- **Parent context**: The effect of the population size in FOA is studied.

### R120: At K = 2, FOA outperforms NoAdapt and T3A in accuracy.
- **Rubric ID**: 7a05f97c-bf1a-4a37-9aa6-6129b28befad
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: At K = 2, FOA outperforms NoAdapt and T3A in accuracy.
- **Parent context**: The results are consistent with those in Section 4.3.

### R121: At K = 6, FOA is comparable to or is better than TENT in acc...
- **Rubric ID**: 46befbf5-4bc6-41dc-9cba-ec49c08a6936
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: At K = 6, FOA is comparable to or is better than TENT in accuracy.
- **Parent context**: The results are consistent with those in Section 4.3.

### R122: The accuracy of FOA converges as K goes past 15.
- **Rubric ID**: b4b1643c-c2f7-4027-95bf-06dffd840008
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy of FOA converges as K goes past 15.
- **Parent context**: The results are consistent with those in Section 4.3.

### R123: The accuracy and ECE values are computed for the above value...
- **Rubric ID**: be075650-2f5c-4237-92fa-7b6832ce34b7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy and ECE values are computed for the above values of N_p, both on FOA and on NoAdapt, , on the Gaussian noise corrupted samples from ImageNet-C (severity level 5).
- **Parent context**: The effect of the number of prompt embeddings N_p in FOA is studied.

### R124: The ECE only maks minor variations across different values o...
- **Rubric ID**: 51f85c1f-45c8-4f63-b636-cbcb687c43ff
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The ECE only maks minor variations across different values of N_p.
- **Parent context**: The effect of the number of prompt embeddings N_p in FOA is studied.

### R125: The accuracy and ECE values are computed for the above value...
- **Rubric ID**: 1e18930c-fd61-4c7c-9e71-2e0d46018726
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The accuracy and ECE values are computed for the above values of Q, both on FOA and on NoAdapt, , on the Gaussian noise corrupted samples from ImageNet-C (severity level 5).
- **Parent context**: The effect of the number of samples Q for source training statistics is analyzed.

### R126: The accuracy is stable when Q goes past 32.
- **Rubric ID**: 684701d0-8160-4bb6-b7da-aedb1a3f4576
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The accuracy is stable when Q goes past 32.
- **Parent context**: The effect of the number of samples Q for source training statistics is analyzed.

### R127: The ECE is stable when Q goes past 32.
- **Rubric ID**: 4a0dce24-a6c0-4d68-915e-3959c7e0792e
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The ECE is stable when Q goes past 32.
- **Parent context**: The effect of the number of samples Q for source training statistics is analyzed.

### R128: NoAdapt baseline performance is measured.
- **Rubric ID**: noadapt-baseline
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: NoAdapt baseline performance is measured.
- **Parent context**: FOA-I is evaluated with different interval values I on ImageNet-C (Gaussian noise level 5).

### R129: TENT baseline with batch size 64 is measured.
- **Rubric ID**: tent-baseline
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: TENT baseline with batch size 64 is measured.
- **Parent context**: FOA-I is evaluated with different interval values I on ImageNet-C (Gaussian noise level 5).

### R130: FOA-I with I=4 outperforms TENT (with batch size 64), both i...
- **Rubric ID**: interval-4-results
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA-I with I=4 outperforms TENT (with batch size 64), both in terms of accuracy score and ECE score.
- **Parent context**: The results match Table 6 showing accuracies and ECE values for different intervals.

### R131: FOA-I with smaller intervals (e.g., I=4) shows better perfor...
- **Rubric ID**: interval-scaling
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA-I with smaller intervals (e.g., I=4) shows better performance than with I=64.
- **Parent context**: The results match Table 6 showing accuracies and ECE values for different intervals.

### R132: Memory usage is measured for different batch sizes for NoAda...
- **Rubric ID**: memory-measurements
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Memory usage is measured for different batch sizes for NoAdapt, TENT, CoTTA, FOA, and FOA (8-bit), measuring both runtime and peak GPU memory usage.
- **Parent context**: Memory usage is measured for different methods as in Table 7

### R133: Memory usage for 8-bit models is calculated as 0.25x of the...
- **Rubric ID**: memory-8bit
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Memory usage for 8-bit models is calculated as 0.25x of the corresponding 32-bit model measurements, following Liu et al. (2021b).
- **Parent context**: Memory usage is measured for different methods as in Table 7

### R134: Memory usage is measured for different interval lengths for...
- **Rubric ID**: 3100d5c8-761f-4529-8046-f1cd0d6e45fb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Memory usage is measured for different interval lengths for FOA-I V1 (which stores features between updates) and FOA-I V2 (which stores images between updates).
- **Parent context**: Memory usage is measured for different methods as in Table 7

### R135: The memory usage of FOA is comparable or slightly higher tha...
- **Rubric ID**: foa-memory
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The memory usage of FOA is comparable or slightly higher than that of NoAdapt over all batch sizes.
- **Parent context**: The memory usage results are consistent with Table 7.

### R136: FOA uses significantly less memory than gradient-based metho...
- **Rubric ID**: gradient-memory
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA uses significantly less memory than gradient-based methods for all batch sizes.
- **Parent context**: The memory usage results are consistent with Table 7.

### R137: FOA-I V1 and FOA-I V2 use less memory than FOA.
- **Rubric ID**: 2ce903d7-0dc1-424a-8b2a-d07ebaec0e01
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA-I V1 and FOA-I V2 use less memory than FOA.
- **Parent context**: The memory usage results are consistent with Table 7.

### R138: The model is trained with different learnable parameters (no...
- **Rubric ID**: component-experiments
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The model is trained with different learnable parameters (norm layers only vs prompts only) and the accuracy scores and ECE scores are computed
- **Parent context**: The experiments varying model components, optimizers and loss functions are run on ImageNet-C (Gauss...

### R139: The proposed fitness function (Eqn. 5) achieves excellent pe...
- **Rubric ID**: sgd-fitness-effectiveness
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The proposed fitness function (Eqn. 5) achieves excellent performance even with SGD learning, showing significant improvement (> 8% increase in average accuracy) compared to TENT with entropy loss.
- **Parent context**: The results are consistent with Table 9 showing the effects of different design choices.

### R140: The ResNet-50 model pretrained on ImageNet is obtained and e...
- **Rubric ID**: resnet-noadapt-setup
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The ResNet-50 model pretrained on ImageNet is obtained and evaluated without any adaptation.
- **Parent context**: The baseline methods (NoAdapt, BN Adapt) are evaluated on ResNet-50 on ImageNet-C Gaussian noise lev...

### R141: Both methods are evaluated with exactly the same test data s...
- **Rubric ID**: resnet-baseline-eval
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Both methods are evaluated with exactly the same test data samples and ordering.
- **Parent context**: The baseline methods (NoAdapt, BN Adapt) are evaluated on ResNet-50 on ImageNet-C Gaussian noise lev...

### R142: The gradient-based methods (TENT, SAR), NoAdapt, BN Adapt, S...
- **Rubric ID**: resnet-gradient
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The gradient-based methods (TENT, SAR), NoAdapt, BN Adapt, SGD FOA and FOA are evaluated on ResNet-50 on ImageNet-C Gaussian noise level 5.
- **Parent context**: The experiments with ResNet-50 are reproduced

### R143: FOA outperforms BNAdapt, both in accuracy and ECE.
- **Rubric ID**: a7aee4f5-952e-4baa-8925-0ec7fc0266e7
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA outperforms BNAdapt, both in accuracy and ECE.
- **Parent context**: The accuracies and ECE values are consistent with results in Section 4.4 and Table 10.

### R144: FOA has lower accuracy than TENT.
- **Rubric ID**: 63ded527-cd6b-49e1-ade5-c6e1b6fc2cea
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA has lower accuracy than TENT.
- **Parent context**: The accuracies and ECE values are consistent with results in Section 4.4 and Table 10.

### R145: The NoAdapt baseline is evaluated on VisionMamba on ImageNet...
- **Rubric ID**: mamba-baselines
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The NoAdapt baseline is evaluated on VisionMamba on ImageNet-C Gaussian noise level 5.
- **Parent context**: The experiments with VisionMamba are reproduced

### R146: The gradient-based methods (TENT, SAR), NoAdapt, BN Adapt, S...
- **Rubric ID**: mamba-gradient
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The gradient-based methods (TENT, SAR), NoAdapt, BN Adapt, SGD FOA and FOA are evaluated on VisionMamba on ImageNet-C Gaussian noise level 5.
- **Parent context**: The experiments with VisionMamba are reproduced

### R147: FOA achieves accuracy and ECE scores that are comparable to...
- **Rubric ID**: mamba-foa
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA achieves accuracy and ECE scores that are comparable to or better than TENT.
- **Parent context**: The accuracies and ECE values are consistent with results in Table 10.

### R148: FOA achieves accuracy and ECE scores that are comparable to...
- **Rubric ID**: 804f5639-b465-486b-bb6e-4bfdbfc0bfea
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA achieves accuracy and ECE scores that are comparable to or better than SAR.
- **Parent context**: The accuracies and ECE values are consistent with results in Table 10.

### R149: Performance is evaluated on ImageNet-C (severity level 5) te...
- **Rubric ID**: label-shift-eval
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Performance is evaluated on ImageNet-C (severity level 5) test samples arranged in class order.
- **Parent context**: The online imbalanced label shift scenario is implemented correctly.

### R150: Performance is evaluated on the mixed stream containing rand...
- **Rubric ID**: mixed-domain-eval
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Performance is evaluated on the mixed stream containing randomly interleaved samples from all corruption types.
- **Parent context**: The mixed domain shift scenario is implemented correctly.

### R151: The three methods TENT, SAR, FOA are evaluated under the non...
- **Rubric ID**: method-comparison
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The three methods TENT, SAR, FOA are evaluated under the non-i.i.d. conditions (online imbalanced label shift and mixed domain shift).
- **Parent context**: The experiments under online imbalanced label distribution shifts and mixed domain shifts are run as...

### R152: The performance of all methods (TENT, SAR, FOA) shows some d...
- **Rubric ID**: performance-degradation
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The performance of all methods (TENT, SAR, FOA) shows some degradation under non-i.i.d. scenarios compared to i.i.d. scenarios, but FOA's degradation is bounded (ECE increase < 5%, accuracy decrease < 8%).
- **Parent context**: The results match the analysis in Section 4.4 showing FOA's effectiveness under non-i.i.d. settings.

### R153: FOA maintains better performance than TENT and SAR under bot...
- **Rubric ID**: relative-performance
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA maintains better performance than TENT and SAR under both non-i.i.d. settings (online imbalanced label shifts and mixed domain shifts).
- **Parent context**: The results match the analysis in Section 4.4 showing FOA's effectiveness under non-i.i.d. settings.

### R154: For each method, relative accuracy decline from NoAdapt is c...
- **Rubric ID**: relative-decline
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each method, relative accuracy decline from NoAdapt is calculated by subtracting its accuracy from NoAdapt's 85.17% baseline.
- **Parent context**: The results are consistent with those in Section 4.4 and Table 12.

### R155: FOA maintains baseline NoAdapt accuracy with minimal degrada...
- **Rubric ID**: noadapt-comparison
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA maintains baseline NoAdapt accuracy with minimal degradation (< 2 %).
- **Parent context**: The results are consistent with those in Section 4.4 and Table 12.

### R156: FOA outperforms or is comparable to TENT, CoTTA, and SAR in...
- **Rubric ID**: other-methods-comparison
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA outperforms or is comparable to TENT, CoTTA, and SAR in terms of maintaining in-distribution accuracy.
- **Parent context**: The results are consistent with those in Section 4.4 and Table 12.

### R157: FOA achieves lower ECE on in-distribution data compared to N...
- **Rubric ID**: ece-comparison
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FOA achieves lower ECE on in-distribution data compared to NoAdapt
- **Parent context**: The results are consistent with those in Section 4.4 and Table 12.

## Data Processing & Preparation

### R158: The full ImageNet-1K validation set is used for computing so...
- **Rubric ID**: new-uuid-2
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The full ImageNet-1K validation set is used for computing source statistics.
- **Parent context**: The default hyperparameters for FOA are set correctly.

### R159: The statistics $\{\mu^S_i, \sigma^S_i\}^N_{i=0}$ are compute...
- **Rubric ID**: new-uuid-3
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The statistics $\{\mu^S_i, \sigma^S_i\}^N_{i=0}$ are computed and stored for use in FOA.
- **Parent context**: The Forward-Optimization Adaptation (FOA) method is implemented with its core components

### R160: The ImageNet-C test data stream is arranged such that sample...
- **Rubric ID**: label-shift-data
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The ImageNet-C test data stream is arranged such that samples are encountered in class order, with instances from each class appearing consecutively.
- **Parent context**: The online imbalanced label shift scenario is implemented correctly.

### R161: A single data stream is created that randomly mixes test sam...
- **Rubric ID**: mixed-domain-data
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: A single data stream is created that randomly mixes test samples from all 15 corruption types of ImageNet-C.
- **Parent context**: The mixed domain shift scenario is implemented correctly.

### R162: The test data stream is created by randomly interleaving sam...
- **Rubric ID**: mixed-domain-random
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The test data stream is created by randomly interleaving samples from all 15 corruption types of ImageNet-C.
- **Parent context**: The mixed domain shift scenario is implemented correctly.

## Logging, Analysis & Presentation

### R163: The accuracy only makes minor variations across different va...
- **Rubric ID**: 25d31a1a-498a-44a8-8c48-25dd2e06be05
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The accuracy only makes minor variations across different values of N_p.
- **Parent context**: The effect of the number of prompt embeddings N_p in FOA is studied.
