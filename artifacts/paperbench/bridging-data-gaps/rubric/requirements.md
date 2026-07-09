# Rubric Requirements — bridging-data-gaps
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 172

## Method Implementation

### R01: Code has been written to train a binary classifier to predic...
- **Rubric ID**: 5d7eb9db-5d5a-47d0-a5ee-991ab9327106
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a binary classifier to predict whether an input $x_t$ originates from the source domain or target domain.
- **Parent context**: Algorithm 1 for training DPMs with Adversarial Noise-based Transfer has been implemented.

### R02: A binary classifier has been trained to predict whether an i...
- **Rubric ID**: 5d7eb9db-5d5a-47d0-a5ee-991ab9327103894398
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A binary classifier has been trained to predict whether an input $x_t$ originates from the source domain or target domain.
- **Parent context**: Algorithm 1 for training DPMs with Adversarial Noise-based Transfer has been implemented.

### R03: The adaptor module from Noguchi & Harada, 2019 has been impl...
- **Rubric ID**: 44e8d794-412f-4b59-931d-c4076a73231a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The adaptor module from Noguchi & Harada, 2019 has been implemented.
- **Parent context**: Algorithm 1 for training DPMs with Adversarial Noise-based Transfer has been implemented.

### R04: Code has been written to compute the adaptive inner maximum...
- **Rubric ID**: 1209cc8c-40e9-46c9-9b00-ae2a0c133f34343ffb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the adaptive inner maximum as defined in Equation 7.
- **Parent context**: Algorithm 1 for training DPMs with Adversarial Noise-based Transfer has been implemented.

### R05: The adaptive inner maximum has been computed as defined in E...
- **Rubric ID**: 1209cc8c-40e9-46c9-9b00-ae2a0c133ffb
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The adaptive inner maximum has been computed as defined in Equation 7.
- **Parent context**: Algorithm 1 for training DPMs with Adversarial Noise-based Transfer has been implemented.

### R06: Code has been written to compute the similarity guided loss...
- **Rubric ID**: 492163d6-6e41-46e9-a9b6-1ef49061d81d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the similarity guided loss as defined in Equation 5.
- **Parent context**: Algorithm 1 for training DPMs with Adversarial Noise-based Transfer has been implemented.

### R07: The similarity guided loss has been computed as defined in E...
- **Rubric ID**: 492163d6-6e41-46e9-a9b6-1ef49061d84234f1d
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The similarity guided loss has been computed as defined in Equation 5.
- **Parent context**: Algorithm 1 for training DPMs with Adversarial Noise-based Transfer has been implemented.

### R08: Code has been written to update the adaptor module parameter...
- **Rubric ID**: 34cb106d-4b83-4bbd-a1fd-29cba4c26f3gw3rw3d94
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to update the adaptor module parameters via gradient descent with similarity-guided loss and adversarial noise as the objective. The objective function is defined in Equation 8.
- **Parent context**: Algorithm 1 for training DPMs with Adversarial Noise-based Transfer has been implemented.

### R09: The adaptor module parameters are updated via gradient desce...
- **Rubric ID**: 34cb106d-4b83-4bbd-a1fd-29cba4c26d94
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The adaptor module parameters are updated via gradient descent with similarity-guided loss and adversarial noise as the objective. The objective function is defined in Equation 8.
- **Parent context**: Algorithm 1 for training DPMs with Adversarial Noise-based Transfer has been implemented.

### R10: Code has been written to fine-tune a pre-trained LDM in the...
- **Rubric ID**: 3b484d81-4352-4eea-a568-da927824c92f33ee9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune a pre-trained LDM in the shift module of the U-net. The pre-trained DPM and autoencoders in LDM are kept fixed.
- **Parent context**: The experimental setup to evaluate the DDPM and LDM models has been replicated.

### R11: A pre-trained LDM has been fine-tuned in the shift module of...
- **Rubric ID**: 3b484d81-4352-4eea-a568-da927824c9e9
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A pre-trained LDM has been fine-tuned in the shift module of the U-net. The pre-trained DPM and autoencoders in LDM are kept fixed.
- **Parent context**: The experimental setup to evaluate the DDPM and LDM models has been replicated.

### R12: Code has been written to initialize the parameters of the ad...
- **Rubric ID**: 3282140d-e00b-45a1-9e14-cb2638632423494fa8
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to initialize the parameters of the adapter layer to zero.
- **Parent context**: The experimental setup to evaluate the DDPM and LDM models has been replicated.

### R13: The parameters of the adapter layer are initialized to zero.
- **Rubric ID**: 3282140d-e00b-45a1-9e14-cb2638694fa8
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The parameters of the adapter layer are initialized to zero.
- **Parent context**: The experimental setup to evaluate the DDPM and LDM models has been replicated.

### R14: Code has been written to generate 1,000 images from the mode...
- **Rubric ID**: bb0a98fa-568e-452e-a51f-9a027223223314251a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to generate 1,000 images from the models.
- **Parent context**: The Intra-LPIPS metric has been implemented.

### R15: Each image has been assigned to the training sample with the...
- **Rubric ID**: 57dc269b-20f0-445f-831f-8463079fbe26
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: Each image has been assigned to the training sample with the smallest LPIPS distance.
- **Parent context**: The Intra-LPIPS metric has been implemented.

### R16: TGAN has been implemented by adapting the StyleGAN2 codebase...
- **Rubric ID**: d20894c8-1e25-458f-96fe-db2ce2bd22a9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: TGAN has been implemented by adapting the StyleGAN2 codebase.
- **Parent context**: The baseline models used in Table 1 have been implemented by adapting pre-existing implementations f...

### R17: TGAN+ADA has been implemented by adapting the StyleGAN2 code...
- **Rubric ID**: 1a32ffae-af23-465e-bc16-c0f0cd828ffd
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: TGAN+ADA has been implemented by adapting the StyleGAN2 codebase.
- **Parent context**: The baseline models used in Table 1 have been implemented by adapting pre-existing implementations f...

### R18: EWC has been implemented by adapting the StyleGAN2 codebase.
- **Rubric ID**: afc80729-a8ca-4cce-aa43-2c1779cdabc8
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: EWC has been implemented by adapting the StyleGAN2 codebase.
- **Parent context**: The baseline models used in Table 1 have been implemented by adapting pre-existing implementations f...

### R19: CDC has been implemented by adapting the StyleGAN2 codebase.
- **Rubric ID**: d13c3a0b-1304-4e28-b3c4-ba9fb6eaf30a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: CDC has been implemented by adapting the StyleGAN2 codebase.
- **Parent context**: The baseline models used in Table 1 have been implemented by adapting pre-existing implementations f...

