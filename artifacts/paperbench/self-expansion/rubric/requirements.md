# Rubric Requirements — self-expansion
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 253

## Dataset and Model Acquisition

### R01: Code has been implemented such that a ViT-B/16 model pretrai...
- **Rubric ID**: 5b88aaa9-8bf2-4346-ad0d-4656eb6a0dd9
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been implemented such that a ViT-B/16 model pretrained on ImageNet-1K can be loaded into memory
- **Parent context**: The paper 'Self-Expansion of Pre-trained Models with Mixture of Adapters for Continual Learning' has...

### R02: The train and test sets of CIFAR-100 are available
- **Rubric ID**: 3aabf7f3-3079-4a8b-8953-37ad230f8992
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The train and test sets of CIFAR-100 are available
- **Parent context**: The datasets from Section 4.1 have been imported.

### R03: The train and test sets of of ImageNet-R are available
- **Rubric ID**: 3964f08d-b6c6-4b00-ad76-1e736728aa94
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The train and test sets of of ImageNet-R are available
- **Parent context**: The datasets from Section 4.1 have been imported.

### R04: The train and test sets of ImageNet-A are available
- **Rubric ID**: b4553344-eb16-4a4d-a410-216a1d413a99
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The train and test sets of ImageNet-A are available
- **Parent context**: The datasets from Section 4.1 have been imported.

## Data Processing & Preparation

### R05: The train and test sets of VTAB are available. The VTAB data...
- **Rubric ID**: f727d425-215a-486a-b0ef-9fe5b2057e23
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The train and test sets of VTAB are available. The VTAB dataset used is the VTAB subset from the ADAM paper; only five domains are used, and the domain order is fixed to "resisc45 10-19; dtd 20-29; pets 30-39; eurosat 40-49; flowers 50-59". Only 10 classes are selected and used for each domain; the numbers denote the class index of the 10 classes for each domain. For example, 10-19 denotes the 10th - 19th classes are in resisc are used. The original resisc contains 45 classes.
- **Parent context**: The datasets from Section 4.1 have been imported.

### R06: Datasets (CIFAR-100, ImageNet_R, ImageNet-A) are split in a...
- **Rubric ID**: 638c80be-8c5f-43a4-b24a-33bba041660d
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Datasets (CIFAR-100, ImageNet_R, ImageNet-A) are split in a manner where each task/domain consists of 10 distinct classes
- **Parent context**: The datasets from Section 4.1 have been imported.

## Method Implementation

### R07: The LoRA adapter can be applied (it is either implemented or...
- **Rubric ID**: 2fc5dc38-c1b5-419d-a2ea-4629b27b85b2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The LoRA adapter can be applied (it is either implemented or an existing implementation is imported)
- **Parent context**: The LoRA, Convpass and ADAM adapters are available

### R08: The Convpass adapter architecture has been implemented from...
- **Rubric ID**: 7fa8715e-3ab6-4116-be67-eb1baeb1d8de
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The Convpass adapter architecture has been implemented from https://github.com/JieShibo/PETL-ViT/blob/main/convpass/vtab/convpass.py and can be selected as the functional adapter
- **Parent context**: The LoRA, Convpass and ADAM adapters are available

### R09: The ADAM "adapter" is implemented from https://github.com/Sh...
- **Rubric ID**: e0aa0321-72f7-447b-b98d-06527a5fa4bf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The ADAM "adapter" is implemented from https://github.com/ShoufaChen/AdaptFormer/blob/main/models/adapter.py
- **Parent context**: The LoRA, Convpass and ADAM adapters are available

### R10: The functional adapter has been implemented correctly as des...
- **Rubric ID**: dc0de847-ec32-40f3-9f7b-3b056ba43a3e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The functional adapter has been implemented correctly as described in Section 3.3, as a learnable down projection layer, then a ReLU function, then a learnable up projection layer
- **Parent context**: The functional adapter, representation descriptor, and router have been implemented correctly

### R11: The encoder of the representation descriptor is implemented...
- **Rubric ID**: 2da70bdf-21c8-487f-83b5-091929ce056c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The encoder of the representation descriptor is implemented as a linear layer that projects to 128 dimensions
- **Parent context**: The representation descriptor is implemented as an autoencoder with an encoder, non-linearity, then ...

### R12: LeakyReLU is applied to the output of the encoder of the rep...
- **Rubric ID**: 6c7fab21-2130-4f8e-a472-1722b8fa8643
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LeakyReLU is applied to the output of the encoder of the representation descriptor
- **Parent context**: The representation descriptor is implemented as an autoencoder with an encoder, non-linearity, then ...

### R13: The decoder of the representation descriptor is implemented...
- **Rubric ID**: f76f7de8-b0f0-4bf6-ad9c-5c45bdf027aa
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The decoder of the representation descriptor is implemented as a linear layer that projects from 128 dimensions back to the original dimensionality
- **Parent context**: The representation descriptor is implemented as an autoencoder with an encoder, non-linearity, then ...

### R14: The router has been implemented as a linear mapping function...
- **Rubric ID**: b990c55b-8d9b-47e5-ba2a-ab8050e26eb9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The router has been implemented as a linear mapping function (using a learnable matrix) followed by a softmax operation
- **Parent context**: The functional adapter, representation descriptor, and router have been implemented correctly

### R15: The output of the second normalization layer (after the firs...
- **Rubric ID**: c1e41bb2-f119-4577-ab3b-6ea9cb4d7467
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The output of the second normalization layer (after the first normalization layer, then multi-head self-attention, then residual connection) is used as input for the representation descriptors, functional adapters, and router
- **Parent context**: The functional adapter, representation descriptor and router have been correctly integrated into a t...

### R16: A linear combination of the outputs of the functional adapte...
- **Rubric ID**: 8f70800b-dc7b-4ad2-845e-78966f029223
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: A linear combination of the outputs of the functional adapters is computed, with the weights corresponding to the output of the router
- **Parent context**: The functional adapter, representation descriptor and router have been correctly integrated into a t...

### R17: A linear combination of the outputs of the functional adapte...
- **Rubric ID**: 7cf18f2c-1622-477d-b5b4-2c3359bec297
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: A linear combination of the outputs of the functional adapters is added to the output of the fully connected layer and the residual layer in the transformer block to produce the output for the transformer layer
- **Parent context**: The functional adapter, representation descriptor and router have been correctly integrated into a t...

### R18: When training SEMA, the z-score corresponding to the $k$-th...
- **Rubric ID**: 85768b74-9fe9-470f-9166-490c2a6f6eb2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When training SEMA, the z-score corresponding to the $k$-th representation descriptor in layer $l$ can be computed as $z_k^l = (r_k^l - u_k^l)/\sigma_k^l$, where $r_k^l$ is the reconstruction error of the current input, $u_k^l$ is the associated running mean of the representation descriptor, and $\sigma_k^l$ is the associated running standard deviation of the representation descriptor
- **Parent context**: The training loop of SEMA has been implemented correctly.

### R19: When training SEMA on the $t$-th task, before starting any t...
- **Rubric ID**: 3345ee1d-7c91-4f35-a34d-cc884f7381c7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When training SEMA on the $t$-th task, before starting any training, the layers that are valid for expansion are scanned iteratively for evaluating whether layers should have adapters added, from shallowest to deepest
- **Parent context**: When training SEMA, for a dataset containing $n_t$ samples for the $t$-th task, the SEMA algorithm h...

### R20: When training SEMA on the $t$-th task, when scanning each la...
- **Rubric ID**: ddf48454-e7b6-41ea-8133-4accd720eee6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When training SEMA on the $t$-th task, when scanning each layer, if after some sample, all the z-scores of all the representation descriptors on some layer are above some pre-defined threshold, an expansion signal is triggered for such layer, and an adapter is added to such layer and trained on the task $t$. After training on the task $t$, the next deepest layer is scanned. If no deeper layer exists, the training proceeds to the next task, and the scanning restarts from the first (valid) layer
- **Parent context**: When training SEMA, for a dataset containing $n_t$ samples for the $t$-th task, the SEMA algorithm h...

### R21: When training SEMA on the $t$-th task, when scanning each la...
- **Rubric ID**: ac81c23b-6d25-457b-be95-e20264c29e1b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When training SEMA on the $t$-th task, when scanning each layer, if no expansion signals are triggered, the task is skipped (no training is performed for such task and no adapters are added), and all existing functional adapters and representation descriptors are frozen
- **Parent context**: When training SEMA, for a dataset containing $n_t$ samples for the $t$-th task, the SEMA algorithm h...

### R22: When training SEMA, when adding a new adapter, the weights i...
- **Rubric ID**: f3854228-889d-4a91-8d17-399677173729
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When training SEMA, when adding a new adapter, the weights in the new adapter are learnable, and all the weights in the other adapters in all other layers are frozen.
- **Parent context**: When training SEMA, when adding a new adapter and retraining, the parameters to freeze / update have...

### R23: When training SEMA, when adding a new adapter, the weights i...
- **Rubric ID**: 2d34ab6a-eae2-4df9-845f-6d0c680dacc5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When training SEMA, when adding a new adapter, the weights in the representation descriptor corresponding to the new adapter are learnable, and all the other weights in the other representation descriptors are frozen.
- **Parent context**: When training SEMA, when adding a new adapter and retraining, the parameters to freeze / update have...

### R24: When a new task is added, the classification head has been e...
- **Rubric ID**: 9aeec6b6-c3c2-40a1-b1f7-c56fda9c4983
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When a new task is added, the classification head has been expanded to handle the new classes
- **Parent context**: The training loop of SEMA has been implemented correctly.

### R25: For training SEMA, the loss of the model $F$ is implemented...
- **Rubric ID**: 061cf57d-6d29-4850-85eb-99934f8e65b3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For training SEMA, the loss of the model $F$ is implemented correctly; given an input-label pair $(x, y)$, the cross entropy loss between the output of the model $F(x)$ and $y$ is computed
- **Parent context**: When training SEMA, the training loss and its components including the cross-entropy loss and the re...

### R26: For training SEMA, the reconstruction loss for the represent...
- **Rubric ID**: 5b0fa5b0-bd67-47d4-be6b-f90527f85a49
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For training SEMA, the reconstruction loss for the representation descriptors is implemented correctly; given an input $x$ to the representation descriptor $g$, the loss is computed as the 2-norm of the difference between the input and output; $||x - g(x)||_2^2$
- **Parent context**: When training SEMA, the training loss and its components including the cross-entropy loss and the re...

### R27: For training SEMA, the overall loss given an input-label pai...
- **Rubric ID**: 7c152eab-cdfd-4c02-8107-8f72fff4006b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For training SEMA, the overall loss given an input-label pair $(x, y)$ is computed as the cross-entropy loss of the output of the network with the label $y$ and the sum of reconstruction losses of all representation descriptors across all layers
- **Parent context**: When training SEMA, the training loss and its components including the cross-entropy loss and the re...

