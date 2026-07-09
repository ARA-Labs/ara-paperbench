# Rubric Requirements — sample-specific-masks
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 331

## Dataset and Model Acquisition

### R01: Code for making ResNet-18, pre-trained on ImageNet-1K, avail...
- **Rubric ID**: 3982c682-eeb3-4298-8ecc-894dee051bdc
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for making ResNet-18, pre-trained on ImageNet-1K, available for further training and evaluation has been implemented
- **Parent context**: Code for making the required models available for further training and evaluation has been implement...

### R02: Code for making ResNet-50, pre-trained on ImageNet-1K, avail...
- **Rubric ID**: 57d7b55b-a190-4f96-9468-4446a8343575
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for making ResNet-50, pre-trained on ImageNet-1K, available for further training and evaluation has been implemented
- **Parent context**: Code for making the required models available for further training and evaluation has been implement...

### R03: Code for making ViT-B32, pre-trained on ImageNet-1K, availab...
- **Rubric ID**: 6c6b1ad5-64e9-4985-be0b-97841918c297
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for making ViT-B32, pre-trained on ImageNet-1K, available for further training and evaluation has been implemented
- **Parent context**: Code for making the required models available for further training and evaluation has been implement...

### R04: Code for accessing the train and test splits from the CIFAR1...
- **Rubric ID**: f84d16cb-9fa4-4a48-a998-8341fbda33df
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and test splits from the CIFAR10 dataset has been implemented
- **Parent context**: Code for accessing the required datasets has been implemented

### R05: Code for accessing the train and test splits from the CIFAR1...
- **Rubric ID**: d79dc535-2f03-42da-a0dc-d3ec04ce2a3c
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and test splits from the CIFAR100 dataset has been implemented
- **Parent context**: Code for accessing the required datasets has been implemented

### R06: Code for accessing the train and test splits from the SVHN d...
- **Rubric ID**: 08e02fff-9106-4d26-8fab-75b400762f68
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and test splits from the SVHN dataset has been implemented
- **Parent context**: Code for accessing the required datasets has been implemented

### R07: Code for accessing the train and test splits from the GTSRB...
- **Rubric ID**: 95f3c004-5727-4bb0-afb2-6d1ea62209a5
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and test splits from the GTSRB dataset has been implemented
- **Parent context**: Code for accessing the required datasets has been implemented

### R08: Code for accessing the train and test splits from the Flower...
- **Rubric ID**: bfed30a3-49a1-44a6-810c-c04822744046
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and test splits from the Flowers102 dataset has been implemented
- **Parent context**: Code for accessing the required datasets has been implemented

### R09: Code for accessing the train and test splits from the DTD da...
- **Rubric ID**: 75fd216b-5141-4c86-afe7-458d5f121c5e
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and test splits from the DTD dataset has been implemented
- **Parent context**: Code for accessing the required datasets has been implemented

### R10: Code for accessing the train and test splits from the UCF101...
- **Rubric ID**: fe02873b-c79e-40c2-9c7c-04b61bf0f8a5
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and test splits from the UCF101 dataset has been implemented
- **Parent context**: Code for accessing the required datasets has been implemented

### R11: Code for accessing the train and test splits from the Food10...
- **Rubric ID**: b0ddd385-32f8-4cdd-9549-96989613d593
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and test splits from the Food101 dataset has been implemented
- **Parent context**: Code for accessing the required datasets has been implemented

### R12: Code for accessing the train and test splits from the EuroSA...
- **Rubric ID**: 4c9b219d-860f-4571-9ab7-1262786f28e1
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and test splits from the EuroSAT dataset has been implemented
- **Parent context**: Code for accessing the required datasets has been implemented

### R13: Code for accessing the train and test splits from the Oxford...
- **Rubric ID**: f45b8463-27f2-4014-8fdb-2c95c23c98be
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and test splits from the OxfordPets dataset has been implemented
- **Parent context**: Code for accessing the required datasets has been implemented

### R14: Code for accessing the train and test splits from the SUN397...
- **Rubric ID**: 66937e8a-d389-42ad-b860-9090226c8abf
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code for accessing the train and test splits from the SUN397 dataset has been implemented
- **Parent context**: Code for accessing the required datasets has been implemented

## Data Processing & Preparation

### R15: When computing the frequency distribution of the dataset, a...
- **Rubric ID**: 2a23ed70-e265-48b3-add8-52b8fed355b3
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: When computing the frequency distribution of the dataset, a matrix $d$ is initialized with zeros; $d \leftarrow \{0\}^{|\mathcal{Y}^P| \times |\mathcal{Y}^T|}$, where $\mathcal{Y}^T$ are the labels of the target task, and $\mathcal{Y}^P$ are the labels of the pre-trained task
- **Parent context**: The frequency distribution of the dataset of the new task can be computed, following Algorithm 2

### R16: When computing the frequency distribution of the dataset, gi...
- **Rubric ID**: 04ab5a91-e779-4ae7-adc2-b2542e8a53dc
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: When computing the frequency distribution of the dataset, given a target training set $\{(x_i^T,y_i^T)\}_{i=1}^n$, for each sample in the training set, the output label is computed as $\hat{y}_i^P \leftarrow f_P\left(f_\text{in}\left(x_i^\top \vert \theta \right)\right)$, where $f_P$ is the pre-trained model, and $f_{\text{in}}(\cdot | \theta)$ is the visual reprogramming model
- **Parent context**: The frequency distribution of the dataset of the new task can be computed, following Algorithm 2

### R17: For the Narrow baseline, each input image is resized using b...
- **Rubric ID**: 029e1a82-664e-40b0-8e98-56202d5f080c
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: For the Narrow baseline, each input image is resized using bilinear interpolation to match the expected size of the pre-trained model
- **Parent context**: The Narrow baseline has been implemented, which adds a narrow padding binary mask with a width of 28...

### R18: For the Narrow baseline, the pattern is added to the input i...
- **Rubric ID**: c3885380-1f1d-4339-9e6d-0432536f505f
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: For the Narrow baseline, the pattern is added to the input image only where the mask permits
- **Parent context**: The Narrow baseline has been implemented, which adds a narrow padding binary mask with a width of 28...

### R19: For the Medium baseline, each input image is resized using b...
- **Rubric ID**: 07faea63-1076-4e47-bd1a-ce590440dda9
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: For the Medium baseline, each input image is resized using bilinear interpolation to match the expected size of the pre-trained model
- **Parent context**: The Medium baseline has been implemented, which adds a mask being a quarter of the size of watermark...

### R20: For the Medium baseline, the pattern is added to the input i...
- **Rubric ID**: 011c0d8d-d496-43d2-bcdc-b11680a3a1d0
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: For the Medium baseline, the pattern is added to the input image only where the mask permits
- **Parent context**: The Medium baseline has been implemented, which adds a mask being a quarter of the size of watermark...

### R21: For the Full baseline, each input image is resized using bil...
- **Rubric ID**: 19720506-113d-45b6-9a81-ba89ed523ec8
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: For the Full baseline, each input image is resized using bilinear interpolation to match the expected size of the pre-trained model
- **Parent context**: The Full baseline has been implemented, adding a full watermark to cover whole images

### R22: For SSM, each input image is resized using bilinear interpol...
- **Rubric ID**: fe4f42fb-ee29-4c26-9385-f1a6472e6b23
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: For SSM, each input image is resized using bilinear interpolation to match the expected size of the mask generator
- **Parent context**: SSM has been implemented

### R23: When training a model using the SSM method, for each trainin...
- **Rubric ID**: dc46fc23-12fd-44ef-845f-c435dc4ae22e
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: When training a model using the SSM method, for each training batch, each image is first resized using bilinear interpolation if they do not match the expected input shape of the pre-trained model
- **Parent context**: The learning strategy is implemented, following Algorithm 1

### R24: 5000 samples are (separately) randomly selected from the tra...
- **Rubric ID**: 78ac48cc-7ba9-4469-a1dc-ea3c0b379b53
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: 5000 samples are (separately) randomly selected from the training sets of the SVHN and EuroSAT datasets
- **Parent context**: The experiments under the "Feature Space Visualization Results" subsection have been executed

## Evaluation, Metrics & Benchmarking

### R25: When computing the frequency distribution of the dataset, fo...
- **Rubric ID**: e72bdc32-4752-4664-bf89-cf19d5f1c06a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When computing the frequency distribution of the dataset, for each predicted label $\hat{y}_i^P$, the frequency distribution matrix is updated; $d_{\hat{y}_i^P, y_i^T} \leftarrow d_{\hat{y}_i^P, y_i^T} + 1$
- **Parent context**: The frequency distribution of the dataset of the new task can be computed, following Algorithm 2

### R26: For the Narrow baseline, cross-entropy loss is computed betw...
- **Rubric ID**: 5760dac1-e5e8-4510-8dcb-93786fe80c5c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the Narrow baseline, cross-entropy loss is computed between the predicted labels and the target labels
- **Parent context**: The Narrow baseline has been implemented, which adds a narrow padding binary mask with a width of 28...

### R27: For the Full baseline, cross-entropy loss is computed betwee...
- **Rubric ID**: cda0f380-0bfd-4658-83e0-5214fc81e560
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the Full baseline, cross-entropy loss is computed between the predicted labels and the target labels
- **Parent context**: The Full baseline has been implemented, adding a full watermark to cover whole images

### R28: When training a model using the SSM method, cross-entropy lo...
- **Rubric ID**: 37ad5b36-37c2-477a-94f4-699ac646af46
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When training a model using the SSM method, cross-entropy loss is computed between the predicted labels and the target labels
- **Parent context**: The learning strategy is implemented, following Algorithm 1