### R20: DCL has been implemented by adapting the StyleGAN2 codebase.
- **Rubric ID**: 1eb7c592-f303-4de0-ac80-73d11b55f6b3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: DCL has been implemented by adapting the StyleGAN2 codebase.
- **Parent context**: The baseline models used in Table 1 have been implemented by adapting pre-existing implementations f...

### R21: DDPM-PA has been implemented by adapting the StyleGAN2 codeb...
- **Rubric ID**: ca04bf90-d5cb-4703-86fa-c01372398751
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: DDPM-PA has been implemented by adapting the StyleGAN2 codebase.
- **Parent context**: The baseline models used in Table 1 have been implemented by adapting pre-existing implementations f...

### R22: Code has been written to train a diffusion model to generate...
- **Rubric ID**: 1d502a68-3fb3-4bce-953a-764cd09d7ea6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a diffusion model to generate data from a 2-dimensional Gaussian distribution with mean [1, 1] and unit variance.
- **Parent context**: Figure 2 has been replicated.

### R23: Code has been written to transfer the trained model to gener...
- **Rubric ID**: f3935ee2-c8e0-401e-9b75-dc7260e5fc8d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to transfer the trained model to generate samples from a 2-dimensional Gaussian distribution with a mean of [-1, -1] and unit variance using three methods: DDPM, DDPM-ANT w/o AN, and DDPM-ANT.
- **Parent context**: Figure 2 has been replicated.

### R24: The trained model has been transferred to generate samples f...
- **Rubric ID**: f3935ee2-c8e0-401e-9b75-dc7260e53f3afw3fc8d
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The trained model has been transferred to generate samples from a 2-dimensional Gaussian distribution with a mean of [-1, -1] and unit variance using three methods: DDPM, DDPM-ANT w/o AN, and DDPM-ANT.
- **Parent context**: Figure 2 has been replicated.

### R25: Code has been written to calculate the gradient direction us...
- **Rubric ID**: 7820ea5b-97be-4f81-ac79-3c971132342344423c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the gradient direction used as reference using 10,000 samples.
- **Parent context**: Figure 2a has been replicated.

### R26: Code has been written to calculate the gradient of the outpu...
- **Rubric ID**: cdfa5f7a-6d39-4228-959b-aecfe10243r31a0af
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the gradient of the output layer during the first iteration with 10-shot samples for DDPM.
- **Parent context**: Figure 2a has been replicated.

### R27: The gradient of the output layer during the first iteration...
- **Rubric ID**: cdfa5f7a-6d39-4228-959b-aecfe101a0af
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The gradient of the output layer during the first iteration has been calculated with 10-shot samples for DDPM.
- **Parent context**: Figure 2a has been replicated.

### R28: Code has been written to calculate the gradient of the outpu...
- **Rubric ID**: bd36332e-aed0-4d65-bf04-9d1432g3rw313ba4fee
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the gradient of the output layer during the first iteration with 10-shot samples for DDPM fine-tuned using similarity-guided training only (DDPM-ANT w/o AN).
- **Parent context**: Figure 2a has been replicated.

### R29: The gradient of the output layer during the first iteration...
- **Rubric ID**: bd36332e-aed0-4d65-bf04-9d1413ba4fee
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The gradient of the output layer during the first iteration has been calculated with 10-shot samples for DDPM fine-tuned using similarity-guided training only (DDPM-ANT w/o AN).
- **Parent context**: Figure 2a has been replicated.

### R30: Code has been written to calculate the gradient of the outpu...
- **Rubric ID**: eed7cd00-1ddd-4986-b5e6-76daff843423e2f3we848
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to calculate the gradient of the output layer during the first iteration with 10-shot samples for DDPM fine-tuned using similarity-guided training and adversarial noise selection (DDPM-ANT as defined by Equation 8).
- **Parent context**: Figure 2a has been replicated.

### R31: The gradient of the output layer during the first iteration...
- **Rubric ID**: eed7cd00-1ddd-4986-b5e6-76daff84e848
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The gradient of the output layer during the first iteration has been calculated with 10-shot samples for DDPM fine-tuned using similarity-guided training and adversarial noise selection (DDPM-ANT as defined by Equation 8).
- **Parent context**: Figure 2a has been replicated.

### R32: Code has been written to generate 20,000 samples using the D...
- **Rubric ID**: 20389b30-6a9c-4c52-bbe4-595e132423rfd47548
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to generate 20,000 samples using the DDPM model.
- **Parent context**: Figure 2b and Figure 2c have been replicated.

### R33: The DDPM model has been used to generate 20,000 samples.
- **Rubric ID**: 20389b30-6a9c-4c52-bbe4-595e1fd47548
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The DDPM model has been used to generate 20,000 samples.
- **Parent context**: Figure 2b and Figure 2c have been replicated.

### R34: Code has been written to generate 20,000 samples using the D...
- **Rubric ID**: 733d5b92-0acb-418b-bf4a-9c5793d3423rf3b3c17
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to generate 20,000 samples using the DDPM-ANT model.
- **Parent context**: Figure 2b and Figure 2c have been replicated.

### R35: Code has been written to perform 10-shot image generation, a...
- **Rubric ID**: acf3e6db-2136-4b89-953a-e8132fe3fd33fdb25b63
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to perform 10-shot image generation, adapting the LSUN Church dataset to Landscape drawings using the CDC model.
- **Parent context**: The 10-shot image generation for adapting LSUN Church to Landscape drawings have been replicated.

### R36: Code has been written to perform 10-shot image generation, a...
- **Rubric ID**: 91e045b5-a545-4a1c-92cb-8f0da2363f33frb5ea
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to perform 10-shot image generation, adapting the LSUN Church dataset to Landscape drawings using the DCL model.
- **Parent context**: The 10-shot image generation for adapting LSUN Church to Landscape drawings have been replicated.

### R37: Code has been written to perform 10-shot image generation, a...
- **Rubric ID**: b0e511b4-a831-4c28-99ba-cffdd3f3fd1a454c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to perform 10-shot image generation, adapting the LSUN Church dataset to Landscape drawings using the DDPM-PA model.
- **Parent context**: The 10-shot image generation for adapting LSUN Church to Landscape drawings have been replicated.

### R38: Code has been written to perform 10-shot image generation, a...
- **Rubric ID**: 0b788d47-6e35-4a79-8ff6-8b01932e23f377548a6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to perform 10-shot image generation, adapting the LSUN Church dataset to Landscape drawings using the DDPM-ANT model.
- **Parent context**: The 10-shot image generation for adapting LSUN Church to Landscape drawings have been replicated.

