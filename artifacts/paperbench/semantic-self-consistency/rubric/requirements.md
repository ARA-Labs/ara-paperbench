# Rubric Requirements — semantic-self-consistency
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 77

## Dataset and Model Acquisition

### R01: The test split of the AQuA-RAT dataset (254 samples) is avai...
- **Rubric ID**: 43f23e0e-2c5b-4a2b-80ab-6cc9c62723f1
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The test split of the AQuA-RAT dataset (254 samples) is available for use.
- **Parent context**: The datasets AQuA-RAT, StrategyQA, and SVAMP have been prepared for evaluation.

### R02: The test split of the StrategyQA dataset (687 samples) is av...
- **Rubric ID**: 8006761a-19e1-4990-92fa-778b6ee89266
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The test split of the StrategyQA dataset (687 samples) is available for use.
- **Parent context**: The datasets AQuA-RAT, StrategyQA, and SVAMP have been prepared for evaluation.

### R03: The full SVAMP dataset (1000 samples including both the trai...
- **Rubric ID**: 067da205-f599-4a40-92fe-4cfc3f635c41
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The full SVAMP dataset (1000 samples including both the train and test split) is available for use.
- **Parent context**: The datasets AQuA-RAT, StrategyQA, and SVAMP have been prepared for evaluation.

## Experimental Setup

### R04: Inference can be performed on gpt-3.5-turbo (any version)
- **Rubric ID**: 5096c429-1bd2-45ef-acf9-edadd7c9286b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Inference can be performed on gpt-3.5-turbo (any version)
- **Parent context**: Obtained access to each generator model to perform inference

### R05: All models use top-p=1. Note, the default value for top-p th...
- **Rubric ID**: 7e05fd91-a2fa-47ce-918f-9626d9b23f75
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All models use top-p=1. Note, the default value for top-p through the OpenAI API is 1
- **Parent context**: All Generators listed in Section 3.1 have been set up with the correct hyperparameters listed

### R06: All models generate up to 250 max new tokens on SVAMP, 400 o...
- **Rubric ID**: a560cc7a-6ad0-453b-8283-239b981d8754
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All models generate up to 250 max new tokens on SVAMP, 400 on AQuA-RAT, and 450 on StrategyQA
- **Parent context**: All Generators listed in Section 3.1 have been set up with the correct hyperparameters listed

### R07: All models use the 4-shot prompt provided in Table 21 of "Ch...
- **Rubric ID**: 77d8f917-a53e-4374-8eaa-c24fa70186e2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All models use the 4-shot prompt provided in Table 21 of "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" when evaluated on AQuA-RAT
- **Parent context**: All models use the correct k-shot prompt, depending on the dataset they are being evaluated on

### R08: All models use the 6-shot prompt provided in Table 25 of "Ch...
- **Rubric ID**: f4ea36de-ac1c-498b-a8db-7616907780cb
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All models use the 6-shot prompt provided in Table 25 of "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" when evaluated on StrategyQA
- **Parent context**: All models use the correct k-shot prompt, depending on the dataset they are being evaluated on

### R09: All models use the 8-shot math prompt provided in Table 20 o...
- **Rubric ID**: 9e88e0f1-e7ee-443c-b64a-e6d835e08f1d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All models use the 8-shot math prompt provided in Table 20 of "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" when evaluated on SVAMP
- **Parent context**: All models use the correct k-shot prompt, depending on the dataset they are being evaluated on

### R10: The number of neighbours used is set to 5 (the "n_neighbors"...
- **Rubric ID**: 50fe90ba-39a2-4b00-8e52-edb99448ca7b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The number of neighbours used is set to 5 (the "n_neighbors" argument is set to 6 if using the sklearn implementation of KNeighborsClassifier to return the 5 nearest neighbours, note 5 is the default value of this argument)
- **Parent context**: The K-nearest neighbour outlier removal method has been set up correctly