### R28: The Finetune Adapter baseline is implemented by adding one S...
- **Rubric ID**: 821e4ced-2ead-46e8-bd3b-80a6b5ab3d98
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The Finetune Adapter baseline is implemented by adding one SEMA adapter to each of all layers in the frozen ViT
- **Parent context**: The Finetune Adapter baseline has been implemented

### R29: L2P has been implemented, using the implementation available...
- **Rubric ID**: 2522988f-d45e-4537-94a9-c4748671883e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: L2P has been implemented, using the implementation available within this repo: https://github.com/sun-hailong/LAMDA-PILOT
- **Parent context**: The baseline methods have been implemented, as in Section 4.1.

### R30: DualPrompt has been implemented, using the implementation av...
- **Rubric ID**: e40c9f90-3815-4876-a944-68673586aa1e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: DualPrompt has been implemented, using the implementation available within this repo: https://github.com/sun-hailong/LAMDA-PILOT
- **Parent context**: The baseline methods have been implemented, as in Section 4.1.

### R31: CODA-P has been implemented, using the implementation availa...
- **Rubric ID**: 65005d38-e4e9-44c5-a08c-d05e9856ed20
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: CODA-P has been implemented, using the implementation available within this repo: https://github.com/sun-hailong/LAMDA-PILOT
- **Parent context**: The baseline methods have been implemented, as in Section 4.1.

### R32: SimpleCIL has been implemented, using the official implement...
- **Rubric ID**: 258321d1-3921-4d88-a955-42c4d6a75683
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: SimpleCIL has been implemented, using the official implementation at https://github.com/zhoudw-zdw/RevisitingCIL
- **Parent context**: The baseline methods have been implemented, as in Section 4.1.

### R33: ADAM with Adapter has been implemented, using the official i...
- **Rubric ID**: 897aae5d-6cef-4135-9266-b432afef1cf7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: ADAM with Adapter has been implemented, using the official implementation at https://github.com/zhoudw-zdw/RevisitingCIL
- **Parent context**: The baseline methods have been implemented, as in Section 4.1.

### R34: Self-expansion is only enabled in the last three transformer...
- **Rubric ID**: 39b9fadf-ef29-480e-9084-279e30bf9e0e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Self-expansion is only enabled in the last three transformer layers.
- **Parent context**: The hyperparameters stated in Section 4.1 have been used, unless otherwise stated

### R35: The adapters in SEMA and ADAM project down to a dimensionali...
- **Rubric ID**: 253a9dca-1d45-4c3f-af01-2347893e39b3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The adapters in SEMA and ADAM project down to a dimensionality of 48
- **Parent context**: The hyperparameters stated in Section 4.1 have been used, unless otherwise stated

### R36: The architecture variant "No Expansion" introduced in Sectio...
- **Rubric ID**: f4446727-6b06-4e68-b065-367ce9d5161e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" is a variant of SEMA that has one adapter per layer of the transformer
- **Parent context**: The architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module exp...

### R37: The architecture variant "No Expansion" introduced in Sectio...
- **Rubric ID**: 3ebfcc70-eabc-42b3-bfce-610813252204
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" does not add adapters during training, i.e., there is no self-expansion
- **Parent context**: The architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module exp...

### R38: The architecture variant "No Expansion" introduced in Sectio...
- **Rubric ID**: 55756009-1626-491e-8875-d7ccb8b80778
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" does train the adapters after the first task
- **Parent context**: The architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module exp...

### R39: The architecture variant "Average Weighting" introduced in S...
- **Rubric ID**: 952bbc57-c7f9-45e3-b440-825ad0ea994d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The architecture variant "Average Weighting" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" is implemented as a variant of the SEMA architecture that uses an average weighting of the outputs of the functional adapters (e.g. the router has the same weight for each adapter)
- **Parent context**: The architecture variants introduced in Section 4.3 on "Ablation studies on module expansion and ada...

### R40: The architecture variant "Random Weighting" introduced in Se...
- **Rubric ID**: a5959da9-798c-4eb0-9579-c3a92e23191c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The architecture variant "Random Weighting" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" is implemented as a variant of the SEMA architecture that uses a linear combination (from random weights) of the outputs of the functional adapters (e.g. the router has random weights for each adapter), where the random weights are re-computed per-sample
- **Parent context**: The architecture variants introduced in Section 4.3 on "Ablation studies on module expansion and ada...

### R41: The architecture variant "Top-1 Selection" introduced in Sec...
- **Rubric ID**: 4eed6ff6-738b-4515-a0fb-dfddd356b957
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The architecture variant "Top-1 Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" is implemented as a variant of the SEMA architecture that only uses the output of the single adapter that has the highest weight from the router during both training and inference
- **Parent context**: The architecture variants introduced in Section 4.3 on "Ablation studies on module expansion and ada...

### R42: The architecture variant "Random Selection" introduced in Se...
- **Rubric ID**: aecc19c4-4c4c-4929-a596-52080af9f789
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The architecture variant "Random Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" is implemented as a variant of the SEMA architecture that only uses the output of the single adapter chosen at random, where the adapter that is randomly chosen is re-computed (randomly) per-sample
- **Parent context**: The architecture variants introduced in Section 4.3 on "Ablation studies on module expansion and ada...

### R43: The architecture variant "Top-1 Selection" introduced in Sec...
- **Rubric ID**: 02c22ec6-80c7-4bd1-b709-213d921c70dd
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The architecture variant "Top-1 Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" is implemented as a variant of the SEMA architecture that uses the standard SEMA method during training, but during inference only uses the output of the single adapter that has the highest router weight
- **Parent context**: The architecture variants introduced in Section 4.3 on "Ablation studies on module expansion and ada...

## Experimental Setup

### R44: When training SEMA, the parameters of the pretrained model (...
- **Rubric ID**: 505dd960-6d1e-4a62-8627-5da5b3b51043
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: When training SEMA, the parameters of the pretrained model (e.g. ViT) are frozen.
- **Parent context**: The training loop of SEMA has been implemented correctly.

### R45: When training SEMA, the running statistics of the mean and s...
- **Rubric ID**: 186e1f6a-31bb-4df7-b44e-41544010b083
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: When training SEMA, the running statistics of the mean and standard deviation of the reconstruction error are stored for each representation descriptor, using the previous 500 samples (over all tasks) that were used for training prior to the current sample
- **Parent context**: The training loop of SEMA has been implemented correctly.

### R46: When training SEMA, when adding a new adapter, the weights i...
- **Rubric ID**: ede350f7-1ac5-4f6b-ad2c-3f97d24881f4
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: When training SEMA, when adding a new adapter, the weights in the router corresponding to the new adapter are learnable parameters, and all the other weights in the router are frozen.
- **Parent context**: When training SEMA, when adding a new adapter and retraining, the parameters to freeze / update have...

### R47: The Finetune Adapter baseline is trained by continually fine...
- **Rubric ID**: 213fe0b4-346f-4c1f-b7b2-23f198b3e03e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The Finetune Adapter baseline is trained by continually fine-tuning the SEMA adapters throughout all tasks in the task stream encountered during training
- **Parent context**: The Finetune Adapter baseline has been implemented

### R48: When training the Finetune Adapter baseline, the backbone Vi...
- **Rubric ID**: 033c6646-e283-4075-923b-e16e70c3320e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: When training the Finetune Adapter baseline, the backbone ViT is frozen and only the (parameters of the) adapters are updated continually by all tasks
- **Parent context**: The Finetune Adapter baseline has been implemented

### R49: All adapters are trained for 5 epochs.
- **Rubric ID**: 06cd5080-8910-4fe1-88e7-6d75b10c6ddb
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All adapters are trained for 5 epochs.
- **Parent context**: The hyperparameters stated in Section 4.1 have been used, unless otherwise stated

### R50: The representation descriptors are trained for 20 epochs.
- **Rubric ID**: 256cc0e7-eb7b-4514-8a17-821098949e4e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The representation descriptors are trained for 20 epochs.
- **Parent context**: The hyperparameters stated in Section 4.1 have been used, unless otherwise stated

### R51: The batch size is 32.
- **Rubric ID**: 4b60235a-76f2-4412-933b-37b370fb319d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The batch size is 32.
- **Parent context**: The hyperparameters stated in Section 4.1 have been used, unless otherwise stated

### R52: SGD is used as the optimizer.
- **Rubric ID**: 5ecb2fba-990a-4b97-b510-7e26d3eb257f
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: SGD is used as the optimizer.
- **Parent context**: SGD is used as the optimizer, and the learning rates and schedules are consistent with those in Sect...

### R53: The initial learning rate is set to 0.005 for adapters.
- **Rubric ID**: 81f71ca5-7f2b-45b9-9c44-a8ee5da1563b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The initial learning rate is set to 0.005 for adapters.
- **Parent context**: The learning rates are correct.

### R54: The initial learning rate is set to 0.01 for representationa...
- **Rubric ID**: ed1f909f-6dbd-4622-8307-fe24e0fd22e2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The initial learning rate is set to 0.01 for representational descriptors.
- **Parent context**: The learning rates are correct.

### R55: The learning rate decays with cosine annealing.
- **Rubric ID**: 3be032fb-a0c4-47c1-9311-f17a0dcd1fd1
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The learning rate decays with cosine annealing.
- **Parent context**: SGD is used as the optimizer, and the learning rates and schedules are consistent with those in Sect...

### R56: The Finetune Adapter baseline has been trained on the CIFAR-...
- **Rubric ID**: 192d5f0a-8465-42bd-8ec6-b7e71ca5f33f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The Finetune Adapter baseline has been trained on the CIFAR-100 dataset
- **Parent context**: The Finetune Adapter has trained and evaluated on the CIFAR-100 dataset

### R57: The Finetune Adapter baseline has been trained on the ImageN...
- **Rubric ID**: 69a418f5-05c9-44b5-8d69-5b0a94573144
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The Finetune Adapter baseline has been trained on the ImageNet-R dataset
- **Parent context**: The Finetune Adapter has been trained and evaluated on the ImageNet-R dataset

### R58: The Finetune Adapter baseline has been trained on the ImageN...
- **Rubric ID**: 13236aed-6725-40b8-b833-a0dc8a806bf6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The Finetune Adapter baseline has been trained on the ImageNet-A dataset
- **Parent context**: The Finetune Adapter has been trained and evaluated on the ImageNet-A dataset

### R59: The Finetune Adapter baseline has been trained on the VTAB d...
- **Rubric ID**: 0a7f5caf-0714-4bd9-b575-c0f0e59d48eb
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The Finetune Adapter baseline has been trained on the VTAB dataset
- **Parent context**: The Finetune Adapter has been trained and evaluated on the VTAB dataset

