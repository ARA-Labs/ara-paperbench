# Rubric Requirements — robust-clip
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 106

## Method Implementation

### R01: Code has been implemented such that LLaVA-1.5 7B can be load...
- **Rubric ID**: 25dfc428-a168-4a20-9673-f01a1469b39d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that LLaVA-1.5 7B can be loaded into memory
- **Parent context**: The models for LLaVA-1.5 7B (LLaVA) and OpenFlamingo 9B (OF) have been correctly configured and impo...

### R02: LLaVA-1.5 7B is set up to use the OpenAI CLIP ViT-L/14@224 v...
- **Rubric ID**: 00dc942f-0d35-4fe2-8ff7-7bf11c391f3a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LLaVA-1.5 7B is set up to use the OpenAI CLIP ViT-L/14@224 vision encoder (rather than the default ViT-L/14@336).
- **Parent context**: The models for LLaVA-1.5 7B (LLaVA) and OpenFlamingo 9B (OF) have been correctly configured and impo...

### R03: Code has been implemented such that OpenFlamingo 9B can be l...
- **Rubric ID**: fb356827-4d60-4dfb-b881-5616c17c2368
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that OpenFlamingo 9B can be loaded into memory
- **Parent context**: The models for LLaVA-1.5 7B (LLaVA) and OpenFlamingo 9B (OF) have been correctly configured and impo...

### R04: The code has been modified as needed to allow LLaVA to work...
- **Rubric ID**: 9b0dfbb6-18c7-4e80-98b2-0516dbc75f45
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The code has been modified as needed to allow LLaVA to work with OpenCLIP CLIP implementation instead of the Huggingface implementation.
- **Parent context**: The models for LLaVA-1.5 7B (LLaVA) and OpenFlamingo 9B (OF) have been correctly configured and impo...

### R05: Code has been implemented such that OpenAI's ViT-L/14 visual...
- **Rubric ID**: fbc512b3-ce82-4701-8577-6f9fb109772c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that OpenAI's ViT-L/14 visual encoder can be loaded into memory
- **Parent context**: The relevant visual and text encoders, as well as the relevant models, have been successfully config...

### R06: Code has been implemented such that OpenAI's ViT-L/14 text e...
- **Rubric ID**: fbc512b3-ce82-4701-8577-6f9fb109772d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that OpenAI's ViT-L/14 text encoder can be loaded into memory
- **Parent context**: The relevant visual and text encoders, as well as the relevant models, have been successfully config...

### R07: The visual encoder is properly isolated from the text encode...
- **Rubric ID**: 53ac73ee-e2ed-4f74-93d2-efde644d2f2a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The visual encoder is properly isolated from the text encoder, ensuring that only the visual encoder weights are updated during fine-tuning while the text encoder weights remain frozen.
- **Parent context**: The relevant visual and text encoders, as well as the relevant models, have been successfully config...

### R08: There is gradient normalization with elementwise sign for l_...
- **Rubric ID**: 8527cd53-317a-4ca4-bd6b-2b4f274000fe
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: There is gradient normalization with elementwise sign for l_infinity.
- **Parent context**: The PGD algorithm has been implemented correctly.

### R09: There is an initialization with uniform random perturbation.
- **Rubric ID**: 625d35e7-1b52-4309-a7c8-d08e966fc43c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: There is an initialization with uniform random perturbation.
- **Parent context**: The PGD algorithm has been implemented correctly.

### R10: An l_{infinity} ball is computed around non-normalized input...
- **Rubric ID**: ea973e69-e246-4abe-a554-f144c7e530ea
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: An l_{infinity} ball is computed around non-normalized inputs.
- **Parent context**: The PGD algorithm has been implemented correctly.

### R11: Given an input x and text prompts t_1, ..., t_k, the ith log...
- **Rubric ID**: f064f31b-babf-484c-8081-1769af682926
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Given an input x and text prompts t_1, ..., t_k, the ith logit of the classifieris computed as the cosine similarity of output of the image encoder on x and the output of the text encoder on t_i.
- **Parent context**: The training loop for TeCoA has been implemented correctly, consistent with section 3.2.

### R12: Given a label y, the loss is correctly computed as the cross...
- **Rubric ID**: 2339b2a9-cf8b-462d-ba57-65b7a1ae2098
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Given a label y, the loss is correctly computed as the cross-entropy loss as in equation 1 of section 3.2.
- **Parent context**: The training loop for TeCoA has been implemented correctly, consistent with section 3.2.

### R13: For each training sample x_i, the worst-case perturbed sampl...
- **Rubric ID**: 5734c557-4f09-4fc2-a886-fce0fc35f373
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each training sample x_i, the worst-case perturbed sample z_i is found using PGD by maximizing the cross-entropy loss against label y_i within an l_{infinity} ball of radius epsilon around x_i, where x_i is the non-normalized input.
- **Parent context**: The loss from a worst-case l_{infinity} perturbation is summed over the elements in the training set...

