# Rubric Requirements — what-will-my-model-forget
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 921

## Data Processing & Preparation

### R01: Code has been implemented for creating the pre-training data...
- **Rubric ID**: f1d4b756-ea03-4caa-8e74-50883d9d8960
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been implemented for creating the pre-training dataset $D_{PT}$ so that it is composed of 36 tasks from the training split of the Public Pool of Prompts (P3) dataset.
- **Parent context**: Code has been implemented for creating the the pre-training dataset $D_{PT}$, as described in Sectio...

### R02: Code has been implemented for creating the pre-training data...
- **Rubric ID**: fdf8791a-22a1-493c-a399-c9702d753196
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been implemented for creating the pre-training dataset $D_{PT}$, such that each task in the pre-training dataset $D_{PT}$ will contain 100 examples randomly drawn from the original task in the P3 train split.
- **Parent context**: Code has been implemented for creating the the pre-training dataset $D_{PT}$, as described in Sectio...

### R03: The pre-training dataset $D_{PT}$ has been created such that...
- **Rubric ID**: 475b2e49-6ecc-4f44-a240-c6edc0dcdb60
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The pre-training dataset $D_{PT}$ has been created such that it contains 36 tasks from the training split of the Public Pool of Prompts (P3) dataset.
- **Parent context**: The pre-training dataset $D_{PT}$ has been created, as described in Section 4.1 Training and Evaluat...

### R04: The pre-training dataset $D_{PT}$ has been created such that...
- **Rubric ID**: a18c17c2-7e04-479c-a021-63b57e774ea7
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The pre-training dataset $D_{PT}$ has been created such that each task in the pre-training dataset $D_{PT}$ contains 100 examples randomly drawn from the original task in the P3 train split.
- **Parent context**: The pre-training dataset $D_{PT}$ has been created, as described in Section 4.1 Training and Evaluat...