### R60: The L2P baseline has been trained on the CIFAR-100 dataset
- **Rubric ID**: e8a269ed-6bc4-4cfc-90b0-64790b6bec74
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The L2P baseline has been trained on the CIFAR-100 dataset
- **Parent context**: The L2P baseline has trained and evaluated on the CIFAR-100 dataset

### R61: The L2P baseline has been trained on the ImageNet-R dataset
- **Rubric ID**: 05874696-8483-4a4b-b7ac-7c1cbe1a6b60
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The L2P baseline has been trained on the ImageNet-R dataset
- **Parent context**: The L2P baseline has been trained and evaluated on the ImageNet-R dataset

### R62: The L2P baseline has been trained on the ImageNet-A dataset
- **Rubric ID**: eb076b13-d21f-48dd-89e8-ede70f119a75
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The L2P baseline has been trained on the ImageNet-A dataset
- **Parent context**: The L2P baseline has been trained and evaluated on the ImageNet-A dataset

### R63: The L2P baseline has been trained on the VTAB dataset
- **Rubric ID**: dbdf1a55-a18a-42d1-ba50-0e335e574596
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The L2P baseline has been trained on the VTAB dataset
- **Parent context**: The L2P baseline has been trained and evaluated on the VTAB dataset

### R64: The DualPrompt baseline has been trained on the CIFAR-100 da...
- **Rubric ID**: 2f9a66b3-8474-426c-a5b8-c6be1000c987
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DualPrompt baseline has been trained on the CIFAR-100 dataset
- **Parent context**: The DualPrompt baseline has trained and evaluated on the CIFAR-100 dataset

### R65: The DualPrompt baseline has been trained on the ImageNet-R d...
- **Rubric ID**: 09d9ee7d-f276-4f97-901a-e16bfa510d2f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DualPrompt baseline has been trained on the ImageNet-R dataset
- **Parent context**: The DualPrompt baseline has been trained and evaluated on the ImageNet-R dataset

### R66: The DualPrompt baseline has been trained on the ImageNet-A d...
- **Rubric ID**: da7fdd37-7d05-4d35-bac7-75fc9e753d5d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DualPrompt baseline has been trained on the ImageNet-A dataset
- **Parent context**: The DualPrompt baseline has been trained and evaluated on the ImageNet-A dataset

### R67: The DualPrompt baseline has been trained on the VTAB dataset
- **Rubric ID**: cd7a377f-e43b-4dc8-9c57-4321323c03eb
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The DualPrompt baseline has been trained on the VTAB dataset
- **Parent context**: The DualPrompt baseline has been trained and evaluated on the VTAB dataset

### R68: The CODA-P baseline has been trained on the CIFAR-100 datase...
- **Rubric ID**: 0e3ef2ca-c244-41b9-9a7d-984e76a8023f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The CODA-P baseline has been trained on the CIFAR-100 dataset
- **Parent context**: The CODA-P baseline has trained and evaluated on the CIFAR-100 dataset

### R69: The CODA-P baseline has been trained on the ImageNet-R datas...
- **Rubric ID**: 7a6875cc-6817-4aa0-8b17-4fb38be67d98
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The CODA-P baseline has been trained on the ImageNet-R dataset
- **Parent context**: The CODA-P baseline has been trained and evaluated on the ImageNet-R dataset

### R70: The CODA-P baseline has been trained on the ImageNet-A datas...
- **Rubric ID**: 375b7bcb-d19d-4766-9d81-c87c19cfc26a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The CODA-P baseline has been trained on the ImageNet-A dataset
- **Parent context**: The CODA-P baseline has been trained and evaluated on the ImageNet-A dataset

### R71: The CODA-P baseline has been trained on the VTAB dataset
- **Rubric ID**: 185b60df-f765-4a82-a32e-d3b566769ace
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The CODA-P baseline has been trained on the VTAB dataset
- **Parent context**: The CODA-P baseline has been trained and evaluated on the VTAB dataset

### R72: The SimpleCIL baseline has been trained on the CIFAR-100 dat...
- **Rubric ID**: a090a7e3-19b6-4e0a-8b68-5b545b95de2a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The SimpleCIL baseline has been trained on the CIFAR-100 dataset
- **Parent context**: The SimpleCIL baseline has trained and evaluated on the CIFAR-100 dataset

### R73: The SimpleCIL baseline has been trained on the ImageNet-R da...
- **Rubric ID**: 0d712907-d5e4-4b19-96c9-2b002c5e744d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The SimpleCIL baseline has been trained on the ImageNet-R dataset
- **Parent context**: The SimpleCIL baseline has been trained and evaluated on the ImageNet-R dataset

### R74: The SimpleCIL baseline has been trained on the ImageNet-A da...
- **Rubric ID**: 4925dc88-99f5-48eb-9c9e-65da2ec4dae5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The SimpleCIL baseline has been trained on the ImageNet-A dataset
- **Parent context**: The SimpleCIL baseline has been trained and evaluated on the ImageNet-A dataset

### R75: The SimpleCIL baseline has been trained on the VTAB dataset
- **Rubric ID**: c9f55aa9-84d3-449b-8a2f-5ca6dea7c5fc
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The SimpleCIL baseline has been trained on the VTAB dataset
- **Parent context**: The SimpleCIL baseline has been trained and evaluated on the VTAB dataset

### R76: The ADAM baseline has been trained on the CIFAR-100 dataset
- **Rubric ID**: 35932abf-afbd-42d8-8c4f-5c1f26467332
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The ADAM baseline has been trained on the CIFAR-100 dataset
- **Parent context**: The ADAM baseline has trained and evaluated on the CIFAR-100 dataset

### R77: The ADAM baseline has been trained on the ImageNet-R dataset
- **Rubric ID**: 9a0968f0-3799-4179-afbf-e8c354a8b711
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The ADAM baseline has been trained on the ImageNet-R dataset
- **Parent context**: The ADAM baseline has been trained and evaluated on the ImageNet-R dataset

### R78: The ADAM baseline has been trained on the ImageNet-A dataset
- **Rubric ID**: ddea6ece-9300-4804-b36a-f12f1d94528c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The ADAM baseline has been trained on the ImageNet-A dataset
- **Parent context**: The ADAM baseline has been trained and evaluated on the ImageNet-A dataset

### R79: The ADAM baseline has been trained on the VTAB dataset
- **Rubric ID**: 52b8105c-c036-4406-a71e-ea3b02c2c7e4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The ADAM baseline has been trained on the VTAB dataset
- **Parent context**: The ADAM baseline has been trained and evaluated on the VTAB dataset

### R80: SEMA has been trained on the CIFAR-100 dataset
- **Rubric ID**: 2bc9441f-5df1-4692-b9c4-bca597a7431f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SEMA has been trained on the CIFAR-100 dataset
- **Parent context**: SEMA has trained and evaluated on the CIFAR-100 dataset

### R81: SEMA has been trained on the ImageNet-R dataset
- **Rubric ID**: 765a25a3-5d23-47ef-9cf5-3c409f042b94
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SEMA has been trained on the ImageNet-R dataset
- **Parent context**: SEMA has been trained and evaluated on the ImageNet-R dataset

### R82: SEMA has been trained on the ImageNet-A dataset
- **Rubric ID**: cd6d6a59-bcbe-4a9a-9aa6-6bde44b1df1a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SEMA has been trained on the ImageNet-A dataset
- **Parent context**: SEMA has been trained and evaluated on the ImageNet-A dataset

### R83: SEMA has been trained on the VTAB dataset
- **Rubric ID**: 1dfccd39-cef3-4ad8-823e-4183d4092d85
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SEMA has been trained on the VTAB dataset
- **Parent context**: SEMA has been trained and evaluated on the VTAB dataset

### R84: The architecture variant "No Expansion" introduced in Sectio...
- **Rubric ID**: ef33c6a5-add3-4836-a25e-a9bf30ae2b5f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" has been trained on ImageNet-A
- **Parent context**: The architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module exp...

### R85: The architecture variant "No Expansion" introduced in Sectio...
- **Rubric ID**: 5e45d561-3737-4289-baa0-8555670e27dc
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" has been trained on VTAB
- **Parent context**: The architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module exp...

### R86: The architecture variant "Average Weighting" introduced in S...
- **Rubric ID**: 135f6fdc-ee33-40f1-ae9f-164625f2f755
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The architecture variant "Average Weighting" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" has been trained on ImageNet-A
- **Parent context**: The architecture variant "Average Weighting" introduced in Section 4.3 on "Ablation studies on modul...

### R87: The architecture variant "Average Weighting" introduced in S...
- **Rubric ID**: 1bc09532-d65f-4e7f-87db-ee875ad0a28c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The architecture variant "Average Weighting" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" has been trained on VTAB
- **Parent context**: The architecture variant "Average Weighting" introduced in Section 4.3 on "Ablation studies on modul...

### R88: The architecture variant "Random Weighting" introduced in Se...
- **Rubric ID**: 1d30f56d-b0c8-4b5e-845e-153ee9a723ed
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The architecture variant "Random Weighting" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" has been trained on ImageNet-A
- **Parent context**: The architecture variant "Random Weighting" introduced in Section 4.3 on "Ablation studies on module...

### R89: The architecture variant "Random Weighting" introduced in Se...
- **Rubric ID**: 1325a4b3-1e03-493a-9b59-fc0ba78a3b89
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The architecture variant "Random Weighting" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" has been trained on VTAB
- **Parent context**: The architecture variant "Random Weighting" introduced in Section 4.3 on "Ablation studies on module...

### R90: The architecture variant "Top-1 Selection" introduced in Sec...
- **Rubric ID**: 4f01fac3-3bb3-456d-851d-541b77d26186
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The architecture variant "Top-1 Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" has been trained on ImageNet-A
- **Parent context**: The architecture variant "Top-1 Selection" introduced in Section 4.3 on "Ablation studies on module ...

### R91: The architecture variant "Top-1 Selection" introduced in Sec...
- **Rubric ID**: 8c9ebd55-9b06-4251-95d0-1d4c5cf787e4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The architecture variant "Top-1 Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" has been trained on VTAB
- **Parent context**: The architecture variant "Top-1 Selection" introduced in Section 4.3 on "Ablation studies on module ...

### R92: The architecture variant "Random Selection" introduced in Se...
- **Rubric ID**: 70e161eb-5840-4210-8c38-eb7c66844a36
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The architecture variant "Random Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" has been trained on ImageNet-A
- **Parent context**: The architecture variant "Random Selection" introduced in Section 4.3 on "Ablation studies on module...

### R93: The architecture variant "Random Selection" introduced in Se...
- **Rubric ID**: 6bd258ed-e7c4-401d-a496-390255ec65cf
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The architecture variant "Random Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" has been trained on VTAB
- **Parent context**: The architecture variant "Random Selection" introduced in Section 4.3 on "Ablation studies on module...