### R14: The cross-entropy loss is computed for each z_i against its...
- **Rubric ID**: 04a3d883-480f-4d1b-88c0-67c117a6277b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The cross-entropy loss is computed for each z_i against its corresponding label y_i.
- **Parent context**: The loss from a worst-case l_{infinity} perturbation is summed over the elements in the training set...

### R15: For each batch, the loss is computed by summing these indivi...
- **Rubric ID**: f8574d37-0507-44e3-b59e-0a794c6e7601
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each batch, the loss is computed by summing these individual losses over all samples in a batch from the training set and taking their mean.
- **Parent context**: The loss from a worst-case l_{infinity} perturbation is summed over the elements in the training set...

### R16: The model parameters are updated using gradient descent on t...
- **Rubric ID**: 7b03775b-fb66-4ffe-a09b-e3ea320e4363
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The model parameters are updated using gradient descent on this loss.
- **Parent context**: The loss from a worst-case l_{infinity} perturbation is summed over the elements in the training set...

### R17: Given an image encoder phi, image x and constant epsilon, th...
- **Rubric ID**: 42de5ca7-4e06-4143-a87b-3e2dc2fa6c50
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Given an image encoder phi, image x and constant epsilon, the loss is the max of ||phi(z) - phi_{Org}(x)||_2^2 over perturbations z of image x satisfying ||z - x||_{\infty} \leq epsilon, where phi(z) and phi_{Org}(x) are the (non-normalized) feature embeddings produced by the fine-tuned and original CLIP vision encoders respectively, as in equation 3. Here, phi_{Org}(x) is frozen.
- **Parent context**: The training loop for FARE has been implemented correctly, consistent with section 3.3.

### R18: The loss is summed over the samples in a batch, and their me...
- **Rubric ID**: 044b6a7f-aac8-4a69-a9e6-ddd41193df85
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The loss is summed over the samples in a batch, and their mean is taken.
- **Parent context**: The training loop for FARE has been implemented correctly, consistent with section 3.3.

### R19: The APGD algorithm from Croce & Hein 2020 has been correctly...
- **Rubric ID**: 5ac1855b-f62b-445b-8de9-4c370ce43e38
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The APGD algorithm from Croce & Hein 2020 has been correctly implemented / imported at single precision and half precision, with an initial step-size of epsilon.
- **Parent context**: The pipeline of untargeted high-precision and low-precision attacks have been correctly implemented ...

### R20: A targeted attack with "maybe" and a targeted attack with "W...
- **Rubric ID**: 74b14f74-2275-4476-8078-ddbabfb94301
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: A targeted attack with "maybe" and a targeted attack with "Word" are run on the most frequent ground truth sample, by minimizing the loss with respect to the target string.
- **Parent context**: The attack pipeline has been correctly implemented for visual question answering.

### R21: APGD has been implemented to run for 10000 iterations for ep...
- **Rubric ID**: 29ead7c7-b0b6-4530-96cf-3c5c45b7d906
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: APGD has been implemented to run for 10000 iterations for epsilon = 2/255 and 4/255, minimizing the autoregressive cross-entropy loss with respect to the target string.
- **Parent context**: The attack methods from the attack setup in Section 4.2 have been correctly implemented.

### R22: In each dataset, for each class, the text embedding is creat...
- **Rubric ID**: 5b330a3b-ab8e-4e7d-b3ff-e6447ec69e5f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In each dataset, for each class, the text embedding is created by averaging the output of the text encoder on all the prompt templates for the class.
- **Parent context**: The experiments from section 4.3 for the evaluation of zero-shot classification have been reproduced...

### R23: The first two attacks of AutoAttack are implemented, with th...
- **Rubric ID**: a7684df0-0574-42a3-9d32-d429f7acf20e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The first two attacks of AutoAttack are implemented, with the correct types, as explained in the attack setup from section 4.3.
- **Parent context**: The first two attacks of AutoAttack are imported, with the correct losses, as explained in the attac...

### R24: The jailbreaking attacks and prompts are implemented correct...
- **Rubric ID**: 451efc49-3524-4ee5-9780-ee6d1025fddb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The jailbreaking attacks and prompts are implemented correctly.
- **Parent context**: The jailbreaking attacks are correctly evaluated on LLaVA with TeCoA, FARE, and the original CLIP en...

## Experimental Setup

### R25: There is a momentum factor of 0.9.
- **Rubric ID**: 6f59a8d7-1429-41de-97c7-314f35331a1f
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: There is a momentum factor of 0.9.
- **Parent context**: The PGD algorithm has been implemented correctly.

### R26: For each model, training is done for two epochs on the Image...
- **Rubric ID**: c20fed83-21ae-45a5-ab9d-22f5f808cab6
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For each model, training is done for two epochs on the ImageNet dataset.
- **Parent context**: TeCoA^2, TeCoA^4, FARE^2, and FARE^4 have been trained correctly via finetuning on ImageNet, using t...

