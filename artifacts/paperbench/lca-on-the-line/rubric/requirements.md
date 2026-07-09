# Rubric Requirements — lca-on-the-line
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 819

## Method Implementation

### R01: Code has been written to find the lowest common ancestor of...
- **Rubric ID**: 4fe131d4-617e-4407-9aeb-fd4c9ee71939
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to find the lowest common ancestor of two nodes, $N_{L C A}\left(y^{\prime}, y\right)$.
- **Parent context**: The LCA distance has been implemented, as described in Section 2.

### R02: Code to compute the probability of each node in a given clas...
- **Rubric ID**: b78b143f-cd83-43ef-a578-9b36e31ef873
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code to compute the probability of each node in a given class hierarchy, $p(y)$, has been written. The probability of a node is computed by summing the probabilities of its descendants where leaf nodes are assigned uniform probabilities, as described in the paper "Hierarchical classification at multiple operating points".
- **Parent context**: Code has been written to compute the information content of a node.

### R03: Code to compute the information content of a node, $y$, has...
- **Rubric ID**: 54f426ad-c2c8-48d1-83c7-911b447095f7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code to compute the information content of a node, $y$, has been implemented via $-\log_2 p(y)$.
- **Parent context**: Code has been written to compute the information content of a node.

### R04: Code has been written to compute the depth of a node $x$ in...
- **Rubric ID**: 339d75bc-44dc-454b-8ba3-876955340d44
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the depth of a node $x$ in a tree $T$.
- **Parent context**: The LCA distance has been implemented, as described in Section 2.

### R05: Code has been written to compute the LCA distance between tw...
- **Rubric ID**: 00438d76-0175-42b3-848b-a2f799e5d5d6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the LCA distance between two nodes using information content, $D_{L C A}\left(y^{\prime}, y\right) := f(y) - f\left(N_{L C A}\left(y, y^{\prime}\right)\right)$, where $f$ is the information content.
- **Parent context**: The LCA distance has been implemented, as described in Section 2.

### R06: Code has been written to compute the LCA distance between tw...
- **Rubric ID**: c7bc93bd-2786-4613-a563-d6d2fdd74938
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the LCA distance between two nodes using tree depth, $D_{L C A}^P\left(y^{\prime}, y\right):=\left(P(y)-P\left(N_{L C A}\left(y^{\prime}, y\right)\right)\right)+\left(P\left(y^{\prime}\right)-P\left(N_{L C A}\left(y^{\prime}, y\right)\right)\right)$, where $P$ is a function which retrieves the depth of node $x$ from a tree $T$.
- **Parent context**: The LCA distance has been implemented, as described in Section 2.

### R07: Code has been written to compute the reverse LCA matrix by s...
- **Rubric ID**: 4337ed0c-25a7-496d-8b13-a63bb8337e89
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the reverse LCA matrix by subtracting the given LCA matrix from 1, as described in Step 2 in Algorithm 1.
- **Parent context**: The LCA alignment loss has been implemented, as described in Algorithm 1.

### R08: Code has been written to compute the predicted probabilities...
- **Rubric ID**: 9e88cced-9020-4b4d-8127-a83839d76e1d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the predicted probabilities from the logits by applying the softmax function along the correct dimension, as described in Step 3 of Algorithm 1.
- **Parent context**: The LCA alignment loss has been implemented, as described in Algorithm 1.

### R09: Code has been written to compute the standard cross-entropy...
- **Rubric ID**: fdebcd06-4561-4139-a083-51765bfb49cb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the standard cross-entropy loss using the one-hot encoded targets and the predicted probabilities, as described in Step 5 of Algorithm 1.
- **Parent context**: The LCA alignment loss has been implemented, as described in Algorithm 1.

### R10: Code has been written to compute the conditional soft loss a...
- **Rubric ID**: 8580ac2c-ca66-4df2-bf28-aeae62f74d46
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the conditional soft loss as described in Algorithm 1. This should select between computing binary cross-entropy (BCE) loss or a version of cross-entropy loss on the reverse LCA matrix, based on the value of 'alignment_mode', as described in Steps 6 - 10 of Algorithm 1.
- **Parent context**: The LCA alignment loss has been implemented, as described in Algorithm 1.

### R11: Code has been written to combine the standard loss and the c...
- **Rubric ID**: 2f544cf5-d8ff-4531-90a8-2a992dbae74b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to combine the standard loss and the computed soft loss with the lambda weight (e.g., $\text{total_loss} = $\lambda$ * \text{standard_loss} + \text{soft_loss}) and return the mean loss over the batch, as described in Steps 12 and 13 of Algorithm 1.
- **Parent context**: The LCA alignment loss has been implemented, as described in Algorithm 1.

### R12: All 36 VM architectures in Appendix A are enumerated in code...
- **Rubric ID**: 89178dc1-4c91-4420-a5a1-ba844f28384d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: All 36 VM architectures in Appendix A are enumerated in code.
- **Parent context**: All 36 Vision Models (VMs) are available to be queried.

### R13: All 39 VLM architectures in Appendix A are enumerated in cod...
- **Rubric ID**: a5e2feb0-ea72-4611-bbe7-c8b04884441b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: All 39 VLM architectures in Appendix A are enumerated in code.
- **Parent context**: All 39 Vision-Language Models (VLMs) are available to be queried.

### R14: For each of the 75 pre-trained models $M$, code has been wri...
- **Rubric ID**: 917720c6-4a3b-4b8b-a817-7df040085dab
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each of the 75 pre-trained models $M$, code has been written to use $M$ with the in-distribution ImageNet image test set data $X$ and labels $Y$ to extract and compute the average feature representation for each class.
- **Parent context**: 75 latent hierarchies have been computed using $k$-means clustering, with one hierarchy generated us...

### R15: For each of the 75 pre-trained models $M$, $M$ has been used...
- **Rubric ID**: 7245950d-e024-4f52-986c-c96eef90f3fa
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: For each of the 75 pre-trained models $M$, $M$ has been used with the in-distribution ImageNet image test set data $X$ and labels $Y$ to extract and compute the average feature representation for each class.
- **Parent context**: 75 latent hierarchies have been computed using $k$-means clustering, with one hierarchy generated us...

### R16: For each set of the 75 model-specific averaged class labels,...
- **Rubric ID**: 1b4732c1-25d8-4766-a3bd-0f47d666f595
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each set of the 75 model-specific averaged class labels, code has been written to compute a 9-layer hierarchical clustering using the $k$-means algorithm on the computed per-class average features setting the number of cluster centers as $2^i$, where $i$ ranges from 1, 2, 3, 4, ..., 9, as described in Appendix E.1.
- **Parent context**: 75 latent hierarchies have been computed using $k$-means clustering, with one hierarchy generated us...

### R17: For each set of the 75 model-specific averaged class labels,...
- **Rubric ID**: fd1dc370-52ff-4018-a004-8ced36e8addd
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: For each set of the 75 model-specific averaged class labels, a 9-layer hierarchical clustering using the $k$-means algorithm on the computed per-class average features setting the number of cluster centers as $2^i$, where $i$ ranges from 1, 2, 3, 4, ..., 9, has been computed, as described in Appendix E.1.
- **Parent context**: 75 latent hierarchies have been computed using $k$-means clustering, with one hierarchy generated us...

### R18: For each model, code has been written to compute the latent...
- **Rubric ID**: 40469efb-5c05-4a4a-a4c1-84b6a9a4584a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each model, code has been written to compute the latent class hierarchy by finding the lowest common ancestor nodes for every pair of classes based on the clustering outcomes. The cluster level at which a pair of classes first share a cluster is the pairwise LCA height.
- **Parent context**: 75 latent hierarchies have been computed using $k$-means clustering, with one hierarchy generated us...

### R19: For each model, the latent class hierarchy has been computed...
- **Rubric ID**: c9eec8ad-859f-4f97-b132-57238d9c6a49
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: For each model, the latent class hierarchy has been computed by finding the lowest common ancestor nodes for every pair of classes based on the clustering outcomes. The cluster level at which a pair of classes first share a cluster is the pairwise LCA height.
- **Parent context**: 75 latent hierarchies have been computed using $k$-means clustering, with one hierarchy generated us...

### R20: Code has been written to compute the $n \times n$ LCA distan...
- **Rubric ID**: a73ea29c-7b60-4ab3-9a57-698c908bd7c1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the $n \times n$ LCA distance matrix using tree node depth, where row $i$ and column $j$ correspond to the lowest common ancestor distance using node depth, $D_{LCA}^P(i, j)$, between class $i$ and class $j$ according to the WordNet hierarchy, as described in Appendix E.2.
- **Parent context**: The soft labels based on LCA distance using tree node depth and the WordNet hierarchy have been comp...

### R21: The $n \times n$ LCA distance matrix has been computed using...
- **Rubric ID**: b857f31e-a257-4827-a6df-f96b0a4e8bbe
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The $n \times n$ LCA distance matrix has been computed using tree node depth, where row $i$ and column $j$ correspond to the lowest common ancestor distance using node depth, $D_{LCA}^P(i, j)$, between class $i$ and class $j$ according to the WordNet hierarchy, as described in Appendix E.2.
- **Parent context**: The soft labels based on LCA distance using tree node depth and the WordNet hierarchy have been comp...

### R22: Code has been written to exponentiate all elements of the LC...
- **Rubric ID**: ff6349a8-e777-4ba3-b1e5-5743b87b79b5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to exponentiate all elements of the LCA distance matrix and apply minmax (i.e., $M_{\mathrm{LCA}}=\operatorname{MinMax}\left(M^T\right)$ where $T$ is the temperature).
- **Parent context**: The soft labels based on LCA distance using tree node depth and the WordNet hierarchy have been comp...

### R23: Code has been written to exponentiate all elements of the LC...
- **Rubric ID**: ed811ccd-9157-4edd-906b-31590ec2d766
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to exponentiate all elements of the LCA distance matrix by a temperature value $T$, as described in Appendix E.2.
- **Parent context**: The soft labels based on LCA distance using tree node depth and the WordNet hierarchy have been comp...

### R24: All elements of the LCA distance matrix have been exponentia...
- **Rubric ID**: cfdf727d-10d2-4d4a-89af-02df849194ea
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: All elements of the LCA distance matrix have been exponentiated by a temperature value $T$, as described in Appendix E.2.
- **Parent context**: The soft labels based on LCA distance using tree node depth and the WordNet hierarchy have been comp...

### R25: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: 1e8fe9fd-79c8-4c02-874b-c2078e883e0c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a ResNet-18 backbone by optimizing the probe using the cross entropy loss. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R26: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: e725f78b-9aca-4ce3-bae2-ae319291ebed
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a ResNet-18 backbone by optimizing the probe using the cross entropy loss. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R27: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: 4d1011c0-523d-4cb5-b3d6-eb13660b30b3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a ResNet-18 backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the WordNet hierarchy.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R28: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: 01918a1b-1298-4963-b961-0c8e26f0718f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a ResNet-50 backbone by optimizing the probe using the cross entropy loss. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R29: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: 9f622228-7a53-4c17-9c9d-1cee353d5917
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a ResNet-50 backbone by optimizing the probe using the cross entropy loss. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R30: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: b4f5c17a-e2ea-44a2-a66d-55f6485921cf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a ResNet-50 backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the WordNet hierarchy.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R31: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: bae4a653-2823-4135-be6f-24b0e7de83c7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a VIT-B backbone by optimizing the probe using the cross entropy loss. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R32: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: 7a7f2f28-7b5d-4451-bf06-c54cda5005ab
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a VIT-B backbone by optimizing the probe using the cross entropy loss. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R33: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: 8d753159-27a3-488d-838f-c9222a5b3fc4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a VIT-B backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the WordNet hierarchy.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R34: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: 0f3c67a2-d009-469d-a084-917ec30493f3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a VIT-L backbone by optimizing the probe using the cross entropy loss. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R35: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: 190f72c5-403e-4a07-a491-36cbf6df2214
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a VIT-L backbone by optimizing the probe using the cross entropy loss. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R36: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: bfa800d0-e179-4195-8d68-fef8244594fd
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a VIT-L backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the WordNet hierarchy.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R37: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: b7541451-d93c-4931-93e0-8f0b67b12d4c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a ConvNext backbone by optimizing the probe using the cross entropy loss. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R38: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: 94f7e77a-aefb-44b0-8927-19834a706339
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a ConvNext backbone by optimizing the probe using the cross entropy loss. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R39: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: 42104596-f5c9-4df0-89c9-7a9aa5ef92ce
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a ConvNext backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the WordNet hierarchy.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R40: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: 137aac0d-b874-4097-8aee-f1e315c489bd
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a Swin Transformer backbone by optimizing the probe using the cross entropy loss. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R41: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: 05ffa3fb-e239-41c1-b94a-c7a6d56a6093
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a Swin Transformer backbone by optimizing the probe using the cross entropy loss. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R42: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: baaa2209-1a83-4a92-9b0e-1148ff1a2be8
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a Swin Transformer backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the WordNet hierarchy.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R43: Code has been written to use the MnasNet model, $M$, with th...
- **Rubric ID**: e30ab55c-809e-4efc-bd2a-a8c64a2b786b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to use the MnasNet model, $M$, with the in-distribution ImageNet image test set data $X$ and labels $Y$ to compute the average feature representation for each class.
- **Parent context**: A latent hierarchy produced with MnasNet has been computed using $k$-means clustering, as described ...

### R44: The MnasNet model, $M$, has been used with the in-distributi...
- **Rubric ID**: 7fb2a220-dea5-4d07-aed8-0cf912568997
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The MnasNet model, $M$, has been used with the in-distribution ImageNet image test set data $X$ and labels $Y$ to compute the average feature representation for each class.
- **Parent context**: A latent hierarchy produced with MnasNet has been computed using $k$-means clustering, as described ...

### R45: Code has been written to perform a 9-layer hierarchical clus...
- **Rubric ID**: 71fb111d-2879-4346-9444-a305be94cfb0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to perform a 9-layer hierarchical clustering using the $k$-means algorithm on the per-class average features extracted by MnasNet. The number of cluster centers is set to $2^i$, where $i$ ranges from 1 to 9, as described in Appendix E.1.
- **Parent context**: A latent hierarchy produced with MnasNet has been computed using $k$-means clustering, as described ...

### R46: A 9-layer hierarchical clustering has been computed using th...
- **Rubric ID**: ba057805-241c-4c6d-b40d-b29def277f30
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A 9-layer hierarchical clustering has been computed using the $k$-means algorithm on the per-class average features extracted by MnasNet, with the number of cluster centers set to $2^i$, where $i$ ranges from 1 to 9, as described in Appendix E.1.
- **Parent context**: A latent hierarchy produced with MnasNet has been computed using $k$-means clustering, as described ...

### R47: For the clustered MnasNet class representations, code has be...
- **Rubric ID**: 323c4e36-8b47-4bca-8be2-0db209843aca
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the clustered MnasNet class representations, code has been written to compute the latent class hierarchy by finding the lowest common ancestor nodes for every pair of classes based on the clustering outcomes. The cluster level at which a pair of classes first share a cluster is the pairwise LCA height.
- **Parent context**: A latent hierarchy produced with MnasNet has been computed using $k$-means clustering, as described ...

### R48: For the clustered MnasNet class representations, the latent...
- **Rubric ID**: 0e390944-2c73-41a2-a62e-9e22d8f0b46f
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: For the clustered MnasNet class representations, the latent class hierarchy has been computed by finding the lowest common ancestor nodes for every pair of classes based on the clustering outcomes. The cluster level at which a pair of classes first share a cluster is the pairwise LCA height.
- **Parent context**: A latent hierarchy produced with MnasNet has been computed using $k$-means clustering, as described ...

### R49: Code has been written to use the ResNet-18 model, $M$, with...
- **Rubric ID**: f8efbab3-8171-411d-99b9-f19bddbdb67c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to use the ResNet-18 model, $M$, with the in-distribution ImageNet image test set data $X$ and labels $Y$ to compute the average feature representation for each class.
- **Parent context**: A latent hierarchy produced with the ResNet-18 model has been computed using $k$-means clustering, a...

### R50: Code has been written to perform a 9-layer hierarchical clus...
- **Rubric ID**: 62791914-70ab-436d-98a1-64e2a655a2ca
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to perform a 9-layer hierarchical clustering using the $k$-means algorithm on the per-class average features extracted by the ResNet-18 model. The number of cluster centers is set to $2^i$, where $i$ ranges from 1 to 9, as described in Appendix E.1.
- **Parent context**: A latent hierarchy produced with the ResNet-18 model has been computed using $k$-means clustering, a...

### R51: A 9-layer hierarchical clustering has been computed using th...
- **Rubric ID**: f6108c38-6c2f-4553-9420-fc82cf30028e
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A 9-layer hierarchical clustering has been computed using the $k$-means algorithm on the per-class average features extracted by the ResNet-18 model, with the number of cluster centers set to $2^i$, where $i$ ranges from 1 to 9, as described in Appendix E.1.
- **Parent context**: A latent hierarchy produced with the ResNet-18 model has been computed using $k$-means clustering, a...

### R52: For the clustered ResNet-18 class representations, the laten...
- **Rubric ID**: 27fae5c7-62b7-4dcb-bf02-09b9da549a57
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: For the clustered ResNet-18 class representations, the latent class hierarchy has been computed by finding the lowest common ancestor nodes for every pair of classes based on the clustering outcomes. The cluster level at which a pair of classes first share a cluster is the pairwise LCA height.
- **Parent context**: A latent hierarchy produced with the ResNet-18 model has been computed using $k$-means clustering, a...

### R53: Code has been written to use the vit-1-14 model, $M$, with t...
- **Rubric ID**: a5e07a67-22a8-4971-9548-45d9e6f26f71
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to use the vit-1-14 model, $M$, with the in-distribution ImageNet image test set data $X$ and labels $Y$ to compute the average feature representation for each class.
- **Parent context**: A latent hierarchy produced with the vit-1-14 model has been computed using $k$-means clustering, as...

### R54: The vit-1-14 model, $M$, has been used with the in-distribut...
- **Rubric ID**: d33811e3-e182-4746-91a6-6a8e8c03eefc
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The vit-1-14 model, $M$, has been used with the in-distribution ImageNet image test set data $X$ and labels $Y$ to compute the average feature representation for each class.
- **Parent context**: A latent hierarchy produced with the vit-1-14 model has been computed using $k$-means clustering, as...

### R55: Code has been written to perform a 9-layer hierarchical clus...
- **Rubric ID**: c8c3d420-7264-4d2d-88cc-00bd403150be
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to perform a 9-layer hierarchical clustering using the $k$-means algorithm on the per-class average features extracted by the vit-1-14 model. The number of cluster centers is set to $2^i$, where $i$ ranges from 1 to 9, as described in Appendix E.1.
- **Parent context**: A latent hierarchy produced with the vit-1-14 model has been computed using $k$-means clustering, as...

### R56: A 9-layer hierarchical clustering has been computed using th...
- **Rubric ID**: 865fa279-5670-4115-8840-f48cea16b88a
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A 9-layer hierarchical clustering has been computed using the $k$-means algorithm on the per-class average features extracted by the vit-1-14 model, with the number of cluster centers set to $2^i$, where $i$ ranges from 1 to 9, as described in Appendix E.1.
- **Parent context**: A latent hierarchy produced with the vit-1-14 model has been computed using $k$-means clustering, as...

### R57: For the clustered vit-1-14 class representations, code has b...
- **Rubric ID**: 5b651a0d-9121-4c4b-9cd3-c616ccb5b738
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the clustered vit-1-14 class representations, code has been written to compute the latent class hierarchy by finding the lowest common ancestor nodes for every pair of classes based on the clustering outcomes. The cluster level at which a pair of classes first share a cluster is the pairwise LCA height.
- **Parent context**: A latent hierarchy produced with the vit-1-14 model has been computed using $k$-means clustering, as...

### R58: For the clustered vit-1-14 class representations, the latent...
- **Rubric ID**: 063a173a-3e9e-4d9f-bfdc-7eea19a060e6
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: For the clustered vit-1-14 class representations, the latent class hierarchy has been computed by finding the lowest common ancestor nodes for every pair of classes based on the clustering outcomes. The cluster level at which a pair of classes first share a cluster is the pairwise LCA height.
- **Parent context**: A latent hierarchy produced with the vit-1-14 model has been computed using $k$-means clustering, as...

### R59: Code has been written to use the OpenCLIP(vit-l-14) model, $...
- **Rubric ID**: 4cf68e6c-13d8-4145-9eb4-f05af515093c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to use the OpenCLIP(vit-l-14) model, $M$, with the in-distribution ImageNet image test set data $X$ and labels $Y$ to compute the average feature representation for each class.
- **Parent context**: A latent hierarchy produced with the OpenCLIP(vit-l-14) model has been computed using $k$-means clus...

### R60: Code has been written to perform a 9-layer hierarchical clus...
- **Rubric ID**: a581d827-f8ff-4a23-acf9-00885aebed46
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to perform a 9-layer hierarchical clustering using the $k$-means algorithm on the per-class average features extracted by the OpenCLIP(vit-l-14) model. The number of cluster centers is set to $2^i$, where $i$ ranges from 1 to 9, as described in Appendix E.1.
- **Parent context**: A latent hierarchy produced with the OpenCLIP(vit-l-14) model has been computed using $k$-means clus...

### R61: A 9-layer hierarchical clustering has been computed using th...
- **Rubric ID**: 05a3ea15-094f-460c-bf9c-f333c06b8f7c
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A 9-layer hierarchical clustering has been computed using the $k$-means algorithm on the per-class average features extracted by the OpenCLIP(vit-l-14) model, with the number of cluster centers set to $2^i$, where $i$ ranges from 1 to 9, as described in Appendix E.1.
- **Parent context**: A latent hierarchy produced with the OpenCLIP(vit-l-14) model has been computed using $k$-means clus...

