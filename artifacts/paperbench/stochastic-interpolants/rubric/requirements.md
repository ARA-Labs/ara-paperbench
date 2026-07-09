# Rubric Requirements — stochastic-interpolants
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 69

## Method Implementation

### R01: The U-Net architecture implementation from lucidrain's denoi...
- **Rubric ID**: fa71af11-bf4e-47c1-bd63-1733ef30029c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The U-Net architecture implementation from lucidrain's denoising-diffusion-pytorch repository is available
- **Parent context**: U-Net and ImageNet are available

### R02: During training the Dependent Coupling model for in-painting...
- **Rubric ID**: e04c1c97-d217-4385-b328-17086c66bad3
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Dependent Coupling model for in-painting, for each $i$-th sample in each mini-batch, the mask is drawn randomly by tiling the image into 64 tiles of equal sizes; each tile is selected to enter the mask with probability $p = 0.3$
- **Parent context**: During training the Dependent Coupling model for in-painting, for each $i$-th sample in each mini-ba...

### R03: During training the Dependent Coupling model for in-painting...
- **Rubric ID**: 036df75d-d021-4560-b6d0-906ddc881275
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: During training the Dependent Coupling model for in-painting, for each $i$-th sample in each mini-batch, the mask that is computed takes the same value for all channels in a given spatial location
- **Parent context**: During training the Dependent Coupling model for in-painting, for each $i$-th sample in each mini-ba...

### R04: During training the Dependent Coupling model for in-painting...
- **Rubric ID**: 551ad22d-eaf1-42b1-b662-704f748d0c5d
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Dependent Coupling model for in-painting, for each $i$-th sample in each mini-batch, the mask is applied to an image from the ImageNet training set such that masked regions contain random noise, computed as $x_0 = \xi \circ x_1 + (1-\xi) \circ \zeta$, where $\circ$ denotes the Hadamard (elementwise) product, and the random noise $\zeta \in \mathbb{R}^{C \times W \times H}, \zeta \sim N(0, Id)$ is used to initialize the pixels within the masked region (separate noise is used for each channel), and $\xi$ denotes the mask
- **Parent context**: During training the Dependent Coupling model for in-painting, for each $i$-th sample in each mini-ba...

### R05: During training the Dependent Coupling model for in-painting...
- **Rubric ID**: 75cc97d2-9f78-4d91-8cdd-406e86c92c70
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Dependent Coupling model for in-painting, for each $i$-th sample in each mini-batch, a channel is added which is uniformly filled with the sample's class value
- **Parent context**: Training the Dependent Coupling model for in-painting has been implemented, following Algorithm 1

### R06: During training the Dependent Coupling model for in-painting...
- **Rubric ID**: 8c2b4e77-f1ed-4e73-98e9-71be856aa0e2
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Dependent Coupling model for in-painting, for each $i$-th sample in a mini-batch, the interpolant $I_{t_i}$ is computed as $I_{t_i} = t x_0^i + (1-t) x_1^i$, where $x_0$ is the masked image, $x_1$ is the original ImageNet image, and $t$ is the sampled time
- **Parent context**: Training the Dependent Coupling model for in-painting has been implemented, following Algorithm 1

### R07: During training the Dependent Coupling model for in-painting...
- **Rubric ID**: 2326b8d4-922a-42ca-8e25-2fc0d5e546e6
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Dependent Coupling model for in-painting, for each $i$-th sample in a mini-batch, the time-derivative interpolant $\dot{I}_{t_i}$ is computed as $\dot{I}_{t_i} = x_1 - x_0$, where $x_0$ is the masked image, $x_1$ is the original ImageNet image, and $t$ is the sampled time
- **Parent context**: Training the Dependent Coupling model for in-painting has been implemented, following Algorithm 1