### R39: Code has been written to perform 10-shot image generation, a...
- **Rubric ID**: 6cbd6a02-363b-46d2-b179-c7667f23f365546d3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to perform 10-shot image generation, adapting the LSUN Church dataset to Landscape drawings using the LDM-ANT model.
- **Parent context**: The 10-shot image generation for adapting LSUN Church to Landscape drawings have been replicated.

### R40: Code has been written to perform 10-shot image generation, a...
- **Rubric ID**: 74baef43-248d-4b62-a5c6-c27255342341eb607
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to perform 10-shot image generation, adapting the FFHQ dataset to Raphael's paintings using the CDC model.
- **Parent context**: The 10-shot image generation for adapting FFHQ to Raphael's paintings has been replicated.

### R41: The CDC model has been used to perform 10-shot image generat...
- **Rubric ID**: 74baef43-248d-4b62-a5c6-c272551eb607
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The CDC model has been used to perform 10-shot image generation, adapting the FFHQ dataset to Raphael's paintings.
- **Parent context**: The 10-shot image generation for adapting FFHQ to Raphael's paintings has been replicated.

### R42: Code has been written to perform 10-shot image generation, a...
- **Rubric ID**: d2b6ae69-fd8b-4e58-9e98-c95feb72324234322838
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to perform 10-shot image generation, adapting the FFHQ dataset to Raphael's paintings using the DCL model.
- **Parent context**: The 10-shot image generation for adapting FFHQ to Raphael's paintings has been replicated.

### R43: Code has been written to perform 10-shot image generation, a...
- **Rubric ID**: 58a28f17-9837-4c7f-9bc5-eeec22342342b4376c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to perform 10-shot image generation, adapting the FFHQ dataset to Raphael's paintings using the DDPM-PA model.
- **Parent context**: The 10-shot image generation for adapting FFHQ to Raphael's paintings has been replicated.

### R44: Code has been written to perform 10-shot image generation, a...
- **Rubric ID**: 37ed1897-f4c6-4da9-9828-e0bb69324234f32d2c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to perform 10-shot image generation, adapting the FFHQ dataset to Raphael's paintings using the DDPM-ANT model.
- **Parent context**: The 10-shot image generation for adapting FFHQ to Raphael's paintings has been replicated.

### R45: Code has been written to perform 10-shot image generation, a...
- **Rubric ID**: b6c81e95-82ca-4c9b-83fd-9a7223423490f5548
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to perform 10-shot image generation, adapting the FFHQ dataset to Raphael's paintings using the LDM-ANT model.
- **Parent context**: The 10-shot image generation for adapting FFHQ to Raphael's paintings has been replicated.

### R46: Code has been written to update all parameters of TGAN durin...
- **Rubric ID**: 44633b1b-0847-41c7-95a1-0ba8910b90232328
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to update all parameters of TGAN during fine-tuning.
- **Parent context**: The results for TGAN have been replicated.

### R47: Code has been written to update all parameters of TGAN+ADA d...
- **Rubric ID**: 501bca60-25bc-4526-9fb2-78ba689cc32323230b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to update all parameters of TGAN+ADA during fine-tuning.
- **Parent context**: The results for TGAN+ADA have been replicated.

### R48: Code has been written to update all parameters of EWC during...
- **Rubric ID**: 1c449e47-a797-4e95-a4df-62aae23232370f15e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to update all parameters of EWC during fine-tuning.
- **Parent context**: The results for EWC have been replicated.

### R49: All parameters of the model were updated during fine-tuning...
- **Rubric ID**: 1c449e47-a797-4e95-a4df-62aae370f15e
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: All parameters of the model were updated during fine-tuning of EWC.
- **Parent context**: The results for EWC have been replicated.

### R50: Code has been written to update all parameters of CDC during...
- **Rubric ID**: 16f0e37d-e2a2-4ec3-a1f6-612fd23234ea3f79
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to update all parameters of CDC during fine-tuning.
- **Parent context**: The results for CDC have been replicated.

### R51: Code has been written to update all parameters of DCL during...
- **Rubric ID**: 35d26ce2-eacb-4394-8c7a-7175323235e2a81a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to update all parameters of DCL during fine-tuning.
- **Parent context**: The results for DCL have been replicated.

### R52: Code has been written to update all parameters of DDPM-PA du...
- **Rubric ID**: 3a1f7621-ed55-4604-95a0-296223238bc90b5d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to update all parameters of DDPM-PA during fine-tuning.
- **Parent context**: The results for DDPM-PA have been replicated.

### R53: Code has been written to fine-tune the DPM model using only...
- **Rubric ID**: 5ae20584-256c-4b30-9a02-0b2342ae3242344187
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the DPM model using only similarity guided training on a 10-shot sunglasses dataset for 300 iterations.
- **Parent context**: Figure 4 has been replicated.

### R54: Code has been written to fine-tune the DPM model using the p...
- **Rubric ID**: bcccd310-9ffd-4ad2-9ba8-0433e1ff32422342343455cf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the DPM model using the proposed DPM-ANT strategy on a 10-shot sunglasses dataset for 300 iterations.
- **Parent context**: Figure 4 has been replicated.

### R55: Code has been written to use the DPM-ANT model to transfer F...
- **Rubric ID**: 97c453a4-1925-40fe-aec7-c94c010a2323e8d5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to use the DPM-ANT model to transfer FFHQ to Sunglasses, and train a classifier on 10 adapted images.
- **Parent context**: The results for the 10-shot classifier have been replicated.

### R56: The DPM-ANT model was used to transfer FFHQ to Sunglasses, a...
- **Rubric ID**: 97c453a4-1925-40fe-aec7-c94c010ae8d5
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The DPM-ANT model was used to transfer FFHQ to Sunglasses, and a classifier was trained on 10 adapted images.
- **Parent context**: The results for the 10-shot classifier have been replicated.

### R57: Code has been written to use the DPM-ANT model to transfer F...
- **Rubric ID**: 84319b5f-e28f-4d85-a5c0-b8f324234e834dfcf4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to use the DPM-ANT model to transfer FFHQ to Sunglasses, and train a classifier on 100 adapted images.
- **Parent context**: The results for the 100-shot classifier have been replicated.

### R58: The DPM-ANT model was used to transfer FFHQ to Sunglasses, a...
- **Rubric ID**: 84319b5f-e28f-4d85-a5c0-b8fe834dfcf4
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The DPM-ANT model was used to transfer FFHQ to Sunglasses, and a classifier was trained on 100 adapted images.
- **Parent context**: The results for the 100-shot classifier have been replicated.

## Data Processing & Preparation

