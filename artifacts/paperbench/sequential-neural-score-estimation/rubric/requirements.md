# Rubric Requirements — sequential-neural-score-estimation
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 92

## Data Processing & Preparation

### R01: The Gaussian Linear task is available such that synthetic da...
- **Rubric ID**: 18fa145c-1614-4c29-8cc7-b99386a75872
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The Gaussian Linear task is available such that synthetic data can be sampled from the task
- **Parent context**: The necessary tasks are implemented, as described in Appendix E.1

### R02: The Gaussian Mixture task is available such that synthetic d...
- **Rubric ID**: 3a845c86-5343-4145-b38a-4f54fa8f065d
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The Gaussian Mixture task is available such that synthetic data can be sampled from the task
- **Parent context**: The necessary tasks are implemented, as described in Appendix E.1

### R03: The Two Moons task is available such that synthetic data can...
- **Rubric ID**: b0e7463b-dc2d-4a42-84c6-b59c34a0f5ac
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The Two Moons task is available such that synthetic data can be sampled from the task
- **Parent context**: The necessary tasks are implemented, as described in Appendix E.1

### R04: The Gaussian Linear Uniform task is available such that synt...
- **Rubric ID**: 636b493d-6459-4c02-9d26-e11ab99a0e43
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The Gaussian Linear Uniform task is available such that synthetic data can be sampled from the task
- **Parent context**: The necessary tasks are implemented, as described in Appendix E.1

### R05: The Bernoulli GLM task is available such that synthetic data...
- **Rubric ID**: 8ffe1960-87c2-48fb-9c6a-0e17cfe064bd
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The Bernoulli GLM task is available such that synthetic data can be sampled from the task
- **Parent context**: The necessary tasks are implemented, as described in Appendix E.1

### R06: The SLCP task is available such that synthetic data can be s...
- **Rubric ID**: f6f6e39c-0759-4cd7-8efc-5d20db3b67c7
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The SLCP task is available such that synthetic data can be sampled from the task
- **Parent context**: The necessary tasks are implemented, as described in Appendix E.1

### R07: The SIR task is available such that synthetic data can be sa...
- **Rubric ID**: 584fceff-d6b8-406b-a605-4b1671e74659
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The SIR task is available such that synthetic data can be sampled from the task
- **Parent context**: The necessary tasks are implemented, as described in Appendix E.1

### R08: The Lotka Volterra task is available such that synthetic dat...
- **Rubric ID**: b84bf196-46d7-4a15-b8a4-ff6a6a1e6177
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The Lotka Volterra task is available such that synthetic data can be sampled from the task
- **Parent context**: The necessary tasks are implemented, as described in Appendix E.1

### R09: The Neuroscience problem is available such that synthetic da...
- **Rubric ID**: 33a68532-f8bc-45bf-9794-fc4d54a7562a
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: The Neuroscience problem is available such that synthetic data can be sampled from the task
- **Parent context**: The necessary tasks are implemented, as described in Appendix E.1