### R08: During training the Dependent Coupling model for in-painting...
- **Rubric ID**: 718205ed-8bb4-40d5-8a9a-7c8c4694e4b0
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Dependent Coupling model for in-painting, the approximate velocity field $b_t(x, \xi)$ is defined such that $b_t(x, \xi) = 0$ except in the masked regions of the image; the output of the approximate velocity field is masked to enforce that the unmasked pixels remain fixed. Here, $x$ denotes some image and $\xi$ denotes the conditioning variable. The approximate velocity field only acts on the image, not the additional class channel that has been appended
- **Parent context**: Training the Dependent Coupling model for in-painting has been implemented, following Algorithm 1

### R09: During training the Dependent Coupling model for in-painting...
- **Rubric ID**: cbe7cd9e-8c54-46c7-8b13-b7d36f755814
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Dependent Coupling model for in-painting, the loss for a minibatch is computed as $\hat{L}_b(\hat{b}) = n_b^{-1} \sum_{i=1}^{n_b} \left[ |\hat{b}_{t_i}(I_{t_i})|^2 - 2\dot{I}_{t_i} \cdot \hat{b}_{t_i}(I_{t_i}) \right]$, where $n_b$ is the number of samples in the $i$-th minibatch, $\hat{b}_{t_i}$ is the approximate velocity field, $I_{t_i}$ is the interpolant, and $\dot{I}_{t_i}$ is the time-derivative interpolant
- **Parent context**: Training the Dependent Coupling model for in-painting has been implemented, following Algorithm 1

### R10: During sampling with the Dependent Coupling model for in-pai...
- **Rubric ID**: 4b3e6602-1f2d-4680-978b-cd195cee0d71
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: During sampling with the Dependent Coupling model for in-painting, the mask is drawn randomly by tiling the image into 64 tiles of equal sizes; each tile is selected to enter the mask with probability $p = 0.3$
- **Parent context**: During sampling with the Dependent Coupling model for in-painting, a masked image is first computed

### R11: During sampling with the Dependent Coupling model for in-pai...
- **Rubric ID**: c6ba9100-ddf4-4188-8416-a63081e4ceea
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: During sampling with the Dependent Coupling model for in-painting, the mask that is computed takes the same value for all channels in a given spatial location
- **Parent context**: During sampling with the Dependent Coupling model for in-painting, a masked image is first computed

### R12: During sampling with the Dependent Coupling model for in-pai...
- **Rubric ID**: d9883334-d824-4aee-8f98-ac4eb660fd5c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: During sampling with the Dependent Coupling model for in-painting, the mask is applied to the input image such that masked regions contain random noise, computed as $x_0 = \xi \circ x_1 + (1-\xi) \circ \zeta$, where $\circ$ denotes the Hadamard (elementwise) product, and the random noise $\zeta \in \mathbb{R}^{C \times W \times H}, \zeta \sim N(0, Id)$ is used to initialize the pixels within the masked region (separate noise is used for each channel), and $\xi$ denotes the mask. This input image is from the ImageNet validation or test set
- **Parent context**: During sampling with the Dependent Coupling model for in-painting, a masked image is first computed

### R13: When sampling with the Dependent Coupling model for in-paint...
- **Rubric ID**: 3fd598f3-f9a3-421c-abfc-db3edee67cfe
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When sampling with the Dependent Coupling model for in-painting, for each $i$-th sample in each mini-batch, a channel is added which is uniformly filled with the sample's class value
- **Parent context**: Sampling with the Dependent Coupling model for in-painting has been implemented, following Algorithm...

### R14: When sampling with the Dependent Coupling model for in-paint...
- **Rubric ID**: 35183fae-4786-4b84-b1e7-a49ef31ba90c
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: When sampling with the Dependent Coupling model for in-painting, given $N \in \mathbb{N}$ total iterations, on the $i$-th iteration the sample $\hat{X}_{i+1}$ is computed as $\hat{X}_i + N^{-1}\hat{b}_{i/N}(\hat{X}_i)$, where $\hat{X}_0$ is the original masked image, and $\hat{b}_{i/N}$ is the approximate velocity field at time $i/N$. The final result after $N$ iterations is the in-painted image
- **Parent context**: Sampling with the Dependent Coupling model for in-painting has been implemented, following Algorithm...