### R59: Code has been written to select training samples from the ta...
- **Rubric ID**: 5acc0f6c-9b8a-496d-beb1-5ca89a44f5a353533
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to select training samples from the target dataset, a time-step selected randomly, and standard Gaussian noise for each sample.
- **Parent context**: Algorithm 1 for training DPMs with Adversarial Noise-based Transfer has been implemented.

## Experimental Setup

### R60: Training samples are drawn from the target dataset, each pai...
- **Rubric ID**: 5acc0f6c-9b8a-496d-beb1-5ca89a44f5a3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Training samples are drawn from the target dataset, each paired with a randomly selected timestep and standard Gaussian noise.
- **Parent context**: Algorithm 1 for training DPMs with Adversarial Noise-based Transfer has been implemented.

### R61: Code has been written to set the hyper-parameter gamma for s...
- **Rubric ID**: b41c12f5-f27e-433a-bbd3-66b1c343fwf3eedc097
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to set the hyper-parameter gamma for similarity-guided training to 5.
- **Parent context**: The experimental setup to evaluate the DDPM and LDM models has been replicated.

### R62: The hyper-parameter gamma for similarity-guided training is...
- **Rubric ID**: b41c12f5-f27e-433a-bbd3-66b1ceedc097
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The hyper-parameter gamma for similarity-guided training is set to 5.
- **Parent context**: The experimental setup to evaluate the DDPM and LDM models has been replicated.

### R63: Code has been written to fine-tune a pre-trained model on Im...
- **Rubric ID**: 44de168e-4f56-4c7d-800f-16dda3432r3c66a289
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune a pre-trained model on ImageNet with a binary classifier head on 10 target domain images.
- **Parent context**: The experimental setup to evaluate the DDPM and LDM models has been replicated.

### R64: A pre-trained model on ImageNet is fine-tuned with a binary...
- **Rubric ID**: 44de168e-4f56-4c7d-800f-16ddac66a289
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A pre-trained model on ImageNet is fine-tuned with a binary classifier head on 10 target domain images.
- **Parent context**: The experimental setup to evaluate the DDPM and LDM models has been replicated.

### R65: Code has been written to set the hyperparameters $J$ and $\o...
- **Rubric ID**: 00c640f9-2865-4d4d-ab62-d381e5763423415b3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to set the hyperparameters $J$ and $\omega$ to 10 and 0.02, respectively, for adversarial noise selection.
- **Parent context**: The experimental setup to evaluate the DDPM and LDM models has been replicated.

### R66: The hyperparameters $J$ and $\omega$ are set to 10 and 0.02,...
- **Rubric ID**: 00c640f9-2865-4d4d-ab62-d381e57615b3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The hyperparameters $J$ and $\omega$ are set to 10 and 0.02, respectively, for adversarial noise selection.
- **Parent context**: The experimental setup to evaluate the DDPM and LDM models has been replicated.

### R67: The learning rate is set to 0.00005 for DDPM and 0.00001 for...
- **Rubric ID**: d96e73af-6bc0-405d-bebf-0730dca61911
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The learning rate is set to 0.00005 for DDPM and 0.00001 for LDM. Both models are trained for 300 iterations and a batch size of 40.
- **Parent context**: The experimental setup to evaluate the DDPM and LDM models has been replicated.

### R68: The learning rate is set to 0.00005 for DDPM and 0.00001 for...
- **Rubric ID**: d96e73af-6bc0-405d-bebf-0730dca61911
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The learning rate is set to 0.00005 for DDPM and 0.00001 for LDM. Both models are trained for 300 iterations and a batch size of 40.
- **Parent context**: The experimental setup to evaluate the DDPM and LDM models has been replicated.

### R69: A diffusion model has been trained to generate data from a 2...
- **Rubric ID**: 1d502a68-3fb3-4bce-953a-764cd09d2443r7ea6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A diffusion model has been trained to generate data from a 2-dimensional Gaussian distribution with mean [1, 1] and unit variance.
- **Parent context**: Figure 2 has been replicated.

### R70: The DDPM-ANT model has been used to generate 20,000 samples.
- **Rubric ID**: 733d5b92-0acb-418b-bf4a-9c5793db3c17
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DDPM-ANT model has been used to generate 20,000 samples.
- **Parent context**: Figure 2b and Figure 2c have been replicated.

### R71: The CDC model has been used to perform 10-shot image generat...
- **Rubric ID**: acf3e6db-2136-4b89-953a-e813fdb25b63
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The CDC model has been used to perform 10-shot image generation, adapting the LSUN Church dataset to Landscape drawings.
- **Parent context**: The 10-shot image generation for adapting LSUN Church to Landscape drawings have been replicated.

### R72: The DCL model has been used to perform 10-shot image generat...
- **Rubric ID**: 91e045b5-a545-4a1c-92cb-8f0da236b5ea
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DCL model has been used to perform 10-shot image generation, adapting the LSUN Church dataset to Landscape drawings.
- **Parent context**: The 10-shot image generation for adapting LSUN Church to Landscape drawings have been replicated.

### R73: The DDPM-PA model has been used to perform 10-shot image gen...
- **Rubric ID**: b0e511b4-a831-4c28-99ba-cffddd1a454c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DDPM-PA model has been used to perform 10-shot image generation, adapting the LSUN Church dataset to Landscape drawings.
- **Parent context**: The 10-shot image generation for adapting LSUN Church to Landscape drawings have been replicated.

### R74: The DDPM-ANT model has been used to perform 10-shot image ge...
- **Rubric ID**: 0b788d47-6e35-4a79-8ff6-8b01977548a6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DDPM-ANT model has been used to perform 10-shot image generation, adapting the LSUN Church dataset to Landscape drawings.
- **Parent context**: The 10-shot image generation for adapting LSUN Church to Landscape drawings have been replicated.

### R75: The LDM-ANT model has been used to perform 10-shot image gen...
- **Rubric ID**: 6cbd6a02-363b-46d2-b179-c766765546d3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The LDM-ANT model has been used to perform 10-shot image generation, adapting the LSUN Church dataset to Landscape drawings.
- **Parent context**: The 10-shot image generation for adapting LSUN Church to Landscape drawings have been replicated.

### R76: The DCL model has been used to perform 10-shot image generat...
- **Rubric ID**: d2b6ae69-fd8b-4e58-9e98-c95feb722838
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DCL model has been used to perform 10-shot image generation, adapting the FFHQ dataset to Raphael's paintings.
- **Parent context**: The 10-shot image generation for adapting FFHQ to Raphael's paintings has been replicated.

### R77: The DDPM-PA model has been used to perform 10-shot image gen...
- **Rubric ID**: 58a28f17-9837-4c7f-9bc5-eeec22b4376c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DDPM-PA model has been used to perform 10-shot image generation, adapting the FFHQ dataset to Raphael's paintings.
- **Parent context**: The 10-shot image generation for adapting FFHQ to Raphael's paintings has been replicated.