### R27: All robust models use 10 steps of PGD.
- **Rubric ID**: 39905299-5a1d-4ef5-9ce7-83b08fff294c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All robust models use 10 steps of PGD.
- **Parent context**: TeCoA^2, TeCoA^4, FARE^2, and FARE^4 have been trained correctly via finetuning on ImageNet, using t...

### R28: All robust models are trained with l_{infinity} radius of ei...
- **Rubric ID**: db6842ed-8431-4afa-8f0a-ca6f23c87481
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All robust models are trained with l_{infinity} radius of either 4/255 or 2/255 with step size set to 1/255.
- **Parent context**: TeCoA^2, TeCoA^4, FARE^2, and FARE^4 have been trained correctly via finetuning on ImageNet, using t...

### R29: AdamW optimizer is used with momentum coefficients beta_1 =...
- **Rubric ID**: 2188f0dc-1e74-45b8-84a7-c8f3e8bf9f83
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: AdamW optimizer is used with momentum coefficients beta_1 = 0.9 and beta_2 = 0.95.
- **Parent context**: The optimizer, learning rate, and batch size are implemented correctly and match those mentioned in ...

### R30: The learning rate is implemented with cosine decay schedule...
- **Rubric ID**: 61f6d477-295f-449c-a683-fbd792cba564
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The learning rate is implemented with cosine decay schedule and linear warmup to a peak learning rate of 1e-5 at 7% of total training steps.
- **Parent context**: The optimizer, learning rate, and batch size are implemented correctly and match those mentioned in ...

### R31: The weight decay coefficient is set to 1e-4.
- **Rubric ID**: 6a930f99-32a5-4784-8c27-cd41843121c9
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The weight decay coefficient is set to 1e-4.
- **Parent context**: The optimizer, learning rate, and batch size are implemented correctly and match those mentioned in ...

### R32: An effective batch size of 128 is used.
- **Rubric ID**: 0e405780-5eaf-4f6d-9c83-aea7c42e93f8
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: An effective batch size of 128 is used.
- **Parent context**: The optimizer, learning rate, and batch size are implemented correctly and match those mentioned in ...

### R33: APGD at half precision was run for 100 iterations for each o...
- **Rubric ID**: 34ca52d0-f4f8-4ede-8455-9f24c34df846
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: APGD at half precision was run for 100 iterations for each of the five ground-truth labels for each image, maximizing the autoregressive cross-entropy loss with respect to the ground-truth captions.
- **Parent context**: The attack pipeline has been correctly implemented for image captioning.

### R34: For the COCO samples with score at least 10, and for the Fli...
- **Rubric ID**: ed00f7ca-e5ef-426b-92ec-44865dd26c40
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For the COCO samples with score at least 10, and for the Flickr30k samples with score at least 2, an additional single precision attack is made (with the perturbation initialized with the best perturbation for each sample from the previous attacks), using the ground-truth that led to the lowest score for each sample.
- **Parent context**: The attack pipeline has been correctly implemented for image captioning.

### R35: APGD at half precision was run for 100 iterations for each o...
- **Rubric ID**: c4b9e13b-7c78-478c-9a57-82b3bc778293
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: APGD at half precision was run for 100 iterations for each of the five most frequent ground-truth labels (among the 10 available ground-truths), maximizing the autoregressive cross-entropy loss with respect to the ground-truth answers.
- **Parent context**: The attack pipeline has been correctly implemented for visual question answering.

### R36: For all samples, an additional single precision attack is ma...
- **Rubric ID**: 869f880d-fcb4-466e-8178-1b3e2c3b8377
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For all samples, an additional single precision attack is made, using the ground-truth that led to the lowest score for each sample. The single precision attack also initializes perturbations with the perturbation of the previous attacks that led to the lowest score for each sample
- **Parent context**: The attack pipeline has been correctly implemented for visual question answering.

### R37: The targeted attack with "Word" is not run on TextVQA.
- **Rubric ID**: 2bbf067d-71b0-42f7-a239-6c902509fbb7
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The targeted attack with "Word" is not run on TextVQA.
- **Parent context**: The attack pipeline has been correctly implemented for visual question answering.

### R38: The adversarial image has been perturbed by epsilon = 4 / 25...
- **Rubric ID**: 580c596d-7ec0-4b9d-8ba1-7d034d93c7ff
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The adversarial image has been perturbed by epsilon = 4 / 255.
- **Parent context**: Example targeted attacks are shown for CLIP, TeCaA^4, and FARE^4, as in Figures 1 and 3.

### R39: The adversarial attacks are performed on all versions of CLI...
- **Rubric ID**: 5a705380-610d-4cad-8471-0fcfc1cc711b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The adversarial attacks are performed on all versions of CLIP using the corresponding loss types from AutoAttack. The logits are taken from the cosine similarities described in Section 3.1.
- **Parent context**: The first two attacks of AutoAttack are imported, with the correct losses, as explained in the attac...