### R15: During training the Uncoupled Interpolant model for in-paint...
- **Rubric ID**: f823b47a-bc58-4ab5-b59a-eec1f7b04183
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Uncoupled Interpolant model for in-painting, for each $i$-th sample in each mini-batch, a channel is added which is uniformly filled with the sample's class value
- **Parent context**: Training the Uncoupled Interpolant model for in-painting has been implemented, following Algorithm 1

### R16: During training the Uncoupled Interpolant model for in-paint...
- **Rubric ID**: 3a9c64b6-5def-4278-ae63-f194f873c488
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Uncoupled Interpolant model for in-painting, for each $i$-th sample in a mini-batch, the interpolant $I_{t_i}$ is computed as $I_{t_i} = t x_0^i + (1-t) x_1^i$, where $x_0$ is the noisy image, $x_1$ is the original ImageNet image, and $t$ is the sampled time
- **Parent context**: Training the Uncoupled Interpolant model for in-painting has been implemented, following Algorithm 1

### R17: During training the Uncoupled Interpolant model for in-paint...
- **Rubric ID**: 44d89bd8-3321-4f3d-842f-8e7421e91cdd
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Uncoupled Interpolant model for in-painting, for each $i$-th sample in a mini-batch, the time-derivative interpolant $\dot{I}_{t_i}$ is computed as $\dot{I}_{t_i} = x_1 - x_0$, where $x_0$ is the noisy image, $x_1$ is the original ImageNet image, and $t$ is the sampled time
- **Parent context**: Training the Uncoupled Interpolant model for in-painting has been implemented, following Algorithm 1

### R18: During training the Uncoupled Interpolant model for in-paint...
- **Rubric ID**: 4730f7b6-cbae-4b1f-8527-7c451cc50c97
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Uncoupled Interpolant model for in-painting, the loss for a minibatch is computed as $\hat{L}_b(\hat{b}) = n_b^{-1} \sum_{i=1}^{n_b} \left[ |\hat{b}_{t_i}(I_{t_i})|^2 - 2\dot{I}_{t_i} \cdot \hat{b}_{t_i}(I_{t_i}) \right]$, where $n_b$ is the number of samples in the $i$-th minibatch, $\hat{b}_{t_i}$ is the approximate velocity field, $I_{t_i}$ is the interpolant, and $\dot{I}_{t_i}$ is the time-derivative interpolant
- **Parent context**: Training the Uncoupled Interpolant model for in-painting has been implemented, following Algorithm 1

### R19: During sampling with the Uncoupled Interpolant model for in-...
- **Rubric ID**: 5afccb74-6140-4766-9aa6-8e7c486e7db4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: During sampling with the Uncoupled Interpolant model for in-painting, the initial image is sampled as gaussian noise; $x_0 \sim \mathcal{N}(0, Id)$
- **Parent context**: Sampling with the Uncoupled Interpolant model for in-painting has been implemented, following Algori...

### R20: When sampling with the Uncoupled Interpolant model for in-pa...
- **Rubric ID**: e9d03723-1f93-496f-aaa1-9800fea87b1c
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: When sampling with the Uncoupled Interpolant model for in-painting, given $N \in \mathbb{N}$ total iterations, on the $i$-th iteration the sample $\hat{X}_{i+1}$ is computed as $\hat{X}_i + N^{-1}\hat{b}_{i/N}(\hat{X}_i)$, where $\hat{X}_0$ is the original gaussian noisy image, and $\hat{b}_{i/N}$ is the approximate velocity field at time $i/N$. The final result after $N$ iterations is the in-painted image
- **Parent context**: Sampling with the Uncoupled Interpolant model for in-painting has been implemented, following Algori...

### R21: During training the Dependent Coupling model for super-resol...
- **Rubric ID**: f701ec5c-f4e1-48b7-9f74-cfce8826fadf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: During training the Dependent Coupling model for super-resolution, for each $i$-th sample in each mini-batch, Gaussian noise is added to the downsampled and upsampled ImageNet image; $x_0 = \mathcal{U} ( \mathcal{D} (x_1)) + \zeta$, where $\zeta \sim \mathcal{N}(0, Id)$, $\mathcal{U}$ is the upsampling operation, and $\mathcal{D}$ is the downsampling operation
- **Parent context**: During training the Dependent Coupling model for super-resolution, for each $i$-th sample in each mi...