### R78: The DDPM-ANT model has been used to perform 10-shot image ge...
- **Rubric ID**: 37ed1897-f4c6-4da9-9828-e0bb69f32d2c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DDPM-ANT model has been used to perform 10-shot image generation, adapting the FFHQ dataset to Raphael's paintings.
- **Parent context**: The 10-shot image generation for adapting FFHQ to Raphael's paintings has been replicated.

### R79: The LDM-ANT model has been used to perform 10-shot image gen...
- **Rubric ID**: b6c81e95-82ca-4c9b-83fd-9a72890f5548
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The LDM-ANT model has been used to perform 10-shot image generation, adapting the FFHQ dataset to Raphael's paintings.
- **Parent context**: The 10-shot image generation for adapting FFHQ to Raphael's paintings has been replicated.

### R80: All parameters of TGAN were updated during fine-tuning.
- **Rubric ID**: 44633b1b-0847-41c7-95a1-0ba8910b9028
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: All parameters of TGAN were updated during fine-tuning.
- **Parent context**: The results for TGAN have been replicated.

### R81: All parameters of the model were updated during fine-tuning...
- **Rubric ID**: 501bca60-25bc-4526-9fb2-78ba689cc30b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: All parameters of the model were updated during fine-tuning of TGAN+ADA.
- **Parent context**: The results for TGAN+ADA have been replicated.

### R82: All parameters of the model were updated during fine-tuning...
- **Rubric ID**: 16f0e37d-e2a2-4ec3-a1f6-612fd4ea3f79
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: All parameters of the model were updated during fine-tuning of CDC.
- **Parent context**: The results for CDC have been replicated.

### R83: All parameters of the model were updated during fine-tuning...
- **Rubric ID**: 35d26ce2-eacb-4394-8c7a-717535e2a81a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: All parameters of the model were updated during fine-tuning of DCL.
- **Parent context**: The results for DCL have been replicated.

### R84: All parameters of the models were updated during fine-tuning...
- **Rubric ID**: 3a1f7621-ed55-4604-95a0-29628bc90b5d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: All parameters of the models were updated during fine-tuning of DDPM-PA.
- **Parent context**: The results for DDPM-PA have been replicated.

### R85: Only 1.3% of the total number of parameters of the model wer...
- **Rubric ID**: 6e0a78b8-9b91-4232-affd-fc2d89d7674f
- **Category**: Result Analysis / Experimental Setup
- **Weight**: 1
- **Requirement**: Only 1.3% of the total number of parameters of the model were updated during fine-tuning of DDPM-ANT.
- **Parent context**: The results for DDPM-ANT have been replicated.

### R86: Only 1.6% of the total number of parameters of the model wer...
- **Rubric ID**: 70b18b4a-1a76-406f-aca5-525cef082ea1
- **Category**: Result Analysis / Experimental Setup
- **Weight**: 1
- **Requirement**: Only 1.6% of the total number of parameters of the model were updated during fine-tuning of LDM-ANT. 
- **Parent context**: The results for LDM-ANT have been replicated.

### R87: Code has been written to fine-tune the DPM model on a 10-sho...
- **Rubric ID**: 5c926d2d-c604-4d54-b620-f11cd5e232327f2c9
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the DPM model on a 10-shot sunglasses dataset for 300 iterations.
- **Parent context**: Figure 4 has been replicated.

### R88: The DPM model was fine-tuned on a 10-shot sunglasses dataset...
- **Rubric ID**: 5c926d2d-c604-4d54-b620-f11cd5e7f2c9
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DPM model was fine-tuned on a 10-shot sunglasses dataset for 300 iterations.
- **Parent context**: Figure 4 has been replicated.

### R89: Code has been written to fine-tune the DPM model using an ad...
- **Rubric ID**: 66c2a90b-8f8a-483b-bd37-906bb3c34234239c2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the DPM model using an adaptor layer on a 10-shot sunglasses dataset for 300 iterations, updating only the adaptor layer.
- **Parent context**: Figure 4 has been replicated.

### R90: The DPM model was fine-tuned using an adaptor layer on a 10-...
- **Rubric ID**: 66c2a90b-8f8a-483b-bd37-906bb3c239c2
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DPM model was fine-tuned using an adaptor layer on a 10-shot sunglasses dataset for 300 iterations, updating only the adaptor layer.
- **Parent context**: Figure 4 has been replicated.

### R91: The DPM model was fine-tuned using only similarity guided tr...
- **Rubric ID**: 5ae20584-256c-4b30-9a02-0b2342ae4187
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DPM model was fine-tuned using only similarity guided training on a 10-shot sunglasses dataset for 300 iterations.
- **Parent context**: Figure 4 has been replicated.

### R92: The DPM model was fine-tuned using the proposed DPM-ANT stra...
- **Rubric ID**: bcccd310-9ffd-4ad2-9ba8-0433e1ff32423455cf
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DPM model was fine-tuned using the proposed DPM-ANT strategy on a 10-shot sunglasses dataset for 300 iterations.
- **Parent context**: Figure 4 has been replicated.

### R93: Code has been written to fine-tune the DPM model using the p...
- **Rubric ID**: bcccd310-9ffd-4ad2-9ba8-0433e1ff55cf
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the DPM model using the proposed DPM-ANT strategy on a 10-shot sunglasses dataset for 300 iterations.
- **Parent context**: Figure 4 has been replicated.

## Logging, Analysis & Presentation

### R94: 1,000 images have been generated from the models.
- **Rubric ID**: bb0a98fa-568e-452e-a51f-9a027214251a
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: 1,000 images have been generated from the models.
- **Parent context**: The Intra-LPIPS metric has been implemented.

### R95: The images generated by CDC and DCL capture the style of the...
- **Rubric ID**: 9cc039c6-a2ff-440c-bcaf-714436639a52
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The images generated by CDC and DCL capture the style of the target domain, but the generated images are blurry or distorted.
- **Parent context**: The 10-shot image generation for adapting FFHQ to Raphael's paintings has been replicated.

### R96: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 4740fcf9-1223-4e23-9b8e-9ca1661829fb
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Haunted houses using CDC was approximately 0.620.
- **Parent context**: The results for CDC have been replicated.

### R97: DPM-ANT generated images show better quality and detail than...
- **Rubric ID**: 3f10eb63-5b7f-4e4f-899c-b2292224130a
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: DPM-ANT generated images show better quality and detail than the other ones.
- **Parent context**: Figure 4 has been replicated.

## Evaluation, Metrics & Benchmarking