### R94: The architecture variant "Top-1 Selection Inference" introdu...
- **Rubric ID**: 0cf9f0b3-7cc6-4175-823f-b3fc04f2eda7
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The architecture variant "Top-1 Selection Inference" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" has been trained on ImageNet-A
- **Parent context**: The architecture variant "Top-1 Selection Inference" introduced in Section 4.3 on "Ablation studies ...

### R95: The architecture variant "Top-1 Selection Inference" introdu...
- **Rubric ID**: 7bf23f28-f39e-4f0f-a458-fe136c2f9490
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The architecture variant "Top-1 Selection Inference" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing" has been trained on VTAB
- **Parent context**: The architecture variant "Top-1 Selection Inference" introduced in Section 4.3 on "Ablation studies ...

### R96: For the SEMA model trained for the experiment in in Section...
- **Rubric ID**: c35a2668-8fd3-4a0c-8012-ecbf780f84a9
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For the SEMA model trained for the experiment in in Section 4.3 on "Analysis on dynamic expansion process", self-expansion is limited to the final layer of the transformer
- **Parent context**: The experiments required to replicate the results in Section 4.3 on "Analysis on dynamic expansion p...

### R97: The modified SEMA model for Section 4.3 on "Analysis on dyna...
- **Rubric ID**: 30c33054-c83b-432e-b942-fc35a06beaea
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The modified SEMA model for Section 4.3 on "Analysis on dynamic expansion process" is trained on the first five tasks from the VTAB dataset
- **Parent context**: The experiments required to replicate the results in Section 4.3 on "Analysis on dynamic expansion p...

### R98: SEMA is separately trained with expansion thresholds 1.0, 1....
- **Rubric ID**: bb921111-8c41-401a-b96d-f71da28178f0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SEMA is separately trained with expansion thresholds 1.0, 1.1, 1.2, ...., 2.0 on ImageNet-A
- **Parent context**: SEMA is separately trained with expansion thresholds 1.0, 1.1, 1.2, ...., 2.0 on ImageNet-A. For eac...

### R99: SEMA is separately trained with expansion thresholds 1.0, 1....
- **Rubric ID**: 1a82caf9-c8cd-4e7e-ac8f-925b10ef676c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SEMA is separately trained with expansion thresholds 1.0, 1.1, 1.2, ...., 2.0 on VTAB
- **Parent context**: SEMA is separately trained with expansion thresholds 1.0, 2.0, 3.0, ...., 8.0 on VTAB. For each trai...

### R100: A variant of SEMA is trained on ImageNet-A where the only la...
- **Rubric ID**: df30022a-2ae3-4cbf-a303-a0b599a06978
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A variant of SEMA is trained on ImageNet-A where the only layers allowed for self-expansion are 11-12 (the last 2 layers)
- **Parent context**: Different SEMA models are trained on ImageNet-A with varying number of layers that are allowed for s...

### R101: A variant of SEMA is trained on ImageNet-A where the only la...
- **Rubric ID**: 0a1ec651-be06-442d-b56a-6b5bd11c4a4f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A variant of SEMA is trained on ImageNet-A where the only layers allowed for self-expansion are 10-12 (the last 3 layers)
- **Parent context**: Different SEMA models are trained on ImageNet-A with varying number of layers that are allowed for s...

### R102: A variant of SEMA is trained on ImageNet-A where the only la...
- **Rubric ID**: 1fac6183-d19f-4061-baaa-5879a87781db
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A variant of SEMA is trained on ImageNet-A where the only layers allowed for self-expansion are 9-12 (the last 4 layers)
- **Parent context**: Different SEMA models are trained on ImageNet-A with varying number of layers that are allowed for s...

### R103: A variant of SEMA is trained on VTAB where the only layers a...
- **Rubric ID**: b4c0cd35-5f88-458b-89a2-2e7669d67aaa
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A variant of SEMA is trained on VTAB where the only layers allowed for self-expansion are 11-12 (the last 2 layers)
- **Parent context**: Different SEMA models are trained on VTAB with varying number of layers that are allowed for self-ex...

### R104: A variant of SEMA is trained on VTAB where the only layers a...
- **Rubric ID**: 1a95e296-a68c-4aac-8b19-88e2eec2fe88
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A variant of SEMA is trained on VTAB where the only layers allowed for self-expansion are 10-12 (the last 3 layers)
- **Parent context**: Different SEMA models are trained on VTAB with varying number of layers that are allowed for self-ex...

### R105: A variant of SEMA is trained on VTAB where the only layers a...
- **Rubric ID**: 411ec21b-24e6-42cc-bde6-31b602f51e59
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A variant of SEMA is trained on VTAB where the only layers allowed for self-expansion are 9-12 (the last 4 layers)
- **Parent context**: Different SEMA models are trained on VTAB with varying number of layers that are allowed for self-ex...

### R106: A variant of the SEMA architecture that uses the "Adapter" a...
- **Rubric ID**: 65b2a690-5e4f-40dd-bea6-e4d65224621b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A variant of the SEMA architecture that uses the "Adapter" adapter from the baseline has been trained on the ImageNet-A dataset
- **Parent context**: A variant of the SEMA architecture using the "Adapter" adapter from the baseline has been trained on...

### R107: A variant of the SEMA architecture that uses the "Adapter" a...
- **Rubric ID**: aa90c0b1-8464-44b0-9244-8de8acebfcf8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A variant of the SEMA architecture that uses the "Adapter" adapter from the baseline has been trained on the VTAB dataset
- **Parent context**: A variant of the SEMA architecture using the "Adapter" adapter from the baseline has been trained on...

### R108: A variant of the SEMA architecture that uses the LoRA adapte...
- **Rubric ID**: ef151297-8bd5-4d7f-8468-b920e61f2360
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A variant of the SEMA architecture that uses the LoRA adapter has been trained on the ImageNet-A dataset
- **Parent context**: A variant of the SEMA architecture using the LoRA adapter has been trained on ImageNet-A, and the av...

### R109: A variant of the SEMA architecture that uses the LoRA adapte...
- **Rubric ID**: 84f686ae-76b7-41ad-bea9-4a0a49db75ee
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A variant of the SEMA architecture that uses the LoRA adapter has been trained on the VTAB dataset
- **Parent context**: A variant of the SEMA architecture using the LoRA adapter has been trained on VTAB, and the average ...

### R110: A variant of the SEMA architecture that uses the Convpass ad...
- **Rubric ID**: 02dd9608-1f23-42bb-9669-8aa6456186ca
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A variant of the SEMA architecture that uses the Convpass adapter has been trained on the ImageNet-A dataset
- **Parent context**: A variant of the SEMA architecture using the Convpass adapter has been trained on ImageNet-A, and th...

### R111: A variant of the SEMA architecture that uses the Convpass ad...
- **Rubric ID**: 34f8c2f8-8713-4c8f-8f16-412fac11218d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A variant of the SEMA architecture that uses the Convpass adapter has been trained on the VTAB dataset
- **Parent context**: A variant of the SEMA architecture using the Convpass adapter has been trained on VTAB, and the aver...

### R112: L2P has been trained on ImageNet-A
- **Rubric ID**: 2185ffad-3111-410a-921e-fe18f43df530
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: L2P has been trained on ImageNet-A
- **Parent context**: The experiments required to replicate the results in Section 4.3 on "Ablation studies on adapter var...

### R113: DualPrompt has been trained on ImageNet-A
- **Rubric ID**: 5ce798f5-bfc2-4867-bba3-568bf4435bce
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: DualPrompt has been trained on ImageNet-A
- **Parent context**: The experiments required to replicate the results in Section 4.3 on "Ablation studies on adapter var...

### R114: CODA-P has been trained on ImageNet-A
- **Rubric ID**: 8ddf9659-1674-4d25-ae92-6527a3258791
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: CODA-P has been trained on ImageNet-A
- **Parent context**: The experiments required to replicate the results in Section 4.3 on "Ablation studies on adapter var...

### R115: SEMA has been trained on ImageNet-A
- **Rubric ID**: 5c1a9ec3-78a4-4d60-8d5e-b178264d7625
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SEMA has been trained on ImageNet-A
- **Parent context**: The experiments required to replicate the results in Section 4.3 on "Ablation studies on adapter var...

## Evaluation, Metrics & Benchmarking

### R116: When training SEMA on the $t$-th task, when scanning each la...
- **Rubric ID**: 4b3a8b1d-e03e-4f93-aab0-db267899e2a1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When training SEMA on the $t$-th task, when scanning each layer the reconstruction error is computed over all samples in the $t$-th task. No training occurs during this scanning, and no gradients are computed
- **Parent context**: When training SEMA, for a dataset containing $n_t$ samples for the $t$-th task, the SEMA algorithm h...

### R117: The average accuracy $A_N$ of all seen tasks after training...
- **Rubric ID**: 9b147fe2-16a2-4976-8242-e175b390510b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy $A_N$ of all seen tasks after training on the $N$-th task, is computed as $A_N = \frac{1}{N} \sum_{i=1}^N A_{i,N}$, where $A_{i,N}$ is the accuracy of the $i$-th task after training on the $N$-th task
- **Parent context**: The accuracy formulas are implemented correctly as in Section B.3.

### R118: The average incremental accuracy $\bar{A}$ is computed as $\...
- **Rubric ID**: db420a9d-1f89-4455-b1e3-5224229785e7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average incremental accuracy $\bar{A}$ is computed as $\bar{A} = \frac{1}{N} \sum_{t=1}^N A_t$, where $A_t$ is the average accuracy on all seen tasks after training on the $t$-th task
- **Parent context**: The accuracy formulas are implemented correctly as in Section B.3.

### R119: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 26ae9c3c-3e90-453e-9f31-5a80bd455213
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the Finetune Adapter baseline during training on the CIFAR-100 dataset has been computed using the test split
- **Parent context**: The Finetune Adapter has trained and evaluated on the CIFAR-100 dataset

### R120: The incremental accuracy of the Finetune Adapter baseline du...
- **Rubric ID**: 0b974c55-6589-4e9f-95c0-64f163ed77f6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the Finetune Adapter baseline during training on the CIFAR-100 dataset has been computed using the test split at the end of each task
- **Parent context**: The Finetune Adapter has trained and evaluated on the CIFAR-100 dataset

### R121: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: d4e485c4-a554-4ea1-8e6a-fb608e945b24
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the Finetune Adapter baseline during training on the ImageNet-R dataset has been computed using the test split
- **Parent context**: The Finetune Adapter has been trained and evaluated on the ImageNet-R dataset

### R122: The incremental accuracy of the Finetune Adapter baseline du...
- **Rubric ID**: cfca4361-1647-41e8-a4b8-cea6b6c37add
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the Finetune Adapter baseline during training on the ImageNet-R dataset has been computed using the test split at the end of each task
- **Parent context**: The Finetune Adapter has been trained and evaluated on the ImageNet-R dataset