### R40: The jailbreaking attacks are set to have the following param...
- **Rubric ID**: e5ee8d92-8996-4ec9-979b-d04aae3abe10
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The jailbreaking attacks are set to have the following parameters: 5000 iterations and alpha = 1/255.
- **Parent context**: The jailbreaking attacks are correctly evaluated on LLaVA with TeCoA, FARE, and the original CLIP en...

### R41: Jailbreaking attacks are run on LLaVA with CLIP, FARE^4, and...
- **Rubric ID**: ffc8deff-04b6-4d37-a576-cf904d87b7e5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Jailbreaking attacks are run on LLaVA with CLIP, FARE^4, and TeCoA^4 with epsilon = 0, 16/255, and 32/255, and 64/255 on harmful target strings.
- **Parent context**: The jailbreaking attacks are correctly evaluated on LLaVA with TeCoA, FARE, and the original CLIP en...

## Dataset and Model Acquisition

### R42: The ImageNet dataset is imported.
- **Rubric ID**: 5579c962-ab39-4edb-88c9-099352403dfd
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The ImageNet dataset is imported.
- **Parent context**: TeCoA^2, TeCoA^4, FARE^2, and FARE^4 have been trained correctly via finetuning on ImageNet, using t...

### R43: The image captioning datasets COCO 2014 and Flickr30K have b...
- **Rubric ID**: 5d76e49d-d912-4b5b-8fea-2270b5f70162
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The image captioning datasets COCO 2014 and Flickr30K have been imported.
- **Parent context**: The image captioning datasets and the visual question answering datasets listed in Section 4.1 have ...

### R44: The visual question answering datasets VQAv2 and TextVQA hav...
- **Rubric ID**: 852ce44e-697d-4379-b732-0be1bfa8a457
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The visual question answering datasets VQAv2 and TextVQA have been imported.
- **Parent context**: The image captioning datasets and the visual question answering datasets listed in Section 4.1 have ...

### R45: Images are gathered for all the six target captions from App...
- **Rubric ID**: ed3d2db0-11ce-4876-b233-b4ac1b6e50ae
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Images are gathered for all the six target captions from Appendix B.8.
- **Parent context**: The results from section 4.2 have been correctly reproduced.

### R46: Imagenet, as well as the 13 zero-shot datasets listed in App...
- **Rubric ID**: f826f3b0-5978-4c13-91bd-2b5466615251
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Imagenet, as well as the 13 zero-shot datasets listed in Appendix B.10, have been successfully imported.
- **Parent context**: The experiments from section 4.3 for the evaluation of zero-shot classification have been reproduced...

## Data Processing & Preparation

### R47: ImageNet images are used at resolution 224x224.
- **Rubric ID**: 2ae96f37-e6b0-4162-9e16-a61d193bc8b5
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: ImageNet images are used at resolution 224x224.
- **Parent context**: TeCoA^2, TeCoA^4, FARE^2, and FARE^4 have been trained correctly via finetuning on ImageNet, using t...

### R48: The adversarial COCO images previously generated at epsilon...
- **Rubric ID**: 22b66dd8-e5c5-40f8-9af1-ee5a23ddc3cb
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The adversarial COCO images previously generated at epsilon = 4/255 against OF-CLIP and LLaVA-CLIP in Section 4.1 are prepared for transfer attack evaluation.
- **Parent context**: The transfer attacks from Section 4.1 have been correctly reproduced.

### R49: For captions 1 - 5, 25 images are randomly sampled from COCO...
- **Rubric ID**: a06564f5-6a7b-4370-b5db-91a1e9de9792
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: For captions 1 - 5, 25 images are randomly sampled from COCO.
- **Parent context**: The APGD attack is run on all 6 target captions from Appendix B.8 for LLaVA on all five encoders, wi...

### R50: For caption 6, some certain 25 handpicked images from a stoc...
- **Rubric ID**: 15a1c1e5-75c1-4f7b-8e18-44a83ae597c6
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: For caption 6, some certain 25 handpicked images from a stock website are used.
- **Parent context**: The APGD attack is run on all 6 target captions from Appendix B.8 for LLaVA on all five encoders, wi...

### R51: A single image is prepared for the jailbreaking attacks to b...
- **Rubric ID**: 81e3025f-c810-43b2-bc69-1cff925f99e3
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: A single image is prepared for the jailbreaking attacks to be run on.
- **Parent context**: The jailbreaking attacks are correctly evaluated on LLaVA with TeCoA, FARE, and the original CLIP en...

## Evaluation, Metrics & Benchmarking

### R52: For each dataset, 500 samples are used for adversarial evalu...
- **Rubric ID**: bf9835a7-e280-41e9-ab7a-100759482bdd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each dataset, 500 samples are used for adversarial evaluations.
- **Parent context**: The evaluation metrics for image captioning and visual question answering have been correctly implem...