### R05: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: d39373af-6169-4000-9887-434bd2c6bc29
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R06: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 518dc07d-5fd9-49e4-ba93-78347a4a50cc
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R07: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 513eae23-b191-4b6c-940b-70ad0d36e6e6
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R08: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 58d951f8-8873-4b3e-9312-e74454af14aa
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R09: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 4ce74906-994c-49cc-a9a2-3b809ae66650
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R10: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: ae26b638-4880-4336-8bb0-91868c792323
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R11: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 495b2f92-044b-467f-9484-bcb55bf14b40
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R12: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 6572edc0-4120-468a-b153-4cd16d588c3f
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R13: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 45637175-8a67-4482-bfd5-a7a6ffdb5b38
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R14: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 94650465-a011-42d8-92df-f6914a5e26f5
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R15: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: e8e80750-6feb-47ab-bccb-b4a023d49c5a
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R16: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 0df21893-b2f4-433d-a8c4-24ed26f4322a
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R17: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 7ae76633-2044-4458-811a-631799f27b9d
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R18: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 6e80a2b0-5d99-444d-9736-b09fac2951ca
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R19: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: bceed80b-62fc-47ad-9318-a50eecfef62b
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R20: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 66563e30-bf2c-4842-a3fa-9604a4aeb26b
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R21: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 8d872a02-e4b3-4633-a46a-ece418a5aed1
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R22: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: c1ca4fce-0b03-4294-9309-171d5610187d
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R23: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 9b7b723d-1152-4e88-8469-cbad0874906b
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R24: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: ecbcf181-5941-4b18-9f5d-acf94218542f
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R25: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 82bfcff1-66af-4061-ad13-5da6f0895880
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R26: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 5c5ef034-4795-4174-9622-bdbe61c5b0c0
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R27: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 1132c8b2-d890-45f6-9097-9370de47b867
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R28: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: daa9b56e-a4da-44d9-b6e9-a128c7b6b8cc
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R29: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: a834f0ee-e1ad-4936-b660-16fe0297ca4c
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R30: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 8a250fa7-c9aa-4639-895f-252b44e3137e
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R31: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: ebb8ca52-cab8-4b1f-b5d3-2cb8e689f3a9
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R32: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: e53b2542-905b-49a0-8bad-266ee66ad0fb
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R33: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: d6e9c182-de66-4400-a811-0a376c2cdddf
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R34: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: e969ba1d-2310-4e02-b731-95ae1278a6b0
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R35: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 351f4a92-3819-48bc-b5e5-87cfe8b64683
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R36: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 8d18730b-f63c-4c73-8a08-027185b4f4f0
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R37: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 9af8ec57-42b4-4c87-812b-dbf7929ee347
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R38: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: fb53b556-bbaf-4331-b84f-2da103b1b4cc
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R39: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 79d46f4d-0fd9-49c9-b0a5-bb60e238017f
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R40: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 2b7a75ff-d655-455d-90fd-a8dfb72d1f88
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R41: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 8643827f-c673-445a-a9a7-f5b756b33b73
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$ sets for each model.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using the BART0_{...

### R42: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 8c442be2-44bb-4357-b68f-c0c016a4f38d
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R43: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 5ea077d2-a232-4f30-aab9-54b8ae2849e9
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting models using the FLAN-T5_...

### R44: The code is implemented such that The P3-Test_{ID} dataset w...
- **Rubric ID**: e46e7287-50d4-4dc7-a09c-5d36be43d814
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The code is implemented such that The P3-Test_{ID} dataset will be comprised of the test splits of the SuperGlue-Cb, SuperGlue-RTE, SuperGLUE-wsc.fixed, SuperGlue-Copa and SuperGlue-wic tasks from the P3 dataset.
- **Parent context**: Code for splitting the P3-test dataset into ID and OOD splits has been implemented as outlined in Ap...

### R45: The code is implemented such that The P3-Test_{OOD} dataset...
- **Rubric ID**: ff13f96a-93b0-4ddb-975c-83801cef3d04
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The code is implemented such that The P3-Test_{OOD} dataset will be comprised of the test splits of the storycloze, hellaswag, anli, winograde-xl tasks from the P3-Test dataset.
- **Parent context**: Code for splitting the P3-test dataset into ID and OOD splits has been implemented as outlined in Ap...

### R46: The P3-Test dataset has been split into P3-Test_{ID} and P3-...
- **Rubric ID**: 4d8e4aee-6396-4c20-bbdf-0e02b221200b
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The P3-Test dataset has been split into P3-Test_{ID} and P3-Test_{OOD} as outlined in Appendix B
- **Parent context**: The P3-Test dataset has been split into P3-Test_{ID} and P3-Test_{OOD}.

### R47: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: e9eff70e-ac4a-48cb-ac7e-bed44f46e894
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R48: The $D_R^{train}$, $D_R^{test}$ and $D_{PT}$ datasets requir...
- **Rubric ID**: 3412d69e-7222-40a0-8242-40c1e7873887
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The $D_R^{train}$, $D_R^{test}$ and $D_{PT}$ datasets required for Table 2 have been generated.
- **Parent context**: Table 2 has been replicated.

### R49: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 1f66b2ac-671d-47e6-bfbf-6437c6dcbc84
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$ sets for each model.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using the BART0_{...

### R50: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 99eaaaab-a67e-4a6e-92c7-84ca0d36ce12
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R51: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 2683217b-36ff-4705-8c80-ef7ede72a9ae
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R52: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: b438aa30-a3f5-417e-87f4-84956873d1b3
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R53: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: a5548411-bffa-40f4-a42f-d350bf3ce69c
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R54: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 606271fc-a62a-42db-b853-1fc49f8359fc
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R55: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: e6b02e2a-3f62-4602-b2b1-f6b20740410c
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R56: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: c82809a1-43fd-45c9-99d7-681e6f2514b0
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R57: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: cdc0bef9-33b7-491c-95b8-f55e634529dd
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R58: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: f574efa9-32c5-4e33-9516-ba64caa4d6a2
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R59: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 52abd1e0-c955-4065-bc36-b547a1c1a169
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R60: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 9e5d1fcd-c2ed-4b8e-9c70-8349086f35bc
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R61: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 9fe7a706-378b-4921-b6aa-d4ebf6c459f1
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R62: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 48cab4ad-b260-4296-8ca9-90c6e6bdaffe
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R63: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 9f8efde4-36e8-4749-b529-2421d8ea29f0
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R64: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 454f3aef-a03e-49e4-a3a8-07ed0183e002
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R65: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 9e6f46f4-e2ad-4fde-a8e8-ab3ef4b628ee
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R66: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 31cd0913-6846-4d5d-9b54-6a0eaab73eff
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R67: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 07590ff9-4b3f-4ff8-a519-8463dea005c9
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R68: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 98f4860d-5b49-40fe-abae-fccd8f089402
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R69: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: c7f80e89-df0c-47ef-b268-a2b40794462d
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R70: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 9533e06e-3634-47a7-8d61-40f7286a8014
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R71: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: f4377bcf-26a0-4fab-af22-8c56d8c832d1
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R72: Code has been written to generate predictions on the validat...
- **Rubric ID**: 0501cd6e-c133-4027-9040-0672abe35d43
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R73: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 42c416bf-38e1-40a2-82f2-7f18e8eb001d
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R74: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: c42e6e55-1550-4d7d-9f5b-fee69713c9fa
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R75: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 75041314-266e-4ed6-90ad-163190ff095b
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R76: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 0e28a1a3-712b-422b-b84f-84cb662d3fb9
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R77: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 8ad4e41b-030e-4283-bd14-9dd7ba970301
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R78: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 158418f0-40ff-4ebc-a072-6dd72614943c
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R79: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: db938e71-f9e7-44fe-a2f5-3c542c083a14
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R80: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 342d1ed2-c69a-4dee-8bda-a1d6250ac4b9
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$ sets for each model.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using the BART0_{...

### R81: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 42ba7af8-3bfc-4e80-a8f9-d8edc0b64cc4
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R82: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 7aa7c91c-5cbc-42c1-b5aa-d2af93047d9c
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R83: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: d11da858-c6c4-49e3-84e2-e2203b45ec17
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R84: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 22a97dd7-8817-42b2-b51b-860d6b2896ec
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R85: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 426589e8-ff98-4b41-adfb-a360844a59b0
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R86: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 38623980-a419-4621-babc-bb86aa83e56a
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R87: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 03ac19ca-e14b-438a-932b-578d26724027
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R88: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 4a967984-7ade-44f8-9f2b-3ae2af26c14d
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R89: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 385796d8-8e14-4896-9260-6b325bc6ec8e
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R90: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: bb0a0dc1-edd9-47b7-b0ac-fb6a9d42c28d
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R91: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 3e2b0834-78c0-4a21-917f-7f2f0735b894
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R92: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 91f1f81b-0411-40dc-87d9-aa00a9db5606
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R93: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 9a9edddc-5e5a-433f-9823-60f061a9bcf9
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R94: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: b2238091-5d3b-455b-a6b5-3de077e16953
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R95: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: bb69d029-d191-40a2-8bee-dd0359df405f
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R96: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 8730d8e9-7b86-4094-987b-cec8d3dea05f
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R97: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: ec19d48f-7ffa-4e13-9d33-9334dfa12ea7
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R98: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 2e580624-21b2-4771-9aa5-9bd2ca599ec1
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R99: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 0ffcba46-8475-424a-a889-18359f126acd
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R100: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 50fcef9c-1d5c-4dad-9557-081118ebdcfc
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R101: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 842aee24-daba-4157-96f9-67e8f8b6694e
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R102: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 8b44b1c3-e6c8-43cb-a899-36528f4b3288
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R103: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 7c5f399a-97d1-42f7-8ad2-96cd1f48fc31
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R104: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: cde3dd3b-b3fd-4603-963d-83365b0a55b5
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R105: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 0299f2d6-ed24-4207-a225-122e7e1d65de
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using FLAN-T5_{Large},...

### R106: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 5f1b7c13-edaf-40b7-a01a-5dba31ced398
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R107: $D_R$ is randomly split into 60% and 40% subsets to create t...
- **Rubric ID**: 4b64643c-ec15-4831-961f-de4134258d69
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: $D_R$ is randomly split into 60% and 40% subsets to create the $D^{Train}_R$ and $D^{Test}_R$.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

## Dataset and Model Acquisition

### R108: The 36 tasks used are: glue-mrpc, glue-qqp, paws_x-en, kilt_...
- **Rubric ID**: afd0d576-03ab-4108-8cf4-dff15a649c1e
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The 36 tasks used are: glue-mrpc, glue-qqp, paws_x-en, kilt_tasks-hotpotqa, wiki_qa, adversarial_qa-dbert, adversarial_qa-dbidaf, adversarial_qa-droberta, duorc-SelfRC, duorc-ParaphraseRC, ropes, quoref, cos_e-v1.11, cosmos_qa, dream, qasc, quail, quartz, sciq, social_i_qa, wiki_hop-original, wiqa, amazon_polarity, app_reviews, imdb, rotten_tomatoes, yelp_review_full, common_gen, wiki_bio, cnn_dailymail-3.0.0, gigaword, multi_news, samsum, xsum, ag_news and dbpedia_14.
- **Parent context**: Code has been implemented for creating the the pre-training dataset $D_{PT}$, as described in Sectio...

### R109: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 504a0bf7-45f2-49ff-ad24-7fa7f07af414
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R110: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: d48f8290-dd41-4d50-a106-f78a50ffbf2b
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R111: The original validation split of the MMLU dataset containing...
- **Rubric ID**: ec2c9cc9-f548-4a96-bb29-a101c4cf5e8a
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R112: The original validation split of the MMLU dataset containing...
- **Rubric ID**: c1f669b6-9ea1-478d-904a-43c83d4f70e9
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R113: The original validation split of the MMLU dataset containing...
- **Rubric ID**: cb7888cf-5902-40e9-8dd8-3fb6a0360f35
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R114: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 374d8588-f266-4c29-8154-678c7122ccaf
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R115: The original validation split of the MMLU dataset containing...
- **Rubric ID**: e795de8f-f158-4648-8cd5-ec9b4a6bda14
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R116: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 98ad5974-b78d-467c-9d91-5621347bb21e
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R117: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 43bf6604-8bb0-4fc8-b809-a2aa00e73d6d
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R118: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 4a8cd2ef-f3e3-4d32-8ed3-392e66816865
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R119: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 97a86919-cf1f-4dc4-9d80-71304535b021
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R120: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 4b6ee1a9-a50c-4866-8f0b-ee130cb73b09
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R121: The original validation split of the MMLU dataset containing...
- **Rubric ID**: fb8a9377-8b96-47b0-9720-df82f7baddb4
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R122: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 787b5787-4491-41a7-8ee0-db24ef65fb41
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R123: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 4344d14e-d49f-41b1-80be-c4bd7495cb42
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R124: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 79469f47-610a-4024-9bda-e0bdb2d53e02
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R125: The original validation split of the MMLU dataset containing...
- **Rubric ID**: c4919796-190a-42dc-b51a-d9277dc1baa4
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R126: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 74178f66-e84b-4551-8e28-817fbda60012
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R127: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 1a0450ac-48a1-471a-ab1a-01d936fabe8a
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R128: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 8a0852c0-879c-4c01-baf1-c1ae5dde4ecd
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R129: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 9e78c5c1-8224-48e9-b285-264f140c7d68
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R130: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 025df226-c25d-4516-914a-bb4d721e8f5e
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R131: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 8a8e2979-3a7b-4f2a-a366-8721b2170612
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R132: The original validation split of the MMLU dataset containing...
- **Rubric ID**: e3b6de07-7775-4dd7-9380-ab321b356aa7
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R133: The original validation split of the MMLU dataset containing...
- **Rubric ID**: b173c0cf-7768-4a82-a697-ddf5f14a450b
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R134: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 3f7d8e6a-d551-46ea-aa90-c5f5c78ca790
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R135: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 8f819b53-2278-461b-8d5f-e99f8cc1c81d
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R136: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 1b552c52-6051-47be-bf19-4029438e4a2c
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R137: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 7c4e38d6-a926-4ffe-87ca-ffeb6fd3637d
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R138: The original validation split of the MMLU dataset containing...
- **Rubric ID**: b23610a8-7341-4775-a23f-e20adc179f18
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R139: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 5822cb07-fb1c-4ac1-8e32-777a25eb3495
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R140: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 2c371d3a-2299-4d86-bea8-38b3514658fa
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R141: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 1f7db427-1522-4d80-9098-1ea8004c37f4
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using the FLAN-T5_{Large} and FLAN-T5_{3B} models.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using the BART0_{...

### R142: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: a2aef4a4-c7a1-47d2-b110-6af531c92547
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using the BART0_{...

### R143: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 7950e842-b097-447e-89da-95853f866cd7
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R144: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 15743e41-ab32-4723-ae12-2c03070d097a
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using the FLAN-T5_{Large} model.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting models using the FLAN-T5_...

### R145: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 1a95776d-57cd-4564-b1c5-77abe15dd78e
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using the BART0_{...

### R146: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 7200fbfb-ee3b-442c-8af2-f712dd6bbe34
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R147: The original validation split of the MMLU dataset containing...
- **Rubric ID**: cd78d042-c19a-4e41-9c17-5eae1af455db
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R148: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 11a893b4-d486-41ea-98d4-a3c5de911421
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R149: The original validation split of the MMLU dataset containing...
- **Rubric ID**: e7113085-5350-42dc-890b-9172309ff4a2
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R150: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 429895b6-1fb7-419f-96b9-c808164796de
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R151: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 58371225-3541-464a-8a6d-975a484d6f8c
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R152: The original validation split of the MMLU dataset containing...
- **Rubric ID**: b1af2da2-80e0-483a-8a90-1ecb233f48f6
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R153: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 91e103a4-d6fa-4436-871a-0d3b9706964c
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R154: The original validation split of the MMLU dataset containing...
- **Rubric ID**: d49df284-9ed0-44dd-a565-960410c7d16d
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R155: The original validation split of the MMLU dataset containing...
- **Rubric ID**: c9d9f50b-dbbc-4394-b3c1-084a493a6832
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R156: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 9ea71ea3-7fbf-44f6-a6f8-3c0083ee685b
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R157: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 1809309c-3d0c-4d29-8d71-6a266435df33
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R158: The original validation split of the MMLU dataset containing...
- **Rubric ID**: a562fafe-490a-4ab6-b5bd-8ad5ccc8cf09
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R159: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 12117f46-b620-4d97-92e7-6c85f9232c31
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R160: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 7d5cd077-656d-48d7-acfc-782573af7e77
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R161: The original validation split of the MMLU dataset containing...
- **Rubric ID**: c000edd9-c932-4d81-a6c7-4294be98c984
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R162: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 814520ce-d812-49fc-8c3c-0cc935952095
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R163: The original validation split of the MMLU dataset containing...
- **Rubric ID**: d45616c1-aae6-41d2-8a22-8717e4be8a1c
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R164: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: c362a7a9-98be-4b87-9a82-9da23296a792
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R165: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 79330a11-feb3-4e1d-a8df-4796ea8f3570
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R166: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 8a59f9aa-cf51-49b3-bbb9-bf51ac6401e3
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R167: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 2c36d8d9-e721-4514-847b-fc128dc2327c
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R168: The original validation split of the MMLU dataset containing...
- **Rubric ID**: b22c1fc7-7c17-42fd-9a9d-44095a5a223f
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using the FLAN-T5_{Large} and FLAN-T5_{3B} models.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using the BART0_{...

### R169: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 723a0e18-5032-4f29-b353-7f694d6cc8ab
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using the BART0_{...

### R170: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 0adf6d43-27a2-413d-83eb-2a3e11ea6504
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R171: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 95706f9a-ba79-439a-b1f4-fdf26e29f978
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R172: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 337defd7-d8e0-48f5-8b5a-bd7d6670d5b5
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R173: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 51471371-6849-422d-9ee6-2b16fe57e0ca
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R174: The original validation split of the MMLU dataset containing...
- **Rubric ID**: f23ac72e-7cdb-4bee-8c89-56c9afd96fd5
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R175: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 3ed6e36f-356f-4cb4-a159-e10c81009f45
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R176: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 74274053-7acd-45cf-8620-5ec2c6efb9b1
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R177: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 7ae340af-c1e1-4857-967c-06b1e179a773
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R178: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 368dfa9e-c5c8-4fb4-a4cc-de3497df619c
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R179: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 8259417d-ec41-42b0-8cf5-cffe5d4d679d
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R180: The original validation split of the MMLU dataset containing...
- **Rubric ID**: bc58f4e9-89cc-4218-a0c7-cf5e8d98dda9
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R181: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 7978c487-6781-4961-bee0-3da7eae7b9f0
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R182: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: f664c411-075a-4c04-af2a-d5eccd69a751
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R183: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 83c5901a-e5f4-4a17-8889-4eb908d32a58
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R184: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 72fe3497-e78c-4bdc-8027-b4b942537f29
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R185: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 39846858-2343-49fd-8943-cbbdeb531d6b
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R186: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 95fe8227-1007-4ff6-8f7e-f0186dadf2dd
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R187: The original validation split of the MMLU dataset containing...
- **Rubric ID**: 79ff40d0-1013-44db-b0be-f80ce85d40a8
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R188: The original validation split of the MMLU dataset containing...
- **Rubric ID**: a50afc5c-d6f0-4b01-9aad-893b5f8bbe18
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{Large}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{La...

### R189: The original validation split of the MMLU dataset containing...
- **Rubric ID**: c9831188-4982-4aca-9e8f-a18b1e6a5ccf
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

## Evaluation, Metrics & Benchmarking

### R190: Code has been written to generate predictions on the test se...
- **Rubric ID**: abb6cc09-e53c-4976-9839-b477bf5aeb5b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R191: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 71d18331-f966-4747-b448-19a92c0dd0b9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R192: Code has been written to compute the ground-truth forgetting...
- **Rubric ID**: 977c1044-ff82-4697-9669-8a6f27008fa5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the ground-truth forgetting binary indicator $z_{ij}$ by fine-tuning a copy of BART0_{Large} on each $(x_i, y_i) \in D_R^{	ext{train}}$, querying it on the $j$th sample from $\hat{D}{PT}$, and grading the output using the Exact Match score.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R193: Code has been written to query the frequency-threshold based...
- **Rubric ID**: 0744d171-bc12-49f0-b339-3664534e4822
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to query the frequency-threshold based forecasting function $g$ for every sample $(x_i, y_i) \in D_R^{test}$ and $(x_j, y_j) \in \hat{D}_{PT}$ and grade it using the Exact Match score, producing a prediction $\hat{z}_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R194: Code has been written to fine-tune a copy of BART0_{Large} o...
- **Rubric ID**: 6fa84b8c-069a-44df-a86d-9f3e1daa4c9b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune a copy of BART0_{Large} on $(x_i, y_i) \in D_R^{test}$, query it on the $j$th sample from the filtered pre-training dataset $(x_j, y_j) \in \hat{D}_{PT}$, and grade it using the Exact Match score, producing a ground-truth forgetting binary indicator $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R195: Code has been written to compute the F1-score of the frequen...
- **Rubric ID**: dcc82c9a-58ba-41d3-a02a-b1d24af29c1a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score of the frequency-threshold based forecasting function $g$ on $D_R^{test}$ using the predicted and ground-truth forgetting binary indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R196: Code has been written to generate predictions on the test se...
- **Rubric ID**: 4d08d775-2b93-4932-86c6-f7c7ce0d8702
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R197: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 1f0cccce-1a13-4996-ba6e-9326a6785f91
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R198: Code has been written to compute the ground-truth forgetting...
- **Rubric ID**: 862a28f8-5236-4dfa-a55a-0fbc6385bf70
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the ground-truth forgetting binary indicator $z_{ij}$ for all pairs $(x_i, y_i) \in D_R^{\text{train}}$ and $(x_j, y_j) \in \hat{D}_{PT}$ by evaluating the copy of BART0_{Large} fine-tuned on each $(x_i, y_i)$ on the corresponding $j$th sample from $\hat{D}_{PT}$ and grading the output using the Exact Match score.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R199: Code has been written to query the frequency-threshold based...
- **Rubric ID**: e430e631-4d78-4fd9-9df5-f6f56f33d7dd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to query the frequency-threshold based forecasting function $g$ for every sample $(x_i, y_i) \in D_R^{test}$ and $(x_j, y_j) \in \hat{D}_{PT}$ to produce a prediction $\hat{z}_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R200: Code has been written to query the copy of BART0_{Large} ful...
- **Rubric ID**: 14f81679-15fd-4bc0-bd29-033cf86300bd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to query the copy of BART0_{Large} fully fine-tuned on $(x_i, y_i) \in D_R^{test}$ on the $j^\text{th}$ sample from the filtered pre-training dataset $(x_j, y_j) \in \hat{D}_{PT}$ and graded using the Exact Match score, producing a ground-truth forgetting binary indicator $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R201: Code has been written to compute the F1-score of the frequen...
- **Rubric ID**: 592813ae-175a-4a89-a922-7db5ad124b66
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score of the frequency-threshold based forecasting function $g$ on $D_R^{test}$ using the predicted and ground-truth forgetting binary indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R202: Code has been written to generate predictions on the MMLU va...
- **Rubric ID**: 8968eba8-f72b-4526-ab7f-220eafad6680
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the MMLU validation set using FLAN-T5_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1 -- Training and Evaluation of the Forecasting Model $g$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R203: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 85ee3b38-7b8b-4d5b-982a-cb8c2dff54e0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R204: Code has been developed to compute the ground-truth forgetti...
- **Rubric ID**: afa92ef1-f129-4cc3-8ee0-84cac44baaba
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground-truth forgetting binary indicator $z_{ij}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i) \in D_R^{train}$ on the $j$th sample from the filtered pre-training dataset $(x_j, y_j) \in \hat{D}_{PT}$ and grading it using the Exact Match score.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R205: Code has been written to query the frequency-threshold based...
- **Rubric ID**: 5f0f5bd7-6980-42f1-9cd1-46e68d8c41e2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to query the frequency-threshold based forecasting function $g$ for every sample $(x_i, y_i) \in D_R^{test}$ and $(x_j, y_j) \in \hat{D}_{PT}$ to produce a prediction $\hat{z}_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R206: Code has been written to query the copy of FLAN-T5_{Large} f...
- **Rubric ID**: fb45886a-feab-41b5-868a-0151fb1f2030
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to query the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i) \in D_R^{test}$ on the $j$th sample from the filtered pre-training dataset $(x_j, y_j) \in \hat{D}_{PT}$ and grade it using the Exact Match score, producing a ground-truth forgetting binary indicator $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R207: Code has been written to compute the F1-score of the frequen...
- **Rubric ID**: e31eaa4d-9c25-4a80-bbdf-1801f93f49c6
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score of the frequency-threshold based forecasting function $g$ on $D_R^{test}$ using the predicted and ground-truth forgetting binary indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R208: Code has been written to generate predictions on the MMLU va...
- **Rubric ID**: 31e58c35-b95a-4b74-a4b1-e38bf584ccdf
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the MMLU validation set using FLAN-T5_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R209: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 569ee723-3214-4f1a-aa0a-a91756799694
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R210: Code has been developed to compute the ground-truth forgetti...
- **Rubric ID**: 050963db-9905-4962-9c49-3aa1774a5771
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground-truth forgetting binary indicator $z_{ij}$ by evaluating each LoRA-updated copy of FLAN-T5_{Large}, fine-tuned on $(x_i, y_i) \in D_R^{train}$, on the $j$th sample from the filtered pre-training dataset $(x_j, y_j) \in \hat{D}_{PT}$ and grading it using Exact Match.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R211: Code has been written to apply the frequency-threshold based...
- **Rubric ID**: 9a4f8f2b-f9db-4d64-85cd-a6e2e2dcb7e8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to apply the frequency-threshold based forecasting function $g$ to every sample $(x_i, y_i) \in D_R^{test}$ and $(x_j, y_j) \in \hat{D}_{PT}$, producing a predicted forgetting indicator $\hat{z}_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R212: Code has been developed to evaluate each LoRA-updated copy o...
- **Rubric ID**: c5da973c-f197-426d-92ec-0a657f6109ce
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to evaluate each LoRA-updated copy of FLAN-T5_{Large}, fine-tuned on $(x_i, y_i) \in D_R^{test}$, on the $j$th sample from the filtered pre-training dataset $(x_j, y_j) \in \hat{D}_{PT}$ using Exact Match, producing a ground-truth forgetting binary indicator $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R213: Code has been written to compute the F1-score of the frequen...
- **Rubric ID**: 3de1c01f-646f-405d-a044-8759cd636e64
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score of the frequency-threshold based forecasting function $g$ on $D_R^{test}$ by comparing the predicted forgetting binary indicators $\hat{z}_{ij}^{test}$ with the ground-truth indicators $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R214: Code has been written to generate predictions on the MMLU va...
- **Rubric ID**: fc454662-52b0-430e-a86c-1a873f877410
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the MMLU validation set using FLAN-T5_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R215: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: c3f068fb-0e24-4e1c-9c4c-d16fdd8cc5cc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R216: Code has been developed to compute the ground-truth forgetti...
- **Rubric ID**: d7048f8f-433d-45ba-b20e-efb77a5a4056
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground-truth forgetting binary indicator $z_{ij}$ by evaluating each fully fine-tuned copy of FLAN-T5_{Large} on $(x_j, y_j) \in \hat{D}_{PT}$ using the Exact Match score, as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R217: Code has been written to apply the frequency-threshold based...
- **Rubric ID**: 5208cf5e-b1c9-45e4-ae35-1c517a4c48f5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to apply the frequency-threshold based forecasting function $g$ to each sample $(x_i, y_i) \in D_R^{test}$ and $(x_j, y_j) \in \hat{D}_{PT}$ to produce a prediction $\hat{z}_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R218: Code has been developed to evaluate each fully fine-tuned co...
- **Rubric ID**: 8e4d8393-6d3f-4a9f-818c-cc6cb8f5d4a1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to evaluate each fully fine-tuned copy of FLAN-T5_{Large}, trained on $(x_i, y_i) \in D_R^{test}$, on $(x_j, y_j) \in \hat{D}_{PT}$ using the Exact Match score, producing the ground-truth forgetting binary indicator $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R219: Code has been written to compute the F1-score of the frequen...
- **Rubric ID**: 76dd0c51-105e-421c-86f3-9d150e315b9e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score of the frequency-threshold based forecasting function $g$ on $D_R^{test}$ using the predicted forgetting binary indicators $\hat{z}_{ij}^{test}$ and the ground-truth indicators $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R220: Code has been written to generate predictions on the MMLU va...
- **Rubric ID**: 3d97590d-02e1-4dad-a5de-9bb67e6db61a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the MMLU validation set using FLAN-T5_{3B} and evaluated with the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described under Section 4.1 -- Training and Evaluation Setup.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R221: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 3c3f9e27-34d2-4eae-82ab-52a0955e75a4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded with the Exact Match score to create the dataset of correct pre-training samples $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R222: For each fine-tuned model on $(x_i, y_i) \in D_R^{train}$, c...
- **Rubric ID**: cc9033d3-e75b-4459-af66-39db61f2b69c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each fine-tuned model on $(x_i, y_i) \in D_R^{train}$, code has been written to compute the ground-truth forgetting indicator $z_{ij}$ by evaluating on each sample $(x_j, y_j) \in \hat{D}_{PT}$ using the Exact Match score, as described in Section 2.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R223: Code has been written to apply the frequency-threshold based...
- **Rubric ID**: ecd5625f-2320-452e-9fb5-9d0afba49599
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to apply the frequency-threshold based forecasting function $g$ to each sample pair $(x_i, y_i) \in D_R^{test}$ and $(x_j, y_j) \in \hat{D}_{PT}$, producing a predicted forgetting indicator $\hat{z}_{ij}^{test}$ for each pair.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R224: Code has been developed to evaluate the FLAN-T5_{3B} model f...
- **Rubric ID**: d1213300-363b-467b-a262-17eee6c8072b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to evaluate the FLAN-T5_{3B} model fine-tuned on $(x_i, y_i) \in D_R^{test}$ on each $(x_j, y_j) \in \hat{D}_{PT}$ using the Exact Match score, producing the ground-truth forgetting indicator $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R225: Code has been written to compute the F1-score for the freque...
- **Rubric ID**: c7f9626e-8b6b-43d9-abd9-cfe55be477ea
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the frequency-threshold based forecasting method $g$ on $D_R^{test}$ by comparing the predicted forgetting indicators $\hat{z}_{ij}^{test}$ with the ground-truth indicators $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R226: Code has been written to generate predictions on the MMLU va...
- **Rubric ID**: da8ba158-a013-4bf2-aa4a-a433a55c07c2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the MMLU validation set using FLAN-T5_{3B} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R227: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: ca8d1897-1a31-402e-a537-20e6afc33a95
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R228: Code has been written to compute the ground-truth forgetting...
- **Rubric ID**: dae7c516-d30e-4115-a50c-233a49843304
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the ground-truth forgetting binary indicator $z_{ij}$ by evaluating the LoRA-updated copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i) \in D_R^{train}$ on the $j^\text{th}$ sample from the filtered pre-training dataset $(x_j, y_j) \in \hat{D}_{PT}$ and grading it using the Exact Match score.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R229: Code has been written to evaluate each LoRA-updated copy of...
- **Rubric ID**: 2323f3fd-7c18-45eb-ab31-1417d3950cc0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate each LoRA-updated copy of FLAN-T5_{3B}, fine-tuned on $(x_i, y_i) \in D_R^{test}$, on the $j^\text{th}$ sample from the filtered pre-training dataset $(x_j, y_j) \in \hat{D}_{PT}$ using Exact Match, producing a ground-truth forgetting binary indicator $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R230: Code has been written to compute the F1-score of the frequen...
- **Rubric ID**: e7bc5616-150a-493a-b021-ef301a8eae47
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score of the frequency-threshold based forecasting function $g$ on $D_R^{test}$ by comparing the predicted forgetting binary indicators $\hat{z}_{ij}^{test}$ with the ground-truth indicators $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R231: Code has been written to generate predictions on the test se...
- **Rubric ID**: b9da911e-6df4-4968-8cbd-46d687121408
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using BART0_{Large}, th...

### R232: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: bac36a09-c57f-44d7-908b-ab0e70aea6dc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using BART0_{Large}, th...

### R233: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 3b02483b-6ccc-4d7b-8d55-3f2700b76fd0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of BART0_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using BART0_{Large}, th...

### R234: Code has been written to compute the F1-score for the fixed-...
- **Rubric ID**: ae6ee867-6020-490a-b545-3686259d46de
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the fixed-logit based forecasting method and BART0_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using BART0_{Large}, th...

### R235: Code has been written to generate predictions on the test se...
- **Rubric ID**: b4c462f0-4fed-447b-8aad-5c066352da56
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using BART0_{Large}, th...

### R236: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 3ed62cd1-74f5-41cb-9147-4e746de81962
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using BART0_{Large}, th...

### R237: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 746d6ff4-50d6-41e9-ad69-41ecdf5e0a53
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of BART0_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using BART0_{Large}, th...

### R238: Code has been written to compute the F1-score for the fixed-...
- **Rubric ID**: d513c27e-1bbe-4697-85de-ad494fd3ab27
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the fixed-logit based forecasting method and BART0_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using BART0_{Large}, th...

### R239: Code has been written to generate predictions on the MMLU va...
- **Rubric ID**: 846ecad6-6cf8-47cb-8c1e-ba31e5b57f82
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the MMLU validation set using FLAN-T5_{Large} and evaluated with the Exact Match score to create the dataset $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, ...

### R240: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: aae7d581-a42d-4af2-841c-553a0531a275
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded with the Exact Match score to create the dataset of correct pre-training samples $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, ...

### R241: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 978f6dc3-335d-4934-a634-c5cd24b59b85
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, ...

### R242: Code has been written to compute the F1-score for the fixed-...
- **Rubric ID**: 5c4608b0-ae19-48b6-865f-42526151e894
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the fixed-logit based forecasting method and FLAN-T5_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, ...

### R243: Code has been written to generate predictions on the MMLU va...
- **Rubric ID**: f053e70d-4634-4719-b9d8-9c1b1448ccc4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the MMLU validation set using FLAN-T5_{Large} and evaluated with the Exact Match score to create the dataset $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, th...

### R244: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: edf48032-0a2b-4b25-91a2-dab7b4d40345
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded with the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, th...

### R245: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 1e9c8c93-28e6-4e5e-ac20-419cf5f487c3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the FLAN-T5_{Large} model fine-tuned with LoRA on $(x_i, y_i)$ against $(x_j, y_j)$, and scoring with the Exact Match metric.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, th...

### R246: Code has been written to compute the F1-score for the fixed-...
- **Rubric ID**: 2695bb5f-712d-4263-9aa0-f01d4e1faa2f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the fixed-logit based forecasting method and FLAN-T5_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, th...

### R247: Code has been written to generate predictions on the MMLU va...
- **Rubric ID**: 5f146d19-5f0a-4839-867f-65453c35f949
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the MMLU validation set using FLAN-T5_{Large} and evaluate them with the Exact Match score to produce $D_R^{test}$, following the details in Section 4.1.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, ...

### R248: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: d88aabf3-7613-4d8b-98e9-8da84794ee60
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large}, evaluating them with the Exact Match score to create the filtered dataset of correct pre-training samples, $\hat{D}_{PT}$, as detailed in Section 2.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, ...

### R249: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 080e3fda-5d33-469c-9591-d5c963ea3c73
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$, and scoring with the Exact Match metric.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, ...

### R250: Code has been written to compute the F1-score for the fixed-...
- **Rubric ID**: c80dd0b7-7074-442e-8cf7-0a09846f02e0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the fixed-logit based forecasting method with FLAN-T5_{Large} under full fine-tuning using the predicted and ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, ...

### R251: Code has been written to generate predictions on the MMLU va...
- **Rubric ID**: e209131f-6910-46eb-a050-09e69a870887
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the MMLU validation set using FLAN-T5_{3B} and evaluated with the Exact Match score to create the dataset $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{3B}, the M...

### R252: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: b9dfbe59-5b92-4ec9-ab6a-349fc0f3a43a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded with the Exact Match score to create the dataset of correct pre-training samples $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{3B}, the M...

### R253: Code has been written to compute the F1-score for the fixed-...
- **Rubric ID**: b46bad55-1c68-47bb-acbd-e5c9a82e4119
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the fixed-logit based forecasting method with FLAN-T5_{3B} under full fine-tuning using the predicted and ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{3B}, the M...

### R254: Code has been written to generate predictions on the MMLU va...
- **Rubric ID**: 55fbeecf-8795-49b3-b8b3-a9af9e16e880
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the MMLU validation set using FLAN-T5_{3B} and evaluate them with the Exact Match score to produce $D_R^{test}$, following the details in Section 4.1.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{3B}, the M...

### R255: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: bad62d40-a5dc-4afe-803e-783a4a0fa876
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B}, evaluating them with the Exact Match score to create the filtered dataset of correct pre-training samples, $\hat{D}_{PT}$, as detailed in Section 2.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{3B}, the M...

### R256: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: bc747911-97e0-414a-8734-e3454efb0ee4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$, and scoring with the Exact Match metric.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{3B}, the M...

### R257: Code has been written to compute the F1-score for the fixed-...
- **Rubric ID**: 7015d677-3936-41e6-92ed-7bcac5c4af76
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the fixed-logit based forecasting method with FLAN-T5_{3B} with only LoRA parameters updated using the predicted and ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{3B}, the M...

### R258: Code has been written to generate predictions on the test se...
- **Rubric ID**: f27ffa70-bffa-45c0-9421-8d4d4d7eb18b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R259: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: ac9b7299-c71c-4e84-b2f8-ce1411bdb090
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R260: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 500108d6-51d2-444b-a617-7f1fcb5c839f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R261: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: fc2de1d5-e896-442a-b601-9c2d6e3e3c87
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of BART0_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R262: Code has been written to compute the F1-score for the traina...
- **Rubric ID**: cff8e9a1-bf96-4473-83ee-8fbda323ffb4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the trainable logit based forecasting method and BART0_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R263: Code has been written to generate predictions on the test se...
- **Rubric ID**: 17824cf1-807f-4126-8def-430ab4d1c79c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R264: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 9a283ea6-2053-4429-8df8-2c1765d911ad
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R265: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 9f0bcde1-1dca-42b0-b5a9-8140740e713b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R266: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 2abcae14-795e-4c2d-bf5d-3f296c36bb2d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of BART0_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R267: Code has been written to compute the F1-score for the traina...
- **Rubric ID**: 4d0b29b6-7578-45e0-b409-3c0f0f3ce6f1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the trainable logit based forecasting method and BART0_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R268: Code has been written to generate predictions on the test se...
- **Rubric ID**: e0f644bd-f166-4dcb-9b24-b47ceb2a29e1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R269: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 211fce06-637c-48e5-8dc0-7fc95fcd95c6
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R270: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: cf2d3672-3fda-4049-93c1-f878dc949dc6
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R271: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 9b2f3b3d-6f16-40d7-b91b-83d72bc45aa9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R272: Code has been written to compute the F1-score for the traina...
- **Rubric ID**: b71f50c9-a3c1-4db5-8334-060a5690f052
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the trainable logit based forecasting method and FLAN-T5_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R273: Code has been written to generate predictions on the test se...
- **Rubric ID**: 22a21012-ec86-4f86-ab74-d009ea1cba58
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R274: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: de6e7d9b-5d08-4fe9-9dad-3f0e4b14784d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R275: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 7d34963b-0219-46f2-9782-fe27945a6673
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R276: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 3f9fb8e3-861b-43e1-8231-4163790d4423
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R277: Code has been written to compute the F1-score for the traina...
- **Rubric ID**: c0ab94d8-e6a1-4680-b9d6-83fbe4da056c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the trainable logit based forecasting method and FLAN-T5_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R278: Code has been written to generate predictions on the test se...
- **Rubric ID**: 6e17b020-9c97-4b17-bc46-d569a706d097
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R279: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 16d8741a-66ed-4f2c-bb25-0d6eccc4de4f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R280: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 07caba9e-481b-4353-ae0b-219bc5807d90
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R281: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: be8df16c-1971-47ed-b189-f69d0a039b86
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R282: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 60808cdc-c5bf-467f-a571-12db1f47381e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R283: Code has been written to compute the F1-score for the traina...
- **Rubric ID**: 1920f82f-c7b9-450f-9b35-eaf2dd7592f4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the trainable logit based forecasting method and FLAN-T5_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R284: Code has been written to generate predictions on the test se...
- **Rubric ID**: e78b32fb-c776-405d-928a-de12caa772fb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{3B} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R285: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 06856a86-c063-47d8-bca5-6c7bee7235bf
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R286: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 8e82d920-461c-410a-9a74-1fa12d940c30
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R287: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: e8d503f4-a060-489f-ac85-d37dc518d199
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R288: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: cb7b00f6-5f81-46ec-a68e-54d997763301
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R289: Code has been written to compute the F1-score for the traina...
- **Rubric ID**: dcf6ee4c-93c5-4cb8-8d3e-ccc373420bc0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the trainable logit based forecasting method and FLAN-T5_{3B} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R290: Code has been written to generate predictions on the test se...
- **Rubric ID**: 8792d15b-25e4-4777-b5e3-61f28f88ed9e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{3B} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R291: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 40d11a81-42a3-4c0a-95f0-401fcde73f2e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R292: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 161bbe48-17f9-471f-84d3-e932788ff642
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R293: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 8e1ee458-4c40-40ca-afa2-879c2fb72398
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R294: Code has been written to compute the F1-score for the traina...
- **Rubric ID**: 45b0cace-2885-42a7-bf2b-bd8948f98b5a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the trainable logit based forecasting method and FLAN-T5_{3B} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R295: Code has been written to generate predictions on the test se...
- **Rubric ID**: 87cee42e-29cd-4a2d-8041-38de4624c221
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R296: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: a3c47bb2-2dce-4e31-be88-3672405d01c2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R297: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: e086b968-69fc-4550-9b7b-208890bd1e60
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of BART0_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R298: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 22368542-ce9f-492a-91af-48e2bcc591a8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R299: Code has been written to compute the F1-score for the repres...
- **Rubric ID**: 1a7e4b7f-9e8c-400a-bb13-a9bc2ffa92ed
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the representation based forecasting method and BART0_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R300: Code has been written to generate predictions on the test se...
- **Rubric ID**: 9e9f8a57-b914-4e9c-acb1-312ed505032b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R301: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: d06f7ce9-7daa-4d5a-a4ba-f9b481cbda99
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of BART0_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R302: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 63a8380a-13ef-4c0f-8e04-d5bbaf18577c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R303: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: afba0931-4303-45f3-af6d-c441f8bd4709
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R304: Code has been written to compute the F1-score for the repres...
- **Rubric ID**: d329ca84-346c-4614-a59e-0513e6eb923c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the representation based forecasting method and BART0_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R305: Code has been written to generate predictions on the test se...
- **Rubric ID**: 18cc5bde-766f-47f9-99e1-673a59a88490
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R306: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 67fd08da-20ac-4467-b7c7-401d55007537
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R307: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 75dc26c3-0478-43b0-94fb-40057dc18d80
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R308: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 17dd529d-df49-4d42-af97-5a7dbdac7611
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R309: Code has been written to compute the F1-score for the repres...
- **Rubric ID**: 0e369b7c-3c17-47b9-9c9a-cf71c19dc7ba
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the representation based forecasting method and FLAN-T5_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R310: Code has been written to generate predictions on the test se...
- **Rubric ID**: 9c2d1ac4-a3f9-40ae-bf49-f25f4e376316
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R311: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 05a1be46-3f8a-43fd-aa52-1fab65cfc587
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R312: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 33aed2ef-af78-4b8a-9448-8c8819dff569
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R313: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: ef9d8d75-b51d-49d7-bb22-b32709183f11
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R314: Code has been written to compute the F1-score for the repres...
- **Rubric ID**: 3fc9f83b-2c04-4407-9d17-be09be90991a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the representation based forecasting method and FLAN-T5_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R315: Code has been written to generate predictions on the test se...
- **Rubric ID**: 46cfe617-7dca-4754-bdfa-576abfdf4aff
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R316: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 370c87c6-94da-45a7-bd86-6c0328bcfc02
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R317: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 20dde124-2c23-42a6-9600-02c16fa8116f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R318: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 128bfaef-93b9-443a-9053-e079fc6bed99
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R319: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 68fa1652-3dc1-4073-8f3f-e6710928ca5d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the representation forecasting model as described in Algorithm 4 and the learned encoder $h$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R320: Code has been written to compute the F1-score for the repres...
- **Rubric ID**: 964edbae-e585-4baa-b899-1dff4ff4a697
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the representation based forecasting method and FLAN-T5_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R321: Code has been written to generate predictions on the test se...
- **Rubric ID**: ea96d790-b30c-467b-89d7-cb86564ddc5e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{3B} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R322: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 4b36fa4c-f5f2-440b-b84b-c747c5af8f0c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R323: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 39f45fbe-6df3-48d3-9f53-71f65a11549e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R324: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: d67e736e-52b3-404a-9c01-9998d4e62396
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R325: Code has been written to compute the F1-score for the repres...
- **Rubric ID**: 2c56e8c4-0c05-4083-a79b-93ac825df9c9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the representation based forecasting method and FLAN-T5_{3B} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R326: Code has been written to generate predictions on the test se...
- **Rubric ID**: 5bb66e33-37e7-4f03-8069-3c9164131638
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{3B} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R327: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 26003fa4-4f57-4e13-b51b-fb5dd3ac140a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R328: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: f69d9d70-22b0-476a-89e1-8450c9114e93
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R329: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: b98aed0f-8d3b-409a-8a33-244b56af6b73
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R330: Code has been written to compute the F1-score for the repres...
- **Rubric ID**: a62843fe-91fa-46b2-b7c8-902bd4179cd1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the representation based forecasting method and FLAN-T5_{3B} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R331: Code has been written to generate predictions on the test se...
- **Rubric ID**: d0d51b0b-d689-46ce-9780-3c45f0edb222
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R332: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 37cc2b5f-a0c6-4425-9779-d999b2888938
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of BART0_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R333: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: a8acf39d-a711-47c0-ac6a-5a6220c531a3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R334: Code has been written to compute the F1-score for the prior-...
- **Rubric ID**: b8f4f845-2da0-41ad-88a7-8acc81251a9d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the prior-free representation based forecasting method and BART0_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R335: Code has been written to generate predictions on the test se...
- **Rubric ID**: 65957caa-a6a9-4f48-9133-d7e3a41b0b09
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R336: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 70598095-6493-41e2-a4b0-bb8c9974b790
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of BART0_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R337: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: c6c521e9-769d-4382-ba81-197409c86d21
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R338: Code has been written to compute the F1-score for the prior-...
- **Rubric ID**: b16ebf02-9413-44d8-96bf-a550c6857a78
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the prior-free representation based forecasting method and BART0_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R339: Code has been written to generate predictions on the test se...
- **Rubric ID**: 013f84cf-41a5-4eb5-92e9-7fc8aeb84a31
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R340: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: c5f31493-5876-458a-8f92-bd7ffade6d3b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R341: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 8af6822b-1dc7-4228-b248-bccb30f7b2bb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R342: Code has been written to compute the F1-score for the prior-...
- **Rubric ID**: 8feb9575-35a2-41b8-a059-123df6b08c0a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the prior-free representation based forecasting method and FLAN-T5_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R343: Code has been written to generate predictions on the test se...
- **Rubric ID**: d0ff95b6-fe8c-41f5-9276-36a87897098b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R344: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: c8f30ae2-689e-4ef2-9a51-68b7f0996bc6
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R345: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: d728839d-53c9-4d64-9caf-2009e9177831
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R346: Code has been written to compute the F1-score for the prior-...
- **Rubric ID**: 7a4f577e-4b5f-453d-bc98-cf13ee96bba9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the prior-free representation based forecasting method and FLAN-T5_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R347: Code has been written to generate predictions on the test se...
- **Rubric ID**: 0ef5d18e-3018-4d33-b712-55a6c2821352
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R348: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 1294ac14-7a5f-4c45-be96-0b1053cf389f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R349: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: da3b1c88-c843-4b4a-a34a-c4c8ec42b908
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R350: Code has been written to compute the F1-score for the prior-...
- **Rubric ID**: f8d09d08-b88a-4c26-8116-9570c5abf3ba
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the prior-free representation based forecasting method and FLAN-T5_{Large} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R351: Code has been written to generate predictions on the test se...
- **Rubric ID**: fb5b99b1-597a-4424-a00e-1b42e614cbe4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{3B} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R352: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 9dbefa4d-92dd-4296-8ede-a83ef34bf917
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R353: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 74515d6c-d6f6-4391-b9cb-07d8920790bf
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R354: Code has been written to compute the F1-score for the prior-...
- **Rubric ID**: 2b0392f5-be04-4b26-9385-8b051860f6a1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the prior-free representation based forecasting method and FLAN-T5_{3B} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R355: Code has been written to generate predictions on the test se...
- **Rubric ID**: 958eba68-515a-4dd7-a2e6-3232071af901
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the MMLU dataset using FLAN-T5_{3B} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R356: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 7ea3194e-cb99-481d-ba62-4af4316b80ca
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R357: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: a956566b-6762-4e19-a4d3-21a57eba82f5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R358: Code has been written to compute the F1-score for the prior-...
- **Rubric ID**: 6570d5d2-8ea4-459d-9a49-efb59c48109e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score for the prior-free representation based forecasting method and FLAN-T5_{3B} using the predicted and the ground-truth forgetting indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R359: The code to evaluate the frequency-threshold based forecasti...
- **Rubric ID**: 78c3588a-60a8-4932-857e-3e49b02f5063
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the frequency-threshold based forecasting method on all model, dataset and fine-tuning configurations present in Table 1 has been executed and the F1-scores have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 1 has been executed and the F1-scores for...

### R360: The code to evaluate the fixed-logit based forecasting metho...
- **Rubric ID**: c1c05bb0-74f1-41aa-9217-2c0ab7d05a4c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the fixed-logit based forecasting method on all model, dataset and fine-tuning configurations present in Table 1 has been executed and the F1-scores have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 1 has been executed and the F1-scores for...

### R361: The code to evaluate the trainable logit based forecasting m...
- **Rubric ID**: 6287ddc2-cce8-4ff2-b24a-2e3ab1de81e1
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the trainable logit based forecasting method on all model, dataset and fine-tuning configurations present in Table 1 has been executed and the F1-scores have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 1 has been executed and the F1-scores for...

### R362: The code to evaluate the representation based forecasting me...
- **Rubric ID**: 58142e07-7a09-4e88-8f6d-dbba05dff9c4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the representation based forecasting method on all model, dataset and fine-tuning configurations present in Table 1 has been executed and the F1-scores have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 1 has been executed and the F1-scores for...

### R363: The code to evaluate the prior-free representation based for...
- **Rubric ID**: f57935fb-5c1e-405e-93b1-8511dcb5bf6d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the prior-free representation based forecasting method on all model, dataset and fine-tuning configurations present in Table 1 has been executed and the F1-scores have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 1 has been executed and the F1-scores for...

### R364: The recorded F1-scores show that removing the frequency prio...
- **Rubric ID**: 9d19418f-ad74-4bcc-8817-7a8c0acfcbb4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded F1-scores show that removing the frequency prior term from the representation based forecasting method reduces the average F1-score for all model, dataset and fine-tuning setups.
- **Parent context**: The recorded F1-scores match those presented in Table 1.

### R365: Code has been written to generate predictions on the MMLU va...
- **Rubric ID**: 10717b81-59ea-40fb-a095-075802e66ec9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the MMLU validation set using FLAN-T5_{Large} and graded using the Exact Match score to create the datasets $D_R^{train}$ and $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Figure 3 has been replicated.

### R366: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 2723c720-6cc7-4abb-b191-3c554a09b81b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Figure 3 has been replicated.

### R367: Predictions have been generated on the MMLU validation set a...
- **Rubric ID**: 9a70d6c0-8911-4453-8e00-2c7c2443fbd9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Predictions have been generated on the MMLU validation set and graded using Exact Match score to create $D_R^{train}$ and $D_R^{test}$. Predictions have been generated on $D_{PT}$ and graded to create $\hat{D}_{PT}$.
- **Parent context**: Figure 3 has been replicated.

### R368: Code has been developed to evaluate the copy of FLAN-T5_{Lar...
- **Rubric ID**: 13f431f2-8e41-4cf3-a370-d11ddaf65c49
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to evaluate the copy of FLAN-T5_{Large} trained on $t$-many samples from $D_R^{test}$ on $(x_j, y_j) \in \hat{D}_{PT}$ using the Exact Match score, producing the ground-truth forgetting binary indicator at each time step $t$: $z^{t}_{ij}^{test}$.
- **Parent context**: Figure 3 has been replicated.

### R369: The FLAN-T5 model has been fine-tuned on a subset of $D_R^{\...
- **Rubric ID**: 8b5a0232-b699-4b70-90a8-87929dca33b6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The FLAN-T5 model has been fine-tuned on a subset of $D_R^{\text{test}}$ with at least 40 samples, and the forgetting binary indicators $z_{ij}$ have been computed by evaluating fine-tuned model copies on $\hat{D}_{PT}$
- **Parent context**: Figure 3 has been replicated.

### R370: Code has been written to compute the ground-truth forgetting...
- **Rubric ID**: 9bc4392b-86be-4283-9c79-faa9eb1f9091
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the ground-truth forgetting binary indicator $z_{ij}$ by evaluating each fully fine-tuned copy of FLAN-T5_{Large} on $(x_j, y_j) \in \hat{D}_{PT}$ using the Exact Match score, as described in Section 4.1.
- **Parent context**: The frequency-threshold based forecasting function $g$ has been developed, as described in Section 3...

### R371: Code has been written to compute the average F1-score for ea...
- **Rubric ID**: eb488a54-1b9a-4859-ac97-6679e8b545a3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average F1-score for each time step using $\hat{z}_{ij}^{test}$ and $z^{t}_{ij}^{test}$, and by computing the running average with $\frac{1}{T} \sum_{t=0}^{T} \text{F1-score}_t$ where $T$ is the current time step.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the frequency-threshold based ...

### R372: Code has been written to compute the average precision for e...
- **Rubric ID**: 26324783-507a-4938-ade7-c7f9bf0b8f35
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average precision for each time step using $\hat{z}_{ij}^{test}$ and $z^{t}_{ij}^{test}$, and by computing the running average with $\frac{1}{T} \sum_{t=0}^{T} \text{Precision}_t$ where $T$ is the current time step.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the frequency-threshold based ...

### R373: Code has been written to compute the average recall for each...
- **Rubric ID**: dd9d5e82-8577-43bf-9a03-429837f8bc26
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average recall for each time step using $\hat{z}_{ij}^{test}$ and $z^{t}_{ij}^{test}$, and by computing the running average with $\frac{1}{T} \sum_{t=0}^{T} \text{Recall}_t$ where $T$ is the current time step.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the frequency-threshold based ...

### R374: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: eca38b73-9c36-4769-83c9-e0f0e1483411
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the trainable logit based fore...

### R375: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 38df20bf-4ad8-4a1b-81e2-6ce8fedb814e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the trainable logit based fore...

### R376: Code has been written to compute the average F1-score for ea...
- **Rubric ID**: c1ffc8e0-d94f-4ea7-9e34-b5f70bbdfd1e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average F1-score for each time step using $\hat{z}_{ij}^{test}$ and $z^{t}_{ij}^{test}$, and by computing the running average with $\frac{1}{T} \sum_{t=0}^{T} \text{F1-score}_t$ where $T$ is the current time step.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the trainable logit based fore...

### R377: Code has been written to compute the average precision for e...
- **Rubric ID**: 53bd90ee-9c0f-42fd-be5f-f44acde5aae3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average precision for each time step using $\hat{z}_{ij}^{test}$ and $z^{t}_{ij}^{test}$, and by computing the running average with $\frac{1}{T} \sum_{t=0}^{T} \text{Precision}_t$ where $T$ is the current time step.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the trainable logit based fore...

### R378: Code has been written to compute the average recall for each...
- **Rubric ID**: 939264d2-05cb-435c-b8f6-dc94a7ba0fe7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average recall for each time step using $\hat{z}_{ij}^{test}$ and $z^{t}_{ij}^{test}$, and by computing the running average with $\frac{1}{T} \sum_{t=0}^{T} \text{Recall}_t$ where $T$ is the current time step.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the trainable logit based fore...

### R379: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 5ce6f8b7-e14a-41ad-8119-6fd916dc3fa1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the representation based forec...

### R380: Code has been written to compute the average F1-score for ea...
- **Rubric ID**: d4e696f2-996c-432a-89bf-dca0417291d3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average F1-score for each time step using $\hat{z}_{ij}^{test}$ and $z^{t}_{ij}^{test}$, and by computing the running average with $\frac{1}{T} \sum_{t=0}^{T} \text{F1-score}_t$ where $T$ is the current time step.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the representation based forec...

### R381: Code has been written to compute the average precision for e...
- **Rubric ID**: e3d1b0cc-36bf-4447-a997-b28ed8444ef5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average precision for each time step using $\hat{z}_{ij}^{test}$ and $z^{t}_{ij}^{test}$, and by computing the running average with $\frac{1}{T} \sum_{t=0}^{T} \text{Precision}_t$ where $T$ is the current time step.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the representation based forec...

### R382: Code has been written to compute the average recall for each...
- **Rubric ID**: 97bdee8b-084c-4af3-b855-ed15e28b1052
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average recall for each time step using $\hat{z}_{ij}^{test}$ and $z^{t}_{ij}^{test}$, and by computing the running average with $\frac{1}{T} \sum_{t=0}^{T} \text{Recall}_t$ where $T$ is the current time step.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the representation based forec...

### R383: The running average of the F1-score, recall and precision ha...
- **Rubric ID**: 869c0d87-f9a9-42fc-b295-59dc3ddbe32a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The running average of the F1-score, recall and precision has been computed and recorded for each time step using $z_{ij}^{t,\text{test}}$ for the frequency-threshold, logit-based and representation-based forecasting methods. For a given time step $T$, the running average is defined as $\frac{1}{T} \sum_{t=0}^{T} \text{Metric}_t$ where $\text{Metric}_t$.
- **Parent context**: Figure 3 has been replicated.

### R384: The recorded running average precision roughly increases ove...
- **Rubric ID**: cca26cd1-2627-44a3-b715-ada1d46dbc9c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded running average precision roughly increases over time, peaks, then is relatively stable over time thereafter (i.e. all deviations from the peak are < 0.1 in magnitude) for the frequency-threshold, logit-based and representation-based forecasting methods.
- **Parent context**: The recorded F1-score, recall and precision metrics match those presented in Figure 3.

### R385: The recorded running average recall decreases over time for...
- **Rubric ID**: b4d7d077-9259-42e4-af70-7fb89a4da08b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded running average recall decreases over time for the frequency-threshold, logit-based and representation-based forecasting methods.
- **Parent context**: The recorded F1-score, recall and precision metrics match those presented in Figure 3.

### R386: The recorded running F1-scores show that the representation-...
- **Rubric ID**: 3cf87482-d8d6-4b95-9f4a-aa34236ac7b4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded running F1-scores show that the representation-based forecasting method achieves the highest running F1-score for most time steps, followed by the threshold-based method, while the trainable logit method performs the worst.
- **Parent context**: The recorded F1-score, recall and precision metrics match those presented in Figure 3.

### R387: Code has been written to generate predictions for all sample...
- **Rubric ID**: e1705f3c-740e-493c-8057-64bddd71ee6c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions for all samples in P3-Test_{ID} and P3-Test_{OOD} using BART0_{Large}.
- **Parent context**: Table 2 has been replicated.

### R388: Code has been written to grade the predictions generated by...
- **Rubric ID**: b6a67a5a-f269-4659-90ca-8ab99bc3db5b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to grade the predictions generated by BART0_{Large} on P3-Test_{ID} using the Exact Match score to create the dataset $D_R^{train}$, as described in Section 4.1.
- **Parent context**: Table 2 has been replicated.

### R389: Code has been written to grade the predictions generated by...
- **Rubric ID**: 1d54d6a6-13e1-4a41-a820-314c83aa76d8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to grade the predictions generated by BART0_{Large} on P3-Test_{OOD} using the Exact Match score to create the dataset $D_R^{test}$, as described in Section 4.1.
- **Parent context**: Table 2 has been replicated.

### R390: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 86bb2fa3-f585-4392-95a5-689c6d85417f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Table 2 has been replicated.

### R391: Code has been written to compute the ground-truth forgetting...
- **Rubric ID**: b019e4ce-bf4d-406f-9e92-5eec16369dfe
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the ground-truth forgetting binary indicator $z_{ij}$ by fine-tuning a copy of BART0_{Large} on each $(x_i, y_i) \in D_R^{	ext{train}}$, querying it on the $j$th sample from $\hat{D}{PT}$, and grading the output using the Exact Match score.
- **Parent context**: Table 2 has been replicated.

### R392: Code has been written to compute the ground-truth forgetting...
- **Rubric ID**: 97da0fad-8bbe-4189-8156-57ba0134be87
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{\text{test}}$ by fine-tuning a copy of BART0_{Large} on each $(x_i, y_i) \in D_R^{\text{test}}$, querying it on the $j$th sample from $\hat{D}{PT}$, and grading the output using the Exact Match score.
- **Parent context**: Table 2 has been replicated.

### R393: Code has been written to query the frequency-threshold based...
- **Rubric ID**: 748c3c9f-2562-4f08-acd8-98da5e5e2f08
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to query the frequency-threshold based forecasting function $g$ for every sample $(x_i, y_i) \in D_R^{train}$ and $(x_j, y_j) \in \hat{D}_{PT}$ and grade it using the Exact Match score, producing a prediction $\hat{z}_{ij}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R394: Code has been written to query the frequency-threshold based...
- **Rubric ID**: 7f6554be-8652-4f54-82e0-44ce3f557ead
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to query the frequency-threshold based forecasting function $g$ for every sample $(x_i, y_i) \in D_R^{test}$ and $(x_j, y_j) \in \hat{D}_{PT}$ and grade it using the Exact Match score, producing a prediction $\hat{z}_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R395: Code has been written to compute the F1-score of the frequen...
- **Rubric ID**: f7010c33-fd70-4e37-bad4-67aa940f39e8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score of the frequency-threshold based forecasting function $g$ for P3-Test_{ID} using $D_R^{train}$ and the predicted and ground-truth forgetting binary indicators $\hat{z}_{ij}$ and $z_{ij}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R396: Code has been written to compute the F1-score of the frequen...
- **Rubric ID**: 3cc3ed3f-4516-415c-bd86-828fc0f457d6
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score of the frequency-threshold based forecasting function $g$ for P3-Test_{OOD} using $D_R^{test}$ and the predicted and ground-truth forgetting binary indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R397: Code has been written to compute the F1-score of the trainab...
- **Rubric ID**: 949a3a66-cb91-4804-a45f-a6d1e8148a32
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score of the trainable logit based forecasting function $g$ for P3-Test_{ID} using $D_R^{train}$ and the predicted and ground-truth forgetting binary indicators $\hat{z}_{ij}$ and $z_{ij}$.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R398: Code has been written to compute the F1-score of the trainab...
- **Rubric ID**: 7e89f779-7e89-492c-8ad5-7607b57aa13b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score of the trainable logit based forecasting function $g$ for P3-Test_{OOD} using $D_R^{test}$ and the predicted and ground-truth forgetting binary indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R399: Code has been written to compute the F1-score of the represe...
- **Rubric ID**: a1c7cea1-ccad-4ddf-bdc0-652ae53399da
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score of the representation based forecasting function $g$ for P3-Test_{ID} using $D_R^{train}$ and the predicted and ground-truth forgetting binary indicators $\hat{z}_{ij}$ and $z_{ij}$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R400: Code has been written to compute the F1-score of the represe...
- **Rubric ID**: 517d7cc5-2e6d-45b2-b0c1-85c121040d23
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score of the representation based forecasting function $g$ for P3-Test_{OOD} using $D_R^{test}$ and the predicted and ground-truth forgetting binary indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R401: Code has been written to compute the F1-score of the prior-f...
- **Rubric ID**: 6b1ba9e8-cf35-43c6-a897-a56fd8462d17
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score of the prior-free representation based forecasting function $g$ for P3-Test_{ID} using $D_R^{train}$ and the predicted and ground-truth forgetting binary indicators $\hat{z}_{ij}$ and $z_{ij}$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R402: Code has been written to compute the F1-score of the prior-f...
- **Rubric ID**: 16b8435a-62f7-47c3-8275-eb982e537f55
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the F1-score of the prior-free representation based forecasting function $g$ for P3-Test_{OOD} using $D_R^{test}$ and the predicted and ground-truth forgetting binary indicators $\hat{z}_{ij}^{test}$ and $z_{ij}^{test}$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R403: The code to evaluate the frequency-threshold based forecasti...
- **Rubric ID**: 7fbfdf8f-4cf1-4e11-92d2-46336e784f13
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the frequency-threshold based forecasting method for both the P3-Test_{ID} and P3-Test_{OOD} configurations using BART0_{Large} has been executed and the F1-scores have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 2 has been executed and the F1-scores for...

### R404: The code to evaluate the trainable logit based forecasting m...
- **Rubric ID**: 04e08ca1-b200-4d36-9064-11f7bd9ad4fa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the trainable logit based forecasting method for both the P3-Test_{ID} and P3-Test_{OOD} configurations using BART0_{Large} has been executed and the F1-scores have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 2 has been executed and the F1-scores for...

### R405: The code to evaluate the representation based forecasting me...
- **Rubric ID**: 7f9f4674-5977-46d3-adcb-1f1e4f0e9b26
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the representation based forecasting method for both the P3-Test_{ID} and P3-Test_{OOD} configurations using BART0_{Large} has been executed and the F1-scores have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 2 has been executed and the F1-scores for...

### R406: The code to evaluate the prior-free representation based for...
- **Rubric ID**: fe98edb8-9229-49a0-9d50-b0cd262bdae7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the prior-free representation based forecasting method for both the P3-Test_{ID} and P3-Test_{OOD} configurations using BART0_{Large} has been executed and the F1-scores have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 2 has been executed and the F1-scores for...

### R407: The recorded F1-scores for the ID/OOD experiment show that t...
- **Rubric ID**: e4def2cb-ecf6-4bf3-9be5-2b0ab1cd885c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded F1-scores for the ID/OOD experiment show that the representation-based method has the highest F1-score for the in-domain splits of the P3 test set.
- **Parent context**: The recorded F1-scores match those presented in Table 2.

### R408: The recorded F1-scores for the ID/OOD experiment show that t...
- **Rubric ID**: 2d04ac62-941a-4cad-a5b0-bab0e00059a2
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 3
- **Requirement**: The recorded F1-scores for the ID/OOD experiment show that the representation-based method has the highest F1-score for out-of-domain splits of the P3 test set.
- **Parent context**: The recorded F1-scores match those presented in Table 2.

### R409: The recorded F1-scores for the ID/OOD experiment show that r...
- **Rubric ID**: 7d2158d9-30ba-4401-b0bc-9b1bf2e30bd4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded F1-scores for the ID/OOD experiment show that removing the bias term from the representation-based method reduces the F1-score for the in-domain splits of the P3 test set.
- **Parent context**: The recorded F1-scores match those presented in Table 2.

### R410: The recorded F1-scores for the ID/OOD experiment show that r...
- **Rubric ID**: 14ad0b81-884b-401a-bf3e-8728b6e9c332
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 3
- **Requirement**: The recorded F1-scores for the ID/OOD experiment show that removing the bias term from the representation-based method reduces the F1-score for the out-of-domain splits of the P3 test set.
- **Parent context**: The recorded F1-scores match those presented in Table 2.

### R411: The recorded F1-scores for the ID/OOD experiment show that t...
- **Rubric ID**: 59ebcbe5-1996-4df2-b802-e741f4bae72e
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded F1-scores for the ID/OOD experiment show that the threshold frequency-based method performs worst on the in-domain P3 test split.
- **Parent context**: The recorded F1-scores match those presented in Table 2.

### R412: The recorded F1-scores for the ID/OOD experiment show that t...
- **Rubric ID**: 2f35a2cc-2389-46cd-a930-7e97e84db3c9
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded F1-scores for the ID/OOD experiment show that the threshold frequency-based method performs second best (beaten by the representation-based method) on the out-of-domain P3 test split.
- **Parent context**: The recorded F1-scores match those presented in Table 2.

### R413: Code has been written to generate predictions on the test se...
- **Rubric ID**: 4f59468c-ea43-4aa7-9a54-f670a47abd05
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using BART0_{Large}, the P3 test set ...

### R414: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 97eadfa1-6d74-4bda-bf4f-c956a41c0554
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using BART0_{Large}, the P3 test set ...

### R415: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: d8234acf-7cd1-49ec-91bb-81c19edb58fd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using BART0_{Large}, the P3 test set ...

### R416: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: 5768b984-0d54-4f76-a5a4-3ebe1ec29021
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using BART0_{Large}, the P3 test set ...

### R417: Code has been written to generate predictions on the validat...
- **Rubric ID**: 00ff216a-e6c9-4afc-b2f0-c33859d5b5f0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU valid...

### R418: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: c1ff2b3b-4dda-4988-b68d-afaa54a1aa49
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU valid...

### R419: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: e6904295-c17d-4b66-a84a-d706b74a1fc9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU valid...

### R420: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: 5340250f-8110-421c-9b9b-981a711ba75f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU valid...

### R421: Code has been written to generate predictions on the validat...
- **Rubric ID**: b0434bbc-7321-4ed0-a179-037ca37bc14e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU valid...

### R422: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 9546f88a-7ce0-4d2a-b792-e6b76a85bf1b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU valid...

### R423: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 41d0dbd2-1afe-44e8-a653-92de77f49739
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU valid...

### R424: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: 833a8a45-d946-4eba-97d4-4b7790631554
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU valid...

### R425: Code has been written to generate predictions on the validat...
- **Rubric ID**: e7a80a38-e499-4b20-b429-2392283bd06b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{3B}, the MMLU validati...

### R426: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 4c7035cb-f827-45d0-96a1-20517de83cd1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{3B}, the MMLU validati...

### R427: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 118ece96-18dd-4bd7-81f7-3287c1a213de
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{3B}, the MMLU validati...

### R428: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: bdc36ae9-7c1f-48ec-8da0-103d9a88d75a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{3B}, the MMLU validati...

### R429: Code has been written to generate predictions on the test se...
- **Rubric ID**: e412f29f-778e-482c-ad95-5574689badf8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the random replay method using BART0_{Large}, the P3 test set and ...

### R430: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 9ac9b099-3d73-4922-bf56-df3862103674
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the random replay method using BART0_{Large}, the P3 test set and ...

### R431: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 140f56a2-a62d-4b38-84bd-ceeaa38c68fd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the random replay method using BART0_{Large}, the P3 test set and ...

### R432: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: c87869f4-73ec-404e-b382-5192f3ed2c51
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the random replay method using BART0_{Large}, the P3 test set and ...

### R433: Code has been written to generate predictions on the validat...
- **Rubric ID**: 491443ae-e4ff-4137-9261-be43d4152ee8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R434: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 0349a819-dcea-4ed3-a18e-8e891f68e31a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R435: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 143e7d2f-de97-4f41-95b6-fbfe01300f67
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R436: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: a7164315-0d02-478a-8188-144e58336860
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R437: Code has been written to generate predictions on the validat...
- **Rubric ID**: d0b16c34-5b8c-4324-a030-7c4fd582d02f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R438: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 4af063f6-08f9-4835-8adf-bb9c8a2b3fb9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R439: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 763ad8ac-54d3-4425-bb6b-39c9584ccdbd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R440: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: d5d24892-6922-4d71-9eff-a6aae17277c9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R441: Code has been written to generate predictions on the validat...
- **Rubric ID**: 8ff35b0c-52bf-46c0-b404-f920599cbb58
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{3B}, the MMLU validation s...

### R442: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 6e814134-ceaf-431b-b9c2-e28fab62e3cb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{3B}, the MMLU validation s...

### R443: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: e2d62692-7dc1-46d2-a550-b2741221c998
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{3B}, the MMLU validation s...

### R444: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: 8f645165-f146-47b2-81f2-a23cf4e5f1cb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{3B}, the MMLU validation s...

### R445: Code has been written to generate predictions on the test se...
- **Rubric ID**: a8377590-43fd-4712-a381-38ab6d1ad300
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R446: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 6796a36c-ce95-43cd-99e4-91d0b098dd8a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R447: Code has been written to compute the ground-truth forgetting...
- **Rubric ID**: 883cb9b7-238b-4178-9c26-d78287b6ad98
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the ground-truth forgetting binary indicator $z_{ij}$ for all pairs $(x_i, y_i) \in D_R^{\text{train}}$ and $(x_j, y_j) \in \hat{D}_{PT}$ by evaluating the copy of BART0_{Large} fine-tuned on each $(x_i, y_i)$ on the corresponding $j$th sample from $\hat{D}_{PT}$ and grading the output using the Exact Match score.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R448: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 1bd910c6-3c57-4ae4-ab26-d7554a7690d1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R449: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: 2e00cb23-5c55-49e8-89a9-540895045034
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R450: Code has been written to generate predictions on the validat...
- **Rubric ID**: 1e68bc23-e1e9-45c2-a33d-808d008420d7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R451: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: d0459431-e123-40f0-9411-48a487f6a21e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R452: Code has been written to compute the ground-truth forgetting...
- **Rubric ID**: 0a596475-8f2d-4788-8762-93b9abb2533f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the ground-truth forgetting binary indicator $z_{ij}$ for all pairs $(x_i, y_i) \in D_R^{\text{train}}$ and $(x_j, y_j) \in \hat{D}_{PT}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on each $(x_i, y_i)$ on the corresponding $j$th sample from $\hat{D}_{PT}$ and grading the output using the Exact Match score.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R453: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: d9913c05-e73d-4157-bca4-0f3837ac0796
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R454: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: a0ab851f-49d2-4cd3-9377-921f790d0eeb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R455: Code has been written to generate predictions on the validat...
- **Rubric ID**: 3b3feb08-61b7-447b-89cb-1332d823ca04
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R456: Code has been developed to compute the ground-truth forgetti...
- **Rubric ID**: 690ea75a-89d1-4a2a-a517-8315ee63adcf
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground-truth forgetting binary indicator $z_{ij}$ for all pairs $(x_i, y_i) \in D_R^{\text{train}}$ and $(x_j, y_j) \in \hat{D}_{PT}$ by using the copy of FLAN-T5_{Large} fine-tuned with the LoRA adaptation to model parameters on each $(x_i, y_i)$ on the corresponding $j$th sample from $\hat{D}_{PT}$ and grading the output using the Exact Match score.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R457: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 530b5783-df94-4a98-b878-ef923ce4eda2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R458: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: 749d3508-cbaf-44bc-a1e5-d431970caa07
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R459: Code has been written to generate predictions on the validat...
- **Rubric ID**: 58fbbbec-9ae6-46d5-8d6d-7e54b325ea3f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R460: Code has been developed to compute the ground-truth forgetti...
- **Rubric ID**: b377c78d-6585-4dd0-a158-3d099fdec60a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground-truth forgetting binary indicator $z_{ij}$ for all pairs $(x_i, y_i) \in D_R^{\text{train}}$ and $(x_j, y_j) \in \hat{D}_{PT}$ by using the copy of FLAN-T5_{3B} fine-tuned with the LoRA adaptation to model parameters on each $(x_i, y_i)$ on the corresponding $j$th sample from $\hat{D}_{PT}$ and grading the output using the Exact Match score.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R461: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 8541a8dd-d5e1-4a6e-81e9-7273c7a95502
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R462: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: 6f47eacb-5071-4a60-840b-d27c2622bf26
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R463: Code has been written to generate predictions on the test se...
- **Rubric ID**: c5205495-46f8-47fd-a53f-d75111fa5ebb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using BAR...

### R464: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: f17a9e74-b3d1-4f7b-a00b-b26e5028a82a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using BAR...

### R465: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 4974865e-23e4-421b-b52e-882ec83c1fc5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using BAR...

### R466: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: 82fead89-9952-406e-9709-8726b8281110
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using BAR...

### R467: Code has been written to generate predictions on the validat...
- **Rubric ID**: 98d67f2e-0e83-4b54-81b0-3d077aceebf0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R468: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 09514ad0-0035-4975-aee9-63d1c866ca30
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R469: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 984c11ce-4d17-417e-b1fe-260998ee3659
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R470: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: beef9530-3416-47de-be6b-75e0de005aaa
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R471: Code has been written to generate predictions on the validat...
- **Rubric ID**: 7eef3939-3834-4c36-9b09-d577fd17bb13
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R472: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 5f4d612a-b599-4ef4-80b5-ae3b95868791
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R473: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 1f1e27e9-123b-481d-9987-67449971f35f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R474: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: 6782a82d-d06c-440c-a24d-87afd98b0b7f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R475: Code has been written to generate predictions on the validat...
- **Rubric ID**: 2bbb4172-34f6-488f-938f-e6421f5b70cb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R476: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: f091c8c9-abf7-4787-8de3-37c3c29d24cf
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R477: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: f0ad69e1-da21-4cad-affe-b49acf5bc34c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R478: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 41c6ae74-a642-4916-8a75-7641aec09505
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R479: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: 5337aced-8fa4-4f3e-bc28-da144075c9ae
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R480: Code has been written to generate predictions on the test se...
- **Rubric ID**: 020471c7-fb43-440f-8c83-30ade54317ec
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using BART...

### R481: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 131cd8e4-3364-4e8d-8855-6afac566f9a7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using BART...

### R482: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: a5e729b6-dc0d-4711-939d-9784e8678192
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using BART...

### R483: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: b7555281-8306-4284-95cb-24ef5a0c007b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using BART...

### R484: Code has been written to generate predictions on the validat...
- **Rubric ID**: 50dc0b41-d774-4842-893b-4276c89d00ce
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R485: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 2dcb6c89-5aed-4ffa-85d8-52c16831870a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R486: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 246a0eda-61ab-4e39-aca7-ad9e9ef8ebe1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R487: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: c73168cc-092b-4f84-bea7-0fdbce009faf
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R488: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 153db477-d7d9-43da-8c84-d2647dadd084
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R489: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 63a96a42-6364-4960-95af-8ccb5254fd4c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R490: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: 57d4574e-94d7-4ba1-9943-8a042882c5a6
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R491: Code has been written to generate predictions on the validat...
- **Rubric ID**: 7c933a8b-1076-4e25-92c7-4193d8068e43
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R492: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: edad302b-5265-4402-8ece-a415f4603259
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R493: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: 2f2d00d0-a772-4689-b6de-1a29a483fcca
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R494: Code has been written to generate predictions on the test se...
- **Rubric ID**: 55f9d829-a884-46de-890c-18f965022fce
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using BART0_{Large}, the...

### R495: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: ba5c4e72-2a99-4797-83a3-26bec26a7ad9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using BART0_{Large}, the...

### R496: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: fdd501eb-4db3-4a71-9cf5-c9effe40e292
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of BART0_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using BART0_{Large}, the...

### R497: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: b4331a30-3a52-4962-877f-d3db0d437043
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using BART0_{Large}, the...

### R498: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: c07d9e32-37fc-41eb-951d-9021f5c240a5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using BART0_{Large}, the...

### R499: Code has been written to generate predictions on the validat...
- **Rubric ID**: fedbb9a8-37dc-4a7f-82b2-4830c13c11dd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R500: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 01f36af4-2014-45c4-b082-d211c79af885
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R501: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: c122ca97-1761-4ecf-a8fc-f1afe81cba83
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R502: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: d2c711e1-ca29-4383-af5f-77e90a36b877
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R503: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: 06f51676-5bea-471e-b6a0-6e643f2fe153
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R504: Code has been written to generate predictions on the validat...
- **Rubric ID**: 0bfbf2b3-9969-4c3c-970b-e740efc65e18
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R505: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 3be00c78-6b7c-4b6f-93c0-6b29c8634046
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R506: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: fb5f73f2-7cba-47f3-a2ba-d31c917e403f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R507: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: eff9b215-f64c-4ec4-ad38-847ccea0bd46
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R508: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: 1406507e-82e3-415a-86ca-8eccbf78a4b1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R509: Code has been written to generate predictions on the validat...
- **Rubric ID**: fedadfa6-3cfe-4cbf-913e-0f0f57b9784a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

### R510: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 67b1380d-d7dd-4b23-8738-20482de40b62
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

### R511: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: f8f757cf-4062-4399-ba87-b983dd722679
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

### R512: Code has been written to compute the Edit Success Rate for t...
- **Rubric ID**: 83467bda-2af9-49f8-aa08-d980954025c9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Edit Success Rate for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

### R513: Code has been written to compute the Exact Match Drop Ratio...
- **Rubric ID**: e275e080-824c-494e-b653-cff3e12166f1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Exact Match Drop Ratio (%) for the refined model, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

### R514: The code to evaluate the vanilla fine-tune method on all mod...
- **Rubric ID**: 4695e138-e60e-4ceb-a0e9-67824cda74fa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the vanilla fine-tune method on all model, dataset and fine-tuning configurations present in Table 3 has been executed and the Edit Success Rates and Exact Match Drop Ratios have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 3 has been executed and the Edit Success ...

### R515: The code to evaluate the replay with frequency-threshold bas...
- **Rubric ID**: 55ab6cc0-df48-421b-a87a-9d44ef165290
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the replay with frequency-threshold based forecasting method on all model, dataset and fine-tuning configurations present in Table 3 has been executed and the Edit Success Rates and Exact Match Drop Ratios have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 3 has been executed and the Edit Success ...

### R516: The code to evaluate the replay with fixed-logit based forec...
- **Rubric ID**: 4096d4f9-df7f-4940-8472-57575a2f066b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the replay with fixed-logit based forecasting method on all model, dataset and fine-tuning configurations present in Table 3 has been executed and the Edit Success Rates and Exact Match Drop Ratios have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 3 has been executed and the Edit Success ...

### R517: The code to evaluate the replay with trainable logit based f...
- **Rubric ID**: 675b58d4-5f25-4da3-922a-b705d0340f34
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the replay with trainable logit based forecasting method on all model, dataset and fine-tuning configurations present in Table 3 has been executed and the Edit Success Rates and Exact Match Drop Ratios have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 3 has been executed and the Edit Success ...

### R518: The code to evaluate the replay with representation based fo...
- **Rubric ID**: df4854e5-06fb-4a45-8c7a-895e9925ead9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the replay with representation based forecasting method on all model, dataset and fine-tuning configurations present in Table 3 has been executed and the Edit Success Rates and Exact Match Drop Ratios have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 3 has been executed and the Edit Success ...

### R519: The code to evaluate the ground truth forgetting replay meth...
- **Rubric ID**: 667fe5f7-5152-4af8-8f30-2426be620c7a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the ground truth forgetting replay method on all model, dataset and fine-tuning configurations present in Table 3 has been executed and the Edit Success Rates and Exact Match Drop Ratios have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 3 has been executed and the Edit Success ...

### R520: The recorded Exact Match Drop Ratios show that the ground tr...
- **Rubric ID**: 30c68f82-26d0-458d-ba87-2fac0619a8de
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded Exact Match Drop Ratios show that the ground truth forgetting replay method has the lowest Exact Match Drop Ratio for all evaluated model, dataset and fine-tuning setups.
- **Parent context**: The recorded Edit Success rates and Exact Match Drop Ratios match those presented in Table 3, with t...

### R521: The recorded Exact Match Drop Ratios show that the replay wi...
- **Rubric ID**: e9a20917-53be-4d5a-9415-2859a30ce6aa
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 3
- **Requirement**: The recorded Exact Match Drop Ratios show that the replay with representation based forecasting method has the second lowest Exact Match Drop Ratios for all evaluated model, dataset and fine-tuning setups, second only to the ground truth forgetting replay method.
- **Parent context**: The recorded Edit Success rates and Exact Match Drop Ratios match those presented in Table 3, with t...

### R522: The recorded Edit Success Rates and Exact Match Drop Ratios...
- **Rubric ID**: a8e920e2-4591-47bf-9101-bed468d8896f
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded Edit Success Rates and Exact Match Drop Ratios show that the vanilla fine-tuning method has the lowest Edit Success Rate and the highest Exact Match Drop Ratio for all evaluated model, dataset and fine-tuning setups.
- **Parent context**: The recorded Edit Success rates and Exact Match Drop Ratios match those presented in Table 3, with t...

### R523: The recorded Edit Success Rates for all configurations metho...
- **Rubric ID**: fc36825b-4d6c-4bf1-8877-81cb39d560eb
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The recorded Edit Success Rates for all configurations method, model and dataset configurations in the full fine-tuning setup are comparable i.e. within +/- 6% of each other.
- **Parent context**: The recorded Edit Success rates and Exact Match Drop Ratios match those presented in Table 3, with t...

### R524: All three of replay with frequency-threshold, trainable logi...
- **Rubric ID**: b69720bd-84b5-41f8-88be-335ea0c07ec0
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 3
- **Requirement**: All three of replay with frequency-threshold, trainable logit and representation based methods reduced forgetting compared to the random replay method, as measured by the EM Drop Ratio (where lower is better).
- **Parent context**: The recorded Edit Success rates and Exact Match Drop Ratios match those presented in Table 3, with t...

### R525: The recorded Exact Match Drop Ratios show that replay with f...
- **Rubric ID**: e973fe6d-4a1b-4133-b1fe-20133cf1c6de
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 3
- **Requirement**: The recorded Exact Match Drop Ratios show that replay with frequency-threshold, trainable logit, and representation-based forecasting mostly aligns with their forecasting performance (i.e. F1-scores) shown in Table 1, except for FLAN-T5_{Large} Full FT.
- **Parent context**: The recorded Edit Success rates and Exact Match Drop Ratios match those presented in Table 3, with t...

### R526: Code has been written to generate predictions on the test se...
- **Rubric ID**: ef59ba63-c979-411f-afcd-d40e0b1eb460
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the vanilla fine-tune method using BART0_{Large}, the P3 test se...

### R527: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: ad64104d-3859-4d7f-9f90-4210c63ed091
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the vanilla fine-tune method using BART0_{Large}, the P3 test se...

### R528: Code has been written to generate predictions on the validat...
- **Rubric ID**: bd958531-7af0-4b67-ab66-ea6713e115fd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU valid...

### R529: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 7cd4e05d-f185-4c22-80d5-8e4e30d2c4ca
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU valid...

### R530: Code has been written to generate predictions on the validat...
- **Rubric ID**: b2f9b760-3a33-4934-8bc8-35a970713582
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU val...

### R531: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: cd762592-86c9-4235-b0bd-cee4ce82275a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU val...

### R532: Code has been written to generate predictions on the validat...
- **Rubric ID**: cc988303-4787-4a76-9a91-b5256faf132f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{3B}, the MMLU validati...

### R533: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 9df116d6-1bd4-4c8a-a7ff-86791d83b113
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{3B}, the MMLU validati...

### R534: Code has been written to generate predictions on the test se...
- **Rubric ID**: f933a665-8403-47e8-88d8-f12d0105b4db
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the random replay method using BART0_{Large}, the P3 test set an...

### R535: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: d9ac0f35-0bac-42dd-8d02-c9a4f8ade812
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the random replay method using BART0_{Large}, the P3 test set an...

### R536: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: c68fac13-85da-4f32-aeee-706c392d2885
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R537: Code has been written to generate predictions on the validat...
- **Rubric ID**: facd327b-bf0c-4e27-b3fd-8d3b5074c2ca
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validat...

### R538: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 19c11b52-0598-49fc-b4ed-50cc1dfabc05
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validat...

### R539: Code has been written to generate predictions on the validat...
- **Rubric ID**: 7105699a-5afb-4f49-b564-866b9337e347
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R540: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 81b4d0cb-591b-4bd9-89da-44f0925c5c89
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R541: Code has been written to generate predictions on the validat...
- **Rubric ID**: efc0dc75-90e4-4a28-a916-c7d3dc1e03ea
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the random replay method using FLAN-T5_{3B}, the MMLU validation...

### R542: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 2af8b1a3-38aa-41d3-b55a-a8acf4f88235
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the random replay method using FLAN-T5_{3B}, the MMLU validation...

### R543: Code has been written to generate predictions on the test se...
- **Rubric ID**: c616b723-4a4b-435b-b96e-682546f3591f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R544: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: c6fdd560-77e2-42bf-bd84-3d667bbf0fe3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R545: Code has been developed to compute the ground-truth forgetti...
- **Rubric ID**: 41933187-1916-4924-bfaa-614062b8397a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground-truth forgetting binary indicator $z_{ij}$ for all pairs $(x_i, y_i) \in D_R^{\text{train}}$ and $(x_j, y_j) \in \hat{D}_{PT}$ by evaluating the copy of BART0_{Large} fine-tuned on each $(x_i, y_i)$ on the corresponding $j$th sample from $\hat{D}_{PT}$ and grading the output using the Exact Match score.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R546: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 86fc0136-60b4-4908-a0c0-65735d74f6e2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R547: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 2cdd87ac-650e-498b-b74f-2f760970a3f9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R548: Code has been written to generate predictions on the validat...
- **Rubric ID**: 68afb8b5-6d99-4e4c-a599-cb4733a71a7b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R549: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 51731563-efc9-45d3-a329-fb1c76e045ec
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R550: Code has been developed to compute the ground-truth forgetti...
- **Rubric ID**: ffe7f355-4c5a-46cd-b2a0-a9c81679d74e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground-truth forgetting binary indicator $z_{ij}$ for all pairs $(x_i, y_i) \in D_R^{\text{train}}$ and $(x_j, y_j) \in \hat{D}_{PT}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on each $(x_i, y_i)$ on the corresponding $j$th sample from $\hat{D}_{PT}$ and grading the output using the Exact Match score.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R551: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 2408fcf8-0d57-4a3d-9722-af5e279661ce
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R552: Code has been written to generate predictions on the validat...
- **Rubric ID**: 280f77d8-9d26-48cb-86d7-fb68b2b4a40b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R553: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 71639f96-b240-4127-a1a4-46cbfbb25fe9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R554: Code has been written to compute the ground-truth forgetting...
- **Rubric ID**: 866eb3b0-da99-43dd-844d-c821c3da5c63
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the ground-truth forgetting binary indicator $z_{ij}$ for all pairs $(x_i, y_i) \in D_R^{\text{train}}$ and $(x_j, y_j) \in \hat{D}_{PT}$ by using the copy of FLAN-T5_{Large} fine-tuned with the LoRA adaptation to model parameters on each $(x_i, y_i)$ on the corresponding $j$th sample from $\hat{D}_{PT}$ and grading the output using the Exact Match score.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R555: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 1fbfc600-037a-4e23-90df-ffe434c531e8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R556: Code has been written to generate predictions on the validat...
- **Rubric ID**: 72eba066-1a8e-4406-8edb-a37e5dfd9550
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R557: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 7582681b-f690-4655-8980-1ebc6a287119
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R558: Code has been developed to compute the ground-truth forgetti...
- **Rubric ID**: 25eee9c4-f9d0-4344-b255-63713a3df003
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground-truth forgetting binary indicator $z_{ij}$ for all pairs $(x_i, y_i) \in D_R^{\text{train}}$ and $(x_j, y_j) \in \hat{D}_{PT}$ by evaluating the copy of FLAN-T5_{3B} fine-tuned using the LoRA adaptation to model parameters on each $(x_i, y_i)$ on the corresponding $j$th sample from $\hat{D}_{PT}$ and grading the output using the Exact Match score.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R559: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: e97c7a6b-a0d2-4c99-9661-1ee7afef75ec
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R560: Code has been written to generate predictions on the test se...
- **Rubric ID**: c0bd0b39-fafe-4ce1-a141-002fddb0c7fc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using B...

### R561: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: c4d0f36c-1bf8-42da-88c5-ed04592431c5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using B...

### R562: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 4c5b954d-68d9-4bf7-b8ce-4e1a4d7b8cff
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using B...

### R563: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 7a9cb744-a376-41ed-91cf-d74e9d1cf154
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using B...

### R564: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 33912ee2-985d-4aeb-a5bc-44ae294b8d0b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R565: Code has been written to generate predictions on the validat...
- **Rubric ID**: e66854d3-3734-4cd0-8361-189d5a06a33e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R566: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 3bedbaa8-5100-4547-a612-78421ab0a9fb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R567: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: b0f0470d-5823-4194-b29d-33f2b34ac9e4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R568: Code has been written to generate predictions on the validat...
- **Rubric ID**: 0b1e626f-35f9-46f8-89f4-df2bf140c4b3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R569: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: d7eba443-2fec-4f56-b13a-74fb294405ca
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R570: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: c2caf11e-e533-43a0-b1fe-99dc8c2f8b5e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R571: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 2ae3d40e-cbee-4428-9988-06ebb34a4702
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R572: Code has been written to generate predictions on the validat...
- **Rubric ID**: 7cd01614-622c-4ea7-a8e0-f3be4c65a120
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R573: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 92c1d253-eb16-488b-ad06-1d75536d7a72
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R574: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: c8e48356-0dab-48e3-b2cc-9d150c74a68a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R575: Code has been written to generate predictions on the test se...
- **Rubric ID**: 1e25c554-0c01-4a47-99f7-835dde834f3c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using BA...

### R576: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: bb9252b1-4aff-4710-993a-566f65db0319
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using BA...

### R577: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 5369eaf1-b602-49be-a104-f8079ed48a12
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using BA...

### R578: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 333e63d8-4d69-4fcf-85f4-8aed4b0b3a8e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using BA...

### R579: Code has been written to generate predictions on the validat...
- **Rubric ID**: b1ca25c7-465a-44e7-ac0f-d67e654a497a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R580: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 7dcd81de-dc13-4cd0-91e2-da8f305b9356
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R581: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: f84e89e6-29bb-4737-a4c3-fddef85b5bac
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the representation forecasting model as described in Algorithm 4 and the learned encoder $h$.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R582: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: f54949cb-fc90-4f9f-a0bb-f793105464eb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R583: Code has been written to generate predictions on the validat...
- **Rubric ID**: 0cefa907-5edc-4b31-b3e6-0f7d4ac70840
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R584: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: a3073b08-a7f6-4de0-9fd7-f60bdab960ca
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R585: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 4fbad1c3-a64a-449d-9dee-3628bea1b3f8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R586: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 1c59ef09-764a-4202-a243-54db9f7018db
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R587: Code has been written to generate predictions on the validat...
- **Rubric ID**: 340b22ae-499c-4fa1-8d89-20b102a0f796
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset $D_R^{train}$ and $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R588: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 380f4576-4d60-41e9-bf55-6b9d55181d7b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R589: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 1f2d7e60-995a-48dc-929f-743547181876
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R590: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 6c18df34-3846-4ebd-909d-3baaae4ec512
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R591: Code has been written to generate predictions on the test se...
- **Rubric ID**: 075b6fb1-0a35-4b08-9b84-043f5d540377
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the test set of the P3 dataset using BART0_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using BART0_{Large}, t...

### R592: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 740b85af-7811-4656-ba3c-8799daaf0820
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using BART0_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using BART0_{Large}, t...

### R593: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 13c70b74-370b-46ab-98ba-95e77475ee80
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of BART0_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using BART0_{Large}, t...

### R594: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: e36bd0dc-442c-4b58-8d61-59155eb53969
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using BART0_{Large}, t...

### R595: Code has been written to generate predictions on the validat...
- **Rubric ID**: 133fb3ac-2c53-44f5-83da-29c681f0c655
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using FLAN-T5_{Large},...

### R596: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: 6a9c4c4a-d317-4e3e-ab18-54a450211d7d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using FLAN-T5_{Large},...

### R597: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 3cbc0dab-ae95-4b52-83e4-a844d8a5b4ab
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using FLAN-T5_{Large},...

### R598: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 9c44ed49-4ffa-4e81-8f49-afe12ef36217
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using FLAN-T5_{Large},...

### R599: Code has been written to generate predictions on the validat...
- **Rubric ID**: fbe3a850-a470-4ea1-a2b9-b60c255e256f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{Large} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using FLAN-T5_{Large},...

### R600: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: c7e71699-86e7-476f-8cca-7f1deb18ee63
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using FLAN-T5_{Large},...

### R601: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 65c82d0e-b316-4c85-898a-811c97039a5b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using FLAN-T5_{Large},...

### R602: Code has been written to generate predictions on the validat...
- **Rubric ID**: 13c7cd54-7b95-40ef-8073-38efc422e5f4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the validation set of MMLU using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset $D_R^{test}$ as described in Section 4.1.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

### R603: Code has been written to generate predictions on the pre-tra...
- **Rubric ID**: e73ec461-66a6-43e1-9507-0847407de787
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to generate predictions on the pre-training dataset $D_{PT}$ using FLAN-T5_{3B} and graded using the Exact Match score to create the dataset of correct pre-training samples, $\hat{D}_{PT}$, as described in Section 2 -- Forecasting Forgetting.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

### R604: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 0d82fde1-dcdd-4ac9-a6d2-a1a86cbd77d5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the ground-truth forgetting binary indicator $z_{ij}^{test}$ by evaluating the copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$ against $(x_j, y_j)$ and evaluating the output using the Exact Match score.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

### R605: Code has been written to compute the average Exact Match Dro...
- **Rubric ID**: 17c37f94-c2b2-40aa-81c4-b99d724f0238
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average Exact Match Drop Ratio (%) across each of the $|D_R^{test}|$-many refined models, as described in "Section 2 -- Model Refinement".
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

### R606: The code to evaluate the vanilla fine-tune method on all mod...
- **Rubric ID**: 14bc3d05-ddf5-434f-bc67-62db48be2525
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the vanilla fine-tune method on all model, dataset and fine-tuning configurations present in Table 4 has been executed and the Exact Match Drop Ratios have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 4 has been executed and the Exact Match D...

### R607: The code to evaluate the replay with frequency-threshold bas...
- **Rubric ID**: 99a4bfad-a80e-468c-a314-b1d0a94ebc37
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the replay with frequency-threshold based method on all model, dataset and fine-tuning configurations present in Table 4 has been executed and the Exact Match Drop Ratios have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 4 has been executed and the Exact Match D...

### R608: The code to evaluate the replay with fixed-logit based forec...
- **Rubric ID**: c12ea1e8-5d16-4533-b9b9-5a0ebf2b01cf
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the replay with fixed-logit based forecasting method on all model, dataset and fine-tuning configurations present in Table 4 has been executed and the Exact Match Drop Ratios have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 4 has been executed and the Exact Match D...

### R609: The code to evaluate the replay with trainable logit based f...
- **Rubric ID**: c89b83de-bbeb-4f4b-8605-b24f79a2ae1e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the replay with trainable logit based forecasting method on all model, dataset and fine-tuning configurations present in Table 4 has been executed and the Exact Match Drop Ratios have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 4 has been executed and the Exact Match D...

### R610: The code to evaluate the replay with representation based fo...
- **Rubric ID**: 0c5192a3-e9db-4d30-affe-1abbfaa72178
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the replay with representation based forecasting method on all model, dataset and fine-tuning configurations present in Table 4 has been executed and the Exact Match Drop Ratios have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 4 has been executed and the Exact Match D...

### R611: The code to evaluate the ground truth forgetting replay meth...
- **Rubric ID**: eec6bd65-93d0-4d63-9cd8-6b2a78f9bcc2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The code to evaluate the ground truth forgetting replay method on all model, dataset and fine-tuning configurations present in Table 4 has been executed and the Exact Match Drop Ratios have been recorded.
- **Parent context**: All code necessary to reproduce the results shown in Table 4 has been executed and the Exact Match D...

### R612: The recorded Exact Match Drop Ratios show that the ground tr...
- **Rubric ID**: d59425d1-58ab-491f-8901-2789f369a606
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded Exact Match Drop Ratios show that the ground truth forgetting replay method has the lowest Exact Match Drop Ratio for all evaluated model, dataset and fine-tuning setups.
- **Parent context**: The recorded Exact Match Drop ratios match those as presented in Table 4.

### R613: The recorded Exact Match Drop Ratios show that the replay wi...
- **Rubric ID**: 2989e54d-5471-468f-a448-4bec0573878b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded Exact Match Drop Ratios show that the replay with representation based forecasting method has the second lowest Exact Match Drop Ratios for all evaluated model, dataset and fine-tuning setups, second only to the ground truth forgetting replay method.
- **Parent context**: The recorded Exact Match Drop ratios match those as presented in Table 4.

### R614: The recorded Exact Match Drop ratios show that replaying exa...
- **Rubric ID**: 55bfda49-4a45-4c17-bc93-a1dac8a9da2d
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded Exact Match Drop ratios show that replaying examples forecasted to be forgotten by the representation-based forecasting method can reduce forgetting (EM Drop ratio) to roughly 2.2% for BART0_{Large} and < 0.1% for FLAN-T5_{Large} and FLAN-T5_{3B}.
- **Parent context**: The recorded Exact Match Drop ratios match those as presented in Table 4.

## Experimental Setup

### R615: Code has been written to fine-tune the head of BART0_{Large}...
- **Rubric ID**: ad7e2c72-facf-4ff1-9e92-d1198cc94479
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of BART0_{Large} on each $(x_i, y_i)$ in $D_R^{train}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", keeping the remaining parameters fixed, thereby creating $| D_R^{train} |$-many models.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R616: Code has been written to train the frequency-threshold based...
- **Rubric ID**: a2e25c2c-dc83-4dee-b026-ef880b63256d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$, and to find a value for $\gamma$ which maximises the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R617: Code has been written to fine-tune the head of BART0_{Large}...
- **Rubric ID**: ddcf5aab-6855-483d-8bed-e17f29725a68
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of BART0_{Large} on each $(x_i, y_i)$ in $D_R^{test}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", keeping the remaining parameters fixed, thereby creating $| D_R^{test} |$-many models.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R618: Code has been written to fine-tune the entire BART0_{Large}...
- **Rubric ID**: 7ba72065-8842-44f7-b6a2-1010543b707c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entire BART0_{Large} model on each $(x_i, y_i) \in D_R^{train}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", altering all parameters, thereby creating $|D_R^{train}|$-many models.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R619: Code has been written to train the frequency-threshold based...
- **Rubric ID**: 67375e9a-26b4-4518-beea-7d6f038529b5
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$, and to find a value for $\gamma$ which maximizes the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R620: Code has been written to fine-tune the entire BART0_{Large}...
- **Rubric ID**: ebcfb981-d9bf-4d17-b437-f8e499dc2be6
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entire BART0_{Large} model on each $(x_i, y_i) \in D_R^{test}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", altering all parameters, thereby creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R621: Code has been written to fine-tune the head of FLAN-T5_{Larg...
- **Rubric ID**: 2b2f6bc3-6da8-412a-ba51-cdb6a71741ca
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of FLAN-T5_{Large} on each $(x_i, y_i)$ in $D_R^{train}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", keeping the remaining parameters fixed, thereby creating $| D_R^{train} |$-many models.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R622: Code has been written to fine-tune the head of FLAN-T5_{Larg...
- **Rubric ID**: 664b7083-d11a-43a2-9b96-789b5002226a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of FLAN-T5_{Large} on each $(x_i, y_i)$ in $D_R^{test}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", keeping the remaining parameters fixed, thereby creating $| D_R^{test} |$-many models.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R623: Code has been written to fine-tune FLAN-T5_{Large} with LoRA...
- **Rubric ID**: ed1a3e41-2948-4918-961c-bf2c6f9d6bf8
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune FLAN-T5_{Large} with LoRA on each $(x_i, y_i)$ in $D_R^{train}$ using the hyperparameters in Section 4.1, modifying only LoRA parameters, thereby creating $|D_R^{train}|$ separate updated models.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R624: Code has been written to fine-tune FLAN-T5_{Large} with LoRA...
- **Rubric ID**: 2e386f4d-0c44-4b4d-bbae-73f68acf0ba8
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune FLAN-T5_{Large} with LoRA on each $(x_i, y_i)$ in $D_R^{test}$ using the hyperparameters in Section 4.1, modifying only LoRA parameters, thereby creating $|D_R^{test}|$ separate updated models.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R625: Code has been developed to fine-tune the entire FLAN-T5_{Lar...
- **Rubric ID**: cecd49d7-d327-4a34-b43f-6fd7ed97154d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entire FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{train}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", altering all parameters, thereby creating $|D_R^{train}|$-many models.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R626: Code has been written to train the frequency-threshold based...
- **Rubric ID**: 9c786e50-cbef-4729-b4bf-a8ef968c1e5b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$, and to find a value for $\gamma$ which maximizes the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R627: Code has been developed to fine-tune the entire FLAN-T5_{Lar...
- **Rubric ID**: ae16276e-f272-4a08-bb18-6fe1077d49d0
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entire FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{test}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", altering all parameters, thereby creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R628: Code has been written to fine-tune the head of FLAN-T5_{3B}...
- **Rubric ID**: 1ca94ce6-f3a9-46e4-ab56-c42fb840ad3e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of FLAN-T5_{3B} on each $(x_i, y_i) \in D_R^{train}$ using the specified hyperparameters in Section 4.1, keeping other parameters fixed, thereby creating $|D_R^{train}|$-many models; one for each train example.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R629: Code has been written to train the frequency-threshold based...
- **Rubric ID**: 4647cc68-8081-43e8-a1d2-4cd8a643ed8c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicators $z_{ij}$ to find an optimal value of $\gamma$ that maximizes the F1-score, as described in Section 3.1 -- Frequency-Threshold Based Forecasting.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R630: Code has been written to fine-tune the head of FLAN-T5_{3B}...
- **Rubric ID**: 633e2fd9-381e-4dba-9f4b-e0103f2ddb2c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of FLAN-T5_{3B} on each $(x_i, y_i) \in D_R^{test}$ using the specified hyperparameters in Section 4.1, keeping other parameters fixed, thereby creating $|D_R^{test}|$-many models; one for each test example.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R631: Code has been written to fine-tune FLAN-T5_{3B} with LoRA on...
- **Rubric ID**: a1aba794-8741-412d-9c9c-846b11e655a6
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune FLAN-T5_{3B} with LoRA on each $(x_i, y_i) \in D_R^{train}$ using the hyperparameters in Section 4.1, modifying only LoRA parameters, thereby creating $|D_R^{train}|$ separate updated models.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R632: Code has been written to fine-tune FLAN-T5_{3B} with LoRA on...
- **Rubric ID**: 9b7fffab-9fc8-40e4-8a2f-439c2bf1f135
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune FLAN-T5_{3B} with LoRA on each $(x_i, y_i) \in D_R^{test}$ using the hyperparameters in Section 4.1, modifying only LoRA parameters, thereby creating $|D_R^{test}|$ separate updated models.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R633: Code has been written to fine-tune the head of BART0_{Large}...
- **Rubric ID**: fa8fb85d-73d8-41da-b551-085cb3479f8d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of BART0_{Large} on each $(x_i, y_i) \in D_R^{test}$, keeping the remaining parameters fixed, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using BART0_{Large}, th...

### R634: Code has been written to fine-tune BART0_{Large} on each $(x...
- **Rubric ID**: 6a33e8b2-b16a-4a42-afe0-1465fac30302
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune BART0_{Large} on each $(x_i, y_i) \in D_R^{test}$, creating $|D_R^{test}|$-many models, with all parameters being updated (i.e. none are frozen).
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using BART0_{Large}, th...

### R635: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: b9a9ece2-e8c4-4770-8041-ef041d208783
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R636: Code has been written to fine-tune the head of FLAN-T5_{Larg...
- **Rubric ID**: 334991f3-c87c-4cee-9092-f21103310d36
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of FLAN-T5_{Large} on each $(x_i, y_i) \in D_R^{test}$ using the hyperparameters specified in "Section 4.1 -- Hyperparameters", thereby creating $|D_R^{test}|$ updated models with only the heads parameters altered.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, ...

### R637: Code has been developed to fine-tune FLAN-T5_{Large} with Lo...
- **Rubric ID**: de476f91-2cd2-4a9d-bae0-67c7c3db27b3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune FLAN-T5_{Large} with LoRA on each $(x_i, y_i) \in D_R^{test}$ using the specified hyperparameters in Section 4.1, to create separate updated models for each test example while only adjusting LoRA-specific parameters.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, th...

### R638: Code has been developed to fine-tune the entire FLAN-T5_{Lar...
- **Rubric ID**: 0f6ce5ce-9784-4344-a51d-cb5cbc3aa1dd
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entire FLAN-T5_{Large} model on each $(x_i, y_i)$ in $D_R^{test}$ using the full fine-tuning approach described in Section 4.1, creating $|D_R^{test}|$ updated models.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, ...

### R639: Code has been written to fine-tune the head of FLAN-T5_{3B}...
- **Rubric ID**: ba41bec6-2023-4c2c-90bd-a1bde60c7bba
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of FLAN-T5_{3B} on each $(x_i, y_i)$ in $D_{R}^{test}$ using the specified hyperparameters in "Section 4.1 -- Hyperparameters", freezing all other parameters, and thereby creating $|D_R^{test}|$-many separate models.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{3B}, the M...

### R640: Code has been developed to fine-tune FLAN-T5_{3B} with LoRA...
- **Rubric ID**: cf0aa19d-12d8-4587-94ca-a2f6344a163a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune FLAN-T5_{3B} with LoRA $(x_i, y_i)$ in $D_R^{test}$ as described in Section 4.1, creating $|D_R^{test}|$ updated models with only the LoRA parameters updated.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{3B}, the M...

### R641: Code has been written to fine-tune the head of BART0_{Large}...
- **Rubric ID**: c4ee6107-35dd-4f64-9644-27a7c441a4b4
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of BART0_{Large} on each $(x_i, y_i) \in D_R^{test}$, keeping the remaining parameters fixed, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R642: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: b8794e88-4e0c-41f6-bcf0-5d5e0ab344f2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R643: Code has been written to fine-tune the entirety of BART0_{La...
- **Rubric ID**: 45125811-250d-4772-ae77-38f1ab68abed
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entirety of BART0_{Large} on each $(x_i, y_i) \in D_R^{test}$, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R644: Code has been written to fine-tune the head of FLAN-T5_{Larg...
- **Rubric ID**: ca3afa12-1cfa-4b9c-9731-136c71a34b7f
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of FLAN-T5_{Large} on each $(x_i, y_i) \in D_R^{test}$, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R645: Code has been developed to fine-tune FLAN-T5_{Large} on each...
- **Rubric ID**: e17bd065-8ee3-4a4b-bdca-f7cbcb79aea9
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune FLAN-T5_{Large} on each $(x_i, y_i) \in D_R^{test}$ using the LoRA adaptation to model parameters, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R646: Code has been written to fine-tune the entirety of FLAN-T5_{...
- **Rubric ID**: 4d7d66c1-4295-49c8-82ec-2c8fe292c731
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entirety of FLAN-T5_{Large} on each $(x_i, y_i) \in D_R^{test}$, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R647: Code has been written to fine-tune the head of FLAN-T5_{3B}...
- **Rubric ID**: c4330280-52f9-438b-86bb-cb62510694dd
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of FLAN-T5_{3B} on each $(x_i, y_i) \in D_R^{test}$, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R648: Code has been developed to fine-tune FLAN-T5_{3B} on each $(...
- **Rubric ID**: 320e6cc4-8036-48ab-b9d4-40adf0768089
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune FLAN-T5_{3B} on each $(x_i, y_i) \in D_R^{test}$ using the LoRA adaptation to model parameters, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R649: Code has been written to fine-tune the head of BART0_{Large}...
- **Rubric ID**: 4b3bcf6e-4a24-40b6-a36b-5add495f4101
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of BART0_{Large} on each $(x_i, y_i) \in D_R^{test}$, keeping the remaining parameters fixed, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R650: Code has been written to fine-tune the entirety of BART0_{La...
- **Rubric ID**: 234ab267-fb24-45ec-b538-c5ab073444d2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entirety of BART0_{Large} on each $(x_i, y_i) \in D_R^{test}$, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R651: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: fb859942-8f9e-4240-8f85-0d1907f33d3f
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R652: Code has been written to fine-tune the head of FLAN-T5_{Larg...
- **Rubric ID**: c2c626f2-3bb6-406c-8618-d8515342455d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of FLAN-T5_{Large} on each $(x_i, y_i) \in D_R^{test}$, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R653: Code has been developed to fine-tune FLAN-T5_{Large} on each...
- **Rubric ID**: d0d8c6a3-477f-4e4a-9e7d-c783f1d9712c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune FLAN-T5_{Large} on each $(x_i, y_i) \in D_R^{test}$ using the LoRA adaptation to model parameters, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R654: Code has been written to fine-tune the entirety of FLAN-T5_{...
- **Rubric ID**: b48f6689-081c-4f6c-9d25-384bfd5c371c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entirety of FLAN-T5_{Large} on each $(x_i, y_i) \in D_R^{test}$, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R655: Code has been written to fine-tune the head of FLAN-T5_{3B}...
- **Rubric ID**: ce9ba178-3185-44e3-a0cb-f604ac865297
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of FLAN-T5_{3B} on each $(x_i, y_i) \in D_R^{test}$, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R656: Code has been written to fine-tune FLAN-T5_{3B} on each $(x_...
- **Rubric ID**: 54c359b4-1701-4016-84e9-cb1de188c93d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune FLAN-T5_{3B} on each $(x_i, y_i) \in D_R^{test}$ using the LoRA adaptation to model parameters, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R657: Code has been written to fine-tune the head of BART0_{Large}...
- **Rubric ID**: 3294c5ea-2c7c-4363-ab58-3742ef8ba3c3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of BART0_{Large} on each $(x_i, y_i) \in D_R^{test}$, keeping the remaining parameters fixed, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R658: Code has been written to fine-tune the entirety of BART0_{La...
- **Rubric ID**: b17ec18c-a17c-4805-9f64-79e4914fb160
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entirety of BART0_{Large} on each $(x_i, y_i) \in D_R^{test}$, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R659: Code has been written to fine-tune the head of FLAN-T5_{Larg...
- **Rubric ID**: c2216682-79b3-43ce-8cb0-bd7d2852b048
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of FLAN-T5_{Large} on each $(x_i, y_i) \in D_R^{test}$, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R660: Code has been developed to fine-tune FLAN-T5_{Large} on each...
- **Rubric ID**: 1e3f51cb-7c6a-4608-8bbe-d0701eee659e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune FLAN-T5_{Large} on each $(x_i, y_i) \in D_R^{test}$ using the LoRA adaptation to model parameters, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R661: Code has been developed to fine-tune the entirety of FLAN-T5...
- **Rubric ID**: d17d2a39-7cee-4aca-9fc3-5cc303aa2cdd
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of FLAN-T5_{Large} on each $(x_i, y_i) \in D_R^{test}$, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R662: Code has been written to fine-tune the head of FLAN-T5_{3B}...
- **Rubric ID**: 3a22e846-d40a-44ba-a1cd-10430eeedd76
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the head of FLAN-T5_{3B} on each $(x_i, y_i) \in D_R^{test}$, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R663: Code has been written to fine-tune FLAN-T5_{3B} on each $(x_...
- **Rubric ID**: f100d158-8396-4707-8d35-12f0cc1abaea
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune FLAN-T5_{3B} on each $(x_i, y_i) \in D_R^{test}$ using the LoRA adaptation to model parameters, creating $|D_R^{test}|$-many models.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R664: Code has been developed to fine-tune the entire FLAN-T5_{Lar...
- **Rubric ID**: a23d9d0e-d0bf-4292-9105-43f127fa8b89
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entire FLAN-T5_{Large} model on a random subset of $D_R^{test}$ of at least 40 samples using the hyperparameters in "Section 4.1 -- Hyperparameters", altering all parameters and fine-tuning on one sample at a time.
- **Parent context**: Figure 3 has been replicated.

### R665: Code has been written to fine-tune the entire FLAN-T5_{Large...
- **Rubric ID**: 1c0c6161-e14f-4882-be7f-0685f68d2239
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entire FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{train}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", altering all parameters, thereby creating $|D_R^{train}|$-many models.
- **Parent context**: The frequency-threshold based forecasting function $g$ has been developed, as described in Section 3...

### R666: Code has been written to train the frequency-threshold based...
- **Rubric ID**: e14969cd-5ac6-4364-887f-f1a2a0ffbc21
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$, and to find a value for $\gamma$ which maximizes the F1-score, as described in Section 3.1.
- **Parent context**: The frequency-threshold based forecasting function $g$ has been developed, as described in Section 3...

### R667: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 2c535d88-5266-4209-b966-d9bb80c93d93
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R668: Code has been written to fine-tune all parameters of BART0_{...
- **Rubric ID**: 2052b2c4-a173-40fb-9efc-a3c65c975160
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune all parameters of BART0_{Large} on each $(x_i, y_i)$ in $D_R^{train}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", thereby creating $| D_R^{train} |$-many models.
- **Parent context**: Table 2 has been replicated.

### R669: Code has been written to fine-tune all parameters of BART0_{...
- **Rubric ID**: 78edb4b3-01b7-48c3-a5bf-3329e9a2665e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune all parameters of BART0_{Large} on each $(x_i, y_i)$ in $D_R^{test}$ using the hyperparameters in Section 4.1 -- Hyperparameters, thereby creating $| D_R^{test} |$-many models.
- **Parent context**: Table 2 has been replicated.

### R670: Code has been developed to train the frequency-threshold bas...
- **Rubric ID**: 00a29abe-6215-4eea-9b9f-c5034a40b213
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$, and to find a value for $\gamma$ which maximises the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using BART0_{Larg...

### R671: Code has been developed to fine-tune the entirety of the BAR...
- **Rubric ID**: 51ea69d7-3704-4d3e-9270-104e7e1168cd
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the BART0_{Large} model on each $(x_i, y_i) \in D_R^{test}$, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using BART0_{Large}, the P3 test set ...

### R672: Code has been developed to fine-tune the entirety of the FLA...
- **Rubric ID**: ee1f1e26-a0f0-4296-bf6b-6a1882df297a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{test}$, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU valid...

### R673: Code has been developed to fine-tune the FLAN-T5_{Large} mod...
- **Rubric ID**: 49932ad3-4ad1-4896-a7f1-cc7cef0c5060
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU valid...

### R674: Code has been developed to fine-tune the FLAN-T5_{3B} model...
- **Rubric ID**: 568a1a5a-95b3-4ae1-9bb2-3779ee001973
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{3B}, the MMLU validati...

### R675: Code has been developed to fine-tune the entirety of the BAR...
- **Rubric ID**: 5d52e92d-618b-4e06-88f5-d20ba513f3a9
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the BART0_{Large} model on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing)..
- **Parent context**: Code has been written to evaluate the random replay method using BART0_{Large}, the P3 test set and ...

### R676: Code was written to fine-tune the BART0_{Large} model on a r...
- **Rubric ID**: 8feb9ab9-d6b0-4dda-96f3-820aed5f9f4a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code was written to fine-tune the BART0_{Large} model on a random mini-batch of 8 examples from $\hat{D}_{PT}$ every 10 training steps using distillation loss against the base BART0_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the random replay method using BART0_{Large}, the P3 test set and ...

### R677: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 1563c8c9-fc6a-40de-a569-37ef08bea30e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R678: Code has been developed to fine-tune the entirety of the FLA...
- **Rubric ID**: bba009e9-841a-4bc9-8459-b2c8f6f415ca
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R679: Code was developed to fine-tune the FLAN-T5_{Large} model on...
- **Rubric ID**: 1340d3a4-0387-41e6-9c49-d139e26e5ea6
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the FLAN-T5_{Large} model on a random mini-batch of 8 examples from $\hat{D}_{PT}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R680: Code has been developed to fine-tune the FLAN-T5_{Large} mod...
- **Rubric ID**: 3ada421d-0cc6-4823-a840-aad6d1fb1dfd
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R681: Code was developed to fine-tune the FLAN-T5_{Large} model us...
- **Rubric ID**: 7a8914cc-82e5-4c01-a807-99e886a01056
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on a random mini-batch of 8 examples from $\hat{D}_{PT}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R682: Code has been developed to fine-tune the FLAN-T5_{3B} model...
- **Rubric ID**: a1852e8e-461e-4348-9e94-e0453768a471
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{3B}, the MMLU validation s...

### R683: Code was developed to fine-tune the FLAN-T5_{3B} model using...
- **Rubric ID**: 6a47cbef-208a-4d37-9652-820e55569683
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on a random mini-batch of 4 examples from $\hat{D}_{PT}$ every 5 training steps using distillation loss against the base FLAN-T5_{3B} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{3B}, the MMLU validation s...

### R684: Code has been written to fine-tune the entire BART0_{Large}...
- **Rubric ID**: b499bdb8-bae6-4899-88c5-c764742a13a0
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entire BART0_{Large} model on each $(x_i, y_i) \in D_R^{train}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", altering all parameters, thereby creating $|D_R^{train}|$-many models.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R685: Code has been written to train the frequency-threshold based...
- **Rubric ID**: 78954bef-5140-4e2d-a477-879fed50f0dc
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$, and to find a value for $\gamma$ which maximizes the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R686: Code has been developed to fine-tune the entirety of the BAR...
- **Rubric ID**: 96021833-5291-44d0-8095-baa7fa8805ad
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the BART0_{Large} model on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R687: Code was developed to fine-tune the BART0_{Large} model on a...
- **Rubric ID**: 9bfacdd0-06f7-4fb2-8ab2-5cedaa330449
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the BART0_{Large} model on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten by $g$ every 10 training steps using distillation loss against the base BART0_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R688: Code has been developed to fine-tune the entire FLAN-T5_{Lar...
- **Rubric ID**: 26d995a3-7abc-4d7b-a72b-6105b9201842
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entire FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{train}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", altering all parameters, thereby creating $|D_R^{train}|$-many models.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R689: Code has been written to train the frequency-threshold based...
- **Rubric ID**: e003e3e3-219f-4fdc-bd8e-1f169c3886b2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$, and to find a value for $\gamma$ which maximizes the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R690: Code has been developed to fine-tune the entirety of the FLA...
- **Rubric ID**: 3262101b-1a97-44e5-8fcd-e722a5f577c7
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R691: Code has been developed to fine-tune the entire FLAN-T5_{Lar...
- **Rubric ID**: ca17c287-5935-4d69-9172-c13a4b4733d5
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entire FLAN-T5_{Large} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{train}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", thereby creating $|D_R^{train}|$-many models.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R692: Code has been written to train the frequency-threshold based...
- **Rubric ID**: 7a68b940-d0f0-4779-944f-773cd3055c98
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$, and to find a value for $\gamma$ which maximizes the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R693: Code has been developed to fine-tune the FLAN-T5_{Large} mod...
- **Rubric ID**: ec09fde5-53fe-4262-9579-3e4389c2c872
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R694: Code has been written to fine-tune the entire FLAN-T5_{3B} m...
- **Rubric ID**: a2e89801-c75d-4417-851d-7e9b609a35ce
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entire FLAN-T5_{3B} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{train}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", thereby creating $|D_R^{train}|$-many models.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R695: Code has been written to train the frequency-threshold based...
- **Rubric ID**: b55e2ce4-8d26-4fdf-a779-7ae2f447744b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$, and to find a value for $\gamma$ which maximizes the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R696: Code has been developed to fine-tune the FLAN-T5_{3B} model...
- **Rubric ID**: ce60c6d7-3fc9-42af-98d9-9355f1350ab4
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R697: Code has been written to fine-tune the entirety of the BART0...
- **Rubric ID**: 5ddb3b3f-0a22-4751-b1bb-2ef71f2db11b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entirety of the BART0_{Large} model on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using BAR...

### R698: Code has been developed to fine-tune the entirety of the FLA...
- **Rubric ID**: c7abdfcb-6c43-45ef-9e7a-692aa58289e2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R699: Code has been developed to fine-tune the FLAN-T5_{Large} mod...
- **Rubric ID**: 166750d2-bb17-4137-8d1c-50e46d17e29e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R700: Code has been developed to fine-tune the FLAN-T5_{3B} model...
- **Rubric ID**: 237aa8b7-7d3b-47f5-adef-86d4a56d35a0
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R701: Code has been developed to fine-tune the entirety of the BAR...
- **Rubric ID**: 6416c1e2-2a0f-422a-a2b0-6422cd073c39
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the BART0_{Large} model on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using BART...

### R702: Code was developed to fine-tune the BART0_{Large} model on a...
- **Rubric ID**: 47158307-0bad-43ad-b071-f3c22f6a73a9
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the BART0_{Large} model on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 10 training steps using distillation loss against the base BART0_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using BART...

### R703: The P3 test split in https://github.com/INK-USC/ReCross/blob...
- **Rubric ID**: 6f90b722-06ff-42f3-85cd-066287c7c074
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The P3 test split in https://github.com/INK-USC/ReCross/blob/main/data/ was used when evaluating forecasting methods using the BART0_{Large} model, specifically using the following tasks: super_glue-wsc.fixed, winogrande-winogrande_xl, super_glue-cb, super_glue-rte, anli, super_glue-copa, hellaswag and super_glue-wic.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using BART0_{Larg...

### R704: Code has been developed to fine-tune the entirety of the FLA...
- **Rubric ID**: f953deff-0c29-481b-af72-bf03e1a493e1
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R705: Code was developed to fine-tune the FLAN-T5_{Large} model on...
- **Rubric ID**: 93b1d676-4a55-429e-bebf-a41cedb001dd
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the FLAN-T5_{Large} model on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R706: Code has been developed to fine-tune the FLAN-T5_{Large} mod...
- **Rubric ID**: 334386b6-e0f1-48f7-9c5a-7ae78f86c08a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R707: Code has been developed to fine-tune the FLAN-T5_{3B} model...
- **Rubric ID**: 2acb6caa-bf14-4cca-9a20-2ff7cc5cd152
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R708: Code has been developed to fine-tune the entirety of the BAR...
- **Rubric ID**: bd3db6e1-5107-4d7e-bf65-aec801584fa3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the BART0_{Large} model on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using BART0_{Large}, the...

### R709: Code has been developed to fine-tune the entirety of the FLA...
- **Rubric ID**: 7b26d7ba-71d0-4929-8d7c-2df49d1cc2c6
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R710: Code has been developed to fine-tune the FLAN-T5_{3B} model...
- **Rubric ID**: 2d80cfe9-96b1-4769-b68e-100c39beba95
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

### R711: Code has been written to fine-tune the entirety of the BART0...
- **Rubric ID**: 50fcdcf5-78e1-4c0e-96ec-0bd9dbd7c941
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entirety of the BART0_{Large} model on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the vanilla fine-tune method using BART0_{Large}, the P3 test se...

### R712: Code has been developed to fine-tune the entirety of the FLA...
- **Rubric ID**: 2206c259-e988-4deb-87a6-f626ad419b12
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU valid...

### R713: Code has been developed to fine-tune the FLAN-T5_{Large} mod...
- **Rubric ID**: e79e61c0-69d0-4cf5-ad9b-09debce73f71
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU val...

### R714: The original validation split of the MMLU dataset containing...
- **Rubric ID**: f6e9cc0f-1a05-4154-8c41-83b9c73f1f42
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The original validation split of the MMLU dataset containing 57 tasks, available at https://people.eecs.berkeley.edu/~hendrycks/data.tar, was used when evaluating forecasting methods using FLAN-T5_{3B}.
- **Parent context**: The correct dataset splits and tasks were used when evaluating forecasting methods using FLAN-T5_{3B...

### R715: Code has been written to fine-tune the entirety of the BART0...
- **Rubric ID**: 2b9e26dc-5921-40d9-90f3-145899467a82
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entirety of the BART0_{Large} model on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the random replay method using BART0_{Large}, the P3 test set an...

### R716: Code has been developed to fine-tune the entirety of the FLA...
- **Rubric ID**: 7895f6b5-b880-4ef2-97ff-e2cf0ae1b0f5
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validat...

### R717: Code has been developed to fine-tune the FLAN-T5_{Large} mod...
- **Rubric ID**: 9fcff492-f49c-4ec6-8dce-62ca072fa90b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R718: Code has been developed to fine-tune the FLAN-T5_{3B} model...
- **Rubric ID**: a973e75d-9771-495e-8319-88074250e040
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the random replay method using FLAN-T5_{3B}, the MMLU validation...

### R719: Code has been written to fine-tune the entire BART0_{Large}...
- **Rubric ID**: 777a8827-eb1b-4093-9e56-dad06bfe2de8
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entire BART0_{Large} model on each $(x_i, y_i) \in D_R^{train}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", altering all parameters, thereby creating $|D_R^{train}|$-many models.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R720: Code has been written to train the frequency-threshold based...
- **Rubric ID**: cef9c85d-da16-4c57-beff-f589a27f41c2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$, and to find a value for $\gamma$ which maximizes the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R721: Code has been written to fine-tune the entirety of the BART0...
- **Rubric ID**: db41c3a0-889d-4f72-84d1-d3e453f50de3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entirety of the BART0_{Large} model on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R722: Code has been developed to fine-tune the entire FLAN-T5_{Lar...
- **Rubric ID**: 95f45cd9-d3c5-439c-85d8-69beea843c98
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entire FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{train}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", altering all parameters, thereby creating $|D_R^{train}|$-many models.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R723: Code has been developed to train the frequency-threshold bas...
- **Rubric ID**: 946063fa-ea71-45e9-8494-88942191046f
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$, and to find a value for $\gamma$ which maximizes the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R724: Code has been developed to fine-tune the entirety of the FLA...
- **Rubric ID**: 19ce0534-e406-4748-9894-0bc38cf76715
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R725: Code has been developed to fine-tune the entire FLAN-T5_{Lar...
- **Rubric ID**: 6f3dbd99-6db7-49b5-b84b-a76c354b0b7a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entire FLAN-T5_{Large} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{train}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", thereby creating $|D_R^{train}|$-many models.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R726: Code has been developed to train the frequency-threshold bas...
- **Rubric ID**: 68d985bf-831c-4e48-8a72-ce01aca34095
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$, and to find a value for $\gamma$ which maximizes the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R727: Code has been developed to fine-tune the FLAN-T5_{Large} mod...
- **Rubric ID**: 70e5a2d5-f5f6-40b4-ad53-0f1902385bed
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R728: Code has been developed to fine-tune the entire FLAN-T5_{3B}...
- **Rubric ID**: 9984fbbb-8bb5-4a00-9e59-4a4130829169
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entire FLAN-T5_{3B} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{train}$ using the hyperparameters in "Section 4.1 -- Hyperparameters", thereby creating $|D_R^{train}|$-many models.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R729: Code has been developed to train the frequency-threshold bas...
- **Rubric ID**: 92f6c652-4ccf-404a-905b-7d016525342a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$, and to find a value for $\gamma$ which maximizes the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to train the frequency-threshold based forecasting classifier $g$ using $D_R^{...

### R730: Code has been developed to fine-tune the FLAN-T5_{3B} model...
- **Rubric ID**: d697f0f1-48d0-4a7b-bca5-27f6bf1c0167
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R731: Code has been written to fine-tune the entirety of the BART0...
- **Rubric ID**: 13698680-73f8-4a48-8d0d-ff4ade490ee9
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entirety of the BART0_{Large} model on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using B...

### R732: Code has been developed to fine-tune the entirety of the FLA...
- **Rubric ID**: bd997469-8937-4fcb-8a87-77de702df0cf
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R733: Code has been developed to fine-tune the FLAN-T5_{Large} mod...
- **Rubric ID**: 4933b798-afa6-43b1-a65a-c7ced61b9eb8
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R734: Code has been developed to fine-tune the FLAN-T5_{3B} model...
- **Rubric ID**: 8eac4bc6-a8b8-40a3-b038-1e829bbb9dac
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R735: Code has been written to fine-tune the entirety of the BART0...
- **Rubric ID**: 87f0524b-bac7-4978-9d30-9a812b259443
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entirety of the BART0_{Large} model on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using BA...

### R736: Code has been developed to fine-tune the entirety of the FLA...
- **Rubric ID**: 8512e379-cb22-4e4a-9941-f79d4eb2a8da
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R737: Code has been developed to fine-tune the FLAN-T5_{Large} mod...
- **Rubric ID**: 3fcfdd5b-b675-4e92-beef-16599074d1ae
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R738: Code has been developed to fine-tune the FLAN-T5_{3B} model...
- **Rubric ID**: eb2d9378-36e4-4ce6-b2bd-35e35505fbe1
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R739: Code has been written to fine-tune the entirety of the BART0...
- **Rubric ID**: 524c27cf-b64a-4eb4-b43f-be37972e22ee
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to fine-tune the entirety of the BART0_{Large} model on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using BART0_{Large}, t...

### R740: Code has been developed to fine-tune the entirety of the FLA...
- **Rubric ID**: c963875e-1d5e-4895-a8b5-d9caeba1cc44
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the entirety of the FLAN-T5_{Large} model on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using FLAN-T5_{Large},...

### R741: Code has been developed to fine-tune the FLAN-T5_{Large} mod...
- **Rubric ID**: c14d0fdf-da77-438c-9993-5b39daac6091
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using FLAN-T5_{Large},...

### R742: Code has been developed to fine-tune the FLAN-T5_{3B} model...
- **Rubric ID**: a4593b27-8f17-420a-853e-81bb6130ec33
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

## Method Implementation

### R743: Code has been developed to train the frequency-threshold bas...
- **Rubric ID**: 247fe90c-6519-4b13-82ce-071ed4732e9c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$, and to find a value for $\gamma$ that maximises the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R744: Code has been written to train the frequency-threshold based...
- **Rubric ID**: a4d33abb-6681-47b5-bffa-4cb75682b145
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$ to determine a value for $\gamma$ that maximizes the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R745: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 6b3ec7c4-16f3-4459-9e0a-b5eed97384d0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{La...

### R746: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 812a1fce-bdc9-425f-ad5d-bbea9b5a14ea
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R747: Code has been written to train the frequency-threshold based...
- **Rubric ID**: 216b1eef-64a3-4608-a118-a29d393ed4cd
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train the frequency-threshold based forecasting function $g$ on $D_R^{train}$ using the binary indicator $z_{ij}$ to determine a value for $\gamma$ that maximizes the F1-score, as described in Section 3.1.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R748: Code has been written to apply the frequency-threshold based...
- **Rubric ID**: e9f2c0bb-19d5-46c8-a4cd-364a81008625
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to apply the frequency-threshold based forecasting function $g$ to every sample $(x_i, y_i) \in D_R^{test}$ and $(x_j, y_j) \in \hat{D}_{PT}$, producing a predicted forgetting indicator $\hat{z}_{ij}^{test}$.
- **Parent context**: Code has been written to evaluate the frequency-threshold based forecasting method using FLAN-T5_{3B...

### R749: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 1d7f7602-c30c-494e-a19e-3b72c553cbb2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the logit-based forecasting model as described in Algorithm 2, where the encoding function $h$ is the final layer of the base BART0_{Large} model and $f_0$ is the base BART0_{Large} model, as described in Section 4.2.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using BART0_{Large}, th...

### R750: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 84389cf1-c54e-4d6a-9056-f5b94025690c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the logit-based forecasting model as described in Algorithm 2, where the encoding function $h$ is the final layer of the base BART0_{Large} model and $f_0$ is the base BART0_{Large} model, as described in Section 4.2.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using BART0_{Large}, th...

### R751: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: f6f63fc9-e405-4906-a356-698343aaaa1d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the logit-based forecasting model as described in Algorithm 2, where the encoding function $h$ is the final layer of the base FLAN-T5_{Large} model and $f_0$ is the base FLAN-T5_{Large} model, as described in Section 4.2.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, ...

### R752: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 35d51993-fa63-4189-ba15-2e33fc9bc019
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, th...

### R753: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: fbae7478-32c8-45a9-8c86-1eda3d1a1110
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the logit-based forecasting model as described in Algorithm 2, where the encoding function $h$ is the final layer of the base FLAN-T5_{Large} model and $f_0$ is the base FLAN-T5_{Large} model, as described in Section 4.2.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, th...

### R754: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: c0294ff3-ddf6-4921-8b02-4af6a799b76b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting indicator $\hat{z}_{ij}^{test}$ using the fixed-logit based forecasting model as described in Algorithm 2, with the final layer of the base FLAN-T5_{Large} model serving as the encoding function $h$.
- **Parent context**: Code has been developed to evaluate the fixed-logit based forecasting method using FLAN-T5_{Large}, ...

### R755: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: afdb6afc-8cd7-44a0-b988-e1011fb004a8
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the logit-based forecasting model as described in Algorithm 2. The encoding function $h$ is the final layer representation of the base FLAN-T5_{3B} model, as described in Section 3.2.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{3B}, the M...

### R756: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 619f34b6-cd0e-4c9e-b761-9ef9bb0959ef
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting indicator $\hat{z}_{ij}^{test}$ using the fixed-logit based forecasting model as described in Algorithm 2, with the final layer of the base FLAN-T5_{3B} model serving as the encoding function $h$.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{3B}, the M...

### R757: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 838dad0b-eee7-4430-918b-4d968f0b716d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{3B}, the M...

### R758: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 723ada6b-d58c-4d20-a62a-bfb146424f88
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting indicator $\hat{z}_{ij}^{test}$ using the fixed-logit based forecasting model as described in Algorithm 2, with the final layer of the base FLAN-T5_{3B} model serving as the encoding function $h$.
- **Parent context**: Code has been written to evaluate the fixed-logit based forecasting method using FLAN-T5_{3B}, the M...

### R759: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 42305fe2-bf2f-4fd3-8448-85c4ff71117e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R760: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: d5f0be79-1af6-4585-8e29-b3db281ce39a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R761: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 1fc4211f-515b-46b5-b81e-ac4d4e9151bb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R762: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 9e028f66-cf6b-4889-8f51-48c8e33bca43
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R763: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: aabe3c2c-7588-407a-ac0a-99c2bb535179
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R764: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: da66880b-d4e7-47b4-9d3e-f9895265cde2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R765: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: d82b66ce-412e-452c-a444-57349b104df5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R766: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 884236f3-00f5-4a3a-af14-910de658e11b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R767: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 2a872b27-0b80-42fc-811d-b884a79ab07b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R768: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 2efd9093-545c-4c33-89ec-8e3f25c2fe66
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{Larg...

### R769: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 4b3ed262-de8b-4568-be6d-92b45fec6ee3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R770: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 2541e67b-6a49-4a5a-af08-3c9700575c27
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R771: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 912f6664-ef7d-4052-9fb9-4b99bd7a8d6a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using FLAN-T5_{3B},...

### R772: Code has been written to compute the bias term $b_j$ for all...
- **Rubric ID**: efdfced2-6624-4784-9fdc-f8a6330c61e2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the bias term $b_j$ for all $(x_j, y_j) \in D_R^{train}$ as described in Section 3.3 -- Forecasting with Frequency Priors.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R773: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 03436229-eae5-448f-a2bd-42c0a39c4764
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R774: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 2945f439-bad1-4cfb-ad95-b229e1ebdd5c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the representation forecasting model as described in Algorithm 4 and the learned encoder $h$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R775: Code has been written to compute the bias term $b_j$ for all...
- **Rubric ID**: c3170323-347b-4c25-ae38-482bc26acabb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the bias term $b_j$ for all $(x_j, y_j) \in D_R^{train}$ as described in Section 3.3 -- Forecasting with Frequency Priors.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R776: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: bfe35a39-16bc-41d1-b856-788b5e143bb5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R777: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 87404145-140f-4233-b1b1-35ab2173c20b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ by implementing the representation forecasting model as described in Algorithm 4 using the learned encoder $h$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R778: Code has been written to compute the bias term $b_j$ for all...
- **Rubric ID**: 26b144ee-fb28-4c54-aa2f-9025c33ef5c1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the bias term $b_j$ for all $(x_j, y_j) \in D_R^{train}$ as described in Section 3.3 -- Forecasting with Frequency Priors.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R779: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 07e551cf-dc3e-4a65-9c64-6b2c10d755a1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R780: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 18cd87bc-7b28-4827-b548-c87deb89903e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ by implementing the representation forecasting model as described in Algorithm 4 using the learned encoder $h$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R781: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 06406544-f297-4e01-8981-16dec5b0f99c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R782: Code has been written to compute the bias term $b_j$ for all...
- **Rubric ID**: c2552ea4-9ade-4b0c-9a1b-696b72d9d163
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the bias term $b_j$ for all $(x_j, y_j) \in D_R^{train}$ as described in Section 3.3 -- Forecasting with Frequency Priors.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R783: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 2227fe4c-7b57-42d5-8303-d778d39db3de
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R784: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 70c71479-8a4a-4d76-a276-7bcf228f4913
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ by implementing the representation forecasting model as described in Algorithm 4 using the learned encoder $h$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R785: Code has been written to compute the bias term $b_j$ for all...
- **Rubric ID**: 10adb80d-6568-472a-8762-48ee498af4e1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the bias term $b_j$ for all $(x_j, y_j) \in D_R^{train}$ as described in Section 3.3 -- Forecasting with Frequency Priors.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R786: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 05fc0593-2186-47ae-be57-a8b85cfe61e7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{Large...

### R787: Code has been written to compute the bias term $b_j$ for all...
- **Rubric ID**: 702b36ce-16eb-4c64-99d1-0b21256aefb5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the bias term $b_j$ for all $(x_j, y_j) \in D_R^{train}$ as described in Section 3.3 -- Forecasting with Frequency Priors.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R788: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: da085143-5b4f-4b57-9ed1-44708b910013
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R789: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 9a9fb048-fbc2-4401-bca4-d908b714c2f8
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ by implementing the representation forecasting model as described in Algorithm 4 using the learned encoder $h$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R790: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: ce2bdd3a-dcb1-4f2c-9272-8ae16bc88bd0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R791: Code has been written to compute the bias term $b_j$ for all...
- **Rubric ID**: b5968b1c-bd33-4e1b-8cc9-2214bacf8550
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the bias term $b_j$ for all $(x_j, y_j) \in D_R^{train}$ as described in Section 3.3 -- Forecasting with Frequency Priors.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R792: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 9131a08e-ad38-4b29-aa93-987657ff4070
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R793: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: b124446f-d27f-4d81-9631-bbf503043071
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ by implementing the representation forecasting model as described in Algorithm 4 using the learned encoder $h$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using FLAN-T5_{3B}, ...

### R794: Code has been written to train the encoding function $h$ for...
- **Rubric ID**: e5a4c777-d9bd-46d3-9bbe-d3c40bb2c734
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train the encoding function $h$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F, though without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R795: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: bde68381-264f-4a9f-bea5-dda7ec5a5db2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the prior-free representation forecasting model as described in Algorithm 4 using the learned encoder $h$ and without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R796: Code has been written to train the encoding function $h$ for...
- **Rubric ID**: 14a499b1-66c7-4d83-8c1d-d5e43b42c6c7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train the encoding function $h$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix, though without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R797: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 2ff83e17-0dab-4104-af72-0d0021e625b3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the prior-free representation forecasting model as described in Algorithm 4 using the learned encoder $h$ and without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R798: Code has been written to train the encoding function $h$ for...
- **Rubric ID**: cb26630e-5657-417f-b9d1-0badb9fe6556
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F, though without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R799: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: ee0315a5-01a9-4664-b083-4d6d4faedd0f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the prior-free representation forecasting model as described in Algorithm 4 using the learned encoder $h$ and without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R800: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 530139c3-dec2-4995-9220-abd70433da77
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R801: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: bdca81d2-542c-442d-b81f-6203b1c5b057
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F, though without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R802: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: d4a6677b-e075-4460-beff-9aab4b65c513
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the prior-free representation forecasting model as described in Algorithm 4 using the learned encoder $h$ and without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R803: Code has been written to train the encoding function $h$ for...
- **Rubric ID**: 5e10455a-c362-4039-bb03-279e2f90c906
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F, though without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R804: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: b0659e93-9112-4a2d-8e78-7a32e487e42e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the prior-free representation forecasting model as described in Algorithm 4 using the learned encoder $h$ and without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R805: Code has been written to train the encoding function $h$ for...
- **Rubric ID**: 0c1e1c80-f73e-4495-a16b-b94bd1d25199
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train the encoding function $h$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F, though without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R806: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 8aeafacd-658d-467f-88ab-ef2c89e3b38c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the prior-free representation forecasting model as described in Algorithm 4 using the learned encoder $h$ and without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R807: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: cd2e0b25-85e4-4777-9b75-7a15e2031d75
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R808: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: a5dbb412-beda-4b13-b6c9-6618b3a01416
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F, though without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R809: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 35cf58a8-4f44-40ad-bda9-b09834ab1d53
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the prior-free representation forecasting model as described in Algorithm 4 using the learned encoder $h$ and without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using FLA...

### R810: Code has been written to apply the frequency-threshold based...
- **Rubric ID**: 7d71d787-eeed-446f-9bbf-7d968d460dbf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to apply the frequency-threshold based forecasting function $g$ to each sample $(x_i, y_i) \in D_R^{test}$ and $(x_j, y_j) \in \hat{D}_{PT}$ to produce a prediction $\hat{z}_{ij}^{test}$.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the frequency-threshold based ...

### R811: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 0d5cda97-83aa-4998-acb6-60b822068604
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the trainable logit based fore...

### R812: Code has been written to compute the bias term $b_j$ for all...
- **Rubric ID**: f8bbf8fd-b52a-4a96-98fa-b4c5dab38627
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the bias term $b_j$ for all $(x_j, y_j) \in D_R^{train}$ as described in Section 3.3 -- Forecasting with Frequency Priors.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the representation based forec...

### R813: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 0068d95f-c9a8-4598-9a54-35e2cdef7b4b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the representation based forec...

### R814: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 4d85d494-8bd5-4297-9510-99bf1a59ecf2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the representation forecasting model as described in Algorithm 4 and the learned encoder $h$.
- **Parent context**: Code has been implemented for reproducing the results of Figure 3 for the representation based forec...

### R815: Code has been written to compute the bias term $b_j$ for all...
- **Rubric ID**: 1aaf8c40-d81d-484a-955d-3b240ae53726
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the bias term $b_j$ for all $(x_j, y_j) \in D_R^{train}$ as described in Section 3.3 -- Forecasting with Frequency Priors.
- **Parent context**: Table 2 has been replicated.

### R816: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 3654f3c3-2105-4b23-a279-c418a3abf4cf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R817: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 6ce414e3-63d1-41d7-9aa7-a217e54c7510
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R818: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{train} \tim...
- **Rubric ID**: 3928aec6-0de2-4c0e-8a23-5c30000187bf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{train} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been developed to evaluate the trainable logit based forecasting method using BART0_{Large}...

### R819: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 128b0a20-e3cd-47a4-b8ca-a6de58a501be
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R820: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{train} \tim...
- **Rubric ID**: 292ca92f-ab86-4598-a993-d0d5a29bc0f8
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{train} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}$ by implementing the representation forecasting model as described in Algorithm 4 using the learned encoder $h$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R821: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: ca18a282-48a9-4e55-8695-82f0c3d93832
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the representation forecasting model as described in Algorithm 4 and the learned encoder $h$.
- **Parent context**: Code has been developed to evaluate the representation based forecasting method using BART0_{Large},...

### R822: Code has been written to train the encoding function $h$ for...
- **Rubric ID**: 920f9a28-6c1f-4b67-ab40-8ccc7198dde2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train the encoding function $h$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F, though without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R823: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{train} \tim...
- **Rubric ID**: 7e224e2b-4a9d-41b8-9dcf-04b733da5bfe
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{train} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}$ by implementing the prior-free representation forecasting model as described in Algorithm 4 using the learned encoder $h$  and without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R824: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 21866885-0b73-4a9f-a8c7-b371d279cb59
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the prior-free representation forecasting model as described in Algorithm 4 using the learned encoder $h$  and without the bias term $b_j$.
- **Parent context**: Code has been developed to evaluate the prior-free representation based forecasting method using BAR...

### R825: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 87fa6cf6-a42f-4dc7-b46b-8d24b51ddf8a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU valid...

### R826: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 08463c84-a256-4055-bf1f-71f2f85b3a09
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{3B}, the MMLU validati...

### R827: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 9185c775-0814-42a7-9f00-25049e31e4e6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R828: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 5e30fcd4-c85c-4227-92ec-d873478858d3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{3B}, the MMLU validation s...

### R829: Code was developed to fine-tune the FLAN-T5_{Large} model on...
- **Rubric ID**: e805f290-425f-4c4e-aa6f-c58db2210c03
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the FLAN-T5_{Large} model on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten by $g$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R830: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: d9d3c6a5-ef86-48df-844c-07ebf158c4b3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R831: Code was developed to fine-tune the FLAN-T5_{Large} model us...
- **Rubric ID**: 8af3e98c-2105-4d29-a165-c3c7e7fbfe50
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten by $g$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R832: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: a4a7ce0c-16a6-43c9-b851-52d729f3e8b1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R833: Code was developed to fine-tune the FLAN-T5_{3B} model using...
- **Rubric ID**: 0acc6980-14b6-4e65-bdae-79fa78d2d910
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on a random mini-batch of 4 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten by $g$ every 5 training steps using distillation loss against the base FLAN-T5_{3B} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R834: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 3c08c00f-1e9b-45a4-8baa-4b0d4708434e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using BAR...

### R835: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 73e69ea4-d3fc-401a-96e4-6c15bed52e6d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using BAR...

### R836: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 8642af3f-7902-4c71-8a24-b8eede215040
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using BAR...

### R837: Code was developed to fine-tune the BART0_{Large} model on a...
- **Rubric ID**: 45813cc4-8b3b-4266-85c6-7f649df2cfaf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the BART0_{Large} model on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 10 training steps using distillation loss against the base BART0_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using BAR...

### R838: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: f5875d41-3255-4e9b-a989-00bafd7a2190
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R839: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 103c09b5-f6fe-4af5-aed7-663dbedf7bf7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R840: Code was developed to fine-tune the FLAN-T5_{Large} model on...
- **Rubric ID**: 8791f382-fbaa-4434-a7d1-5ada0fc8364f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the FLAN-T5_{Large} model on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R841: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: a19f7695-2f61-4204-abce-af4323f441e6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R842: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: e91399ee-1b0a-456a-87a7-7458d9552826
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R843: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: d6fd8fc1-f1ef-4839-990d-d05fdaa05468
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R844: Code was developed to fine-tune the FLAN-T5_{Large} model us...
- **Rubric ID**: e2cfc257-0044-477d-96b8-0a3bddfa7eed
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R845: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: b6696601-bd94-49bb-8223-de08b0e7a450
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R846: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 3ec6b01d-de64-4dd3-85a7-da2cfd7e0d5d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R847: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 31a359d7-2d39-4d23-9559-f157563d3405
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R848: Code was developed to fine-tune the FLAN-T5_{3B} model using...
- **Rubric ID**: 95212175-919c-43a4-97a2-f7814c0f0c31
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on a random mini-batch of 4 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 5 training steps using distillation loss against the base FLAN-T5_{3B} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the replay with trainable logit based forecasting method using FLA...

### R849: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: cb9c0df4-45bb-4d96-b41e-32f144ad15c0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using BART...

### R850: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 1f359b2d-cac0-4dfa-b6fc-78bcea8ce49f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the representation forecasting model as described in Algorithm 4 and the learned encoder $h$.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using BART...

### R851: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: d212316a-b3f5-4f15-94e7-ef1f795f8d02
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R852: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 43793f81-e241-4e6e-887c-3db97fc3c363
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the representation forecasting model as described in Algorithm 4 and the learned encoder $h$.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R853: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: aa84a313-2cad-41f4-bf4b-bbe1c28a42a7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R854: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 888906cc-d7d8-48e6-bf77-92a0fe30a85d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ by implementing the representation forecasting model as described in Algorithm 4 using the learned encoder $h$.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R855: Code was developed to fine-tune the FLAN-T5_{Large} model us...
- **Rubric ID**: a2a74879-2e5e-4283-84ad-df69eeb915fa
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R856: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 7224e221-e8a5-4135-84e5-e2bc301ca6c0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R857: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: aafa35eb-f2a4-4bb9-ad4b-c485cf35f646
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R858: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: c50b126b-3ca1-44fd-a213-01577167a12c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ by implementing the representation forecasting model as described in Algorithm 4 using the learned encoder $h$.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R859: Code was developed to fine-tune the FLAN-T5_{3B} model using...
- **Rubric ID**: 0108bf24-5a37-49f7-833d-abd12e838fb9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on a random mini-batch of 4 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 5 training steps using distillation loss against the base FLAN-T5_{3B} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R860: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: bcd723ba-0a71-41dd-8ede-0d078bf8e51b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the replay with representation based forecasting method using FLAN...

### R861: Code was developed to fine-tune the BART0_{Large} model on a...
- **Rubric ID**: 638fa6a0-cc12-4953-a263-ef538e4b7718
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the BART0_{Large} model on a mini-batch of 8 examples from $\hat{D}_{PT}$ which were forgotten according to $z_{ij}^{test}$ every 10 training steps using distillation loss against the base BART0_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using BART0_{Large}, the...

### R862: Code was developed to fine-tune the FLAN-T5_{Large} model on...
- **Rubric ID**: 309e0fe1-105f-458b-bf00-dd05e73ca149
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code was developed to fine-tune the FLAN-T5_{Large} model on a mini-batch of 8 examples from $\hat{D}_{PT}$ which were forgotten according to $z_{ij}^{test}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R863: Code has been developed to fine-tune the FLAN-T5_{Large} mod...
- **Rubric ID**: d44310ea-2bcd-43bd-9ffe-909ec523d570
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, one at a time, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters" (N.B. the lower learning rates used for sequential error fixing).
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R864: Code was written to fine-tune the FLAN-T5_{Large} model usin...
- **Rubric ID**: af4f5336-6e60-47b9-a413-8d97b17e0eca
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code was written to fine-tune the FLAN-T5_{Large} model using the LoRA adaptation to model parameters on a mini-batch of 8 examples from $\hat{D}_{PT}$ which were forgotten according to $z_{ij}^{test}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R865: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 1dafd2cd-2e27-4d05-a1fd-cbdd85224bea
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{Large}, t...

### R866: Code was written to fine-tune the FLAN-T5_{3B} model using t...
- **Rubric ID**: 98f1f2e0-c1f5-44b2-a53a-403334cf7bd7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code was written to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on a mini-batch of 4 examples from $\hat{D}_{PT}$ which were forgotten according to $z_{ij}^{test}$ every 5 training steps using distillation loss against the base FLAN-T5_{3B} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

### R867: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 4ecdde4c-9c30-4cfb-8e39-817dde6d9ec1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

### R868: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: bb9c72be-a4ef-484e-ae77-f7231d6ef0f9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been developed to evaluate the vanilla fine-tune method using FLAN-T5_{Large}, the MMLU val...

### R869: Code has been developed to fine-tune the FLAN-T5_{3B} model...
- **Rubric ID**: 4457d984-efe2-4674-9c10-2b33ea4294fe
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to fine-tune the FLAN-T5_{3B} model using the LoRA adaptation to model parameters on each $(x_i, y_i) \in D_R^{test}$, thereby creating $|D_R^{test}|$-many separate models, as described in Section 5.2, and using the hyperparameters outlined in "Section 4.1 -- Hyperparameters".
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{3B}, the MMLU validati...

### R870: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: b8cadfae-2523-47c6-9204-340c0e667e74
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the vanilla fine-tune method using FLAN-T5_{3B}, the MMLU validati...

### R871: For each copy of BART0_{Large} fine-tuned on $(x_i, y_i)$, c...
- **Rubric ID**: 3b047b2c-080f-464b-b333-db89d641b2aa
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of BART0_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it on a random mini-batch of 8 examples from $D_{PT}$ every 10 training steps using distillation loss against the base BART0_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the random replay method using BART0_{Large}, the P3 test set an...

### R872: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$,...
- **Rubric ID**: b7f9b534-55da-45f9-b32f-8098d8160e39
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it on a random mini-batch of 8 examples from $D_{PT}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validat...

### R873: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$,...
- **Rubric ID**: bfd0c2dd-33e6-4175-aaf9-caeef894f261
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it using the LoRA adaptation to the model parameters on a random mini-batch of 8 examples from $D_{PT}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R874: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: e2faa9ab-e7b6-4ea3-b7c4-bbda44402f4b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the random replay method using FLAN-T5_{Large}, the MMLU validatio...

### R875: For each copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$, co...
- **Rubric ID**: 1a58a441-a746-48aa-a2f6-a937b3a53932
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it using the LoRA adaptation to the model parameters on a random mini-batch of 4 examples from $\hat{D}_{PT}$ every 5 training steps using distillation loss against the base FLAN-T5_{3B} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the random replay method using FLAN-T5_{3B}, the MMLU validation...

### R876: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: e88bab54-bf02-499b-ab4c-b3071c114db3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been developed to evaluate the random replay method using FLAN-T5_{3B}, the MMLU validation...

### R877: For each copy of BART0_{Large} fine-tuned on $(x_i, y_i)$, c...
- **Rubric ID**: 06f8bd12-c5d9-453b-9d3c-95a66653f37f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of BART0_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten by $g$ every 10 training steps using distillation loss against the base BART0_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R878: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$,...
- **Rubric ID**: 7a4fe5d6-d85f-423d-8de4-c195befb2095
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten by $g$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R879: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$,...
- **Rubric ID**: 68418baa-05c7-4bb8-a273-210079a562ad
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it using the LoRA adaptation to model parameters on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten by $g$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R880: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 5151a3d3-f857-423c-ab70-0386ee5345e4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the replay with frequency-threshold based forecasting method using...

### R881: For each copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$, co...
- **Rubric ID**: ea55a15d-3b87-409d-a831-9417525611bc
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it using the LoRA adaptation to model parameters on a random mini-batch of 4 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten by $g$ every 5 training steps using distillation loss against the base FLAN-T5_{3B} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R882: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 032d9061-bd50-4e56-844a-e763c79e565b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been developed to evaluate the replay with frequency-threshold based forecasting method usi...

### R883: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: d0378f6e-5175-4a1b-98d9-2fafc17f0b5f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using B...

### R884: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: b1a5b562-6c47-49f3-8b56-55cc3627a3d2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using B...

### R885: For each copy of BART0_{Large} fine-tuned on $(x_i, y_i)$, c...
- **Rubric ID**: 251ef2b5-1ccf-4e94-bb13-45f59c6ee87e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of BART0_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 10 training steps using distillation loss against the base BART0_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using B...

### R886: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 80646b53-cbe2-4e16-8859-96627d74dbea
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R887: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 958eb6ec-5a7d-45fe-903e-2c84df321c7e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R888: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$,...
- **Rubric ID**: a79c36fb-269b-43bb-8ae4-e84fd970fae8
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $z_{ij}^{test}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R889: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: f5a27e4c-8915-4f98-8fc2-12f6d58ddcee
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R890: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$,...
- **Rubric ID**: c0488026-5eb2-484d-8273-72f5dcabe1a6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it using the LoRA adaptation to model parameters on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R891: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 5ddc06b1-22a5-4f27-a2f1-3fe010d77f36
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R892: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 6a961e01-2c70-4b71-a951-4dd659fa2c94
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 1 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R893: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: a22f34cd-f0fb-41bb-87d7-d0c7f57de0c5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the trainable logit-based forecasting model as described in Algorithm 2.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R894: For each copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$, co...
- **Rubric ID**: fd9fd4d1-af3a-40df-9fe9-13a53c90ce8d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it using the LoRA adaptation to model parameters on a random mini-batch of 4 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 5 training steps using distillation loss against the base FLAN-T5_{3B} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R895: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 8451499e-1829-453a-b0cc-912aed47df3e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been developed to evaluate the replay with trainable logit based forecasting method using F...

### R896: Code has been written to compute the bias term $b_j$ for all...
- **Rubric ID**: 231e403c-3c15-49f0-be75-c314b4697ddb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the bias term $b_j$ for all $(x_j, y_j) \in D_R^{train}$ as described in Section 3.3 -- Forecasting with Frequency Priors.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using BA...

### R897: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 753fb2fc-ba39-4ac3-8434-e644e2e376ac
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for BART0_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using BA...

### R898: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: ad0eccd2-8fb9-4208-aa4e-ed288ca6270b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ by implementing the representation forecasting model as described in Algorithm 4 using the learned encoder $h$.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using BA...

### R899: For each copy of BART0_{Large} fine-tuned on $(x_i, y_i)$, c...
- **Rubric ID**: 3b3ae663-cf19-463e-8b56-671232b0548d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of BART0_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 10 training steps using distillation loss against the base BART0_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using BA...

### R900: Code has been developed to compute the ground truth forgetti...
- **Rubric ID**: 99439204-39cd-4ffb-8491-aa4c82889720
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to compute the ground truth forgetting indicator $z_{ij}$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ and $D_R^{train}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R901: Code has been written to compute the bias term $b_j$ for all...
- **Rubric ID**: f5215eb4-3ab8-4e30-9901-47cd95a72670
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the bias term $b_j$ for all $(x_j, y_j) \in D_R^{train}$ as described in Section 3.3 -- Forecasting with Frequency Priors.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R902: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: c82bf90a-4fcd-429f-9313-bcbcee3f206e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R903: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$,...
- **Rubric ID**: 0ba72d1f-efcb-4d67-919e-8da8953809fb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R904: Code has been written to compute the bias term $b_j$ for all...
- **Rubric ID**: 95a74a85-27d9-4533-9415-a9d36de0a6fb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the bias term $b_j$ for all $(x_j, y_j) \in D_R^{train}$ as described in Section 3.3 -- Forecasting with Frequency Priors.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R905: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: 1694196d-34d2-4020-8e07-95f3f540b884
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{Large} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R906: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 0c1274ff-dffd-4162-8d16-c5770d68fcb9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the representation forecasting model as described in Algorithm 4 and the learned encoder $h$.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R907: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$,...
- **Rubric ID**: 719b4afc-f184-4416-b614-44c8dde91e34
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it using the LoRA adaptation to model parameters on a random mini-batch of 8 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R908: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 30278e59-5b00-4925-8919-2490d6b2c72c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R909: Code has been written to compute the bias term $b_j$ for all...
- **Rubric ID**: 8529db28-c96a-4674-96e1-a67f25d941fc
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the bias term $b_j$ for all $(x_j, y_j) \in D_R^{train}$ as described in Section 3.3 -- Forecasting with Frequency Priors.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R910: Code has been developed to train the encoding function $h$ f...
- **Rubric ID**: ea9883dc-c2ab-409c-8fe9-96a66111e498
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been developed to train the encoding function $h$ for FLAN-T5_{3B} using $\hat{D}_{PT}$ as input $D_{PT}$ as described in Algorithm 3 in Appendix F.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R911: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \time...
- **Rubric ID**: 259c0fea-afc0-42d3-9f86-245e9468d702
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each pair $((x_i, y_i), (x_j, y_j)) \in D_R^{test} \times \hat{D}_{PT}$, code has been written to compute the predicted forgetting binary indicator $\hat{z}_{ij}^{test}$ using the representation forecasting model as described in Algorithm 4 and the learned encoder $h$.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R912: For each copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$, co...
- **Rubric ID**: 1469535a-3dd9-4051-897a-0e549ed32bf4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it using the LoRA adaptation to model parameters on a random mini-batch of 4 examples from $\hat{D}_{PT}$ which were forecasted to be forgotten according to $\hat{z}_{ij}^{test}$ every 5 training steps using distillation loss against the base FLAN-T5_{3B} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R913: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 4b99949c-1fb8-4264-be18-b1c2f08c280c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been developed to evaluate the replay with representation based forecasting method using FL...

### R914: For each copy of BART0_{Large} fine-tuned on $(x_i, y_i)$, c...
- **Rubric ID**: 984cec31-9582-42b0-9ef2-a1b8fb02f9bb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of BART0_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it on a mini-batch of 8 examples from $\hat{D}_{PT}$ which were forgotten according to $z_{ij}^{test}$ every 10 training steps using distillation loss against the base BART0_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using BART0_{Large}, t...

### R915: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$,...
- **Rubric ID**: 1148b7ad-8210-4867-842b-a5f23e79197e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it on a mini-batch of 8 examples from $\hat{D}_{PT}$ which were forgotten according to $z_{ij}^{test}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using FLAN-T5_{Large},...

### R916: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$,...
- **Rubric ID**: 185f67fb-786f-43d3-942c-49cb05d7088a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{Large} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it using the LoRA adaptation to model parameters on a mini-batch of 8 examples from $\hat{D}_{PT}$ which were forgotten according to $z_{ij}^{test}$ every 10 training steps using distillation loss against the base FLAN-T5_{Large} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using FLAN-T5_{Large},...

### R917: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: 34e2200a-bc05-48b6-a603-aede8afd0b05
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been developed to evaluate the ground truth forgetting replay method using FLAN-T5_{Large},...

### R918: For each copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$, co...
- **Rubric ID**: 1aa2cc93-b142-4c9b-a03b-68bbc767d240
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each copy of FLAN-T5_{3B} fine-tuned on $(x_i, y_i)$, code was also written to fine-tune it using the LoRA adaptation to model parameters on a mini-batch of 4 examples from $\hat{D}_{PT}$ which were forgotten according to $z_{ij}^{test}$ every 5 training steps using distillation loss against the base FLAN-T5_{3B} model, thereby 'replaying' examples, as described in Section 4.2 -- Model Refinement.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

### R919: LoRA was applied to the query and value (but not key) matric...
- **Rubric ID**: a3e144cd-ea3a-41e0-978c-7eb687e71103
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: LoRA was applied to the query and value (but not key) matrices in all self-attention layers.
- **Parent context**: Code has been written to evaluate the ground truth forgetting replay method using FLAN-T5_{3B}, the ...

## Logging, Analysis & Presentation

### R920: The recorded F1-scores show that the representation based me...
- **Rubric ID**: 347247f5-4fd3-4f10-9de6-90389da50239
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The recorded F1-scores show that the representation based method has the highest F1-score for all models, dataset and fine-tuning setups, except for the head of FLAN-T5_{Large} fine-tuned on MMLU, where the fixed logit based forecasting method performs best.
- **Parent context**: The recorded F1-scores match those presented in Table 1.

### R921: The recorded running average F1-score decreases over time fo...
- **Rubric ID**: 3f8ed9c9-84f3-4fba-ac6b-27b59763e60f
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The recorded running average F1-score decreases over time for the frequency-threshold, logit-based and representation-based forecasting methods.
- **Parent context**: The recorded F1-score, recall and precision metrics match those presented in Figure 3.
