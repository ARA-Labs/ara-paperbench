# Rubric Requirements — all-in-one
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 174

## Method Implementation

### R01: The drift term for Variance Exploding SDE is defined as $f(x...
- **Rubric ID**: 0ac16f05-bdb9-48c8-9103-764068f5301a
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: The drift term for Variance Exploding SDE is defined as $f(x, t)=0$
- **Parent context**: Variance Exploding SDE (VESDE) is implemented, as described in A2.1

### R02: The diffusion term for Variance Exploding SDE is defined as...
- **Rubric ID**: 1402caf0-ee17-48a4-b0f5-ee4523807747
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: The diffusion term for Variance Exploding SDE is defined as $g(t)=\sigma_{min} \cdot (\frac{\sigma_{max}}{\sigma_{min}})^t \cdot \sqrt{2 \log \frac{\sigma_{max}}{\sigma_{min}}}$
- **Parent context**: Variance Exploding SDE (VESDE) is implemented, as described in A2.1

### R03: The perturbation kernel for the Variance Exploding SDE is de...
- **Rubric ID**: 396c0b27-9d8c-49d4-a9e8-667b7c1a9e5c
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: The perturbation kernel for the Variance Exploding SDE is defined as $p(x_t|x_0) = \mathcal{N}(x_t, x_t, \sigma(t)I)$ where $\sigma(t) = \sigma_{min}^2\left( \frac{\sigma_{max}}{\sigma_{min}} \right)^{2t}$
- **Parent context**: Variance Exploding SDE (VESDE) is implemented, as described in A2.1

### R04: Each unique variable has an integer identifier. Multiple obs...
- **Rubric ID**: 437abe9f-4b33-4293-9c64-d9cf83fd2a55
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Each unique variable has an integer identifier. Multiple observations of the same variable share the same identifier
- **Parent context**: The tokenizer correctly tokenizes and embeds the identifiers

### R05: The tokenizer uses learnable vector embeddings to embed each...
- **Rubric ID**: 714bdd7e-b21c-4407-aa3d-f50307633bb4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The tokenizer uses learnable vector embeddings to embed each identifier
- **Parent context**: The tokenizer correctly tokenizes and embeds the identifiers

### R06: The embedding for a single value is created by repeating the...
- **Rubric ID**: af5cd308-83c7-4b2b-bc9f-b006183ea3ed
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The embedding for a single value is created by repeating the scalar value to match the desired dimensionality. For example, to embed the value 1 to desired dimensionality N, we would have a vector [1, 1, ...., 1] of length N
- **Parent context**: The tokenizer for the Simformer has been implemented

### R07: The tokenizer correctly tokenizes and embeds the metadata (i...
- **Rubric ID**: 2e46fc8d-2ecb-46f3-86b1-0c80fceec733
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The tokenizer correctly tokenizes and embeds the metadata (if required); the tokenizer applies a learnable linear mapping of a random Fourier embedding of the elements in the index set to the desired dimensionality.
- **Parent context**: The tokenizer for the Simformer has been implemented

### R08: The tokenizer uses learnable vector embeddings to embed each...
- **Rubric ID**: 2ff0a481-00b4-47e9-939a-4dd7f7a00361
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The tokenizer uses learnable vector embeddings to embed each value in a condition state - "True" values are mapped to a shared learnable vector embedding, whereas "False" values are mapped to zeros (of the desired dimensionality)
- **Parent context**: The tokenizer for the Simformer has been implemented

### R09: For each input, the tokenizer concatenates the embeddings of...
- **Rubric ID**: 407dcc3b-5f84-48b4-b5e5-730336b97fbe
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For each input, the tokenizer concatenates the embeddings of the identifier, value, metadata (if used), and condition state in that order
- **Parent context**: The tokenizer for the Simformer has been implemented

### R10: The tokenizer takes inputs: a sequence of scalar values, a s...
- **Rubric ID**: c6eb15a5-65f9-4ac9-9927-f50f3118d8fe
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The tokenizer takes inputs: a sequence of scalar values, a sequence of integer variable identifiers, a condition mask $M_C$, and optional metadata if required. It embeds these inputs into a sequence of tokens, each of equal dimensionality
- **Parent context**: The tokenizer for the Simformer has been implemented

### R11: The Simformer model is a slightly modified vanilla encoder-o...
- **Rubric ID**: 09008e24-26e7-4aa9-8d9a-881feb20538f
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: The Simformer model is a slightly modified vanilla encoder-only transformer following the implementation proposed by (Vaswani et al., 2017). The only modification is that the decoder is a single linear layer that produces a single scalar score for each variable token in the input sequence. The Simformer model is described in Section 3, Figure 2, and Appendix A.1
- **Parent context**: The Simformer architecture has been implemented

### R12: Diffusion time is embedded as a random Gaussian Fourier embe...
- **Rubric ID**: b1b80f04-e17c-49f6-831c-3cd3d15acf26
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Diffusion time is embedded as a random Gaussian Fourier embedding, and a linear projection of diffusion time is added to the output of each feed-forward block in the transformer
- **Parent context**: The Simformer architecture has been implemented

### R13: The Simformer takes inputs: the diffusion time $t$, a sequen...
- **Rubric ID**: 25eecc1a-cc2c-48e5-addc-082fdb7f638b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The Simformer takes inputs: the diffusion time $t$, a sequence of tokens from the tokenizer, and an attention mask. These are projected to a sequence of scalar outputs, representing the marginal scores of the diffusion process at time $t$.
- **Parent context**: The Simformer architecture has been implemented

### R14: During training, for each training sample, the condition mas...
- **Rubric ID**: be65afa3-69f8-4f5a-8b0a-a2f7895b0b85
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: During training, for each training sample, the condition mask $M_C$ is randomly sampled as either 1) the joint distribution, where $M_C=[0, 0, ..., 0]$, 2) the posterior distribution where data variables are observed and parameters are unobserved, 3) the likelihood function where data variables are unobserved and parameter variables are observed, 4) a Bernoulli distribution with p=0.3 (resampled for each element), 5) a Bernoulli distribution with p=0.7 (resampled for each element)
- **Parent context**: The condition and attention masks are correctly computed for each sample passed to the Simformer

### R15: $M_E$ is selected to be undirected, directed, or fully dense
- **Rubric ID**: 3e515973-3a59-46ca-b0b6-be1d8b4fea96
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: $M_E$ is selected to be undirected, directed, or fully dense
- **Parent context**: The attention mask $M_E$ is correctly computed for each sample passed to the Simformer

### R16: If $M_E$ is selected to be fully dense, every token is allow...
- **Rubric ID**: 8e07cc4f-6176-4391-a8bb-578831aa3aa4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: If $M_E$ is selected to be fully dense, every token is allowed to attend to every other token
- **Parent context**: The attention mask $M_E$ is correctly computed for each sample passed to the Simformer

### R17: For both undirected and directed cases, the attention mask $...
- **Rubric ID**: 08a90ef1-cf86-4bfa-b17a-9269e223a57e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For both undirected and directed cases, the attention mask $M_E$ is computed to capture the known dependencies of the current task. Specifically, each task provides $M_E$ as given by the adjacency matrix of a directed/undirected graphical model with the diagonal set to True.
- **Parent context**: The attention mask $M_E$ is correctly computed for the undirected and directed cases

### R18: If $M_E$ is directed it must be updated for a given $M_C$. T...
- **Rubric ID**: 6f05f0cf-c61a-4ad9-b2b0-a353b7cab492
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: If $M_E$ is directed it must be updated for a given $M_C$. The algorithm proposed by Webb at al. (2018) is used to add the minimal number of edges required to represent additional dependencies from conditioning as specified in $M_C$
- **Parent context**: The attention mask $M_E$ is correctly computed for the undirected and directed cases

### R19: A diffusion model loss is used that targets (un)conditional...
- **Rubric ID**: 0e335268-1035-4b34-b99c-97054665db5c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: A diffusion model loss is used that targets (un)conditional marginal score $\nabla_{\mathbf{x}_t^{\text{unobserved}}}\,\log p_t(\mathbf{x}_t^{\text{unobserved}} \mid \mathbf{x}^{\text{observed}})$ as defined by the condition mask $M_C$ and p(x).
- **Parent context**: The loss function for the Simformer is correctly defined