### R53: All the samples are used for clean evaluations.
- **Rubric ID**: 53203b37-8b33-4ca1-b16c-f7da228fca34
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All the samples are used for clean evaluations.
- **Parent context**: The evaluation metrics for image captioning and visual question answering have been correctly implem...

### R54: The CIDEr score is used for image captioning, and is correct...
- **Rubric ID**: 7cfd21a3-4227-40e4-862e-ae34fca73ff0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The CIDEr score is used for image captioning, and is correctly implemented.
- **Parent context**: The evaluation metrics for image captioning and visual question answering have been correctly implem...

### R55: VQA accuracy is used for visual question answering, and is c...
- **Rubric ID**: 3629342c-a8ca-447d-8950-ea5ddf16521d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: VQA accuracy is used for visual question answering, and is correctly implemented.
- **Parent context**: The evaluation metrics for image captioning and visual question answering have been correctly implem...

### R56: CIDEr scores are calculated after each attack on every sampl...
- **Rubric ID**: 5f96de37-02fb-4b36-ac06-8fab781d8641
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: CIDEr scores are calculated after each attack on every sample.
- **Parent context**: The CIDEr scores have been correctly computed and tracked throughout the attack process:

### R57: For each sample, the lowest CIDEr score across all ground-tr...
- **Rubric ID**: 14d3767b-326c-4617-a9a5-3760c2317cc2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each sample, the lowest CIDEr score across all ground-truth captions is identified and stored.
- **Parent context**: The CIDEr scores have been correctly computed and tracked throughout the attack process:

### R58: Scores are computed using the standard CIDEr metric implemen...
- **Rubric ID**: b8a21c35-d5e2-4647-a4ca-2f2acb9b80a7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Scores are computed using the standard CIDEr metric implementation following Vedantam et al. 2015
- **Parent context**: The CIDEr scores have been correctly computed and tracked throughout the attack process:

### R59: VQA accuracy scores are calculated after each attack on ever...
- **Rubric ID**: 01478154-5c21-423f-816b-6166bc800108
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: VQA accuracy scores are calculated after each attack on every sample.
- **Parent context**: The VQA accuracy scores have been correctly computed and tracked throughout the attack process:

### R60: For each sample, the lowest VQA accuracy score across all gr...
- **Rubric ID**: d799c493-f264-4ab2-ab4f-ca5999b418cf
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each sample, the lowest VQA accuracy score across all ground-truth answers is identified and stored.
- **Parent context**: The VQA accuracy scores have been correctly computed and tracked throughout the attack process:

### R61: The VQA accuracy scores have been computed for all the sampl...
- **Rubric ID**: 782f24ee-c3fc-41ca-b156-9538af47b8d4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The VQA accuracy scores have been computed for all the samples.
- **Parent context**: The attack pipeline has been correctly implemented for visual question answering.

### R62: The CIDEr score has been computed and displayed for all five...
- **Rubric ID**: 5d45a1c4-bb8f-4fc8-bfee-d3a5107bced4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The CIDEr score has been computed and displayed for all five encoders for OF and LLaVA on image captioning, for all the image captioning datasets (COCO and Flickr3k) on clean images, adversarial images with epsilon = 2 / 225, and adversarial images with epsilon = 4 / 255.
- **Parent context**: The metrics for clean images and adversarial images have been computed and plotted for all five visi...

### R63: The VQA accuracy score has been computed and displayed for a...
- **Rubric ID**: d75c44fa-05a8-42cc-8365-cd2e408c790c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The VQA accuracy score has been computed and displayed for all five encoders for OF and LLaVA on image captioning, for all the VQA datasets (TextVQA and VQAv2) on clean images, adversarial images with epsilon = 2 / 225, and adversarial images with epsilon = 4 / 255.
- **Parent context**: The metrics for clean images and adversarial images have been computed and plotted for all five visi...

### R64: For each (vision encoder, VLM) pair, for each type of attack...
- **Rubric ID**: a4627f29-a2bd-4308-a579-2c98434f23a5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each (vision encoder, VLM) pair, for each type of attack (clean, epsilon = 2/255, epsilon = 4/255), the average over the metrics has been computed and reported.
- **Parent context**: The metrics for clean images and adversarial images have been computed and plotted for all five visi...

### R65: The original CLIP encoder attains the best performance on cl...
- **Rubric ID**: b28763cb-b94e-47a7-b1be-8d7c098cd34e
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The original CLIP encoder attains the best performance on clean data.
- **Parent context**: The performance of the original CLIP encoder on clean and robust examples follows the trends describ...

### R66: The original CLIP encoder has very low scores on perturbed d...
- **Rubric ID**: 9c9ab5f4-6b97-4d46-bf1f-39e10443a7cc
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The original CLIP encoder has very low scores on perturbed data.
- **Parent context**: The performance of the original CLIP encoder on clean and robust examples follows the trends describ...