### R123: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 16c22564-007b-4b6a-b462-3d7ab9014c3d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the Finetune Adapter baseline during training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The Finetune Adapter has been trained and evaluated on the ImageNet-A dataset

### R124: The incremental accuracy of the Finetune Adapter baseline du...
- **Rubric ID**: 579dfe1c-9ed2-4084-a203-ecabaf8b0c4b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the Finetune Adapter baseline during training on the ImageNet-A dataset has been computed using the test split at the end of each task
- **Parent context**: The Finetune Adapter has been trained and evaluated on the ImageNet-A dataset

### R125: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 9a243585-d2da-42cf-ba6e-e514a39012b6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the Finetune Adapter baseline during training on the VTAB dataset has been computed using the test split
- **Parent context**: The Finetune Adapter has been trained and evaluated on the VTAB dataset

### R126: The incremental accuracy of the Finetune Adapter baseline du...
- **Rubric ID**: 2ed1c7e3-5e32-47fd-8103-017178704161
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the Finetune Adapter baseline during training on the VTAB dataset has been computed using the test split at the end of each task
- **Parent context**: The Finetune Adapter has been trained and evaluated on the VTAB dataset

### R127: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: a1b55b52-8665-477e-b583-a3a1e331525c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the L2P baseline during training on the CIFAR-100 dataset has been computed using the test split
- **Parent context**: The L2P baseline has trained and evaluated on the CIFAR-100 dataset

### R128: The incremental accuracy of the L2P baseline during training...
- **Rubric ID**: c4bebbb6-4ab9-431b-a44c-93aca56872e6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the L2P baseline during training on the CIFAR-100 dataset has been computed using the test split at the end of each task
- **Parent context**: The L2P baseline has trained and evaluated on the CIFAR-100 dataset

### R129: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 9be7a9d0-8ac9-4df1-9dad-02abf7a2eb12
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the L2P baseline during training on the ImageNet-R dataset has been computed using the test split
- **Parent context**: The L2P baseline has been trained and evaluated on the ImageNet-R dataset

### R130: The incremental accuracy of the L2P baseline during training...
- **Rubric ID**: d52a6d71-2b3f-4c51-8ffa-9d420776880d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the L2P baseline during training on the ImageNet-R dataset has been computed using the test split at the end of each task
- **Parent context**: The L2P baseline has been trained and evaluated on the ImageNet-R dataset

### R131: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 6c0812b0-c13b-4cac-bb69-94ad1d7522b5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the L2P baseline during training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The L2P baseline has been trained and evaluated on the ImageNet-A dataset

### R132: The incremental accuracy of the L2P baseline during training...
- **Rubric ID**: 4724438d-92dd-44df-a51a-34521d2c8ea9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the L2P baseline during training on the ImageNet-A dataset has been computed using the test split at the end of each task
- **Parent context**: The L2P baseline has been trained and evaluated on the ImageNet-A dataset

### R133: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: c0b9fac8-c6f1-42f6-8340-908b9675f4c0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the L2P baseline during training on the VTAB dataset has been computed using the test split
- **Parent context**: The L2P baseline has been trained and evaluated on the VTAB dataset

### R134: The incremental accuracy of the L2P baseline during training...
- **Rubric ID**: 81a4f03e-9869-4df9-b827-b6fce4a2a8d2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the L2P baseline during training on the VTAB dataset has been computed using the test split at the end of each task
- **Parent context**: The L2P baseline has been trained and evaluated on the VTAB dataset

### R135: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: d1650d7a-0bfe-427e-ad50-840dfcbd0215
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the DualPrompt baseline during training on the CIFAR-100 dataset has been computed using the test split
- **Parent context**: The DualPrompt baseline has trained and evaluated on the CIFAR-100 dataset

### R136: The incremental accuracy of the DualPrompt baseline during t...
- **Rubric ID**: 1270002b-256d-499a-99cb-b9454c189464
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the DualPrompt baseline during training on the CIFAR-100 dataset has been computed using the test split at the end of each task
- **Parent context**: The DualPrompt baseline has trained and evaluated on the CIFAR-100 dataset

### R137: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: e0841bd6-3ee5-414c-b579-34058dc7a476
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the DualPrompt baseline during training on the ImageNet-R dataset has been computed using the test split
- **Parent context**: The DualPrompt baseline has been trained and evaluated on the ImageNet-R dataset

### R138: The incremental accuracy of the DualPrompt baseline during t...
- **Rubric ID**: 747afc17-942d-42be-98c5-d1e1649616b2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the DualPrompt baseline during training on the ImageNet-R dataset has been computed using the test split at the end of each task
- **Parent context**: The DualPrompt baseline has been trained and evaluated on the ImageNet-R dataset

### R139: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 3439a080-4f7d-4e17-a733-c854a52a83ce
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the DualPrompt baseline during training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The DualPrompt baseline has been trained and evaluated on the ImageNet-A dataset

### R140: The incremental accuracy of the DualPrompt baseline during t...
- **Rubric ID**: 89e2d79e-c189-442d-91db-a3999c7a8bba
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the DualPrompt baseline during training on the ImageNet-A dataset has been computed using the test split at the end of each task
- **Parent context**: The DualPrompt baseline has been trained and evaluated on the ImageNet-A dataset

### R141: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 6e295ddf-4558-4ae5-b6be-6904251bf465
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the DualPrompt baseline during training on the VTAB dataset has been computed using the test split
- **Parent context**: The DualPrompt baseline has been trained and evaluated on the VTAB dataset

### R142: The incremental accuracy of the DualPrompt baseline during t...
- **Rubric ID**: f974b5e9-f577-48a9-b9d0-e2cfb54599a8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the DualPrompt baseline during training on the VTAB dataset has been computed using the test split at the end of each task
- **Parent context**: The DualPrompt baseline has been trained and evaluated on the VTAB dataset

### R143: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: b73b37e9-1921-4595-97dd-9590e3ece961
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the CODA-P baseline during training on the CIFAR-100 dataset has been computed using the test split
- **Parent context**: The CODA-P baseline has trained and evaluated on the CIFAR-100 dataset

### R144: The incremental accuracy of the CODA-P baseline during train...
- **Rubric ID**: a147e3f0-ff9d-4324-b9d0-0d9a40618009
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the CODA-P baseline during training on the CIFAR-100 dataset has been computed using the test split at the end of each task
- **Parent context**: The CODA-P baseline has trained and evaluated on the CIFAR-100 dataset

### R145: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 17908706-adca-40cb-9cf4-51c11074bd1f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the CODA-P baseline during training on the ImageNet-R dataset has been computed using the test split
- **Parent context**: The CODA-P baseline has been trained and evaluated on the ImageNet-R dataset

### R146: The incremental accuracy of the CODA-P baseline during train...
- **Rubric ID**: 718ec9cb-442c-49c8-b6a8-3f34e47f0dd2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the CODA-P baseline during training on the ImageNet-R dataset has been computed using the test split at the end of each task
- **Parent context**: The CODA-P baseline has been trained and evaluated on the ImageNet-R dataset

### R147: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 0bfe5cc5-7115-4e94-b482-241889d50492
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the CODA-P baseline during training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The CODA-P baseline has been trained and evaluated on the ImageNet-A dataset

### R148: The incremental accuracy of the CODA-P baseline during train...
- **Rubric ID**: bbdbde01-55a1-454d-9b57-5478321d8d30
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the CODA-P baseline during training on the ImageNet-A dataset has been computed using the test split at the end of each task
- **Parent context**: The CODA-P baseline has been trained and evaluated on the ImageNet-A dataset

### R149: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 58163fe2-db78-42ce-b8c7-e93651cdb134
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the CODA-P baseline during training on the VTAB dataset has been computed using the test split
- **Parent context**: The CODA-P baseline has been trained and evaluated on the VTAB dataset

### R150: The incremental accuracy of the CODA-P baseline during train...
- **Rubric ID**: c3441c0e-60ee-45cd-adfe-6b048adfdb01
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the CODA-P baseline during training on the VTAB dataset has been computed using the test split at the end of each task
- **Parent context**: The CODA-P baseline has been trained and evaluated on the VTAB dataset

### R151: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 97fb02ce-a6e6-4458-8617-bfab65687edc
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the SimpleCIL baseline during training on the CIFAR-100 dataset has been computed using the test split
- **Parent context**: The SimpleCIL baseline has trained and evaluated on the CIFAR-100 dataset

### R152: The incremental accuracy of the SimpleCIL baseline during tr...
- **Rubric ID**: 09aae679-d912-43ee-a696-f04f051a6c1d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the SimpleCIL baseline during training on the CIFAR-100 dataset has been computed using the test split at the end of each task
- **Parent context**: The SimpleCIL baseline has trained and evaluated on the CIFAR-100 dataset

### R153: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: d6978e68-39f9-4f32-a3c8-3e2431a10055
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the SimpleCIL baseline during training on the ImageNet-R dataset has been computed using the test split
- **Parent context**: The SimpleCIL baseline has been trained and evaluated on the ImageNet-R dataset

### R154: The incremental accuracy of the SimpleCIL baseline during tr...
- **Rubric ID**: e2244dfc-e8ce-49fa-81e6-fef56a5d7c58
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the SimpleCIL baseline during training on the ImageNet-R dataset has been computed using the test split at the end of each task
- **Parent context**: The SimpleCIL baseline has been trained and evaluated on the ImageNet-R dataset

### R155: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: f35c04f0-4510-49b6-ae19-998eaf5ed29c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the SimpleCIL baseline during training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The SimpleCIL baseline has been trained and evaluated on the ImageNet-A dataset

### R156: The incremental accuracy of the SimpleCIL baseline during tr...
- **Rubric ID**: 7b195482-9298-4854-8fe3-73573180b92e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the SimpleCIL baseline during training on the ImageNet-A dataset has been computed using the test split at the end of each task
- **Parent context**: The SimpleCIL baseline has been trained and evaluated on the ImageNet-A dataset

### R157: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: d97eb786-4620-4370-99b1-84b99d736c1a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the SimpleCIL baseline during training on the VTAB dataset has been computed using the test split
- **Parent context**: The SimpleCIL baseline has been trained and evaluated on the VTAB dataset

### R158: The incremental accuracy of the SimpleCIL baseline during tr...
- **Rubric ID**: eee2b9ed-1dd7-440f-9069-a33f02801532
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the SimpleCIL baseline during training on the VTAB dataset has been computed using the test split at the end of each task
- **Parent context**: The SimpleCIL baseline has been trained and evaluated on the VTAB dataset

### R159: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 7143f82b-35c2-48c2-a409-43113afb7777
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the ADAM baseline during training on the CIFAR-100 dataset has been computed using the test split
- **Parent context**: The ADAM baseline has trained and evaluated on the CIFAR-100 dataset