### R20: As defined in Section 3.3, for each (partially) noisy traini...
- **Rubric ID**: b3e915ef-1f57-4b70-b3da-546947d6c1b5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: As defined in Section 3.3, for each (partially) noisy training sample $\hat{x}_t^{M_c}$, the Simformer loss is defined as: $\ell(\phi, M_C, t, \hat{\mathbf{x}}_0, \hat{\mathbf{x}}_t) = (1-M_C)\cdot \left(s_\phi^{M_E}(\hat{\mathbf{x}}_t^{M_C}, t) - \nabla_{\hat{\mathbf{x}}_t} \log p_t(\hat{\mathbf{x}}_t|\hat{\mathbf{x}}_0)\right)$, where $s_\phi^{M_E}$ denotes the score model equipped with a specific attention mask $M_E$
- **Parent context**: The loss function for the Simformer is correctly defined

### R21: The Simformer loss is only computed over samples that are un...
- **Rubric ID**: e3cd228e-467b-4c47-a23d-6e212249115e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The Simformer loss is only computed over samples that are unobserved, i.e., they have a value of 0 in $M_C$
- **Parent context**: The loss function for the Simformer is correctly defined

### R22: The total Simformer loss per mini-match is given by a weight...
- **Rubric ID**: 2cb4d86f-19c4-438f-b6f1-52c588ba9d09
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The total Simformer loss per mini-match is given by a weighted sum, as given by a positive weighting function $\lambda(t)$ e.g. $\lambda(t)=g(t)^2$ where $g(t)$ is the diffusion coefficient of the VESDE.
- **Parent context**: The loss function for the Simformer is correctly defined

### R23: When performing inference using Simformer, the reverse diffu...
- **Rubric ID**: 79df6718-c5e7-4967-92b0-4a66d1e8998e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When performing inference using Simformer, the reverse diffusion process is run on all unobserved variables. Observed variables are kept constant at their initial values
- **Parent context**: Code for sampling arbitrary conditionals from a trained Simformer model has been implemented

### R24: Euler-Maruyama discretization has been implemented to run th...
- **Rubric ID**: 7c953e3a-a3ec-4c91-a897-c6691ed60a80
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Euler-Maruyama discretization has been implemented to run the diffusion process backward for Simformer
- **Parent context**: Euler-Maruyama discretization has been implemented to run the diffusion process backward

### R25: For conditioning on intervals, the self-recurrence is implem...
- **Rubric ID**: 386472cc-f299-4e46-89c9-95e9b9a4addf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For conditioning on intervals, the self-recurrence is implemented such that a mutable hyperparameter $r$ specifies how many times future points undergo a forward diffusion step followed by a reverse step, incrementally refining each sample.
- **Parent context**: Algorithm 1 has been implemented such that conditioning on intervals can optionally be selected

### R26: For conditioning on intervals, the constraint function is de...
- **Rubric ID**: 39362fd2-1f41-4f81-97ec-ce3c1e893502
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For conditioning on intervals, the constraint function is defined as $c(\hat{x}) = \hat{x} - u$, where $u$ is a mutable hyperparameter
- **Parent context**: Algorithm 1 has been implemented such that conditioning on intervals can optionally be selected

### R27: For conditioning on intervals, the scaling function $s(t)$ i...
- **Rubric ID**: 091fd46a-e09e-4989-986b-2a14ba8b6e25
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For conditioning on intervals, the scaling function $s(t)$ is defined as $s(t)=\frac{1}{\sigma(t)^2)|$, i.e., inversely proportional to the variance
- **Parent context**: Algorithm 1 has been implemented such that conditioning on intervals can optionally be selected

### R28: Algorithm 1 has been fully implemented to sample from condit...
- **Rubric ID**: 58d5bd8c-e8c0-41d7-aa31-684e0e0ddc61
- **Category**: Code Development / Method Implementation
- **Weight**: 3
- **Requirement**: Algorithm 1 has been fully implemented to sample from conditions specified by the constraint function.
- **Parent context**: Algorithm 1 has been implemented such that conditioning on intervals can optionally be selected

### R29: Conditioning on intervals can optionally be used when sampli...
- **Rubric ID**: f5b9aa3e-f51e-4071-ad3c-fa381e0c060b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Conditioning on intervals can optionally be used when sampling
- **Parent context**: The Simformer supports conditioning on intervals.

### R30: The sbi library (Tejero-Cantero et al., 2020) is used to imp...
- **Rubric ID**: ad5f1aac-30cc-425c-bc8a-409a58a71447
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: The sbi library (Tejero-Cantero et al., 2020) is used to implement NPE, NRE, and NLE. Default parameters from the library are used, aside from using a more expressive neural spine flow for NPE and NLE
- **Parent context**: Baseline methods Neural Posterior Estimation (NPE), Neural Ratio Estimation (NRE), and Neural Likeli...

### R31: N Markov chains with samples are initialized from the joint...
- **Rubric ID**: 9fa888e9-7fb0-4a65-8322-e26c7a021143
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: N Markov chains with samples are initialized from the joint distribuiton
- **Parent context**: For Two Moons, the method to obtain N reference samples for a possible conditional can be computed

### R32: Only the last samples of each chain are considered, yielding...
- **Rubric ID**: 92486973-e7a9-4da9-8a38-556e3bae3dd9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Only the last samples of each chain are considered, yielding N reference samples
- **Parent context**: For Two Moons, the method to obtain N reference samples for a possible conditional can be computed

### R33: N Markov chains with samples are initialized from the joint...
- **Rubric ID**: af3a4299-578a-4cdd-abb6-021e5c1f5c7d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: N Markov chains with samples are initialized from the joint distribuiton
- **Parent context**: For SLCP, the method to obtain N reference samples for a possible conditional can be computed

### R34: 600 steps of a random direction slice sampling algorithm are...
- **Rubric ID**: 028a6cbe-387e-456d-941c-0c4a4b970dd5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: 600 steps of a random direction slice sampling algorithm are run
- **Parent context**: For SLCP, the method to obtain N reference samples for a possible conditional can be computed

### R35: An additional 2000 steps of Metropolis-Hastings Markov Chain...
- **Rubric ID**: 1e941abb-e1d9-4f91-958c-db60dad4c82e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: An additional 2000 steps of Metropolis-Hastings Markov Chain Monte Carlo (MHMCMC) are run with step size of 0.1
- **Parent context**: For SLCP, the method to obtain N reference samples for a possible conditional can be computed

### R36: Only the last samples of each chain are considered, yielding...
- **Rubric ID**: 0051bf87-8706-4531-9b1d-00bbb499d8e4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Only the last samples of each chain are considered, yielding N reference samples
- **Parent context**: For SLCP, the method to obtain N reference samples for a possible conditional can be computed

### R37: N Markov chains with samples are initialized from the joint...
- **Rubric ID**: acc664bc-89fb-4b2d-8813-330dc6a109b7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: N Markov chains with samples are initialized from the joint distribution
- **Parent context**: For Tree, the method to obtain N reference samples for a possible conditional can be computed

### R38: 5000 steps of a HMC sampler is run
- **Rubric ID**: 35e0a7bf-ddf7-429e-a1e3-a298bffcc301
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: 5000 steps of a HMC sampler is run
- **Parent context**: For Tree, the method to obtain N reference samples for a possible conditional can be computed

### R39: Only the last samples of each chain are considered, yielding...
- **Rubric ID**: 462ad866-65cb-4e08-bbd4-83dd471d9358
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Only the last samples of each chain are considered, yielding N reference samples
- **Parent context**: For Tree, the method to obtain N reference samples for a possible conditional can be computed

### R40: N Markov chains with samples are initialized from the joint...
- **Rubric ID**: 52f952b5-752a-4f30-9b53-edd0a3543361
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: N Markov chains with samples are initialized from the joint distribution
- **Parent context**: For HMM, the method to obtain N reference samples for a possible conditional can be computed

### R41: Only the last samples of each chain are considered, yielding...
- **Rubric ID**: bc5f359e-8302-4a9d-a617-6e3312aea9cc
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Only the last samples of each chain are considered, yielding N reference samples
- **Parent context**: For HMM, the method to obtain N reference samples for a possible conditional can be computed