### R98: Code has been written to assign each image to the training s...
- **Rubric ID**: 57dc269b-20f0-445f-831f-8463079f3423r23be26
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to assign each image to the training sample with the smallest LPIPS distance.
- **Parent context**: The Intra-LPIPS metric has been implemented.

### R99: The average pair-wise distance within each cluster has compu...
- **Rubric ID**: 2a3fc09c-ad26-4374-8892-28173fc8d669
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average pair-wise distance within each cluster has computed. The average score from each cluster has been calculated as Intra-LPIPS metric.
- **Parent context**: The Intra-LPIPS metric has been implemented.

### R100: The average pair-wise distance within each cluster has compu...
- **Rubric ID**: 2a3fc09c-ad26-4374-8892-28173fc8d669
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average pair-wise distance within each cluster has computed. The average score from each cluster has been calculated as Intra-LPIPS metric.
- **Parent context**: The Intra-LPIPS metric has been implemented.

### R101: The FID metric has been implemented.
- **Rubric ID**: 9dc4e2e6-838a-4348-892a-a9592ceb55a1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID metric has been implemented.
- **Parent context**: The evaluation metrics have been implemented.

### R102: The gradient direction used as reference has been calculated...
- **Rubric ID**: 7820ea5b-97be-4f81-ac79-3c971134423c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The gradient direction used as reference has been calculated using 10,000 samples.
- **Parent context**: Figure 2a has been replicated.

### R103: The gradients computed for DDPM show the largest angular dev...
- **Rubric ID**: f43671c8-7696-4cc2-97ff-85029f88aaa1
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The gradients computed for DDPM show the largest angular deviation from the reference gradient. Using DDPM without AN shows a decrease in the angular difference, and the closest angular difference between the direction of the gradient and the reference was achieved by the proposed method DDPM-ANT.
- **Parent context**: Figure 2a has been replicated.

### R104: The samples generated by DDPM-ANT has a larger concentration...
- **Rubric ID**: 5c62087a-20c0-469c-8cdf-6ec267a7b4c8
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The samples generated by DDPM-ANT has a larger concentration of samples around -1,  which is the mean of the target distribution, than DDPM.
- **Parent context**: Figure 2b and Figure 2c have been replicated.

### R105: The images generated by DDPM-ANT and LDM-ANT show better res...
- **Rubric ID**: 063c7847-11ea-4fb7-88f2-1c233d2016dd
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The images generated by DDPM-ANT and LDM-ANT show better results at capturing the style of landscapes and representing buildings from the source domain.
- **Parent context**: The 10-shot image generation for adapting LSUN Church to Landscape drawings have been replicated.

### R106: The images generated by CDC and DCL capture the color scheme...
- **Rubric ID**: 3395e370-2eb0-4b73-bf02-2ad5774db404
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The images generated by CDC and DCL capture the color scheme of the target domain, but fail to capture the structure of the source domain.
- **Parent context**: The 10-shot image generation for adapting LSUN Church to Landscape drawings have been replicated.

### R107: The images generated by DDPM-PA capture the structure of the...
- **Rubric ID**: 45cabdee-165f-4305-8d56-6be77eb58633
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The images generated by DDPM-PA capture the structure of the source domain, but fail to capture the color scheme of the target domain.
- **Parent context**: The 10-shot image generation for adapting LSUN Church to Landscape drawings have been replicated.

### R108: The images generated by DDPM-PA are clear, but fail to captu...
- **Rubric ID**: a10da90c-5368-4b3a-bbbc-b18a642d5d33
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The images generated by DDPM-PA are clear, but fail to capture the style of the target domain.
- **Parent context**: The 10-shot image generation for adapting FFHQ to Raphael's paintings has been replicated.

### R109: The images generated by DDPM-ANT and LDM-ANT results at bett...
- **Rubric ID**: 1681b1fb-ef15-4ca4-bd40-5e8170526456
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The images generated by DDPM-ANT and LDM-ANT results at better capture the style of the target domain, while being less blurry or distorted than those generated by CDC and DCL.
- **Parent context**: The 10-shot image generation for adapting FFHQ to Raphael's paintings has been replicated.

### R110: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 7c37b754-9301-4e6e-be00-dfdc9d89a0cb
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Babies using TGAN was approximately 0.510.
- **Parent context**: The results for TGAN have been replicated.

### R111: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 974200ad-33dd-42e1-ab26-569de0a40c54
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Sunglasses using TGAN was approximately 0.550.
- **Parent context**: The results for TGAN have been replicated.

### R112: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 95959820-8424-4b4a-85b2-ee257922bdc7
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Raphael's painting using TGAN was approximately 0.533.
- **Parent context**: The results for TGAN have been replicated.

### R113: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 0dc44954-bc82-4c95-83c8-56a1b7b43598
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Haunted houses using TGAN was approximately 0.585.
- **Parent context**: The results for TGAN have been replicated.

### R114: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 1c6e4adc-f61f-49c5-a4d9-c53ca75583b4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Landscape drawings using TGAN was approximately 0.601.
- **Parent context**: The results for TGAN have been replicated.

### R115: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 113d31aa-fbfc-4174-8439-9d85b1fa90e9
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Babies using TGAN+ADA was approximately 0.546. 
- **Parent context**: The results for TGAN+ADA have been replicated.

### R116: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 1e57b62f-bc4d-456d-b491-a94f9ebcc73e
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Sunglasses using TGAN+ADA was approximately 0.571.
- **Parent context**: The results for TGAN+ADA have been replicated.

### R117: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: ef4d66f8-9fa2-46d1-b71e-075eb285d065
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Raphael's painting using TGAN+ADA was approximately 0.546. 
- **Parent context**: The results for TGAN+ADA have been replicated.

### R118: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 37027468-1b5e-4455-9dc5-70cd2a1c8c84
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Haunted houses using TGAN+ADA was approximately 0.615.
- **Parent context**: The results for TGAN+ADA have been replicated.

### R119: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: fc9676f4-d2b4-407c-bdef-1348b109f314
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Landscape drawings using TGAN+ADA was approximately 0.643.
- **Parent context**: The results for TGAN+ADA have been replicated.

### R120: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 74d173bc-f118-4c57-be85-701a9c4e05eb
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Babies using EWC was approximately 0.560. 
- **Parent context**: The results for EWC have been replicated.

### R121: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 5e3bd49e-eb36-4eea-bc6e-068c6e24e1d5
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Sunglasses using EWC was approximately 0.550. 
- **Parent context**: The results for EWC have been replicated.

### R122: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 7c911ac9-dc1e-4211-91f3-020564e07e7d
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Raphael's painting using EWC was approximately 0.541. 
- **Parent context**: The results for EWC have been replicated.