### R22: During training the Dependent Coupling model for super-resol...
- **Rubric ID**: 36ae2f00-8362-4e46-afa3-84293258b53d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: During training the Dependent Coupling model for super-resolution, for each $i$-th sample in each mini-batch, the image that has been downsampled, upsampled, and had gaussian noise added to it is appended to the original ImageNet image along the channel dimension to create the corrupted image
- **Parent context**: During training the Dependent Coupling model for super-resolution, for each $i$-th sample in each mi...

### R23: During training the Dependent Coupling model for super-resol...
- **Rubric ID**: 6b23bcf6-f14e-4dc7-89f7-10dca66c402e
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Dependent Coupling model for super-resolution, for each $i$-th sample in a mini-batch, the interpolant $I_{t_i}$ is computed as $I_{t_i} = t x_0^i + (1-t) x_1^i$, where $x_0$ is the corrupted image, $x_1$ is the original ImageNet image, and $t$ is the sampled time
- **Parent context**: Training the Dependent Coupling model for super-resolution has been implemented, following Algorithm...

### R24: During training the Dependent Coupling model for super-resol...
- **Rubric ID**: 5aa12bc7-58ad-4119-951b-2d4da8ff82ec
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Dependent Coupling model for super-resolution, for each $i$-th sample in a mini-batch, the time-derivative interpolant $\dot{I}_{t_i}$ is computed as $\dot{I}_{t_i} = x_1 - x_0$, where $x_0$ is the corrupted image, $x_1$ is the original ImageNet image, and $t$ is the sampled time
- **Parent context**: Training the Dependent Coupling model for super-resolution has been implemented, following Algorithm...

### R25: During training the Dependent Coupling model for super-resol...
- **Rubric ID**: b3d613a2-6116-4439-bbe4-e059d15ec476
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Dependent Coupling model for super-resolution, the velocity field only acts on the interpolant image, not the additional class channel that has been appended, or the low-resolution image that has been appended
- **Parent context**: Training the Dependent Coupling model for super-resolution has been implemented, following Algorithm...

### R26: During training the Dependent Coupling model for super-resol...
- **Rubric ID**: ff8dbe4e-1509-44f5-9abe-b2db93a560c9
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: During training the Dependent Coupling model for super-resolution, the loss for a minibatch is computed as $\hat{L}_b(\hat{b}) = n_b^{-1} \sum_{i=1}^{n_b} \left[ |\hat{b}_{t_i}(I_{t_i})|^2 - 2\dot{I}_{t_i} \cdot \hat{b}_{t_i}(I_{t_i}) \right]$, where $n_b$ is the number of samples in the $i$-th minibatch, $\hat{b}_{t_i}$ is the approximate velocity field, $I_{t_i}$ is the interpolant, and $\dot{I}_{t_i}$ is the time-derivative interpolant
- **Parent context**: Training the Dependent Coupling model for super-resolution has been implemented, following Algorithm...

### R27: During sampling with the Dependent Coupling model for super-...
- **Rubric ID**: 52dab287-6086-4c13-88a5-0f804bfbda87
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: During sampling with the Dependent Coupling model for super-resolution, nearest neighbour interpolation is applied to upsample the cropped image back to the original resolution
- **Parent context**: During sampling with the Dependent Coupling model for super-resolution, the corrupted image is corre...

### R28: During sampling with the Dependent Coupling model for super-...
- **Rubric ID**: 3a59ebee-e895-4a9f-b7ee-10edb27cf345
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: During sampling with the Dependent Coupling model for super-resolution, Gaussian noise is added to the downsampled and upsampled ImageNet image; $x_0 = \mathcal{U} ( \mathcal{D} (x_1)) + \zeta$, where $\zeta \sim \mathcal{N}(0, Id)$
- **Parent context**: During sampling with the Dependent Coupling model for super-resolution, the corrupted image is corre...