### R42: For Lotka-Volterra, inference is performed for the full time...
- **Rubric ID**: bcf546a2-f0a7-42e5-9956-3bc18b67483a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: For Lotka-Volterra, inference is performed for the full time-series and the implementation doesn't rely on summary statistics.
- **Parent context**: The Lotka Volterra task is prepared, as described in A2.2

### R43: In the SIRD task, for the time-dependent contact rate, $\hat...
- **Rubric ID**: 22bc638a-ddbe-40f5-9de2-4436b28f62bf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In the SIRD task, for the time-dependent contact rate, $\hat{\beta} \sim \mathcal{G}(0, k)$ is first sampled from a gaussian prior with $k$ representing an RBF kernel defined as $k(t_1, t_2) = 2.5^2 \exp\left(-\frac{1}{2} \frac{\|t_1 - t_2\|^2}{7^2}\right)$, then is transformed via a sigmoid function
- **Parent context**: The SIRD task is prepared, as described in A2.2

### R44: In the SIRD task, the contact rate is implemented to vary ov...
- **Rubric ID**: 4332dc3c-76d7-4b84-b317-35e82990b266
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In the SIRD task, the contact rate is implemented to vary over time, whereas the recovery and death rate are constant in time.
- **Parent context**: The SIRD task is prepared, as described in A2.2

### R45: In the SIRD task, observational data is modeled with log-nor...
- **Rubric ID**: 19f4319f-3056-4264-8fe4-3b4d13fe7a27
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In the SIRD task, observational data is modeled with log-normal noise with a mean of $S(t)$ and a standard deviation of $\sigma=0.05$
- **Parent context**: The SIRD task is prepared, as described in A2.2

### R46: In the Hodgkin-Huxley task, the rate functions as defined fo...
- **Rubric ID**: 57d03e3d-386c-4163-9945-428714362bfd
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In the Hodgkin-Huxley task, the rate functions as defined following the equations in A2.2
- **Parent context**: The Hodgkin-Huxley task is prepared, as described in A2.2

### R47: In all Simformers, the random Gaussian Fourier embedding use...
- **Rubric ID**: da87d682-3f30-443c-b318-8bb158048285
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In all Simformers, the random Gaussian Fourier embedding used in the tokenizer to embed metadata objects has 128 dimensions (if required)
- **Parent context**: The hyperparameters for Simformer stated in Section A.2.1 are used in all experiments, unless otherw...

### R48: In all Simformers, the random Gaussian Fourier embedding use...
- **Rubric ID**: 5963d717-2765-4535-80d8-8a92a9052a21
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In all Simformers, the random Gaussian Fourier embedding used for diffusion time has 256 dimensions
- **Parent context**: The hyperparameters for Simformer stated in Section A.2.1 are used in all experiments, unless otherw...

### R49: In all Simformers, the feed-forward block expands to a hidde...
- **Rubric ID**: 85db9bf8-1b9c-4d82-8b53-1813b1d31b3a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In all Simformers, the feed-forward block expands to a hidden dimension of 150.
- **Parent context**: The hyperparameters for Simformer stated in Section A.2.1 are used in all experiments, unless otherw...

### R50: Simformers used for all experiments in Section 4.1 have 6 la...
- **Rubric ID**: 237efc4f-17f7-4078-b987-802bebdefa43
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Simformers used for all experiments in Section 4.1 have 6 layers
- **Parent context**: The recorded metrics show that the results in section 4.1 have been replicated

### R51: For the SLCP task, samples for ten ground-truth posteriors a...
- **Rubric ID**: 8f6a3486-8f4c-4c48-ab4f-9e0e8f16bf13
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: For the SLCP task, samples for ten ground-truth posteriors are obtained
- **Parent context**: For each task Linear Gaussian, Mixture Gaussian, Two Moons, SLCP, samples for ten ground-truth poste...

### R52: For the Mixture Gaussian task, for each model trained for 10...
- **Rubric ID**: 157423ff-ee2b-437e-b2ca-bcec8d433b3b
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: For the Mixture Gaussian task, for each model trained for 10^3, 10^4, and 10^5 simulations, N posterior samples are generated from the 10 different reference observations, where N is the number of reference samples
- **Parent context**: For each task Linear Gaussian, Mixture Gaussian, Two Moons, SLCP, for each model trained for 10^3, 1...

### R53: For the Two Moons task, ground truth posterior samples with...
- **Rubric ID**: 409deb4c-dab8-4430-ac6d-9ca3026707e3
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: For the Two Moons task, ground truth posterior samples with Markov-Chain Monte-Carlo are generated on 100 randomly sampled selected conditional or full joint distributions
- **Parent context**: For each task Tree, HMM, Two Moons, and SLCP, ground truth posterior samples with Markov-Chain Monte...

### R54: For the SLCP task, ground truth posterior samples with Marko...
- **Rubric ID**: c2239ebc-0b8c-4651-9561-353cc0db8ce2
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: For the SLCP task, ground truth posterior samples with Markov-Chain Monte-Carlo are generated on 100 randomly sampled selected conditional or full joint distributions
- **Parent context**: For each task Tree, HMM, Two Moons, and SLCP, ground truth posterior samples with Markov-Chain Monte...

### R55: For the Tree task, for each model trained for 10^3, 10^4, an...
- **Rubric ID**: 77fa71bf-bb82-4bfc-b03b-428b37278f91
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: For the Tree task, for each model trained for 10^3, 10^4, and 10^5 simulations, for each of the ground truth posterior samples, N model-generated posteriors are created by conditioning on the observations, where N is the number of reference samples
- **Parent context**: For each task Tree, HMM, Two Moons, and SLCP, for each model trained for 10^3, 10^4, and 10^5 simula...

### R56: For the HMM task, for each model trained for 10^3, 10^4, and...
- **Rubric ID**: 913b099a-e731-4a8a-8a91-ccfb4ef5e650
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: For the HMM task, for each model trained for 10^3, 10^4, and 10^5 simulations, for each of the ground truth posterior samples, N model-generated posteriors are created by conditioning on the observations, where N is the number of reference samples
- **Parent context**: For each task Tree, HMM, Two Moons, and SLCP, for each model trained for 10^3, 10^4, and 10^5 simula...

### R57: The Simformer used for all experiments in Section 4.2 has 8...
- **Rubric ID**: aa888ef9-bcd4-429d-801b-c0ec0b989e57
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The Simformer used for all experiments in Section 4.2 has 8 layers
- **Parent context**: The recorded metrics show that the results in section 4.2 have been replicated

### R58: The Simformer used for all experiments in Section 4.3 has 8...
- **Rubric ID**: a0b66551-0aea-443f-8936-bc8db21c949b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The Simformer used for all experiments in Section 4.3 has 8 layers
- **Parent context**: The recorded metrics show that the results in section 4.3 have been replicated

### R59: The Simformer used in Section 4.3 uses the dense attention m...
- **Rubric ID**: e0c85d33-977f-4839-b149-312cdfcd5b34
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The Simformer used in Section 4.3 uses the dense attention mask
- **Parent context**: The recorded metrics show that the results in section 4.3 have been replicated

### R60: The predicted mean of the death population intercepts the sy...
- **Rubric ID**: 296dadfa-105d-4e23-aedd-9ce6cde8836b
- **Category**: Result Analysis / Method Implementation
- **Weight**: 2
- **Requirement**: The predicted mean of the death population intercepts the synthetic observation, using the Simformer given the five synthetic observations
- **Parent context**: Results for the Simformer accurately sampling parameter-conditioned posterior distributions have bee...

### R61: The Simformer used for all experiments in Section 4.4 has 8...
- **Rubric ID**: 4dce6753-f211-4e45-9f86-152ab3367ccb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The Simformer used for all experiments in Section 4.4 has 8 layers
- **Parent context**: The recorded metrics show that the results in section 4.4 have been replicated

### R62: The Simformer used in Section 4.4 uses the dense attention m...
- **Rubric ID**: c9544022-72fb-4e87-977f-84731c412783
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The Simformer used in Section 4.4 uses the dense attention mask
- **Parent context**: The recorded metrics show that the results in section 4.4 have been replicated