### R160: The incremental accuracy of the ADAM baseline during trainin...
- **Rubric ID**: fdbca1a2-e9a8-4344-9101-7045c9242517
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the ADAM baseline during training on the CIFAR-100 dataset has been computed using the test split at the end of each task
- **Parent context**: The ADAM baseline has trained and evaluated on the CIFAR-100 dataset

### R161: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: f0a875ba-e83b-4e55-942c-4b5162ad6055
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the ADAM baseline during training on the ImageNet-R dataset has been computed using the test split
- **Parent context**: The ADAM baseline has been trained and evaluated on the ImageNet-R dataset

### R162: The incremental accuracy of the ADAM baseline during trainin...
- **Rubric ID**: e4e36305-652d-445f-af74-77deb7ad5b83
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the ADAM baseline during training on the ImageNet-R dataset has been computed using the test split at the end of each task
- **Parent context**: The ADAM baseline has been trained and evaluated on the ImageNet-R dataset

### R163: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 622aacbb-bbc7-4222-b2ce-a6786fc9201f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the ADAM baseline during training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The ADAM baseline has been trained and evaluated on the ImageNet-A dataset

### R164: The incremental accuracy of the ADAM baseline during trainin...
- **Rubric ID**: 53e5b34f-b7b7-44ef-bfbb-0ea7250a6b82
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the ADAM baseline during training on the ImageNet-A dataset has been computed using the test split at the end of each task
- **Parent context**: The ADAM baseline has been trained and evaluated on the ImageNet-A dataset

### R165: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 136f8a5c-6fa9-4308-8c56-c5c5e8779fa3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of the ADAM baseline during training on the VTAB dataset has been computed using the test split
- **Parent context**: The ADAM baseline has been trained and evaluated on the VTAB dataset

### R166: The incremental accuracy of the ADAM baseline during trainin...
- **Rubric ID**: a02c8f1a-d10e-4d7f-a951-9103bb43f75a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of the ADAM baseline during training on the VTAB dataset has been computed using the test split at the end of each task
- **Parent context**: The ADAM baseline has been trained and evaluated on the VTAB dataset

### R167: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: dc6a493b-e6bf-4128-a9ed-873356a99669
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of SEMA during training on the CIFAR-100 dataset has been computed using the test split
- **Parent context**: SEMA has trained and evaluated on the CIFAR-100 dataset

### R168: The incremental accuracy of SEMA during training on the CIFA...
- **Rubric ID**: cdc7db5a-0ee4-486a-b646-a37e9f3c5cc4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of SEMA during training on the CIFAR-100 dataset has been computed using the test split at the end of each task
- **Parent context**: SEMA has trained and evaluated on the CIFAR-100 dataset

### R169: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 13629fa4-e6ad-41ca-bd64-8628db83706a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of SEMA during training on the ImageNet-R dataset has been computed using the test split
- **Parent context**: SEMA has been trained and evaluated on the ImageNet-R dataset

### R170: The incremental accuracy of SEMA during training on the Imag...
- **Rubric ID**: 6d2442b9-4c78-4c63-ab0e-604abbfbd4cf
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of SEMA during training on the ImageNet-R dataset has been computed using the test split at the end of each task
- **Parent context**: SEMA has been trained and evaluated on the ImageNet-R dataset

### R171: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 8f54e2fe-1a5e-4306-8d09-0a19f71f25ce
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of SEMA during training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: SEMA has been trained and evaluated on the ImageNet-A dataset

### R172: The incremental accuracy of SEMA during training on the Imag...
- **Rubric ID**: ace39db2-a349-4196-a76f-94d4d0240ad4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of SEMA during training on the ImageNet-A dataset has been computed using the test split at the end of each task
- **Parent context**: SEMA has been trained and evaluated on the ImageNet-A dataset

### R173: The average accuracy (of all seen tasks after training on al...
- **Rubric ID**: 40ac1b84-a97c-4674-8e65-084f83bed434
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average accuracy (of all seen tasks after training on all tasks) of SEMA during training on the VTAB dataset has been computed using the test split
- **Parent context**: SEMA has been trained and evaluated on the VTAB dataset

### R174: The incremental accuracy of SEMA during training on the VTAB...
- **Rubric ID**: bb23038c-38fc-4c86-8ad2-e29aaad62285
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The incremental accuracy of SEMA during training on the VTAB dataset has been computed using the test split at the end of each task
- **Parent context**: SEMA has been trained and evaluated on the VTAB dataset

### R175: The recorded metrics show that the average accuracy of SEMA...
- **Rubric ID**: fd1aa6e8-bf99-4cfa-a437-b866cd7baf77
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the average accuracy of SEMA is almost always higher than that of the other methods for all the datasets.
- **Parent context**: The recorded metrics show that the results from Section 4.2 have been replicated

### R176: The recorded metrics show that the average incremental accur...
- **Rubric ID**: 5392a57b-f0a3-4e29-b0d1-14c6daa85946
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the average incremental accuracy of SEMA at the end of training is almost always higher than that of the other methods for all the datasets.
- **Parent context**: The recorded metrics show that the results from Section 4.2 have been replicated

### R177: The recorded metrics show that the average incremental accur...
- **Rubric ID**: f88415b6-2fea-48f9-a543-2af0f15b1825
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the average incremental accuracy of SEMA throughout training is almost always higher than that of the other methods, when comparing to methods trained on the same dataset for the same number of tasks
- **Parent context**: The recorded metrics show that the results from Section 4.2 have been replicated

### R178: Using the architecture variant "No Expansion" introduced in...
- **Rubric ID**: 960373b2-6408-411f-87f0-a02c35013f1a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the average accuracy (of all seen tasks after training on all tasks) during training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module exp...

### R179: Using the architecture variant "No Expansion" introduced in...
- **Rubric ID**: d99b7241-4ba8-4f60-ab2c-70ff85127c8f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the incremental accuracy at the end of training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module exp...

### R180: Using the architecture variant "No Expansion" introduced in...
- **Rubric ID**: 8f05eab2-286f-44a8-ac9e-968219c2b35e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the average accuracy (of all seen tasks after training on all tasks) during training on the VTAB dataset has been computed using the test split
- **Parent context**: The architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module exp...

### R181: Using the architecture variant "No Expansion" introduced in...
- **Rubric ID**: 4b4a6027-0b38-4e56-a391-f9097d3300f4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the incremental accuracy at the end of training on the VTAB dataset has been computed using the test split
- **Parent context**: The architecture variant "No Expansion" introduced in Section 4.3 on "Ablation studies on module exp...

### R182: Using the architecture variant "Average Weighting" introduce...
- **Rubric ID**: f7de59e1-a4c2-4986-bc01-706fb0238a50
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Average Weighting" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the average accuracy (of all seen tasks after training on all tasks) during training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The architecture variant "Average Weighting" introduced in Section 4.3 on "Ablation studies on modul...

### R183: Using the architecture variant "Average Weighting" introduce...
- **Rubric ID**: 0a7c2994-584f-40a9-8d1b-1fd207ed2130
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Average Weighting" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the incremental accuracy at the end of training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The architecture variant "Average Weighting" introduced in Section 4.3 on "Ablation studies on modul...

### R184: Using the architecture variant "Average Weighting" introduce...
- **Rubric ID**: 50cb9235-3350-4290-9814-827121ddcd05
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Average Weighting" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the average accuracy (of all seen tasks after training on all tasks) during training on the VTAB dataset has been computed using the test split
- **Parent context**: The architecture variant "Average Weighting" introduced in Section 4.3 on "Ablation studies on modul...

### R185: Using the architecture variant "Average Weighting" introduce...
- **Rubric ID**: 2c12a5aa-da6e-4cb7-b318-45b458779b6f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Average Weighting" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the incremental accuracy at the end of training on the VTAB dataset has been computed using the test split
- **Parent context**: The architecture variant "Average Weighting" introduced in Section 4.3 on "Ablation studies on modul...

### R186: Using the architecture variant "Random Weighting" introduced...
- **Rubric ID**: 06d94970-28e2-460f-a0ca-5bcfdca8b90a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Random Weighting" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the average accuracy (of all seen tasks after training on all tasks) during training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The architecture variant "Random Weighting" introduced in Section 4.3 on "Ablation studies on module...

### R187: Using the architecture variant "Random Weighting" introduced...
- **Rubric ID**: dc6f4c73-f3d1-4540-b488-a054a45572e6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Random Weighting" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the incremental accuracy at the end of training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The architecture variant "Random Weighting" introduced in Section 4.3 on "Ablation studies on module...

### R188: Using the architecture variant "Random Weighting" introduced...
- **Rubric ID**: 5bb576a8-6c47-4e4d-b805-82a3a9c483bb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Random Weighting" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the average accuracy (of all seen tasks after training on all tasks) during training on the VTAB dataset has been computed using the test split
- **Parent context**: The architecture variant "Random Weighting" introduced in Section 4.3 on "Ablation studies on module...

### R189: Using the architecture variant "Random Weighting" introduced...
- **Rubric ID**: a094edbc-e7ea-4538-b134-aab5a40509b9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Random Weighting" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the incremental accuracy at the end of training on the VTAB dataset has been computed using the test split
- **Parent context**: The architecture variant "Random Weighting" introduced in Section 4.3 on "Ablation studies on module...

### R190: Using the architecture variant "Top-1 Selection" introduced...
- **Rubric ID**: 330f557e-3fc8-4432-8a61-7cb1f976b106
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Top-1 Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the average accuracy (of all seen tasks after training on all tasks) during training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The architecture variant "Top-1 Selection" introduced in Section 4.3 on "Ablation studies on module ...

### R191: Using the architecture variant "Top-1 Selection" introduced...
- **Rubric ID**: ce346361-4a21-4b98-bcc4-8185ed0823cf
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Top-1 Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the incremental accuracy at the end of training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The architecture variant "Top-1 Selection" introduced in Section 4.3 on "Ablation studies on module ...

### R192: Using the architecture variant "Top-1 Selection" introduced...
- **Rubric ID**: 8d8efa6c-edb7-4ca2-a336-1dc093acdb95
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Top-1 Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the average accuracy (of all seen tasks after training on all tasks) during training on the VTAB dataset has been computed using the test split
- **Parent context**: The architecture variant "Top-1 Selection" introduced in Section 4.3 on "Ablation studies on module ...

### R193: Using the architecture variant "Top-1 Selection" introduced...
- **Rubric ID**: f793a9ba-c47c-4601-9227-f0be2b853edd
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Top-1 Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the incremental accuracy at the end of training on the VTAB dataset has been computed using the test split
- **Parent context**: The architecture variant "Top-1 Selection" introduced in Section 4.3 on "Ablation studies on module ...