### R62: For the clustered OpenCLIP(vit-l-14) class representations,...
- **Rubric ID**: 8df4cc83-ffe2-4b34-b4ad-5f7766d61478
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For the clustered OpenCLIP(vit-l-14) class representations, code has been written to compute the latent class hierarchy by finding the lowest common ancestor nodes for every pair of classes based on the clustering outcomes. The cluster level at which a pair of classes first share a cluster is the pairwise LCA height.
- **Parent context**: A latent hierarchy produced with the OpenCLIP(vit-l-14) model has been computed using $k$-means clus...

### R63: For the clustered OpenCLIP(vit-l-14) class representations,...
- **Rubric ID**: ea122b1d-2ca4-4eb1-82e4-01a6e45cf2ca
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: For the clustered OpenCLIP(vit-l-14) class representations, the latent class hierarchy has been computed by finding the lowest common ancestor nodes for every pair of classes based on the clustering outcomes. The cluster level at which a pair of classes first share a cluster is the pairwise LCA height.
- **Parent context**: A latent hierarchy produced with the OpenCLIP(vit-l-14) model has been computed using $k$-means clus...

### R64: Code has been written to compute the $n \times n$ LCA distan...
- **Rubric ID**: 6b009a22-b296-472e-9451-e88993a37b02
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the $n \times n$ LCA distance matrix, where row $i$ and column $j$ correspond to the lowest common ancestor distance, $D_{LCA}(i, j)$, between class $i$ and class $j$ according to the latent hierarchy computed using the Mnasnet model, as described in Appendix E.2.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R65: The $n \times n$ LCA distance matrix has been computed, wher...
- **Rubric ID**: da3cbda5-9ef6-4f5f-a14f-236770f94db1
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The $n \times n$ LCA distance matrix has been computed, where row $i$ and column $j$ correspond to the lowest common ancestor distance using node depth, $D_{LCA}^P(i, j)$, between class $i$ and class $j$ according to the latent hierarchy computed using the Mnasnet model, as described in Appendix E.2.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R66: Code has been written to exponentiate all elements of the LC...
- **Rubric ID**: 5ad75244-582c-4088-9b9e-7fc4fdaffcad
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to exponentiate all elements of the LCA distance (using node depth in the tree hierarchy) matrix and apply minmax (i.e., $M_{\mathrm{LCA}}=\operatorname{MinMax}\left(M^T\right)$).
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R67: All elements of the LCA distance (using node depth in the tr...
- **Rubric ID**: 78c82d85-04cf-40e6-b909-88dffeb8db8b
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: All elements of the LCA distance (using node depth in the tree hierarchy) matrix have been exponentiated followed by minmax scaling (i.e., $M_{\mathrm{LCA}}=\operatorname{MinMax}\left(M^T\right)$).
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R68: Code has been written to compute invert the $n \times n$ LCA...
- **Rubric ID**: f56e5446-b391-4aa3-a872-309e74d53338
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute invert the $n \times n$ LCA distance matrix, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R69: The $n \times n$ LCA distance matrix has been inverted, as d...
- **Rubric ID**: 4dc7f404-fc41-4a5b-8a37-6289e8c42e14
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The $n \times n$ LCA distance matrix has been inverted, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R70: Code has been written to compute the $n \times n$ LCA distan...
- **Rubric ID**: 1d77aefa-52e8-4d21-9902-02cbefe69f08
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the $n \times n$ LCA distance matrix, where row $i$ and column $j$ correspond to the lowest common ancestor distance using node depth, $D_{LCA}^P(i, j)$, between class $i$ and class $j$ according to the latent hierarchy computed using the ResNet-18 model, as described in Appendix E.2.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R71: The $n \times n$ LCA distance matrix has been computed, wher...
- **Rubric ID**: 0c6e6199-8f4c-4685-b7e9-1c09fb80a8c7
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The $n \times n$ LCA distance matrix has been computed, where row $i$ and column $j$ correspond to the lowest common ancestor distance using node depth, $D_{LCA}^P(i, j)$, between class $i$ and class $j$ according to the latent hierarchy computed using the ResNet-18 model, as described in Appendix E.2.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R72: Code has been written to exponentiate all elements of the LC...
- **Rubric ID**: 78c41efa-b1f2-4d3b-80a5-7f063223ba87
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to exponentiate all elements of the LCA distance (using node depth in the tree hierarchy) matrix and apply minmax (i.e., $M_{\mathrm{LCA}}=\operatorname{MinMax}\left(M^T\right)$).
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R73: All elements of the LCA distance (using node depth in the tr...
- **Rubric ID**: 3813681e-e1b1-4cfd-85e4-722ad6ab3d53
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: All elements of the LCA distance (using node depth in the tree hierarchy) matrix have been exponentiated followed by minmax scaling (i.e., $M_{\mathrm{LCA}}=\operatorname{MinMax}\left(M^T\right)$).
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R74: Code has been written to invert the LCA distance matrix $max...
- **Rubric ID**: 416ab149-ad9f-4c7e-a072-1bb31611c1d4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to invert the LCA distance matrix $max(M) - M$, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R75: The LCA distance matrix has been inverted $max(M) - M$, as d...
- **Rubric ID**: 735f24e6-bacf-4990-9afc-3aa057fc6bc1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The LCA distance matrix has been inverted $max(M) - M$, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R76: Code has been written to compute invert the $n \times n$ LCA...
- **Rubric ID**: 81b24325-1013-42c7-9481-4f952dc33c0d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute invert the $n \times n$ LCA distance matrix, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R77: The $n \times n$ LCA distance matrix has been inverted, as d...
- **Rubric ID**: 2040a0e1-6788-4236-95f6-dd2b4e016c12
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The $n \times n$ LCA distance matrix has been inverted, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R78: Code has been written to compute the $n \times n$ LCA distan...
- **Rubric ID**: 5182974a-346d-4835-98ee-a89e9baead8e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the $n \times n$ LCA distance matrix, where row $i$ and column $j$ correspond to the lowest common ancestor distance using node depth, $D_{LCA}^P(i, j)$, between class $i$ and class $j$ according to the latent hierarchy computed using the vit-1-14 model, as described in Appendix E.2.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R79: The $n \times n$ LCA distance matrix has been computed, wher...
- **Rubric ID**: 650d1352-4224-46eb-b540-914972bf991f
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The $n \times n$ LCA distance matrix has been computed, where row $i$ and column $j$ correspond to the lowest common ancestor distance using node depth, $D_{LCA}^P(i, j)$, between class $i$ and class $j$ according to the latent hierarchy computed using the vit-1-14 model, as described in Appendix E.2.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R80: Code has been written to exponentiate all elements of the LC...
- **Rubric ID**: de26413a-8058-45ad-9bae-3dc454235324
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to exponentiate all elements of the LCA distance (using node depth in the tree hierarchy) matrix and apply minmax (i.e., $M_{\mathrm{LCA}}=\operatorname{MinMax}\left(M^T\right)$).
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R81: All elements of the LCA distance (using node depth in the tr...
- **Rubric ID**: 2537d0aa-1a4c-46bb-9add-3ad790832ba4
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: All elements of the LCA distance (using node depth in the tree hierarchy) matrix have been exponentiated followed by minmax scaling (i.e., $M_{\mathrm{LCA}}=\operatorname{MinMax}\left(M^T\right)$).
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R82: Code has been written to invert the LCA distance matrix $max...
- **Rubric ID**: 8b06a5bb-4e0c-4325-a43d-4d9909aa5e07
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to invert the LCA distance matrix $max(M) - M$, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R83: The LCA distance matrix has been inverted $max(M) - M$, as d...
- **Rubric ID**: 1b3f5136-2af9-4b3f-906d-2723d21c16c5
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The LCA distance matrix has been inverted $max(M) - M$, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R84: Code has been written to compute invert the $n \times n$ LCA...
- **Rubric ID**: 57b89448-2520-4def-92b9-dcaf97bbebfa
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute invert the $n \times n$ LCA distance matrix, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R85: The $n \times n$ LCA distance matrix has been inverted, as d...
- **Rubric ID**: b3ab91e9-e216-49e3-98a5-4495c7bc4643
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The $n \times n$ LCA distance matrix has been inverted, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R86: Code has been written to compute the $n \times n$ LCA distan...
- **Rubric ID**: 86c4b76d-7c7c-4e79-b555-40bcffaca26d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute the $n \times n$ LCA distance matrix, where row $i$ and column $j$ correspond to the lowest common ancestor distance using node depth, $D_{LCA}^P(i, j)$, between class $i$ and class $j$ according to the latent hierarchy computed using the OpenCLIP(vit-l-14) model, as described in Appendix E.2.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R87: The $n \times n$ LCA distance matrix has been computed, wher...
- **Rubric ID**: e6da095a-eb9c-42a5-92b4-6b3f4a5e391b
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The $n \times n$ LCA distance matrix has been computed, where row $i$ and column $j$ correspond to the lowest common ancestor distance using node depth, $D_{LCA}^P(i, j)$, between class $i$ and class $j$ according to the latent hierarchy computed using the OpenCLIP(vit-l-14) model, as described in Appendix E.2.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R88: Code has been written to exponentiate all elements of the LC...
- **Rubric ID**: d17ee8a4-58c5-448f-b2c3-f31ff7cb1c4c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to exponentiate all elements of the LCA distance (using node depth in the tree hierarchy) matrix and apply minmax (i.e., $M_{\mathrm{LCA}}=\operatorname{MinMax}\left(M^T\right)$).
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R89: All elements of the LCA distance (using node depth in the tr...
- **Rubric ID**: d14f2015-9229-401d-9593-8d31f9927476
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: All elements of the LCA distance (using node depth in the tree hierarchy) matrix have been exponentiated followed by minmax scaling (i.e., $M_{\mathrm{LCA}}=\operatorname{MinMax}\left(M^T\right)$).
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R90: Code has been written to invert the LCA distance matrix $max...
- **Rubric ID**: b8f7cbea-f1fc-403f-9be1-65845fafe2c3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to invert the LCA distance matrix $max(M) - M$, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R91: The LCA distance matrix has been inverted $max(M) - M$, as d...
- **Rubric ID**: ffe46762-ed1f-43fe-82f7-8cf51a9e78d1
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The LCA distance matrix has been inverted $max(M) - M$, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R92: Code has been written to compute invert the $n \times n$ LCA...
- **Rubric ID**: 5e7ea0f2-7247-4520-be64-f7ca8684d27a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to compute invert the $n \times n$ LCA distance matrix, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R93: The $n \times n$ LCA distance matrix has been inverted, as d...
- **Rubric ID**: acdc6a11-6c82-41b4-ba8a-3e296ea57a53
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The $n \times n$ LCA distance matrix has been inverted, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R94: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: 7e3348fa-01dc-4b24-8818-cb27821c0c67
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a ResNet-18 backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the latent hierarchy determined by MnasNet.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R95: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: cbd51f39-06a8-4a7d-9d46-df02e2e49769
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a ResNet-18 backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the latent hierarchy determined by ResNet-18.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R96: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: a36718b1-9a32-4275-9ea6-f48e6b0e9998
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a ResNet-18 backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the latent hierarchy determined by ResNet-18.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R97: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: 3e86d264-7d69-411d-b4be-586c2a3e2006
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a ResNet-18 backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the latent hierarchy determined by vit-1-14.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R98: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: 75446d0a-785d-48ef-bac0-b090b05849d7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a ResNet-18 backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the latent hierarchy determined by OpenCLIP(vit-1-14).
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R99: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: bee479fe-66c6-4413-be3b-be553ddbcb4a
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a ResNet-18 backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the latent hierarchy determined by OpenCLIP(vit-1-14).
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

## Evaluation, Metrics & Benchmarking

### R100: The LCA distance for a model on dataset $\mathcal{M}:=X_1, \...
- **Rubric ID**: ca51e156-4e6f-4859-94ed-6db53ea1d978
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The LCA distance for a model on dataset $\mathcal{M}:=X_1, \ldots, X_n$ has been implemented as $D_{L C A}(\text { model }, \mathcal{M}) := \frac{1}{n} \sum_{i=1}^n D_{L C A}\left(\widehat{y}_i, y_i\right) \Longleftrightarrow y_i \neq \widehat{y}_i$ where $\hat{y}_i$ is the predicted class for sample $X_i$ using the model, $y_i$ is the ground truth class for sample $X_i$, and $y_i \neq \hat{y}_i$.
- **Parent context**: The LCA distance has been implemented, as described in Section 2.

### R101: Code to compute the coefficient of determination, $R^2$, has...
- **Rubric ID**: db79b149-e8a7-4b7a-b5b3-f8c3589b43b0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute the coefficient of determination, $R^2$, has been implemented according to Equation (2) in Appendix D.1.1 i.e., $R^2=1-\frac{\sum_{i=1}^n\left(y_i-f\left(x_i\right)\right)^2}{\sum_{i=1}^n\left(y_i-\bar{y}\right)^2}$ where $f(x_i)$ is the prediction of $y_i$ from the model, $\bar{y}$ is the mean of the actual $y$ values, and $n$ is the number of data points. Min-max scaling has been used to pre-process to input, transforming it to the range [0, 1].
- **Parent context**: All evaluation metrics have been implemented.

### R102: Code to compute the Pearson correlation coefficient (PEA) ha...
- **Rubric ID**: c98a690a-0a93-42eb-bee1-f66e408b6f94
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute the Pearson correlation coefficient (PEA) has been implemented according to Equation (3) in Appendix D.1.1 i.e., $r=\frac{\sum_{i=1}^n\left(x_i-\bar{x}\right)\left(y_i-\bar{y}\right)}{\sqrt{\sum_{i=1}^n\left(x_i-\bar{x}\right)^2} \sqrt{\sum_{i=1}^n\left(y_i-\bar{y}\right)^2}}$ where $\bar{x}$ and $\bar{y}$ are the mean values of the datasets $x$ and $y$, respectively, and $n$ is the number of data points. Min-max scaling has been used to pre-process to input, transforming it to the range [0, 1].
- **Parent context**: All evaluation metrics have been implemented.

### R103: Code to compute the Kendall rank correlation coefficient (KE...
- **Rubric ID**: f96bc158-7ccb-490a-bf6f-30c2523245df
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute the Kendall rank correlation coefficient (KEN) has been implemented according to Equation (4) in Appendix D.1.2 i.e., $\tau=\frac{\text { (number of concordant pairs) }- \text { (number of discordant pairs) }}{\frac{1}{2} n(n-1)}$ where $n$ is the number of data points. Min-max scaling has been used to pre-process to input, transforming it to the range [0, 1].
- **Parent context**: All evaluation metrics have been implemented.

### R104: Code to compute the Spearman rank-order correlation coeffici...
- **Rubric ID**: aa18ad82-bd0a-49e3-b0ba-284ca8908ded
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute the Spearman rank-order correlation coefficient (SPE) has been implemented according to Equation (5) in Appendix D.1.2 i.e., $\rho=1-\frac{6 \sum_{i=1}^n d_i^2}{n\left(n^2-1\right)}$ where $d_i$ is the difference between the ranks of corresponding data points in the two datasets and $n$ is the number of data points. Min-max scaling has been used to pre-process to input, transforming it to the range [0, 1].
- **Parent context**: All evaluation metrics have been implemented.

### R105: Code to compute the Mean Absolute Error (MAE) has been imple...
- **Rubric ID**: db064bf8-cb08-4bcf-8cde-122c82952b53
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute the Mean Absolute Error (MAE) has been implemented.
- **Parent context**: All evaluation metrics have been implemented.

### R106: Code to compute top-1 accuracy has been implemented.
- **Rubric ID**: d50ac494-aa2a-4c58-b95f-12ed16b4a7e2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute top-1 accuracy has been implemented.
- **Parent context**: All evaluation metrics have been implemented.

### R107: Code to compute top-5 accuracy has been implemented.
- **Rubric ID**: 3d7f4028-6ced-4fdc-83a7-b499ff7ca402
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute top-5 accuracy has been implemented.
- **Parent context**: All evaluation metrics have been implemented.

### R108: Code to evaluate all 36 Vision Models in Appendix A on the I...
- **Rubric ID**: 87244cf3-11ae-44c4-ab82-24f572f25eeb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 36 Vision Models in Appendix A on the ImageNet test set has been written, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) average LCA distance (using information c...

### R109: All 36 Vision Models in Appendix A have been evaluated on th...
- **Rubric ID**: b6b8e787-40f2-44ef-b599-ac5fac1cd174
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models in Appendix A have been evaluated on the ImageNet test set, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) average LCA distance (using information c...

### R110: Code to evaluate all 39 Vision-Language Models in Appendix A...
- **Rubric ID**: b531609e-96bf-42b3-ac96-1277c986ffc2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 39 Vision-Language Models in Appendix A on the ImageNet test set has been written, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) average LCA distance (using info...

### R111: All 39 Vision-Language Models in Appendix A have been evalua...
- **Rubric ID**: e1c4f0c7-ec19-4bc3-8b4c-234761bb2340
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models in Appendix A have been evaluated on the ImageNet test set, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) average LCA distance (using info...

### R112: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: d7ff490a-dd6d-40bd-8812-a83a79e0de83
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution Top-1 accuracy on the ObjectNet test set com...

### R113: All 36 Vision Models have been evaluated on the ObjectNet te...
- **Rubric ID**: 0a971622-51ac-4316-bd23-a0d6c685f8f4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution Top-1 accuracy on the ObjectNet test set com...

### R114: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: d3b6dca2-a1a8-4b8a-93de-b0fabbfc735a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution Top-1 accuracy on the ObjectNet tes...

### R115: All 39 Vision-Language Models have been evaluated on the Obj...
- **Rubric ID**: 0933650d-eb24-4ea3-b19e-18341e19958f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution Top-1 accuracy on the ObjectNet tes...

### R116: Code has been written to compute a line of best fit between...
- **Rubric ID**: 8f2c4d01-616b-4f8f-9d56-e0b886c1b24a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute a line of best fit between the average LCA distance (using information content) on the ImageNet test set and the Top-1 test accuracy on the out-of-distribution ObjectNet dataset.
- **Parent context**: A line of best fit has been computed between the average LCA distance (using information content) on...

### R117: The slope of the line of best fit between in-distribution Im...
- **Rubric ID**: 6717c081-7d4d-4803-82ed-ed6d831e50ef
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The slope of the line of best fit between in-distribution ImageNet (y-axis) Top-1 test accuracy and the Top-1 test accuracy on the out-of-distribution ObjectNet dataset (x-axis) is positive.
- **Parent context**: Figure 1 has been reproduced.

### R118: The slope of the line of best fit between in-distribution Im...
- **Rubric ID**: 0e58be49-2e5f-43fd-a514-e547dc3db674
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The slope of the line of best fit between in-distribution ImageNet (y-axis) average LCA distance (using information content) on the test set and the Top-1 test accuracy on the out-of-distribution ObjectNet dataset (x-axis) is negative.
- **Parent context**: Figure 1 has been reproduced.

### R119: Code to evaluate ResNet18 on the ImageNet test set has been...
- **Rubric ID**: 401841b7-260a-4843-a4e5-e7118b32f859
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate ResNet18 on the ImageNet test set has been written, computing and saving both the average LCA distance (using information content) and Top-1 accuracy.
- **Parent context**: ResNet18 was evaluated on the ImageNet test set, with the average LCA distance (using information co...

### R120: ResNet18 has been evaluated on the ImageNet test set, comput...
- **Rubric ID**: 0a25d842-cefb-474a-97a7-4ef4fe2999a1
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: ResNet18 has been evaluated on the ImageNet test set, computing and saving both the average LCA distance (using information content) and Top-1 accuracy.
- **Parent context**: ResNet18 was evaluated on the ImageNet test set, with the average LCA distance (using information co...

### R121: Code to evaluate ResNet18 on the ImageNet-Sketch test set ha...
- **Rubric ID**: 0ab5de18-278b-4d89-9deb-f95250ff7bf0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate ResNet18 on the ImageNet-Sketch test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet18 was evaluated on the ImageNet-Sketch test set, with the Top-1 accuracy metrics computed and...

### R122: ResNet18 has been evaluated on the ImageNet-Sketch test set,...
- **Rubric ID**: 15257957-95eb-4046-8e53-b6208ae7b601
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: ResNet18 has been evaluated on the ImageNet-Sketch test set, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet18 was evaluated on the ImageNet-Sketch test set, with the Top-1 accuracy metrics computed and...

### R123: Code to evaluate ResNet18 on the ImageNet-Rendition test set...
- **Rubric ID**: 738e0aa0-db15-491f-b30d-6bc6e22abb1b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate ResNet18 on the ImageNet-Rendition test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet18 was evaluated on the ImageNet-Rendition test set, with the Top-1 accuracy metrics computed ...

### R124: ResNet18 has been evaluated on the ImageNet-Rendition test s...
- **Rubric ID**: d519e9fc-684d-4fac-bc00-a5e7a32d9ca0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: ResNet18 has been evaluated on the ImageNet-Rendition test set, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet18 was evaluated on the ImageNet-Rendition test set, with the Top-1 accuracy metrics computed ...

### R125: Code to evaluate ResNet18 on the ImageNet-Adversarial test s...
- **Rubric ID**: 31dd84b2-c2c8-40e0-b1ee-9955f62fed18
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate ResNet18 on the ImageNet-Adversarial test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet18 was evaluated on the ImageNet-Adversarial test set, with the Top-1 accuracy metrics compute...

### R126: ResNet18 has been evaluated on the ImageNet-Adversarial test...
- **Rubric ID**: 7919518e-256f-4d8d-b8b4-e55b382097a6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: ResNet18 has been evaluated on the ImageNet-Adversarial test set, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet18 was evaluated on the ImageNet-Adversarial test set, with the Top-1 accuracy metrics compute...

### R127: Code to evaluate ResNet18 on the ObjectNet test set has been...
- **Rubric ID**: f88d6e71-9ad7-4aa1-a545-4104e5489327
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate ResNet18 on the ObjectNet test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet18 was evaluated on the ObjectNet test set, with the Top-1 accuracy metrics computed and saved...

### R128: ResNet18 has been evaluated on the ObjectNet test set, compu...
- **Rubric ID**: e1011195-fc14-4f38-bd9c-94e804f100ea
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: ResNet18 has been evaluated on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet18 was evaluated on the ObjectNet test set, with the Top-1 accuracy metrics computed and saved...

### R129: Code to evaluate ResNet50 on the ImageNet test set has been...
- **Rubric ID**: ab6c5816-f0b8-40f2-8d4b-352996cdf2b0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate ResNet50 on the ImageNet test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet50 was evaluated on the ImageNet test set, with the average LCA distance (using information co...

### R130: ResNet50 has been evaluated on the ImageNet test set, comput...
- **Rubric ID**: 9fb0c74b-e410-4216-8672-89c7b4fffffa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: ResNet50 has been evaluated on the ImageNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet50 was evaluated on the ImageNet test set, with the average LCA distance (using information co...

### R131: Code to evaluate ResNet50 on the ImageNet-Sketch test set ha...
- **Rubric ID**: 841446d4-dd9b-4f30-94fd-fdf5e0611a95
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate ResNet50 on the ImageNet-Sketch test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet50 was evaluated on the ImageNet-Sketch test set, with the Top-1 accuracy computed and saved.

### R132: ResNet50 has been evaluated on the ImageNet-Sketch test set,...
- **Rubric ID**: 5ab7b8f5-efaf-4a2e-94d5-a21baf13c6f8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: ResNet50 has been evaluated on the ImageNet-Sketch test set, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet50 was evaluated on the ImageNet-Sketch test set, with the Top-1 accuracy computed and saved.

### R133: Code to evaluate ResNet50 on the ImageNet-Rendition test set...
- **Rubric ID**: 843cb5a0-a995-4fe3-be9d-cb6273015335
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate ResNet50 on the ImageNet-Rendition test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet50 was evaluated on the ImageNet-Rendition test set, with the Top-1 accuracy computed and save...

### R134: ResNet50 has been evaluated on the ImageNet-Rendition test s...
- **Rubric ID**: d04a001f-95de-4ad3-a58b-98247b6f7295
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: ResNet50 has been evaluated on the ImageNet-Rendition test set, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet50 was evaluated on the ImageNet-Rendition test set, with the Top-1 accuracy computed and save...

### R135: Code to evaluate ResNet50 on the ImageNet-Adversarial test s...
- **Rubric ID**: 249ffd18-b5bf-4c04-b3b4-f0e28bf07113
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate ResNet50 on the ImageNet-Adversarial test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet50 was evaluated on the ImageNet-Adversarial test set, with the Top-1 accuracy computed and sa...

### R136: ResNet50 has been evaluated on the ImageNet-Adversarial test...
- **Rubric ID**: 82862f6c-42dd-43b0-ab70-5cc7a16f546f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: ResNet50 has been evaluated on the ImageNet-Adversarial test set, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet50 was evaluated on the ImageNet-Adversarial test set, with the Top-1 accuracy computed and sa...

### R137: Code to evaluate ResNet50 on the ObjectNet test set has been...
- **Rubric ID**: 2b5a251d-4837-45ff-8767-79017d447035
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate ResNet50 on the ObjectNet test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet50 was evaluated on the ObjectNet test set, with the Top-1 accuracy computed and saved.

### R138: ResNet50 has been evaluated on the ObjectNet test set, compu...
- **Rubric ID**: 26aed230-d5df-4f0e-b967-53727b03030f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: ResNet50 has been evaluated on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: ResNet50 was evaluated on the ObjectNet test set, with the Top-1 accuracy computed and saved.

### R139: Code to evaluate CLIP_RN50 on the ImageNet test set has been...
- **Rubric ID**: 1ec4911d-64b0-4ba1-822b-f93046c628c3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate CLIP_RN50 on the ImageNet test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50 was evaluated on the ImageNet test set, with the average LCA distance (using information c...

### R140: CLIP_RN50 has been evaluated on the ImageNet test set, compu...
- **Rubric ID**: 8b337d0b-2c7d-4539-99c2-53f32ee82069
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: CLIP_RN50 has been evaluated on the ImageNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50 was evaluated on the ImageNet test set, with the average LCA distance (using information c...

### R141: Code to evaluate CLIP_RN50 on the ImageNet-Sketch test set h...
- **Rubric ID**: 1140905b-ac38-4bde-bb79-bf9a32a045bc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate CLIP_RN50 on the ImageNet-Sketch test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50 was evaluated on the ImageNet-Sketch test set, with the Top-1 accuracy computed and saved.

### R142: CLIP_RN50 has been evaluated on the ImageNet-Sketch test set...
- **Rubric ID**: 918b0b64-3a63-4fc3-a5ae-0b45193b4df2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: CLIP_RN50 has been evaluated on the ImageNet-Sketch test set, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50 was evaluated on the ImageNet-Sketch test set, with the Top-1 accuracy computed and saved.

### R143: Code to evaluate CLIP_RN50 on the ImageNet-Rendition test se...
- **Rubric ID**: 27a6f695-7ed0-45d5-a6c1-cde28f64a67c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate CLIP_RN50 on the ImageNet-Rendition test set has been written, computing and saving theTop-1 accuracy.
- **Parent context**: CLIP_RN50 was evaluated on the ImageNet-Rendition test set, with the Top-1 accuracy computed and sav...

### R144: CLIP_RN50 has been evaluated on the ImageNet-Rendition test...
- **Rubric ID**: 3be55da7-8edb-47e0-8ed9-79df76ccd868
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: CLIP_RN50 has been evaluated on the ImageNet-Rendition test set, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50 was evaluated on the ImageNet-Rendition test set, with the Top-1 accuracy computed and sav...

### R145: Code to evaluate CLIP_RN50 on the ImageNet-Adversarial test...
- **Rubric ID**: e0268799-7823-498e-afc1-c89a0b9c83c8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate CLIP_RN50 on the ImageNet-Adversarial test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50 was evaluated on the ImageNet-Adversarial test set, with the Top-1 accuracy computed and s...

### R146: CLIP_RN50 has been evaluated on the ImageNet-Adversarial tes...
- **Rubric ID**: 691c0fc3-31ef-4e00-a03b-34601eccfabe
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: CLIP_RN50 has been evaluated on the ImageNet-Adversarial test set, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50 was evaluated on the ImageNet-Adversarial test set, with the Top-1 accuracy computed and s...

### R147: Code to evaluate CLIP_RN50 on the ObjectNet test set has bee...
- **Rubric ID**: d819f952-6e83-4190-a868-1eee36d083b1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate CLIP_RN50 on the ObjectNet test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50 was evaluated on the ObjectNet test set, with the Top-1 accuracy computed and saved.

### R148: CLIP_RN50 has been evaluated on the ObjectNet test set, comp...
- **Rubric ID**: 9943a161-6d65-45fa-a202-66144b15aff6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: CLIP_RN50 has been evaluated on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50 was evaluated on the ObjectNet test set, with the Top-1 accuracy computed and saved.

### R149: Code to evaluate CLIP_RN50x4 on the ImageNet test set has be...
- **Rubric ID**: 5ace6dff-cfe6-4c3f-906c-4738557683b0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate CLIP_RN50x4 on the ImageNet test set has been written, computing and saving both the average LCA distance (using information content) and Top-1 accuracy.
- **Parent context**: CLIP_RN50x4 was evaluated on the ImageNet test set, with the average LCA distance (using information...

### R150: CLIP_RN50x4 has been evaluated on the ImageNet test set, com...
- **Rubric ID**: 5f0ac033-acf0-4d37-8e22-2f671346fdd4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: CLIP_RN50x4 has been evaluated on the ImageNet test set, computing and saving both the average LCA distance (using information content) and Top-1 accuracy.
- **Parent context**: CLIP_RN50x4 was evaluated on the ImageNet test set, with the average LCA distance (using information...

### R151: Code to evaluate CLIP_RN50x4 on the ImageNet-Sketch test set...
- **Rubric ID**: 724b3437-baf1-4aac-8985-8ddb18b6fdf7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate CLIP_RN50x4 on the ImageNet-Sketch test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50x4 was evaluated on the ImageNet-Sketch test set, with the Top-1 accuracy computed and save...

### R152: CLIP_RN50x4 has been evaluated on the ImageNet-Sketch test s...
- **Rubric ID**: e248d48c-c2c9-4ff1-8e1f-344c35838af5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: CLIP_RN50x4 has been evaluated on the ImageNet-Sketch test set, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50x4 was evaluated on the ImageNet-Sketch test set, with the Top-1 accuracy computed and save...

### R153: Code to evaluate CLIP_RN50x4 on the ImageNet-Rendition test...
- **Rubric ID**: 8a7253db-8874-496c-a40b-e538235f0a00
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate CLIP_RN50x4 on the ImageNet-Rendition test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50x4 was evaluated on the ImageNet-Rendition test set, with the Top-1 accuracy computed and s...

### R154: CLIP_RN50x4 has been evaluated on the ImageNet-Rendition tes...
- **Rubric ID**: 481feda0-9c06-4cad-a6e4-ea068e39b0ee
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: CLIP_RN50x4 has been evaluated on the ImageNet-Rendition test set, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50x4 was evaluated on the ImageNet-Rendition test set, with the Top-1 accuracy computed and s...

### R155: Code to evaluate CLIP_RN50x4 on the ImageNet-Adversarial tes...
- **Rubric ID**: b0244b68-af6a-47e2-a655-f866f9c06c76
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate CLIP_RN50x4 on the ImageNet-Adversarial test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50x4 was evaluated on the ImageNet-Adversarial test set, with the Top-1 accuracy computed and...

### R156: CLIP_RN50x4 has been evaluated on the ImageNet-Adversarial t...
- **Rubric ID**: 584c4ec8-84c0-499c-8758-08dddf0b7814
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: CLIP_RN50x4 has been evaluated on the ImageNet-Adversarial test set, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50x4 was evaluated on the ImageNet-Adversarial test set, with the Top-1 accuracy computed and...

### R157: Code to evaluate CLIP_RN50x4 on the ObjectNet test set has b...
- **Rubric ID**: 4760fce7-cbe2-46a3-8b14-6426980960c4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate CLIP_RN50x4 on the ObjectNet test set has been written, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50x4 was evaluated on the ObjectNet test set, with the Top-1 accuracy computed and saved.

### R158: CLIP_RN50x4 has been evaluated on the ObjectNet test set, co...
- **Rubric ID**: e7a29857-fe71-4534-84fe-9ad34bac6784
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: CLIP_RN50x4 has been evaluated on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: CLIP_RN50x4 was evaluated on the ObjectNet test set, with the Top-1 accuracy computed and saved.

### R159: The saved average LCA distance (using information content)s...
- **Rubric ID**: 04131141-f096-44f0-b42a-fda87727c29b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The saved average LCA distance (using information content)s show that both CLIP_RN50 and CLIP_RN50x4 achieve lower average LCA distance (using information content)s on the ImageNet test set compared to ResNet18 and ResNet50.
- **Parent context**: Table 1 has been reproduced.

### R160: The saved Top-1 accuracies show that both CLIP_RN50 and CLIP...
- **Rubric ID**: a2a038ae-e9fa-48e4-8608-5a249da3712c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The saved Top-1 accuracies show that both CLIP_RN50 and CLIP_RN50x4 achieve higher Top-1 accuracy scores on the ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial and ObjectNet test sets than both ResNet18 and ResNet50.
- **Parent context**: Table 1 has been reproduced.

### R161: Code to evaluate all 36 Vision Models in Appendix A on the I...
- **Rubric ID**: f4bac22d-0336-49c5-b7fc-214f57a8ebc5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 36 Vision Models in Appendix A on the ImageNet test set has been written, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) average LCA distance (using information c...

### R162: All 36 Vision Models in Appendix A have been evaluated on th...
- **Rubric ID**: d3467a48-d5ba-4efa-b810-711187f2caf7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models in Appendix A have been evaluated on the ImageNet test set, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) average LCA distance (using information c...

### R163: Code to evaluate all 39 Vision-Language Models in Appendix A...
- **Rubric ID**: c268b0f5-dc2f-48fa-9c6e-f2b2bdcc648c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 39 Vision-Language Models in Appendix A on the ImageNet test set has been written, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) average LCA distance (using info...

### R164: All 39 Vision-Language Models in Appendix A have been evalua...
- **Rubric ID**: 7a5f13ad-3591-4ef7-9868-9ac04334dc3d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models in Appendix A have been evaluated on the ImageNet test set, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) average LCA distance (using info...

### R165: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: 70c02545-7ff6-45ca-bae0-07d08c713e64
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-v2 test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-v2 Top-1 and Top-5 accuracy compute...

### R166: All 36 Vision Models have been evaluated on the ImageNet-v2...
- **Rubric ID**: b1f4ba87-2d12-46e4-b89a-413e2795726a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-v2 test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-v2 Top-1 and Top-5 accuracy compute...

### R167: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: 40d18a6d-df02-4a3a-b57d-ca4e3f51f095
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-Sketch test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Sketch Top-1 and Top-5 accuracy com...

### R168: All 36 Vision Models have been evaluated on the ImageNet-Ske...
- **Rubric ID**: a1037484-4eac-4f29-b1cd-5e1ef3bde266
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-Sketch test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Sketch Top-1 and Top-5 accuracy com...

### R169: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: a302153e-fad0-4b11-8637-b111fd508714
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-Rendition test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Rendition Top-1 and Top-5 accuracy ...

### R170: All 36 Vision Models have been evaluated on the ImageNet-Ren...
- **Rubric ID**: 8c026559-da9e-4ac3-8b91-3115200a334a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-Rendition test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Rendition Top-1 and Top-5 accuracy ...

### R171: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: 16c324bf-1902-4c4b-88e0-c46383136030
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-Adversarial test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Adversarial Top-1 and Top-5 accurac...

### R172: All 36 Vision Models have been evaluated on the ImageNet-Adv...
- **Rubric ID**: dd329228-116b-4680-a588-d5301a2af1e3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-Adversarial test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Adversarial Top-1 and Top-5 accurac...

### R173: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: 6a658efe-9b81-44f9-bf63-f022e230eaf0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ObjectNet test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ObjectNet Top-1 and Top-5 accuracy computed ...

### R174: All 36 Vision Models have been evaluated on the ObjectNet te...
- **Rubric ID**: 745c929a-97c2-4cf3-955f-c3274d2740d5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ObjectNet test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ObjectNet Top-1 and Top-5 accuracy computed ...

### R175: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: 13bea061-5e2d-4d92-9bd7-1adde9ae3cfb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-v2 test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-v2 Top-1 and Top-5 accurac...

### R176: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: db0e80fa-d4b0-412f-8c89-b725dc792dc7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-v2 test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-v2 Top-1 and Top-5 accurac...

### R177: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: 55c30739-d5cc-454e-abb9-74aea4a20f86
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-Sketch test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Sketch Top-1 and Top-5 acc...

### R178: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: 58326117-4404-42a2-b878-a926d3168df4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-Sketch test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Sketch Top-1 and Top-5 acc...

### R179: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: f60e5854-296c-4aba-8869-6b3540d80ebc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-Rendition test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Rendition Top-1 and Top-5 ...

### R180: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: e3821ab3-c09c-49a0-8232-0a439e202fc3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-Rendition test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Rendition Top-1 and Top-5 ...

### R181: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: b155c707-9b60-4a3a-bf17-71f632d723bf
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-Adversarial test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Adversarial Top-1 and Top-...

### R182: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: ca5db5f6-2ae6-42af-8ad3-e1cc51e75d26
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-Adversarial test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Adversarial Top-1 and Top-...

### R183: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: d3279666-448f-452b-9845-3e15bb95f9bf
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ObjectNet test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ObjectNet Top-1 and Top-5 accuracy ...

### R184: All 39 Vision-Language Models have been evaluated on the Obj...
- **Rubric ID**: 4aa4a151-efa7-4313-8d99-68c25d8d5b59
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ObjectNet test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ObjectNet Top-1 and Top-5 accuracy ...

### R185: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: 0332855c-1d8a-40e1-910c-9013ce00910e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution Top-1 and ImageNet-v2 out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the ImageNet-v2 in-distribution Top-1 and out-of-dis...

### R186: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 4f76ff6e-e88c-4f6d-afa9-c887b210759f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution Top-1 and ImageNet-v2 out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the ImageNet-v2 in-distribution Top-1 and out-of-dis...

### R187: The $R^2$ value between the in-distribution Top-1 and ImageN...
- **Rubric ID**: 2923ecc4-84d0-4265-91dc-8fecce97262b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution Top-1 and ImageNet-v2 out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the ImageNet-v2 in-distribution Top-1 and out-of-dis...

### R188: The Pearson correlation between the in-distribution Top-1 an...
- **Rubric ID**: 7b302466-1d59-4f13-a982-97c0fdd37bae
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution Top-1 and ImageNet-v2 out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the ImageNet-v2 in-distribution Top-1 and out-of-dis...

### R189: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: a747d947-34d7-4971-b8d2-0351a6db0eab
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution average LCA and ImageNet-v2 out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R190: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 3669f3a2-fcdd-483e-b1a0-c80b1d86623f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution average LCA and ImageNet-v2 out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R191: The $R^2$ value between the in-distribution average LCA and...
- **Rubric ID**: 3aacf358-8d91-47e0-91c2-154e1d582eb2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution average LCA and ImageNet-v2 out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R192: The Pearson correlation between the in-distribution average...
- **Rubric ID**: b1847dea-8a98-4b66-9d55-0507ff37ca39
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution average LCA and ImageNet-v2 out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R193: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: 5e327498-3055-40bd-872c-c3aaf70cccee
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution Top-1 and ImageNet-v2 out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-v2 out-of-dis...

### R194: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 86287685-0eaa-4fe4-bfb7-f6b9a182ae61
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution Top-1 and ImageNet-v2 out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-v2 out-of-dis...

### R195: The $R^2$ value between the in-distribution Top-1 and ImageN...
- **Rubric ID**: 2ad910e9-f2d7-43a6-b663-744915bcad14
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution Top-1 and ImageNet-v2 out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-v2 out-of-dis...

### R196: The Pearson correlation between the in-distribution Top-1 an...
- **Rubric ID**: 67e08fbb-16a1-40f6-9168-dad122521f71
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution Top-1 and ImageNet-v2 out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-v2 out-of-dis...

### R197: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: 71a4f61e-5f30-4ac2-a2a4-339c40d34fe8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution average LCA and ImageNet-v2 out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R198: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: f4aebd24-018f-4485-82bb-402124ee23b9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution average LCA and ImageNet-v2 out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R199: The $R^2$ value between the in-distribution average LCA and...
- **Rubric ID**: 57784005-0c7d-4307-b9c4-a0ff86aa71a0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution average LCA and ImageNet-v2 out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R200: The Pearson correlation between the in-distribution average...
- **Rubric ID**: 4f8bcb56-9848-40bd-bd88-f28791b83277
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution average LCA and ImageNet-v2 out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R201: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: d00eb606-a093-4f43-b5df-9cbcf034ba89
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution Top-1 and ImageNet-Sketch out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Sketch out-of...

### R202: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: e950c48a-6164-4ada-ac64-710f4b175445
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution Top-1 and ImageNet-Sketch out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Sketch out-of...

### R203: The $R^2$ value between the in-distribution Top-1 and ImageN...
- **Rubric ID**: 3b5b135f-5da9-4d49-9909-3cc59a4aafc2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution Top-1 and ImageNet-Sketch out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Sketch out-of...

### R204: The Pearson correlation between the in-distribution Top-1 an...
- **Rubric ID**: 22e488e3-3ebe-4291-9de1-58101f4b0f55
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution Top-1 and ImageNet-Sketch out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Sketch out-of...

### R205: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: 282f58bf-4382-4b98-8804-14b81d5a4fd6
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution average LCA and ImageNet-Sketch out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R206: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 440494a4-cf0a-4698-8942-5ce397b36266
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution average LCA and ImageNet-Sketch out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R207: The $R^2$ value between the ImageNet-Sketch average LCA and...
- **Rubric ID**: 83b2d915-a067-4bc0-bf38-e83c2d81d049
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the ImageNet-Sketch average LCA and ImageNet-Sketch out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R208: The Pearson correlation between the in-distribution average...
- **Rubric ID**: b9151019-d7c1-44ac-a134-d0e2c0430964
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution average LCA and ImageNet-Sketch out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R209: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: 4e0c7434-0e5f-4c03-afad-dc28d95901da
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution Top-1 and ImageNet-Sketch out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Sketch out-of...

### R210: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 5dc44cc1-7860-4e15-bb9d-dc500c2a93fc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution Top-1 and ImageNet-Sketch out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Sketch out-of...

### R211: The $R^2$ value between the in-distribution Top-1 and ImageN...
- **Rubric ID**: 73c88ca9-454a-4337-a9e3-edfcf40d7cb5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution Top-1 and ImageNet-Sketch out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Sketch out-of...

### R212: The Pearson correlation between the in-distribution Top-1 an...
- **Rubric ID**: c7bf9fb2-7f16-42c4-92e8-dc931e8fe241
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution Top-1 and ImageNet-Sketch out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Sketch out-of...

### R213: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: b21d8ce1-8bcd-4cfb-988c-9f3ba5565553
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution average LCA and ImageNet-Sketch out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R214: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 9b1eedfd-0d0f-4daa-a46a-2dc249a7d149
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution average LCA and ImageNet-Sketch out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R215: The $R^2$ value between the in-distribution average LCA and...
- **Rubric ID**: 7ce6f02b-36a3-4719-81e1-e4faf7f4b0d4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution average LCA and ImageNet-Sketch out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R216: The Pearson correlation between the in-distribution average...
- **Rubric ID**: d023dc98-4471-4618-86f6-2aad233f3cd7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution average LCA and ImageNet-Sketch out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R217: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: 1b72e3de-4b8a-4291-97fc-4f345e891d63
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution Top-1 and ImageNet-Rendition out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Rendition out...

### R218: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 9a213c9b-00fd-4e7c-b3b8-381b0648819b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution Top-1 and ImageNet-Rendition out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Rendition out...

### R219: The $R^2$ value between the in-distribution Top-1 and ImageN...
- **Rubric ID**: 95c0937c-a07b-4f6d-b20d-a45b5afaf50d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution Top-1 and ImageNet-Rendition out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Rendition out...

### R220: The Pearson correlation between the in-distribution Top-1 an...
- **Rubric ID**: 847b49e3-2f28-4a51-9e21-fdbec2c2023b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution Top-1 and ImageNet-Rendition out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Rendition out...

### R221: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: 7676b570-1cfb-48b3-8761-56bb100f358f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution average LCA and ImageNet-Rendition out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R222: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 07923b7f-000a-4825-b5e0-3637b1c90fd5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution average LCA and ImageNet-Rendition out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R223: The $R^2$ value between the in-distribution average LCA and...
- **Rubric ID**: 07a69338-6552-426a-9f9a-9c698d13da5c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution average LCA and ImageNet-Rendition out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R224: The Pearson correlation between the in-distribution average...
- **Rubric ID**: ba161222-be80-4fbc-b534-1c99c58f61cb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution average LCA and ImageNet-Rendition out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R225: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: ee76060d-d855-4c2f-a4a6-088f7928ac27
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution Top-1 and ImageNet-Rendition out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Rendition out...

### R226: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 31d405c0-0e4d-4409-8fb8-def418dcee7d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution Top-1 and ImageNet-Rendition out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Rendition out...

### R227: The $R^2$ value between the in-distribution Top-1 and ImageN...
- **Rubric ID**: 0ff719d4-eeb2-4749-bedb-0ad2154c4029
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution Top-1 and ImageNet-Rendition out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Rendition out...

### R228: The Pearson correlation between the in-distribution Top-1 an...
- **Rubric ID**: bb603e8d-a98c-45fc-b606-cc02074ea1b1
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution Top-1 and ImageNet-Rendition out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Rendition out...

### R229: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: ba5d3333-d4aa-4e95-b72b-65769bb23b90
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution average LCA and ImageNet-Rendition out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R230: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 4b69f61a-d860-4afe-a8fe-7e0ec4c1562f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution average LCA and ImageNet-Rendition out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R231: The $R^2$ value between the in-distribution average LCA and...
- **Rubric ID**: 24a02286-bb9a-42c6-88a8-030c9d62b359
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution average LCA and ImageNet-Rendition out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R232: The Pearson correlation between the in-distribution average...
- **Rubric ID**: ee7c00a5-3473-4cb8-87b8-0cf89de8cf0d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution average LCA and ImageNet-Rendition out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R233: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: 3dbb5283-3780-4326-8a24-4c89e5daffa8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution Top-1 and ImageNet-Adversarial out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Adversarial o...

### R234: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: cb4c10fb-92c3-4915-8f36-40ebbb32004b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution Top-1 and ImageNet-Adversarial out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Adversarial o...

### R235: The $R^2$ value between the in-distribution Top-1 and ImageN...
- **Rubric ID**: bb05661c-0344-4471-a5a2-ac7e5738f038
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution Top-1 and ImageNet-Adversarial out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Adversarial o...

### R236: The Pearson correlation between the in-distribution Top-1 an...
- **Rubric ID**: 3c99273e-6d58-4804-99d4-f9e33cd3ed4d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution Top-1 and ImageNet-Adversarial out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Adversarial o...

### R237: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: 49b3bf31-8204-4374-b512-0f76a7325dea
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution average LCA and ImageNet-Adversarial out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R238: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: e7aa5124-1c8f-4bf0-b0f1-9764ba844178
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution average LCA and ImageNet-Adversarial out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R239: The $R^2$ value between the in-distribution average LCA and...
- **Rubric ID**: 8c9b559b-7435-486f-b803-b2261d3d6d45
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution average LCA and ImageNet-Adversarial out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R240: The Pearson correlation between the in-distribution average...
- **Rubric ID**: fb9098cd-5f3f-41ea-b818-774db9803806
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution average LCA and ImageNet-Adversarial out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R241: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: ad9dd112-5378-4cd1-be88-78bd2b6bf588
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution Top-1 and ImageNet-Adversarial out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Adversarial o...

### R242: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 6a89546e-d9fe-48c2-b90e-4fd6ca3b35e8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution Top-1 and ImageNet-Adversarial out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Adversarial o...

### R243: The $R^2$ value between the in-distribution Top-1 and ImageN...
- **Rubric ID**: 03fbe707-cf73-4ff7-82f8-64c168aad180
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution Top-1 and ImageNet-Adversarial out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Adversarial o...

### R244: The Pearson correlation between the in-distribution Top-1 an...
- **Rubric ID**: 8bcb208f-9922-45b4-a819-8f79987bc172
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution Top-1 and ImageNet-Adversarial out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ImageNet-Adversarial o...

### R245: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: fd0b8d4a-0fd1-421d-9a94-75da9673847b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution average LCA and ImageNet-Adversarial out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R246: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 143d4e7a-676c-4ffc-890f-2f3f2f208a5a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution average LCA and ImageNet-Adversarial out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R247: The $R^2$ value between the in-distribution average LCA and...
- **Rubric ID**: 300c67ad-053b-4caa-90dd-2a33d91d05c8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution average LCA and ImageNet-Adversarial out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R248: The Pearson correlation between the in-distribution average...
- **Rubric ID**: 550173dd-cb22-4df0-9078-ef769a069190
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution average LCA and ImageNet-Adversarial out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R249: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: b24885db-5e8d-4558-8ca8-e215a4dfba55
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution Top-1 and ObjectNet out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ObjectNet out-of-distr...

### R250: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 260cca63-4cdb-473f-98bd-386faad3c455
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution Top-1 and ObjectNet out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ObjectNet out-of-distr...

### R251: The $R^2$ value between the in-distribution Top-1 and Object...
- **Rubric ID**: 18e743e8-e443-4542-bc26-a126c440b844
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution Top-1 and ObjectNet out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ObjectNet out-of-distr...

### R252: The Pearson correlation between the in-distribution Top-1 an...
- **Rubric ID**: fe5195a8-51df-4816-86c7-90130023733e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution Top-1 and ObjectNet out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ObjectNet out-of-distr...

### R253: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: 13696a22-3f32-48ab-b30e-c85c7e5ed84b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution average LCA and ObjectNet out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R254: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 65ba607f-0902-45d7-bcce-df6d2cf62872
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution average LCA and ObjectNet out-of-distribution Top-1 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R255: The $R^2$ value between the in-distribution average LCA and...
- **Rubric ID**: 0d8d4993-f2f0-4165-81f9-cd983b46ec59
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution average LCA and ObjectNet out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R256: The Pearson correlation between the in-distribution average...
- **Rubric ID**: 9f84cfcb-7a54-40bc-af96-34a224d35557
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution average LCA and ObjectNet out-of-distribution Top-1 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R257: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: d437e229-aafe-4326-9322-24d44e0b3e55
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution Top-1 and ObjectNet out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ObjectNet out-of-distr...

### R258: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 72c9ba79-598d-4400-ab4e-3aadd5ff2056
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution Top-1 and ObjectNet out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ObjectNet out-of-distr...

### R259: The $R^2$ value between the in-distribution Top-1 and Object...
- **Rubric ID**: 5f822a88-fc79-4ab2-a01e-9c7a3c93fd9c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution Top-1 and ObjectNet out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ObjectNet out-of-distr...

### R260: The Pearson correlation between the in-distribution Top-1 an...
- **Rubric ID**: f6e85aba-e26c-4740-bd57-ac067ab2c699
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution Top-1 and ObjectNet out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution Top-1 and ObjectNet out-of-distr...

### R261: Code has been written to compute and save the $R^2$ value be...
- **Rubric ID**: 36ac7f1c-8769-45bd-b94e-c59b53d27e1c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the $R^2$ value between the in-distribution average LCA and ObjectNet out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R262: Code has been written to compute and save the Pearson correl...
- **Rubric ID**: 81b8cf17-8529-4198-b647-62aa944e300a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute and save the Pearson correlation between the in-distribution average LCA and ObjectNet out-of-distribution Top-5 test set accuracies for all 75 models.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R263: The $R^2$ value between the in-distribution average LCA and...
- **Rubric ID**: 16f99a17-0128-45b0-ad0f-bfe97326afcf
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The $R^2$ value between the in-distribution average LCA and ObjectNet out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R264: The Pearson correlation between the in-distribution average...
- **Rubric ID**: 70dae064-432b-423d-a95a-a910836d0bba
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the in-distribution average LCA and ObjectNet out-of-distribution Top-5 test set accuracies for all 75 models has been computed and saved.
- **Parent context**: The $R^2$ value and Pearson correlation between the in-distribution average LCA distance (using info...

### R265: The saved results show that the Pearson correlation between...
- **Rubric ID**: 4db03667-be04-4c0b-9853-b1ce86d67123
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The saved results show that the Pearson correlation between the in-distribution average LCA distance (using information content) and out-of-distribution Top-1 test set accuracy is higher than the Pearson correlation between the in-distribution average Top-1 and out-of-distribution Top-1 test set accuracies for ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial and ObjectNet, but not ImageNet-v2.
- **Parent context**: Table 2 has been reproduced.

### R266: The saved results show that the Pearson correlation between...
- **Rubric ID**: 07b41f38-31e8-4070-856a-c6a5bbf549d2
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The saved results show that the Pearson correlation between the in-distribution average LCA distance (using information content) and out-of-distribution Top-5 test set accuracy is higher than the Pearson correlation between the in-distribution average Top-1 and out-of-distribution Top-5 test set accuracies for ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial and ObjectNet, but not ImageNet-v2.
- **Parent context**: Table 2 has been reproduced.

### R267: Code to evaluate all 36 Vision Models in Appendix A on the I...
- **Rubric ID**: 93bebe9c-0323-4d23-b73a-5c91ba1a56e8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 36 Vision Models in Appendix A on the ImageNet test set has been written, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) average LCA distance (using information c...

### R268: All 36 Vision Models in Appendix A have been evaluated on th...
- **Rubric ID**: 9d75ccf9-4cc1-44c4-ae1a-ca0520d65d2c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models in Appendix A have been evaluated on the ImageNet test set, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) average LCA distance (using information c...

### R269: Code to evaluate all 39 Vision-Language Models in Appendix A...
- **Rubric ID**: ac4a60ea-7cfa-4ab5-9185-aa776e3177ba
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 39 Vision-Language Models in Appendix A on the ImageNet test set has been written, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) average LCA distance (using info...

### R270: All 39 Vision-Language Models in Appendix A have been evalua...
- **Rubric ID**: 7ba8b97b-4753-490e-92c7-d08ac6f2a5d1
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models in Appendix A have been evaluated on the ImageNet test set, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) average LCA distance (using info...

### R271: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: eb5a8b52-a4fb-4c0c-87cf-953e8ea68bae
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-v2 test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-v2 Top-1 accuracy computed and save...

### R272: All 36 Vision Models have been evaluated on the ImageNet-v2...
- **Rubric ID**: a9f568ad-24b1-4420-ab64-bf7244c7930e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-v2 test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-v2 Top-1 accuracy computed and save...

### R273: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: 5e8197b5-3f54-4a6f-897f-979302e0a00f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-Sketch test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Sketch Top-1 accuracy computed and ...

### R274: All 36 Vision Models have been evaluated on the ImageNet-Ske...
- **Rubric ID**: 9be85329-160a-4628-b800-b7d1502ff8a0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-Sketch test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Sketch Top-1 accuracy computed and ...

### R275: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: b20798f9-66aa-4f01-956a-004ff0e1a316
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-Rendition test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Rendition Top-1 accuracy computed a...

### R276: All 36 Vision Models have been evaluated on the ImageNet-Ren...
- **Rubric ID**: fa388189-b1b5-423a-9f5a-0b190bc0ee0c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-Rendition test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Rendition Top-1 accuracy computed a...

### R277: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: 33a19c4d-fb59-4d55-9b9b-377046940f21
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-Adversarial test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Adversarial Top-1 accuracy computed...

### R278: All 36 Vision Models have been evaluated on the ImageNet-Adv...
- **Rubric ID**: 19850e16-a6fe-4479-9eae-d2bee59766cc
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-Adversarial test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Adversarial Top-1 accuracy computed...

### R279: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: be7734a2-a2ef-4387-9416-50065311d0f7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ObjectNet Top-1 accuracy computed and saved.

### R280: All 36 Vision Models have been evaluated on the ObjectNet te...
- **Rubric ID**: 3c2990b8-1cff-4c91-b9a2-9937a52372ed
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ObjectNet Top-1 accuracy computed and saved.

### R281: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: 22e6afc0-2bea-4c90-8bf9-8a7e46796206
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-v2 test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-v2 Top-1 accuracy computed...

### R282: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: 5d89c239-df5b-4b96-8694-ad79cc569204
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-v2 test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-v2 Top-1 accuracy computed...

### R283: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: 2e961d54-83ef-4437-bf91-49dda015cc10
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-Sketch test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Sketch Top-1 accuracy comp...

### R284: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: b48abe19-07a5-4530-8d98-0a5ea587c70b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-Sketch test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Sketch Top-1 accuracy comp...

### R285: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: 30380729-007a-4d86-95e0-17776b33c7a1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-Rendition test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Rendition Top-1 accuracy c...

### R286: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: ea2efe7c-912e-476c-941c-a084df46543e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-Rendition test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Rendition Top-1 accuracy c...

### R287: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: 51d82d14-8b8b-4280-a3f8-062ebb21bb4d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-Adversarial test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Adversarial Top-1 accuracy...

### R288: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: 7eab65f5-d4d7-4d54-8da1-ba15b80401ec
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-Adversarial test set, computing and saving both the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Adversarial Top-1 accuracy...

### R289: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: 353c344e-a629-4698-b892-1c023ec9825b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ObjectNet Top-1 accuracy computed a...

### R290: All 39 Vision-Language Models have been evaluated on the Obj...
- **Rubric ID**: 118d6f66-5077-4096-838f-09febb1eaf37
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ObjectNet Top-1 accuracy computed a...

### R291: Code has been written to compute the average confidence $AC...
- **Rubric ID**: ae1b0053-1813-485f-a3b8-1f0fc4948d3a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the average confidence $AC = \frac{1}{N} \sum_{i=1}^N \max _j P\left(y_j \mid x_i\right)$ where $N$ is the number of samples, $P\left(y_j \mid x_i\right)$ is the predicted probability for class $j$ given input $x_i$, and $\max _j P\left(y_j \mid x_i\right)$ selects the highest probability for each sample.
- **Parent context**: All 75 models have their in-distribution (ImageNet) average confidence computed and saved.

### R292: Code to evaluate all 36 Vision Models in Appendix A on the I...
- **Rubric ID**: 9d13df03-190e-4ad6-9fef-1cd693feb1ae
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 36 Vision Models in Appendix A on the ImageNet test set has been written, computing and saving the average confidence for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) average confidence on the test set comput...

### R293: All 36 Vision Models in Appendix A have been evaluated on th...
- **Rubric ID**: bf1d880f-74d2-41b5-8ffe-d9351de731fc
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models in Appendix A have been evaluated on the ImageNet test set, computing and saving the average confidence for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) average confidence on the test set comput...

### R294: Code to evaluate all 39 Vision-Language Models in Appendix A...
- **Rubric ID**: 209edebd-fd66-4e67-8e2f-3b3a9530ef0f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 39 Vision-Language Models in Appendix A on the ImageNet test set has been written, computing and saving the average confidence for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) average confidence on the test s...

### R295: All 39 Vision-Language Models in Appendix A have been evalua...
- **Rubric ID**: 1841ce5a-760f-4ac8-ba4f-7ae5ea2ae433
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models in Appendix A have been evaluated on the ImageNet test set, computing and saving the average confidence for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) average confidence on the test s...

### R296: Code has been written to compute the Aline-D, as described i...
- **Rubric ID**: 06bc4d7e-ba54-43ed-8999-e31d7f7057a5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Aline-D, as described in the addendum.
- **Parent context**: All 75 models have their in-distribution (ImageNet) Aline-D computed and saved.

### R297: Code to evaluate all 36 Vision Models in Appendix A on the I...
- **Rubric ID**: 4eb27873-495b-4d4c-a4d7-b90ad281523f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 36 Vision Models in Appendix A on the ImageNet test set has been written, computing and saving the Aline-D for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) Aline-D on the test set computed and save...

### R298: All 36 Vision Models in Appendix A have been evaluated on th...
- **Rubric ID**: 5b5c31b4-f845-421b-b501-2eabd1efaa17
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models in Appendix A have been evaluated on the ImageNet test set, computing and saving the Aline-D for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) Aline-D on the test set computed and save...

### R299: Code to evaluate all 39 Vision-Language Models in Appendix A...
- **Rubric ID**: a4388551-d829-477a-817c-56d1fd950c32
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 39 Vision-Language Models in Appendix A on the ImageNet test set has been written, computing and saving the Aline-D for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) Aline-D on the test set computed...

### R300: All 39 Vision-Language Models in Appendix A have been evalua...
- **Rubric ID**: 7ed2677c-6c52-4ab9-a245-07d5f2077428
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models in Appendix A have been evaluated on the ImageNet test set, computing and saving the Aline-D for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) Aline-D on the test set computed...

### R301: Code has been written to compute the Aline-S, as described i...
- **Rubric ID**: 6535ab8d-82cb-4bfd-a8c9-f6140d1d23b2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute the Aline-S, as described in the addendum.
- **Parent context**: All 75 models have their in-distribution (ImageNet) Aline-S computed and saved.

### R302: Code to evaluate all 36 Vision Models in Appendix A on the I...
- **Rubric ID**: bf0ba4b3-c50f-4e8c-a7f3-bab43991f23e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 36 Vision Models in Appendix A on the ImageNet test set has been written, computing and saving the Aline-S for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) Aline-S on the test set computed and save...

### R303: All 36 Vision Models in Appendix A have been evaluated on th...
- **Rubric ID**: ed4a7d32-eee1-42d5-9bf5-b59ed09e46f3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models in Appendix A have been evaluated on the ImageNet test set, computing and saving the Aline-S for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) Aline-S on the test set computed and save...

### R304: Code to evaluate all 39 Vision-Language Models in Appendix A...
- **Rubric ID**: 28b9ac77-dcf5-4ee1-911f-37708cc5e40b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 39 Vision-Language Models in Appendix A on the ImageNet test set has been written, computing and saving the Aline-S for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) Aline-S on the test set computed...

### R305: All 39 Vision-Language Models in Appendix A have been evalua...
- **Rubric ID**: bece351b-0bde-4b4e-b1ac-504ebd11f41b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models in Appendix A have been evaluated on the ImageNet test set, computing and saving the Aline-S for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) Aline-S on the test set computed...

### R306: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: b16a6afc-5161-44a5-bb0d-de71ebed4b9f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R307: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: 483b6a2f-3e81-4504-8ae5-46a7dee44012
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R308: The mean absolute error has been computed and saved for the...
- **Rubric ID**: ac7972a0-e584-4c33-9a5b-509692d4abc8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R309: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: 89d79f9c-0b61-4534-a3ec-871fcf7967bd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R310: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: cdb7675d-e01e-404d-bc7a-1764b19ea5ac
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R311: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: 9753a94c-8bc7-49c6-801f-608c56b37d4c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R312: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 19d43582-dfc2-4a11-8263-d1af7f8aa682
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R313: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: 9a0d92ec-47a0-49f2-9e1a-48bc897b7efb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R314: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: 5e25601d-c540-4cfc-9355-9c0bc97f7959
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R315: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: 553b6972-7554-4abd-b6c1-ee5758df07c0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R316: The mean absolute error has been computed and saved for the...
- **Rubric ID**: c4a37593-2dbc-4a4d-9123-d893d38fc643
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R317: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: 2f107109-29c4-4768-8526-b7fdb29be4b0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R318: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: 89939b87-5a2f-439d-9d95-247a9ec0d7c1
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R319: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: e4e6b9b0-f725-4500-ba21-62acc440277a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R320: The mean absolute error has been computed and saved for the...
- **Rubric ID**: ac9c6a5f-8988-4eed-ba50-ea57972652d3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R321: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: e72f01e4-af6a-477e-8d91-ea9c24dd4318
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R322: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: ca2ac54b-8228-4e37-8ea3-76a404ffb498
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R323: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 8558a71c-8c7f-4be7-add6-8e2c04485a74
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R324: Code to compute a line of best fit between the average confi...
- **Rubric ID**: 1b12d6ca-a556-49a0-9acb-c3a3d59aa762
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R325: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: 220726d7-10c8-4df7-81a3-52ef56fd9249
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R326: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 07338db4-6359-4425-8627-b6d2a46b9f2e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R327: Code to compute a line of best fit between the average confi...
- **Rubric ID**: eb805cee-ac9e-45cb-8055-9a5458f5fa72
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R328: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: 54a1374e-2f5e-4b77-aa70-ed782e637e82
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R329: The mean absolute error has been computed and saved for the...
- **Rubric ID**: b45866d0-6bd7-4523-8756-3c8d518b58ef
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R330: Code to compute a line of best fit between the average confi...
- **Rubric ID**: 823cc3f0-e360-4ce1-98ec-7f7f81c7fc10
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R331: A line of best fit has been computed between the average con...
- **Rubric ID**: 9310569e-d06a-4eba-9dc8-172cdb07b040
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R332: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: 6329ce6f-fe76-47c3-968d-86ed261babcd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R333: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 839e3757-6e1c-45db-a63e-fc3031eb39e5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R334: Code to compute a line of best fit between the average confi...
- **Rubric ID**: 5e7110ab-16bb-4203-97bc-8d36b894ba8e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R335: A line of best fit has been computed between the average con...
- **Rubric ID**: 781254b0-a22c-4e37-9e94-9c2017bd4239
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R336: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: 3b981ee9-ee07-4608-a09a-d40a1e889bd8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R337: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 0ca220fa-2fe6-47fc-b81a-a820a5d6d452
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R338: Code to compute a line of best fit between the average confi...
- **Rubric ID**: 258dd0fb-f3da-4de0-b50b-0c2a8eca482b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R339: A line of best fit has been computed between the average con...
- **Rubric ID**: 5120723d-419b-44fc-8867-ccb2bcbb5c4a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R340: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: e5289fbf-f792-4269-8d50-ce82284e7efe
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R341: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 377b7ce7-3dcd-4138-8726-b5e2d108e2b9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R342: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: 2fdb2674-10df-41de-b41c-b7436a5dd43c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R343: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: a605126b-e2fc-46a8-a22f-a44a0249712f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R344: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: afbcace8-ff6a-4db7-842b-4590ab73e6c0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R345: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 3ad9a26b-b494-4d02-82b4-a73cba32e1a6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R346: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: 34081763-d14c-41c3-adc5-69d6e0b4cc86
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R347: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: a06e0923-9bd8-4aca-8d26-b2268a40b718
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R348: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: 5d105cc7-844d-42d9-a50e-0c14e659e147
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R349: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 20c16021-83b0-4805-80e4-d094fdaaf22c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R350: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: d89103f1-6a6e-4e5b-8396-f3918bd5c155
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R351: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: 2fca8305-ac20-41c7-a0f8-3ff60a8d9e51
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R352: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: 5058f446-c98e-43ee-86cf-a845ea1d8dce
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R353: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 77f92272-aaf6-4fab-8314-54af8e24149c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R354: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: 24d04008-f3d5-483c-8f62-44c8b3c2b7c1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R355: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: 4a61c7c7-4602-408c-aee7-78ab898b037e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R356: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 6c6d3906-64ef-4323-ac6a-140513d82e9f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R357: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: a6cdc1a3-b554-4550-9d61-1c940b25b01a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R358: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: 373c0ee5-29fe-44c2-913d-5aba9bd7fbb7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R359: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: a36852a6-8e52-4fcc-adaf-cdb1351ef42e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R360: The mean absolute error has been computed and saved for the...
- **Rubric ID**: b3bc832d-13e1-48f2-a3ff-0fa44278abb7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R361: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: e6c8e561-b885-4b32-9d1b-d6bcf3876257
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R362: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: 8fa35782-9ee8-43be-9385-45d4f4f917ff
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R363: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: f25ffbe7-7b6e-4bf1-9873-22a3baeac6fc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R364: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 21db3d0c-8d8b-4ef4-8dfc-947fe0e47085
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R365: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: b7097b9c-c34f-41e5-a081-446a0d460f7d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R366: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: 8f4263fa-0a54-4a7d-b752-074b72c883ab
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R367: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: 31922376-ffb3-422f-a792-e494126065f3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R368: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 0c84cffd-56ba-4cbb-97bb-8ba8c3fc5df4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R369: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: b5262219-8f1a-4d43-a542-2e01bd18600d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R370: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: a4a712c8-4ac7-49d4-a7f8-3c81845d0a03
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R371: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: b54ce732-c95b-428a-9b1b-100c8adfba6b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R372: The mean absolute error has been computed and saved for the...
- **Rubric ID**: c4676214-9eff-4c31-9d90-f4982a7bbb5a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R373: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: d213a9bb-f33d-413d-ace1-cac900ee49bd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R374: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: 4c3e8582-595c-45fa-b502-f9c92861e611
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R375: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: c84af08d-7d03-4457-bd9f-fb675e7336df
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R376: The mean absolute error has been computed and saved for the...
- **Rubric ID**: b33b298a-f4cc-4218-b597-48f81ee79943
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R377: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: ed20e611-8aac-47db-b996-7668d0c00be0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R378: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: d2d49485-47d3-4dda-ae3b-ce553acc65b1
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R379: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: f9922947-2052-408f-bc1b-c47edad12830
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R380: The mean absolute error has been computed and saved for the...
- **Rubric ID**: c5ada85f-1980-4187-a36b-0e31736277f8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) Aline-S scores on the test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R381: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: 799e8e0b-a75a-4a8e-b7cb-272f610b60a5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R382: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: 5a33082f-20d6-429e-8f46-aa72e4744a3a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R383: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: d07938f7-8284-4eb2-9d54-42444372fd27
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R384: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 9891533b-9d09-4120-95d4-032f05a0777d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R385: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: 86ce67b1-05a2-4fa5-aa97-25fd36bb33d7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R386: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: 7e287ec2-e698-450d-8ce5-584677b8d7cc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R387: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 85322084-e513-4d42-a6e4-ebcad665131e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R388: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: 11918fc5-b833-4ed7-9bcd-fd5e9080d181
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R389: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: 4a18db61-3c4b-4bdf-b0c3-e833ae8ded16
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R390: The mean absolute error has been computed and saved for the...
- **Rubric ID**: d8acae09-5640-4898-af72-f2e5e0776f11
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R391: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: d311fe91-1fbb-480a-b307-c8e662ffb933
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R392: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: e2897fb8-c5ba-42df-8126-da845d454fec
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R393: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: a397cd66-3a01-46d2-9210-200daf442750
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R394: The mean absolute error has been computed and saved for the...
- **Rubric ID**: d0a3178f-45ee-4a9e-9778-891f5569743a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R395: Code to compute a line of best fit between the in-distributi...
- **Rubric ID**: 3a3c7dd5-1a7d-4778-9e0f-19639794df0f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute a line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R396: Code to compute and save the mean absolute error for the lin...
- **Rubric ID**: d1c37b75-852c-47d3-8d3c-924f6dd8f332
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean absolute error for the line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models has been written.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R397: The mean absolute error has been computed and saved for the...
- **Rubric ID**: 701223e9-3bdd-4954-b552-3b2ea4a6bfcf
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean absolute error has been computed and saved for the line of best fit between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R398: Code to evaluate all 36 Vision Models in Appendix A on the I...
- **Rubric ID**: 47eca1cb-f9e4-45ee-be00-b27b095fa780
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 36 Vision Models in Appendix A on the ImageNet test set has been written, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) average LCA distance (using information c...

### R399: All 36 Vision Models in Appendix A have been evaluated on th...
- **Rubric ID**: 927dfd2c-243f-4df3-b1ab-a2c56db05f0a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models in Appendix A have been evaluated on the ImageNet test set, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) average LCA distance (using information c...

### R400: Code to evaluate all 39 Vision-Language Models in Appendix A...
- **Rubric ID**: 8fd14ac0-2ded-4cf6-bdc2-3c06d491ecde
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 39 Vision-Language Models in Appendix A on the ImageNet test set has been written, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) average LCA distance (using info...

### R401: All 39 Vision-Language Models in Appendix A have been evalua...
- **Rubric ID**: 2a8d0f0c-9432-4701-9664-9a3c688ef025
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models in Appendix A have been evaluated on the ImageNet test set, computing and saving both the average LCA distance (using information content) and Top-1 accuracy for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) average LCA distance (using info...

### R402: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: cee3b961-fa71-4279-b396-f5abedd44c08
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-v2 test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-v2 Top-1 and Top-5 accuracy compute...

### R403: All 36 Vision Models have been evaluated on the ImageNet-v2...
- **Rubric ID**: 5349908f-47e3-40fc-b050-e20b8f01b1b9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-v2 test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-v2 Top-1 and Top-5 accuracy compute...

### R404: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: 5b37ef1c-6a35-4f95-a35c-69470b9c9253
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-Sketch test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Sketch Top-1 and Top-5 accuracy com...

### R405: All 36 Vision Models have been evaluated on the ImageNet-Ske...
- **Rubric ID**: f5fb76a4-7046-41bc-8e2d-6653a1f2573a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-Sketch test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Sketch Top-1 and Top-5 accuracy com...

### R406: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: 69e565da-765a-456e-aaef-84b980d7eb0b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-Rendition test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Rendition Top-1 and Top-5 accuracy ...

### R407: All 36 Vision Models have been evaluated on the ImageNet-Ren...
- **Rubric ID**: 26a3fb49-dbd6-4da9-a743-99b9d1c9ca7f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-Rendition test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Rendition Top-1 and Top-5 accuracy ...

### R408: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: 4832ef27-3976-43aa-898e-996e80986ab5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-Adversarial test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Adversarial Top-1 and Top-5 accurac...

### R409: All 36 Vision Models have been evaluated on the ImageNet-Adv...
- **Rubric ID**: 01fb30a2-20b1-416d-bf8e-a302c4a44d59
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-Adversarial test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Adversarial Top-1 and Top-5 accurac...

### R410: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: 4e90f87e-8903-43ba-b030-36bb062bcf9f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ObjectNet test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ObjectNet Top-1 and Top-5 accuracy computed ...

### R411: All 36 Vision Models have been evaluated on the ObjectNet te...
- **Rubric ID**: 14449ac6-6391-494f-8b26-df93e8061030
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ObjectNet test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ObjectNet Top-1 and Top-5 accuracy computed ...

### R412: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: 8e375a58-3d3b-4700-8217-e89a58953c8f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-v2 test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-v2 Top-1 and Top-5 accurac...

### R413: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: 1008e9a9-93bf-48a8-a5be-b1a72df64aad
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-v2 test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-v2 Top-1 and Top-5 accurac...

### R414: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: f17a9621-0d67-495f-aee5-78bb423ef85f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-Sketch test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Sketch Top-1 and Top-5 acc...

### R415: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: 04ad1d76-2a04-473e-a112-a5511ccd32bf
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-Sketch test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Sketch Top-1 and Top-5 acc...

### R416: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: 31df176f-361e-42ae-9a20-0e499944ed1a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-Rendition test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Rendition Top-1 and Top-5 ...

### R417: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: a7e0613c-f6e2-49e0-8d78-c34ab8376c8b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-Rendition test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Rendition Top-1 and Top-5 ...

### R418: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: d16ac027-b101-4712-813b-04006cd4f0fd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-Adversarial test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Adversarial Top-1 and Top-...

### R419: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: 7f8a8c1e-16f8-4d5d-a26e-23bc13b802fc
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-Adversarial test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Adversarial Top-1 and Top-...

### R420: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: d75f84e8-20ca-4ec1-93e6-31f8312ce6f9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ObjectNet test set, computing and saving both Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ObjectNet Top-1 and Top-5 accuracy ...

### R421: All 39 Vision-Language Models have been evaluated on the Obj...
- **Rubric ID**: 785d4bfa-b645-4906-8c79-40ebbf96ba21
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ObjectNet test set, computing and saving both the Top-1 and Top-5 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ObjectNet Top-1 and Top-5 accuracy ...

### R422: A line of best fit has been computed between ImageNet (in-di...
- **Rubric ID**: 15f2ea57-1390-4572-ba6c-6153fc3e21db
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between ImageNet (in-distribution) Top-1 test accuracy and the Top-1 test accuracy on the out-of-distribution datasets: ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, and ObjectNet.
- **Parent context**: A line of best fit has been computed between ImageNet (in-distribution) Top-1 test accuracy and both...

### R423: A line of best fit has been computed between ImageNet (in-di...
- **Rubric ID**: e5998aa6-f9fb-40ad-92f2-75257454ff26
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between ImageNet (in-distribution) Top-1 test accuracy and the Top-5 test accuracy on the out-of-distribution datasets: ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, and ObjectNet.
- **Parent context**: A line of best fit has been computed between ImageNet (in-distribution) Top-1 test accuracy and both...

### R424: Code has been written to compute a line of best fit between...
- **Rubric ID**: 0dec7d31-f155-4cde-a946-2019ada2568d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to compute a line of best fit between the average LCA distance (using information content) on the ImageNet test set and the Top-5 test accuracy on the out-of-distribution datasets: ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, and ObjectNet.
- **Parent context**: A line of best fit between the average LCA distance (using information content) on the ImageNet test...

### R425: A line of best fit between the average LCA distance (using i...
- **Rubric ID**: 73444339-2d64-4199-ae98-69e57990de5f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A line of best fit between the average LCA distance (using information content) on the ImageNet test set and the Top-5 test accuracy on the out-of-distribution datasets (ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, and ObjectNet) has been computed.
- **Parent context**: A line of best fit between the average LCA distance (using information content) on the ImageNet test...

### R426: The slope of the line of best fit between ImageNet (in-distr...
- **Rubric ID**: 6457f099-5734-42e5-be31-e2044aaf2c68
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 accuracy (y-axis) and ImageNet-v2 Top-1 accuracy (x-axis) is positive.
- **Parent context**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 test accuracy and the out...

### R427: The slope of the line of best fit between ImageNet (in-distr...
- **Rubric ID**: bb0951fb-551c-4848-89e5-793919491aea
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 accuracy (y-axis) and ImageNet-Sketch Top-1 accuracy (x-axis) is positive.
- **Parent context**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 test accuracy and the out...

### R428: The slope of the line of best fit between ImageNet (in-distr...
- **Rubric ID**: 5a93bd6f-97a0-478d-b800-ac5d10b81967
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 accuracy (y-axis) and ImageNet-Rendition Top-1 accuracy (x-axis) is positive.
- **Parent context**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 test accuracy and the out...

### R429: The slope of the line of best fit between ImageNet (in-distr...
- **Rubric ID**: 6d6d6700-f411-4c4f-84dd-406bbc6ce574
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 accuracy (y-axis) and ImageNet-Adversarial Top-1 accuracy (x-axis) is positive.
- **Parent context**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 test accuracy and the out...

### R430: The slope of the line of best fit between ImageNet (in-distr...
- **Rubric ID**: f4ba4df6-1145-4d87-b743-42cf8ea0bcc2
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 accuracy (y-axis) and ObjectNet Top-1 accuracy (x-axis) is positive.
- **Parent context**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 test accuracy and the out...

### R431: The slope of the line of best fit between ImageNet (in-distr...
- **Rubric ID**: e949287f-6ad0-4505-b0b0-fdee393118e0
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 accuracy (y-axis) and ImageNet-v2 Top-5 accuracy (x-axis) is positive.
- **Parent context**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 test accuracy and the Top...

### R432: The slope of the line of best fit between ImageNet (in-distr...
- **Rubric ID**: e6f5488f-934e-4754-b609-ffe388831ded
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 accuracy (y-axis) and ImageNet-Sketch Top-5 accuracy (x-axis) is positive.
- **Parent context**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 test accuracy and the Top...

### R433: The slope of the line of best fit between ImageNet (in-distr...
- **Rubric ID**: b7c69409-a3f0-40ea-8d60-d82dae8e9498
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 accuracy (y-axis) and ImageNet-Rendition Top-5 accuracy (x-axis) is positive.
- **Parent context**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 test accuracy and the Top...

### R434: The slope of the line of best fit between ImageNet (in-distr...
- **Rubric ID**: d0eb4519-1828-4e9c-9c8f-79e631dd4589
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 accuracy (y-axis) and ImageNet-Adversarial Top-5 accuracy (x-axis) is positive.
- **Parent context**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 test accuracy and the Top...

### R435: The slope of the line of best fit between ImageNet (in-distr...
- **Rubric ID**: b7f522d1-6988-46bf-afa7-33b7bd239c22
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 accuracy (y-axis) and ObjectNet Top-5 accuracy (x-axis) is positive.
- **Parent context**: The slope of the line of best fit between ImageNet (in-distribution) Top-1 test accuracy and the Top...

### R436: The slope of the line of best fit between the average LCA di...
- **Rubric ID**: 15f170cf-08b6-47f1-a260-b36d248235c2
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between the average LCA distance (using information content) on the ImageNet test set (y-axis) and the Top-1 accuracy (x-axis) on the ImageNet-v2 dataset is negative.
- **Parent context**: The slope of the line of best fit between the average LCA distance (using information content) on th...

### R437: The slope of the line of best fit between the average LCA di...
- **Rubric ID**: c941cb4b-1918-4545-b292-1b2bd2171271
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between the average LCA distance (using information content) on the ImageNet test set (y-axis) and the Top-1 accuracy (x-axis) on the ImageNet-Sketch dataset is negative.
- **Parent context**: The slope of the line of best fit between the average LCA distance (using information content) on th...

### R438: The slope of the line of best fit between the average LCA di...
- **Rubric ID**: 432867ec-f650-401f-982a-4bf13dd926d9
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between the average LCA distance (using information content) on the ImageNet test set (y-axis) and the Top-1 accuracy (x-axis) on the ImageNet-Rendition dataset is negative.
- **Parent context**: The slope of the line of best fit between the average LCA distance (using information content) on th...

### R439: The slope of the line of best fit between the average LCA di...
- **Rubric ID**: b70aed07-70ea-4a85-98ea-f0e420de11e9
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between the average LCA distance (using information content) on the ImageNet test set (y-axis) and the Top-1 accuracy (x-axis) on the ImageNet-Adversarial dataset is negative.
- **Parent context**: The slope of the line of best fit between the average LCA distance (using information content) on th...

### R440: The slope of the line of best fit between the average LCA di...
- **Rubric ID**: ad5b891c-d440-4d11-a62d-400cb80b8820
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between the average LCA distance (using information content) on the ImageNet test set (y-axis) and the Top-1 accuracy (x-axis) on the ObjectNet dataset is negative.
- **Parent context**: The slope of the line of best fit between the average LCA distance (using information content) on th...

### R441: The slope of the line of best fit between the average LCA di...
- **Rubric ID**: 231f083c-dd68-45f2-96b0-6a8b7887a023
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between the average LCA distance (using information content) on the ImageNet test set (y-axis) and the Top-5 accuracy (x-axis) on the ImageNet-v2 dataset is negative.
- **Parent context**: The slope of the line of best fit between the average LCA distance (using information content) on th...

### R442: The slope of the line of best fit between the average LCA di...
- **Rubric ID**: 1faabfec-8a2d-4e83-8c8d-ce52c8dc46a2
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between the average LCA distance (using information content) on the ImageNet test set (y-axis) and the Top-5 accuracy (x-axis) on the ImageNet-Sketch dataset is negative.
- **Parent context**: The slope of the line of best fit between the average LCA distance (using information content) on th...

### R443: The slope of the line of best fit between the average LCA di...
- **Rubric ID**: 6db1b1f8-1cb6-4b20-851d-dc5ac95b50e4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between the average LCA distance (using information content) on the ImageNet test set (y-axis) and the Top-5 accuracy (x-axis) on the ImageNet-Rendition dataset is negative.
- **Parent context**: The slope of the line of best fit between the average LCA distance (using information content) on th...

### R444: The slope of the line of best fit between the average LCA di...
- **Rubric ID**: 9cd89339-91c7-4e45-9a3c-ba3baf455e2a
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between the average LCA distance (using information content) on the ImageNet test set (y-axis) and the Top-5 accuracy (x-axis) on the ImageNet-Adversarial dataset is negative.
- **Parent context**: The slope of the line of best fit between the average LCA distance (using information content) on th...

### R445: Code to evaluate all 36 Vision Models in Appendix A on the I...
- **Rubric ID**: 99b032ec-71d6-47b9-a5ec-96896affc2a4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 36 Vision Models in Appendix A on the ImageNet test set has been written, computing and saving the average LCA distance (using information content) using each of the 75 model-specific latent heirarchies computed via $k$-means for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) average LCA distance (using information c...

### R446: All 36 Vision Models in Appendix A have been evaluated on th...
- **Rubric ID**: 109a2b20-712b-4378-b1fb-5ed9bb60547a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models in Appendix A have been evaluated on the ImageNet test set, computing and saving the average LCA distance (using information content) using each of the 75 model-specific latent heirarchies computed via $k$-means for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) average LCA distance (using information c...

### R447: Code to evaluate all 39 Vision-Language Models in Appendix A...
- **Rubric ID**: 782e8ba0-1f93-4dc9-ba5c-f197ab73e51b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 39 Vision-Language Models in Appendix A on the ImageNet test set has been written, computing and saving the average LCA distance (using information content) using each of the 75 model-specific latent heirarchies computed via $k$-means for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) average LCA distance (using info...

### R448: All 39 Vision-Language Models in Appendix A have been evalua...
- **Rubric ID**: 4febf73f-9c10-4464-a0aa-6d683524bf12
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models in Appendix A have been evaluated on the ImageNet test set, computing and saving the average LCA distance (using information content) using each of the 75 model-specific latent heirarchies computed via $k$-means for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) average LCA distance (using info...

### R449: Code to evaluate all 36 Vision Models in Appendix A on the I...
- **Rubric ID**: 76a6f803-ef49-4c32-b5bf-5dc9fbb77aca
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 36 Vision Models in Appendix A on the ImageNet test set has been written, computing and saving the average LCA distance (using information content) using the WordNet hierarchy accuracy for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) average LCA distance (using information c...

### R450: All 36 Vision Models in Appendix A have been evaluated on th...
- **Rubric ID**: ba6df4ae-7242-412a-a735-e3617ac8b9d6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models in Appendix A have been evaluated on the ImageNet test set, computing and saving the average LCA distance (using information content) using the WordNet hierarchy for each model.
- **Parent context**: All 36 Vision Models have their in-distribution (ImageNet) average LCA distance (using information c...

### R451: Code to evaluate all 39 Vision-Language Models in Appendix A...
- **Rubric ID**: 9d0e23da-705f-4fcf-a5ef-a1bb5c1a233e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 39 Vision-Language Models in Appendix A on the ImageNet test set has been written, computing and saving the average LCA distance (using information content) using the WordNet hierarchy for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) average LCA distance (using info...

### R452: All 39 Vision-Language Models in Appendix A have been evalua...
- **Rubric ID**: ec3bd251-cdda-4261-9482-3d0335ca1c86
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models in Appendix A have been evaluated on the ImageNet test set, computing and saving the average LCA distance (using information content) using the WordNet hierarchy for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution (ImageNet) average LCA distance (using info...

### R453: Code to evaluate all 36 Vision Models in Appendix A on the I...
- **Rubric ID**: 96cdabdc-1bff-4758-87f7-1fac99dcf273
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 36 Vision Models in Appendix A on the ImageNet test set has been written, computing and saving the Top-1 accuracy for each model.
- **Parent context**: All 36 Vision Models have their in-distribution Top-1 accuracy on the ImageNet test set computed and...

### R454: All 36 Vision Models in Appendix A have been evaluated on th...
- **Rubric ID**: 42c9a7c3-b4e8-48f3-85ef-8f4c5e1ec4c7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models in Appendix A have been evaluated on the ImageNet test set, computing and saving the Top-1 accuracy for each model.
- **Parent context**: All 36 Vision Models have their in-distribution Top-1 accuracy on the ImageNet test set computed and...

### R455: Code to evaluate all 39 Vision-Language Models in Appendix A...
- **Rubric ID**: 8f66f249-7c39-423f-ab03-c905c4bf1ba8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to evaluate all 39 Vision-Language Models in Appendix A on the ImageNet test set has been written, computing and saving the Top-1 accuracy for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution Top-1 accuracy on the ImageNet test set com...

### R456: All 39 Vision-Language Models in Appendix A have been evalua...
- **Rubric ID**: b646b14a-5ce3-4517-a5d2-c9ba9c25ec45
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models in Appendix A have been evaluated on the ImageNet test set, computing and saving the Top-1 accuracy for each model.
- **Parent context**: All 39 Vision-Language Models have their in-distribution Top-1 accuracy on the ImageNet test set com...

### R457: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: eaa8995c-39da-40b5-b251-99d3e47403b0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-v2 test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-v2 Top-1 accuracy computed and save...

### R458: All 36 Vision Models have been evaluated on the ImageNet-v2...
- **Rubric ID**: cd92d3a0-6431-4c01-8a4e-5027c40af781
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-v2 test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-v2 Top-1 accuracy computed and save...

### R459: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: 459f46dc-3ebe-48b4-9fbd-ba24584bbbd2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-Sketch test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Sketch Top-1 accuracy computed and ...

### R460: All 36 Vision Models have been evaluated on the ImageNet-Ske...
- **Rubric ID**: ad31e770-6dd3-4f14-ba03-8bc7c2625dcf
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-Sketch test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Sketch Top-1 accuracy computed and ...

### R461: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: d7ba6934-ff9d-4da6-b3ba-d4ad676c65e0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-Rendition test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Rendition Top-1 accuracy computed a...

### R462: All 36 Vision Models have been evaluated on the ImageNet-Ren...
- **Rubric ID**: b145e558-5a3d-48a1-9b34-9105979afe21
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-Rendition test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Rendition Top-1 accuracy computed a...

### R463: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: 482dc4f3-611b-41f0-9db7-511711656e76
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ImageNet-Adversarial test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Adversarial Top-1 accuracy computed...

### R464: All 36 Vision Models have been evaluated on the ImageNet-Adv...
- **Rubric ID**: fe6f9d78-767b-4272-92d4-9604150e91c5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ImageNet-Adversarial test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ImageNet-Adversarial Top-1 accuracy computed...

### R465: Code has been written to evaluate all 36 Vision Models on th...
- **Rubric ID**: a7481a1d-23fd-47ae-8e87-976396fe4487
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 36 Vision Models on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ObjectNet Top-1 accuracy computed and saved.

### R466: All 36 Vision Models have been evaluated on the ObjectNet te...
- **Rubric ID**: 1062f8a5-6d90-4f33-b4cd-3a408d1eaaf7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 36 Vision Models have been evaluated on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 36 Vision Models have had their out-of-distribution ObjectNet Top-1 accuracy computed and saved.

### R467: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: 3651998c-b65e-4a9d-b978-1884a07ac18a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-v2 test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-v2 Top-1 accuracy computed...

### R468: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: 472949aa-d73f-45e8-b7b0-43c778f9918b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-v2 test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-v2 Top-1 accuracy computed...

### R469: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: 2d85ddc0-ba21-4c71-9d44-a4f06326b7e0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-Sketch test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Sketch Top-1 accuracy comp...

### R470: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: 8ee8900d-70b0-4f2d-b0cd-461b5c9d3dca
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-Sketch test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Sketch Top-1 accuracy comp...

### R471: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: 5356f325-7f96-4510-b9fb-6e4104507cbd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-Rendition test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Rendition Top-1 accuracy c...

### R472: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: 32dc3cce-c201-453b-9bd9-950a5d9daaf0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-Rendition test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Rendition Top-1 accuracy c...

### R473: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: eea6c753-03d6-480c-8f47-1193b6aed15d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ImageNet-Adversarial test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Adversarial Top-1 accuracy...

### R474: All 39 Vision-Language Models have been evaluated on the Ima...
- **Rubric ID**: 9de50806-b11c-406b-91ef-b45a1101ba1c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ImageNet-Adversarial test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ImageNet-Adversarial Top-1 accuracy...

### R475: Code has been written to evaluate all 39 Vision-Language Mod...
- **Rubric ID**: 9b535027-4f33-4783-a422-0264c2ea4508
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate all 39 Vision-Language Models on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ObjectNet Top-1 accuracy computed a...

### R476: All 39 Vision-Language Models have been evaluated on the Obj...
- **Rubric ID**: 735ca768-890c-4eb8-88f0-382e94bb01ce
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All 39 Vision-Language Models have been evaluated on the ObjectNet test set, computing and saving the Top-1 accuracy.
- **Parent context**: All 39 Vision-Language Models have had their out-of-distribution ObjectNet Top-1 accuracy computed a...

### R477: For each of the 75 latent hierarchies generated using $k$-me...
- **Rubric ID**: 549d4152-712c-4a04-a613-a4b88427b61f
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each of the 75 latent hierarchies generated using $k$-means, the Pearson correlation between the average LCA distance (using information content) (with respect to the latent hierarchy) on the ImageNet test set and the out-of-distribution Top-1 accuracy on the ImageNet-v2 dataset has been computed and saved, for a total of 75 Pearson correlations.
- **Parent context**: For each of the 75 latent hierarchies generated using $k$-means and the 5 out-of-distribution datase...

### R478: For each of the 75 latent hierarchies generated using $k$-me...
- **Rubric ID**: d5ce00cf-8d20-4c17-8bce-525080efd218
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each of the 75 latent hierarchies generated using $k$-means, the Pearson correlation between the average LCA distance (using information content) (with respect to the latent hierarchy) on the ImageNet test set and the out-of-distribution Top-1 accuracy on the ImageNet-Sketch dataset has been computed and saved, for a total of 75 Pearson correlations.
- **Parent context**: For each of the 75 latent hierarchies generated using $k$-means and the 5 out-of-distribution datase...

### R479: For each of the 75 latent hierarchies generated using $k$-me...
- **Rubric ID**: aee8422e-5570-4a14-aea0-953214d15a99
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each of the 75 latent hierarchies generated using $k$-means, the Pearson correlation between the average LCA distance (using information content) (with respect to the latent hierarchy) on the ImageNet test set and the out-of-distribution Top-1 accuracy on the ImageNet-Rendition dataset has been computed and saved, for a total of 75 Pearson correlations.
- **Parent context**: For each of the 75 latent hierarchies generated using $k$-means and the 5 out-of-distribution datase...

### R480: For each of the 75 latent hierarchies generated using $k$-me...
- **Rubric ID**: 3f5de389-9d28-4e86-b96a-45ca428d7636
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each of the 75 latent hierarchies generated using $k$-means, the Pearson correlation between the average LCA distance (using information content) (with respect to the latent hierarchy) on the ImageNet test set and the out-of-distribution Top-1 accuracy on the ImageNet-Adversarial dataset has been computed and saved, for a total of 75 Pearson correlations.
- **Parent context**: For each of the 75 latent hierarchies generated using $k$-means and the 5 out-of-distribution datase...

### R481: For each of the 75 latent hierarchies generated using $k$-me...
- **Rubric ID**: 2bb9a89b-7157-4f3d-8353-e19b7ff14a10
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each of the 75 latent hierarchies generated using $k$-means, the Pearson correlation between the average LCA distance (using information content) (with respect to the latent hierarchy) on the ImageNet test set and the out-of-distribution Top-1 accuracy on the ObjectNet dataset has been computed and saved, for a total of 75 Pearson correlations.
- **Parent context**: For each of the 75 latent hierarchies generated using $k$-means and the 5 out-of-distribution datase...

### R482: The Pearson correlation between the average LCA distance (us...
- **Rubric ID**: 15ad790e-289d-4860-acbf-ecbff9088554
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the average LCA distance (using information content) (with respect to the WordNet hierarchy) on the ImageNet test set and the out-of-distribution Top-1 accuracy on the ImageNet-v2 dataset has been computed and saved.
- **Parent context**: For each of the 5 out-of-distribution datasets (ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, Im...

### R483: The Pearson correlation between the average LCA distance (us...
- **Rubric ID**: 59d96bb3-76b1-4a63-88d0-6295e3cc239f
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the average LCA distance (using information content) (with respect to the WordNet hierarchy) on the ImageNet test set and the out-of-distribution Top-1 accuracy on the ImageNet-Sketch dataset has been computed and saved.
- **Parent context**: For each of the 5 out-of-distribution datasets (ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, Im...

### R484: The Pearson correlation between the average LCA distance (us...
- **Rubric ID**: a5145532-255e-4234-9a79-58b2c7b15e36
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the average LCA distance (using information content) (with respect to the WordNet hierarchy) on the ImageNet test set and the out-of-distribution Top-1 accuracy on the ImageNet-Rendition dataset has been computed and saved.
- **Parent context**: For each of the 5 out-of-distribution datasets (ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, Im...

### R485: The Pearson correlation between the average LCA distance (us...
- **Rubric ID**: 7a1dc339-d292-4760-87b5-fe7ae055a832
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the average LCA distance (using information content) (with respect to the WordNet hierarchy) on the ImageNet test set and the out-of-distribution Top-1 accuracy on the ImageNet-Adversarial dataset has been computed and saved.
- **Parent context**: For each of the 5 out-of-distribution datasets (ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, Im...

### R486: The Pearson correlation between the average LCA distance (us...
- **Rubric ID**: ddb041b0-5a88-497a-84d5-d464305f4fbf
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Pearson correlation between the average LCA distance (using information content) (with respect to the WordNet hierarchy) on the ImageNet test set and the out-of-distribution Top-1 accuracy on the ObjectNet dataset has been computed and saved.
- **Parent context**: For each of the 5 out-of-distribution datasets (ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, Im...

### R487: Code to compute and save the mean of the 75 Pearson correlat...
- **Rubric ID**: 78b9ab95-ee85-48af-9df8-6ae0813fb0cd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-v2 dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R488: The mean of the 75 Pearson correlations between average LCA...
- **Rubric ID**: ca6fd309-e63b-4325-b78e-400866459f2f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-v2 dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R489: Code to compute and save the min of the 75 Pearson correlati...
- **Rubric ID**: ce0bf884-c39a-40b4-badb-8255f79bfd1c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the min of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-v2 dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R490: The min of the 75 Pearson correlations between average LCA d...
- **Rubric ID**: 3345c51a-6d37-4a42-b87f-3bf2afb5a368
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The min of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-v2 dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R491: Code to compute and save the max of the 75 Pearson correlati...
- **Rubric ID**: c455f771-3286-41a5-85fd-82ad57c14f27
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the max of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-v2 dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R492: The max of the 75 Pearson correlations between average LCA d...
- **Rubric ID**: 4622a17c-6941-4206-8b08-523a7be4a3df
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The max of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-v2 dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R493: Code to compute and save the standard deviation of the 75 Pe...
- **Rubric ID**: 1d5bb7f8-17dd-454e-91a2-7dece3eabbbb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the standard deviation of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-v2 dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R494: The standard deviation of the 75 Pearson correlations betwee...
- **Rubric ID**: 9bae163a-e97d-4d93-a7bb-93faf8d19467
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The standard deviation of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-v2 dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R495: Code to compute and save the mean of the 75 Pearson correlat...
- **Rubric ID**: 4c632086-036e-42b0-a09a-d4b534223513
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Sketch dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R496: The mean of the 75 Pearson correlations between average LCA...
- **Rubric ID**: 92285984-06ce-411c-91cd-7f6bdc9495dc
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Sketch dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R497: Code to compute and save the min of the 75 Pearson correlati...
- **Rubric ID**: deb81d6a-82da-4916-ab20-45953a1409f7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the min of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Sketch dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R498: The min of the 75 Pearson correlations between average LCA d...
- **Rubric ID**: 311af68c-035e-42bb-9de9-bade73b692aa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The min of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Sketch dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R499: Code to compute and save the max of the 75 Pearson correlati...
- **Rubric ID**: 694a4def-6382-41f0-978b-6f3c0daa3efc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the max of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Sketch dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R500: The max of the 75 Pearson correlations between average LCA d...
- **Rubric ID**: 932b8cd1-fa67-4849-93fa-bb3cadef8126
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The max of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Sketch dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R501: Code to compute and save the standard deviation of the 75 Pe...
- **Rubric ID**: f0f23ceb-e24b-404b-9004-aef1a53542f1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the standard deviation of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Sketch dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R502: The standard deviation of the 75 Pearson correlations betwee...
- **Rubric ID**: e12b8688-ca7c-49c1-b703-22b98b9e454a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The standard deviation of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Sketch dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R503: Code to compute and save the mean of the 75 Pearson correlat...
- **Rubric ID**: 2f17a34d-758c-499b-a7e4-ef3dfd9313cc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Rendition dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R504: The mean of the 75 Pearson correlations between average LCA...
- **Rubric ID**: 6c4e0af1-c329-440f-b5d5-9d1f9b291144
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Rendition dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R505: Code to compute and save the min of the 75 Pearson correlati...
- **Rubric ID**: 990d8e0a-8ca3-4aae-b363-f4ced06cb772
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the min of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Rendition dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R506: The min of the 75 Pearson correlations between average LCA d...
- **Rubric ID**: 4cc483db-6195-4083-941e-94f31147f225
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The min of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Rendition dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R507: Code to compute and save the max of the 75 Pearson correlati...
- **Rubric ID**: e0672e72-9244-40f7-be22-de2845a72028
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the max of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Rendition dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R508: The max of the 75 Pearson correlations between average LCA d...
- **Rubric ID**: 7a450fe5-979d-4c28-bb10-cf2dc6aab748
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The max of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Rendition dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R509: Code to compute and save the standard deviation of the 75 Pe...
- **Rubric ID**: 21bbb9eb-9f69-4120-9b43-3380081c6500
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the standard deviation of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Rendition dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R510: The standard deviation of the 75 Pearson correlations betwee...
- **Rubric ID**: 04b430f4-0616-482f-8b29-d252095b52be
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The standard deviation of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Rendition dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R511: Code to compute and save the mean of the 75 Pearson correlat...
- **Rubric ID**: 55476501-8c38-45a7-80b3-50e24e2aa2d7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the mean of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Adversarial dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R512: The mean of the 75 Pearson correlations between average LCA...
- **Rubric ID**: 98db6576-f3e2-4fb7-8901-2a375314183b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The mean of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Adversarial dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R513: Code to compute and save the min of the 75 Pearson correlati...
- **Rubric ID**: 733588d3-a96b-4840-8e46-6e129566e28b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the min of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Adversarial dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R514: The min of the 75 Pearson correlations between average LCA d...
- **Rubric ID**: c0e5df85-1d50-4b79-8c5f-a13906e4bb32
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The min of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Adversarial dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R515: Code to compute and save the max of the 75 Pearson correlati...
- **Rubric ID**: fb456f66-9108-490c-8852-2197e70acae4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the max of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Adversarial dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R516: The max of the 75 Pearson correlations between average LCA d...
- **Rubric ID**: 52b8117a-3f02-4af4-a456-381d622fca48
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The max of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Adversarial dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R517: Code to compute and save the standard deviation of the 75 Pe...
- **Rubric ID**: dad4cef0-d671-4683-9429-ebc260fdb434
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the standard deviation of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Adversarial dataset has been written.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R518: The standard deviation of the 75 Pearson correlations betwee...
- **Rubric ID**: f4886461-60d8-40b4-b60a-3c62a4ee0fa4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The standard deviation of the 75 Pearson correlations between average LCA distances (using information content) on the ImageNet test set and Top-1 accuracy on the ImageNet-Adversarial dataset has been computed and saved.
- **Parent context**: The mean, min, max, and standard deviation of the 75 Pearson correlations between average LCA distan...

### R519: The Pearson correlation between the Top-1 accuracy on the Im...
- **Rubric ID**: 224b8453-0017-41f6-9187-3e4d61bdda61
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy on the ImageNet-v2 dataset across all 75 models has been computed and saved.
- **Parent context**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy a...

### R520: Code to compute and save the Pearson correlation between the...
- **Rubric ID**: 28c3d898-679b-401f-9388-cb419b12177c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy on the ImageNet-v2 dataset across all 75 models has been written.
- **Parent context**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy a...

### R521: The Pearson correlation between the Top-1 accuracy on the Im...
- **Rubric ID**: 47e32c7d-f7c3-428a-b935-04df5af51472
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy on the ImageNet-Sketch dataset across all 75 models has been computed and saved.
- **Parent context**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy a...

### R522: Code to compute and save the Pearson correlation between the...
- **Rubric ID**: 0576a1e6-d703-46b5-9c8e-0aaf93edf5dd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy on the ImageNet-Sketch dataset across all 75 models has been written.
- **Parent context**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy a...

### R523: The Pearson correlation between the Top-1 accuracy on the Im...
- **Rubric ID**: c14c3d85-c1c6-4e1f-9f22-53b5e7b1ba14
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy on the ImageNet-Rendition dataset across all 75 models has been computed and saved.
- **Parent context**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy a...

### R524: Code to compute and save the Pearson correlation between the...
- **Rubric ID**: fe4ba27f-b88a-4367-80db-a2adeaaa2684
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy on the ImageNet-Rendition dataset across all 75 models has been written.
- **Parent context**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy a...

### R525: The Pearson correlation between the Top-1 accuracy on the Im...
- **Rubric ID**: 4d8381cc-d0a0-42bf-a141-ee1b09b193f0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy on the ImageNet-Adversarial dataset across all 75 models has been computed and saved.
- **Parent context**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy a...

### R526: Code to compute and save the Pearson correlation between the...
- **Rubric ID**: 9db332cd-4503-4055-90d1-4c340bedf20e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy on the ImageNet-Adversarial dataset across all 75 models has been written.
- **Parent context**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy a...

### R527: The Pearson correlation between the Top-1 accuracy on the Im...
- **Rubric ID**: 3b43637f-a779-4629-9968-93a5ccd23ffd
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy on the ObjectNet dataset across all 75 models has been computed and saved.
- **Parent context**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy a...

### R528: Code to compute and save the Pearson correlation between the...
- **Rubric ID**: 7d09f086-7c6c-490e-b4c1-2c94922ef60c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code to compute and save the Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy on the ObjectNet dataset across all 75 models has been written.
- **Parent context**: The Pearson correlation between the Top-1 accuracy on the ImageNet test set and the Top-1 accuracy a...

### R529: Code has been written to sanity check the resultant soft-lab...
- **Rubric ID**: d92dd79c-0a1e-4d73-bed1-3284457056c4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to sanity check the resultant soft-label matrix, as described in the addendum.
- **Parent context**: The soft labels based on LCA distance using tree node depth and the WordNet hierarchy have been comp...

### R530: Code has been written find the $\alpha$ such that the interp...
- **Rubric ID**: 2db37c1e-e205-4e2f-9328-ad0e2911520f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written find the $\alpha$ such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ maximizes the Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ is varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R531: A value for $\alpha$ has been found such that the interpolat...
- **Rubric ID**: 6a08ac28-5991-42f8-9591-c8c32fe91396
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A value for $\alpha$ has been found such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ has maximal Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ has been varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R532: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: a2feaa79-2c91-45a0-9005-107bdd030472
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R533: The interpolated linear probe has been evaluated on the in-d...
- **Rubric ID**: eb0ad9dc-934e-4ab0-9054-6d8eecc7f9e0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R534: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 889db697-e787-42bb-9547-45698b369640
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R535: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 7778d03d-047b-4e1f-a6c2-3e3883e3c5a2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R536: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: cf484644-d612-4a0f-bb9a-a79a60858b39
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R537: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 0e7b3049-9875-42cd-b3d0-c134c3d821ca
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R538: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: bd4aff6e-fa22-4e79-8662-7fdcb92a591b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R539: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 0ee24031-4446-4f0d-bb7f-f93c0cd8000c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R540: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 67ab15da-2546-4795-b713-f2cabd71709f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R541: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 454153ce-0f2a-4ec1-8894-f0d84f7af8a7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R542: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 92ec2b06-d6ff-4331-8446-c64316cd2f43
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R543: The interpolated linear probe has been evaluated on the Obje...
- **Rubric ID**: f5b07f76-dc5d-417c-9180-c694fbd94b14
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R544: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 3641f17e-426f-46fc-8a9d-f2d9476c2a19
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R545: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 08a97c75-78bc-4cbe-be03-79ab94c3eb41
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R546: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: fbb99be9-12d8-4250-a8c9-7bac40b9b650
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R547: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: c2b94915-5e81-4d4c-a3d4-0021d0b94a53
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R548: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: ff65e5da-ca67-4496-bb06-072a84a24bd5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R549: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: a7d2dd78-d4f4-45d8-b4ee-8aa4e7af44d7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R550: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: e8eb0464-9781-4b2a-89a5-bcb1650a1563
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R551: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: f4e1274f-d321-4c39-9428-d6486084e3f9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R552: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: d754bc2b-55d9-47a8-bac9-7c698ba7f91d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R553: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 29aeb360-2945-46c0-818f-6890892a8ace
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R554: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 5b501084-cf54-42dd-9e1f-f0d76812930a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R555: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 20d8644c-5c41-4d5e-9f88-1b580a5e2199
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R556: Code has been written find the $\alpha$ such that the interp...
- **Rubric ID**: 83228c0a-5eaa-4785-913e-3794a767dd45
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written find the $\alpha$ such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ maximizes the Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ is varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R557: A value for $\alpha$ has been found such that the interpolat...
- **Rubric ID**: 25536d74-8b55-4b97-a586-17572e831ec6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A value for $\alpha$ has been found such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ has maximal Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ has been varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R558: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: be2ccc26-06a9-4001-9e4c-7b50fe5ca0f6
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R559: The interpolated linear probe has been evaluated on the in-d...
- **Rubric ID**: 80e928b2-3a44-40f3-8386-d0757f13c052
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R560: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 2e37028f-1d65-4210-91ca-8c95cca5d7f3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R561: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 70af9c70-3877-4aa3-b8aa-4d384cd223d6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R562: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 3ac813d2-d158-4adf-8025-4ab5c88d325e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R563: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 2ead02ff-a372-4966-ab70-9507a602c07f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R564: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 2c3c4835-dbe9-41a0-bd91-550a4fae0031
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R565: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 281c3840-7ebf-4dc4-8191-444cd74009cf
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R566: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 87c9d4fa-8d80-40e4-a544-b87c3818fb1e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R567: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: f7a345ae-5987-42da-9495-7d0cbafb8125
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R568: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 04ec9a6c-42f3-4268-ac4b-0799c190b4bb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R569: The interpolated linear probe has been evaluated on the Obje...
- **Rubric ID**: ddba83a1-137b-4eb4-9bd0-573916f2c5d1
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R570: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 5d7d45d9-673d-42fa-a9e4-1255b4bacd9e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R571: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 9a721f24-19dd-43ec-95c7-8781de2fc888
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R572: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 907872a7-9d8d-471a-942d-8e4106e6886b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R573: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 7034e638-3ceb-44d0-a572-2f5e676e8e12
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R574: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 6add721f-ab94-4f20-8fd2-4b7b1e48cbde
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R575: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: caeecf8b-42d5-4813-95fa-5a9d80e6f7cb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R576: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: ec5a3529-3391-4854-955a-35b6ec050787
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R577: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 28afa61b-760f-44fb-9927-bc8289ba1852
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R578: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: ea0503eb-7686-4893-a3dc-facf949cb93c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R579: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 88650a96-24b9-4dba-a22c-7592e9ca9f42
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R580: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: e7d742c8-59bd-4012-889c-0cf5c18ea3f0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R581: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 56572b1d-13bf-4ed3-97c9-091ca479060e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R582: Code has been written find the $\alpha$ such that the interp...
- **Rubric ID**: 8ce6a9a6-1bde-4a34-9199-2af13df8c9b6
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written find the $\alpha$ such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ maximizes the Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ is varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R583: A value for $\alpha$ has been found such that the interpolat...
- **Rubric ID**: 39530183-ad24-4989-ac22-16f2ae8bc0d1
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A value for $\alpha$ has been found such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ has maximal Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ has been varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R584: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 1e4ccac1-a01f-41d8-8b9b-8a9029469454
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R585: The interpolated linear probe has been evaluated on the in-d...
- **Rubric ID**: ff04e374-d79c-4579-b9ed-971cda10e5d0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R586: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: c62c1fab-8c2e-4433-ad04-3457a6813aba
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R587: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 552cc337-ce4f-484a-bfb4-cc1f66140df8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R588: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 07e8799d-d6a6-4b90-ade9-58c70d802273
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R589: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 28cda5fe-10fd-43f8-b86b-95ffa9735e5d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R590: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 4af9175b-c3fc-422f-bb07-be8aa1b5175e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R591: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: b0add35a-ede7-4dba-a291-a7c25ac7c59b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R592: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: a08caab8-db5b-4361-912b-9a946e3f12fa
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R593: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: a017885b-7380-4841-b815-765be3e3105c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R594: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: b1e1448a-7242-4af1-afec-724c62484d55
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R595: The interpolated linear probe has been evaluated on the Obje...
- **Rubric ID**: f8868524-71db-4258-8535-109abedd7ace
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R596: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: c8e94de6-a51e-423e-903b-4932e747c60b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R597: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 3ad43e0e-0348-49fe-a595-5d7ff4e1c575
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R598: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: a0556b47-af15-40bd-9d14-dc77b778d181
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R599: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: fb8b0c1b-a413-4074-b87d-10a9f2e5b5d7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R600: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 57f9e9eb-25a2-4af7-94fe-cb57c0c56b36
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R601: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: f86ce2ff-1608-4559-ac16-f25dea2636c0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R602: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: f82f872a-0d19-41b4-b364-dbea5c641fa8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R603: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 9e5d2967-6deb-4128-9769-36dd8d61662b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R604: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 9bedd5f3-7b34-48eb-ad93-48c46ea1d981
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R605: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: db6431bf-ee07-49b0-b1d6-57d5d5059feb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R606: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 3ca7e821-34aa-4c1b-86b7-64061330a74f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R607: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 4863b03d-0f1f-4e52-87b6-a7f44aaf26c5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R608: A value for $\alpha$ has been found such that the interpolat...
- **Rubric ID**: 13c4d32c-01d3-4ade-bbd7-05010201c86a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A value for $\alpha$ has been found such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ has maximal Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ has been varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R609: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 7cf773e8-6e14-4340-a55d-837d1946d6b9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R610: The interpolated linear probe has been evaluated on the in-d...
- **Rubric ID**: 0af08bb2-7ca3-401d-87db-7800c3cd4905
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R611: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 4170166c-7336-4c12-a6de-fb66ee0f54f2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R612: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: ba69c94b-57a6-4870-8739-ed2909d4ff25
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R613: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: af6459d0-ef40-4095-a2db-8523718466d6
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R614: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 7d711cc1-52a0-46a8-be29-15cee8bd88ef
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R615: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 9b4f6e36-f3f8-425b-b578-ef4f14e36c01
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R616: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 0db881cd-bec6-4536-a854-a3985df41223
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R617: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: ff45c34f-f2c1-40f2-918a-87ca0a600859
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R618: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: edfea5df-7e75-4250-a094-a0f259c9c2be
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R619: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: bb1443a7-c8d7-401a-9a6d-cb0d9c86b07a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R620: The interpolated linear probe has been evaluated on the Obje...
- **Rubric ID**: 672cce65-627d-4257-915f-fbb14e5054f0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R621: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 5d876667-1008-4f17-9823-751fb16bdc96
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R622: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 8431f2ac-78aa-42f6-b8a1-9f839142fd61
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R623: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 974a0392-768e-463b-8109-29391f15ccfe
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R624: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 30a52866-9070-49b3-b749-1b63581f28b9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R625: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 97a4a324-225d-4222-8ab0-b4a5198d1d15
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R626: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 8bf40213-89a5-4420-9952-e99daae1c62a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R627: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: eef84dae-b211-4304-9e66-1959fffed195
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R628: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: ca55c4ad-3ad3-4aba-b03c-0034704e4803
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R629: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 80d62554-2882-4595-8eda-8569321d97cc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R630: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 755b0a8e-fcd2-46e2-a080-3ed536d6c05a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R631: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 3a69d87e-0612-40bd-9e15-bcbba4e73cf8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R632: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 9456426d-f64e-4379-ba10-a1eb72b57fee
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R633: Code has been written find the $\alpha$ such that the interp...
- **Rubric ID**: 8b265399-8cc1-4871-b4f7-8c9e14869233
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written find the $\alpha$ such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ maximizes the Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ is varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R634: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 9565544c-de5b-4453-94a7-7ed95e3209c0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R635: The interpolated linear probe has been evaluated on the in-d...
- **Rubric ID**: 4144524d-c4b5-4f37-be9e-dc7d6e233594
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R636: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: c0c47e8e-018b-4a31-9ed4-49c36ae0db87
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R637: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 49e0adfd-2b08-4a41-971d-6bb87adb14eb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R638: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: e041a5c9-99d5-4cd3-9e2d-aadbcd0ce26b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R639: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: ec8e9375-4f53-4ce2-85ef-b3849076627c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R640: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 20e58eb4-ee05-409a-b4e5-3aacc7d2d33e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R641: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 713a1b6d-3622-490e-85f3-84a6d79f50cd
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R642: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 5d24a712-ace6-4f0a-942e-58514113c77d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R643: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: cb029a98-7a8a-41f2-a31a-fc189569b7e9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R644: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: fd55e7c7-5088-448a-babd-b2468eebcbc5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R645: The interpolated linear probe has been evaluated on the Obje...
- **Rubric ID**: 5f35dd85-94c4-46a4-b5bf-a7488ce140df
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R646: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: de1d7e4f-eb99-4483-b4b8-7428a2fec5aa
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R647: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: b46cecbd-d624-4fac-a64f-52f31d9192a5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R648: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: e16bc294-9376-4d21-931c-1f9d321ceeea
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R649: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 189d967f-1171-44cf-9658-05122c02536a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R650: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 6ac2a4bb-609c-4166-92f3-f7881425fe66
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R651: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: b37568db-77c3-4887-998b-3eda441ecca2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R652: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: cd6a83af-2921-40ab-88a3-c13d26c79c52
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R653: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 68683d70-712b-44d9-8ebe-f5d81ec87548
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R654: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 6dd1f747-be38-4f4c-abba-10ba6ea86602
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R655: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 6723176d-222e-4ce8-9e64-14bb7ef6ed4d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R656: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 6cc9d89f-8913-481c-adb9-fff64c26cb51
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R657: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 8d8a9bc2-b185-4245-b88b-bf7ec1a47520
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R658: Code has been written find the $\alpha$ such that the interp...
- **Rubric ID**: cdac76ba-4ed6-491e-b7aa-8b2e14f76ddd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written find the $\alpha$ such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ maximizes the Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ is varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R659: A value for $\alpha$ has been found such that the interpolat...
- **Rubric ID**: 46832485-34bb-4ec6-ad55-82fe1aa1097e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A value for $\alpha$ has been found such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ has maximal Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ has been varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R660: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 22a76e41-c737-40e9-b16e-0aad061e6cf7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R661: The interpolated linear probe has been evaluated on the in-d...
- **Rubric ID**: 36891736-f634-48e2-9611-07ac67aaf867
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R662: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 427a9668-1920-4311-ba66-4e307e59ec95
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R663: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: e2856c7e-bb3f-4be2-afb8-24ff848b72f3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R664: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 3246d9a5-52e7-4bae-9e7f-6135aac43d8e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R665: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: cf310b49-86fb-459a-8caf-add0b9df9058
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R666: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 99ff86c1-8b0f-4b64-b774-1243d2dc8725
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R667: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: f60ad9ea-3a16-458f-a44a-c21f0146ef08
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R668: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 42ac0506-42d9-4ecf-aaa8-0d38b656e0c9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R669: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: f1b514b8-4f71-479e-aad9-e548b740d3f7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R670: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 44d8e0ba-62ca-45c2-b166-bc3ce5a49646
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R671: The interpolated linear probe has been evaluated on the Obje...
- **Rubric ID**: 6be4adcd-82c4-4188-b4a8-fc55d62ae85d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R672: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 6e78e1ca-15f7-4be6-aaac-f09b68cf21b0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R673: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: ad910022-efb7-4ab8-a15f-48e27da740d8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R674: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 3cd16ca9-3c11-49b4-a411-18fe606e0da0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R675: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: f207fd64-7aa6-479a-a177-60d3f946fec5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R676: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 40667351-c2f3-43e2-97b8-6a9981c779bf
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R677: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 5c49a493-8e95-40b6-8c73-d48042051a9f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R678: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 2e62e6c4-87f2-4b60-a204-1bfc6afb0f63
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R679: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: ce42865d-11cd-4340-9615-680dc87d98bf
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R680: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 6d967a19-3c27-4a68-8aa5-31a4a8fa8a82
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R681: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: a5dec052-63b3-4d8f-98ef-bd2930fe8101
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R682: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 690d8711-42bb-400b-af8c-ba77ca4ee584
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy loss on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R683: The baseline linear probe trained with cross entropy loss ha...
- **Rubric ID**: 14764bfb-c71b-4649-9d77-1ae0644bae20
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy loss has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R684: The saved Top-1 accuracies show that the interpolated linear...
- **Rubric ID**: 2704d53a-9d2d-42c0-8fc7-610980beb82f
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The saved Top-1 accuracies show that the interpolated linear probes for all backbones (ResNet-18, ResNet-50, VIT-B, VIT-L, ConvNext, Swin Transformer) using the WordNet hierarchy beats the baseline linear probe (trained with cross-entropy and one-hot labels) on the ImageNet, ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, and ObjectNet test sets, except for VIT-B on ImageNet-v2, VIT-B on ImageNet-v2, Swin Transformer on ImageNet-v2 and ResNet-18 on ImageNet (where it tied).
- **Parent context**: Table 5 has been reproduced.

### R685: The ResNet-18 model, $M$, has been used with the in-distribu...
- **Rubric ID**: 8751d19c-d521-4a25-9f14-fbef8134bd01
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The ResNet-18 model, $M$, has been used with the in-distribution ImageNet image test set data $X$ and labels $Y$ to compute the average feature representation for each class.
- **Parent context**: A latent hierarchy produced with the ResNet-18 model has been computed using $k$-means clustering, a...

### R686: For the clustered ResNet-18 class representations, code has...
- **Rubric ID**: 79da70f2-78e0-4af9-a8c8-02dbd180d3fe
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the clustered ResNet-18 class representations, code has been written to compute the latent class hierarchy by finding the lowest common ancestor nodes for every pair of classes based on the clustering outcomes. The cluster level at which a pair of classes first share a cluster is the pairwise LCA height.
- **Parent context**: A latent hierarchy produced with the ResNet-18 model has been computed using $k$-means clustering, a...

### R687: Code has been written to sanity check the resultant soft-lab...
- **Rubric ID**: 39de8c84-b890-4df1-9d57-e6d379fb02fc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to sanity check the resultant soft-label matrix, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R688: Sanity checks have been run on the resultant soft-label matr...
- **Rubric ID**: ecfabc43-1519-4f5b-8457-d4394fe503eb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Sanity checks have been run on the resultant soft-label matrix, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R689: Code has been written to sanity check the resultant soft-lab...
- **Rubric ID**: 65de0ea0-8de1-4fe0-acef-dd82e5300d4f
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to sanity check the resultant soft-label matrix, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R690: Sanity checks have been run on the resultant soft-label matr...
- **Rubric ID**: 15c802c5-ca8a-4312-b4e1-b6dc555b1885
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Sanity checks have been run on the resultant soft-label matrix, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R691: Code has been written to sanity check the resultant soft-lab...
- **Rubric ID**: 8b91077f-02a2-4ac1-a103-2cb866daded3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to sanity check the resultant soft-label matrix, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R692: Sanity checks have been run on the resultant soft-label matr...
- **Rubric ID**: d05d920c-53e7-4731-be02-25782453dc7b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Sanity checks have been run on the resultant soft-label matrix, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R693: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: e0277db8-6e86-434c-b2c1-e58bf24630cb
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: A baseline linear probe trained with cross entropy has been trained and evaluated on all five out-of...

### R694: The baseline linear probe trained with cross entropy has bee...
- **Rubric ID**: 956f3600-9267-43ee-a4f0-f181792975f3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: A baseline linear probe trained with cross entropy has been trained and evaluated on all five out-of...

### R695: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: d9c33ae0-2ff1-428e-af23-c61c5501a267
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy on the in-distribution ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: A baseline linear probe trained with cross entropy has been trained and evaluated on all five out-of...

### R696: The baseline linear probe trained with cross entropy has bee...
- **Rubric ID**: dc53b1e7-3847-4968-b520-50da9334af42
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: A baseline linear probe trained with cross entropy has been trained and evaluated on all five out-of...

### R697: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: b264ed4c-fd96-46fb-aa58-4fcd5be2fb0d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy on the in-distribution ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: A baseline linear probe trained with cross entropy has been trained and evaluated on all five out-of...

### R698: The baseline linear probe trained with cross entropy has bee...
- **Rubric ID**: 34022bec-69c8-410f-96d9-63cd953b5a0c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: A baseline linear probe trained with cross entropy has been trained and evaluated on all five out-of...

### R699: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 346bc4eb-3847-4239-ad94-c3a7d45cf669
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy on the in-distribution ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: A baseline linear probe trained with cross entropy has been trained and evaluated on all five out-of...

### R700: The baseline linear probe trained with cross entropy has bee...
- **Rubric ID**: 9ac7ddae-88a1-49e9-a2ab-2d74b0eaafba
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: A baseline linear probe trained with cross entropy has been trained and evaluated on all five out-of...

### R701: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: b7ecf513-34bb-44f3-8310-50aad2c80d68
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy on the in-distribution ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: A baseline linear probe trained with cross entropy has been trained and evaluated on all five out-of...

### R702: The baseline linear probe trained with cross entropy has bee...
- **Rubric ID**: 8020826b-f2a1-42f9-9825-956ffdd924d9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: A baseline linear probe trained with cross entropy has been trained and evaluated on all five out-of...

### R703: Code has been written to evaluate the baseline linear probe...
- **Rubric ID**: 93e77e06-a6e0-4be5-a9d8-4759e1467812
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the baseline linear probe trained with cross entropy on the in-distribution ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: A baseline linear probe trained with cross entropy has been trained and evaluated on all five out-of...

### R704: The baseline linear probe trained with cross entropy has bee...
- **Rubric ID**: 08c2eb43-35df-4609-8d5c-d7b6585e8e48
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The baseline linear probe trained with cross entropy has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: A baseline linear probe trained with cross entropy has been trained and evaluated on all five out-of...

### R705: A value for $\alpha$ has been found such that the interpolat...
- **Rubric ID**: 1c5427d9-5eb9-4eea-bbfb-45bcfb1b0d66
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A value for $\alpha$ has been found such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ has maximal Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ has been varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R706: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 901b116d-cad2-472b-9a09-3556489cd540
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R707: The interpolated linear probe has been evaluated on the in-d...
- **Rubric ID**: 62e31bd8-5fb5-4148-b0bd-13408632d7e9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R708: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 27feae35-771b-4eed-9987-8ae6132bca11
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R709: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 2e76e6b3-1f49-4d11-b49e-2d500d159a47
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R710: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 6fa43267-0c6b-44cd-bb00-648915224786
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R711: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: cfb613e9-83f7-40ce-b85e-264053f2a335
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R712: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 192594e1-a6b5-438a-8d45-2c39e9b565f2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R713: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: e9924d6f-6ac9-46a3-a8bf-3ecaa0ded03c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R714: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: bf77e831-d695-46cd-b257-a36c5378a16d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R715: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: c43209ce-58cc-42ab-8cf3-0e59ad2615c1
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R716: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: bcb889dc-405f-49f8-8c16-9db3b744f1a2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R717: The interpolated linear probe has been evaluated on the Obje...
- **Rubric ID**: d68c52e3-1bb8-48fd-8e9c-85c7137ebc78
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R718: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: e72883e9-80ff-4be1-bfd3-07a2b6c6f0a5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R719: The interpolated linear probe has been evaluated on the in-d...
- **Rubric ID**: 8d54735a-f576-43e1-93e7-b2f2dd757402
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R720: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 0378c109-bfd7-4bac-ba4c-5f50391446da
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R721: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 53488990-aa8a-4a50-a400-6439e601adba
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R722: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: df399832-0045-41c2-8d61-122b92418c53
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R723: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: b12529c8-f2ee-463c-9ee2-89643292a6b0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R724: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 6da543b3-5a86-4ab5-b81e-b669ab8dbb48
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R725: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 2713c16c-2739-4348-b028-606464b4f818
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R726: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 9370f1b3-b44c-4560-bd25-3a7c8eaef8d8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R727: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: b1e1d239-6513-4841-bbc7-32f6769507c2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R728: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 90d79dbc-8248-47e3-ac9a-3aa573467017
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R729: The interpolated linear probe has been evaluated on the Obje...
- **Rubric ID**: 74c55c56-7655-4c7e-888b-778e81da8358
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R730: Code has been written find the $\alpha$ such that the interp...
- **Rubric ID**: dee88f98-62ad-4aea-93a8-a95b989d93dd
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written find the $\alpha$ such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ maximizes the Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ is varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R731: A value for $\alpha$ has been found such that the interpolat...
- **Rubric ID**: a6946f37-b0a6-4444-ba23-2480c717a4a9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A value for $\alpha$ has been found such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ has maximal Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ has been varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R732: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 1f55fa78-3df4-4980-aed8-57448e73e8c2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R733: The interpolated linear probe has been evaluated on the in-d...
- **Rubric ID**: 3a962379-ad60-44e1-b3f7-f37df81e569a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R734: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 240551e7-c78e-4a08-8246-e85abebedd0c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R735: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: ce0959b0-b6bf-4d17-a8ff-25b3359f1bf9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R736: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: e72e1d33-42b0-4db7-9f04-f5412bdca849
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R737: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: dbd64c36-7372-4af1-abee-eff073556af2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R738: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: a6ae9eae-5295-495b-b255-a837a9e6925e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R739: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 6a722e2c-55e9-43d6-8116-9097e2f8aa3b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R740: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 385307b3-b6f6-417c-904f-12b116c77676
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R741: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 06005283-d781-4829-b5e2-c68ffcf0a892
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R742: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 02159561-cf4a-4809-bbce-328a6d3e9a48
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R743: The interpolated linear probe has been evaluated on the Obje...
- **Rubric ID**: 6f23fe37-f3fe-4791-95fe-6f0fd560ecb7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R744: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 32e6ba9f-aa38-4943-8f43-0d7e05a32a5e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R745: The interpolated linear probe has been evaluated on the in-d...
- **Rubric ID**: 458de89f-f3ce-4a5b-8399-9e5850622b4b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the in-distribution ImageNet test set, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R746: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 32de5344-3bd9-4b84-9439-41dc6ec9b277
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R747: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: d066be41-5b76-4460-9b69-30741b3ef1a3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-v2 dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R748: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: c57fec17-d7fc-46b3-8fb5-dd6670a617f9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R749: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: 14556fa2-298f-43b3-99a2-52c580341bb8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Sketch dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R750: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: f60b9c66-5c58-46ef-9d9f-84bcecebba93
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R751: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: fcf94206-25f4-48e4-a4c2-c08d054ba87a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Rendition dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R752: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 1ee9b3de-601b-490c-825e-bc6fc4a30778
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R753: The interpolated linear probe has been evaluated on the Imag...
- **Rubric ID**: dcdfc777-dcc5-4551-9ae1-565898938349
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ImageNet-Adversarial dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R754: Code has been written to evaluate the interpolated linear pr...
- **Rubric ID**: 1feb98fa-c698-4418-a33f-7ef748bc6f23
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to evaluate the interpolated linear probe on the in-distribution ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R755: The interpolated linear probe has been evaluated on the Obje...
- **Rubric ID**: c47aa9e1-37e4-4df6-bd90-d199f9824968
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The interpolated linear probe has been evaluated on the ObjectNet dataset, computing Top-1 accuracy and saving the results.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R756: The saved Top-1 accuracies show that the interpolated linear...
- **Rubric ID**: 0c04bd6e-d4bf-4a70-9802-f7a5ee2ffb8b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The saved Top-1 accuracies show that the interpolated linear probe using the latent hierarchy computed by OpenCLIP(vit-l-14) achieves the highest score on the ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, and ObjectNet datasets, out of the probes trained with latent hierarchies (i.e., excluding WordNet).
- **Parent context**: Table 6 has been reproduced.

### R757: The saved Top-1 accuracies show that the interpolated linear...
- **Rubric ID**: d1721568-a65a-4c43-b781-76d763b2121c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The saved Top-1 accuracies show that the interpolated linear probe using the latent hierarchy computed by MnasNet achieves the lowest score (or equal in some cases) out of the interpolated linear probes (i.e., excluding the baselines) on the ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, and ObjectNet datasets.
- **Parent context**: Table 6 has been reproduced.

### R758: The saved Top-1 accuracies show that the baseline linear pro...
- **Rubric ID**: 59130136-990c-4e16-aa89-31d765b8d77b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The saved Top-1 accuracies show that the baseline linear probes using the cross entropy loss score worse than the interpolated linear probes across all of datasets: ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, and ObjectNet.
- **Parent context**: Table 6 has been reproduced.

## Data Processing & Preparation

### R759: Code has been written to one-hot encode the target labels, a...
- **Rubric ID**: 378d49a1-234b-41ad-9b04-f42dc4b1ef5a
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been written to one-hot encode the target labels, as described in Step 4 of Algorithm 1.
- **Parent context**: The LCA alignment loss has been implemented, as described in Algorithm 1.

## Dataset and Model Acquisition

### R760: Logic to load the checkpoints of all 36 VMs using the `torch...
- **Rubric ID**: da446952-be3f-4055-8fa1-5d55c6a4fdc2
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Logic to load the checkpoints of all 36 VMs using the `torchvision` module has been implemented.
- **Parent context**: All 36 Vision Models (VMs) are available to be queried.

### R761: Logic to load the checkpoints of all 39 VLMs using the `Open...
- **Rubric ID**: 83e9d518-be11-4315-842b-434512252335
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Logic to load the checkpoints of all 39 VLMs using the `OpenCLIP` (https://github.com/mlfoundations/open_clip) and CLIP (https://github.com/openai/CLIP) modules has been implemented.
- **Parent context**: All 39 Vision-Language Models (VLMs) are available to be queried.

### R762: Code to download the WordNet dataset has been written.
- **Rubric ID**: 04800542-0742-493d-bb7a-9dd1618bc4b4
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code to download the WordNet dataset has been written.
- **Parent context**: The WordNet dataset is available.

### R763: The WordNet dataset has been downloaded.
- **Rubric ID**: dc47354e-58c6-4124-98ff-3eb78b2d1953
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The WordNet dataset has been downloaded.
- **Parent context**: The WordNet dataset is available.

### R764: Code to download the in-distribution ImageNet dataset has be...
- **Rubric ID**: baeb4283-0ea1-4285-bdad-348ae6b47711
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code to download the in-distribution ImageNet dataset has been written.
- **Parent context**: The in-distribution (in-distribution) ImageNet dataset is available.

### R765: The in-distribution ImageNet dataset has been downloaded.
- **Rubric ID**: 5ed585a4-a860-4449-95b1-98f82119e943
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The in-distribution ImageNet dataset has been downloaded.
- **Parent context**: The in-distribution (in-distribution) ImageNet dataset is available.

### R766: Code to download the ImageNet-v2 dataset has been written.
- **Rubric ID**: 99095d00-4cb3-4883-99ca-c2b0c4f4a9ce
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code to download the ImageNet-v2 dataset has been written.
- **Parent context**: The ImageNet-v2 dataset is available.

### R767: The ImageNet-v2 dataset has been downloaded.
- **Rubric ID**: fed38aad-ecb2-4657-8e5f-c3e2a74c4e69
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The ImageNet-v2 dataset has been downloaded.
- **Parent context**: The ImageNet-v2 dataset is available.

### R768: Code to download the ImageNet-Sketch dataset has been writte...
- **Rubric ID**: b526562e-66e2-442a-8d2f-e03ab022f443
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code to download the ImageNet-Sketch dataset has been written.
- **Parent context**: The ImageNet-Sketch (ImageNet-S) dataset is available.

### R769: The ImageNet-Sketch dataset has been downloaded.
- **Rubric ID**: a01f454a-719f-45d4-a46d-20da7f6b6c0e
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The ImageNet-Sketch dataset has been downloaded.
- **Parent context**: The ImageNet-Sketch (ImageNet-S) dataset is available.

### R770: Code to download the ImageNet-Rendition dataset has been wri...
- **Rubric ID**: a0691fc4-f8c8-4363-a35c-ecacb8e9b09b
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code to download the ImageNet-Rendition dataset has been written.
- **Parent context**: The ImageNet-Rendition (ImageNet-R) dataset is available.

### R771: The ImageNet-Rendition dataset has been downloaded.
- **Rubric ID**: 4727aa07-853b-4838-bff8-da8694c39f3f
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The ImageNet-Rendition dataset has been downloaded.
- **Parent context**: The ImageNet-Rendition (ImageNet-R) dataset is available.

### R772: Code to download the ImageNet-Adversarial dataset has been w...
- **Rubric ID**: d9235995-2ba1-4218-af85-4d6db32b0508
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code to download the ImageNet-Adversarial dataset has been written.
- **Parent context**: The ImageNet-Adversarial (ImageNet-A) dataset is available.

### R773: The ImageNet-Adversarial dataset has been downloaded.
- **Rubric ID**: d3b10c98-dc0e-426b-ab8a-02e42c2c7c08
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The ImageNet-Adversarial dataset has been downloaded.
- **Parent context**: The ImageNet-Adversarial (ImageNet-A) dataset is available.

### R774: Code to download the ObjectNet dataset has been written.
- **Rubric ID**: a0698105-e5de-42e6-b32d-0605485291c1
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code to download the ObjectNet dataset has been written.
- **Parent context**: The ObjectNet dataset is available.

### R775: The ObjectNet dataset has been downloaded.
- **Rubric ID**: 53bb5699-ed93-4f13-bb0a-4ee168893599
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: The ObjectNet dataset has been downloaded.
- **Parent context**: The ObjectNet dataset is available.

## Logging, Analysis & Presentation

### R776: Code has been written to compute a line of best fit between...
- **Rubric ID**: d2777034-91ef-43c5-b4b1-462746ac6ea9
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to compute a line of best fit between ImageNet (in-distribution) Top-1 test accuracy and the Top-1 test accuracy on the out-of-distribution ObjectNet dataset.
- **Parent context**: A line of best fit has been computed between the Top-1 accuracy on the ImageNet test set (in-distrib...

### R777: A line of best fit has been computed between ImageNet (in-di...
- **Rubric ID**: 59e3b82c-5350-480d-8258-4b28a9e9122a
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between ImageNet (in-distribution) Top-1 test accuracy and the Top-1 test accuracy on the out-of-distribution ObjectNet dataset.
- **Parent context**: A line of best fit has been computed between the Top-1 accuracy on the ImageNet test set (in-distrib...

### R778: A line of best fit between the average LCA distance (using i...
- **Rubric ID**: 4910bf94-c7d6-462b-a1c0-febfc6bffd87
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: A line of best fit between the average LCA distance (using information content) on the ImageNet test set and the Top-1 test accuracy on the out-of-distribution ObjectNet dataset has been computed.
- **Parent context**: A line of best fit has been computed between the average LCA distance (using information content) on...

### R779: The saved Top-1 accuracies show that both CLIP_RN50 and CLIP...
- **Rubric ID**: 965d31d5-1615-4b1d-b877-88b07ba47219
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The saved Top-1 accuracies show that both CLIP_RN50 and CLIP_RN50x4 achieve lower Top-1 accuracy scores on the ImageNet test set than both ResNet18 and ResNet50.
- **Parent context**: Table 1 has been reproduced.

### R780: The saved results show that $R^2$ value of the in-distributi...
- **Rubric ID**: 3bf0c5ba-14e7-41ff-879e-3a7bdd0de95f
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The saved results show that $R^2$ value of the in-distribution average LCA distance (using information content) and out-of-distribution Top-1 test set accuracy is higher than the $R^2$ value of the in-distribution average Top-1 and out-of-distribution Top-1 test set accuracies for ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial and ObjectNet, but not ImageNet-v2.
- **Parent context**: Table 2 has been reproduced.

### R781: The saved results show that $R^2$ value of the in-distributi...
- **Rubric ID**: a20a080a-06d5-4d02-bea2-1f433635d2ec
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The saved results show that $R^2$ value of the in-distribution average LCA distance (using information content) and out-of-distribution Top-5 test set accuracy is higher than the $R^2$ value of the in-distribution average Top-1 and out-of-distribution Top-5 test set accuracies for ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial and ObjectNet, but not ImageNet-v2.
- **Parent context**: Table 2 has been reproduced.

### R782: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: ad30eeb1-3692-423e-8201-7e51db49d2e8
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R783: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: 0347b5e4-e8a9-4ca0-ad4b-9a677fc6d602
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Top-1 test set accuracy and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R784: A line of best fit has been computed between the average con...
- **Rubric ID**: 008e179d-e778-416f-b56d-df85836711fd
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-v2) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R785: A line of best fit has been computed between the average con...
- **Rubric ID**: 7c157751-d0c0-4af0-ad8a-8fb6eb89c603
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the average confidence on the in-distribution (ImageNet) test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the av...

### R786: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: cd987ebd-e29b-4311-86d7-8ecced5fb668
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) Aline-D scores on the test set and the out-of-distribution (ImageNet-A) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R787: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: 6fe1a978-bb1e-4eac-a0db-1595eae5c5c3
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-S) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R788: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: 7cce8201-881c-454e-a305-a774e33e4855
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ImageNet-R) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R789: A line of best fit has been computed between the in-distribu...
- **Rubric ID**: df65cd5e-50f4-4205-aafe-868d98607304
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: A line of best fit has been computed between the in-distribution (ImageNet) average LCA distance (using information content) on the test set and the out-of-distribution (ObjectNet) Top-1 test set accuracy for all 75 models.
- **Parent context**: The mean absolute error has been computed and saved for the linear regression model fitted to the in...

### R790: The saved mean absolute errors show that the LCA distance (u...
- **Rubric ID**: bb0e5670-acc2-4022-9afc-e6727c6e6d9c
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The saved mean absolute errors show that the LCA distance (using information content) achieves the lowest error for the ImageNet-S, ImageNet-A, and ObjectNet datasets.
- **Parent context**: Table 3 has been reproduced.

### R791: The saved mean absolute errors show that the LCA distance (u...
- **Rubric ID**: 14eed445-f0c6-423b-892a-a639405b309a
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The saved mean absolute errors show that the LCA distance (using information content) achieves the second lowest error for the ImageNet-R dataset.
- **Parent context**: Table 3 has been reproduced.

### R792: Code has been written to compute a line of best fit between...
- **Rubric ID**: 17ae5c6e-bbf5-46ee-9a1e-f6fc6332f96f
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to compute a line of best fit between ImageNet (in-distribution) Top-1 test accuracy and the Top-1 test accuracy on the out-of-distribution datasets: ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, and ObjectNet.
- **Parent context**: A line of best fit has been computed between ImageNet (in-distribution) Top-1 test accuracy and both...

### R793: Code has been written to compute a line of best fit between...
- **Rubric ID**: 41bf1c9a-dd8f-4a4d-8b8a-83934a1b038e
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to compute a line of best fit between ImageNet (in-distribution) Top-1 test accuracy and the Top-5 test accuracy on the out-of-distribution datasets: ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, and ObjectNet.
- **Parent context**: A line of best fit has been computed between ImageNet (in-distribution) Top-1 test accuracy and both...

### R794: Code has been written to compute a line of best fit between...
- **Rubric ID**: bbdd7184-d300-4f8c-8380-b5edbb049a14
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to compute a line of best fit between the average LCA distance (using information content) on the ImageNet test set and the Top-1 test accuracy on the out-of-distribution datasets: ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, and ObjectNet.
- **Parent context**: A line of best fit between the average LCA distance (using information content) on the ImageNet test...

### R795: A line of best fit between the average LCA distance (using i...
- **Rubric ID**: f5b56acd-5b5c-4768-b6ff-d9ee5e408104
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: A line of best fit between the average LCA distance (using information content) on the ImageNet test set and the Top-1 test accuracy on the out-of-distribution datasets (ImageNet-v2, ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial, and ObjectNet) has been computed.
- **Parent context**: A line of best fit between the average LCA distance (using information content) on the ImageNet test...

### R796: The slope of the line of best fit between the average LCA di...
- **Rubric ID**: c2f43bc3-5cb5-4d5d-837c-deeaf9c9b540
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The slope of the line of best fit between the average LCA distance (using information content) on the ImageNet test set (y-axis) and the Top-5 accuracy (x-axis) on the ObjectNet dataset is negative.
- **Parent context**: The slope of the line of best fit between the average LCA distance (using information content) on th...

### R797: The saved results show that the mean Pearson correlation bet...
- **Rubric ID**: 96623b45-6874-4928-a2c3-eba01d4b683c
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The saved results show that the mean Pearson correlation between the average LCA distance (using information content) (with respect to the latent hierarchies) on the ImageNet test set and the Top-1 accuracy on the out-of-distribution datasets is lower than the Pearson correlation between the average LCA distance (using information content) (with respect to the WordNet hierarchy) on the ImageNet test set and the Top-1 accuracy on the out-of-distribution datasets for ImageNet-Sketch, ImageNet-Rendition, ImageNet-Adversarial and ObjectNet, but not ImageNet-v2.
- **Parent context**: Table 4 has been reproduced.

### R798: The soft labels matrix has been saved for later use.
- **Rubric ID**: c4e5e526-5968-48fb-8fe5-143e81e2e465
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The soft labels matrix has been saved for later use.
- **Parent context**: The soft labels based on LCA distance using tree node depth and the WordNet hierarchy have been comp...

### R799: Sanity checks have been run on the resultant soft-label matr...
- **Rubric ID**: 5891eb11-7250-4099-b07a-e2d517f24faf
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Sanity checks have been run on the resultant soft-label matrix, as described in the addendum.
- **Parent context**: The soft labels based on LCA distance using tree node depth and the WordNet hierarchy have been comp...

### R800: The OpenCLIP(vit-l-14) model, $M$, has been used with the in...
- **Rubric ID**: ec6d4869-50ac-43ef-bed0-c8ca21016a45
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The OpenCLIP(vit-l-14) model, $M$, has been used with the in-distribution ImageNet image test set data $X$ and labels $Y$ to compute the average feature representation for each class.
- **Parent context**: A latent hierarchy produced with the OpenCLIP(vit-l-14) model has been computed using $k$-means clus...

### R801: Sanity checks have been run on the resultant soft-label matr...
- **Rubric ID**: 4cf37c13-07d1-47b5-ae0f-0d9d1c4a7b5d
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Sanity checks have been run on the resultant soft-label matrix, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

### R802: Code has been written to sanity check the resultant soft-lab...
- **Rubric ID**: a7193b21-3927-4fea-9789-1d057c2e597a
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: Code has been written to sanity check the resultant soft-label matrix, as described in the addendum.
- **Parent context**: Code has been written to compute the soft labels based on LCA distance (using node depth in the tree...

## Experimental Setup

### R803: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: 8cd7cc36-afbb-4691-ace3-419d780a3255
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a ResNet-18 backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the WordNet hierarchy.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set, a...

### R804: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: 029737d9-0481-46b8-a928-d46735e57aff
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a ResNet-50 backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the WordNet hierarchy.
- **Parent context**: An interpolated linear probe with a ResNet-50 backbone has been trained on the ImageNet train set, a...

### R805: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: 066be783-f37f-4b0c-89dd-df8697bd25d2
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a VIT-B backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the WordNet hierarchy.
- **Parent context**: An interpolated linear probe with a VIT-B backbone has been trained on the ImageNet train set, and h...

### R806: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: e61574de-0604-49d6-baf6-907cb593b7a3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a VIT-L backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the WordNet hierarchy.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R807: Code has been written find the $\alpha$ such that the interp...
- **Rubric ID**: c4a8428e-7da5-409e-bc8a-5c6f32bd3654
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written find the $\alpha$ such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ maximizes the Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ is varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a VIT-L backbone has been trained on the ImageNet train set, and h...

### R808: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: f3d64ba4-3848-4208-b29b-af0d753aa51d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a ConvNext backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the WordNet hierarchy.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R809: A value for $\alpha$ has been found such that the interpolat...
- **Rubric ID**: 78e5b6a0-93d8-49a9-b5e9-4d08b32cf79d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A value for $\alpha$ has been found such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ has maximal Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ has been varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a ConvNext backbone has been trained on the ImageNet train set, an...

### R810: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: e8f36ed3-e090-4f0e-a417-6b435198f454
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a Swin Transformer backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the WordNet hierarchy.
- **Parent context**: An interpolated linear probe with a Swin Transformer backbone has been trained on the ImageNet train...

### R811: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: d673ea89-1a41-43e9-ae57-ac711e746d06
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a ResNet-18 backbone by optimizing the probe using the cross entropy loss. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer.
- **Parent context**: A baseline linear probe trained with cross entropy has been trained and evaluated on all five out-of...

### R812: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: 5ff579f5-93b9-49c8-8415-23b86467a092
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a ResNet-18 backbone by optimizing the probe using the cross entropy loss. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer.
- **Parent context**: A baseline linear probe trained with cross entropy has been trained and evaluated on all five out-of...

### R813: Code has been written to train a linear probe on the ImageNe...
- **Rubric ID**: 72a49636-2934-4e67-8835-0dea2f2c028a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train a linear probe on the ImageNet train set with a ResNet-18 backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the latent hierarchy determined by MnasNet.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R814: Code has been written find the $\alpha$ such that the interp...
- **Rubric ID**: a9839c1c-a904-45ab-ae58-c86573a51e44
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written find the $\alpha$ such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ maximizes the Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ is varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R815: Code has been written find the $\alpha$ such that the interp...
- **Rubric ID**: 05b95451-4fce-49bc-b71e-38c7d50cb17f
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written find the $\alpha$ such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ maximizes the Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ is varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R816: A value for $\alpha$ has been found such that the interpolat...
- **Rubric ID**: d734bdee-f44f-4948-ab47-9620aeccca3b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A value for $\alpha$ has been found such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ has maximal Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ has been varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R817: A linear probe has been trained on the ImageNet train set wi...
- **Rubric ID**: 78542a61-1131-4209-89c6-88faba333407
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A linear probe has been trained on the ImageNet train set with a ResNet-18 backbone by optimizing the probe using the alignment loss, as described in Algorithm 1, with $\lambda = 0.03$, temperature $T$ set to 25, and alignment mode set to `CE`. The probe is a linear layer mapping the last hidden layer before the linear classifier (FC layer) to a 1000-dimension vector (corresponding to the 1000 classes in ImageNet) followed by a softmax layer. The soft labels used in the loss function are derived from the matrix $M_{\mathrm{LCA}} = \operatorname{Min} \operatorname{Max}(M^T)$, which is computed using the latent hierarchy determined by vit-1-14.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R818: Code has been written find the $\alpha$ such that the interp...
- **Rubric ID**: 2dc9215e-626e-4b64-bc3b-2ee77372f3bc
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written find the $\alpha$ such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ maximizes the Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ is varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...

### R819: A value for $\alpha$ has been found such that the interpolat...
- **Rubric ID**: a8cf4e7b-daab-460d-8811-9db915e2fdd8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: A value for $\alpha$ has been found such that the interpolated linear probe with parameters $\alpha W_{CE} + (1-\alpha)W_{CE+soft}$ has maximal Top-1 accuracy on the ImageNet validation set, where $W_{CE}$ denotes the trained weights from the probe optimized solely with cross entropy loss, and $W_{CE+soft}$ denotes the trained weights from the probe optimized with alignment loss. The hyperparameter $\alpha$ has been varied from $0$ to $1$ in step sizes of $0.1$.
- **Parent context**: An interpolated linear probe with a ResNet-18 backbone has been trained on the ImageNet train set us...