### R29: When sampling with the Dependent Coupling model for super-re...
- **Rubric ID**: 3c8fd9d0-3819-400f-b04c-1962b0f688d9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When sampling with the Dependent Coupling model for super-resolution, for each $i$-th sample in each mini-batch, a channel is added which is uniformly filled with the sample's class value
- **Parent context**: Sampling with the Dependent Coupling model for super-resolution has been implemented, following Algo...

### R30: When sampling with the Dependent Coupling model for super-re...
- **Rubric ID**: 547af5aa-6d91-40bb-932c-85f92d1b2ea1
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: When sampling with the Dependent Coupling model for super-resolution, given $N \in \mathbb{N}$ total iterations, on the $i$-th iteration the sample $\hat{X}_{i+1}$ is computed as $\hat{X}_i + N^{-1}\hat{b}_{i/N}(\hat{X}_i)$, where $\hat{X}_0$ is the original corrupted image, and $\hat{b}_{i/N}$ is the approximate velocity field at time $i/N$. The final result after $N$ iterations is the image at a higher resolution
- **Parent context**: Sampling with the Dependent Coupling model for super-resolution has been implemented, following Algo...

### R31: The approximate velocity model is implemented as the U-net f...
- **Rubric ID**: 748d82fe-9f02-4d0c-bbb3-b7be65feca15
- **Category**: Code Development / Method Implementation
- **Weight**: 5
- **Requirement**: The approximate velocity model is implemented as the U-net from the lucidrain's denoisingdiffusion-pytorch repository
- **Parent context**: The architecture of the velocity model is implemented correctly