### R194: Using the architecture variant "Random Selection" introduced...
- **Rubric ID**: 97d148e1-8400-4d27-ad52-6b033bbbdbfc
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Random Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the average accuracy (of all seen tasks after training on all tasks) during training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The architecture variant "Random Selection" introduced in Section 4.3 on "Ablation studies on module...

### R195: Using the architecture variant "Random Selection" introduced...
- **Rubric ID**: 1a82263f-f9c4-40ec-a8b9-fb9a897a4bae
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Random Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the incremental accuracy at the end of training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The architecture variant "Random Selection" introduced in Section 4.3 on "Ablation studies on module...

### R196: Using the architecture variant "Random Selection" introduced...
- **Rubric ID**: 51534b80-118e-47ec-b3c6-d5721cec9843
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Random Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the average accuracy (of all seen tasks after training on all tasks) during training on the VTAB dataset has been computed using the test split
- **Parent context**: The architecture variant "Random Selection" introduced in Section 4.3 on "Ablation studies on module...

### R197: Using the architecture variant "Random Selection" introduced...
- **Rubric ID**: f0a4782b-8349-4262-b04a-ff7e7bd3c74d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Random Selection" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the incremental accuracy at the end of training on the VTAB dataset has been computed using the test split
- **Parent context**: The architecture variant "Random Selection" introduced in Section 4.3 on "Ablation studies on module...

### R198: Using the architecture variant "Top-1 Selection Inference" i...
- **Rubric ID**: ef83772a-6c9d-4545-96b3-dfea96d51c36
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Top-1 Selection Inference" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the average accuracy (of all seen tasks after training on all tasks) during training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The architecture variant "Top-1 Selection Inference" introduced in Section 4.3 on "Ablation studies ...

### R199: Using the architecture variant "Top-1 Selection Inference" i...
- **Rubric ID**: bd448bde-180e-47ec-a30c-3d1eb36d7270
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Top-1 Selection Inference" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the incremental accuracy at the end of training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: The architecture variant "Top-1 Selection Inference" introduced in Section 4.3 on "Ablation studies ...

### R200: Using the architecture variant "Top-1 Selection Inference" i...
- **Rubric ID**: 4aa24932-fc7c-4bf1-bd34-8185da64d837
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Top-1 Selection Inference" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the average accuracy (of all seen tasks after training on all tasks) during training on the VTAB dataset has been computed using the test split
- **Parent context**: The architecture variant "Top-1 Selection Inference" introduced in Section 4.3 on "Ablation studies ...

### R201: Using the architecture variant "Top-1 Selection Inference" i...
- **Rubric ID**: 7bd04838-b39a-451b-9c8b-c9f243b9699c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the architecture variant "Top-1 Selection Inference" introduced in Section 4.3 on "Ablation studies on module expansion and adapter composing", the incremental accuracy at the end of training on the VTAB dataset has been computed using the test split
- **Parent context**: The architecture variant "Top-1 Selection Inference" introduced in Section 4.3 on "Ablation studies ...

### R202: The recorded metrics show that SEMA achieves about equal or...
- **Rubric ID**: 4d764fd4-0c3c-4284-98aa-7774ce363af7
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that SEMA achieves about equal or higher performance wrt. incremental accuracy and average accuracy on both the ImageNet-A and VTAB datasets
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Ablation studies on module expansion a...

### R203: The recorded metrics show that the Top-1 Selection Inference...
- **Rubric ID**: 32f0f139-2d20-48f0-b58f-f540ef3c7c27
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the Top-1 Selection Inference variant achieves about equal or higher performance wrt. incremental accuracy and average accuracy on both the ImageNet-A and VTAB datasets compared to all other variants (but not compared to SEMA)
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Ablation studies on module expansion a...

### R204: For the SEMA model trained in Section 4.3 on "Analysis on dy...
- **Rubric ID**: 8e458cfa-d612-4672-99e3-c8996d3d0882
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the SEMA model trained in Section 4.3 on "Analysis on dynamic expansion process", the reconstruction error from each representation descriptor is recorded for each batch
- **Parent context**: The experiments required to replicate the results in Section 4.3 on "Analysis on dynamic expansion p...

### R205: The recorded metrics show that, during training, each repres...
- **Rubric ID**: 22377755-0ce5-4de4-bda0-cbc476c6a4ee
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, during training, each representation descriptor's reconstruction loss lowers over the course of training, and eventually oscillates around some value
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Analysis on dynamic expansion process"...

### R206: The recorded metrics show that, during the detection phase a...
- **Rubric ID**: 4c514efc-422d-4f91-b5d0-0d1c6767a281
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, during the detection phase at the start of each task, the reconstruction loss increases for each present representation descriptor that was introduced in the previous task
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Analysis on dynamic expansion process"...

### R207: The recorded metrics show that in total three representation...
- **Rubric ID**: afdd1870-f248-48c6-8da0-80ee80c2a249
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that in total three representation descriptors are present in the final model after training
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Analysis on dynamic expansion process"...

### R208: Using the model trained in Section 4.3 on "Analysis on dynam...
- **Rubric ID**: 8e1377c2-0b2f-4aa8-b3f9-476e7f7a8b09
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the model trained in Section 4.3 on "Analysis on dynamic expansion process", the adapter usage for each task has been computed by averaging the routing weight vectors from all samples seen in tasks in the test set, then normalizing the final result such that the sum of average weights for each task sums to one
- **Parent context**: The results in Section 4.3 on "Analysis on adapter usage" have been replicated

### R209: The recorded metrics show that, the first adapter has a larg...
- **Rubric ID**: 4e89af61-b259-4c12-a179-26a3651a8f50
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, the first adapter has a large usage for the first task, the second adapter has a large usage for the second task, and the third adapter has a large usage for the third task
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Analysis on adapter usage" have been r...

### R210: The recorded metrics show that, the fourth task uses the fir...
- **Rubric ID**: 3dc20642-dc33-4467-b5bf-f1b9a528cbdd
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, the fourth task uses the first adapter; the first adapter has the largest usage for the fourth task
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Analysis on adapter usage" have been r...

### R211: The recorded metrics show that, the fifth task uses the thir...
- **Rubric ID**: 88dcf9d6-bd8b-4427-b00f-fdcd087fa3c9
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, the fifth task uses the third adapter; the thirs adapter has the largest usage for the fifth task
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Analysis on adapter usage" have been r...

### R212: For each SEMA model trained with a different expansion thres...
- **Rubric ID**: 9254bba9-cd1d-4d1b-a51a-1e5585a0b9ba
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each SEMA model trained with a different expansion threshold, the average accuracy at the end of training on the ImageNet-A dataset has been computed using the test split at the end of each task
- **Parent context**: SEMA is separately trained with expansion thresholds 1.0, 1.1, 1.2, ...., 2.0 on ImageNet-A. For eac...

### R213: For each SEMA model trained with a different expansion thres...
- **Rubric ID**: 2d255c7d-aca3-4032-93e5-87606f0a272e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each SEMA model trained with a different expansion threshold on ImageNet-A, the number of adapters at the end of training in each of the last three layers is computed
- **Parent context**: SEMA is separately trained with expansion thresholds 1.0, 1.1, 1.2, ...., 2.0 on ImageNet-A. For eac...

### R214: For each SEMA model trained with a different expansion thres...
- **Rubric ID**: 9e2e9c35-5b31-4c23-ada6-25cadcb089b3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each SEMA model trained with a different expansion threshold, the average accuracy at the end of training on the VTAB dataset has been computed using the test split at the end of each task
- **Parent context**: SEMA is separately trained with expansion thresholds 1.0, 2.0, 3.0, ...., 8.0 on VTAB. For each trai...

### R215: For each SEMA model trained with a different expansion thres...
- **Rubric ID**: db0f6083-9914-49e6-91d8-5d7552307fa8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each SEMA model trained with a different expansion threshold on VTAB, the number of adapters at the end of training in each of the last three layers is computed
- **Parent context**: SEMA is separately trained with expansion thresholds 1.0, 2.0, 3.0, ...., 8.0 on VTAB. For each trai...

### R216: The recorded metrics show that the average accuracy of the S...
- **Rubric ID**: cac935d6-0663-4748-92e0-6f91b32e6a35
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the average accuracy of the SEMA models trained on ImageNet-A does not significantly vary over expansion thresholds 1.0, 1.1, 1.2, ...., 2.0
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Study of expansion threshold" have bee...

### R217: The recorded metrics show that the incremental accuracy of t...
- **Rubric ID**: b1205f44-85ca-4494-a143-eb9e5a362521
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the incremental accuracy of the SEMA models trained on ImageNet-A does not significantly vary over expansion thresholds 1.0, 1.1, 1.2, ...., 2.0
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Study of expansion threshold" have bee...

### R218: The recorded metrics show that the SEMA models trained on Im...
- **Rubric ID**: a50983cd-2b51-4f3d-8b7a-934ebf53813b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the SEMA models trained on ImageNet-A have more adapters when trained with lower expansion thresholds then when they are trained with higher expansion thresholds
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Study of expansion threshold" have bee...

### R219: The recorded metrics show that the average accuracy of the S...
- **Rubric ID**: a302cd1d-26d1-498c-a96f-3691052e040c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the average accuracy of the SEMA models trained on VTAB is higher with low expansion thresholds (1.0, 2.0) than high expansion thresholds (7.0, 8.0)
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Study of expansion threshold" have bee...

### R220: The recorded metrics show that the incremental accuracy of t...
- **Rubric ID**: e9857488-805e-4c0b-b6ee-445ae79380cf
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the incremental accuracy of the SEMA models trained on VTAB is higher with low expansion thresholds (1.0, 2.0) than high expansion thresholds (7.0, 8.0)
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Study of expansion threshold" have bee...

### R221: The recorded metrics show that the SEMA models trained on VT...
- **Rubric ID**: d91d9aa5-72fd-4d78-b923-df6bc4510d7e
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the SEMA models trained on VTAB have more adapters when trained with lower expansion thresholds then when they are trained with higher expansion thresholds
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Study of expansion threshold" have bee...

### R222: For each SEMA variant trained on ImageNet-A allowing differe...
- **Rubric ID**: 7960f0dc-ff3d-483c-ac44-74865510d7fb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each SEMA variant trained on ImageNet-A allowing different layers for self-expansion, the average accuracy at the end of training has been computed using the test split at the end of each task
- **Parent context**: Different SEMA models are trained on ImageNet-A with varying number of layers that are allowed for s...

### R223: For each SEMA variant trained on ImageNet-A allowing differe...
- **Rubric ID**: e92d099c-b0d7-414b-b92f-e6bff6d7e6e0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each SEMA variant trained on ImageNet-A allowing different layers for self-expansion, the total number of added adapters at the end of training is computed
- **Parent context**: Different SEMA models are trained on ImageNet-A with varying number of layers that are allowed for s...