### R67: Compared to TeCoA, FARE overall has better clean performance...
- **Rubric ID**: c5d0da9e-8be9-4182-a719-0b5160dbde51
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Compared to TeCoA, FARE overall has better clean performance and better robust performance.
- **Parent context**: Versions of OF and LLaVA have been correctly evaluated on the datasets, and their trends match those...

### R68: For LLaVA, FARE^4 outperforms TeCoA^2 and TeCoA^4 in all dat...
- **Rubric ID**: e9452862-044f-4cda-8232-725b4b972d24
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For LLaVA, FARE^4 outperforms TeCoA^2 and TeCoA^4 in all datasets in clean examples and in most datasets on perturbed examples.
- **Parent context**: Versions of OF and LLaVA have been correctly evaluated on the datasets, and their trends match those...

### R69: In LLaVA, FARE^2 has a higher clean performance on average t...
- **Rubric ID**: 8d0f5f86-b66b-4f1e-98cc-657ed45362cd
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: In LLaVA, FARE^2 has a higher clean performance on average than FARE^4, but a lower performance on average on datasets with pertubed examples at both epsilon = 2 / 255 and epsilon = 4 / 255.
- **Parent context**: Versions of OF and LLaVA have been correctly evaluated on the datasets, and their trends match those...

### R70: In OF, FARE4 is rivalled in clean performance by TeCoA^2 onl...
- **Rubric ID**: 068a0e17-5b57-4ab6-9eca-9d0a09bb2fc3
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: In OF, FARE4 is rivalled in clean performance by TeCoA^2 only on VQAv2, with a negligible performance gap.
- **Parent context**: Versions of OF and LLaVA have been correctly evaluated on the datasets, and their trends match those...

### R71: FARE^2 demonstrates higher clean performance and the best ov...
- **Rubric ID**: 29a35cf2-5e44-40c3-8c6d-6be949e0a7f1
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FARE^2 demonstrates higher clean performance and the best overall robustness at epsilon = 2/255.
- **Parent context**: Versions of OF and LLaVA have been correctly evaluated on the datasets, and their trends match those...

### R72: OF and LLaVA with the five image encoders are evaluated on t...
- **Rubric ID**: 29b2389a-1f5e-4121-a8a4-a7444154c41a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: OF and LLaVA with the five image encoders are evaluated on the above adversarial examples, and a table of the CIDEr scores is plotted, as in Table 2.
- **Parent context**: The transfer attacks from Section 4.1 have been correctly reproduced.

### R73: As in section 4.1, the attacks transfer well between OF and...
- **Rubric ID**: de583bc3-1579-49bd-be27-f1458b1bc08e
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: As in section 4.1, the attacks transfer well between OF and LLaVA for standard CLIP.
- **Parent context**: The transfer attacks from Section 4.1 have been correctly reproduced.

### R74: As in section 4.1, the attacks do not transfer well between...
- **Rubric ID**: 1aa7adf7-a05b-4262-8a7c-bbae900b2cdf
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: As in section 4.1, the attacks do not transfer well between OF and LLaVA for robust versions of CLIP.
- **Parent context**: The transfer attacks from Section 4.1 have been correctly reproduced.

### R75: An attack is defined to be successful if the target string i...
- **Rubric ID**: a83bea8b-7ef5-4fd6-922c-9895aeb17f89
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: An attack is defined to be successful if the target string is contained exactly in the output of the model.
- **Parent context**: The attack methods from the attack setup in Section 4.2 have been correctly implemented.

### R76: The total number of successful attacks (out of 25) is report...
- **Rubric ID**: a9e3bff9-b22f-420c-a9aa-3c42fba552c3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The total number of successful attacks (out of 25) is reported, for each (target, epsilon, encoder) tuple.
- **Parent context**: The results from section 4.2 have been correctly reproduced.

### R77: The original CLIP is vulnerable to all the attacks, and the...
- **Rubric ID**: 145e6d25-ce49-4bcb-9724-32728729ed42
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The original CLIP is vulnerable to all the attacks, and the robust CLIP never breaks for epsilon = 2/255.
- **Parent context**: The trends for the image encoders on the attacks, including the vulnerability of the original CLIP a...

### R78: When using TeCOA, the attack is not successful in generating...
- **Rubric ID**: b9ac88d4-ba17-4aaa-b42b-160048f187f4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using TeCOA, the attack is not successful in generating the target string, but does produce captions of lower quality.
- **Parent context**: The trends for the image encoders on the attacks, including the vulnerability of the original CLIP a...

### R79: FARE is robust to attacks, and also produces good captions.
- **Rubric ID**: 04b35fad-ee3d-4703-93ae-726e882dbbd8
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FARE is robust to attacks, and also produces good captions.
- **Parent context**: The trends for the image encoders on the attacks, including the vulnerability of the original CLIP a...