### R29: Using the "Pad" reprogramming method, ResNet-18 (pre-trained...
- **Rubric ID**: 29ccdd70-e06c-4317-8fce-b698657e6859
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R30: Using the "Pad" reprogramming method, ResNet-18 (pre-trained...
- **Rubric ID**: 507aac89-d860-4cc5-a8f5-a4953412c82a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R31: Using the "Pad" reprogramming method, ResNet-18 (pre-trained...
- **Rubric ID**: cc6cc6c8-b198-4a7a-99db-5256e0e73240
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R32: Using the "Pad" reprogramming method, ResNet-18 (pre-trained...
- **Rubric ID**: 55186fba-a6e3-4296-872e-3cf423508676
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R33: Using the "Pad" reprogramming method, ResNet-18 (pre-trained...
- **Rubric ID**: 890db47b-85d4-4fc7-bfd5-8695a090cad8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R34: Using the "Pad" reprogramming method, ResNet-18 (pre-trained...
- **Rubric ID**: 9435d586-0ad5-4276-8ef4-3b7f84ecd883
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R35: Using the "Pad" reprogramming method, ResNet-18 (pre-trained...
- **Rubric ID**: 7d3baa68-7210-4700-ae69-81edfe605a14
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R36: Using the "Pad" reprogramming method, ResNet-18 (pre-trained...
- **Rubric ID**: 179ec066-78af-4c98-b33a-8a996015b8b2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R37: Using the "Pad" reprogramming method, ResNet-18 (pre-trained...
- **Rubric ID**: 5eff8822-110b-454b-9453-1e77d0da3ed9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R38: Using the "Pad" reprogramming method, ResNet-18 (pre-trained...
- **Rubric ID**: e345f418-b3b7-412f-a792-fcd1fd2b8d8b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R39: Using the "Narrow" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 28778123-dfc5-4cee-a284-131270c0f159
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R40: Using the "Narrow" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: bc1ed4f4-55f3-4600-9a44-6285695ac92e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R41: Using the "Narrow" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: cfb894a7-3cdc-48fa-b307-b93d75fcc4c4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R42: Using the "Narrow" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 2665ab5f-488b-4bb5-bac7-cad8f8a0006a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R43: Using the "Narrow" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: c5196646-8166-4f11-bc17-07f2d6938bf5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R44: Using the "Medium" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 1453da88-a0b4-43f4-92aa-305c06b56c9b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R45: Using the "Medium" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 5915df12-91e2-445d-8938-520188dcd02e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R46: Using the "Medium" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 89abb1eb-a439-44b8-9a3a-3c83b8318200
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R47: Using the "Medium" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 955b0715-d788-4f0a-818b-90736f25a360
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R48: Using the "Medium" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 938918ed-4ba3-4cb5-a7b1-e0ef8e8fa629
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R49: Using the "Full" reprogramming method, ResNet-18 (pre-traine...
- **Rubric ID**: ef08558e-06dd-4168-b274-2fd1d5de1c1e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R50: Using the "Full" reprogramming method, ResNet-18 (pre-traine...
- **Rubric ID**: c420319f-a681-45c1-8869-3d9d2db0679c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R51: Using the "Full" reprogramming method, ResNet-18 (pre-traine...
- **Rubric ID**: f3f20f30-4785-4854-addf-c5297541e019
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R52: Using the "Full" reprogramming method, ResNet-18 (pre-traine...
- **Rubric ID**: 71dcda3d-7d5a-45c0-9b7d-7884f8126569
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R53: Using the "Full" reprogramming method, ResNet-18 (pre-traine...
- **Rubric ID**: 8ce8c977-a950-4e41-9c8c-ae5208fc67a2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R54: Using the "Full" reprogramming method, ResNet-18 (pre-traine...
- **Rubric ID**: 2710a81b-28a7-4440-95bf-376522377e0b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R55: Using the "Full" reprogramming method, ResNet-18 (pre-traine...
- **Rubric ID**: a73f93c3-6820-4954-b332-99e09bef9e5b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R56: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 4e8a2662-0cbf-4d73-8b57-49cc0727f30b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R57: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 495e381e-68e4-4b1d-a59e-55f3a63116ad
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R58: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 8d6e26aa-8470-4af6-b372-8b43d3d64dad
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R59: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: bc63b917-7f1a-4102-beff-30a5c62ca8ca
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R60: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 5e321fad-a1f8-4571-b113-31d82214a317
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R61: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: c5d8822e-2d53-4d54-83e8-a9687c694f6c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R62: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: f6cb53fa-d651-4557-b693-a82d5937805e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R63: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 6b00f1df-6407-4f2b-afe0-7e9d46e3046b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R64: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: d7e8316a-b815-424c-bed3-2cfd9509dc91
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R65: Using the "Pad" reprogramming method, ResNet-50 (pre-trained...
- **Rubric ID**: 83f678ea-5f73-42d5-8512-3093fe35b4c5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R66: Using the "Pad" reprogramming method, ResNet-50 (pre-trained...
- **Rubric ID**: 7968f4a6-b007-48c7-ad1a-23215c223b2a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R67: Using the "Pad" reprogramming method, ResNet-50 (pre-trained...
- **Rubric ID**: 5565a652-2ac5-4ca8-95b4-fc936f71291b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R68: Using the "Pad" reprogramming method, ResNet-50 (pre-trained...
- **Rubric ID**: e9a1a7b1-39d1-4cb3-a977-7b9262a0f591
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R69: Using the "Pad" reprogramming method, ResNet-50 (pre-trained...
- **Rubric ID**: 07a67783-16e1-47bf-9f91-9939e1dd18aa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R70: Using the "Pad" reprogramming method, ResNet-50 (pre-trained...
- **Rubric ID**: 9b54a965-1cb8-43d5-b417-16819d33656f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R71: Using the "Pad" reprogramming method, ResNet-50 (pre-trained...
- **Rubric ID**: 99eb0dbf-09b6-4e1a-8462-3fd7abdcc4a6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R72: Using the "Pad" reprogramming method, ResNet-50 (pre-trained...
- **Rubric ID**: f764b439-0d7d-4fb3-a00a-149d06eb1a41
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R73: Using the "Narrow" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: 32489ae8-3e3f-4b98-a26d-25ceecaef662
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R74: Using the "Narrow" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: a034d906-bd34-42d4-bfd5-a95f1ed437cb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R75: Using the "Narrow" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: 5dfcb1ba-7497-4941-b323-9f26ca8f6e65
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R76: Using the "Narrow" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: b69ea444-84d1-42f3-a1f6-7b56782d149a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R77: Using the "Narrow" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: d5f0f39e-e0b5-4900-bf34-fb227db50403
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R78: Using the "Narrow" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: edeea2d0-e7dc-4eca-b9e6-a4c295888259
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R79: Using the "Narrow" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: e8d66a6d-7472-4519-a446-6a26d3fabc05
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R80: Using the "Narrow" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: 95b4b89e-9a09-4dd1-9b6e-92f715187368
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R81: Using the "Narrow" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: 7442d669-f15e-4585-8aa9-93900ee9e4af
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R82: Using the "Medium" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: 58735ef8-a1e9-4df9-9c32-c712715f62f1
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R83: Using the "Medium" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: b698d089-8b6b-47f9-bbe7-fab47b8b164f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R84: Using the "Medium" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: 98a95e4e-0bf0-4b57-bf6d-d76f66b1b8b8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R85: Using the "Medium" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: 92c3101e-9169-4c03-9505-e92f88591d21
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R86: Using the "Medium" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: 9150117a-4e00-45ba-a940-1c01f14ac5ed
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R87: Using the "Medium" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: d95f1d64-1235-4164-82eb-d246084b5201
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R88: Using the "Full" reprogramming method, ResNet-50 (pre-traine...
- **Rubric ID**: 9f41ef29-a3d6-4ec3-92ce-82566db70798
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R89: Using the "Full" reprogramming method, ResNet-50 (pre-traine...
- **Rubric ID**: 11c8c88e-2a95-42ee-a6ce-3fc5a055928f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R90: Using the "Full" reprogramming method, ResNet-50 (pre-traine...
- **Rubric ID**: c1effc96-953b-4bf5-9481-66629ec73072
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R91: Using the "Full" reprogramming method, ResNet-50 (pre-traine...
- **Rubric ID**: 9f77f402-9a84-4832-bb56-aac26818ebef
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R92: Using the "Full" reprogramming method, ResNet-50 (pre-traine...
- **Rubric ID**: 946fa5d8-acca-4a9e-a09a-60842c291c74
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R93: Using the "Full" reprogramming method, ResNet-50 (pre-traine...
- **Rubric ID**: d5db6a1b-37b5-4c02-9e19-ae8aee6fcc1b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R94: Using the "Full" reprogramming method, ResNet-50 (pre-traine...
- **Rubric ID**: 1583dd48-8e9a-4fef-bd5a-9d585b87cc70
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R95: Using the "Full" reprogramming method, ResNet-50 (pre-traine...
- **Rubric ID**: 6c196096-ef61-4479-a0a9-445fdbeb5d01
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R96: Using the SNS method ("Ours"), ResNet-50 (pre-trained on Ima...
- **Rubric ID**: a14d923a-3eee-431d-b317-0ecce2c6a749
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R97: Using the SNS method ("Ours"), ResNet-50 (pre-trained on Ima...
- **Rubric ID**: 7aae7881-87c4-46ee-a870-d805c2811fb8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R98: Using the SNS method ("Ours"), ResNet-50 (pre-trained on Ima...
- **Rubric ID**: 9c5f6794-9b12-4f9b-b0fe-632c387819df
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R99: Using the SNS method ("Ours"), ResNet-50 (pre-trained on Ima...
- **Rubric ID**: 275f8b37-9731-423f-bac6-08362b0e3ce0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R100: Using the SNS method ("Ours"), ResNet-50 (pre-trained on Ima...
- **Rubric ID**: d5073146-7a28-4f48-ae90-7f80be8e20f9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R101: Using the SNS method ("Ours"), ResNet-50 (pre-trained on Ima...
- **Rubric ID**: 087d756b-3a54-42a3-a8ed-4ab5c8be52f1
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R102: Using the SNS method ("Ours"), ResNet-50 (pre-trained on Ima...
- **Rubric ID**: 9fde268b-642c-4de9-b68d-859aa8cf98ae
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R103: Using the SNS method ("Ours"), ResNet-50 (pre-trained on Ima...
- **Rubric ID**: 417f9acb-c222-41c1-89fe-a9c32a995190
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R104: The recorded metrics show that SMM yields higher accuracy co...
- **Rubric ID**: e252d7b2-0ce6-49d2-b1b8-3022ca99f085
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that SMM yields higher accuracy compared to all other input reprogramming methods for ResNet-18 on almost all datasets
- **Parent context**: The results under the "Results on ResNets" subsection have been replicated

### R105: The recorded metrics show that SMM yields higher accuracy co...
- **Rubric ID**: 1415e5b0-7934-4e3e-b7d3-7ab84d1b7da8
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that SMM yields higher accuracy compared to all other input reprogramming methods for ResNet-50 on almost all (or all) datasets
- **Parent context**: The results under the "Results on ResNets" subsection have been replicated

### R106: The recorded metrics show that SMM roughly has a 6% (absolut...
- **Rubric ID**: 28aade60-b9c2-4d87-b732-3454e221f4a2
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that SMM roughly has a 6% (absolute) improvement over the next best input reprogramming method when using ResNet-18 on the SVHN dataset
- **Parent context**: The results under the "Results on ResNets" subsection have been replicated

### R107: The recorded metrics show that SMM roughly has a 3% (absolut...
- **Rubric ID**: 97149f22-4d19-451e-8a86-9e407cda5c0d
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that SMM roughly has a 3% (absolute) improvement over the next best input reprogramming method when using ResNet-50 on the SVHN dataset
- **Parent context**: The results under the "Results on ResNets" subsection have been replicated

### R108: The recorded metrics show that SMM roughly has a 10% (absolu...
- **Rubric ID**: e3db8d69-e576-4a86-99ca-ca09f7b233e9
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that SMM roughly has a 10% (absolute) improvement over the next best input reprogramming method when using ResNet-18 on the Flowers102 dataset
- **Parent context**: The results under the "Results on ResNets" subsection have been replicated

### R109: The recorded metrics show that SMM roughly has a 10% (absolu...
- **Rubric ID**: 36b3e62b-e1ae-41ab-9c61-4a51053e9b71
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that SMM roughly has a 10% (absolute) improvement over the next best input reprogramming method when using ResNet-50 on the Flowers102 dataset
- **Parent context**: The results under the "Results on ResNets" subsection have been replicated

### R110: The recorded metrics show that the Pad method performs the b...
- **Rubric ID**: b1f97919-8387-45c0-8c72-5127475b255b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the Pad method performs the best, or amongst the best, compared to other input reprogramming methods when using ResNet-18 on the DTD dataset
- **Parent context**: The results under the "Results on ResNets" subsection have been replicated

### R111: The recorded metrics show that SMM has the highest average a...
- **Rubric ID**: 49a90fac-eb65-4cd0-a65f-14395e89b6d4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that SMM has the highest average accuracy across all datasets when using ResNet-18
- **Parent context**: The results under the "Results on ResNets" subsection have been replicated

### R112: The recorded metrics show that SMM has the highest average a...
- **Rubric ID**: 7a6194fb-9f1b-4ede-8cab-9a3f53a3a9f9
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that SMM has the highest average accuracy across all datasets when using ResNet-50
- **Parent context**: The results under the "Results on ResNets" subsection have been replicated

### R113: Using the "Pad" reprogramming method, ViT-B32 (pre-trained o...
- **Rubric ID**: a4cb092c-7ead-48c8-a457-3777e86c974e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R114: Using the "Pad" reprogramming method, ViT-B32 (pre-trained o...
- **Rubric ID**: e3784854-210a-4e49-a0c4-2da72d546278
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R115: Using the "Pad" reprogramming method, ViT-B32 (pre-trained o...
- **Rubric ID**: 3bda93fb-a0ad-4ab0-b695-fbebbc1f2ff2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R116: Using the "Pad" reprogramming method, ViT-B32 (pre-trained o...
- **Rubric ID**: cdc0c7bb-577b-4f3c-83fe-34094d4248d7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R117: Using the "Pad" reprogramming method, ViT-B32 (pre-trained o...
- **Rubric ID**: 9a3215ff-923e-4c39-89f5-c78fa0409b09
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R118: Using the "Pad" reprogramming method, ViT-B32 (pre-trained o...
- **Rubric ID**: 4c4295aa-f234-4271-b51f-30682ed8a836
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R119: Using the "Pad" reprogramming method, ViT-B32 (pre-trained o...
- **Rubric ID**: 861a7718-9e50-4dd5-8b18-51f75e41f0e4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R120: Using the "Pad" reprogramming method, ViT-B32 (pre-trained o...
- **Rubric ID**: 9b37d411-0d4d-4c9f-bc2a-2171a18fcc2d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R121: Using the "Pad" reprogramming method, ViT-B32 (pre-trained o...
- **Rubric ID**: 007014ce-e63c-4d91-83ca-d43f6e35a78b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R122: Using the "Narrow" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: 7d0c7ab5-2637-4536-9993-a1040d2b2093
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R123: Using the "Narrow" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: aec8c31f-42d3-4232-81b1-e7ccb1a170f7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R124: Using the "Narrow" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: dfc8a555-d9af-420d-b41c-8e6392e6b0e8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R125: Using the "Narrow" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: 1f1e30fa-97d3-4e06-9ace-d0c8b47d37d4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R126: Using the "Narrow" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: afe9b04f-1a4a-438b-9d3a-b28ec47ee2de
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R127: Using the "Narrow" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: 02d0cdaa-3646-4d36-b1e8-71e8142aae3b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R128: Using the "Narrow" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: 07137382-42ef-488e-bda0-89658f0fa86d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R129: Using the "Medium" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: 4da5e242-4a52-41f7-adb8-a8508d3c2596
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R130: Using the "Medium" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: 28fe8c6f-b124-4ce7-a0df-5c99a059c841
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R131: Using the "Medium" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: 5b2cf32c-d3cf-4d64-b6b9-6fb707ed7b75
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R132: Using the "Medium" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: 7f079120-3868-457e-9ecb-6edf2d53720b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R133: Using the "Medium" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: 363351dd-8141-4789-9977-0c35273159dd
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R134: Using the "Medium" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: e1234c1a-928f-4229-9e09-714dcbb75700
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R135: Using the "Medium" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: 4d17958c-fa70-47a8-8ba8-624d7d6298e7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R136: Using the "Full" reprogramming method, ViT-B32 (pre-trained...
- **Rubric ID**: 22ef5a0c-4a35-4514-8457-d5651f1a1e83
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on t...

### R137: Using the "Full" reprogramming method, ViT-B32 (pre-trained...
- **Rubric ID**: ef4bc970-bc9a-4c55-a6fd-d346c89bfbc3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on t...

### R138: Using the "Full" reprogramming method, ViT-B32 (pre-trained...
- **Rubric ID**: 24558a39-92c2-4d6c-a9e8-2804de1a49c2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on t...

### R139: Using the "Full" reprogramming method, ViT-B32 (pre-trained...
- **Rubric ID**: 70d90d62-24fe-425a-8599-d202675276bf
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on t...

### R140: Using the "Full" reprogramming method, ViT-B32 (pre-trained...
- **Rubric ID**: 8fdd510b-5c9b-4399-9146-8b0ced98da88
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on t...

### R141: Using the "Full" reprogramming method, ViT-B32 (pre-trained...
- **Rubric ID**: 1cdfef7d-cdca-42b5-8dd5-698c637b5b6d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on t...

### R142: Using the "Full" reprogramming method, ViT-B32 (pre-trained...
- **Rubric ID**: c91b790d-0331-46a8-8595-f509968ab135
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on t...

### R143: Using the "Full" reprogramming method, ViT-B32 (pre-trained...
- **Rubric ID**: 55b2acbd-744b-4ef7-984d-98037c25939d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on t...

### R144: Using the SNS method ("Ours"), ViT-B32 (pre-trained on Image...
- **Rubric ID**: d70c899c-d646-4f38-a5c2-4f62c640a0ac
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R145: Using the SNS method ("Ours"), ViT-B32 (pre-trained on Image...
- **Rubric ID**: 8fb53b93-758d-4dea-8be2-2cb8b8d56bbc
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R146: Using the SNS method ("Ours"), ViT-B32 (pre-trained on Image...
- **Rubric ID**: 537b5685-9202-4469-8368-1e439989a60d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R147: Using the SNS method ("Ours"), ViT-B32 (pre-trained on Image...
- **Rubric ID**: 32543e16-0c23-4ca2-bc2d-5f4f16ad85d0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R148: Using the SNS method ("Ours"), ViT-B32 (pre-trained on Image...
- **Rubric ID**: 1055ba97-54aa-4e2f-8877-999c11c7ce34
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R149: Using the SNS method ("Ours"), ViT-B32 (pre-trained on Image...
- **Rubric ID**: 43767618-84d8-40e1-8a26-7d170b93d451
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R150: Using the SNS method ("Ours"), ViT-B32 (pre-trained on Image...
- **Rubric ID**: fde40183-7405-4529-9e68-0b48d4f8e41a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R151: Using the SNS method ("Ours"), ViT-B32 (pre-trained on Image...
- **Rubric ID**: 9d7ca2f0-26fb-4678-9952-a452aefae37d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R152: The recorded metrics show that SMM achieves roughly a 22% (a...
- **Rubric ID**: 80b9098e-1af8-42a0-bd45-8eebd0fac155
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that SMM achieves roughly a 22% (absolute) improvement over the next best input reprogramming method for ViT on the Flowers102 dataset
- **Parent context**: The results under the "Results on ViT" subsection have been replicated

### R153: The recorded metrics show that SMM achieves roughly a 15% (a...
- **Rubric ID**: 688a2c83-0e01-4629-8e56-67c46a3c5371
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that SMM achieves roughly a 15% (absolute) improvement over the next best input reprogramming method for ViT on the Food101 dataset
- **Parent context**: The results under the "Results on ViT" subsection have been replicated

### R154: The recorded metrics show that SMM achieves roughly a 7% (ab...
- **Rubric ID**: d061ec1a-8fd3-4b4f-b582-e14ffb92f688
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that SMM achieves roughly a 7% (absolute) improvement over the next best input reprogramming method for ViT on the SUN397 dataset
- **Parent context**: The results under the "Results on ViT" subsection have been replicated

### R155: The recorded metrics show that pad performs the best, or amo...
- **Rubric ID**: b20f72ec-e4b0-47e2-b870-ce5a8ff3acbc
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that pad performs the best, or amongst the best, compared to other input reprogramming methods for ViT on the EuroSAT dataset
- **Parent context**: The results under the "Results on ViT" subsection have been replicated

### R156: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (...
- **Rubric ID**: bb1e2cb0-d8eb-4a85-b42a-f6b104ff1fda
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fin...

### R157: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (...
- **Rubric ID**: 76919e09-f9d4-4b2f-a5b5-3db205b416d0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fin...

### R158: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (...
- **Rubric ID**: ec58b52e-9130-47ce-98b0-992c1fedd24b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fin...

### R159: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (...
- **Rubric ID**: 05fb0ae1-e802-45a9-ae41-7ab94448e244
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fin...

### R160: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (...
- **Rubric ID**: 850b7e2a-f61d-4289-afbf-e8ecf57502aa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fin...

### R161: Using the "sample-specific pattern without masking" SMM vari...
- **Rubric ID**: ded7a725-4b1b-47b5-9c72-5145cd84c28b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K...

### R162: Using the "sample-specific pattern without masking" SMM vari...
- **Rubric ID**: 58fa0ebb-150c-474f-b93f-85181300e01d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K...

### R163: Using the "sample-specific pattern without masking" SMM vari...
- **Rubric ID**: 86c2b1ea-48b0-4c34-8978-b367ab8d3679
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K...

### R164: Using the "sample-specific pattern without masking" SMM vari...
- **Rubric ID**: cb58e7bb-b960-47eb-87bc-76dce05c5761
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K...

### R165: Using the "sample-specific pattern without masking" SMM vari...
- **Rubric ID**: b737cf67-10f5-4848-8606-7015f70f9ce6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K...

### R166: Using the "sample-specific pattern without masking" SMM vari...
- **Rubric ID**: 53387120-fc5f-4c05-bdc8-f07472041752
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K...

### R167: Using the "sample-specific pattern without masking" SMM vari...
- **Rubric ID**: a2ab7f2f-9e7b-4761-9d6f-e5d20065212a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K...

### R168: Using the "The Single-channel version of SMM" variant, ViT-B...
- **Rubric ID**: 645fe9c1-d993-41b9-a227-2a89b0647041
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been...

### R169: Using the "The Single-channel version of SMM" variant, ViT-B...
- **Rubric ID**: 6832335d-c86f-4aa7-b7a7-e7adf0e2531a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been...

### R170: Using the "The Single-channel version of SMM" variant, ViT-B...
- **Rubric ID**: c7adc31d-2cfb-4c68-adb0-fb9fcc1b2532
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been...

### R171: Using the "The Single-channel version of SMM" variant, ViT-B...
- **Rubric ID**: 08f30815-c66a-419a-a750-e1e15377ecb7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been...

### R172: Using the "The Single-channel version of SMM" variant, ViT-B...
- **Rubric ID**: 31684286-d9d8-496e-a6d7-91c9617b3508
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been...

### R173: Using the "The Single-channel version of SMM" variant, ViT-B...
- **Rubric ID**: 8b6a66ba-207e-40f4-97ea-1f163a36a35e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been...

### R174: Using the "The Single-channel version of SMM" variant, ViT-B...
- **Rubric ID**: 16dbc97f-c485-44f2-978d-1a0585eba671
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been...

### R175: Using the "The Single-channel version of SMM" variant, ViT-B...
- **Rubric ID**: ad45e93e-06b0-44b7-966c-d58787c72357
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been...

### R176: The recorded metrics show that the default SMM ("Ours") meth...
- **Rubric ID**: f516bb4c-c129-4857-8d80-2203a9e0260d
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the default SMM ("Ours") method achieves the best average accuracy for each dataset across all mask variants for ViT
- **Parent context**: The results under the "Impact of Masking" subsection have been replicated

### R177: The recorded metrics show that the Sample-specific pattern w...
- **Rubric ID**: 105c14cc-bf0d-486c-ada0-815d82a92613
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the Sample-specific pattern without masking variant (aka. "Only $f_\text{mask}$") achieves the lowest average accuracy for ViT for the CIFAR10, SVHN, GTSRB, and SUN397 datasets
- **Parent context**: The results under the "Impact of Masking" subsection have been replicated

### R178: The recorded metrics show that the Single-channel version of...
- **Rubric ID**: 251d1112-d76b-463a-add8-6f6b6e801f16
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the Single-channel version of SMM variant (aka. "Single-Chanel $f_\text{mask}^s$") performs significantly worse (at least 5%) than the default SMM ("Ours") method for ViT for the GTSRB and Flowers102 datasets
- **Parent context**: The results under the "Impact of Masking" subsection have been replicated

### R179: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: b016a53e-5a12-403a-840f-c879d8383220
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 1 (i.e. the mask generator has zero max-pooling layers) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 1 (i.e....

### R180: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: f426b856-22cf-4aed-ab75-dd8ac47cc614
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 1 (i.e. the mask generator has zero max-pooling layers) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 1 (i.e....

### R181: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: d4753360-0c17-4baa-810d-e250383108b3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 2 (i.e. the mask generator has one max-pooling layer) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 2 (i.e....

### R182: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 1090e6b8-5ccd-4af2-b27c-203a8504bb87
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 2 (i.e. the mask generator has one max-pooling layer) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 2 (i.e....

### R183: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 83dc0195-4330-478d-95b5-047aab7e656d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 2 (i.e. the mask generator has one max-pooling layer) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 2 (i.e....

### R184: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: ec9f30cb-af3f-47d2-aeef-e250093f3cbc
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 2 (i.e. the mask generator has one max-pooling layer) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 2 (i.e....

### R185: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 476f144c-c94b-4b67-8e03-da4d4733e29b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 4 (i.e. the mask generator has two max-pooling layers) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 4 (i.e....

### R186: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 513d9f00-8b1b-4bc6-8541-c012b9c2e8cf
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 4 (i.e. the mask generator has two max-pooling layers) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 4 (i.e....

### R187: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 426e262b-dfe8-4198-8c6f-ab4a7e7ec49d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 4 (i.e. the mask generator has two max-pooling layers) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 4 (i.e....

### R188: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: ee7c7b65-ad80-4c72-a013-5bb147982603
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 16 (i.e. the mask generator has four max-pooling layers) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 16 (i.e...

### R189: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 6b2a337f-7fc7-4637-b0d5-4953ff3dbef7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 16 (i.e. the mask generator has four max-pooling layers) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 16 (i.e...

### R190: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: d288eb7a-78f2-4d79-b86c-638b17075f67
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 16 (i.e. the mask generator has four max-pooling layers) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 16 (i.e...

### R191: The recorded metrics show that the accuracy of the SMM with...
- **Rubric ID**: 4087ac21-483d-4598-985c-fb90f5bd6f94
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the accuracy of the SMM with patch size 4 is greater than the accuracy of SMM with patch size 1. This result holds for all datasets CIFAR100, FLOWERS102, SVHN, and EUROSAT
- **Parent context**: The results under the the "Impact of Patch Size" subsection have been replicated

### R192: The recorded metrics show that the accuracy of the SMM with...
- **Rubric ID**: e18ae43e-86d7-437d-9eec-7adeb956cc6b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the accuracy of the SMM with patch size 16 is similar the accuracy of SMM with patch size 4, i.e., the difference is smaller than the difference when comparing patch size 4 to patch size 1. This result holds for all datasets CIFAR100, FLOWERS102, SVHN, and EUROSAT
- **Parent context**: The results under the the "Impact of Patch Size" subsection have been replicated

### R193: The recorded metrics show that before applying any VR method...
- **Rubric ID**: 237676cb-e3d2-4934-bd0f-0eb47f928c28
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that before applying any VR methods (i.e. just looking at ResNet-18 embeddings), the output feature space has limited class separation
- **Parent context**: The results under the the "Feature Space Visualization Results" subsection have been replicated

### R194: The recorded metrics show that the "Ours" method has the bes...
- **Rubric ID**: 5f41a380-ebed-4a1f-afee-0939eccc95f7
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that the "Ours" method has the best class separation in output feature space compared to other baseline methods, across both datasets
- **Parent context**: The results under the the "Feature Space Visualization Results" subsection have been replicated

## Method Implementation

### R195: When computing the output mapping using Iterative label mapp...
- **Rubric ID**: 1aa39331-a96a-4a15-b149-8bdc40a8ab9f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When computing the output mapping using Iterative label mapping, at the start of each epoch the frequency distribution of the target training set is first computed
- **Parent context**: The output mapping can be computed, following Algorithm 4

### R196: When computing the output mapping using Iterative label mapp...
- **Rubric ID**: 2da66162-8014-4073-b299-a2ba8a6aeea5
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: When computing the output mapping using Iterative label mapping, on each epoch the following algorithm is applied; $\mathcal{Y}_\text{sub}^P$ is initialized as $\emptyset$. Until the size of $\mathcal{Y}_\text{sub}^P$ is $|\mathcal{Y}^T|$ the following steps are taken: 1) the maximum $d_{y^P, y^T}$ in frequency distribution $d$ is found and added to $\mathcal{Y}_\text{sub}^P$, 2) the label mapping is updated as $f_\text{out}^\text{Ilm} (y^P) \leftarrow y^T$, 3) the frequency distribution is updated as $d_{y^P, t} \leftarrow 0 \text{ for } t=1,2,...,|\mathcal{Y}^T|$, and $d_{s, y^T} \leftarrow 0 \text{ for } s=1,2,...,|\mathcal{Y}^P|$
- **Parent context**: The output mapping can be computed, following Algorithm 4

### R197: For the Pad baseline, a pattern is initialized, with shape e...
- **Rubric ID**: 1659bb57-01ba-4637-9645-ed781a6123c1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Pad baseline, a pattern is initialized, with shape equivalent to the expected input shape of the pre-trained model
- **Parent context**: The Pad baseline has been implemented, where the original image is centered then the noise pattern i...

### R198: For the Pad baseline, the input image is centered, then the...
- **Rubric ID**: d41661a4-c34a-44c9-8493-f2bcd86e5649
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Pad baseline, the input image is centered, then the noise pattern is concatenated around the image to form the expected input shape for the pre-trained model (only if the input image is smaller than the required input size for the pre-trained model)
- **Parent context**: The Pad baseline has been implemented, where the original image is centered then the noise pattern i...

### R199: For the Pad baseline, the input image (that has the masked p...
- **Rubric ID**: 09a272e5-cd45-468f-aa8a-ed481a93e7a1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Pad baseline, the input image (that has the masked pattern concatenated around it) is fed into the pretrained model
- **Parent context**: The Pad baseline has been implemented, where the original image is centered then the noise pattern i...

### R200: For the Pad baseline, the predicted label from the pre-train...
- **Rubric ID**: a7cee3c7-4e8d-42a9-8638-24ba50532c76
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Pad baseline, the predicted label from the pre-trained model is mapped using the iterative label mapping (ILM)
- **Parent context**: The Pad baseline has been implemented, where the original image is centered then the noise pattern i...

### R201: For the Narrow baseline, a pattern is initialized, with shap...
- **Rubric ID**: 82aec253-a90a-4515-95c5-a98a45f2b16b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Narrow baseline, a pattern is initialized, with shape equivalent to the expected input shape of the pre-trained model
- **Parent context**: The Narrow baseline has been implemented, which adds a narrow padding binary mask with a width of 28...

### R202: For the Narrow baseline, a mask is defined with shape equiva...
- **Rubric ID**: 7b29d3dc-4ebf-4b89-a00e-bc6bb6774d95
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Narrow baseline, a mask is defined with shape equivalent to the expected input shape to the pre-trained model. All values are masked aside from the edges of the image, with this edge having width 28
- **Parent context**: The Narrow baseline has been implemented, which adds a narrow padding binary mask with a width of 28...

### R203: For the Narrow baseline, the input image (that has the maske...
- **Rubric ID**: 3010baa0-2eb1-427b-b0c3-c27f12c4a06d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Narrow baseline, the input image (that has the masked pattern added to it) is fed into the pretrained model
- **Parent context**: The Narrow baseline has been implemented, which adds a narrow padding binary mask with a width of 28...

### R204: For the Narrow baseline, the predicted label from the pre-tr...
- **Rubric ID**: 727cea73-8c1c-4015-ab8f-884837a9574f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Narrow baseline, the predicted label from the pre-trained model is mapped using the iterative label mapping (ILM)
- **Parent context**: The Narrow baseline has been implemented, which adds a narrow padding binary mask with a width of 28...

### R205: For the Narrow baseline, only the noise pattern is updated t...
- **Rubric ID**: 3d9bfc0b-52b0-4276-9fb8-c828d5d4a82a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Narrow baseline, only the noise pattern is updated through gradient descent
- **Parent context**: The Narrow baseline has been implemented, which adds a narrow padding binary mask with a width of 28...

### R206: For the Medium baseline, a pattern is initialized, with shap...
- **Rubric ID**: c2bd1ec0-4155-49cb-aac2-04b567980314
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Medium baseline, a pattern is initialized, with shape equivalent to the expected input shape of the pre-trained model
- **Parent context**: The Medium baseline has been implemented, which adds a mask being a quarter of the size of watermark...

### R207: For the Medium baseline, a mask is defined with shape equiva...
- **Rubric ID**: a354fa2f-cb60-4102-9716-a642ce4e98ba
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Medium baseline, a mask is defined with shape equivalent to the expected input shape to the pre-trained model. All values are masked, aside from a central shape being a quarter of the size of the height and width of the expected input shape to the pre-trained model
- **Parent context**: The Medium baseline has been implemented, which adds a mask being a quarter of the size of watermark...

### R208: For the Medium baseline, the predicted label from the pre-tr...
- **Rubric ID**: 76426b26-b4c3-48cd-9b3d-f13897a25f75
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Medium baseline, the predicted label from the pre-trained model is mapped using the iterative label mapping (ILM)
- **Parent context**: The Medium baseline has been implemented, which adds a mask being a quarter of the size of watermark...

### R209: For the Medium baseline, only the noise pattern is updated t...
- **Rubric ID**: a1acec74-2544-4769-814f-76e865385127
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Medium baseline, only the noise pattern is updated through gradient descent
- **Parent context**: The Medium baseline has been implemented, which adds a mask being a quarter of the size of watermark...

### R210: For the Full baseline, a pattern is initialized, with shape...
- **Rubric ID**: 2b92cd04-d3d9-4e2f-bf77-00b305a79595
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Full baseline, a pattern is initialized, with shape equivalent to the expected input shape of the pre-trained model
- **Parent context**: The Full baseline has been implemented, adding a full watermark to cover whole images

### R211: For the Full baseline, the pattern is added to the input ima...
- **Rubric ID**: d9690901-0608-43bc-ba05-de5f7fdd866a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Full baseline, the pattern is added to the input image
- **Parent context**: The Full baseline has been implemented, adding a full watermark to cover whole images

### R212: For the Full baseline, the input image (that has the pattern...
- **Rubric ID**: 618c8e96-f4d0-41bb-acc6-6c39ea233ac7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Full baseline, the input image (that has the pattern added to it) is fed into the pretrained model
- **Parent context**: The Full baseline has been implemented, adding a full watermark to cover whole images

### R213: For the Full baseline, the predicted label from the pre-trai...
- **Rubric ID**: 11e338dc-981c-4f78-989f-d170e615bd5c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Full baseline, the predicted label from the pre-trained model is mapped using the iterative label mapping (ILM)
- **Parent context**: The Full baseline has been implemented, adding a full watermark to cover whole images

### R214: For the Full baseline, only the noise pattern is updated thr...
- **Rubric ID**: 7b3f1fd1-149c-450f-b823-c7fa64e15c23
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the Full baseline, only the noise pattern is updated through gradient descent
- **Parent context**: The Full baseline has been implemented, adding a full watermark to cover whole images

### R215: When using the SSM method with ResNet-18 or ResNet-50, the m...
- **Rubric ID**: 28be07ce-4482-4813-ae60-9824fdb26970
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When using the SSM method with ResNet-18 or ResNet-50, the mask generator is a 5-layer CNN
- **Parent context**: When the SSM method is used with ResNet-18 or ResNet-50, the mask generator has the correct architec...

### R216: When using the SSM method with ResNet-18 or ResNet-50, the f...
- **Rubric ID**: c4ae713d-03bc-487d-82b0-61414ace95cc
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When using the SSM method with ResNet-18 or ResNet-50, the first layer of the mask generator is a 3*3 convolution of padding size 1 and stride 1 with 8 output channels, followed by BatchNorm, ReLU, then a 2*2 Max Pool
- **Parent context**: When the SSM method is used with ResNet-18 or ResNet-50, the mask generator has the correct architec...

### R217: When using the SSM method with ResNet-18 or ResNet-50, the s...
- **Rubric ID**: 02c368c6-9447-4d0b-bdb9-3e8b6719be02
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When using the SSM method with ResNet-18 or ResNet-50, the second layer of the mask generator is a 3*3 convolution of padding size 1 and stride 1 with 16 output channels, followed by BatchNorm, ReLU, then a 2*2 Max Pool
- **Parent context**: When the SSM method is used with ResNet-18 or ResNet-50, the mask generator has the correct architec...

### R218: When using the SSM method with ResNet-18 or ResNet-50, the t...
- **Rubric ID**: b3bb8a27-abe3-4b9b-a22e-0a2a0df25ef8
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When using the SSM method with ResNet-18 or ResNet-50, the third layer of the mask generator is a 3*3 convolution of padding size 1 and stride 1 with 32 output channels, followed by BatchNorm, ReLU, then a 2*2 Max Pool
- **Parent context**: When the SSM method is used with ResNet-18 or ResNet-50, the mask generator has the correct architec...

### R219: When using the SSM method with ResNet-18 or ResNet-50, the f...
- **Rubric ID**: adad65b3-7c4f-46a0-89b8-c4c0b1db4969
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When using the SSM method with ResNet-18 or ResNet-50, the fourth layer of the mask generator is a 3*3 convolution of padding size 1 and stride 1 with 64 output channels, followed by BatchNorm, then ReLU
- **Parent context**: When the SSM method is used with ResNet-18 or ResNet-50, the mask generator has the correct architec...

### R220: When using the SSM method with ResNet-18 or ResNet-50, the f...
- **Rubric ID**: a3709fb5-e8d2-4e18-9fd0-5f819c20f278
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When using the SSM method with ResNet-18 or ResNet-50, the fifth layer of the mask generator is a 3*3 convolution of padding size 1 and stride 1 with 3 output channels
- **Parent context**: When the SSM method is used with ResNet-18 or ResNet-50, the mask generator has the correct architec...

### R221: When using the SSM method with ViT-B32, the mask generator i...
- **Rubric ID**: 50319077-9185-444a-abb3-124e17143454
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When using the SSM method with ViT-B32, the mask generator is a 6-layer CNN
- **Parent context**: When the SSM method is used with ViT-B32, the mask generator has the correct architecture

### R222: When using the SSM method with ViT-B32, the first layer of t...
- **Rubric ID**: 59ff8add-298c-476e-96e2-8820acd6ef7f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When using the SSM method with ViT-B32, the first layer of the mask generator is a 3*3 convolution of padding size 1 and stride 1 with 8 output channels, followed by BatchNorm, ReLU, then a 2*2 Max Pool
- **Parent context**: When the SSM method is used with ViT-B32, the mask generator has the correct architecture

### R223: When using the SSM method with ViT-B32, the second layer of...
- **Rubric ID**: 33204cda-df15-4390-8472-934e7cbc217f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When using the SSM method with ViT-B32, the second layer of the mask generator is a 3*3 convolution of padding size 1 and stride 1 with 16 output channels, followed by BatchNorm, ReLU, then a 2*2 Max Pool
- **Parent context**: When the SSM method is used with ViT-B32, the mask generator has the correct architecture

### R224: When using the SSM method with ViT-B32, the third layer of t...
- **Rubric ID**: 5fc09bcb-ded4-4641-9d18-050c13edb383
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When using the SSM method with ViT-B32, the third layer of the mask generator is a 3*3 convolution of padding size 1 and stride 1 with 32 output channels, followed by BatchNorm, ReLU, then a 2*2 Max Pool
- **Parent context**: When the SSM method is used with ViT-B32, the mask generator has the correct architecture

### R225: When using the SSM method with ViT-B32, the fourth layer of...
- **Rubric ID**: c43bdbe6-744c-4a35-8001-9e6411387b2a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When using the SSM method with ViT-B32, the fourth layer of the mask generator is a 3*3 convolution of padding size 1 and stride 1 with 64 output channels, followed by BatchNorm, then ReLU
- **Parent context**: When the SSM method is used with ViT-B32, the mask generator has the correct architecture

### R226: When using the SSM method with ViT-B32, the fifth layer of t...
- **Rubric ID**: 7719f69d-f138-46d3-a528-fd338f5e37e0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When using the SSM method with ViT-B32, the fifth layer of the mask generator is a 3*3 convolution of padding size 1 and stride 1 with 128 output channels, followed by BatchNorm, then ReLU
- **Parent context**: When the SSM method is used with ViT-B32, the mask generator has the correct architecture

### R227: When using the SSM method with ViT-B32, the sixth layer of t...
- **Rubric ID**: a03cef9e-9922-4be5-8d4e-81169f7c307d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When using the SSM method with ViT-B32, the sixth layer of the mask generator is a 3*3 convolution of padding size 1 and stride 1 with 3 output channels
- **Parent context**: When the SSM method is used with ViT-B32, the mask generator has the correct architecture

### R228: In the mask generator module in SSM, given a three-channel i...
- **Rubric ID**: 43b56ae9-41a4-42f0-b947-f3ad5c90714a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In the mask generator module in SSM, given a three-channel image as input with height $H$ and width $W$, the mask generator outputs a three-channel mask with dimensions $\left\lfloor \frac{H}{2^l} \right\rfloor \times \left\lfloor \frac{W}{2^l} \right\rfloor$, where $l$ denotes the number of pooling layers in the mask generator CNN
- **Parent context**: The mask generator module is implemented, following Section 3.2

### R229: In the Patch-wise Interpolation Module in SSM, if the number...
- **Rubric ID**: 0315e7cf-6348-4a44-ba10-56eb29ff07e7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In the Patch-wise Interpolation Module in SSM, if the number of pooling layers in the mask generator CNN is not zero, each pixel is enlarged to $2^l \times 2^l$ pixels using bilinear interpolation. If this expansion does not evenly cover the image area (e.g. near the image edges) the value of the nearest available pixel is used to fill in any gaps.
- **Parent context**: The Patch-wise Interpolation Module is implemented, following Section 3.3

### R230: In the Patch-wise Interpolation Module in SSM, if the number...
- **Rubric ID**: 1148dc53-dfe7-43b8-9565-1b4d057ac44d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In the Patch-wise Interpolation Module in SSM, if the number of pooling layers in the mask generator CNN is zero, then the input image is not enlarged
- **Parent context**: The Patch-wise Interpolation Module is implemented, following Section 3.3

### R231: When training a model using the SSM method, individual masks...
- **Rubric ID**: 0fde2a77-a2d2-452e-bfce-ef78b96531ab
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When training a model using the SSM method, individual masks for each image in the training batch are generated by the mask generator
- **Parent context**: The learning strategy is implemented, following Algorithm 1

### R232: When training a model using the SSM method, the generated ma...
- **Rubric ID**: 0cea4c76-6b6d-4b12-959f-cbbfe2a8afa5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When training a model using the SSM method, the generated masks for each image in each training batch are resized using the patch-wise interpolation module
- **Parent context**: The learning strategy is implemented, following Algorithm 1

### R233: When training a model using the SSM method, for each image i...
- **Rubric ID**: 27c360ce-967b-49ec-81e7-80c9af5e93f7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When training a model using the SSM method, for each image in the batch, the pattern $\delta$ is multiplied with the mask on a pixel-wise basis and added to the resized input image (which has just resized using the patch-wise interpolation module)
- **Parent context**: The learning strategy is implemented, following Algorithm 1

### R234: When training a model using the SSM method, the resized inpu...
- **Rubric ID**: fa5b099d-814a-4a0f-a5fb-c13522e80285
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: When training a model using the SSM method, the resized input image (with the masked pattern added) is fed into the pretrained model
- **Parent context**: The learning strategy is implemented, following Algorithm 1

### R235: When training a model using the SSM method, the predicted la...
- **Rubric ID**: 00b9d128-545c-4ed3-b493-2200bbd21fa7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When training a model using the SSM method, the predicted label from the pre-trained model is mapped using the computed iterative label mapping
- **Parent context**: The learning strategy is implemented, following Algorithm 1

### R236: When training a model using the SSM method, the pattern and...
- **Rubric ID**: 2ec1cff4-ac72-44af-9033-08232cca5f92
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When training a model using the SSM method, the pattern and parameters of the CNN mask generator are updated through gradient descent
- **Parent context**: The learning strategy is implemented, following Algorithm 1

### R237: The Shared-pattern VR variant (aka. "only $\delta$") is impl...
- **Rubric ID**: 4ab4e8e2-9fe0-41bd-8f53-6950e8230b23
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The Shared-pattern VR variant (aka. "only $\delta$") is implemented by defining visual reprogramming as $f_\text{in}(x_i)=r(x_i)+\delta$, where $r$ is bilinear interpolation, i.e., no masking is used
- **Parent context**: The SMM variants for the "Impact of Masking" subsection have been implemented

### R238: The sample-specific pattern without masking variant (aka. "o...
- **Rubric ID**: b525d390-b25f-4635-b848-dbd5845c0a67
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The sample-specific pattern without masking variant (aka. "only $f_{mask}$") is implemented by defining visual reprogramming as $f_\text{in}(x_i)=r(x_i)+f_\text{mask}(r(x_i))$ where $r$ is bilinear interpolation, i.e., no pattern is used
- **Parent context**: The SMM variants for the "Impact of Masking" subsection have been implemented

### R239: The Single-channel version of SMM variant (aka. "Single-Chan...
- **Rubric ID**: 647e8cc8-d90f-43f5-8ff1-6d24d5cce58c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The Single-channel version of SMM variant (aka. "Single-Channel $f_\text{mask}^s$") is implemented by implementing VR as $f_\text{in}(x_i)=r(x_i)+\delta \odot f_\text{mask}(r(x_i))$, i.e., a single-channel version of SMM is used, averaging the penultimate-layer output of the mask generator
- **Parent context**: The SMM variants for the "Impact of Masking" subsection have been implemented

### R240: The embeddings of the randomly selected samples in the train...
- **Rubric ID**: dcc68c79-615d-4951-8eed-56ecf9153dce
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The embeddings of the randomly selected samples in the training sets of the SVHN and EuroSAT datasets are computed using ResNet-18
- **Parent context**: The experiments under the "Feature Space Visualization Results" subsection have been executed

### R241: The embeddings of the randomly selected samples in the train...
- **Rubric ID**: 9e037051-8d0b-422f-99aa-185da29ffb2a
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The embeddings of the randomly selected samples in the training sets of the SVHN and EuroSAT datasets are computed using the "Pad" reprogramming method, with ResNet-18 as the pre-trained model
- **Parent context**: The embeddings of the randomly selected samples in the training sets of the SVHN and EuroSAT dataset...

### R242: The embeddings of the randomly selected samples in the train...
- **Rubric ID**: ca6af6fc-70fe-4dda-a146-9b4eb409591b
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The embeddings of the randomly selected samples in the training sets of the SVHN and EuroSAT datasets are computed using the "Narrow" reprogramming method, with ResNet-18 as the pre-trained model
- **Parent context**: The embeddings of the randomly selected samples in the training sets of the SVHN and EuroSAT dataset...

### R243: The embeddings of the randomly selected samples in the train...
- **Rubric ID**: 5691f99a-0131-4429-b37c-cdd7ca59a643
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The embeddings of the randomly selected samples in the training sets of the SVHN and EuroSAT datasets are computed using the "Medium" reprogramming method, with ResNet-18 as the pre-trained model
- **Parent context**: The embeddings of the randomly selected samples in the training sets of the SVHN and EuroSAT dataset...

### R244: The embeddings of the randomly selected samples in the train...
- **Rubric ID**: 6f88164d-6b79-4a95-8894-d180f7a69789
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The embeddings of the randomly selected samples in the training sets of the SVHN and EuroSAT datasets are computed using the "Full" reprogramming method, with ResNet-18 as the pre-trained model
- **Parent context**: The embeddings of the randomly selected samples in the training sets of the SVHN and EuroSAT dataset...

### R245: The embeddings of the randomly selected samples in the train...
- **Rubric ID**: a8339d1b-0b94-4cf7-99f8-1e76f33d25c4
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The embeddings of the randomly selected samples in the training sets of the SVHN and EuroSAT datasets are computed using the SMM ("Ours") reprogramming method, with ResNet-18 as the pre-trained model
- **Parent context**: The embeddings of the randomly selected samples in the training sets of the SVHN and EuroSAT dataset...

## Experimental Setup

### R246: For the Pad baseline, cross-entropy loss is computed between...
- **Rubric ID**: 2f60699e-e7ed-481b-b151-01ba070f0a9a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Pad baseline, cross-entropy loss is computed between the predicted labels and the target labels
- **Parent context**: The Pad baseline has been implemented, where the original image is centered then the noise pattern i...

### R247: For the Pad baseline, only the noise pattern is updated thro...
- **Rubric ID**: 49822754-dac4-45aa-802f-101732638dce
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Pad baseline, only the noise pattern is updated through gradient descent
- **Parent context**: The Pad baseline has been implemented, where the original image is centered then the noise pattern i...

### R248: For the Medium baseline, cross-entropy loss is computed betw...
- **Rubric ID**: 67c77561-a6e0-4f29-aa3a-572b8ca05390
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Medium baseline, cross-entropy loss is computed between the predicted labels and the target labels
- **Parent context**: The Medium baseline has been implemented, which adds a mask being a quarter of the size of watermark...

### R249: When training a model using the SSM method, the parameters o...
- **Rubric ID**: 613293bb-9868-458a-98bb-eb25b05ef5f7
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: When training a model using the SSM method, the parameters of the CNN mask generator are initialized randomly
- **Parent context**: The learning strategy is implemented, following Algorithm 1

### R250: When training a model using the SSM method, the pattern $\de...
- **Rubric ID**: d032889a-bbe7-4d7b-a912-195f277c3566
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: When training a model using the SSM method, the pattern $\delta$ is initialized to zeros
- **Parent context**: The learning strategy is implemented, following Algorithm 1

### R251: The Pad, Narrow, Medium and Full baselines are trained with...
- **Rubric ID**: e1b7d56c-f670-444e-86ea-011fad9c1c97
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The Pad, Narrow, Medium and Full baselines are trained with an initial learning rate of 0.01
- **Parent context**: The hyperparameters for the Pad, Narrow, Medium and Full baselines have been implemented

### R252: The Pad, Narrow, Medium and Full baselines are trained with...
- **Rubric ID**: c19f72e5-3023-4ab6-9435-9a87058406d2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The Pad, Narrow, Medium and Full baselines are trained with a learning rate decay of 0.1, which is applied on the 100th and 145th epochs
- **Parent context**: The hyperparameters for the Pad, Narrow, Medium and Full baselines have been implemented

### R253: The Pad, Narrow, Medium and Full baselines are trained for t...
- **Rubric ID**: 23394dfb-c8f2-4f59-b760-3c4df5532ca2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The Pad, Narrow, Medium and Full baselines are trained for two hundred epochs
- **Parent context**: The hyperparameters for the Pad, Narrow, Medium and Full baselines have been implemented

### R254: The Pad, Narrow, Medium and Full baselines trained on any of...
- **Rubric ID**: 0e394886-4be0-4413-a051-9fb926330dd3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The Pad, Narrow, Medium and Full baselines trained on any of the CIFAR10, CIFAR100, SVHN, GTSRB, FLOWERS102, UCF101, FOOD101, SUN397, EUROSAT datasets use a batch size of 256
- **Parent context**: The hyperparameters for the Pad, Narrow, Medium and Full baselines have been implemented

### R255: The Pad, Narrow, Medium and Full baselines trained on either...
- **Rubric ID**: ff567973-3773-46fc-8c25-afa9d193097d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The Pad, Narrow, Medium and Full baselines trained on either of the DTD and OXFORDPETS datasets use a batch size of 64
- **Parent context**: The hyperparameters for the Pad, Narrow, Medium and Full baselines have been implemented

### R256: All ResNet models trained on any of the CIFAR10, CIFAR100, S...
- **Rubric ID**: 87b4dcc3-ae76-4d29-b521-8374efd8e1ab
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All ResNet models trained on any of the CIFAR10, CIFAR100, SVHN, GTSRB, FLOWERS102, UCF101, FOOD101, SUN397, EUROSAT datasets use a batch size of 256, initial learning rate of 0.01 and learning-rate decay of 0.1
- **Parent context**: The dataset-specific hyperparameters for SSM have been implemented correctly

### R257: All ResNet models trained on either the DTD or OXFORDPETS da...
- **Rubric ID**: 2ac32251-5599-4888-9ad1-4be5532e7447
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All ResNet models trained on either the DTD or OXFORDPETS dataset use a batch size of 64, initial learning rate of 0.01 and learning-rate decay of 0.1
- **Parent context**: The dataset-specific hyperparameters for SSM have been implemented correctly

### R258: All ViT models trained on any of the CIFAR10, CIFAR100, SVHN...
- **Rubric ID**: 7799ad6e-56a5-43c5-958d-6bc0ad6c9f4b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All ViT models trained on any of the CIFAR10, CIFAR100, SVHN, GTSRB, FLOWERS102, UCF101, FOOD101, SUN397, EUROSAT datasets use a batch size of 256, initial learning rate of 0.001 and learning-rate decay of 1
- **Parent context**: The dataset-specific hyperparameters for SSM have been implemented correctly

### R259: All ViT models trained on either the DTD or OXFORDPETS datas...
- **Rubric ID**: 81fdf891-093d-4879-87a9-0fe1c97a5213
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All ViT models trained on either the DTD or OXFORDPETS dataset use a batch size of 64, initial learning rate of 0.001 and learning-rate decay of 1
- **Parent context**: The dataset-specific hyperparameters for SSM have been implemented correctly

### R260: Unless otherwise stated, the patch size for SSM is set to $2...
- **Rubric ID**: a27fe007-59e6-4ccd-a8c0-1eb856cfe9ed
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Unless otherwise stated, the patch size for SSM is set to $2^l$ where $l$ is the number of max-pooling layers
- **Parent context**: The hyperparameters for SSM have been implemeneted

### R261: When training models with the SSM method, if a learning rate...
- **Rubric ID**: 913baecd-873f-4fe9-a701-99ed55502290
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: When training models with the SSM method, if a learning rate decay that isn't 1 is used, the learning rate scheduler applies the decay factor on the 100th and 145th epochs
- **Parent context**: The hyperparameters for SSM have been implemeneted

### R262: Using the "Pad" reprogramming method, ResNet-18 (pre-trained...
- **Rubric ID**: 780ff552-bbe9-4d3d-bb73-bc704acd4a6a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R263: Using the "Narrow" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 6b70962f-569c-4526-897d-66f07d70264a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R264: Using the "Narrow" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 0b93529d-971a-47ec-a6b1-1eab09d5577d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R265: Using the "Narrow" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 854a61a6-8efd-460c-b801-f4aa7e8f058d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R266: Using the "Narrow" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: a0666b7f-f5a4-4210-bfa2-e94baeaa3f9d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R267: Using the "Narrow" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 5e68176b-47e9-46cc-bb67-a4c909ecd762
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R268: Using the "Narrow" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 67ee77ae-e13b-459f-ac99-ff9ab3889a19
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R269: Using the "Medium" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: b6e34e59-9b30-48d0-9d67-e0b73209eeed
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R270: Using the "Medium" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: a1104084-44e6-431b-83fd-a3ff16203159
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R271: Using the "Medium" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 5f73fbf7-a070-4fee-beeb-74960688368c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R272: Using the "Medium" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: c4b92a9c-4961-42a7-98d6-c7c9ac993847
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R273: Using the "Medium" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 5c66af9c-cc0c-41ca-8417-550bb4b931a4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R274: Using the "Medium" reprogramming method, ResNet-18 (pre-trai...
- **Rubric ID**: 5b3bc88a-1aa8-4bcb-aad7-7f9a0b9e2fd2
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R275: Using the "Full" reprogramming method, ResNet-18 (pre-traine...
- **Rubric ID**: e59d6acb-ad45-4e95-bdb6-727bc2d5ed03
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R276: Using the "Full" reprogramming method, ResNet-18 (pre-traine...
- **Rubric ID**: 80bcba6f-a09f-4907-a871-bc461da20a16
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R277: Using the "Full" reprogramming method, ResNet-18 (pre-traine...
- **Rubric ID**: ce5a7f07-8650-47e2-9271-4052061201e0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R278: Using the "Full" reprogramming method, ResNet-18 (pre-traine...
- **Rubric ID**: c42da8be-4177-4372-bba2-dd8d50e24358
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R279: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 14755d1a-a325-4c39-ac0b-c35b8fc4a69b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R280: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 468a2a76-7ffc-48aa-bcec-0cb2946f623b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R281: Using the "Pad" reprogramming method, ResNet-50 (pre-trained...
- **Rubric ID**: 2fba687d-b9ce-4dcc-b8d8-84197538ce1b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R282: Using the "Pad" reprogramming method, ResNet-50 (pre-trained...
- **Rubric ID**: 10f5e67c-a065-408d-a72b-1e6bd54cf2a0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R283: Using the "Pad" reprogramming method, ResNet-50 (pre-trained...
- **Rubric ID**: 9a2fb5fe-926d-47a9-a73c-7724ced34915
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R284: Using the "Narrow" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: c0fc1fa5-ece1-44fc-a8c8-9b7616761cef
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R285: Using the "Narrow" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: 9559594d-ce98-446a-8593-000786a69af6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R286: Using the "Medium" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: 24039560-d8bb-4afd-9a95-c7287791d21c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R287: Using the "Medium" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: 0bba9e2e-f524-447e-84ed-16b002d98244
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R288: Using the "Medium" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: 3301b18f-c642-40e0-9cad-afdce9c4f637
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R289: Using the "Medium" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: 3450328c-0773-4325-b8f8-0c32ba0279a3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R290: Using the "Medium" reprogramming method, ResNet-50 (pre-trai...
- **Rubric ID**: 41d6bccb-cff7-4bdd-98fb-300a56b0977e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned ...

### R291: Using the "Full" reprogramming method, ResNet-50 (pre-traine...
- **Rubric ID**: 0b4fe8c3-0306-40aa-82dd-a8351b3eb7ac
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R292: Using the "Full" reprogramming method, ResNet-50 (pre-traine...
- **Rubric ID**: d655c4ad-e3e9-44f4-980a-a5d5920baa26
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R293: Using the "Full" reprogramming method, ResNet-50 (pre-traine...
- **Rubric ID**: dcd5d8f4-6feb-49df-b62e-fe88e29ff552
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R294: Using the SNS method ("Ours"), ResNet-50 (pre-trained on Ima...
- **Rubric ID**: 6c15c084-aac0-449f-8605-d1c5dc358014
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R295: Using the SNS method ("Ours"), ResNet-50 (pre-trained on Ima...
- **Rubric ID**: 6e482102-b67f-4e1c-a8a7-15445abf75bf
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R296: Using the SNS method ("Ours"), ResNet-50 (pre-trained on Ima...
- **Rubric ID**: 7a933ee3-2907-4780-b739-cdc4d55629a5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-50 (pre-trained on ImageNet-1K) has been fine-tuned on ...

### R297: Using the "Pad" reprogramming method, ViT-B32 (pre-trained o...
- **Rubric ID**: 7dc555f2-f658-4371-83e1-9d282611b244
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R298: Using the "Pad" reprogramming method, ViT-B32 (pre-trained o...
- **Rubric ID**: 61528951-e962-4356-950d-ea9b19205418
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Pad" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R299: Using the "Narrow" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: d3de71e0-6ea5-4d62-8445-c6cbc548812b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR10 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R300: Using the "Narrow" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: 143eeb00-fb65-45cf-8cc8-abf6d889e89f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the GTSRB dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R301: Using the "Narrow" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: e37ef9d5-0d92-413b-8be5-4d721666d043
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R302: Using the "Narrow" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: b8eb525b-553b-4b4a-bb0e-6906c3b570a7
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Narrow" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R303: Using the "Medium" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: 2966827f-f671-4cfe-ae2c-010fef9c2c43
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R304: Using the "Medium" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: e0ac3242-11cb-4f2f-9e79-28ecb4b275de
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R305: Using the "Medium" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: b923fa20-f96a-4615-9b63-d40cb2264347
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R306: Using the "Medium" reprogramming method, ViT-B32 (pre-traine...
- **Rubric ID**: 5c925894-e2f0-4eee-83bc-f3a81dc08af8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Medium" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on...

### R307: Using the "Full" reprogramming method, ViT-B32 (pre-trained...
- **Rubric ID**: 00425b26-1080-4365-b1da-8585ab59848f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on t...

### R308: Using the "Full" reprogramming method, ViT-B32 (pre-trained...
- **Rubric ID**: 430082f8-6cee-428a-a969-2b16fb27031e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SUN397 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on t...

### R309: Using the "Full" reprogramming method, ViT-B32 (pre-trained...
- **Rubric ID**: af3101ed-66b0-4eaf-b328-578722fea0c6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Full" reprogramming method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on t...

### R310: Using the SNS method ("Ours"), ViT-B32 (pre-trained on Image...
- **Rubric ID**: c506baff-8a3f-42a6-92b9-9bb590d7223a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R311: Using the SNS method ("Ours"), ViT-B32 (pre-trained on Image...
- **Rubric ID**: 79f4440d-1313-4660-aca0-d49f177b173f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed. Here, ViT-B32 is trained with an initial learning rate of 0.01 and learning rate decay of 0.1
- **Parent context**: Using the SNS method ("Ours") method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R312: Using the SNS method ("Ours"), ViT-B32 (pre-trained on Image...
- **Rubric ID**: 46ce4412-102f-44c6-b900-cf7043c63c11
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on th...

### R313: The recorded metrics show that SMM, trained with the ViT ver...
- **Rubric ID**: 254a0ee2-b82d-4370-8a08-383fd1e63c47
- **Category**: Result Analysis / Experimental Setup
- **Weight**: 1
- **Requirement**: The recorded metrics show that SMM, trained with the ViT version with an initial learning rate of 0.01 and learning rate decay of 0.1, achieves the best accuracy on the UFC101 dataset compared to all other input reprogramming methods
- **Parent context**: The results under the "Results on ViT" subsection have been replicated

### R314: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (...
- **Rubric ID**: 01b09996-0e4d-49f5-b4ba-4fac65b3364c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fin...

### R315: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (...
- **Rubric ID**: ca6cd119-552d-4d7c-80cc-aef42d6fa342
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fin...

### R316: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (...
- **Rubric ID**: 4f62b012-fa80-4899-8adb-9e7f240203dc
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fin...

### R317: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (...
- **Rubric ID**: 5ddba7bd-23ff-4b0f-9569-9b04d6261abe
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fin...

### R318: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (...
- **Rubric ID**: 12d6d708-4740-44c9-82b8-9c31f3026ef7
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the UCF101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fin...

### R319: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (...
- **Rubric ID**: 82737700-10b7-44d7-a158-eec43ddc8254
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the OXFORDPETS dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "Shared-pattern VR variant" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fin...

### R320: Using the "sample-specific pattern without masking" SMM vari...
- **Rubric ID**: d5023250-623b-4979-a8e3-11337668ad3b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K...

### R321: Using the "sample-specific pattern without masking" SMM vari...
- **Rubric ID**: 3c7a8443-b6cf-4317-be07-b9cb4cf0cc20
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K...

### R322: Using the "sample-specific pattern without masking" SMM vari...
- **Rubric ID**: b7f5c413-0c1d-4192-ab41-c9a8b1d1e2b1
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K...

### R323: Using the "sample-specific pattern without masking" SMM vari...
- **Rubric ID**: 5060ba82-8c58-46b5-8ceb-28405ca04ccb
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "sample-specific pattern without masking" SMM variant, ViT-B32 (pre-trained on ImageNet-1K...

### R324: Using the "The Single-channel version of SMM" variant, ViT-B...
- **Rubric ID**: ccc82fe7-9338-463b-994e-34e08182ad99
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the SVHN dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been...

### R325: Using the "The Single-channel version of SMM" variant, ViT-B...
- **Rubric ID**: e9030090-75a9-4752-8f93-fe062f303b8a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the DTD dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been...

### R326: Using the "The Single-channel version of SMM" variant, ViT-B...
- **Rubric ID**: c603cb34-a59b-4d93-bed3-5c67784e9311
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been fine-tuned on the train split of the FOOD101 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the "The Single-channel version of SMM" variant, ViT-B32 (pre-trained on ImageNet-1K) has been...

### R327: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 336893af-7dcb-4791-8cf6-40bbf4f57083
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 1 (i.e. the mask generator has zero max-pooling layers) has been fine-tuned on the train split of the CIFAR100 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 1 (i.e....

### R328: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 75c8bfe3-6502-478e-8d27-eace694ba330
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 1 (i.e. the mask generator has zero max-pooling layers) has been fine-tuned on the train split of the FLOWERS102 dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 1 (i.e....

### R329: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 79d207fe-1f04-4462-a311-b67a5911e7ef
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 4 (i.e. the mask generator has two max-pooling layers) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 4 (i.e....

### R330: Using the SNS method ("Ours"), ResNet-18 (pre-trained on Ima...
- **Rubric ID**: 002ff71b-c421-43af-b49c-09f3bf6d3177
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Using the SNS method ("Ours"), ResNet-18 (pre-trained on ImageNet-1K) with patch size 16 (i.e. the mask generator has four max-pooling layers) has been fine-tuned on the train split of the EUROSAT dataset, then the accuracy at the end of training on the test split is recorded. This is repeated three times with three unique seeds, and the mean and standard deviation of the test accuracy is computed
- **Parent context**: Using the SNS method ("Ours") method, ResNet-18 (pre-trained on ImageNet-1K) with patch size 16 (i.e...

## Logging, Analysis & Presentation

### R331: tSNE is applied to the embeddings to project the embeddings...
- **Rubric ID**: 9d2a4385-abc9-415e-901a-6993b2963de0
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: tSNE is applied to the embeddings to project the embeddings to 2 dimensions
- **Parent context**: The experiments under the "Feature Space Visualization Results" subsection have been executed