### R224: For each SEMA variant trained on VTAB allowing different lay...
- **Rubric ID**: 18fa0271-4d56-4a56-80ab-52ca2aa24beb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each SEMA variant trained on VTAB allowing different layers for self-expansion, the average accuracy at the end of training has been computed using the test split at the end of each task
- **Parent context**: Different SEMA models are trained on VTAB with varying number of layers that are allowed for self-ex...

### R225: The recorded metrics show that the average accuracy of SEMA...
- **Rubric ID**: 14696e47-fa4c-4f3f-9557-2e22ba3825f1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the average accuracy of SEMA trained on ImageNet-A is higher when layers 9-12 are allowed for self-expansion compared to when only layers 11-12 are allowed for self-expansion
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Analysis of multi-layer expansion" hav...

### R226: The recorded metrics show that the average accuracy of SEMA...
- **Rubric ID**: bf0ca018-644d-41a7-b0a1-8d1d54690e51
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the average accuracy of SEMA trained on VTAB is higher when layers 9-12 are allowed for self-expansion compared to when only layers 11-12 are allowed for self-expansion
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Analysis of multi-layer expansion" hav...

### R227: The recorded metrics show that the incremental accuracy of I...
- **Rubric ID**: 30593624-21a7-44b0-ac75-8635e4d418e3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the incremental accuracy of ImageNet-A trained on VTAB is higher when layers 9-12 are allowed for self-expansion compared to when only layers 11-12 are allowed for self-expansion
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Analysis of multi-layer expansion" hav...

### R228: The recorded metrics show that the incremental accuracy of S...
- **Rubric ID**: 8de7c979-b748-487b-920d-ddf4ce21fa99
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the incremental accuracy of SEMA trained on VTAB is higher when layers 10-12 are allowed for self-expansion compared to when only layers 11-12 are allowed for self-expansion
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Analysis of multi-layer expansion" hav...

### R229: The recorded metrics show that for the SEMA model trained on...
- **Rubric ID**: 2048f2e3-9d3a-4608-bf4f-2f58b41284de
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that for the SEMA model trained on ImageNet-A, more adapters are added in total when more layers are allowed for self-expansion
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Analysis of multi-layer expansion" hav...

### R230: Using a variant of the SEMA architecture that uses the "Adap...
- **Rubric ID**: aa20dc32-9478-4b25-a65a-1aa9757040a4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using a variant of the SEMA architecture that uses the "Adapter" adapter, the average accuracy (of all seen tasks after training on all tasks) at the end of training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: A variant of the SEMA architecture using the "Adapter" adapter from the baseline has been trained on...

### R231: Using a variant of the SEMA architecture that uses the "Adap...
- **Rubric ID**: 9ae9841e-3a43-484a-9766-567c4bf99cba
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using a variant of the SEMA architecture that uses the "Adapter" adapter, the incremental accuracy at the end of training on the ImageNet-A dataset has been computed
- **Parent context**: A variant of the SEMA architecture using the "Adapter" adapter from the baseline has been trained on...

### R232: Using a variant of the SEMA architecture that uses the "Adap...
- **Rubric ID**: 8a3631d4-e7ab-42c8-8e41-2452c4c3870c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using a variant of the SEMA architecture that uses the "Adapter" adapter, the average accuracy (of all seen tasks after training on all tasks) at the end of training on the VTAB dataset has been computed using the test split
- **Parent context**: A variant of the SEMA architecture using the "Adapter" adapter from the baseline has been trained on...

### R233: Using a variant of the SEMA architecture that uses the "Adap...
- **Rubric ID**: 539d5540-287f-45f8-b033-9687094d9710
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using a variant of the SEMA architecture that uses the "Adapter" adapter, the incremental accuracy at the end of training on the VTAB dataset has been computed
- **Parent context**: A variant of the SEMA architecture using the "Adapter" adapter from the baseline has been trained on...

### R234: Using a variant of the SEMA architecture that uses the LoRA...
- **Rubric ID**: 7f08f53d-e894-48a1-9907-273fc4d7e1cd
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using a variant of the SEMA architecture that uses the LoRA adapter, the average accuracy (of all seen tasks after training on all tasks) at the end of training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: A variant of the SEMA architecture using the LoRA adapter has been trained on ImageNet-A, and the av...

### R235: Using a variant of the SEMA architecture that uses the LoRA...
- **Rubric ID**: fac6eece-4f0c-4288-b874-13a9f4b12b0b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using a variant of the SEMA architecture that uses the LoRA adapter, the incremental accuracy at the end of training on the ImageNet-A dataset has been computed
- **Parent context**: A variant of the SEMA architecture using the LoRA adapter has been trained on ImageNet-A, and the av...

### R236: Using a variant of the SEMA architecture that uses the LoRA...
- **Rubric ID**: 412c97f9-1cb1-4a81-b088-39cc2f82af40
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using a variant of the SEMA architecture that uses the LoRA adapter, the average accuracy (of all seen tasks after training on all tasks) at the end of training on the VTAB dataset has been computed using the test split
- **Parent context**: A variant of the SEMA architecture using the LoRA adapter has been trained on VTAB, and the average ...

### R237: Using a variant of the SEMA architecture that uses the LoRA...
- **Rubric ID**: 4926a287-b5c6-4d38-9a72-61376eb43dc5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using a variant of the SEMA architecture that uses the LoRA adapter, the incremental accuracy at the end of training on the VTAB dataset has been computed
- **Parent context**: A variant of the SEMA architecture using the LoRA adapter has been trained on VTAB, and the average ...

### R238: Using a variant of the SEMA architecture that uses the Convp...
- **Rubric ID**: fa28b20d-541a-45e9-9887-864ecf30124c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using a variant of the SEMA architecture that uses the Convpass adapter, the average accuracy (of all seen tasks after training on all tasks) at the end of training on the ImageNet-A dataset has been computed using the test split
- **Parent context**: A variant of the SEMA architecture using the Convpass adapter has been trained on ImageNet-A, and th...

### R239: Using a variant of the SEMA architecture that uses the Convp...
- **Rubric ID**: dc29184c-4604-47d6-b67f-442e2b0d0e37
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using a variant of the SEMA architecture that uses the Convpass adapter, the incremental accuracy at the end of training on the ImageNet-A dataset has been computed
- **Parent context**: A variant of the SEMA architecture using the Convpass adapter has been trained on ImageNet-A, and th...

### R240: Using a variant of the SEMA architecture that uses the Convp...
- **Rubric ID**: 6a6a58c7-0ec1-447f-a847-721f9c0268ed
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using a variant of the SEMA architecture that uses the Convpass adapter, the average accuracy (of all seen tasks after training on all tasks) at the end of training on the VTAB dataset has been computed using the test split
- **Parent context**: A variant of the SEMA architecture using the Convpass adapter has been trained on VTAB, and the aver...

### R241: Using a variant of the SEMA architecture that uses the Convp...
- **Rubric ID**: 3609cd4d-1702-47b2-8271-916014e48336
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using a variant of the SEMA architecture that uses the Convpass adapter, the incremental accuracy at the end of training on the VTAB dataset has been computed
- **Parent context**: A variant of the SEMA architecture using the Convpass adapter has been trained on VTAB, and the aver...

### R242: The recorded metrics show that for each dataset (ImageNet-A,...
- **Rubric ID**: 6329ed8e-e09f-4736-910e-b8a71402fde8
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that for each dataset (ImageNet-A, VTAB) all models trained on such dataset have similar average accuracies and incremental accuracies (<4%)
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Ablation studies on adapter variants" ...

### R243: The recorded metrics show that all models trained on the Ima...
- **Rubric ID**: 4a7122fc-b365-4bc7-ad97-346be8b23f78
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that all models trained on the ImageNet-A dataset achieve an average accuracy >50% and an incremental accuracy >60%
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Ablation studies on adapter variants" ...

### R244: The recorded metrics show that all models trained on the VTA...
- **Rubric ID**: 5ca4eec8-4f2d-495a-9565-669aa37b0483
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that all models trained on the VTAB dataset achieve an average accuracy >85% and an incremental accuracy >88%
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Ablation studies on adapter variants" ...

### R245: Code for computing the total number of parameters added by e...
- **Rubric ID**: 918b9273-aafb-4c0d-a7fe-da67f85de064
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code for computing the total number of parameters added by each method is implemented
- **Parent context**: The results in Section 4.3 on "Sub-linear growth of parameters" have been replicated

### R246: The total number of parameters added by each method is compu...
- **Rubric ID**: da88bff7-d60f-47ea-a705-f21d74d9fba8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The total number of parameters added by each method is computed over the course of training at the end of each task
- **Parent context**: The results in Section 4.3 on "Sub-linear growth of parameters" have been replicated

### R247: Methods CODA-P and DualPrompt exhibit linear growth in numbe...
- **Rubric ID**: 7c95cb96-0d92-4f49-b252-df415e6c3d13
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Methods CODA-P and DualPrompt exhibit linear growth in number of added parameters over the course of training
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Sub-linear growth of parameters" have ...

### R248: A sublinear growth in the number of added parameters is obse...
- **Rubric ID**: 1457caf5-6f03-4b8b-afec-743465692762
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A sublinear growth in the number of added parameters is observed for SEMA over the course of training
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Sub-linear growth of parameters" have ...

### R249: The number of parameters added by L2P remains at zero over t...
- **Rubric ID**: 88a3e48c-5e3e-42a7-a03b-c69c6043c725
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The number of parameters added by L2P remains at zero over the course of training
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Sub-linear growth of parameters" have ...

## Logging, Analysis & Presentation

### R250: The recorded metrics show that no representation descriptors...
- **Rubric ID**: 041c37ec-dec0-46a8-9641-b88963ccda3f
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The recorded metrics show that no representation descriptors were added during the final two tasks
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Analysis on dynamic expansion process"...

### R251: Code is implemented to count the number of adapters added to...
- **Rubric ID**: e416a999-41de-489d-9df7-54edfd80b866
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code is implemented to count the number of adapters added to each of the last three transformer layers
- **Parent context**: The experiments required to replicate the results in Section 4.3 on "Study of expansion threshold" h...

### R252: For each SEMA variant trained on VTAB allowing different lay...
- **Rubric ID**: 5f4eb916-549e-45cf-be21-9ad2a6a33ae9
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: For each SEMA variant trained on VTAB allowing different layers for self-expansion, the total number of added adapters at the end of training is computed
- **Parent context**: Different SEMA models are trained on VTAB with varying number of layers that are allowed for self-ex...

### R253: The recorded metrics show that for the SEMA model trained on...
- **Rubric ID**: b74040f4-5aaa-432d-b18a-ea365cbb06b4
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The recorded metrics show that for the SEMA model trained on VTAB, more adapters are added in total when more layers are allowed for self-expansion
- **Parent context**: The recorded metrics show that the results in Section 4.3 on "Analysis of multi-layer expansion" hav...