### R80: In the epsilon = 4 / 255 threat model, FARE^2 and TeCoA^2 on...
- **Rubric ID**: 06886772-d5a3-4488-bc67-ebe3fef3cfac
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: In the epsilon = 4 / 255 threat model, FARE^2 and TeCoA^2 only break in a few cases.
- **Parent context**: The trends for the image encoders on the attacks, including the vulnerability of the original CLIP a...

### R81: FARE^4 and TeCoA^4 are completely robust against all the att...
- **Rubric ID**: dfe2f5b3-7f50-4d9a-8d2c-95b1fde9a688
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FARE^4 and TeCoA^4 are completely robust against all the attacks.
- **Parent context**: The trends for the image encoders on the attacks, including the vulnerability of the original CLIP a...

### R82: The quality and accuracy of text increase in order of CLIP,...
- **Rubric ID**: 3df2d801-4f72-4057-95d4-c0baac452445
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The quality and accuracy of text increase in order of CLIP, TeCoA, and FARE, as in Figures 1 and 3.
- **Parent context**: Example targeted attacks are shown for CLIP, TeCaA^4, and FARE^4, as in Figures 1 and 3.

### R83: The zero-shot accuracy is computed for clean data, and pertu...
- **Rubric ID**: 12a549f7-72a9-4ee2-9437-3c408d13c38d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The zero-shot accuracy is computed for clean data, and perturbed data (for epsilon = 2/255 and 4/255 separately) for CLIP with all five image encoders.
- **Parent context**: The results of zero-shot classification from Section 4.3 have been correctly reproduced.

### R84: TeCoA is more accurate than the others on clean images.
- **Rubric ID**: d0bf838e-dc2e-467f-be81-ffb37dd586c8
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: TeCoA is more accurate than the others on clean images.
- **Parent context**: The robust and non-robust accuracy for CLIP, FARE, and TeCoA on ImageNet follow the trends in sectio...

### R85: TeCoA is more accurate than the others on perturbed images.
- **Rubric ID**: 6b94a3c5-8134-4fed-98c3-346fd9b5d646
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: TeCoA is more accurate than the others on perturbed images.
- **Parent context**: The robust and non-robust accuracy for CLIP, FARE, and TeCoA on ImageNet follow the trends in sectio...

### R86: The original CLIP model has the best performance on clean da...
- **Rubric ID**: 14e99046-4108-4b83-ae20-eae8e42355d3
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The original CLIP model has the best performance on clean data.
- **Parent context**: The robust and non-robust accuracy for CLIP, FARE, and TeCoA on the other zero-shot datasets follow ...

### R87: The TeCoA models perform significantly worse than the origin...
- **Rubric ID**: cadff81a-3a9b-4898-a286-006e745f6ff6
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The TeCoA models perform significantly worse than the original CLIP model on clean data.
- **Parent context**: The robust and non-robust accuracy for CLIP, FARE, and TeCoA on the other zero-shot datasets follow ...

### R88: FARE has much better clean accuracy than TeCoA.
- **Rubric ID**: d3c609f1-b6d8-4696-a720-4091ed60702d
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FARE has much better clean accuracy than TeCoA.
- **Parent context**: The robust and non-robust accuracy for CLIP, FARE, and TeCoA on the other zero-shot datasets follow ...

### R89: The original CLIP has accuracy close to zero on perturbed da...
- **Rubric ID**: dc3ed8eb-3b4e-4b04-a6a8-6fd2a5f0e416
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The original CLIP has accuracy close to zero on perturbed data.
- **Parent context**: The robust and non-robust accuracy for CLIP, FARE, and TeCoA on the other zero-shot datasets follow ...

### R90: FARE^4 outperforms TeCoA^2 and TeCoA^4 on perturbed data.
- **Rubric ID**: cea15ca3-43dd-4c30-b6df-bee5cef1abfe
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FARE^4 outperforms TeCoA^2 and TeCoA^4 on perturbed data.
- **Parent context**: The robust and non-robust accuracy for CLIP, FARE, and TeCoA on the other zero-shot datasets follow ...

### R91: The POPE benchmark has been implemented correctly.
- **Rubric ID**: ad0e8b4a-5a74-46b0-a117-3ca0e816ae2c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The POPE benchmark has been implemented correctly.
- **Parent context**: LLaVA has been evaluated (separately for each visual encoder) on hallucinations using the POPE bench...

### R92: The POPE scores (Adversarial, Popular, and Random) have been...
- **Rubric ID**: 46a0e1f5-60c5-4fe7-b648-3e10df19bbb3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The POPE scores (Adversarial, Popular, and Random) have been calculated for the five visual encoders with LLaVA.
- **Parent context**: LLaVA has been evaluated (separately for each visual encoder) on hallucinations using the POPE bench...