### R63: The Simformer infers the posterior distribution given only t...
- **Rubric ID**: 2b3aaed1-0d47-4fe4-96df-73b1b8c34c8a
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: The Simformer infers the posterior distribution given only the summary statistics of the voltage (not the energy)
- **Parent context**: Results when inferring the posterior distribution given only the summary statistics have been replic...

### R64: Posterior predictive samples are generated from this new pos...
- **Rubric ID**: 31d0cc76-b73b-4fad-9656-2dda0419e095
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: Posterior predictive samples are generated from this new posterior (via Simformer and by running the simulation), where this "new posterior" is generated given voltage summary statistics
- **Parent context**: Results when inferring the posterior distribution given only the summary statistics have been replic...

### R65: Simformer with guided diffusion is used to infer the posteri...
- **Rubric ID**: 0a2964da-9bad-44c6-8a6d-b107b6522463
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: Simformer with guided diffusion is used to infer the posterior given voltage summary statistics and the constraint on energy consumption
- **Parent context**: Results when applying an observation interval have been replicated

### R66: Posterior predictive samples are generated from this new pos...
- **Rubric ID**: 3c812e66-c1b1-4298-a078-797fd5516d68
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: Posterior predictive samples are generated from this new posterior (via Simformer and by running the simulation), where this "new posterior" is generated given voltage summary statistics and the constraint on energy consumption
- **Parent context**: Results when applying an observation interval have been replicated

## Experimental Setup

### R67: The constant $\sigma_{max}$ for VESDE is set to 15
- **Rubric ID**: 07f7aac1-c623-46e0-b7cc-3991331cbd9c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The constant $\sigma_{max}$ for VESDE is set to 15
- **Parent context**: Variance Exploding SDE (VESDE) is implemented, as described in A2.1

### R68: The constant $\sigma_{min}$ for VESDE is set to 0.0001
- **Rubric ID**: c6cd56ae-e565-4512-978e-80a8afaae037
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The constant $\sigma_{min}$ for VESDE is set to 0.0001
- **Parent context**: Variance Exploding SDE (VESDE) is implemented, as described in A2.1

### R69: In VESDE, samples are drawn from the time interval [1e-5, 1]
- **Rubric ID**: ac3759f1-14f6-4859-a64f-84db470eb2db
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In VESDE, samples are drawn from the time interval [1e-5, 1]
- **Parent context**: Variance Exploding SDE (VESDE) is implemented, as described in A2.1

### R70: When training the Simformer, for each training sample $\hat{...
- **Rubric ID**: 34b6fc70-d083-4bef-986e-336b09845a3c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: When training the Simformer, for each training sample $\hat{x}_0$, the noise level $t$ is sampled in the range [1e-5, 1] to generate a (partially) noisy sample $\hat{\mathbf{x}}_t^{M_C} = (1 - M_C) \cdot \hat{\mathbf{x}}_t + M_C \cdot \hat{\mathbf{x}}_0$ i.e. variables that we want to condition on remain clean.
- **Parent context**: The code for training the Simformer model has been implemented

### R71: 500 steps are used in the Euler-Maruyama discretization proc...
- **Rubric ID**: 23d6d4c9-f750-4f5d-8965-b9c2277d5c6a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: 500 steps are used in the Euler-Maruyama discretization process for Simformer
- **Parent context**: Euler-Maruyama discretization has been implemented to run the diffusion process backward

### R72: Each method NPE, NRE, and NLE is trained using the provided...
- **Rubric ID**: ee41ea7c-8c0f-4f87-95cc-a1f2258596a6
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Each method NPE, NRE, and NLE is trained using the provided training loop (e.g. sbi.SNPE().train())
- **Parent context**: Baseline methods Neural Posterior Estimation (NPE), Neural Ratio Estimation (NRE), and Neural Likeli...

### R73: Each method NPE, NRE and NLE uses a batch size of 1000
- **Rubric ID**: 31ed240f-4e9c-489b-89ae-6ed46a85e8d8
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Each method NPE, NRE and NLE uses a batch size of 1000
- **Parent context**: Baseline methods Neural Posterior Estimation (NPE), Neural Ratio Estimation (NRE), and Neural Likeli...

### R74: Each method NPE, NRE and NLE uses the Adam optimizer
- **Rubric ID**: 6a1ddafa-29df-4e46-bc3e-71236a0b7d76
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Each method NPE, NRE and NLE uses the Adam optimizer
- **Parent context**: Baseline methods Neural Posterior Estimation (NPE), Neural Ratio Estimation (NRE), and Neural Likeli...

### R75: Early stopping is used to stop training early depending on v...
- **Rubric ID**: 56dcd071-8f39-4131-97cd-f6d011e99cf5
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Early stopping is used to stop training early depending on validation loss
- **Parent context**: Baseline methods Neural Posterior Estimation (NPE), Neural Ratio Estimation (NRE), and Neural Likeli...

### R76: 1000 steps of a random direction slice sampling algorithm ar...
- **Rubric ID**: ed3ab4fa-52b1-4328-8d90-988292d02e8f
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: 1000 steps of a random direction slice sampling algorithm are run
- **Parent context**: For Two Moons, the method to obtain N reference samples for a possible conditional can be computed

### R77: An additional 3000 steps of Metropolis-Hastings Markov Chain...
- **Rubric ID**: e4d0c4d5-593a-432a-b5f7-6216655ab5f5
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: An additional 3000 steps of Metropolis-Hastings Markov Chain Monte Carlo (MHMCMC) are run with step size of 0.01
- **Parent context**: For Two Moons, the method to obtain N reference samples for a possible conditional can be computed

### R78: 5000 steps of a HMC sampler is run
- **Rubric ID**: 293a5a7e-aa99-420c-9af6-9c47e07bedb3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: 5000 steps of a HMC sampler is run
- **Parent context**: For HMM, the method to obtain N reference samples for a possible conditional can be computed

### R79: In the Lotka Volterra task, to each simulation, Gaussian obs...
- **Rubric ID**: efe8edda-ebfa-4363-b13a-28bcb3d95ae3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In the Lotka Volterra task, to each simulation, Gaussian observation noise is added with $\sigma=0.1$
- **Parent context**: The Lotka Volterra task is prepared, as described in A2.2

### R80: In the SIRD task, a uniform prior is imposed on the global v...
- **Rubric ID**: 6c80714a-4f4e-4cae-9792-9fff064e4e5f
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In the SIRD task, a uniform prior is imposed on the global variables $\gamma, \delta$ denoted as $\gamma, \delta \sim \text{Unif}(0, 0.5)$
- **Parent context**: The SIRD task is prepared, as described in A2.2

### R81: In the Hodgkin-Huxley task, the initial membrane voltage is...
- **Rubric ID**: 4884d911-0bd8-4a99-a4a5-2721b7185072
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In the Hodgkin-Huxley task, the initial membrane voltage is established at $V_0=-65.0mV$
- **Parent context**: The Hodgkin-Huxley task is prepared, as described in A2.2

### R82: In the Hodgkin-Huxley task, simulations are conducted over a...
- **Rubric ID**: 548511a5-0bfe-451b-8c1d-3b2ecc5693bd
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In the Hodgkin-Huxley task, simulations are conducted over a duration of 200ms
- **Parent context**: The Hodgkin-Huxley task is prepared, as described in A2.2

### R83: In the Hodgkin-Huxley task, an input current of 4mA is appli...
- **Rubric ID**: 688df55a-5c45-4a79-8f1f-0aff770d4167
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In the Hodgkin-Huxley task, an input current of 4mA is applied in the interval between 50ms and 150ms
- **Parent context**: The Hodgkin-Huxley task is prepared, as described in A2.2

### R84: The classifier is a random forest classifier with 100 trees
- **Rubric ID**: 982f7456-e34d-40be-a4a9-76c32826d301
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The classifier is a random forest classifier with 100 trees
- **Parent context**: The C2ST metric has been implemented

### R85: All Simformers have a token dimension of 50
- **Rubric ID**: cdf1bfdd-53dd-420a-83f6-0a110ba9d765
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All Simformers have a token dimension of 50
- **Parent context**: The hyperparameters for Simformer stated in Section A.2.1 are used in all experiments, unless otherw...

### R86: All Simformers have 4 heads
- **Rubric ID**: e9edc2a0-3809-4e69-b9b6-1686b2955aa9
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: All Simformers have 4 heads
- **Parent context**: The hyperparameters for Simformer stated in Section A.2.1 are used in all experiments, unless otherw...