### R10: When training NPSE, for each sampled parameter from the prio...
- **Rubric ID**: 74bb4c17-5d8f-4c1e-ba22-08a1c1e5ac45
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: When training NPSE, for each sampled parameter from the prior $\theta_0$, code is implemented to use the simulator to generate a corresponding observation $x$; $x \sim p(x|theta_0)$
- **Parent context**: A neural network is trained to approximate the sequence of score functions $\nabla_\theta \log p_t(\...

### R11: In TSNPSE, in the $r$-th round, a dataset $\mathcal{D}$ of $...
- **Rubric ID**: 6cf7e83a-748e-42f0-b7d7-55cb4e955f07
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 3
- **Requirement**: In TSNPSE, in the $r$-th round, a dataset $\mathcal{D}$ of $|M|$ samples is constructed by drawing $\theta_i \sim {p}^{-r-1}(\theta)$, $x_i \sim p(x \mid \theta_i)$, and adding $(\theta_i, x_i)$ to $\mathcal{D}$, where ${p}^{-r-1}(\theta)$ denotes the proposal prior and $p(x|\theta)$ denotes the simulator.
- **Parent context**: Truncated SNPSE (TSNPSE) has been implemented

### R12: Both the output of the parameter embedding network $\theta_t...
- **Rubric ID**: cd67e43e-f1fd-4aad-9e4d-e909e2b55ec3
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 2
- **Requirement**: Both the output of the parameter embedding network $\theta_t$ and output of the observation embedding network $x$ are standardized before being inputted to the score network, by subtracting an estimate of the mean and dividing by the standard deviation in each dimension. The empirical mean and empirical standard deviation of the training data is used
- **Parent context**: The score network has been implemented

### R13: 15% of each dataset is held out as a validation split. In se...
- **Rubric ID**: 6113057c-227b-45a4-820f-942878d80a33
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: 15% of each dataset is held out as a validation split. In sequential experiments, the validation split is re-computed on every round as 15% of the available simulations sampled uniformly at random
- **Parent context**: The correct hyperparameters have been implemented, as described in Appendix E.3

## Method Implementation

### R14: The forward noising process has been implemented following S...
- **Rubric ID**: 7cc9e28d-36c6-4895-b52e-cac1bf192f94
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The forward noising process has been implemented following Section 2.2
- **Parent context**: Both Variance-Exploding Stochastic Differential Equation (VESDE) and Variance-Preserving Stochastic ...

### R15: The drift term for VESDE is defined as $f(x, t)=0$
- **Rubric ID**: 5cbe0a62-71be-4aa8-9985-58970518ecf4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The drift term for VESDE is defined as $f(x, t)=0$
- **Parent context**: VESDE has been implemented following Appendix E.3

### R16: The diffusion term for VESDE is defined as $g(t)=\sigma_{min...
- **Rubric ID**: d6a4a408-756f-4efb-9de0-a2b39c92cb46
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The diffusion term for VESDE is defined as $g(t)=\sigma_{min} \cdot (\frac{\sigma_{min}}{\sigma_{max}})^t \cdot \sqrt{2 \log \frac{\sigma_{max}}{\sigma_{min}}}$
- **Parent context**: VESDE has been implemented following Appendix E.3

### R17: The drift term for VPSDE is defined as $f(x, t)=-\frac{1}{2}...
- **Rubric ID**: 13d28eb6-fd14-4738-985b-1335e2b5b9b5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The drift term for VPSDE is defined as $f(x, t)=-\frac{1}{2}\beta_t\theta_t$, where $\beta_t = \beta_{\text{min}} + t(\beta_{\text{max}} - \beta_{\text{min}})$
- **Parent context**: VPSDE has been implemented following Appendix E.3

### R18: The diffusion term for VPSDE is defined as $\sqrt{\beta_t}$,...
- **Rubric ID**: da121c46-2949-4214-9050-56a3d0817994
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The diffusion term for VPSDE is defined as $\sqrt{\beta_t}$, where $\beta_t = \beta_{\text{min}} + t(\beta_{\text{max}} - \beta_{\text{min}})$
- **Parent context**: VPSDE has been implemented following Appendix E.3

### R19: The constant $\beta_\text{max}$ for VPSDE is set to 11.0
- **Rubric ID**: 17102a8e-565c-46c6-908e-708d2ab7efc0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The constant $\beta_\text{max}$ for VPSDE is set to 11.0
- **Parent context**: VPSDE has been implemented following Appendix E.3

### R20: Code has been implemented for VESDE to compute the (gradient...
- **Rubric ID**: 7a91c729-63e7-4f4f-866d-d3d0f37c3a67
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for VESDE to compute the (gradients of the) transition log density
- **Parent context**: Both VESDE and VPSDE have implemented code to compute the (gradients of the) transition log density

### R21: Code has been implemented for VPSDE to compute the (gradient...
- **Rubric ID**: 648352ef-2fbe-480a-bf77-acd8f89bef81
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for VPSDE to compute the (gradients of the) transition log density
- **Parent context**: Both VESDE and VPSDE have implemented code to compute the (gradients of the) transition log density

### R22: The sbibm library is used to implement Neural Posterior Esti...
- **Rubric ID**: 3a389c28-41da-4eff-a2c9-49b423541dbc
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The sbibm library is used to implement Neural Posterior Estimation (NPE)
- **Parent context**: Neural Posterior Estimation (NPE) is implemented and has training defined

### R23: The sbibm library is used to implement Sequential Neural Pos...
- **Rubric ID**: 4c1cc604-a4fe-4bf1-99e3-0bbbfc54c6a5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The sbibm library is used to implement Sequential Neural Posterior Estimation (SNPE)
- **Parent context**: Sequential Neural Posterior Estimation (SNPE) is implemented and has training defined

### R24: Truncated Sequential Neural Posterior Estimation (TSNPE) is...
- **Rubric ID**: 02b42ffb-c304-49d2-b6f5-3cd61cd3e131
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Truncated Sequential Neural Posterior Estimation (TSNPE) is implemented using the GitHub repo https://github.com/mackelab/tsnpe_neurips
- **Parent context**: Baseline methods Neural Posterior Estimation (NPE), Sequential Neural Posterior Estimation (SNPE), a...

### R25: When training NPSE, for each $\theta_0$ and corresponding ob...
- **Rubric ID**: 2dc54398-e427-4caf-8ae2-88f5914b59c9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When training NPSE, for each $\theta_0$ and corresponding observation $x$, code is implemented to simulate the forward diffusion process using an SDE to obtain $\theta_t$ at time $t$
- **Parent context**: A neural network is trained to approximate the sequence of score functions $\nabla_\theta \log p_t(\...

### R26: When training NPSE, code is implemented to compute the loss...
- **Rubric ID**: da18282b-be9d-4e41-ae08-aca90181a908
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: When training NPSE, code is implemented to compute the loss as a Monte Carlo estimate of $\left\| s_\psi(\theta_t, x, t) - \nabla_{\theta_t} \log p_t(\theta_t | \theta) \right\|^2$, where $s_\psi(\theta_t, x, t)$ is the result of the score network, and $\nabla_{\theta_t} \log p_{t \mid 0}(\theta_t \mid \theta_0)$ is the forward diffusion transition log density
- **Parent context**: A neural network is trained to approximate the sequence of score functions $\nabla_\theta \log p_t(\...

### R27: When sampling using NPSE, samples are drawn from the station...
- **Rubric ID**: 3b1bf848-c43c-4179-b76e-ab4cd14b59de
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: When sampling using NPSE, samples are drawn from the stationary distribution $\pi$ (unit gaussian distribution); $\overline{\theta}_0 \sim \pi(\cdot)$
- **Parent context**: Approximate samples can be generated from the target posterior distribution using the neural network

### R28: When sampling using NPSE, the approximation of the time-reve...
- **Rubric ID**: eb61bf5c-7f24-4bb0-92eb-853205a8784c
- **Category**: Code Development / Method Implementation
- **Weight**: 3
- **Requirement**: When sampling using NPSE, the approximation of the time-reversal of the probability flow ODE is implemented given some observation $x = x_{\text{obs}}$, and replacing the score of the (perturbed) posterior(s) with the neural network; $\nabla_\theta \log p_t(\theta \vert x_{\text{obs}}) \approx s_\psi(\theta_t, x_{\text{obs}}, t)$. RK45 is used to solve the ODE
- **Parent context**: Approximate samples can be generated from the target posterior distribution using the neural network

### R29: In TSNPSE, the initial proposal prior is equivalent to the k...
- **Rubric ID**: 48600e77-0489-4561-9e25-ab3007d95db2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In TSNPSE, the initial proposal prior is equivalent to the known prior of the current task; $p(\theta) =: p^{-0}(\theta)$
- **Parent context**: In TSNPSE, the proposal prior in the $r$-th round is correctly computed

### R30: In TSNPSE, in the $r$-th round, after applying the NPSE algo...
- **Rubric ID**: 2fecc389-0e27-464c-afec-7e959ed15525
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In TSNPSE, in the $r$-th round, after applying the NPSE algorithm to learn a score network, 20000 samples are simulated from the approximate posterior via (the time-reversal of) the probability flow ODE using the neural network approximation of $\nabla_\theta \log p_t(\theta \vert x_{\text{obs}})$
- **Parent context**: In TSNPSE, all subsequent proposal priors are correctly computed

### R31: In TSNPSE, in the $r$-th round, the (approximate) likelihood...
- **Rubric ID**: 34fde1e1-8684-48e4-8fa0-4858fa6ef3c4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In TSNPSE, in the $r$-th round, the (approximate) likelihood $p(\theta \mid x_{\text{obs}})$ of the samples under the model is computed using the instantaneous-change-of-variables formula
- **Parent context**: In TSNPSE, all subsequent proposal priors are correctly computed

### R32: In TSNPSE, in the $r$-th round, the truncation boundary is c...
- **Rubric ID**: 5a98077f-3db6-462c-85de-da243375ccc9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In TSNPSE, in the $r$-th round, the truncation boundary is computed as the $\epsilon = 5 \times 10^{-4}$-th percentile of the samples from the approximate posterior. This defines the log-probability rejection threshold for rejection sampling.
- **Parent context**: In TSNPSE, all subsequent proposal priors are correctly computed

### R33: In TSNPSE, in the $r$-th round, when sampling from the trunc...
- **Rubric ID**: dc661069-d24d-4070-9d44-df19553d78d2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In TSNPSE, in the $r$-th round, when sampling from the truncated proposal prior, samples are first drawn from the prior as $\theta \sim p(\theta)$.
- **Parent context**: In TSNPSE, in the $r$-th round, sampling from the truncated proposal prior is correctly implemented

### R34: In TSNPSE, in the $r$-th round, when sampling from the trunc...
- **Rubric ID**: c70a513b-018e-4566-b5af-ab611effe4ce
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In TSNPSE, in the $r$-th round, when sampling from the truncated proposal prior, an initial rejection step is applied to samples drawn from the prior; the samples are rejected if they do not belong to the empirical hyperrectangle defined by the approximate posterior samples. That is, the hyperrectangle defined as the Cartesian product of the one-dimensional intervals with endpoints given by the minimum and maximum of the approximate posterior samples in each dimension.
- **Parent context**: In TSNPSE, in the $r$-th round, sampling from the truncated proposal prior is correctly implemented

### R35: In TSNPSE, in the $r$-th round, when sampling from the trunc...
- **Rubric ID**: c2e78e8a-de60-4cde-8fcc-2616f94ac186
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In TSNPSE, in the $r$-th round, when sampling from the truncated proposal prior, following the initial rejection step, the likelihood of the samples from the prior under the approximate posterior is computed using the instantaneous change-of-variables formula.
- **Parent context**: In TSNPSE, in the $r$-th round, sampling from the truncated proposal prior is correctly implemented

### R36: In TSNPSE, in the $r$-th round, when sampling from the trunc...
- **Rubric ID**: e17ca159-67a6-4117-8a6a-227c77ebc489
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In TSNPSE, in the $r$-th round, when sampling from the truncated proposal prior, samples are accepted if the likelihood under the approximation posterior is greater than the truncation boundary that has been computed on the $r$-th round. Otherwise they are rejected.
- **Parent context**: In TSNPSE, in the $r$-th round, sampling from the truncated proposal prior is correctly implemented

### R37: In TSNPSE, in the $r$-th round, when sampling from the trunc...
- **Rubric ID**: eb56d7bc-ce49-4033-94fe-a284b151e2b9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: In TSNPSE, in the $r$-th round, when sampling from the truncated proposal prior, the previous steps are repeated until the required number of samples from the proposal prior have been obtained.
- **Parent context**: In TSNPSE, in the $r$-th round, sampling from the truncated proposal prior is correctly implemented

### R38: In TSNPSE, in each of the rounds, given a dataset $\mathcal{...
- **Rubric ID**: d2f135a0-7aec-4df3-93db-3be72b20057b
- **Category**: Code Development / Method Implementation
- **Weight**: 3
- **Requirement**: In TSNPSE, in each of the rounds, given a dataset $\mathcal{D}$ of $|M|$ samples, the NPSE algorithm is followed to learn a neural network which approximates the score(s) of the perturbed posterior(s) $\nabla_{\theta_t} \log p_t(\theta_t | x)$
- **Parent context**: Truncated SNPSE (TSNPSE) has been implemented

### R39: In TSNPSE, the score network computed in the final round is...
- **Rubric ID**: 2d2d46c3-6627-47eb-b42d-ef5abaefefce
- **Category**: Code Development / Method Implementation
- **Weight**: 3
- **Requirement**: In TSNPSE, the score network computed in the final round is used as the final approximation of the scores $\nabla_{\theta_t} \log p_t(\theta_t | x)$, and can be used to generate approximate samples from the posterior, as per the standard NPSE algorithm
- **Parent context**: Truncated SNPSE (TSNPSE) has been implemented

### R40: The parameter embedding network $\theta_t$ is a 3-layer full...
- **Rubric ID**: 97d46d53-507a-4a3d-9fad-1bd3dcaaa2f3
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: The parameter embedding network $\theta_t$ is a 3-layer fully-connected MLP with 256 hidden units in each layer.
- **Parent context**: The parameter embedding network has been implemented

### R41: The output dimension from the final layer of the parameter e...
- **Rubric ID**: 3dcddd21-9771-40b6-8fdf-0a1a23f3f945
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The output dimension from the final layer of the parameter embedding network is determined by $\max (30, 4 \cdot d)$, where $d$ is the input dimension to the parameter embedding network
- **Parent context**: The parameter embedding network has been implemented

### R42: The observation embedding network $\x$ is a 3-layer fully-co...
- **Rubric ID**: 6e0acedb-7a05-416f-9863-aed1f683e05e
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: The observation embedding network $\x$ is a 3-layer fully-connected MLP with 256 hidden units in each layer
- **Parent context**: The observation embedding network has been implemented

### R43: The output dimension from the final layer of the observation...
- **Rubric ID**: a3351355-61be-411c-961d-6d7db8b397b1
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The output dimension from the final layer of the observation embedding network is determined by $\max (30, 4 \cdot p)$, where $p$ is the input dimension to the observation embedding network
- **Parent context**: The observation embedding network has been implemented

### R44: The sinusoidal embedding $t$ is embedded into 64 dimensions
- **Rubric ID**: 31a17217-0f10-4522-bda9-89614df502ec
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The sinusoidal embedding $t$ is embedded into 64 dimensions
- **Parent context**: The sinusoidal embedding $t$ is embedded correctly

### R45: The sinusoidal embedding $t$ is computed as follows: the $i$...
- **Rubric ID**: f7eafffb-aea8-460c-8f4c-6fb4be964de5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The sinusoidal embedding $t$ is computed as follows: the $i$-th value is computed as $\sin \left( \frac{t}{10000^{(i-1)/31}} \right)$ if $i \leq 32$, otherwise it is computed as $\cos \left( \frac{t}{10000^{((i-32)-1)/31}} \right)$
- **Parent context**: The sinusoidal embedding $t$ is embedded correctly

### R46: The score network is a 3-layer fully-connected MLP with 256...
- **Rubric ID**: 91963fec-c1e8-4b95-874f-9b85dfd087d3
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: The score network is a 3-layer fully-connected MLP with 256 hidden units in each layer
- **Parent context**: The score network has been implemented

### R47: The score network takes the concatenated input $[\theta_{\te...
- **Rubric ID**: 0203c1b6-f3c2-45f9-892b-e141f1e6e5c6
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: The score network takes the concatenated input $[\theta_{\text{emb}}, x_{\text{emb}}, t_{\text{emb}}] $, i.e. the outputs of the parameter embedding network, the output of the observation embedding network, and the output of the sinusoidal embedding network concatenated together
- **Parent context**: The score network has been implemented

### R48: The output dimension of the score network is equal to the di...
- **Rubric ID**: 20d5ed76-f928-40a2-8248-3f1dbaf2102e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The output dimension of the score network is equal to the dimension of the parameter embedding network
- **Parent context**: The score network has been implemented

### R49: All MLP networks use SiLU activation functions between layer...
- **Rubric ID**: 50b24eb8-9494-4f6a-83a0-ee0b9b9f1321
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: All MLP networks use SiLU activation functions between layers
- **Parent context**: The network architectures have been correctly implemented

## Experimental Setup

### R50: The constant $\sigma_{\text{min}}$ for VESDE is set to 0.01...
- **Rubric ID**: 0d28b6c7-3fa1-47c7-8bbf-7eaafb6e9077
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The constant $\sigma_{\text{min}}$ for VESDE is set to 0.01 for the tasks SIR and Two Moons
- **Parent context**: VESDE has been implemented following Appendix E.3

### R51: The constant $\sigma_{\text{min}}$ for VESDE is set to 0.05...
- **Rubric ID**: 394139bd-20d1-4bf3-b43e-b7af3507435d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The constant $\sigma_{\text{min}}$ for VESDE is set to 0.05 for the tasks Gaussian Linear, Gaussian Mixture, Gaussian Linear Uniform, Bernoulli GLM, SLCP, and Lotka Volterra
- **Parent context**: VESDE has been implemented following Appendix E.3

### R52: The constant $\sigma_{\text{max}}$ for VESDE is chosen to be...
- **Rubric ID**: 47bbd386-53c3-41ee-8068-172ff6496c6e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The constant $\sigma_{\text{max}}$ for VESDE is chosen to be as large as the maximum Euclidean distance between all pairs of training data points for the current task. For sequential methods, the training data points that are used are the training data points available in the first round
- **Parent context**: VESDE has been implemented following Appendix E.3

### R53: The time interval used in VESDE is (0, 1]
- **Rubric ID**: ee6fc1b6-ab2d-4773-ae59-fe29c9f8c39a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The time interval used in VESDE is (0, 1]
- **Parent context**: VESDE has been implemented following Appendix E.3

### R54: The constant $\beta_\text{min}$ for VPSDE is set to 0.1
- **Rubric ID**: c4621fe1-4c93-48a9-a8bb-4830b351ddd6
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The constant $\beta_\text{min}$ for VPSDE is set to 0.1
- **Parent context**: VPSDE has been implemented following Appendix E.3

### R55: The time interval used in VPSDE is (0, 1]
- **Rubric ID**: 6a5e82b9-6d49-435d-9a63-c6f210154c1e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The time interval used in VPSDE is (0, 1]
- **Parent context**: VPSDE has been implemented following Appendix E.3

### R56: Code is implemented to train Neural Posterior Estimation (NP...
- **Rubric ID**: 4c097da3-7391-40b2-adee-c08ec59b0539
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code is implemented to train Neural Posterior Estimation (NPE) using the sbibm library
- **Parent context**: Neural Posterior Estimation (NPE) is implemented and has training defined

### R57: Code is implemented to train Sequential Neural Posterior Est...
- **Rubric ID**: e73d1064-f820-4d47-ba52-e06d79b39711
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code is implemented to train Sequential Neural Posterior Estimation (SNPE) using the sbibm library
- **Parent context**: Sequential Neural Posterior Estimation (SNPE) is implemented and has training defined

### R58: In TSNPSE, given a total budget of $N$ simulations and $R$ r...
- **Rubric ID**: 08b7d601-6d74-42ed-bd7a-6984e1f7507b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: In TSNPSE, given a total budget of $N$ simulations and $R$ rounds, the simulations are evenly distributed across rounds; the number of simulations per round $M$ is computed as $M=N/R$
- **Parent context**: Truncated SNPSE (TSNPSE) has been implemented

### R59: Adam is used as the optimizer to train all networks
- **Rubric ID**: c1c7b1ce-bfc5-46bf-a701-78c98139bc74
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Adam is used as the optimizer to train all networks
- **Parent context**: The correct hyperparameters have been implemented, as described in Appendix E.3

### R60: A learning rate of 10^-4 is used when training all networks
- **Rubric ID**: e32788d4-0ee0-4542-864e-eec5a6e5b779
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: A learning rate of 10^-4 is used when training all networks
- **Parent context**: The correct hyperparameters have been implemented, as described in Appendix E.3

### R61: After each training step the loss on the validation split is...
- **Rubric ID**: 3a7eaa80-8b59-4ca1-b87f-4d71d979fdce
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: After each training step the loss on the validation split is computed. If this validation loss doesn't decrease for 1000 steps, then training is stopped and the network that gave the lowest validation loss is returned
- **Parent context**: The correct hyperparameters have been implemented, as described in Appendix E.3

### R62: The maximum number of training iterations is 3000
- **Rubric ID**: 46eb9ccc-c7eb-40c3-a34d-cc91e9e4db87
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: The maximum number of training iterations is 3000
- **Parent context**: The correct hyperparameters have been implemented, as described in Appendix E.3

### R63: For experiments with a simulation budget of either 1000 or 1...
- **Rubric ID**: b69e449f-2d50-4a36-be43-b0ee00a2c1e3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For experiments with a simulation budget of either 1000 or 10000, the batch size is 50 for non-sequential experiments (NPSE-VE, NPSE-VP, NPE)
- **Parent context**: The correct hyperparameters have been implemented, as described in Appendix E.3

### R64: For experiments with a simulation budget of either 1000 or 1...
- **Rubric ID**: dc9bd609-b5f3-428d-bff9-4d56843bbe06
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For experiments with a simulation budget of either 1000 or 10000, the batch size is 200 for sequential experiments (TSNPSE-VE, TSNPSE-VP, SNPE, TSNPE)
- **Parent context**: The correct hyperparameters have been implemented, as described in Appendix E.3

### R65: For simulation budgets of 100000 the batch size is 500 for a...
- **Rubric ID**: 7f97ba49-e042-4a5b-af23-48e1df11ae8a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: For simulation budgets of 100000 the batch size is 500 for all tasks
- **Parent context**: The correct hyperparameters have been implemented, as described in Appendix E.3

### R66: For each simulation budget 10^3, 10^4, 10^5, all sequential...
- **Rubric ID**: 3edc4750-98e6-4214-836c-8bba322e3000
- **Category**: Code Execution / Experimental Setup
- **Weight**: 3
- **Requirement**: For each simulation budget 10^3, 10^4, 10^5, all sequential methods (TSNPSE-VE, TSNPSE-VP, SNPE, TSNPE) have been trained for 10 rounds on all tasks and evaluated using C2ST
- **Parent context**: The experiments required for Section 5.2 have been executed

### R67: SNPSE-VP is trained with inference over 9 rounds, with 30000...
- **Rubric ID**: 1512d34f-61e1-452d-9d1a-97562bca29bd
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SNPSE-VP is trained with inference over 9 rounds, with 30000 initial simulations and 20000 added simulations in each round
- **Parent context**: The experiments required for Section 5.3 have been executed

## Evaluation, Metrics & Benchmarking

### R68: C2ST has been implemented using the default implementation f...
- **Rubric ID**: e7b8bc58-f9f5-45dd-b701-16bdd85c0975
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: C2ST has been implemented using the default implementation from `sbibm`, using default hyperparameters
- **Parent context**: The paper "Sequential Neural Score Estimation: Likelihood-Free Inference with Conditional Score Base...

### R69: When computing the C2ST score, 10000 samples from both the t...
- **Rubric ID**: ac2ef197-1e19-4e8b-9f2e-7a218dc7484e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When computing the C2ST score, 10000 samples from both the true posterior and the approximate posterior are used
- **Parent context**: The correct hyperparameters have been implemented, as described in Appendix E.3

### R70: For each simulation budget 10^3, 10^4, 10^5, all non-sequent...
- **Rubric ID**: d221f378-c075-4f37-9dad-5dc4c763891e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: For each simulation budget 10^3, 10^4, 10^5, all non-sequential methods (NPSE-VE, NPSE-VP, NPE) have been trained on all tasks and evaluated using C2ST
- **Parent context**: The experiments required for Section 5.2 have been executed

### R71: The recorded metrics show that, for the Lotka Volterra task,...
- **Rubric ID**: c32110eb-720f-4103-88db-9b0865929073
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the Lotka Volterra task, all methods NPSE-VE, NPSE-VP, and NPE achieve similar results to one-another (within +- 0.15 C2ST)
- **Parent context**: The results using non-sequential methods have been replicated

### R72: The recorded metrics show that, for the SLCP task, the metho...
- **Rubric ID**: e5ea6fe2-b69c-410c-a0ba-09df2dad95f9
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the SLCP task, the methods NPSE-VE and NPSE-VP achieve roughly equivalent C2ST scores
- **Parent context**: The results using non-sequential methods have been replicated

### R73: The recorded metrics show that, for the SLCP task, the metho...
- **Rubric ID**: 089460fd-533f-46c4-a148-1f9084898704
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the SLCP task, the methods NPSE-VE and NPSE-VP both achieve lower C2ST scores than NPE
- **Parent context**: The results using non-sequential methods have been replicated

### R74: The recorded metrics show that, for the Gaussian Linear Unif...
- **Rubric ID**: 26b43594-7ddb-41d4-8846-a2908f9a0ab8
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the Gaussian Linear Uniform task, NPE achieves a lower C2ST score than both methods NPSE-VE and NPSE-VP
- **Parent context**: The results using non-sequential methods have been replicated

### R75: The recorded metrics show that, for the Gaussian Linear Unif...
- **Rubric ID**: 54cccd02-52ae-44d0-9ad7-a2a7c12ae49c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the Gaussian Linear Uniform task, the methods NPSE-VE and NPSE-VP achieve roughly equivalent C2ST scores
- **Parent context**: The results using non-sequential methods have been replicated

### R76: The recorded metrics show that, for the Bernoulli GLM task,...
- **Rubric ID**: f4adb128-d3ee-47e9-bae3-c609ae8fc041
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the Bernoulli GLM task, all methods NPSE-VE, NPSE-VP, and NPE achieve roughly equivalent C2ST scores
- **Parent context**: The results using non-sequential methods have been replicated

### R77: The recorded metrics show that, for the SIR task, NPE achiev...
- **Rubric ID**: 9a4dbff1-55f9-4498-8e83-c84e3f831d6f
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the SIR task, NPE achieves a lower C2ST score than NPSE-VP
- **Parent context**: The results using non-sequential methods have been replicated

### R78: The recorded metrics show that, for the Two Moons task, NPE...
- **Rubric ID**: b40d156e-54a4-4102-855a-e797b9fad75b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the Two Moons task, NPE achieves a lower C2ST score than NPSE-VP
- **Parent context**: The results using non-sequential methods have been replicated

### R79: The recorded metrics show that, for the Gaussian Mixture tas...
- **Rubric ID**: 0e6a12ee-fae2-48b6-8c57-05e7fef83a44
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the Gaussian Mixture task, NPE and NPSE-VE achieve roughly equivalent C2ST scores
- **Parent context**: The results using non-sequential methods have been replicated

### R80: The recorded metrics show that, for the Gaussian Mixture tas...
- **Rubric ID**: 54e2553a-4f34-4c43-ab47-d83cb1d00e94
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the Gaussian Mixture task, both NPE and NPSE-VE achieve lower C2ST scores than NPSE-VP
- **Parent context**: The results using non-sequential methods have been replicated

### R81: The recorded metrics show that, for the Gaussian Linear task...
- **Rubric ID**: d560a5b0-9324-4b25-bb31-d9dcf2fd90d6
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the Gaussian Linear task, all methods NPSE-VE, NPSE-VP, and NPE achieve roughly equivalent C2ST scores
- **Parent context**: The results using non-sequential methods have been replicated

### R82: The recorded metrics show that, for the tasks SLCP, Lotka Vo...
- **Rubric ID**: 4f22134a-8d9f-41a1-accb-6c43332f2f9b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the tasks SLCP, Lotka Volterra, and Bernoulli GLM, TSNPSE-VE and TSNPSE-VP achieves a lower or roughly equivalent C2ST score than both SNPE and TSNPE
- **Parent context**: The results using sequential methods have been replicated

### R83: The recorded metrics show that, for the Gaussian Linear task...
- **Rubric ID**: 9176d64d-5d35-444c-be41-99cb2d4ccb74
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the Gaussian Linear task, TSNPSE-VE and TSNPSE-VP achieve a lower or roughly equivalent C2ST score compared to TSNPE
- **Parent context**: The results using sequential methods have been replicated

### R84: The recorded metrics show that, for the tasks Gaussian Linea...
- **Rubric ID**: 5cb794a0-9d35-4010-8f73-5c06f7d6d836
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the tasks Gaussian Linear Uniform, Bernoulli GLM, SIR, Two Moons, Gaussian Mixture, and Gaussian Linear, TSNPSE-VE achieves an equivalent or higher C2ST score compared to SNPE
- **Parent context**: The results using sequential methods have been replicated

### R85: The recorded metrics show that, for the tasks Gaussian Linea...
- **Rubric ID**: e4090d0e-af0b-42e0-87e3-e02c002e3697
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the tasks Gaussian Linear Uniform, Bernoulli GLM, SIR, Two Moons, Gaussian Mixture, and Gaussian Linear, TSNPSE-VP achieves an equivalent or higher C2ST score compared to SNPE
- **Parent context**: The results using sequential methods have been replicated

### R86: The recorded metrics show that, for the tasks Gaussian Linea...
- **Rubric ID**: 4da588d3-ed23-4938-ae45-6f3330b145b9
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the tasks Gaussian Linear Uniform, SIR, Two Moons, and Gaussian Mixture, TSNPSE-VE achieves an equivalent or higher C2ST score compared to TSNPE
- **Parent context**: The results using sequential methods have been replicated

### R87: The recorded metrics show that, for the tasks Gaussian Linea...
- **Rubric ID**: 1e34fed1-7c74-4eb5-a590-759ab003563c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, for the tasks Gaussian Linear Uniform, Bernoulli GLM, SIR, Two Moons, Gaussian Mixture, and Gaussian Linear, TSNPSE-VP achieves an equivalent or higher C2ST score compared to TSNPE
- **Parent context**: The results using sequential methods have been replicated

### R88: The percentage of valid summary statistics from each method...
- **Rubric ID**: db05a3d3-1026-4576-b4de-3a188c567ec8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The percentage of valid summary statistics from each method is computed after each round, where an invalid summary statistic is when the Pyloric simulator returns a `NaN` (in one or more of the output dimensions)
- **Parent context**: The experiments required for Section 5.3 have been executed

### R89: A posterior mean-predictive sample is computed at the end of...
- **Rubric ID**: 13c6dc3c-1578-48a4-9cc9-399a61cd22f2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: A posterior mean-predictive sample is computed at the end of the final round, by first computing the mean of the approximate posterior samples, then acquiring a simulation
- **Parent context**: The experiments required for Section 5.3 have been executed

### R90: The recorded metrics show that, in the final round, SNPSE-VP...
- **Rubric ID**: 46447a4d-bc28-4a37-8124-9db627b9f6b6
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that, in the final round, SNPSE-VP achieves about 80% valid summary statistics
- **Parent context**: The recorded metrics show that the results in Section 5.3 have been replicated

### R91: The recorded metrics show that SNPSE-VP has a higher percent...
- **Rubric ID**: 3fb824b3-9455-4ad1-a8ec-31af2dffad76
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics show that SNPSE-VP has a higher percentage of valid summary statistics for all simulation budgets less than 200*10^3 compared to TSNPE and SNVI
- **Parent context**: The recorded metrics show that the results in Section 5.3 have been replicated

### R92: The recorded metrics for the results in Section 5.3 show tha...
- **Rubric ID**: 445ce9cf-4bb6-40fc-b6d4-c96e32698ddc
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The recorded metrics for the results in Section 5.3 show that, the obtained posterior produces samples which closely match the observed data
- **Parent context**: The recorded metrics show that the results in Section 5.3 have been replicated