### R123: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 4816272b-2f0a-4374-8df1-293449e181b1
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Haunted houses using EWC was approximately 0.579.
- **Parent context**: The results for EWC have been replicated.

### R124: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 7cbca5c0-df59-4820-823f-cbbe48014be3
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Landscape drawings using EWC was approximately 0.596.
- **Parent context**: The results for EWC have been replicated.

### R125: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 13db3b4c-ed4c-4aff-9743-67eee97e775e
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Babies using CDC was approximately 0.583. 
- **Parent context**: The results for CDC have been replicated.

### R126: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: e03e5934-cb83-472a-b646-6ec4feb6f1db
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Sunglasses using CDC was approximately 0.581. 
- **Parent context**: The results for CDC have been replicated.

### R127: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 43da110f-9808-4444-b81a-f7fdd4a711c5
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Raphael's painting using CDC was approximately 0.564. 
- **Parent context**: The results for CDC have been replicated.

### R128: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 8ea8dd6d-d405-476d-9ff2-d335a989683c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Landscape drawings using CDC was approximately 0.674.
- **Parent context**: The results for CDC have been replicated.

### R129: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 21f6d97f-c7d9-4d5b-be65-e5e581b5b6d0
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Babies using DCL was approximately 0.579. 
- **Parent context**: The results for DCL have been replicated.

### R130: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: a233e3c1-23c8-4d95-8a0a-03902681749e
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Sunglasses using DCL was approximately 0.574. 
- **Parent context**: The results for DCL have been replicated.

### R131: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 5a9f9eef-cf7b-41e2-8d01-5bd6256591e2
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Raphael's painting using DCL was approximately 0.558. 
- **Parent context**: The results for DCL have been replicated.

### R132: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 38f5ef2e-5e05-4724-b269-25cb338d1ee2
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Haunted houses using DCL was approximately 0.616.
- **Parent context**: The results for DCL have been replicated.

### R133: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 35aa5b56-360a-4271-89ab-40633432b755
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Landscape drawings using DCL was approximately 0.626.
- **Parent context**: The results for DCL have been replicated.

### R134: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 8c79c1fc-c87a-41c5-8c76-285004ed0a6c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Babies using DDPM-PA was approximately 0.599. 
- **Parent context**: The results for DDPM-PA have been replicated.

### R135: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: cc587c72-982b-40a4-82d9-2a299fd9066b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Sunglasses using DDPM-PA was approximately 0.604. 
- **Parent context**: The results for DDPM-PA have been replicated.

### R136: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: f59ada11-1f81-4826-9a88-f20938af4a40
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Raphael's painting using DDPM-PA was approximately 0.581. 
- **Parent context**: The results for DDPM-PA have been replicated.

### R137: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 048c8922-ce0e-4fe5-8189-dc607b6e2451
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Haunted houses using DDPM-PA was approximately 0.628.
- **Parent context**: The results for DDPM-PA have been replicated.

### R138: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 9e0be390-39ac-4e80-b293-90b429826e6a
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Landscape drawings using DDPM-PA was approximately 0.706.
- **Parent context**: The results for DDPM-PA have been replicated.

### R139: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: f9b1e756-e242-424e-b38e-c52bd3cd7b5f
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Babies using DDPM-ANT was approximately 0.592. 
- **Parent context**: The results for DDPM-ANT have been replicated.

### R140: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 5470d90d-21fc-409e-a43a-702545cedad0
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Sunglasses using DDPM-ANT was approximately 0.613. 
- **Parent context**: The results for DDPM-ANT have been replicated.

### R141: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: bbe9da95-6d05-4ddf-ade6-3f7f5d5c6e14
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Raphael's painting using DDPM-ANT was approximately 0.621. 
- **Parent context**: The results for DDPM-ANT have been replicated.

### R142: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 853e5c69-6216-4ae0-b637-1e6f1e73e6ea
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Haunted houses using DDPM-ANT was approximately 0.648.
- **Parent context**: The results for DDPM-ANT have been replicated.

### R143: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: f7e247be-433e-481f-bb45-b22069ec9c0b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Landscape drawings using DDPM-ANT was approximately 0.723.
- **Parent context**: The results for DDPM-ANT have been replicated.

### R144: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 73d5e78f-0e8b-4431-934e-7f7865b35e82
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Babies using LDM-ANT was approximately 0.601. 
- **Parent context**: The results for LDM-ANT have been replicated.

### R145: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: b12177bc-5005-4eb1-8792-143c69268552
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Sunglasses using LDM-ANT was approximately 0.613. 
- **Parent context**: The results for LDM-ANT have been replicated.

### R146: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: ca670619-1466-4420-a8e4-15e84374635d
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting FFHQ to Raphael's painting using LDM-ANT was approximately 0.592. 
- **Parent context**: The results for LDM-ANT have been replicated.

### R147: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: 5d2ee275-4a50-4ce1-a73a-aa0f5974ac5c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Haunted houses using LDM-ANT was approximately 0.653.
- **Parent context**: The results for LDM-ANT have been replicated.

### R148: The Intra-LPIPS score for the 10-shot image generation adapt...
- **Rubric ID**: ff1c3ebc-0421-442a-9614-db0b26ddd321
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Intra-LPIPS score for the 10-shot image generation adapting LSUN Church to Landscape drawings using LDM-ANT was approximately 0.738.
- **Parent context**: The results for LDM-ANT have been replicated.

### R149: The FID score using TGAN for 10-shot transfer from FFHQ to B...
- **Rubric ID**: 2ece9f53-37f0-48f9-913d-57a9d02378fc
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID score using TGAN for 10-shot transfer from FFHQ to Babies is approximately 104.
- **Parent context**: The results for TGAN have been replicated.

### R150: The FID score using TGAN for 10-shot transfer from FFHQ to S...
- **Rubric ID**: fca53380-dbf2-48a1-b5ef-9bf57f57d2d0
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID score using TGAN for 10-shot transfer from FFHQ to Sunglasses is approximately 55.
- **Parent context**: The results for TGAN have been replicated.

### R151: The FID score using ADA for 10-shot transfer from FFHQ to Ba...
- **Rubric ID**: c86b8b7e-c1f7-4d54-ac82-2ff4da304ffa
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID score using ADA for 10-shot transfer from FFHQ to Babies is approximately 102.
- **Parent context**: The results for ADA have been replicated. 

### R152: The FID score using ADA for 10-shot transfer from FFHQ to Su...
- **Rubric ID**: 9eafca2f-1ce5-4fec-b4b2-8f6eaea87ca9
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID score using ADA for 10-shot transfer from FFHQ to Sunglasses is approximately 53.
- **Parent context**: The results for ADA have been replicated. 