### R87: In all Simformers, the dimensionality of the key, query and...
- **Rubric ID**: 32e4ef3f-9fdc-4845-a2ac-7c988141c039
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In all Simformers, the dimensionality of the key, query and value is 10
- **Parent context**: The hyperparameters for Simformer stated in Section A.2.1 are used in all experiments, unless otherw...

### R88: In all Simformers, a batch size of 1000 is used
- **Rubric ID**: b18e9e5a-0079-420f-9222-4380004418ef
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In all Simformers, a batch size of 1000 is used
- **Parent context**: The hyperparameters for Simformer stated in Section A.2.1 are used in all experiments, unless otherw...

### R89: The Adam optimizer is used to train all Simformers
- **Rubric ID**: 831ca2ca-49a9-46c0-a63a-a39c877050a5
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The Adam optimizer is used to train all Simformers
- **Parent context**: The hyperparameters for Simformer stated in Section A.2.1 are used in all experiments, unless otherw...

### R90: Variance Exploding SDE (VESDE) is used to train the Simforme...
- **Rubric ID**: 7ec03b27-0737-4e4a-9581-bc4720744a1a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Variance Exploding SDE (VESDE) is used to train the Simformer in all experiments
- **Parent context**: The recorded metrics show that the results from section 4 are replicated

### R91: For the Linear Gaussian task, NPE has been trained for 10^3,...
- **Rubric ID**: bc21d6d1-49a5-45d0-93cc-cb42241275b4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Linear Gaussian task, NPE has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Linear Gaussian task, each of the following models have been trained for 10^3, 10^4, and 10^...