### R11: The number of base estimators in the ensemble is set to 200...
- **Rubric ID**: 53060482-d130-4c4d-ac1c-93e755c7db43
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The number of base estimators in the ensemble is set to 200 (the "n_estimators" arg is set to 200 if using the sklearn implementation of IsolationForest")
- **Parent context**: The isolation forest outlier removal method has been set up correctly

### R12: The threshold is determined as in the original paper (the "c...
- **Rubric ID**: c5814593-5393-4a6d-80e7-5b85eac9e593
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The threshold is determined as in the original paper (the "contamination" arg is set to "auto" if using the sklearn implementation of IsolationForest")
- **Parent context**: The isolation forest outlier removal method has been set up correctly

### R13: The number of samples to draw from the training data to trai...
- **Rubric ID**: 4d197469-b5e8-4bff-bae7-211a4f83f140
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The number of samples to draw from the training data to train each base estimator is set to min(256, n_samples) (the "max_samples" arg is set to "auto" if using the sklearn implementation of IsolationForest")
- **Parent context**: The isolation forest outlier removal method has been set up correctly

### R14: A linear kernel is used (the "kernel" arg is set to"linear"...
- **Rubric ID**: 39c1c9c5-c0e1-4d3c-a5ce-5cf7e951b3e7
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: A linear kernel is used (the "kernel" arg is set to"linear" if using the sklearn implementation of OneClassSVM")
- **Parent context**: The support vector machine outlier removal method has been set up correctly

### R15: The upper bound on the fraction of training errors and the l...
- **Rubric ID**: 32076d58-8586-4aac-9eb5-8a7570cc45cf
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The upper bound on the fraction of training errors and the lower bound of the fraction of support vectors parameter is set to 0.01 (the "nu" arg is set to 0.01 if using the sklearn implementation of OneClassSVM)
- **Parent context**: The support vector machine outlier removal method has been set up correctly

### R16: Given a question, the model generates k=10 responses by samp...
- **Rubric ID**: bd9fa816-1437-4f94-825b-d77b0f11af0c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Given a question, the model generates k=10 responses by sampling with temperature=0.8
- **Parent context**: Model answer generation using the Semantic Consensus Weighting method has been implemented as in Sec...

### R17: All evaluations on the AQuA-RAT benchmark use SciBERT as the...
- **Rubric ID**: ad259ecf-0a1e-40a3-8d74-7b46f400301e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All evaluations on the AQuA-RAT benchmark use SciBERT as the featurizer to produce embeddings.
- **Parent context**: Evaluation code for Section 5.1 and Section 5.2 is correctly implemented.

## Method Implementation

### R18: Inference can be performed on gpt-4o-mini (any version)
- **Rubric ID**: 81246c81-3081-4734-8bdd-b6de2992105a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Inference can be performed on gpt-4o-mini (any version)
- **Parent context**: Obtained access to each generator model to perform inference

### R19: The method uses the ball tree algorithm (the "algorithm" arg...
- **Rubric ID**: 2d8d7041-be93-45ae-a6ac-80fa53a49199
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The method uses the ball tree algorithm (the "algorithm" argument is set to "ball_tree" if using the sklearn implementation of KNeighborsClassifier)
- **Parent context**: The K-nearest neighbour outlier removal method has been set up correctly

### R20: Euclidean distance is used (the "metric" argument is set to...
- **Rubric ID**: 796cdb25-0885-4219-a0f9-bdedb3e37a0d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Euclidean distance is used (the "metric" argument is set to "minkowski" if using the sklearn implementation of KNeighborsClassifier, note "minkowski" is the default value of this argument)
- **Parent context**: The K-nearest neighbour outlier removal method has been set up correctly

### R21: RoBERTa base (125 million parameters version) can be used to...
- **Rubric ID**: 8519dd43-eaf9-42dd-b96e-cda00b737479
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: RoBERTa base (125 million parameters version) can be used to generate an embedding vector for an input string
- **Parent context**: All Featurizers listed in Section 3.2 are set up with correct hyperparameters to generate embeddings...

### R22: SciBERT (110 million parameters version) can be used to gene...
- **Rubric ID**: 0dffe1c8-da0c-4829-9bb6-033512baada3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: SciBERT (110 million parameters version) can be used to generate an embedding vector for an input string
- **Parent context**: All Featurizers listed in Section 3.2 are set up with correct hyperparameters to generate embeddings...

### R23: Given a question, the model generates a single response usin...
- **Rubric ID**: 13a6fa19-3d02-4331-b64e-06930fd29626
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Given a question, the model generates a single response using greedy decoding
- **Parent context**: Model answer generation using the top prob method is implemented.

### R24: The parsing extraction approach is applied to extract the mo...
- **Rubric ID**: 463c7875-01e8-4e72-8e07-493ee968b0b3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The parsing extraction approach is applied to extract the models answer from the response
- **Parent context**: Model answer generation using the top prob method is implemented.

### R25: Given a question, the model generates k=10 responses by samp...
- **Rubric ID**: 95520bb4-2c5d-4469-975a-569e1ab76cd4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Given a question, the model generates k=10 responses by sampling with temperature=0.8
- **Parent context**: Model answer generation using the self-consistency baseline method is implemented.

### R26: The parsing extraction approach is applied to extract the an...
- **Rubric ID**: 9daf76c9-d2d0-4744-ba70-bbcf82550191
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The parsing extraction approach is applied to extract the answer from each of the k responses
- **Parent context**: Model answer generation using the self-consistency baseline method is implemented.

### R27: The final answer is selected as the modal answer from the k...
- **Rubric ID**: c08b029c-fa6d-475b-b201-6b43dcd14c5e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The final answer is selected as the modal answer from the k answers extracted from the k responses
- **Parent context**: Model answer generation using the self-consistency baseline method is implemented.

### R28: Given a question, the model generates k=10 responses by samp...
- **Rubric ID**: b4ec7fec-fe79-4cfc-a15e-c2e43db21c2b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Given a question, the model generates k=10 responses by sampling with temperature=0.8
- **Parent context**: Model answer generation using the Centroid Proximity Weighting method has been implemented as in Sec...

### R29: The parsing extraction approach is applied to extract the an...
- **Rubric ID**: abef3d1f-ac05-4b98-a4c4-cdf711863714
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The parsing extraction approach is applied to extract the answer from each of the k responses
- **Parent context**: Model answer generation using the Centroid Proximity Weighting method has been implemented as in Sec...

### R30: An embedding is created for each of the k responses by passi...
- **Rubric ID**: a5c85099-0e2e-46c1-bd19-5bedb2d7886a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: An embedding is created for each of the k responses by passing it through the associated featurizer and getting the embedding at the first ("[CLS]") token
- **Parent context**: Model answer generation using the Centroid Proximity Weighting method has been implemented as in Sec...

### R31: The centroid for the k embeddings is computed using euclidea...
- **Rubric ID**: c2fd8c8a-e7c0-4fbd-8bf5-ef4c6108002a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The centroid for the k embeddings is computed using euclidean distance
- **Parent context**: Model answer generation using the Centroid Proximity Weighting method has been implemented as in Sec...

### R32: Each of the k embeddings has an associated weight inversely...
- **Rubric ID**: 77e2711a-6278-4798-978f-d79c3a337d9f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Each of the k embeddings has an associated weight inversely proportional to their normalized distance to the centroid of all the embeddings. The weight for embedding i is computed as one divided by the normalized distance from embedding i to the centroid
- **Parent context**: Model answer generation using the Centroid Proximity Weighting method has been implemented as in Sec...

### R33: For each of the groups of embeddings with the same answer, t...
- **Rubric ID**: 89b080c5-7ddb-4115-ade2-5d5ce9ebed5c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each of the groups of embeddings with the same answer, the weights are summed together, and the final answer is selected as the answer that has the highest associated weight
- **Parent context**: Model answer generation using the Centroid Proximity Weighting method has been implemented as in Sec...

### R34: The parsing extraction approach is applied to extract the an...
- **Rubric ID**: 82b1a191-e41c-457b-af57-e036b6be7129
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The parsing extraction approach is applied to extract the answer from each of the k responses
- **Parent context**: Model answer generation using the Semantic Consensus Weighting method has been implemented as in Sec...

### R35: An embedding is creating for each of the k responses by pass...
- **Rubric ID**: c8acfeae-4a0f-4915-a8f0-e254fd9d664b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: An embedding is creating for each of the k responses by passing it through the associated featurizer and getting the embedding at the first ("[CLS]") token
- **Parent context**: Model answer generation using the Semantic Consensus Weighting method has been implemented as in Sec...

### R36: For each of the groups of embeddings with the same answer, t...
- **Rubric ID**: e84e0360-1818-41c0-884a-8714732a11fd
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each of the groups of embeddings with the same answer, the scores are summed together, and the final answer is selected as the answer that has the highest associated score
- **Parent context**: Model answer generation using the Semantic Consensus Weighting method has been implemented as in Sec...

### R37: Model answer generation with the k-Nearest Neighbours outlie...
- **Rubric ID**: c066870b-543b-4935-a936-3560101fbb13
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Model answer generation with the k-Nearest Neighbours outlier removal method has been implemented. Given k generated samples for a question, the k-Nearest Neighbours method is applied to filter out some samples, then standard self-consistency is applied to the remaining samples to compute the final answer
- **Parent context**: The 3 semantic outlier removal methods in Section 4.2 (KNN, Isolation Forest, SVM) have been impleme...

### R38: Model answer generation with the Isolation Forest outlier re...
- **Rubric ID**: 0eb8c4c9-c562-4c74-8153-6632e91eccc6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Model answer generation with the Isolation Forest outlier removal method has been implemented. Given k generated samples for a question, the Isolation Forest method is applied to filter out some samples, then standard self-consistency is applied to the remaining samples to compute the final answer
- **Parent context**: The 3 semantic outlier removal methods in Section 4.2 (KNN, Isolation Forest, SVM) have been impleme...

### R39: Model answer generation with the SVM outlier removal method...
- **Rubric ID**: eb67f3e3-fc60-4ba0-97cb-a1e97cdab8e5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Model answer generation with the SVM outlier removal method has been implemented. Given k generated samples for a question, the SVM method is applied to filter out some samples, then standard self-consistency is applied to the remaining samples to compute the final answer
- **Parent context**: The 3 semantic outlier removal methods in Section 4.2 (KNN, Isolation Forest, SVM) have been impleme...

## Data Processing & Preparation

### R40: All input points are sorted by average distance to their nei...
- **Rubric ID**: b63359fc-8d24-4473-bed3-d54fe1586b53
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: All input points are sorted by average distance to their neighbours, and the 10% of inputs to the KNN method with the largest average distances are filtered out
- **Parent context**: The K-nearest neighbour outlier removal method has been set up correctly

### R41: For SVAMP, AQuA_RAT and StrategyQA, given a response, the fu...
- **Rubric ID**: 42296ab8-386b-4645-9fbf-4cd635f4fd81
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: For SVAMP, AQuA_RAT and StrategyQA, given a response, the full string answer after the model generates "The answer is" is parsed as the answer, after removing for whitespace, fullstops, and parentheses
- **Parent context**: The parsing extraction approach has been implemented to extract answers from a generated response (p...

## Evaluation, Metrics & Benchmarking

### R42: When generating answers using the top prob method, only gene...
- **Rubric ID**: be2d3c6c-efbd-477e-97fe-a616f6fc3bf1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When generating answers using the top prob method, only generations where an answer could be extracted should be considered when computing the various metrics in each of the experiments.
- **Parent context**: The parsing extraction approach has been implemented to extract answers from a generated response (p...

### R43: When generating answers for AQuA-RAT, only generations where...
- **Rubric ID**: a09d85b6-e400-42bf-9958-def3b4311d9d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When generating answers for AQuA-RAT, only generations where an answer could be extracted should be considered when computing the various metrics in each of the experiments.
- **Parent context**: The parsing extraction approach has been implemented to extract answers from a generated response (p...

### R44: The normalized distance from each of the k embeddings to the...
- **Rubric ID**: 39f83549-039d-44b4-85d5-1d66e261baa9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The normalized distance from each of the k embeddings to the centroid of the k embeddings is computed
- **Parent context**: Model answer generation using the Centroid Proximity Weighting method has been implemented as in Sec...

### R45: For each embedding, the cosine similarity between it and eve...
- **Rubric ID**: db4e4076-436e-4a5a-b441-8d7d876b7f1a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each embedding, the cosine similarity between it and every other embedding is summed to produce a score for such embedding
- **Parent context**: Model answer generation using the Semantic Consensus Weighting method has been implemented as in Sec...

### R46: Code for model answer generation and grading is implemented...
- **Rubric ID**: ba28ab4e-4b8b-4359-bbac-9bb8753e3d84
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code for model answer generation and grading is implemented correctly for the AQuA-RAT benchmark.
- **Parent context**: Evaluation code for Section 5.1 and Section 5.2 is correctly implemented.

### R47: Code for model answer generation and grading is implemented...
- **Rubric ID**: 0b270d60-8ac8-4102-933d-cc9eddedd22d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code for model answer generation and grading is implemented correctly for the SVAMP benchmark.
- **Parent context**: Evaluation code for Section 5.1 and Section 5.2 is correctly implemented.

### R48: All evaluations on the SVAMP benchmark use SciBERT as the fe...
- **Rubric ID**: 8028e26f-9cc7-482f-b648-02be6d130e53
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All evaluations on the SVAMP benchmark use SciBERT as the featurizer to produce embeddings.
- **Parent context**: Evaluation code for Section 5.1 and Section 5.2 is correctly implemented.

### R49: Code for model answer generation and grading is implemented...
- **Rubric ID**: 489ab4d9-1501-4f01-ad35-75f35f1f174b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code for model answer generation and grading is implemented correctly for the StrategyQA benchmark.
- **Parent context**: Evaluation code for Section 5.1 and Section 5.2 is correctly implemented.

### R50: All evaluations on the StrategyQA benchmark use RoBERTa as t...
- **Rubric ID**: 1c671c6e-e97e-4897-82fd-ec21dc80e744
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All evaluations on the StrategyQA benchmark use RoBERTa as the featurizer to produce embeddings.
- **Parent context**: Evaluation code for Section 5.1 and Section 5.2 is correctly implemented.

### R51: All models have been evaluated on the AQuA-RAT benchmark usi...
- **Rubric ID**: 9d8bb6a7-080b-4e15-a710-dec1da026131
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the AQuA-RAT benchmark using top prob sampling.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R52: All models have been evaluated on the AQuA-RAT benchmark usi...
- **Rubric ID**: 5e1af65d-a62a-4779-bb5f-196983a75c7e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the AQuA-RAT benchmark using the self-consistency baseline.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R53: All models have been evaluated on the AQuA-RAT benchmark usi...
- **Rubric ID**: 02b21e96-830c-4b3b-b399-018f569f4861
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the AQuA-RAT benchmark using the CPW method on SciBERT embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R54: All models have been evaluated on the AQuA-RAT benchmark usi...
- **Rubric ID**: 0535160a-b056-4dfa-a29f-511f1abf6ff8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the AQuA-RAT benchmark using the SCW method on SciBERT embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R55: All models have been evaluated on the SVAMP benchmark using...
- **Rubric ID**: 838cb78c-aade-4c63-8790-35f316e21765
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the SVAMP benchmark using top prob sampling.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R56: All models have been evaluated on the SVAMP benchmark using...
- **Rubric ID**: 860a913a-0f9c-4ea7-927d-bebb039b7cb3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the SVAMP benchmark using the self-consistency baseline.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R57: All models have been evaluated on the SVAMP benchmark using...
- **Rubric ID**: 20e068b7-9f3c-4df2-8c37-91e7640d33b4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the SVAMP benchmark using the CPW method on SciBERT embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R58: All models have been evaluated on the SVAMP benchmark using...
- **Rubric ID**: e17cff0a-859f-4718-a752-8b0b73d37e47
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the SVAMP benchmark using the SCW method on SciBERT embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R59: All models have been evaluated on the StrategyQA benchmark u...
- **Rubric ID**: e8174d6c-a1f7-4266-8e47-8369fde0461f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the StrategyQA benchmark using top prob sampling.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R60: All models have been evaluated on the StrategyQA benchmark u...
- **Rubric ID**: fbdcd693-b8d5-493f-8475-d05c390e27d1
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the StrategyQA benchmark using the self-consistency baseline.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R61: All models have been evaluated on the StrategyQA benchmark u...
- **Rubric ID**: 6b95e4e0-0339-4e5c-948a-698f6386f0f9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the StrategyQA benchmark using the CPW method on RoBERTa embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R62: All models have been evaluated on the StrategyQA benchmark u...
- **Rubric ID**: 970e42e4-8be9-4d3b-a167-f7704065bd35
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the StrategyQA benchmark using the SCW method on RoBERTa embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R63: All models have been evaluated on the AQuA-RAT benchmark usi...
- **Rubric ID**: 729f1e41-1435-4323-97d1-a1e6f2abac8d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the AQuA-RAT benchmark using the Isolation Forest outlier removal method on SciBERT embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R64: All models have been evaluated on the AQuA-RAT benchmark usi...
- **Rubric ID**: 866d7330-a9f7-4ee5-a2b2-f62ed843d522
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the AQuA-RAT benchmark using the KNN outlier removal method on SciBERT embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R65: All models have been evaluated on the AQuA-RAT benchmark usi...
- **Rubric ID**: 8ac54105-5705-4e70-9fda-51c8363bdb44
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the AQuA-RAT benchmark using the One-class SVM outlier removal method on SciBERT embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R66: All models have been evaluated on the SVAMP benchmark using...
- **Rubric ID**: 63aa239f-9288-462e-85f2-c4019768a6f7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the SVAMP benchmark using the Isolation Forest outlier removal method on SciBERT embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R67: All models have been evaluated on the SVAMP benchmark using...
- **Rubric ID**: f9d830a5-dd0a-4b66-90d7-66fd1035ff29
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the SVAMP benchmark using the KNN outlier removal method on SciBERT embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R68: All models have been evaluated on the SVAMP benchmark using...
- **Rubric ID**: c5380fee-79a6-4d19-b0af-a67f252d73c7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the SVAMP benchmark using the One-class SVM outlier removal method on SciBERT embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R69: All models have been evaluated on the StrategyQA benchmark u...
- **Rubric ID**: 77a472fc-c8c9-4316-93a0-ecaa32677a32
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the StrategyQA benchmark using the Isolation Forest outlier removal method on RoBERTa embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R70: All models have been evaluated on the StrategyQA benchmark u...
- **Rubric ID**: e4829498-53f5-434e-a683-47cbc0aced86
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the StrategyQA benchmark using the KNN outlier removal method on RoBERTa embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R71: All models have been evaluated on the StrategyQA benchmark u...
- **Rubric ID**: 879fdf86-cc40-404e-93a9-20d80574f790
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All models have been evaluated on the StrategyQA benchmark using the One-class SVM outlier removal method on RoBERTa embeddings.
- **Parent context**: All the experiments for Section 5.1 and Section 5.2 have been run.

### R72: The SC baseline outperforms the top prob sampling baseline i...
- **Rubric ID**: 10516a66-aec7-437c-9966-7dc0d7fcefc0
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The SC baseline outperforms the top prob sampling baseline in all cases.
- **Parent context**: The reproduced results for Section 5.1 match the conclusions of the paper.

### R73: Across models and datasets, the SCW method outperforms the S...
- **Rubric ID**: e3023d1b-c9d1-4234-8855-d7ee84bf5243
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Across models and datasets, the SCW method outperforms the SC baseline in almost all cases.
- **Parent context**: The reproduced results for Section 5.1 match the conclusions of the paper.

### R74: On average across models, CPW outperforms the SC baseline on...
- **Rubric ID**: c042db31-9804-4360-9ec8-037e70847fc0
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 3
- **Requirement**: On average across models, CPW outperforms the SC baseline on the AQuA-RAT and SVAMP, but has a negative effect on StrategyQA.
- **Parent context**: The reproduced results for Section 5.1 match the conclusions of the paper.

### R75: The One-class SVM outlier removal method outperforms the SC...
- **Rubric ID**: 5335dc2c-5cc8-4cfa-8bd5-e123af878f06
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The One-class SVM outlier removal method outperforms the SC baseline on StrategyQA most of the time across all models.
- **Parent context**: The reproduced results for Section 5.2 match the conclusions of the paper.

### R76: gpt-4o-mini generally achieves a very small performance gain...
- **Rubric ID**: 2322564b-cb87-40b7-931b-1afc876baf55
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: gpt-4o-mini generally achieves a very small performance gain over the SC baseline for all removal methods in all 3 dataset settings
- **Parent context**: The reproduced results for Section 5.2 match the conclusions of the paper.

### R77: GPT-3.5 generally has much higher performance relative to th...
- **Rubric ID**: d5734891-24a1-4df0-82cf-483d1397eb46
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: GPT-3.5 generally has much higher performance relative to the SC baseline for all removal methods in all 3 dataset settings
- **Parent context**: The reproduced results for Section 5.2 match the conclusions of the paper.