### R32: The U-net velocity model has the "dim_mults" argument set to...
- **Rubric ID**: ba327b00-fdd7-4073-b129-93e5e176e204
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The U-net velocity model has the "dim_mults" argument set to (1, 1, 2, 3, 4) (note the default value for the Unet module from the lucidrain's denoisingdiffusion-pytorch repository is (1, 2, 4, 8))
- **Parent context**: The architecture of the velocity model is implemented correctly

### R33: The U-net velocity model has the "dim" argument set to 256 (...
- **Rubric ID**: 0bd8d434-8fae-4159-b89b-199a83f18bbf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The U-net velocity model has the "dim" argument set to 256 (note there is no default value for the Unet module from the lucidrain's denoisingdiffusion-pytorch repository for the dim argument)
- **Parent context**: The architecture of the velocity model is implemented correctly

### R34: The U-net velocity model has the "learned_sinusoidal_cond" a...
- **Rubric ID**: 9c00369e-a138-48b5-b2e7-d8abe24fba7a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The U-net velocity model has the "learned_sinusoidal_cond" argument set to True (note the default value for the Unet module from the lucidrain's denoisingdiffusion-pytorch repository is False)
- **Parent context**: The architecture of the velocity model is implemented correctly

### R35: The U-net velocity model has the "learned_sinusoidal_dim" ar...
- **Rubric ID**: 33409f2f-bbef-4e46-bb41-b2d3e0787ca4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The U-net velocity model has the "learned_sinusoidal_dim" argument set to 32 (note the default value for the Unet module from the lucidrain's denoisingdiffusion-pytorch repository is 16)
- **Parent context**: The architecture of the velocity model is implemented correctly

### R36: The Dopri solver from the torchdiffeq library is used to sol...
- **Rubric ID**: ebc3e8cf-b1bc-43bc-b24f-8168213cbbc1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The Dopri solver from the torchdiffeq library is used to solve the ODEs
- **Parent context**: The correct hyperparameters have been implemented

## Dataset and Model Acquisition

### R37: Code for accessing the train and validation sets from the Im...
- **Rubric ID**: 46ca1cd4-7129-4337-98d7-484d69e98ea0
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and validation sets from the ImageNet dataset has been implemented
- **Parent context**: U-Net and ImageNet are available

## Experimental Setup

### R38: During training the Dependent Coupling model for in-painting...
- **Rubric ID**: ee1e4da3-1dd9-4aea-b537-356b46205382
- **Category**: Code Development / Experimental Setup
- **Weight**: 2
- **Requirement**: During training the Dependent Coupling model for in-painting, for each $i$-th sample in each mini-batch, the time $t$ is uniformly sampled between 0 and 1, as $t_i \sim U(0, 1)$
- **Parent context**: Training the Dependent Coupling model for in-painting has been implemented, following Algorithm 1

### R39: During training the Dependent Coupling model for in-painting...
- **Rubric ID**: 8190541a-ba46-4229-bd12-5d9bc99b0ac6
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: During training the Dependent Coupling model for in-painting, the model is trained using the Adam optimizer
- **Parent context**: Training the Dependent Coupling model for in-painting has been implemented, following Algorithm 1

### R40: During training the Uncoupled Interpolant model for in-paint...
- **Rubric ID**: 3f74c905-def6-44eb-a739-1e17ce51fa8f
- **Category**: Code Development / Experimental Setup
- **Weight**: 2
- **Requirement**: During training the Uncoupled Interpolant model for in-painting, for each $i$-th sample in each mini-batch, the initial image is sampled as gaussian noise; $x_0 \sim \mathcal{N}(0, Id)$
- **Parent context**: Training the Uncoupled Interpolant model for in-painting has been implemented, following Algorithm 1

### R41: During training the Uncoupled Interpolant model for in-paint...
- **Rubric ID**: d5402a39-7e66-47ae-a577-686aeceb7e0b
- **Category**: Code Development / Experimental Setup
- **Weight**: 2
- **Requirement**: During training the Uncoupled Interpolant model for in-painting, for each $i$-th sample in each mini-batch, the time $t$ is uniformly sampled between 0 and 1, as $t_i \sim U(0, 1)$
- **Parent context**: Training the Uncoupled Interpolant model for in-painting has been implemented, following Algorithm 1

### R42: During training the Uncoupled Interpolant model for in-paint...
- **Rubric ID**: 74e1ae29-3878-4030-b964-b9b46d8ce6d2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: During training the Uncoupled Interpolant model for in-painting, the model is trained using the Adam optimizer
- **Parent context**: Training the Uncoupled Interpolant model for in-painting has been implemented, following Algorithm 1

### R43: During training the Dependent Coupling model for super-resol...
- **Rubric ID**: d790efdd-c92c-4eca-8a98-808e228e5282
- **Category**: Code Development / Experimental Setup
- **Weight**: 2
- **Requirement**: During training the Dependent Coupling model for super-resolution, for each $i$-th sample in each mini-batch, the time $t$ is uniformly sampled between 0 and 1, as $t_i \sim U(0, 1)$
- **Parent context**: Training the Dependent Coupling model for super-resolution has been implemented, following Algorithm...

### R44: During training the Dependent Coupling model for super-resol...
- **Rubric ID**: 75958462-f3ab-4b2a-8bb1-688647a26ef6
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: During training the Dependent Coupling model for super-resolution, the model is trained using the Adam optimizer
- **Parent context**: Training the Dependent Coupling model for super-resolution has been implemented, following Algorithm...

### R45: The U-net velocity model has the "attn_dim_head" hyperparame...
- **Rubric ID**: c4401ce0-0110-4207-81b6-2193ea7abe15
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The U-net velocity model has the "attn_dim_head" hyperparameter set to 64 (note the default value for the Unet module from the lucidrain's denoisingdiffusion-pytorch repository is 32)
- **Parent context**: The architecture of the velocity model is implemented correctly

### R46: The U-net velocity model has the "attn_heads" hyperparameter...
- **Rubric ID**: f0329e30-4cd9-41d8-9916-8af46fb59b83
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The U-net velocity model has the "attn_heads" hyperparameter set to 4 (note the default value for the Unet module from the lucidrain's denoisingdiffusion-pytorch repository is 4)
- **Parent context**: The architecture of the velocity model is implemented correctly

### R47: The U-net velocity model has the "random_fourier_features" h...
- **Rubric ID**: eaf72173-961d-4f44-aad3-a67eb4298868
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The U-net velocity model has the "random_fourier_features" hyperparameter set to False (note the default value for the Unet module from the lucidrain's denoisingdiffusion-pytorch repository is False)
- **Parent context**: The architecture of the velocity model is implemented correctly

### R48: A learning rate scheduler is used, which starts at a learnin...
- **Rubric ID**: 67af86d8-2639-49fb-9a96-9e3c90812565
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: A learning rate scheduler is used, which starts at a learning rate of 2e-4 and scaling the learning rate by $\gamma=0.99$ every $N=1000$ steps
- **Parent context**: The correct hyperparameters have been implemented

### R49: Weight decay is not used
- **Rubric ID**: cd04efc2-b2b5-493f-b412-c32f72f7fdba
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Weight decay is not used
- **Parent context**: The correct hyperparameters have been implemented

### R50: Gradient norms are clipped at 10,000 (this is the norm of th...
- **Rubric ID**: cb0f23e1-3efc-49cc-a71b-28a65ab3bb22
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Gradient norms are clipped at 10,000 (this is the norm of the entire set of parameters taken as a vector, the default type of norm clipping in PyTorch library)
- **Parent context**: The correct hyperparameters have been implemented

### R51: All models are trained with a batch size of 32
- **Rubric ID**: 7de84bdb-63f9-4a76-99f9-ae89546b1f32
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All models are trained with a batch size of 32
- **Parent context**: The correct hyperparameters have been implemented

### R52: All models are trained for 200,000 gradient steps
- **Rubric ID**: 7c7ebd70-364d-4bae-ac1c-dcc3ce514c4a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All models are trained for 200,000 gradient steps
- **Parent context**: The correct hyperparameters have been implemented

### R53: The Uncoupled Interpolant model is trained on ImageNet
- **Rubric ID**: 1fb894bd-0b1c-40a4-b1bf-fc67d4ccf7da
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The Uncoupled Interpolant model is trained on ImageNet
- **Parent context**: The experiments required to replicate results in Section 4.1 have been executed

### R54: The Dependent Coupling model is trained on ImageNet
- **Rubric ID**: 2933a4be-d28a-4bc0-bd5e-dac5e7d37560
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The Dependent Coupling model is trained on ImageNet
- **Parent context**: The experiments required to replicate results in Section 4.1 have been executed

### R55: The Dependent Coupling model is trained on ImageNet
- **Rubric ID**: 04e0713d-8d4c-40a8-9386-4f21adbf5fe7
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The Dependent Coupling model is trained on ImageNet
- **Parent context**: The experiments required to replicate results in Section 4.1 have been executed

## Data Processing & Preparation

### R56: During training the Dependent Coupling model for super-resol...
- **Rubric ID**: 74ebafd7-96dc-4ff9-bf22-4da0158b0265
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: During training the Dependent Coupling model for super-resolution, for each $i$-th sample in each mini-batch, an image from the ImageNet training set is first downsampled by cropping to 64x64 if the original resolution was 256x256, or it is cropped to 256x256 if the original resolution was 512x512
- **Parent context**: During training the Dependent Coupling model for super-resolution, for each $i$-th sample in each mi...

### R57: During training the Dependent Coupling model for super-resol...
- **Rubric ID**: af9c0ad4-8e25-4f4e-bd78-78bbaa8bb869
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: During training the Dependent Coupling model for super-resolution, for each $i$-th sample in each mini-batch, nearest neighbour interpolation is applied to upsample the cropped image back to the original resolution
- **Parent context**: During training the Dependent Coupling model for super-resolution, for each $i$-th sample in each mi...

### R58: During training the Dependent Coupling model for super-resol...
- **Rubric ID**: f118676d-f100-4a4c-810e-43758c7183fc
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 2
- **Requirement**: During training the Dependent Coupling model for super-resolution, for each $i$-th sample in each mini-batch, a channel is added which is uniformly filled with the sample's class value
- **Parent context**: Training the Dependent Coupling model for super-resolution has been implemented, following Algorithm...

### R59: During sampling with the Dependent Coupling model for super-...
- **Rubric ID**: 9108d07c-f475-4133-8307-619b14f82a03
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: During sampling with the Dependent Coupling model for super-resolution, an image from the ImageNet validation or test set is sampled, then it is first downsampled by cropping to 64x64 if the original resolution was 256x256, or it is cropped to 256x256 if the original resolution was 512x512
- **Parent context**: During sampling with the Dependent Coupling model for super-resolution, the corrupted image is corre...

### R60: During sampling with the Dependent Coupling model for super-...
- **Rubric ID**: 9d2ac48f-1d73-41d9-ac3d-24df7f9ea6a9
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: During sampling with the Dependent Coupling model for super-resolution, the image that has been downsampled, upsampled, and had gaussian noise added to it is appended to the original ImageNet image along the channel dimension to create the corrupted image
- **Parent context**: During sampling with the Dependent Coupling model for super-resolution, the corrupted image is corre...

## Evaluation, Metrics & Benchmarking

### R61: The Frechet Inception Distance (FID) metric has been impleme...
- **Rubric ID**: 190a2c3f-cc9d-4fa7-ac4a-119bcc1d3419
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Frechet Inception Distance (FID) metric has been implemented
- **Parent context**: The core contributions of the paper "Stochastic Interpolants with Data-Dependent Couplings" have bee...

### R62: Using the Uncoupled Interpolant model that has been trained...
- **Rubric ID**: 948edecc-0bbb-42e9-b2a1-0ecf3dab4e1a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the Uncoupled Interpolant model that has been trained on ImageNet, FID-50k is computed on the ImageNet validation set
- **Parent context**: The experiments required to replicate results in Section 4.1 have been executed

### R63: Using the Dependent Coupling model that has been trained on...
- **Rubric ID**: 9edcca4e-a0ce-44e7-b200-4c8298bb5986
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the Dependent Coupling model that has been trained on ImageNet, FID-50k is computed on the ImageNet validation set
- **Parent context**: The experiments required to replicate results in Section 4.1 have been executed

### R64: The Uncoupled Interpolant model achieves FID-50k around 1.35
- **Rubric ID**: 499e91ba-45c2-410a-8f1a-15cdb5ad2394
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Uncoupled Interpolant model achieves FID-50k around 1.35
- **Parent context**: The recorded metrics show that the results from Section 4.1 have been replicated

### R65: The Dependent Coupling model achieves FID-50k around 1.15
- **Rubric ID**: 79043fe8-a08a-415a-ba2a-7adb16ca0ff0
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Dependent Coupling model achieves FID-50k around 1.15
- **Parent context**: The recorded metrics show that the results from Section 4.1 have been replicated

### R66: Using the Dependent Coupling model that has been trained on...
- **Rubric ID**: 07327a66-c38f-4ce8-9359-cb87f284441d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the Dependent Coupling model that has been trained on ImageNet, FID-50k is computed on the ImageNet train set by comparing against 50k random samples from the training set
- **Parent context**: The experiments required to replicate results in Section 4.1 have been executed

### R67: Using the Dependent Coupling model that has been trained on...
- **Rubric ID**: 58ed3cb6-14ec-4750-bac0-c401a69418c9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the Dependent Coupling model that has been trained on ImageNet, FID-50k is computed on the ImageNet validation set
- **Parent context**: The experiments required to replicate results in Section 4.1 have been executed

### R68: The Dependent Coupling model achieves train FID-50k around 2...
- **Rubric ID**: 4d62ee04-8e84-4840-967c-60e8da5882e3
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Dependent Coupling model achieves train FID-50k around 2.15 for the super-resolution task
- **Parent context**: The recorded metrics show that the results from Section 4.2 have been replicated

### R69: The Dependent Coupling model achieves validation FID-50k aro...
- **Rubric ID**: 33e2261e-9038-4931-a8e0-6a2587a87c7a
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Dependent Coupling model achieves validation FID-50k around 2.05 for the super-resolution task
- **Parent context**: The recorded metrics show that the results from Section 4.2 have been replicated