### R92: For the Linear Gaussian task, Simformer (with a dense attent...
- **Rubric ID**: 71d1e184-3e0e-46da-883c-c8a55244c3b5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Linear Gaussian task, Simformer (with a dense attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Linear Gaussian task, each of the following models have been trained for 10^3, 10^4, and 10^...

### R93: For the Linear Gaussian task, Simformer (with an undirected...
- **Rubric ID**: 3628b28c-b00b-458e-8e1d-1ac6f5e47411
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Linear Gaussian task, Simformer (with an undirected graph for it's attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Linear Gaussian task, each of the following models have been trained for 10^3, 10^4, and 10^...

### R94: For the Linear Gaussian task, Simformer (with a directed gra...
- **Rubric ID**: 8f4524fc-48f5-4615-bd33-aedc2aa58d3a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Linear Gaussian task, Simformer (with a directed graph for it's attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Linear Gaussian task, each of the following models have been trained for 10^3, 10^4, and 10^...

### R95: For the Mixture Gaussian task, NPE has been trained for 10^3...
- **Rubric ID**: 174cb2a9-b358-4ca7-86e0-ea85ac02cc93
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Mixture Gaussian task, NPE has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Mixture Gaussian task, each of the following models have been trained for 10^3, 10^4, and 10...

### R96: For the Mixture Gaussian task, Simformer (with a dense atten...
- **Rubric ID**: 20c740b8-19b8-416e-b35b-e4d98db613d1
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Mixture Gaussian task, Simformer (with a dense attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Mixture Gaussian task, each of the following models have been trained for 10^3, 10^4, and 10...

### R97: For the Mixture Gaussian task, Simformer (with an undirected...
- **Rubric ID**: 152f3333-1368-4e19-a14f-f68c1cc26eb7
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Mixture Gaussian task, Simformer (with an undirected graph for it's attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Mixture Gaussian task, each of the following models have been trained for 10^3, 10^4, and 10...

### R98: For the Mixture Gaussian task, Simformer (with a directed gr...
- **Rubric ID**: fabc5fd9-a064-48d0-8da2-17bd643b8136
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Mixture Gaussian task, Simformer (with a directed graph for it's attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Mixture Gaussian task, each of the following models have been trained for 10^3, 10^4, and 10...

### R99: For the Two Moons task, NPE has been trained for 10^3, 10^4,...
- **Rubric ID**: a5d7b1c2-bf1e-4b84-a3ad-995892f597b8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Two Moons task, NPE has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Two Moons task, each of the following models have been trained for 10^3, 10^4, and 10^5 simu...

### R100: For the Two Moons task, Simformer (with a dense attention ma...
- **Rubric ID**: d47f5e4e-23ec-41f9-96c5-18a471eba572
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Two Moons task, Simformer (with a dense attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Two Moons task, each of the following models have been trained for 10^3, 10^4, and 10^5 simu...

### R101: For the Two Moons task, Simformer (with an undirected graph...
- **Rubric ID**: 629c1323-a808-4f83-9cfd-cdbe4d93cf46
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Two Moons task, Simformer (with an undirected graph for it's attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Two Moons task, each of the following models have been trained for 10^3, 10^4, and 10^5 simu...

### R102: For the Two Moons task, Simformer (with a directed graph for...
- **Rubric ID**: ec9c4b69-613a-42c3-8224-cef629f103ce
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Two Moons task, Simformer (with a directed graph for it's attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Two Moons task, each of the following models have been trained for 10^3, 10^4, and 10^5 simu...

### R103: For the SLCP task, NPE has been trained for 10^3, 10^4, and...
- **Rubric ID**: f2ad95c5-369c-4c20-859e-2f4931957879
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the SLCP task, NPE has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the SLCP task, each of the following models have been trained for 10^3, 10^4, and 10^5 simulatio...

### R104: For the SLCP task, Simformer (with a dense attention mask) h...
- **Rubric ID**: 3859bb58-dad4-4fe6-9c15-1b802e35ac9e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the SLCP task, Simformer (with a dense attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the SLCP task, each of the following models have been trained for 10^3, 10^4, and 10^5 simulatio...

### R105: For the SLCP task, Simformer (with an undirected graph for i...
- **Rubric ID**: fe86ca91-12bb-4ceb-bc1b-254a7aa9aa42
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the SLCP task, Simformer (with an undirected graph for it's attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the SLCP task, each of the following models have been trained for 10^3, 10^4, and 10^5 simulatio...

### R106: For the SLCP task, Simformer (with a directed graph for it's...
- **Rubric ID**: 5bbb52eb-424e-4711-9fad-48011f6af612
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the SLCP task, Simformer (with a directed graph for it's attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the SLCP task, each of the following models have been trained for 10^3, 10^4, and 10^5 simulatio...

### R107: For the Two Moons task, samples for ten ground-truth posteri...
- **Rubric ID**: fd64cfd0-746e-4441-bdc5-2b9bbef4e680
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Two Moons task, samples for ten ground-truth posteriors are obtained
- **Parent context**: For each task Linear Gaussian, Mixture Gaussian, Two Moons, SLCP, samples for ten ground-truth poste...

### R108: For the Two Moons task, for each model trained for 10^3, 10^...
- **Rubric ID**: 56cf845a-2871-4367-ab5f-de7eeca6ad8a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Two Moons task, for each model trained for 10^3, 10^4, and 10^5 simulations, N posterior samples are generated from the 10 different reference observations, where N is the number of reference samples
- **Parent context**: For each task Linear Gaussian, Mixture Gaussian, Two Moons, SLCP, for each model trained for 10^3, 1...

### R109: For the SLCP task, for each model trained for 10^3, 10^4, an...
- **Rubric ID**: 2270f417-52ab-4467-89ab-abbd8f8bc4ea
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the SLCP task, for each model trained for 10^3, 10^4, and 10^5 simulations, N posterior samples are generated from the 10 different reference observations, where N is the number of reference samples
- **Parent context**: For each task Linear Gaussian, Mixture Gaussian, Two Moons, SLCP, for each model trained for 10^3, 1...

### R110: For the Tree task, Simformer (with a dense attention mask) h...
- **Rubric ID**: 4a7698c5-edcd-4b67-a17b-a0f1230856a7
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Tree task, Simformer (with a dense attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Tree task, each of the following models have been trained for 10^3, 10^4, and 10^5 simulatio...

### R111: For the Tree task, Simformer (with an undirected graph for i...
- **Rubric ID**: 5fdb707e-4c2d-4a5d-96d6-d798c260dd79
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Tree task, Simformer (with an undirected graph for it's attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Tree task, each of the following models have been trained for 10^3, 10^4, and 10^5 simulatio...

### R112: For the Tree task, Simformer (with a directed graph for it's...
- **Rubric ID**: 5730c287-4b2c-43de-8b46-c60219839c1d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Tree task, Simformer (with a directed graph for it's attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the Tree task, each of the following models have been trained for 10^3, 10^4, and 10^5 simulatio...

### R113: For the HMM task, Simformer (with a dense attention mask) ha...
- **Rubric ID**: ee48f977-2f31-4cb6-a34f-589699af5fa3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the HMM task, Simformer (with a dense attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the HMM task, each of the following models have been trained for 10^3, 10^4, and 10^5 simulation...

### R114: For the HMM task, Simformer (with an undirected graph for it...
- **Rubric ID**: dbb902c0-3beb-475e-b1e4-e93ba3d9a3d9
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the HMM task, Simformer (with an undirected graph for it's attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the HMM task, each of the following models have been trained for 10^3, 10^4, and 10^5 simulation...

### R115: For the HMM task, Simformer (with a directed graph for it's...
- **Rubric ID**: 0ec528ea-7dc7-4420-ae51-359d30bacd47
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the HMM task, Simformer (with a directed graph for it's attention mask) has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: For the HMM task, each of the following models have been trained for 10^3, 10^4, and 10^5 simulation...

### R116: For the Two Moons task, for each model trained for 10^3, 10^...
- **Rubric ID**: 7413d98d-aa4b-4dd4-90b7-acf047652b39
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the Two Moons task, for each model trained for 10^3, 10^4, and 10^5 simulations, for each of the ground truth posterior samples, N model-generated posteriors are created by conditioning on the observations, where N is the number of reference samples
- **Parent context**: For each task Tree, HMM, Two Moons, and SLCP, for each model trained for 10^3, 10^4, and 10^5 simula...

### R117: For the SLCP task, for each model trained for 10^3, 10^4, an...
- **Rubric ID**: a2fe39cd-7147-490e-ad88-49b391d9b2a0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: For the SLCP task, for each model trained for 10^3, 10^4, and 10^5 simulations, for each of the ground truth posterior samples, N model-generated posteriors are created by conditioning on the observations, where N is the number of reference samples
- **Parent context**: For each task Tree, HMM, Two Moons, and SLCP, for each model trained for 10^3, 10^4, and 10^5 simula...

### R118: The Simformer in section 4.2 has been trained for 10^3, 10^4...
- **Rubric ID**: 7ec881a6-1960-450d-a466-12f0ba03d52d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The Simformer in section 4.2 has been trained for 10^3, 10^4, and 10^5 simulations (in separate training runs)
- **Parent context**: The recorded metrics show that the results in section 4.2 have been replicated

### R119: Given the five synthetic observations, the Simformer is appl...
- **Rubric ID**: 78909e7b-adc2-430f-8d2c-698f870ae046
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Given the five synthetic observations, the Simformer is applied to obtain samples from the posterior distribution of parameters as well as posterior predictive samples for unobserved  infected, recovered, and deceased values on a regular time grid from 0 to 40
- **Parent context**: Results for the Simformer when sampling 5 synthetic observations have been replicated

### R120: An observation interval is defined for the energy consumptio...
- **Rubric ID**: fa934dce-6547-475e-b231-8206c35d596d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: An observation interval is defined for the energy consumption within the lowsest 10% quantile of posterior predictives
- **Parent context**: Results when applying an observation interval have been replicated

## Data Processing & Preparation

### R121: The tasks Gaussian Linear, Gaussian Mixture, Two Moons, and...
- **Rubric ID**: 23688299-d3fa-43ed-be9f-2fa2b2c40fa4
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The tasks Gaussian Linear, Gaussian Mixture, Two Moons, and SLCP are available such that synthetic data can be sampled from each task
- **Parent context**: The four benchmark tasks in (Lueckmann et al., 2021) are prepared, as described in A2.2

### R122: For each of the tasks Gaussian Linear, Gaussian Mixture, Two...
- **Rubric ID**: c09ac29b-6e1f-492a-bb28-0fd1e0921ee8
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: For each of the tasks Gaussian Linear, Gaussian Mixture, Two Moons, and SLCP, N >= 1000 reference samples are generated
- **Parent context**: The four benchmark tasks in (Lueckmann et al., 2021) are prepared, as described in A2.2

### R123: The Tree task is available such that synthetic data can be s...
- **Rubric ID**: 1f652a29-c4c5-4d71-a7e5-9071b6a7da18
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The Tree task is available such that synthetic data can be sampled
- **Parent context**: The Tree task is prepared, as described in A2.2

### R124: For the Tree task, N >= 1000 reference samples are generated
- **Rubric ID**: 36605b43-ee09-4877-a74e-c5250de7a110
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: For the Tree task, N >= 1000 reference samples are generated
- **Parent context**: The Tree task is prepared, as described in A2.2

### R125: The HMM task is available such that synthetic data can be sa...
- **Rubric ID**: 6fc3436c-8304-4955-801b-0e35528e425d
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The HMM task is available such that synthetic data can be sampled
- **Parent context**: The HMM task is prepared, as described in A2.2, as described in A2.2

### R126: For the HMM task, N >= 1000 reference samples are generated
- **Rubric ID**: 321d7fd3-71de-4092-907f-c6197f0a7f69
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: For the HMM task, N >= 1000 reference samples are generated
- **Parent context**: The HMM task is prepared, as described in A2.2, as described in A2.2

### R127: The Lotka Volterra task is available such that synthetic dat...
- **Rubric ID**: 9f70a4e5-0896-4778-814a-1a3dee705854
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The Lotka Volterra task is available such that synthetic data can be sampled
- **Parent context**: The Lotka Volterra task is prepared, as described in A2.2

### R128: The SIRD task is available such that synthetic data can be s...
- **Rubric ID**: b96b17cd-fe54-4a06-9c95-5883018d631e
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The SIRD task is available such that synthetic data can be sampled
- **Parent context**: The SIRD task is prepared, as described in A2.2

### R129: The Hodgkin-Huxley task is available such that synthetic dat...
- **Rubric ID**: 64541d71-1b37-49be-9a3a-69bf786b3427
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The Hodgkin-Huxley task is available such that synthetic data can be sampled
- **Parent context**: The Hodgkin-Huxley task is prepared, as described in A2.2

### R130: In the Hodgkin-Huxley task, for observational data, the summ...
- **Rubric ID**: e2719676-7dc5-4fdd-a38a-eeadc6f81b27
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: In the Hodgkin-Huxley task, for observational data, the summary features are: spike count, resting potential mean, resting potential std, spiking window mean, and centered and standardizes moments up to 4th order
- **Parent context**: The Hodgkin-Huxley task is prepared, as described in A2.2

### R131: In the Hodgkin-Huxley task, the simulator-generated noisy ti...
- **Rubric ID**: 0b14bb53-e680-4ca6-a662-819ecd08cb16
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: In the Hodgkin-Huxley task, the simulator-generated noisy time series is reduced to the correct summary statistics
- **Parent context**: The Hodgkin-Huxley task is prepared, as described in A2.2

### R132: Four synthetic prey observations are sampled at random times
- **Rubric ID**: f4bb304f-5350-49e4-ba0a-c57b664c42ba
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Four synthetic prey observations are sampled at random times
- **Parent context**: Samples from the Simformer have been generated, conditioning on four synthetic prey observations

### R133: Nine additional synthetic observations of the predator popul...
- **Rubric ID**: 6cae1579-72c2-4f69-8c5f-47a6a3941aa9
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Nine additional synthetic observations of the predator population are sampled from Lotka-Volterra at random times
- **Parent context**: Results have been computed after sampling an additional nine synthetic predator observations

### R134: Five synthetic observations are generated from infected, rec...
- **Rubric ID**: a0864d9d-71ad-4650-aa62-150dd52c2b05
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Five synthetic observations are generated from infected, recovered, and deceased individuals at random times
- **Parent context**: Results for the Simformer when sampling 5 synthetic observations have been replicated

### R135: Synthetic observations consisting of four measurements of th...
- **Rubric ID**: a4c1f3af-b890-4414-947c-83ce4ce49ef4
- **Category**: Code Execution / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Synthetic observations consisting of four measurements of the time-dependent contact rate parameter is generated and a single synthetic observation of death population is generated
- **Parent context**: Results for the Simformer accurately sampling parameter-conditioned posterior distributions have bee...

## Evaluation, Metrics & Benchmarking

### R136: In the Hodgkin-Huxley task, energy consumption is computed b...
- **Rubric ID**: 5b2d5ce9-207a-47a0-8304-81c6bad86a69
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: In the Hodgkin-Huxley task, energy consumption is computed based on sodium charge, converted into $\mu J/s$
- **Parent context**: The Hodgkin-Huxley task is prepared, as described in A2.2

### R137: Given inputs X and Y, the classifier-based two-sample test a...
- **Rubric ID**: 3957cfb9-2e44-4026-be71-7d87d2c91583
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Given inputs X and Y, the classifier-based two-sample test accuracy between X and Y is measured as the 5-fold cross-validation score
- **Parent context**: The C2ST metric has been implemented

### R138: A score of 0.5 signifies perfect alignment with the ground t...
- **Rubric ID**: 973db5a3-21f4-48d0-8853-a5047626a637
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A score of 0.5 signifies perfect alignment with the ground truth posterior, and 1.0 indicates that a classifier can completely distinguish between the approximation and the ground truth
- **Parent context**: The C2ST metric has been implemented

### R139: For the Linear Gaussian task, samples for ten ground-truth p...
- **Rubric ID**: a4ad0e3d-c2ff-417d-a9b4-6b8bbcd00669
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the Linear Gaussian task, samples for ten ground-truth posteriors are obtained
- **Parent context**: For each task Linear Gaussian, Mixture Gaussian, Two Moons, SLCP, samples for ten ground-truth poste...

### R140: For the Mixture Gaussian task, samples for ten ground-truth...
- **Rubric ID**: 2ac19789-276a-4951-9d90-ba7a357511fb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the Mixture Gaussian task, samples for ten ground-truth posteriors are obtained
- **Parent context**: For each task Linear Gaussian, Mixture Gaussian, Two Moons, SLCP, samples for ten ground-truth poste...

### R141: For the Linear Gaussian task, for each model trained for 10^...
- **Rubric ID**: 3a9eb157-8938-4dcc-be3d-a3a8bd128a6b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the Linear Gaussian task, for each model trained for 10^3, 10^4, and 10^5 simulations, N posterior samples are generated from the 10 different reference observations, where N is the number of reference samples
- **Parent context**: For each task Linear Gaussian, Mixture Gaussian, Two Moons, SLCP, for each model trained for 10^3, 1...

### R142: For the Linear Gaussian task, for each model trained for 10^...
- **Rubric ID**: 183cc3f0-b19b-4a34-a217-5b912f33b69c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the Linear Gaussian task, for each model trained for 10^3, 10^4, and 10^5 simulations, Classifier Two-Sample Test accuracy between the model-generated posteriors and ground-truth posteriors have been calculated
- **Parent context**: For each task Linear Gaussian, Mixture Gaussian, Two Moons, SLCP, for each model trained for 10^3, 1...

### R143: For the Mixture Gaussian task, for each model trained for 10...
- **Rubric ID**: 59965170-0553-49cb-9c56-10f156301c77
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the Mixture Gaussian task, for each model trained for 10^3, 10^4, and 10^5 simulations, Classifier Two-Sample Test accuracy between the model-generated posteriors and ground-truth posteriors have been calculated
- **Parent context**: For each task Linear Gaussian, Mixture Gaussian, Two Moons, SLCP, for each model trained for 10^3, 1...

### R144: For the Two Moons task, for each model trained for 10^3, 10^...
- **Rubric ID**: 1149eae8-db2d-45ae-ac54-77551d12013d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the Two Moons task, for each model trained for 10^3, 10^4, and 10^5 simulations, Classifier Two-Sample Test accuracy between the model-generated posteriors and ground-truth posteriors have been calculated
- **Parent context**: For each task Linear Gaussian, Mixture Gaussian, Two Moons, SLCP, for each model trained for 10^3, 1...

### R145: For the SLCP task, for each model trained for 10^3, 10^4, an...
- **Rubric ID**: 6a97b353-6945-48ab-96cf-63640b596fbb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the SLCP task, for each model trained for 10^3, 10^4, and 10^5 simulations, Classifier Two-Sample Test accuracy between the model-generated posteriors and ground-truth posteriors have been calculated
- **Parent context**: For each task Linear Gaussian, Mixture Gaussian, Two Moons, SLCP, for each model trained for 10^3, 1...

### R146: Across all four benchmark tasks (Linear Gaussian, Mixture Ga...
- **Rubric ID**: a7604584-412e-4c92-9b49-7063bf40af90
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Across all four benchmark tasks (Linear Gaussian, Mixture Gaussian. Two Moons, SLCP) when approximating the posterior distribution, all Simformer variants almost always outperform neural posterior estimation (NPE) wrt. C2ST accuracy
- **Parent context**: Results Analysis

### R147: When approximating the posterior distribution, both the Simf...
- **Rubric ID**: 1755440f-b437-4700-b2c0-5740d5188fa4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When approximating the posterior distribution, both the Simformer with undirected graph and Simformer with directed graph significantly outperform the regular Simformer on the Linear Gaussian and SLCP tasks wrt. C2ST accuracy
- **Parent context**: Results Analysis

### R148: When approximating the posterior distribution, averaged acro...
- **Rubric ID**: 86499107-3abb-4381-9c83-359efa66286a
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When approximating the posterior distribution, averaged across all benchmark tasks (Linear Gaussian, Mixture Gaussian. Two Moons, SLCP) and number of simulations used in training, the Simformer required about 10 times fewer simulations than NPE to achieve similar performance wrt. C2ST accuracy
- **Parent context**: Results Analysis

### R149: For the Tree task, ground truth posterior samples with Marko...
- **Rubric ID**: dd3a0c20-a060-420d-ab30-2d2f306e1592
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the Tree task, ground truth posterior samples with Markov-Chain Monte-Carlo are generated on 100 randomly sampled selected conditional or full joint distributions
- **Parent context**: For each task Tree, HMM, Two Moons, and SLCP, ground truth posterior samples with Markov-Chain Monte...

### R150: For the HMM task, ground truth posterior samples with Markov...
- **Rubric ID**: 82cb5063-8d65-4270-bbf2-263bed38d932
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the HMM task, ground truth posterior samples with Markov-Chain Monte-Carlo are generated on 100 randomly sampled selected conditional or full joint distributions
- **Parent context**: For each task Tree, HMM, Two Moons, and SLCP, ground truth posterior samples with Markov-Chain Monte...

### R151: For the Tree task, for each model trained for 10^3, 10^4, an...
- **Rubric ID**: c1fdd141-a393-4471-abc9-02347a235cbb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the Tree task, for each model trained for 10^3, 10^4, and 10^5 simulations, Classifier Two-Sample Test accuracy between the model-generated posteriors (trained on 10^3, 10^4 and 10^5 simulations and conditioned on observations) and ground-truth posteriors have been calculated
- **Parent context**: For each task Tree, HMM, Two Moons, and SLCP, for each model trained for 10^3, 10^4, and 10^5 simula...

### R152: For the HMM task, for each model trained for 10^3, 10^4, and...
- **Rubric ID**: 0ece9e6e-a75c-4aa1-aad8-bf5fead43be6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the HMM task, for each model trained for 10^3, 10^4, and 10^5 simulations, Classifier Two-Sample Test accuracy between the model-generated posteriors (trained on 10^3, 10^4 and 10^5 simulations and conditioned on observations) and ground-truth posteriors have been calculated
- **Parent context**: For each task Tree, HMM, Two Moons, and SLCP, for each model trained for 10^3, 10^4, and 10^5 simula...

### R153: For the Two Moons task, for each model trained for 10^3, 10^...
- **Rubric ID**: 2a4fd54c-7609-4bca-be6e-821a1b941bd9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the Two Moons task, for each model trained for 10^3, 10^4, and 10^5 simulations, Classifier Two-Sample Test accuracy between the model-generated posteriors (trained on 10^3, 10^4 and 10^5 simulations and conditioned on observations) and ground-truth posteriors have been calculated
- **Parent context**: For each task Tree, HMM, Two Moons, and SLCP, for each model trained for 10^3, 10^4, and 10^5 simula...

### R154: For the SLCP task, for each model trained for 10^3, 10^4, an...
- **Rubric ID**: 99bb3116-25c7-4b6f-9f09-e97f8b0339eb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For the SLCP task, for each model trained for 10^3, 10^4, and 10^5 simulations, Classifier Two-Sample Test accuracy between the model-generated posteriors (trained on 10^3, 10^4 and 10^5 simulations and conditioned on observations) and ground-truth posteriors have been calculated
- **Parent context**: For each task Tree, HMM, Two Moons, and SLCP, for each model trained for 10^3, 10^4, and 10^5 simula...

### R155: When evaluating arbitrary conditionals on tasks Tree, HMM, T...
- **Rubric ID**: b858fec6-3c95-4e5e-89e1-02d441f30cab
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 3
- **Requirement**: When evaluating arbitrary conditionals on tasks Tree, HMM, Two Moons, and SLCP, when trained with 10^5 simulations, all Simformer models on all tasks achieve low C2ST (below 0.7)
- **Parent context**: The experiments in 4.1 related to evaluating arbitrary conditionals have been replicated

### R156: The Simformer trained on 10^5 simulations of Lotka-Volterra...
- **Rubric ID**: 1f9a15cb-263a-4fb9-957f-2eab2212ffb0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Simformer trained on 10^5 simulations of Lotka-Volterra is used with a dense attention mask to infer the posterior distribution on a uniform grid between t=0 and t=15, given the four synthetic observations and posterior predictive samples for unobserved predator and prey variables.
- **Parent context**: Samples from the Simformer have been generated, conditioning on four synthetic prey observations

### R157: The ground truth parameter is usually within regions of high...
- **Rubric ID**: 2da3fc50-59bb-466c-b167-7cf44c86e029
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The ground truth parameter is usually within regions of high posterior probability, using the Simformer with a dense attention mask trained on 10^5 simulations of Lotka-Volterra
- **Parent context**: Samples from the Simformer have been generated, conditioning on four synthetic prey observations

### R158: The Simformer (trained on 10^5 simulations of Lotka-Volterra...
- **Rubric ID**: c31c4bfa-12c2-4326-adb4-7cf06384a800
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The Simformer (trained on 10^5 simulations of Lotka-Volterra) with a dense attention mask is used to infer the posterior distribution given the four prey synthetic observations and nine predator synthetic observations
- **Parent context**: Results have been computed after sampling an additional nine synthetic predator observations

### R159: Including the nine predator synthetic observations reduces t...
- **Rubric ID**: 0f4a0b23-a0d9-4f11-bc99-9af8c899ad7b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: Including the nine predator synthetic observations reduces the uncertainty in the posterior predictive of both prey and predator populations, when using the Simformer trained on 10^5 simulations of Lotka-Volterra
- **Parent context**: Results have been computed after sampling an additional nine synthetic predator observations

### R160: All Simformers trained on 10^3, 10^4, 10^5 simulations of Lo...
- **Rubric ID**: 2551546a-de57-439f-8a62-0090e278638b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: All Simformers trained on 10^3, 10^4, 10^5 simulations of Lotka-Volterra are separately used to sample from arbitrary conditional distributions to simultaneously generate posterior and posterior predictive samples
- **Parent context**: The recorded metrics show that results in section 4.2 have been replicated.

### R161: Using the Simformer trained for 10^5 simulations of Lotka-Vo...
- **Rubric ID**: 173a3eec-8d27-4b7f-8960-678a592e926d
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: Using the Simformer trained for 10^5 simulations of Lotka-Volterra, the C2ST performance (posterior distribution) is below 0.65
- **Parent context**: The recorded metrics show that results in section 4.2 have been replicated.

### R162: Using the Simformer trained for 10^5 simulations of Lotka-Vo...
- **Rubric ID**: e87233c0-481d-4b86-bae8-bd37448a9231
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: Using the Simformer trained for 10^5 simulations of Lotka-Volterra, the C2ST performance (arbitrary conditionals) is below 0.75
- **Parent context**: The recorded metrics show that results in section 4.2 have been replicated.

### R163: The mean of the death, recovery and contact rate parameters...
- **Rubric ID**: 81423255-fefa-410a-869f-5fba0a9ce93c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The mean of the death, recovery and contact rate parameters is somewhat close to the true parameter that generated the observations, using the Simformer given the five synthetic observations
- **Parent context**: Results for the Simformer when sampling 5 synthetic observations have been replicated

### R164: The mean of the infected, recovered and death population den...
- **Rubric ID**: eeb98ce1-14b2-47f2-af99-c0f06c1ee5f3
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The mean of the infected, recovered and death population densities accurately model the sampled observations, using the Simformer given the five synthetic observations
- **Parent context**: Results for the Simformer when sampling 5 synthetic observations have been replicated

### R165: The Simformer estimated realistic death and recovery rates,...
- **Rubric ID**: aa314a14-d24f-4371-9738-ea3f62cb9a6c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The Simformer estimated realistic death and recovery rates, using the Simformer given the five synthetic observations
- **Parent context**: Results for the Simformer accurately sampling parameter-conditioned posterior distributions have bee...

### R166: The predicted mean intercepts all four measurements of the t...
- **Rubric ID**: 6e727597-f426-43da-9dd2-481dbc2c2b4b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The predicted mean intercepts all four measurements of the time-dependent contact rate parameter, using the Simformer given the five synthetic observations
- **Parent context**: Results for the Simformer accurately sampling parameter-conditioned posterior distributions have bee...

### R167: The predicted posterior is almost equivalent to the simulate...
- **Rubric ID**: edae46eb-6449-451f-8f5d-4936be7bf7bb
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The predicted posterior is almost equivalent to the simulated posterior
- **Parent context**: Results when inferring the posterior distribution given only the summary statistics have been replic...

### R168: The posterior predictive trace of Simformer closely matched...
- **Rubric ID**: 2c03b450-acbe-437f-a079-ee5560abf51d
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The posterior predictive trace of Simformer closely matched the posterior predictive trace obtained by running the simulator
- **Parent context**: Results when inferring the posterior distribution given only the summary statistics have been replic...

### R169: The predicted energy consumption lies below the desired thre...
- **Rubric ID**: d01c197f-aece-4023-af49-d1dfb8fc149b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The predicted energy consumption lies below the desired threshold
- **Parent context**: Results when applying an observation interval have been replicated

### R170: The posterior predictive trace of Simformer closely matched...
- **Rubric ID**: 4444e56a-ac1a-43b5-8b53-005190291454
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The posterior predictive trace of Simformer closely matched the posterior predictive trace obtained by running the simulator
- **Parent context**: Results when applying an observation interval have been replicated

## Logging, Analysis & Presentation

### R171: In the Hodgkin-Huxley task, the metabolic cost consumed by t...
- **Rubric ID**: d342c64a-005d-44f8-88af-5d650c363011
- **Category**: Code Development / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: In the Hodgkin-Huxley task, the metabolic cost consumed by the circuit is recorded and and added as an additional statistic
- **Parent context**: The Hodgkin-Huxley task is prepared, as described in A2.2

### R172: Including the nine predator measurements reduces the uncerta...
- **Rubric ID**: df75afbb-c140-4a59-acb6-df5986ef1780
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: Including the nine predator measurements reduces the uncertainty in both the posterior, when using the Simformer trained on 10^5 simulations of Lotka-Volterra
- **Parent context**: Results have been computed after sampling an additional nine synthetic predator observations

### R173: The posterior distribution has wide marginals for parameters...
- **Rubric ID**: 17113941-b42f-4662-9b19-d5676fa0e3f9
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The posterior distribution has wide marginals for parameters $g_{Na}, g_K$ and narrow marginals for parameters $C_m, g_L$
- **Parent context**: Results when inferring the posterior distribution given only the summary statistics have been replic...

### R174: The additional constraint on energy consumption significantl...
- **Rubric ID**: 540ce42f-c72d-491a-87d6-7aa69373fbab
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The additional constraint on energy consumption significantly constrained the parameters posterior, in particular the maximal sodium and potassium conductances
- **Parent context**: Results when applying an observation interval have been replicated