### R93: The trends in section 4.4, including the good performance of...
- **Rubric ID**: a264d096-4531-4f98-8c47-c65fb56c34db
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The trends in section 4.4, including the good performance of CLIP (with FARE not too much worse), and the poor performance of TeCoA, hold.
- **Parent context**: LLaVA has been evaluated (separately for each visual encoder) on hallucinations using the POPE bench...

### R94: The SQA-I benchmark has been correctly implemented.
- **Rubric ID**: 898dd8bf-1c83-46c0-af28-dce1eb1eaf81
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The SQA-I benchmark has been correctly implemented.
- **Parent context**: LLaVA with TeCoA and FARE has been correctly evaluated on the SQA-I benchmark as in section 4.4.

### R95: FARE and CLIP have comparable scores in the SQA-I benchmark.
- **Rubric ID**: 5c96bdf8-2911-4b26-9c33-90c6364021c7
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FARE and CLIP have comparable scores in the SQA-I benchmark.
- **Parent context**: The trends in section 4.4 are observed, including comparable scores for FARE and CLIP, and a drop in...

### R96: The attacked models are all evaluated on the suite of prompt...
- **Rubric ID**: 12e6fef6-e3d4-48a7-9696-9baf21bc5d03
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The attacked models are all evaluated on the suite of prompts.
- **Parent context**: The jailbreaking attacks are correctly evaluated on LLaVA with TeCoA, FARE, and the original CLIP en...

### R97: The number of passed prompts is reported for categories any,...
- **Rubric ID**: e6459598-9f4e-40ac-a8cc-65fc0026488a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The number of passed prompts is reported for categories any, identity, disinfo, crime, x-risk, in a format comparable to Table 7.
- **Parent context**: The jailbreaking attacks are correctly evaluated on LLaVA with TeCoA, FARE, and the original CLIP en...

### R98: FARE and TECOA are effective even at higher radii than what...
- **Rubric ID**: 0eb6514c-7563-47cb-90d5-cc455337c5c3
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FARE and TECOA are effective even at higher radii than what they were trained at.
- **Parent context**: The trends are consistent with those in section 4.4, including the benefits of using a robust versio...

### R99: FARE and TeCoA defend against significantly more attacks tha...
- **Rubric ID**: b22a53f6-c8b0-4751-897e-0d351b4eecf1
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FARE and TeCoA defend against significantly more attacks than CLIP.
- **Parent context**: The trends are consistent with those in section 4.4, including the benefits of using a robust versio...

### R100: FARE and TeCoA are roughly equally effective for all the val...
- **Rubric ID**: 991b408d-491d-486d-8f31-f086da23d2a1
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: FARE and TeCoA are roughly equally effective for all the values of epsilon in Table 7.
- **Parent context**: The trends are consistent with those in section 4.4, including the benefits of using a robust versio...

## Logging, Analysis & Presentation

### R101: The ground-truth caption and corresponding adversarial pertu...
- **Rubric ID**: daefe337-8286-4a54-8b93-ef52fd7a79dc
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The ground-truth caption and corresponding adversarial perturbation that produced the lowest score are saved for use in subsequent single-precision attacks
- **Parent context**: The CIDEr scores have been correctly computed and tracked throughout the attack process:

### R102: The ground-truth answer and corresponding adversarial pertur...
- **Rubric ID**: b406d554-56fd-4444-be4d-c0e6581d490f
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The ground-truth answer and corresponding adversarial perturbation that produced the lowest score are saved for use in subsequent single-precision attacks
- **Parent context**: The VQA accuracy scores have been correctly computed and tracked throughout the attack process:

### R103: The above zero-shot accuracies are reported.
- **Rubric ID**: d66c762d-da5e-4332-967d-58676f70fab8
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The above zero-shot accuracies are reported.
- **Parent context**: The results of zero-shot classification from Section 4.3 have been correctly reproduced.

### R104: The above POPE scores have been reported along with their me...
- **Rubric ID**: 58c0a841-bb93-4d48-8e35-3add13851733
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The above POPE scores have been reported along with their mean, in a format comparable to Table 5.
- **Parent context**: LLaVA has been evaluated (separately for each visual encoder) on hallucinations using the POPE bench...

### R105: The SQA-I scores are reported for LLaVA with the five visual...
- **Rubric ID**: 903b64f8-4006-483f-9022-380aee0a7a39
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The SQA-I scores are reported for LLaVA with the five visual encoders.
- **Parent context**: LLaVA with TeCoA and FARE has been correctly evaluated on the SQA-I benchmark as in section 4.4.

### R106: There is a drop in the score for TeCOA of SQA-I, when compar...
- **Rubric ID**: 292f770f-491f-44ef-8c1e-2aa4f865d7e8
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: There is a drop in the score for TeCOA of SQA-I, when compared with FARE and CLIP.
- **Parent context**: The trends in section 4.4 are observed, including comparable scores for FARE and CLIP, and a drop in...