### R153: The FID score using EWC for 10-shot transfer from FFHQ to Ba...
- **Rubric ID**: 3657fc20-0ced-49df-b18f-364a4259b242
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID score using EWC for 10-shot transfer from FFHQ to Babies is approximately 87.
- **Parent context**: The results for EWC have been replicated. 

### R154: The FID score using EWC for 10-shot transfer from FFHQ to Su...
- **Rubric ID**: 14bbc0cc-4d2e-4e04-a94b-655d70850df1
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID score using EWC for 10-shot transfer from FFHQ to Sunglasses is approximately 59.
- **Parent context**: The results for EWC have been replicated. 

### R155: The FID score using CDC for 10-shot transfer from FFHQ to Ba...
- **Rubric ID**: 12930c5e-7cb6-4aa3-bbf5-b0187ab11c68
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID score using CDC for 10-shot transfer from FFHQ to Babies is approximately 74.
- **Parent context**: The results for CDC have been replicated. 

### R156: The FID score using CDC for 10-shot transfer from FFHQ to Su...
- **Rubric ID**: 603c094c-d569-49fb-88e4-7c7cf13503da
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID score using CDC for 10-shot transfer from FFHQ to Sunglasses is approximately 42.
- **Parent context**: The results for CDC have been replicated. 

### R157: The FID score using DCL for 10-shot transfer from FFHQ to Ba...
- **Rubric ID**: 4748a6cf-742e-4c47-9d04-c2dcb291ffb4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID score using DCL for 10-shot transfer from FFHQ to Babies is approximately 52.
- **Parent context**: The results for DCL have been replicated. 

### R158: The FID score using DCL for 10-shot transfer from FFHQ to Su...
- **Rubric ID**: 36e4df66-c40b-4a01-aeb6-44b1f24fcd65
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID score using DCL for 10-shot transfer from FFHQ to Sunglasses is approximately 38.
- **Parent context**: The results for DCL have been replicated. 

### R159: The FID score using DDPM-PA for 10-shot transfer from FFHQ t...
- **Rubric ID**: abab77f5-03e8-47e5-a422-56535046ea63
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID score using DDPM-PA for 10-shot transfer from FFHQ to Babies is approximately 48.
- **Parent context**: The results for DDPM-PA have been replicated. 

### R160: The FID score using DDPM-PA for 10-shot transfer from FFHQ t...
- **Rubric ID**: 2edc3515-975b-4c4e-ab06-e0681dcd20d0
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID score using DDPM-PA for 10-shot transfer from FFHQ to Sunglasses is approximately 34.
- **Parent context**: The results for DDPM-PA have been replicated. 

### R161: The FID score using ANT for 10-shot transfer from FFHQ to Ba...
- **Rubric ID**: 9e2006e9-5289-4e71-aea3-9e5ace4bb038
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID score using ANT for 10-shot transfer from FFHQ to Babies is approximately 46.
- **Parent context**: The results for ANT have been replicated. 

### R162: The FID score using ANT for 10-shot transfer from FFHQ to Su...
- **Rubric ID**: c1d68df9-77e2-499b-85ef-e450d524be38
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FID score using ANT for 10-shot transfer from FFHQ to Sunglasses is approximately 20.
- **Parent context**: The results for ANT have been replicated. 

### R163: The adaptor results have the highest FID score, followed by...
- **Rubric ID**: 02e8e688-3b00-4b17-b837-7bc28f693988
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The adaptor results have the highest FID score, followed by the baseline results. DPM-ANT w/o AN achieve a lower FID score while the proposed DPM-ANT has the smallest FID score.
- **Parent context**: Figure 4 has been replicated.

### R164: Both DPM-ANT w/o AN and the proposed DPM ANT successfully tr...
- **Rubric ID**: dd4fd0a1-cc9e-43c1-9ed1-c7661ba76d51
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: Both DPM-ANT w/o AN and the proposed DPM ANT successfully transfer sunglasses to all images. The baseline and adaptor methods both fail to transfer sunglasses to some of the images generated.
- **Parent context**: Figure 4 has been replicated.

### R165: The intra-LPIPS score of the 10-shot classifier is approxima...
- **Rubric ID**: 862eb8c7-c2b2-45cc-8d33-bba33edd9f04
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The intra-LPIPS score of the 10-shot classifier is approximately 0.613.
- **Parent context**: The results for the 10-shot classifier have been replicated.

### R166: The FID score of the 10-shot classifier is approximately 20.
- **Rubric ID**: 4a5afb97-a578-4fde-87a9-114a0c20bdaf
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The FID score of the 10-shot classifier is approximately 20.
- **Parent context**: The results for the 10-shot classifier have been replicated.

### R167: The intra-LPIPS score of the 100-shot classifier is approxim...
- **Rubric ID**: b0ac5f91-386e-4c6d-8340-e4f052c98221
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The intra-LPIPS score of the 100-shot classifier is approximately 0.637.
- **Parent context**: The results for the 100-shot classifier have been replicated.

### R168: The FID score of the 100-shot classifier is approximately 22...
- **Rubric ID**: c9f1f68f-3cfa-4090-a51b-3d0a4f998481
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The FID score of the 100-shot classifier is approximately 22.
- **Parent context**: The results for the 100-shot classifier have been replicated.

## Dataset and Model Acquisition

### R169: Code has been written to load Babies, Sunglasses, Raphael Pe...
- **Rubric ID**: cfa8eaba-9c8d-4cc4-8797-ea27404322131f3de8c3
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been written to load Babies, Sunglasses, Raphael Peale, Sketches, and face paintings from the dataset FFHQ.
- **Parent context**: The target datasets have been selected for their corresponding source datasets.

### R170: Babies, Sunglasses, Raphael Peale, Sketches, and face painti...
- **Rubric ID**: cfa8eaba-9c8d-4cc4-8797-ea27404328c3
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Babies, Sunglasses, Raphael Peale, Sketches, and face paintings have been loaded from the dataset FFHQ.
- **Parent context**: The target datasets have been selected for their corresponding source datasets.

### R171: Haunted Houses and Landscape drawings have been loaded from...
- **Rubric ID**: a40709b6-f522-45cb-b9c4-f05ef341b7f4
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Haunted Houses and Landscape drawings have been loaded from the LSUN dataset.
- **Parent context**: The target datasets have been selected for their corresponding source datasets.

### R172: Haunted Houses and Landscape drawings have been loaded from...
- **Rubric ID**: a40709b6-f522-45cb-b9c4-f05ef341b7f4
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Haunted Houses and Landscape drawings have been loaded from the LSUN dataset.
- **Parent context**: The target datasets have been selected for their corresponding source datasets.
