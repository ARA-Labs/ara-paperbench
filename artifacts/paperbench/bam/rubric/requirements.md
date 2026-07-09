# Rubric Requirements — bam
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 789

## Method Implementation

### R01: BaM has been implemented such that, at minimum,...
- **Rubric ID**: bam-interface-output
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: BaM has been implemented such that, at minimum, it takes batch size, inverse regularization (learning rate), the target score function, the initial mean and the initial covariance as input and outputs the estimated variational parameters.
- **Parent context**: The Batch and Match (BaM) algorithm for Variational Inference (VI) has been implemented as outlin...

### R02: The 'batch' step in BaM has been implemented...
- **Rubric ID**: bam-batch-sampling
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The 'batch' step in BaM has been implemented such that at each iteration the current estimated mean and covariance matrix are used to sample $z_b$ from a Gaussian for $b = 1, \dots, B$, where B is the batch size.
- **Parent context**: The 'batch' step from BaM has been correctly implemented as outlined in Section 3 and Algorithm 1.

### R03: The 'batch' step in BaM has been implemented...
- **Rubric ID**: bam-batch-score-computation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The 'batch' step in BaM has been implemented such that at each iteration the "score" ($\nabla \log (p)$, where $p$ is the density of the target distribution)) can be and is computed for each sampled $z_b$.
- **Parent context**: The 'batch' step from BaM has been correctly implemented as outlined in Section 3 and Algorithm 1.

### R04: The 'batch' step in BaM has been implemented...
- **Rubric ID**: bam-batch-statistics
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The 'batch' step in BaM has been implemented such that the sample statistics are accumulated following equations (6) and (7), as shown in step 5 of Algorithm 1.
- **Parent context**: The 'batch' step from BaM has been correctly implemented as outlined in Section 3 and Algorithm 1.

### R05: The 'match' step in BaM has been implemented...
- **Rubric ID**: bam-qm-equation
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: The 'match' step in BaM has been implemented such that at each iteration, the U and V matrices have been implemented using the accumulated statistics from the 'batch' step, as outlined in equations (10) and (11) and in step 6 of Algorithm 1.
- **Parent context**: The 'match' step from BaM has been correctly implemented as outlined in Section 3 and Algorithm 1.

### R06: The 'match' step in BaM has been implemented...
- **Rubric ID**: bam-updated-mean
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: The 'match' step in BaM has been implemented such that at each iteration, the U and V matrices are used along with the accumulated statistics and the inverse regularization (learning rate) to update the estimated mean and covariance using equations (12) and (13) as shown in step 7 of algorithm 1.
- **Parent context**: The 'match' step from BaM has been correctly implemented as outlined in Section 3 and Algorithm 1.

### R07: The BaM 'match' step has been implemented such...
- **Rubric ID**: bam-low-rank-solver-optional
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The BaM 'match' step has been implemented such that it optionally supports updating covariance using the update in Lemma B.3, asserting that B<D
- **Parent context**: The 'match' step from BaM has been correctly implemented as outlined in Section 3 and Algorithm 1.

### R08: BaM has been implemented such that it generally...
- **Rubric ID**: 6320b786-5d6a-40bd-ac47-deb3c3cff4e4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: BaM has been implemented such that it generally follows the steps in Algorithm 1.
- **Parent context**: The Batch and Match (BaM) algorithm for Variational Inference (VI) has been implemented as outlin...

### R09: ADVI is implemented such that, at minimum, it...
- **Rubric ID**: advi-setup
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: ADVI is implemented such that, at minimum, it takes batch size, a learning rate or learning rate schedule, the unnormalized target log density, the initial mean and the initial covariance as input and outputs the estimated variational parameters.
- **Parent context**: Automatic Differentiation Variational Inference (ADVI) has been implemented as outlined in the pr...

### R10: ADVI has been implemented such that at each...
- **Rubric ID**: advi-sampling-step
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: ADVI has been implemented such that at each iteration, a mini-batch of samples is drawn from the current approximate distribution $q_{t}$, a Gaussian with some mean $\mu_{t}$ and covariance $\Sigma_{t}$.
- **Parent context**: Automatic Differentiation Variational Inference (ADVI) has been implemented as outlined in the pr...

### R11: ADVI has been implemented such that at each...
- **Rubric ID**: advi-elbo-estimation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: ADVI has been implemented such that at each iteration, a stochastic estimate of the (negative) Evidence Lower Bound (ELBO) is computed using the reparameterization trick or an equivalent approach for samples \(z_b\sim q_{t}\). Specifically, the code forms \(-\sum_b [\log p(z_b) - \log q_t(z_b)]\).
- **Parent context**: Automatic Differentiation Variational Inference (ADVI) has been implemented as outlined in the pr...

### R12: ADVI has been implemented such that the gradient...
- **Rubric ID**: advi-update-step
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: ADVI has been implemented such that the gradient of the negative ELBO (with respect to the variational parameters) is used to update the variational parameters (e.g. via the Adam optimizer) as shown in step 5 of Algorithm 2
- **Parent context**: Automatic Differentiation Variational Inference (ADVI) has been implemented as outlined in the pr...

### R13: Overall, the implemented ADVI procedure follows the logic...
- **Rubric ID**: advi-has-followed-algo2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Overall, the implemented ADVI procedure follows the logic of Algorithm 2
- **Parent context**: Automatic Differentiation Variational Inference (ADVI) has been implemented as outlined in the pr...

### R14: Automatic Differentiation Variational Inference (ADVI) "Score" variant has...
- **Rubric ID**: 28288cd0-0d49-4215-aaff-a59eb10f50a5
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: Automatic Differentiation Variational Inference (ADVI) "Score" variant has been implemented, such that it is identical to the ADVI implementation but rather than using ELBO loss, it uses score-based divergence.
- **Parent context**: The core variational inference algorithms studied in the paper have been implemented

### R15: Automatic Differentiation Variational Inference (ADVI) "Fisher" variant has...
- **Rubric ID**: 2b23a5ca-0606-463c-838e-b95f1e69253c
- **Category**: Code Development / Method Implementation
- **Weight**: 2
- **Requirement**: Automatic Differentiation Variational Inference (ADVI) "Fisher" variant has been implemented, such that it is identical to the ADVI implementation but rather than using ELBO loss, it uses Fisher divergence
- **Parent context**: The core variational inference algorithms studied in the paper have been implemented

### R16: GSM has been implemented such that it takes,...
- **Rubric ID**: gsm-interface-output
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: GSM has been implemented such that it takes, at minimum, a batch size, the unnormalized target density, the initial mean and the initial covariance as input and outputs the estimated variational parameters.
- **Parent context**: The Gaussian Score Matching (GSM) approach for Variational Inference (VI) has been implemented as...

### R17: GSM has been implemented such that at each...
- **Rubric ID**: gsm-iteration-loop
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: GSM has been implemented such that at each iteration, a mini-batch of samples is drawn from the current approximate distribution $q_{t}$, a Gaussian with some mean $\mu_{t}$ and covariance $\Sigma_{t}$.
- **Parent context**: The Gaussian Score Matching (GSM) approach for Variational Inference (VI) has been implemented as...

### R18: GSM has been implemented such that at each...
- **Rubric ID**: gsm-score-computation
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: GSM has been implemented such that at each iteration, for each sampled $z_b$ the target distribution's score \$s_b = \nabla \log \tilde{p}(z_b)$ is computed
- **Parent context**: The Gaussian Score Matching (GSM) approach for Variational Inference (VI) has been implemented as...

### R19: GSM has been implemented such that at each...
- **Rubric ID**: c8d8bf97-af2f-46be-b070-e5e128586a3a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: GSM has been implemented such that at each iteration, for each sampled $z_b$, the updated for mean and covariance are estimated following steps 6 and 7 of Algorithm 3.
- **Parent context**: The Gaussian Score Matching (GSM) approach for Variational Inference (VI) has been implemented as...

### R20: GSM has been implemented such that each iteration,...
- **Rubric ID**: gsm-partial-updates
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: GSM has been implemented such that each iteration, the variational mean and covariance are updated following step 9 of Algorithm 3.
- **Parent context**: The Gaussian Score Matching (GSM) approach for Variational Inference (VI) has been implemented as...

### R21: Overall, the GSM procedure has been implemented so...
- **Rubric ID**: gsm-has-followed-algo3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Overall, the GSM procedure has been implemented so that it follows the main steps of Algorithm 3.
- **Parent context**: The Gaussian Score Matching (GSM) approach for Variational Inference (VI) has been implemented as...

### R22: Code has been implemented such that 4-dimensional Gaussian...
- **Rubric ID**: 50edd5b6-1d84-4a50-9e2f-9825a51b4c6a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that 4-dimensional Gaussian distributions can be used as target distributions
- **Parent context**: Code has been implemented such that Gaussian distributions of dimension $D \in \{4, 16, 64, 256\}...

### R23: Code has been implemented such that 16-dimensional Gaussian...
- **Rubric ID**: 92c9368d-79c0-4811-bac5-4f5c013433a3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that 16-dimensional Gaussian distributions can be used as target distributions
- **Parent context**: Code has been implemented such that Gaussian distributions of dimension $D \in \{4, 16, 64, 256\}...

### R24: Code has been implemented such that 64-dimensional Gaussian...
- **Rubric ID**: c970ece1-fb92-4203-aa5d-8e65b145f417
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that 64-dimensional Gaussian distributions can be used as target distributions
- **Parent context**: Code has been implemented such that Gaussian distributions of dimension $D \in \{4, 16, 64, 256\}...

### R25: Code has been implemented such that 256-dimensional Gaussian...
- **Rubric ID**: 63a772a0-d934-49b8-bb2c-56c2cc3d18cc
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that 256-dimensional Gaussian distributions can be used as target distributions
- **Parent context**: Code has been implemented such that Gaussian distributions of dimension $D \in \{4, 16, 64, 256\}...

### R26: Code has been implemented such that the score...
- **Rubric ID**: d6b2f005-796b-4dc9-9b8e-4b3aeb195ae4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the score function for a 4-dimensional Gaussian distribution can be computed (either analytically or with an autodiff solution)
- **Parent context**: Code has been implemented such that the score function for a Gaussian distributions of dimension ...

### R27: Code has been implemented such that the score...
- **Rubric ID**: c7b901f3-450e-41c3-b843-ab635890be05
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the score function for a 16-dimensional Gaussian distribution can be computed (either analytically or with an autodiff solution)
- **Parent context**: Code has been implemented such that the score function for a Gaussian distributions of dimension ...

### R28: Code has been implemented such that the score...
- **Rubric ID**: b2ae9111-5996-4b93-8dca-e80a015adf53
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the score function for a 64-dimensional Gaussian distribution can be computed (either analytically or with an autodiff solution)
- **Parent context**: Code has been implemented such that the score function for a Gaussian distributions of dimension ...

### R29: Code has been implemented such that the score...
- **Rubric ID**: c293cbce-662c-4723-9141-3aa045dbe42e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the score function for a 256-dimensional Gaussian distribution can be computed (either analytically or with an autodiff solution)
- **Parent context**: Code has been implemented such that the score function for a Gaussian distributions of dimension ...

### R30: Code has been implemented for using BaM to...
- **Rubric ID**: c5574df9-467c-4e54-916e-3b5a7796d089
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2
- **Parent context**: BaM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R31: Code has been implemented for using BaM to...
- **Rubric ID**: fbdb544e-f50f-470a-8119-2db6b615bf83
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 5
- **Parent context**: BaM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R32: Code has been implemented for using BaM to...
- **Rubric ID**: ee04129e-d7a7-43f3-ac48-f0a483d8e110
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2
- **Parent context**: BaM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R33: Code has been implemented for using BaM to...
- **Rubric ID**: b35f2cfb-a024-4f04-8455-9901825390f4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 15
- **Parent context**: BaM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R34: Code has been implemented for using BaM to...
- **Rubric ID**: c2e800f3-4cd4-453a-9352-37cf844759e5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2
- **Parent context**: BaM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R35: Code has been implemented for using BaM to...
- **Rubric ID**: d3765100-6550-4508-8b98-d98114ef0040
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 40
- **Parent context**: BaM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R36: Code has been implemented for using BaM to...
- **Rubric ID**: 39e40367-ba29-4826-bcd3-fb6e1dc7963e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2
- **Parent context**: BaM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R37: Code has been implemented for using BaM to...
- **Rubric ID**: a21ce6b6-2b35-4227-878f-d1635b2c9493
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 150
- **Parent context**: BaM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R38: Code has been implemented for using GSM to...
- **Rubric ID**: f6d52f40-cd4c-40d9-a230-be509486b0eb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2
- **Parent context**: GSM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R39: Code has been implemented for using GSM to...
- **Rubric ID**: 7421b712-966c-4476-8aff-e0d6247ceb09
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2
- **Parent context**: GSM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R40: Code has been implemented for using GSM to...
- **Rubric ID**: dd0d8498-77c9-419c-b042-c7befeb3696a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2
- **Parent context**: GSM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R41: Code has been implemented for using GSM to...
- **Rubric ID**: bcc28907-bf05-4e9f-bba6-490e2516697b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2
- **Parent context**: GSM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R42: Code has been implemented for using ADVI to...
- **Rubric ID**: 77c5e4f4-3e37-4d88-9b5f-c1ffb6901a1f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch ...

### R43: Code has been implemented for using ADVI to...
- **Rubric ID**: 019702c4-52c7-4988-baf0-51a951707d80
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch ...

### R44: Code has been implemented for using ADVI to...
- **Rubric ID**: 4d4f636e-6121-460e-98c1-090b51342277
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch...

### R45: Code has been implemented for using ADVI (Score)...
- **Rubric ID**: c7d14bb0-373a-47e1-ac5c-dd91eca1695d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Score) to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 4-dimensional Gaussian distribution with...

### R46: Code has been implemented for using ADVI (Score)...
- **Rubric ID**: f5437611-5a59-42b7-9646-0730ee6667b7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Score) to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wit...

### R47: Code has been implemented for using ADVI (Score)...
- **Rubric ID**: 44fd1ea8-3944-4695-918c-9772a867aa73
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Score) to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wit...

### R48: Code has been implemented for using ADVI (Score)...
- **Rubric ID**: 5775d45e-e528-4c0d-b553-82e5b005c089
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Score) to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 256-dimensional Gaussian distribution wi...

### R49: Code has been implemented for using ADVI (Fisher)...
- **Rubric ID**: dc5a24f1-f2b4-4351-87f5-30a1f7585388
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Fisher) to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 4-dimensional Gaussian distribution wit...

### R50: Code has been implemented for using ADVI (Fisher)...
- **Rubric ID**: f1a39120-2827-4348-8400-c79c79213769
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Fisher) to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wi...

### R51: Code has been implemented for using ADVI (Fisher)...
- **Rubric ID**: 86e8e06c-f129-4d2e-b7d2-e313537abdaa
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Fisher) to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wi...

### R52: Code has been implemented for using ADVI (Fisher)...
- **Rubric ID**: 68163181-2c7e-474b-a8d4-b2b1d7f20276
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Fisher) to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 256-dimensional Gaussian distribution w...

### R53: Code has been implemented such that 10-dimensional sinh-arcsinh...
- **Rubric ID**: ff269cb7-a37d-4a14-8960-ccd93e603f80
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10-dimensional sinh-arcsinh normal distributions with a normal tail ($t=1$) and skew $s=0.2$ can be used as target distributions
- **Parent context**: Code has been implemented such that 10-dimensional sinh-arcsinh normal distributions with differe...

### R54: Code has been implemented such that 10-dimensional sinh-arcsinh...
- **Rubric ID**: d8170870-2836-4d2e-beab-9f291b2ce36d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10-dimensional sinh-arcsinh normal distributions with a normal tail ($t=1$) and skew $s=1$ can be used as target distributions
- **Parent context**: Code has been implemented such that 10-dimensional sinh-arcsinh normal distributions with differe...

### R55: Code has been implemented such that 10-dimensional sinh-arcsinh...
- **Rubric ID**: 82a1992c-1068-4323-a51b-b770b583b878
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10-dimensional sinh-arcsinh normal distributions with a normal tail ($t=1$) and skew $s=1.8$ can be used as target distributions
- **Parent context**: Code has been implemented such that 10-dimensional sinh-arcsinh normal distributions with differe...

### R56: Code has been implemented such that 10-dimensional sinh-arcsinh...
- **Rubric ID**: 207e29f4-75d4-4007-9441-e2b5d8ac8702
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10-dimensional sinh-arcsinh normal distributions with no skew ($s=0$) and tail $t=0.1$ can be used as target distributions
- **Parent context**: Code has been implemented such that 10-dimensional sinh-arcsinh normal distributions with differe...

### R57: Code has been implemented such that 10-dimensional sinh-arcsinh...
- **Rubric ID**: 09019bbd-437c-4f73-97e3-00ecfda7472b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10-dimensional sinh-arcsinh normal distributions with no skew ($s=0$) and tail $t=0.9$ can be used as target distributions
- **Parent context**: Code has been implemented such that 10-dimensional sinh-arcsinh normal distributions with differe...

### R58: Code has been implemented such that 10-dimensional sinh-arcsinh...
- **Rubric ID**: 070becc1-57ff-4e55-8055-561d38bb3cce
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10-dimensional sinh-arcsinh normal distributions with no skew ($s=0$) and tail $t=1.7$ can be used as target distributions
- **Parent context**: Code has been implemented such that 10-dimensional sinh-arcsinh normal distributions with differe...

### R59: Code has been implemented such that the score...
- **Rubric ID**: 5b909bab-d557-4f11-9d59-1ba13436b0d0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the score function for a 10-dimensional sinh-arcsinh normal distribution can be computed (either analytically or with an autodiff solution) with a normal tail ($t=1$) and skew $s=0.2$
- **Parent context**: Code has been implemented such that the score function for a 10-dimensional sinh-arcsinh normal d...

### R60: Code has been implemented such that the score...
- **Rubric ID**: 92a1d7d3-d19f-4754-b3dc-2f732c62e6b4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the score function for a 10-dimensional sinh-arcsinh normal distribution can be computed (either analytically or with an autodiff solution) with a normal tail ($t=1$) and skew $s=1$
- **Parent context**: Code has been implemented such that the score function for a 10-dimensional sinh-arcsinh normal d...

### R61: Code has been implemented such that the score...
- **Rubric ID**: a1e6e69f-5c8c-4c2c-a647-d0b82de248e8
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the score function for a 10-dimensional sinh-arcsinh normal distribution can be computed (either analytically or with an autodiff solution) with a normal tail ($t=1$) and skew $s=1.8$
- **Parent context**: Code has been implemented such that the score function for a 10-dimensional sinh-arcsinh normal d...

### R62: Code has been implemented such that the score...
- **Rubric ID**: 7bab19a2-310f-481f-9afd-57923298ef72
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the score function for a 10-dimensional sinh-arcsinh normal distribution can be computed (either analytically or with an autodiff solution) with no skew ($s=0$) and tail $t=0.1$
- **Parent context**: Code has been implemented such that the score function for a 10-dimensional sinh-arcsinh normal d...

### R63: Code has been implemented such that the score...
- **Rubric ID**: d35ebeb4-c5c5-436a-af5d-b21d48db66ec
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the score function for a 10-dimensional sinh-arcsinh normal distribution can be computed (either analytically or with an autodiff solution) with no skew ($s=0$) and tail $t=0.9$
- **Parent context**: Code has been implemented such that the score function for a 10-dimensional sinh-arcsinh normal d...

### R64: Code has been implemented such that the score...
- **Rubric ID**: fd81315c-b70e-471a-a634-f1ce3a04b328
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the score function for a 10-dimensional sinh-arcsinh normal distribution can be computed (either analytically or with an autodiff solution) with no skew ($s=0$) and tail $t=1.7$
- **Parent context**: Code has been implemented such that the score function for a 10-dimensional sinh-arcsinh normal d...

### R65: Code has been implemented such that when using...
- **Rubric ID**: 18ac0834-f755-44cd-a0c5-6fb1a1b23aa2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using BaM to estimate the posterior of a given 10-dimensional sinh-arcsinh normal distribution, BaM VI can be run for at least 10E4 iterations
- **Parent context**: BaM has been run to estimate the posterior of 10-dimensional sinh-arcsinh normal distributions wi...

### R66: Code has been implemented for using BaM to...
- **Rubric ID**: 28d977ff-e0dc-42bf-a9ff-e6494f3345ec
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R67: Code has been implemented for using BaM to...
- **Rubric ID**: ca596add-6928-4936-b59b-25b3f822c020
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 10
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R68: Code has been implemented for using BaM to...
- **Rubric ID**: 34cdb209-0c54-498c-b77c-4e423e9fadb9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R69: Code has been implemented for using BaM to...
- **Rubric ID**: c8390171-a91e-4106-9af1-778bf2e05fad
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 10
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R70: Code has been implemented for using BaM to...
- **Rubric ID**: d8e5e825-3ff9-4d46-a4a6-4186741e372c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R71: Code has been implemented for using BaM to...
- **Rubric ID**: be0ef39a-0aa7-4417-b5f8-f922061a5314
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 10
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R72: Code has been implemented for using BaM to...
- **Rubric ID**: 6c660cf4-52f7-4a98-bbbb-15ebf344bfee
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R73: Code has been implemented for using BaM to...
- **Rubric ID**: dd07dda1-9b02-43c7-b0ee-66afedde04e6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 10
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R74: Code has been implemented for using BaM to...
- **Rubric ID**: 3105a9d3-ae36-4127-9f05-3aa254cb975f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R75: Code has been implemented for using BaM to...
- **Rubric ID**: 26b2e529-f297-420c-a9e5-cd395d63c6ce
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 10
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R76: Code has been implemented for using BaM to...
- **Rubric ID**: 6534a8e5-36bc-4327-a008-a7757bdd758a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R77: Code has been implemented for using BaM to...
- **Rubric ID**: fa254875-4f75-4ac8-98a2-d7148f8f567e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 10
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R78: Code has been implemented such that when using...
- **Rubric ID**: d712e1e2-19c1-4c18-a578-87e8c0251fa5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using GSM to estimate the posterior of a given 10-dimensional sinh-arcsinh normal distribution, GSM VI can be run for at least 10E4 iterations
- **Parent context**: GSM has been run to estimate the posterior of 10-dimensional sinh-arcsinh normal distributions wi...

### R79: Code has been implemented for using GSM to...
- **Rubric ID**: 5911c6c6-8360-4a6c-8f79-ae88a452e709
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R80: Code has been implemented for using GSM to...
- **Rubric ID**: 757e115e-7858-4b19-b82a-6dab796125ec
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R81: Code has been implemented for using GSM to...
- **Rubric ID**: 12437269-d581-4bf0-b7a3-d5dc97d1b39e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R82: Code has been implemented for using GSM to...
- **Rubric ID**: c13010f1-acdb-41a3-b93a-244c0a010c7c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R83: Code has been implemented for using GSM to...
- **Rubric ID**: 692a185b-7c0b-4b47-a66b-57ab09a21be4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R84: Code has been implemented for using GSM to...
- **Rubric ID**: b3960a65-9de3-4e1c-8b8e-84df01b6f525
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R85: Code has been implemented for using ADVI to...
- **Rubric ID**: 575b0fcc-2b32-48a2-9787-65b00c2c5937
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R86: Code has been implemented for using ADVI to...
- **Rubric ID**: 82ff24a9-8690-4761-9649-665b13de052e
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R87: Code has been implemented for using ADVI to...
- **Rubric ID**: 81f81047-3fd7-49b6-b3c3-f5901be9ecf2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R88: Code has been implemented for using ADVI to...
- **Rubric ID**: a86a18eb-e8fe-4bd2-8b07-14d587e952ce
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R89: Code has been implemented for using ADVI to...
- **Rubric ID**: d0d7f5f5-16de-4649-ad52-88182c79356a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R90: Code has been implemented for using ADVI to...
- **Rubric ID**: 0739e81e-c949-447e-9d79-b396f3fcf9c7
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R91: Code has been implemented for using ADVI (Score)...
- **Rubric ID**: 47484f32-9338-4ff4-be18-6e0c25023ba0
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R92: Code has been implemented for using ADVI (Score)...
- **Rubric ID**: 09d74f73-bfdf-4e05-b0e3-8680f3a416be
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R93: Code has been implemented for using ADVI (Score)...
- **Rubric ID**: b60ec56e-dada-42b2-bf26-dffa3dfeb430
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R94: Code has been implemented for using ADVI (Score)...
- **Rubric ID**: 4f1c6ab7-7de3-4196-98f7-8fe0c8c72ed2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R95: Code has been implemented for using ADVI (Score)...
- **Rubric ID**: 7182ff89-b52d-47c5-88c4-1daa0f14db2d
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R96: Code has been implemented for using ADVI (Score)...
- **Rubric ID**: 364dab3a-85e6-4d19-b497-97e4d95b7176
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R97: Code has been implemented for using ADVI (Fisher)...
- **Rubric ID**: ff9c6de1-680e-431e-9c4f-beafe519df4c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R98: Code has been implemented for using ADVI (Fisher)...
- **Rubric ID**: c7639629-cbea-4374-978c-a64a4678feed
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R99: Code has been implemented for using ADVI (Fisher)...
- **Rubric ID**: acb503d6-f890-4e80-a52d-b81b152f4380
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R100: Code has been implemented for using ADVI (Fisher)...
- **Rubric ID**: 3611d925-d2e6-4630-8ec2-10f108ff4489
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R101: Code has been implemented for using ADVI (Fisher)...
- **Rubric ID**: 783db56e-960f-4c8b-886c-d480852dce1c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R102: Code has been implemented for using ADVI (Fisher)...
- **Rubric ID**: 1fbdf57f-55ca-4a24-be41-92b47ceacd2c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R103: Code has been implemented such reference samples generated...
- **Rubric ID**: f9f9945c-075b-4c5b-8dad-e17f4f855210
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such reference samples generated with Hamiltonian Monte Carlo (HMC) can be sampled for the PosteriorDB `ark` problem, at dimension D=7
- **Parent context**: Code has been implemented such reference samples generated with Hamiltonian Monte Carlo (HMC) can...

### R104: Code has been implemented such reference samples generated...
- **Rubric ID**: 9f19cb98-2466-4e19-9b9b-13460ad71d1b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such reference samples generated with Hamiltonian Monte Carlo (HMC) can be sampled for the PosteriorDB `gp-pois-regr` problem, at dimension D=13
- **Parent context**: Code has been implemented such reference samples generated with Hamiltonian Monte Carlo (HMC) can...

### R105: Code has been implemented such reference samples generated...
- **Rubric ID**: 6ffc9f02-6602-426a-b5d8-cf007613e8aa
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such reference samples generated with Hamiltonian Monte Carlo (HMC) can be sampled for the PosteriorDB `eight-schools-centered` problem, at dimension D=10
- **Parent context**: Code has been implemented such reference samples generated with Hamiltonian Monte Carlo (HMC) can...

### R106: Code has been implemented such that the score...
- **Rubric ID**: 7239250f-8ba2-4dc1-8b7a-55d21f0ce3c9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the score function for the PosteriorDB `ark` problem, at dimension D=7, can be computed (likely via bridgestan)
- **Parent context**: Code has been implemented such that the score function for specific PosteriorDB problems can be c...

### R107: Code has been implemented such that the score...
- **Rubric ID**: 15a0a7e0-5679-4cbe-81e4-767a7caaa3eb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the score function for the PosteriorDB `gp-pois-regr` problem, at dimension D=13, can be computed (likely via bridgestan)
- **Parent context**: Code has been implemented such that the score function for specific PosteriorDB problems can be c...

### R108: Code has been implemented such that the score...
- **Rubric ID**: c840a1e2-a7e5-48f3-a962-11624499939a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the score function for the PosteriorDB `eight-schools-centered` problem, at dimension D=10, can be computed (likely via bridgestan)
- **Parent context**: Code has been implemented such that the score function for specific PosteriorDB problems can be c...

### R109: Code has been implemented for using BaM to...
- **Rubric ID**: ed644299-7e44-4414-93cc-cf8bc6f7d32f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R110: Code has been implemented for using BaM to...
- **Rubric ID**: 685da7ed-db59-4ef8-9f47-017dc6f6f18a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R111: Code has been implemented for using BaM to...
- **Rubric ID**: 4422c31a-b820-4113-b883-6460a36dcae5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 8
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R112: Code has been implemented for using BaM to...
- **Rubric ID**: c7814872-24e9-4f2c-8c2e-4938f92eb838
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 32
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R113: Code has been implemented for using BaM to...
- **Rubric ID**: 7232a9c6-f4ca-4cac-b0ec-7f52d3d3ee03
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R114: Code has been implemented for using BaM to...
- **Rubric ID**: 8b33f3f6-5c3c-4a39-932b-e9117a2db7bb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R115: Code has been implemented for using GSM to...
- **Rubric ID**: ac42eb54-7ed6-4bd5-90b5-f54a21cacb7a
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R116: Code has been implemented for using GSM to...
- **Rubric ID**: 37e8141a-5a1b-4e10-9596-0dc6e6963fc5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R117: Code has been implemented for using GSM to...
- **Rubric ID**: 29399af4-02a7-475f-8549-f5ec78553bd9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 8
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R118: Code has been implemented for using GSM to...
- **Rubric ID**: f6c15b2d-56b7-4bb2-a67a-8ab93aafc3a5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 32
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R119: Code has been implemented for using GSM to...
- **Rubric ID**: f1ecdb68-2e79-4e31-a1ea-38c7002c1f06
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R120: Code has been implemented for using GSM to...
- **Rubric ID**: 7f820046-929f-4da1-add5-23d08128a931
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using GSM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R121: Code has been implemented for using ADVI to...
- **Rubric ID**: 0bc336d8-43c2-427f-84d2-c60b44ce0a76
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, w...

### R122: Code has been implemented for using ADVI to...
- **Rubric ID**: b6354d05-ee4e-47f4-8cda-a986140affef
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, w...

### R123: Code has been implemented for using ADVI to...
- **Rubric ID**: ad56b976-6194-437a-89c6-a329c4830848
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 8
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimensi...

### R124: Code has been implemented for using ADVI to...
- **Rubric ID**: ac0ae3d5-41bf-4a4e-8b5c-6c93305786e6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 32
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimensi...

### R125: Code has been implemented for using ADVI to...
- **Rubric ID**: c62b74ef-7480-40d4-8beb-b8bef5a4288b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, ...

### R126: Code has been implemented for using ADVI to...
- **Rubric ID**: 7a4e53ce-180e-4a2e-a51d-3b4f056cb482
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, ...

### R127: A variational autoencoder architecture has been implemented such...
- **Rubric ID**: b8517162-bb66-404a-af9c-39dcced08412
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: A variational autoencoder architecture has been implemented such that the encoder and decoder each consist of 5 convolutional layers.
- **Parent context**: A generative model based on a variational autoencoder architecture has been implemented as outlin...

### R128: The generative model has been implemented such that...
- **Rubric ID**: fd19a4f4-ca51-4978-bcb4-73b45e2aa418
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The generative model has been implemented such that it models the images using a Gaussian Likelihood over the distribution of images
- **Parent context**: A generative model based on a variational autoencoder architecture has been implemented as outlin...

### R129: The generative model has been implemented such that...
- **Rubric ID**: b8a1676d-4cd0-4397-b4a9-c91b70d1bfaf
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The generative model has been implemented such that its Gaussian likelihood is parameterized by a neural network (decoder) that takes the latent variable as input and outputs the mean of the Gaussian distribution.
- **Parent context**: A generative model based on a variational autoencoder architecture has been implemented as outlin...

### R130: The generative model's gaussian likelihood has been implemented...
- **Rubric ID**: c8f3e04d-9187-4949-91f9-8f363785ffc3
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The generative model's gaussian likelihood has been implemented such that the covariance is fixed to $\sigma^2 I$, where $I$ is the identity matrix and $\sigma^2$ is fixed to 0.1
- **Parent context**: A generative model based on a variational autoencoder architecture has been implemented as outlin...

### R131: The variational autoencoder hyperparameters and architecture generally align...
- **Rubric ID**: a8db3546-d879-4a06-b6a8-ffc58050515c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The variational autoencoder hyperparameters and architecture generally align with what is outlined in the addendum
- **Parent context**: A generative model based on a variational autoencoder architecture has been implemented as outlin...

### R132: Code has been implemented such that the score...
- **Rubric ID**: 81ac357b-830a-4bad-9305-04a91ed77285
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the score function for the posterior ($s(z) = \nabla_z \log p(z \mid x) = \nabla_z \log p(z) + \nabla_z \log p(x \mid z), $ where $p(x \mid z)$ is the decoder network) can be computed (likely via an autodiff solution)
- **Parent context**: Various variational inference methods have been run at various batch sizes to reconstruct a sampl...

### R133: Code has been implemented such that the estimated...
- **Rubric ID**: 30cfc3c2-025c-427d-9e7f-abc61292eaeb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the estimated mean from a given VI method can be input into the decoder so to obtain the reconstructed image
- **Parent context**: Various variational inference methods have been run at various batch sizes to reconstruct a sampl...

### R134: Code has been implemented such that the estimated...
- **Rubric ID**: 4b88bdfd-4056-4cf0-bfc7-86c59aea7047
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the estimated mean from BaM can be input into the decoder at each iteration so to obtain the reconstructed image at that iteration
- **Parent context**: BaM has been run at various batch sizes to reconstruct the sampled test image, and its performanc...

### R135: Code has been implemented such that the estimated...
- **Rubric ID**: 1599c293-f743-42a6-b270-2811a12d44b5
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the estimated mean from ADVI can be input into the decoder at each iteration so to obtain the reconstructed image at that iteration
- **Parent context**: ADVI has been run at various batch sizes to reconstruct the sampled test image, and its performan...

### R136: Code has been implemented such that ADVI can...
- **Rubric ID**: 84a43414-e9c3-4765-aa3a-848b1b8b2014
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that ADVI can be run at batch size 10 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: ADVI has been run at batch size 10 to reconstruct the sampled test image

### R137: Code has been implemented such that ADVI can...
- **Rubric ID**: 7d45f253-70e1-4f43-b68c-1653ae3e38dd
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that ADVI can be run at batch size 300 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: ADVI has been run at batch size 300 to reconstruct the sampled test image

### R138: Code has been implemented such that the estimated...
- **Rubric ID**: 746cbd4c-1558-49ad-bba3-abe9a8fd7c3f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the estimated mean from GSM can be input into the decoder at each iteration so to obtain the reconstructed image at that iteration
- **Parent context**: GSM has been run at various batch sizes to reconstruct the sampled test image, and its performanc...

### R139: Code has been implemented such that GSM can...
- **Rubric ID**: a86e824a-6bc5-41c6-ab6c-89b8797d42a6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that GSM can be run at batch size 10 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: GSM has been run at batch size 10 to reconstruct the sampled test image

### R140: Code has been implemented such that the estimated...
- **Rubric ID**: 97ed714b-be12-420d-8cec-37c94e7c1c82
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the estimated mean from AVI (the trained encoder network) can be input into the decoder so to obtain the reconstructed image
- **Parent context**: AVI (the trained encoder network) has been run to reconstruct the sampled test image, and its per...

### R141: Code has been implemented such that AVI (the...
- **Rubric ID**: f0dbb6ed-4360-4315-b5ea-5f837cfcdb39
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been implemented such that AVI (the trained encoder network) can be run at to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: AVI (the trained encoder network) has been run to reconstruct the sampled test image, and its per...

## Data Processing & Preparation

### R142: Code has been implemented such that the CIFAR...
- **Rubric ID**: 6679061e-6501-4e0f-8e1a-ca8470bdcd2e
- **Category**: Code Development / Data Processing & Preparation
- **Weight**: 1
- **Requirement**: Code has been implemented such that the CIFAR 10 dataset can be used
- **Parent context**: The CIFAR 10 dataset has been acquired

## Dataset & Model Acquisition

### R143: Code has been implemented such that an image...
- **Rubric ID**: 7beb3412-0366-4f3f-93c6-814a5968ca47
- **Category**: Code Development / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been implemented such that an image x' can be sampled from the CIFAR 10 image dataset test split
- **Parent context**: An image x' has been drawn from the CIFAR 10 image dataset test split

## Experimental Setup (Development)

### R144: Code has been implemented such that when using...
- **Rubric ID**: 62a0b2d7-6925-465d-8a76-f56a15dbb1a4
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using BaM to estimate the posterior of a D-dimensional Gaussian distribution, the learning rate can be set to DB, where B is the batch size
- **Parent context**: BaM has been run to estimate the posterior of Gaussian distributions of increasing number of dime...

### R145: Code has been implemented such that when using...
- **Rubric ID**: 3e177584-01ab-47bf-80c3-ee4c2d54091b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using BaM to estimate the posterior of a D-dimensional Gaussian distribution, BaM VI can be run for at least 10E4 iterations
- **Parent context**: BaM has been run to estimate the posterior of Gaussian distributions of increasing number of dime...

### R146: Code has been implemented such that 10 separate...
- **Rubric ID**: 40da5875-e968-42dd-86bc-eed6c375b427
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10 separate seeded runs of BaM VI for estimating the posterior of a D-dimensional Gaussian distribution over some number of iterations can be run.
- **Parent context**: BaM has been run to estimate the posterior of Gaussian distributions of increasing number of dime...

### R147: Code has been implemented such that when using...
- **Rubric ID**: 67253f08-1f31-4efe-b7d9-90f95a0de792
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using GSM to estimate the posterior of a D-dimensional Gaussian distribution, GSM can be run for at least 10E4 iterations
- **Parent context**: GSM has been run to estimate the posterior of Gaussian distributions of increasing number of dime...

### R148: Code has been implemented such that 10 separate...
- **Rubric ID**: b4146816-ff82-4eda-8456-7d042446eb19
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10 separate seeded runs of GSM for estimating the posterior of a D-dimensional Gaussian distribution over some number of iterations can be run.
- **Parent context**: GSM has been run to estimate the posterior of Gaussian distributions of increasing number of dime...

### R149: Code has been implemented such that when using...
- **Rubric ID**: e7325915-a008-4954-be0e-5901babcf792
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using ADVI to estimate the posterior of a D-dimensional Gaussian distribution, ADVI can be run for at least 10E4 iterations
- **Parent context**: ADVI has been run to estimate the posterior of Gaussian distributions of increasing number of dim...

### R150: Code has been implemented such that 10 separate...
- **Rubric ID**: f032d17c-4130-4ec1-8c53-84352d28a0d0
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10 separate seeded runs of ADVI for estimating the posterior of a D-dimensional Gaussian distribution over some number of iterations can be run.
- **Parent context**: ADVI has been run to estimate the posterior of Gaussian distributions of increasing number of dim...

### R151: Code has been implemented for using ADVI to...
- **Rubric ID**: e7397fe9-b5fb-4473-beb9-6104e66f8d5a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented for using ADVI to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch s...

### R152: Code has been implemented such that a grid...
- **Rubric ID**: 61156dc6-1267-4e9e-b920-d98b26a9fbc7
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of a 4-dimensional Gaussian distributionwith batch size 2.
- **Parent context**: ADVI has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch s...

### R153: Code has been implemented such that a grid...
- **Rubric ID**: 3e0ca9f4-b0d4-4003-88fe-7ec12a8875fa
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of a 16-dimensional Gaussian distributionwith batch size 2.
- **Parent context**: ADVI has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch ...

### R154: Code has been implemented such that a grid...
- **Rubric ID**: ff651be2-f063-4e2b-a0a5-03bdb3b396dc
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of a 64-dimensional Gaussian distributionwith batch size 2.
- **Parent context**: ADVI has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch ...

### R155: Code has been implemented such that a grid...
- **Rubric ID**: 46ffe5e8-1cfb-4d74-851d-6304a8063fd3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of a 256-dimensional Gaussian distributionwith batch size 2.
- **Parent context**: ADVI has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch...

### R156: Code has been implemented such that when using...
- **Rubric ID**: 0769c811-66e6-45e5-94aa-59575d21db68
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using ADVI (Score) to estimate the posterior of a D-dimensional Gaussian distribution, ADVI (Score) can be run for at least 10E4 iterations
- **Parent context**: ADVI (Score) has been run to estimate the posterior of Gaussian distributions of increasing numbe...

### R157: Code has been implemented such that 10 separate...
- **Rubric ID**: 19c30243-6859-41b1-a85c-bec6a3535bec
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10 separate seeded runs of ADVI (Score) for estimating the posterior of a D-dimensional Gaussian distribution over some number of iterations can be run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of Gaussian distributions of increasing numbe...

### R158: Code has been implemented such that a grid...
- **Rubric ID**: 172fbeea-8142-445b-b94d-8349006f4659
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Score) to estimate the posterior of a 4-dimensional Gaussian distributionwith batch size 2.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 4-dimensional Gaussian distribution with...

### R159: Code has been implemented such that a grid...
- **Rubric ID**: 84ce8524-3641-45ad-ae93-fe86a2794769
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Score) to estimate the posterior of a 16-dimensional Gaussian distributionwith batch size 2.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wit...

### R160: Code has been implemented such that a grid...
- **Rubric ID**: 8041942c-0edc-4736-a9ba-d62b6e51a547
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Score) to estimate the posterior of a 64-dimensional Gaussian distributionwith batch size 2.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wit...

### R161: Code has been implemented such that a grid...
- **Rubric ID**: 939854ba-18eb-43aa-b498-afb29d6f3e7a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Score) to estimate the posterior of a 256-dimensional Gaussian distributionwith batch size 2.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 256-dimensional Gaussian distribution wi...

### R162: Code has been implemented such that when using...
- **Rubric ID**: 61d2a7ac-d780-45ed-8a66-641d136f208c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using ADVI (Fisher) to estimate the posterior of a D-dimensional Gaussian distribution, ADVI (Fisher) can be run for at least 10E4 iterations
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of Gaussian distributions of increasing numb...

### R163: Code has been implemented such that 10 separate...
- **Rubric ID**: 9e1d9e27-a62f-4135-aeec-ef3ebc8fcc62
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10 separate seeded runs of ADVI (Fisher) for estimating the posterior of a D-dimensional Gaussian distribution over some number of iterations can be run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of Gaussian distributions of increasing numb...

### R164: Code has been implemented such that a grid...
- **Rubric ID**: c4f07ed3-ec49-4ef7-9525-3bde733d1392
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 4-dimensional Gaussian distributionwith batch size 2.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 4-dimensional Gaussian distribution wit...

### R165: Code has been implemented such that a grid...
- **Rubric ID**: a25779c4-d2c7-41ed-af59-44e5971c2f54
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 16-dimensional Gaussian distributionwith batch size 2.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wi...

### R166: Code has been implemented such that a grid...
- **Rubric ID**: bb986eed-e15a-49b3-a549-7478c9939fda
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 64-dimensional Gaussian distributionwith batch size 2.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wi...

### R167: Code has been implemented such that a grid...
- **Rubric ID**: 91e7d1da-8692-4dcd-abf3-d5d84c693da9
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 256-dimensional Gaussian distributionwith batch size 2.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 256-dimensional Gaussian distribution w...

### R168: Code has been implemented such that when using...
- **Rubric ID**: 9dad0b0e-0c6b-40c5-835d-dd2ab6bafb51
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using BaM to estimate the posterior of a given 10-dimensional sinh-arcsinh normal distribution, the learning rate can be set to $10B/(t+1)$, where B is the batch size and t is the iteration
- **Parent context**: BaM has been run to estimate the posterior of 10-dimensional sinh-arcsinh normal distributions wi...

### R169: Code has been implemented such that 10 separate...
- **Rubric ID**: 6c1197c7-b2fa-488b-aeda-ec8adf3005cb
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10 separate seeded runs of BaM VI for estimating the posterior of a given 10-dimensional sinh-arcsinh normal distribution over some number of iterations can be run.
- **Parent context**: BaM has been run to estimate the posterior of 10-dimensional sinh-arcsinh normal distributions wi...

### R170: Code has been implemented such that 10 separate...
- **Rubric ID**: 744581d5-a97d-4383-b7cf-69cac8983134
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10 separate seeded runs of GSM VI for estimating the posterior of a given 10-dimensional sinh-arcsinh normal distribution over some number of iterations can be run.
- **Parent context**: GSM has been run to estimate the posterior of 10-dimensional sinh-arcsinh normal distributions wi...

### R171: Code has been implemented such that when using...
- **Rubric ID**: b9339ea4-d945-4a13-889e-8e7e253b73f1
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using ADVI to estimate the posterior of a given 10-dimensional sinh-arcsinh normal distribution, ADVI can be run for at least 10E4 iterations
- **Parent context**: ADVI has been run to estimate the posterior of 10-dimensional sinh-arcsinh normal distributions w...

### R172: Code has been implemented such that 10 separate...
- **Rubric ID**: 345dd995-ef53-4c4c-85d1-07e57c6ae488
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10 separate seeded runs of ADVI for estimating the posterior of a given 10-dimensional sinh-arcsinh normal distribution over some number of iterations can be run.
- **Parent context**: ADVI has been run to estimate the posterior of 10-dimensional sinh-arcsinh normal distributions w...

### R173: Code has been implemented such that a grid...
- **Rubric ID**: 151d6cf2-a85a-4c1c-b23a-791ac01fb763
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R174: Code has been implemented such that a grid...
- **Rubric ID**: 99555c45-00b7-4afb-a985-b6e6c2a41ed2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R175: Code has been implemented such that a grid...
- **Rubric ID**: 78d157ac-fdde-4959-aa3f-440cdb052670
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R176: Code has been implemented such that a grid...
- **Rubric ID**: 8c63d9a0-c069-47a8-a3b7-0cb083625beb
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R177: Code has been implemented such that a grid...
- **Rubric ID**: 581aeb9c-e314-4c6c-a7fd-8e9b8b3b95f9
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R178: Code has been implemented such that a grid...
- **Rubric ID**: 43a93dcb-54d0-4b76-b720-0c96a293d2ef
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R179: Code has been implemented such that when using...
- **Rubric ID**: 104d165c-6498-4083-9f39-c00307a4d24d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using ADVI (Score) to estimate the posterior of a given 10-dimensional sinh-arcsinh normal distribution, ADVI (Score) can be run for at least 10E4 iterations
- **Parent context**: ADVI (Score) has been run to estimate the posterior of 10-dimensional sinh-arcsinh normal distrib...

### R180: Code has been implemented such that 10 separate...
- **Rubric ID**: b7cbd6a7-e4cb-4343-b584-45c8b590b754
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10 separate seeded runs of ADVI (Score) for estimating the posterior of a given 10-dimensional sinh-arcsinh normal distribution over some number of iterations can be run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of 10-dimensional sinh-arcsinh normal distrib...

### R181: Code has been implemented such that a grid...
- **Rubric ID**: c28c357e-51c7-4c82-9011-aedd051e2e62
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R182: Code has been implemented such that a grid...
- **Rubric ID**: e1ecd6ff-25a2-4d3f-8cf6-6d50728e25b8
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R183: Code has been implemented such that a grid...
- **Rubric ID**: a9c3cf98-0dd9-43e0-881c-36ecc33a31d3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R184: Code has been implemented such that a grid...
- **Rubric ID**: 9ff3a320-5fbd-429e-b64f-71ad91d63241
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R185: Code has been implemented such that a grid...
- **Rubric ID**: f16ba270-2409-478a-a96b-c46c8c58b69a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R186: Code has been implemented such that a grid...
- **Rubric ID**: 50150783-5232-47c4-9ec8-142221692edb
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R187: Code has been implemented such that when using...
- **Rubric ID**: f7235cbe-8bcf-4a59-8cce-df226dd72b43
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using ADVI (Fisher) to estimate the posterior of a given 10-dimensional sinh-arcsinh normal distribution, ADVI (Fisher) can be run for at least 10E4 iterations
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of 10-dimensional sinh-arcsinh normal distri...

### R188: Code has been implemented such that 10 separate...
- **Rubric ID**: 5076880c-8fc8-451b-be3f-edb03aca043a
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that 10 separate seeded runs of ADVI (Fisher) for estimating the posterior of a given 10-dimensional sinh-arcsinh normal distribution over some number of iterations can be run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of 10-dimensional sinh-arcsinh normal distri...

### R189: Code has been implemented such that a grid...
- **Rubric ID**: ac7f12f4-4ce6-4cb4-ba48-524f2d85a5e9
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R190: Code has been implemented such that a grid...
- **Rubric ID**: 2c9bea44-6f86-4921-8237-de3682f56b51
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R191: Code has been implemented such that a grid...
- **Rubric ID**: a08fb80c-5d38-449a-b7f6-88934d994941
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R192: Code has been implemented such that a grid...
- **Rubric ID**: 42c5cdbc-3ebc-410a-b344-410a4ac23ff1
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R193: Code has been implemented such that a grid...
- **Rubric ID**: 19bd3493-e961-46ef-af83-cdd01652e8d2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R194: Code has been implemented such that a grid...
- **Rubric ID**: 3e03d0cf-4147-4124-a77f-ab985b3f6ef3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R195: Code has been implemented such that when using...
- **Rubric ID**: 709db886-9aa9-417e-9a16-ceebfd811410
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using BaM to estimate the posterior of a given PosteriorDB problem, the learning rate can be set to $DB/(t+1)$, where B is the batch size and t is the iteration
- **Parent context**: BaM has been run to estimate the posterior of a PosteriorDB models at batch size 8 and batch size 32

### R196: Code has been implemented such that when using...
- **Rubric ID**: 497dfe00-c70d-47bb-91d9-3587ddbf8091
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using BaM to estimate the posterior of a given PosteriorDB problem, BaM can be run for at least 10E4 iterations
- **Parent context**: BaM has been run to estimate the posterior of a PosteriorDB models at batch size 8 and batch size 32

### R197: Code has been implemented such that 5 separate...
- **Rubric ID**: f7954dbd-e5b3-474a-854b-8919c0b410d9
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that 5 separate seeded runs of BaM for estimating the posterior of a given of a given PosteriorDB problem over some number of iterations can be run.
- **Parent context**: BaM has been run to estimate the posterior of a PosteriorDB models at batch size 8 and batch size 32

### R198: Code has been implemented such that when using...
- **Rubric ID**: 3ac18481-c1f5-4849-b5f2-689da200fa11
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using GSM to estimate the posterior of a given PosteriorDB problem, GSM can be run for at least 10E4 iterations
- **Parent context**: GSM has been run to estimate the posterior of a PosteriorDB models at batch size 8 and batch size 32

### R199: Code has been implemented such that 5 separate...
- **Rubric ID**: 018a3825-2b17-4db9-91d2-d13a8f316a43
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that 5 separate seeded runs of GSM for estimating the posterior of a given of a given PosteriorDB problem over some number of iterations can be run.
- **Parent context**: GSM has been run to estimate the posterior of a PosteriorDB models at batch size 8 and batch size 32

### R200: Code has been implemented such that when using...
- **Rubric ID**: 874b6134-7a33-4846-b7bb-241ca7b8ded0
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using ADVI to estimate the posterior of a given PosteriorDB problem, ADVI can be run for at least 10E4 iterations
- **Parent context**: ADVI has been run to estimate the posterior of a PosteriorDB models at batch size 8 and batch siz...

### R201: Code has been implemented such that 5 separate...
- **Rubric ID**: 5cf2de1a-b303-47c0-9d25-f891119e4f9e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that 5 separate seeded runs of ADVI for estimating the posterior of a given of a given PosteriorDB problem over some number of iterations can be run.
- **Parent context**: ADVI has been run to estimate the posterior of a PosteriorDB models at batch size 8 and batch siz...

### R202: Code has been implemented such that a grid...
- **Rubric ID**: 6e37cfd8-6369-4d00-bcc4-eed046d72b6b
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, w...

### R203: Code has been implemented such that a grid...
- **Rubric ID**: c30c6c6e-9733-4feb-a697-5869ede43aae
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, w...

### R204: Code has been implemented such that a grid...
- **Rubric ID**: 677188c1-0004-4404-848f-59765d1e7547
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 8
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimensi...

### R205: Code has been implemented such that a grid...
- **Rubric ID**: 248c1684-7468-466b-af35-1a0b6001a6f0
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 32
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimensi...

### R206: Code has been implemented such that a grid...
- **Rubric ID**: 57e4a6f5-98a7-470e-b120-bf29b56dfbfd
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, ...

### R207: Code has been implemented such that a grid...
- **Rubric ID**: ccc48c89-f32f-470a-9111-cf4e33a3ce33
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a grid search can be run for determining the optimal learning rate for using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, ...

### R208: Code has been implemented such that a VAE...
- **Rubric ID**: 5bcc62df-5cf7-4978-9fd8-b581f66848ed
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a VAE can be trained on the CIFAR 10 image dataset training split following the standard VAE training procedure from Kingma & Welling, 2014 described in Appendix E.6
- **Parent context**: Code has been implemented such that a VAE can be trained on the CIFAR 10 image dataset training s...

### R209: Code has been implemented such that a VAE...
- **Rubric ID**: 8d91ae75-4503-4268-a56b-67fb863db0ed
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a VAE can be trained on the CIFAR 10 image dataset training split for 100 epochs
- **Parent context**: Code has been implemented such that a VAE can be trained on the CIFAR 10 image dataset training s...

### R210: Code has been implemented such that a VAE...
- **Rubric ID**: 265cfd4c-8965-4a27-83b1-949da54c932f
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a VAE can be trained on the CIFAR 10 image dataset generally following the training hyperparameters outlined in the addendum
- **Parent context**: Code has been implemented such that a VAE can be trained on the CIFAR 10 image dataset training s...

### R211: Code has been implemented such that when using...
- **Rubric ID**: 9136b526-737a-452d-9b48-221ac549d532
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using BaM to reconstruct the sampled test image, BaM can be run for at least 1000 iterations
- **Parent context**: BaM has been run at various batch sizes to reconstruct the sampled test image, and its performanc...

### R212: Code has been implemented such that BaM can...
- **Rubric ID**: 92f8164c-6afa-41fe-9b33-1bcc20080e63
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that BaM can be run at batch size 10 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: BaM has been run at batch size 10 to reconstruct the sampled test image

### R213: Code has been implemented such that a preliminary...
- **Rubric ID**: 4bab7e9b-02aa-40b0-9e22-cf86cd8eb3fd
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a preliminary grid search on 100 iterations can be run for determining the optimal learning rate for using BaM at batch size 10 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: BaM has been run at batch size 10 to reconstruct the sampled test image

### R214: Code has been implemented such that BaM can...
- **Rubric ID**: 5cf24aad-ca74-445b-a873-0d12fb447b3c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that BaM can be run at batch size 100 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: BaM has been run at batch size 100 to reconstruct the sampled test image

### R215: Code has been implemented such that a preliminary...
- **Rubric ID**: 362a7e97-2a07-4f20-af41-e4af3850bebf
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a preliminary grid search on 100 iterations can be run for determining the optimal learning rate for using BaM at batch size 100 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: BaM has been run at batch size 100 to reconstruct the sampled test image

### R216: Code has been implemented such that BaM can...
- **Rubric ID**: 65d88f8d-7c64-46cc-8a72-04e72441e024
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that BaM can be run at batch size 300 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: BaM has been run at batch size 300 to reconstruct the sampled test image

### R217: Code has been implemented such that a preliminary...
- **Rubric ID**: 50ae9c10-4481-4a89-9944-f71198459a83
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a preliminary grid search on 100 iterations can be run for determining the optimal learning rate for using BaM at batch size 300 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: BaM has been run at batch size 300 to reconstruct the sampled test image

### R218: Code has been implemented such that when using...
- **Rubric ID**: 16a7fbdb-d257-4ec0-af3e-0ce49bd9f60d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using ADVI to reconstruct the sampled test image, ADVI can be run for at least 1000 iterations
- **Parent context**: ADVI has been run at various batch sizes to reconstruct the sampled test image, and its performan...

### R219: Code has been implemented such that a preliminary...
- **Rubric ID**: c8c170eb-d12f-4546-bb75-f8376596c8f3
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a preliminary grid search on 100 iterations can be run for determining the optimal learning rate for using ADVI at batch size 10 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: ADVI has been run at batch size 10 to reconstruct the sampled test image

### R220: Code has been implemented such that ADVI can...
- **Rubric ID**: 8c7c43b4-481e-42ec-b699-91855feb3bc6
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that ADVI can be run at batch size 100 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: ADVI has been run at batch size 100 to reconstruct the sampled test image

### R221: Code has been implemented such that a preliminary...
- **Rubric ID**: 6ff69661-d1fe-4cac-9f73-70ad6ab25df2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a preliminary grid search on 100 iterations can be run for determining the optimal learning rate for using ADVI at batch size 100 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: ADVI has been run at batch size 100 to reconstruct the sampled test image

### R222: Code has been implemented such that a preliminary...
- **Rubric ID**: e8ae0196-2a93-4226-8043-70544c914c2d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that a preliminary grid search on 100 iterations can be run for determining the optimal learning rate for using ADVI at batch size 300 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: ADVI has been run at batch size 300 to reconstruct the sampled test image

### R223: Code has been implemented such that when using...
- **Rubric ID**: f3e2ff6e-c0b8-4b54-aee6-8285452f6000
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that when using GSM to reconstruct the sampled test image, GSM can be run for at least 1000 iterations
- **Parent context**: GSM has been run at various batch sizes to reconstruct the sampled test image, and its performanc...

### R224: Code has been implemented such that GSM can...
- **Rubric ID**: 586b4963-d082-4d8d-8640-8055030820f6
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that GSM can be run at batch size 100 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: GSM has been run at batch size 100 to reconstruct the sampled test image

### R225: Code has been implemented such that GSM can...
- **Rubric ID**: 83b55f93-fb44-4259-909c-f3d5e529ab11
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been implemented such that GSM can be run at batch size 300 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: GSM has been run at batch size 300 to reconstruct the sampled test image

## Evaluation & Metrics Implementation

### R226: Code has been implemented for measuring the forward...
- **Rubric ID**: 337c5085-020c-41ec-b709-ad49ad7dd776
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented for measuring the forward and reverse empirical KL divergences between two distributions
- **Parent context**: The results of section 5.1 have been replicated

### R227: Code has been implemented such that the forward...
- **Rubric ID**: 39daebb5-af71-4d2e-a031-5379296040f0
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the forward empirical KL divergences between the estimated and target posterior can be measured at each iteration when using BaM to estimate the posterior of a D-dimensional Gaussian distribution
- **Parent context**: Code has been implemented such that the forward and reverse empirical KL divergences between the ...

### R228: Code has been implemented such that the reverse...
- **Rubric ID**: 71097d28-3052-4d89-8810-3d88cde79c5a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the reverse empirical KL divergences between the estimated and target posterior can be measured at each iteration when using BaM to estimate the posterior of a D-dimensional Gaussian distribution
- **Parent context**: Code has been implemented such that the forward and reverse empirical KL divergences between the ...

### R229: Code has been implemented such that the forward...
- **Rubric ID**: e80199a9-f837-4938-9e58-528b9708dcd8
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the forward and reverse empirical KL divergences between the estimated and target posterior can be measured at each iteration when using GSM to estimate the posterior of a D-dimensional Gaussian distribution
- **Parent context**: GSM has been run to estimate the posterior of Gaussian distributions of increasing number of dime...

### R230: Code has been implemented such that the forward...
- **Rubric ID**: a6f9be76-1337-4d55-be38-09686b2fe584
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the forward and reverse empirical KL divergences between the estimated and target posterior can be measured at each iteration when using ADVI to estimate the posterior of a D-dimensional Gaussian distribution
- **Parent context**: ADVI has been run to estimate the posterior of Gaussian distributions of increasing number of dim...

### R231: Code has been implemented such that the forward...
- **Rubric ID**: b98057f9-dfc7-48a8-8cf7-c1c15e91bb2e
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the forward and reverse empirical KL divergences between the estimated and target posterior can be measured at each iteration when using ADVI (Score) to estimate the posterior of a D-dimensional Gaussian distribution
- **Parent context**: ADVI (Score) has been run to estimate the posterior of Gaussian distributions of increasing numbe...

### R232: Code has been implemented such that the forward...
- **Rubric ID**: b9955d65-6a91-45cd-ba42-223b663f3917
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the forward and reverse empirical KL divergences between the estimated and target posterior can be measured at each iteration when using ADVI (Fisher) to estimate the posterior of a D-dimensional Gaussian distribution
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of Gaussian distributions of increasing numb...

### R233: Code has been implemented such that the forward...
- **Rubric ID**: c32b5a87-6ee1-46ac-8dd2-6e0754ced64d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the forward empirical KL divergences between the estimated and target posterior can be measured at each iteration when using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distributions with different skew and tail configurations
- **Parent context**: Code has been implemented such that the forward and reverse empirical KL divergences between the ...

### R234: Code has been implemented such that the reverse...
- **Rubric ID**: 97d94811-06df-4099-9354-e5174ec8d24a
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the reverse empirical KL divergences between the estimated and target posterior can be measured at each iteration when using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distributions with different skew and tail configurations
- **Parent context**: Code has been implemented such that the forward and reverse empirical KL divergences between the ...

### R235: Code has been implemented such that the forward...
- **Rubric ID**: 98d97674-932f-4271-be5e-d436fceebb2d
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the forward empirical KL divergences between the estimated and target posterior can be measured at each iteration when using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distributions with different skew and tail configurations
- **Parent context**: Code has been implemented such that the forward and reverse empirical KL divergences between the ...

### R236: Code has been implemented such that the reverse...
- **Rubric ID**: 5bfa1a7d-5ce7-4e96-b14e-1ee9791e5fe1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the reverse empirical KL divergences between the estimated and target posterior can be measured at each iteration when using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distributions with different skew and tail configurations
- **Parent context**: Code has been implemented such that the forward and reverse empirical KL divergences between the ...

### R237: Code has been implemented such that the forward...
- **Rubric ID**: a7cc727d-358e-48f8-b95d-b5cbbf3cb1e1
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the forward empirical KL divergences between the estimated and target posterior can be measured at each iteration when using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distributions with different skew and tail configurations
- **Parent context**: Code has been implemented such that the forward and reverse empirical KL divergences between the ...

### R238: Code has been implemented such that the reverse...
- **Rubric ID**: e2f0b6d2-5706-4e29-8b96-6ae2bcee1e32
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the reverse empirical KL divergences between the estimated and target posterior can be measured at each iteration when using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distributions with different skew and tail configurations
- **Parent context**: Code has been implemented such that the forward and reverse empirical KL divergences between the ...

### R239: Code has been implemented such that the forward...
- **Rubric ID**: 4aa82457-3a6e-42bf-8475-a7a8e6630a9c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the forward empirical KL divergences between the estimated and target posterior can be measured at each iteration when using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distributions with different skew and tail configurations
- **Parent context**: Code has been implemented such that the forward and reverse empirical KL divergences between the ...

### R240: Code has been implemented such that the reverse...
- **Rubric ID**: 505ef52e-2a68-4a7f-91b0-72c054e6afac
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the reverse empirical KL divergences between the estimated and target posterior can be measured at each iteration when using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distributions with different skew and tail configurations
- **Parent context**: Code has been implemented such that the forward and reverse empirical KL divergences between the ...

### R241: Code has been implemented such that the forward...
- **Rubric ID**: 0c565abe-eaf8-476b-94ca-8f7b0a0722a9
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the forward empirical KL divergences between the estimated and target posterior can be measured at each iteration when using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distributions with different skew and tail configurations
- **Parent context**: Code has been implemented such that the forward and reverse empirical KL divergences between the ...

### R242: Code has been implemented such that the reverse...
- **Rubric ID**: f3d53b04-002f-4590-b67d-52ad1b1f38ff
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the reverse empirical KL divergences between the estimated and target posterior can be measured at each iteration when using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distributions with different skew and tail configurations
- **Parent context**: Code has been implemented such that the forward and reverse empirical KL divergences between the ...

### R243: Code has been implemented such that the relative...
- **Rubric ID**: 5afd823b-fe2e-43cc-96c6-74e61e317389
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the relative mean error between a given pair of estimated and HMC posterior parameters can be computed, as outlined in equation (242) in Appendix E.5
- **Parent context**: Code has been implemented such that the relative mean error and relative standard error between a...

### R244: Code has been implemented such that the relative...
- **Rubric ID**: 8cb1d179-bf13-4d66-976f-4fefc362dfa4
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the relative standard error between a given pair of estimated and HMC posterior parameters can be computed, as outlined in equation (242) in Appendix E.5
- **Parent context**: Code has been implemented such that the relative mean error and relative standard error between a...

### R245: Code has been implemented such that the relative...
- **Rubric ID**: dba97644-7829-4b04-8873-38341ad8ca7b
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the relative mean error between a given pair of estimated and HMC posterior parameters can be measured at each iteration when using BaM to estimate the posterior of a given PosteriorDB problem
- **Parent context**: Code has been implemented such that the relative mean error and relative standard error between a...

### R246: Code has been implemented such that the relative...
- **Rubric ID**: 9b48b917-da7f-4bd1-b175-0bb7c4fda3e5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the relative standard error between a given pair of estimated and HMC posterior parameters can be measured at each iteration when using BaM to estimate the posterior of a given PosteriorDB problem
- **Parent context**: Code has been implemented such that the relative mean error and relative standard error between a...

### R247: Code has been implemented such that the relative...
- **Rubric ID**: 05aa3933-138f-49b4-b3b9-469bfe492df5
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the relative mean error between a given pair of estimated and HMC posterior parameters can be measured at each iteration when using GSM to estimate the posterior of a given PosteriorDB problem
- **Parent context**: Code has been implemented such that the relative mean error and relative standard error between a...

### R248: Code has been implemented such that the relative...
- **Rubric ID**: 84424446-0e76-485a-8f9f-cc4a33077589
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the relative standard error between a given pair of estimated and HMC posterior parameters can be measured at each iteration when using GSM to estimate the posterior of a given PosteriorDB problem
- **Parent context**: Code has been implemented such that the relative mean error and relative standard error between a...

### R249: Code has been implemented such that the relative...
- **Rubric ID**: c973e81f-cac5-4248-9a1f-80e51b2fa1d7
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the relative mean error between a given pair of estimated and HMC posterior parameters can be measured at each iteration when using ADVI to estimate the posterior of a given PosteriorDB problem
- **Parent context**: Code has been implemented such that the relative mean error and relative standard error between a...

### R250: Code has been implemented such that the relative...
- **Rubric ID**: f8f8ec14-3d78-409e-bfaa-114c288f3873
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the relative standard error between a given pair of estimated and HMC posterior parameters can be measured at each iteration when using ADVI to estimate the posterior of a given PosteriorDB problem
- **Parent context**: Code has been implemented such that the relative mean error and relative standard error between a...

### R251: Code has been implemented such that the Mean...
- **Rubric ID**: 1d9d9df5-f7a5-40e4-800a-705d831371af
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the Mean Squared Error (MSE) between two images can be computed
- **Parent context**: Various variational inference methods have been run at various batch sizes to reconstruct a sampl...

### R252: Code has been implemented such that the MSE...
- **Rubric ID**: c447e67b-342e-47b4-bd00-a434bfd9bbbc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the MSE between reconstructed image obtained from BaM and the sampled test image can be computed at each iteration
- **Parent context**: BaM has been run at various batch sizes to reconstruct the sampled test image, and its performanc...

### R253: Code has been implemented such that the MSE...
- **Rubric ID**: dbea0f87-17b9-443d-85ba-04f9f67a084c
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the MSE between reconstructed image obtained from ADVI and the sampled test image can be computed at each iteration
- **Parent context**: ADVI has been run at various batch sizes to reconstruct the sampled test image, and its performan...

### R254: Code has been implemented such that the MSE...
- **Rubric ID**: f13eba45-776d-4dd6-8e04-8eaa468413b3
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the MSE between reconstructed image obtained from GSM and the sampled test image can be computed at each iteration
- **Parent context**: GSM has been run at various batch sizes to reconstruct the sampled test image, and its performanc...

### R255: Code has been implemented such that the MSE...
- **Rubric ID**: 34cd15c2-47e3-4cc5-86a1-ca64733d35e2
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been implemented such that the MSE between reconstructed image obtained from AVI (the trained encoder network) and the sampled test image can be computed
- **Parent context**: AVI (the trained encoder network) has been run to reconstruct the sampled test image, and its per...

## Code Execution — Method

### R256: AVI (the trained encoder network) has been run...
- **Rubric ID**: 1a663a4f-d707-48d1-9a22-5bcf121b6fd3
- **Category**: Code Execution / Method Implementation
- **Weight**: 1
- **Requirement**: AVI (the trained encoder network) has been run to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: AVI (the trained encoder network) has been run to reconstruct the sampled test image, and its per...

## Code Execution — Dataset/Model Acquisition

### R257: Code has been executed such that the CIFAR...
- **Rubric ID**: 8789e782-2545-4758-a973-0f751ae6ea49
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: Code has been executed such that the CIFAR 10 dataset can be used (e.g. the dataset has been downloaded and other experiments in the reproduction can use it)
- **Parent context**: The CIFAR 10 dataset has been acquired

### R258: An image x' has been sampled from the...
- **Rubric ID**: fb40e7cd-4686-4df4-a152-9f787361db7d
- **Category**: Code Execution / Dataset and Model Acquisition
- **Weight**: 1
- **Requirement**: An image x' has been sampled from the CIFAR 10 image dataset test split
- **Parent context**: An image x' has been drawn from the CIFAR 10 image dataset test split

## Code Execution — Experimental Setup

### R259: BaM has been run to estimate the posterior...
- **Rubric ID**: 1876119e-93f1-4ec8-a2bf-efa33f9ecb14
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2
- **Parent context**: BaM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R260: When using BaM to estimate the posterior of...
- **Rubric ID**: 0056fb57-e234-4234-8c1b-3a28ab17112a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R261: When using BaM to estimate the posterior of...
- **Rubric ID**: 116b2cae-d3f9-4f0a-a378-ef8e58ebce13
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, the learning rate was set to BD
- **Parent context**: BaM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R262: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: db63a034-717a-4b21-8b9b-5fdaec6af548
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R263: BaM has been run to estimate the posterior...
- **Rubric ID**: 09e0158e-3be8-43be-8f47-789b7fa5b524
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 5
- **Parent context**: BaM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R264: When using BaM to estimate the posterior of...
- **Rubric ID**: 24854988-2cbe-421f-9e40-396440c52923
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 5, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R265: When using BaM to estimate the posterior of...
- **Rubric ID**: 7e41d3f2-2c68-460f-bbfb-da5ee396dac2
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 5, the learning rate was set to BD
- **Parent context**: BaM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R266: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: c9e6dd41-bbb8-40db-9ba7-52a5246d2af8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 5 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R267: BaM has been run to estimate the posterior...
- **Rubric ID**: 44e4875f-420e-43aa-b399-a8cb531f2e80
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2
- **Parent context**: BaM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R268: When using BaM to estimate the posterior of...
- **Rubric ID**: 15fcd6ee-7f48-4b38-af7f-10cf71ee4a04
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R269: When using BaM to estimate the posterior of...
- **Rubric ID**: 37efb491-ab72-46ff-ac01-be182e669cf9
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, the learning rate was set to BD
- **Parent context**: BaM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R270: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 7b934673-9cd7-489d-a0b9-07a5634dd6a8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R271: BaM has been run to estimate the posterior...
- **Rubric ID**: 1db9cd8d-b056-4cdf-bfee-a9eb852d9cf1
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 15
- **Parent context**: BaM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R272: When using BaM to estimate the posterior of...
- **Rubric ID**: 27fcf00d-f195-42c9-9a17-c383d656c24f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 15, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R273: When using BaM to estimate the posterior of...
- **Rubric ID**: 4c9ff8c5-b168-4c51-8703-07a92a58adfa
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 15, the learning rate was set to BD
- **Parent context**: BaM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R274: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: c72f3d40-e998-466a-a89f-e7f503fe1ab8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 15 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R275: BaM has been run to estimate the posterior...
- **Rubric ID**: 60cc1054-45fc-4cb8-955e-41d6da1541f1
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2
- **Parent context**: BaM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R276: When using BaM to estimate the posterior of...
- **Rubric ID**: 377271e7-fb3a-495f-995c-6fe875ffcbd8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R277: When using BaM to estimate the posterior of...
- **Rubric ID**: 667cffc6-13a3-4fd1-9ac2-ac8412089d9a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, the learning rate was set to BD
- **Parent context**: BaM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R278: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 212933eb-607c-409c-ae38-b5e839252b71
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R279: BaM has been run to estimate the posterior...
- **Rubric ID**: 194a41c4-2505-446b-bc8f-3dbe6a62e21c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 40
- **Parent context**: BaM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R280: When using BaM to estimate the posterior of...
- **Rubric ID**: f2a43b87-896f-43ea-99ff-ec29cb4b8e5f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 40, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R281: When using BaM to estimate the posterior of...
- **Rubric ID**: f8b76c87-6e7c-4657-9df8-53953550f729
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 40, the learning rate was set to BD
- **Parent context**: BaM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R282: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 705c39a5-6a5a-4e0f-9c24-ab2d79b914c5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 40 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R283: BaM has been run to estimate the posterior...
- **Rubric ID**: 0542821d-25db-4819-aa43-79f889e294c6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2
- **Parent context**: BaM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R284: When using BaM to estimate the posterior of...
- **Rubric ID**: db61caee-7c7d-4bae-9c7b-b26ef18e69e6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R285: When using BaM to estimate the posterior of...
- **Rubric ID**: ba9893da-59e7-45b0-b0dd-399883daaee0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, the learning rate was set to BD
- **Parent context**: BaM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R286: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 349bd088-ece1-4e07-a7a8-384b85077878
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R287: BaM has been run to estimate the posterior...
- **Rubric ID**: ac7d8b06-3bce-47a7-b6b4-8ac2c8c494b3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 150
- **Parent context**: BaM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R288: When using BaM to estimate the posterior of...
- **Rubric ID**: dd94edbd-a41d-445e-8a2b-59172489d0df
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 150, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R289: When using BaM to estimate the posterior of...
- **Rubric ID**: 61c521c9-8cf9-436a-a141-e124dc8acb41
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 150, the learning rate was set to BD
- **Parent context**: BaM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R290: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: bb4d0731-fa2b-4d7e-8977-e3abdccbc566
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 150 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R291: GSM has been run to estimate the posterior...
- **Rubric ID**: 851ebe43-5aec-425a-8a17-ffe296556183
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2
- **Parent context**: GSM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R292: When using GSM to estimate the posterior of...
- **Rubric ID**: 282b6593-9eed-469d-b27d-846238dee3b0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of GSM have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R293: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: 2a37ca79-3836-4de1-ae0d-e6e3d96df615
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R294: GSM has been run to estimate the posterior...
- **Rubric ID**: 68a9da7a-bdf0-4bc7-969b-e6e0bc22afd5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2
- **Parent context**: GSM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R295: When using GSM to estimate the posterior of...
- **Rubric ID**: 86d80488-be67-489e-ae4b-62ad848c5946
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of GSM have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R296: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: e5281d19-9195-46f1-a380-81c1dbe3961f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R297: GSM has been run to estimate the posterior...
- **Rubric ID**: 8ba2f8bb-a6b9-4a86-b900-e4e5991eff59
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2
- **Parent context**: GSM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R298: When using GSM to estimate the posterior of...
- **Rubric ID**: 6259f215-2b2b-4a8d-ac52-f9d19109ae71
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of GSM have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R299: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: b659a37c-65af-4d58-9020-c85e6d3c979d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R300: GSM has been run to estimate the posterior...
- **Rubric ID**: 215b71b4-e27d-4a60-906d-f7a9a7bc9c79
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2
- **Parent context**: GSM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R301: When using GSM to estimate the posterior of...
- **Rubric ID**: 85284cb4-5aae-479a-ae72-ffc46f08d866
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of GSM have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R302: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: a0ea8b20-06e5-4728-bfed-a3078bde3d94
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R303: The optimal learning rate for using ADVI to...
- **Rubric ID**: a315b608-8665-46b8-a89f-92f9d3c1dd0d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch s...

### R304: ADVI has been run to estimate the posterior...
- **Rubric ID**: 379a38a5-13eb-4712-b7a2-c83bef621dc9
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch s...

### R305: When using ADVI to estimate the posterior of...
- **Rubric ID**: 18333b3b-4513-46ae-a937-474d08ec0dad
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch s...

### R306: When using ADVI to estimate the posterior of...
- **Rubric ID**: 24ec6ae5-963d-4eba-876f-c2bc84fc70b9
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch s...

### R307: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: b1ce0df4-588b-4ff9-8f37-e8cd8256e8fd
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch s...

### R308: The optimal learning rate for using ADVI to...
- **Rubric ID**: efa7c7ad-da14-4ad0-9487-5085fe0244c8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch ...

### R309: ADVI has been run to estimate the posterior...
- **Rubric ID**: 412b5e23-12e9-4f02-94fc-fb31b2220c56
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch ...

### R310: When using ADVI to estimate the posterior of...
- **Rubric ID**: 64573f8c-e4e0-439f-8318-06b39dd2cafb
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch ...

### R311: When using ADVI to estimate the posterior of...
- **Rubric ID**: ff35e6b8-d222-45ec-8737-3acad734d39b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch ...

### R312: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: 5316ac87-ca9a-44c1-a83c-44b0172ce7de
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch ...

### R313: The optimal learning rate for using ADVI to...
- **Rubric ID**: 5d231988-06a7-4ba7-b05e-2930586cb8f8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch ...

### R314: ADVI has been run to estimate the posterior...
- **Rubric ID**: fa1f6c32-5350-4063-a9a7-5f4a5a3e5d5a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch ...

### R315: When using ADVI to estimate the posterior of...
- **Rubric ID**: 989ad570-aee8-4d57-b5fd-73483a537697
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch ...

### R316: When using ADVI to estimate the posterior of...
- **Rubric ID**: ca477c48-3805-40bf-a826-5675fde38f7b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch ...

### R317: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: 56de9fef-d4fc-4e82-b8cb-55bcb3b01230
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch ...

### R318: The optimal learning rate for using ADVI to...
- **Rubric ID**: 7f47c6c1-f0d8-4ffd-9b9d-48c1f16ee772
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch...

### R319: ADVI has been run to estimate the posterior...
- **Rubric ID**: fbcd9e0c-f027-4243-aa0c-b5ce3c506294
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch...

### R320: When using ADVI to estimate the posterior of...
- **Rubric ID**: 594de7ea-9e09-4dea-b8d1-91d22fe940ff
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch...

### R321: When using ADVI to estimate the posterior of...
- **Rubric ID**: aa6b4efb-58d7-4b78-ad2b-b7509e717a24
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch...

### R322: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: 01645de4-5857-43b7-94a9-41a6557b87d1
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch...

### R323: The optimal learning rate for using ADVI (Score)...
- **Rubric ID**: c2a2a3d9-7c7f-4124-8803-22cbdf74367e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Score) to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2 has been determined using a grid search
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 4-dimensional Gaussian distribution with...

### R324: ADVI (Score) has been run to estimate the...
- **Rubric ID**: 9f2fbcd5-bf36-42b9-ad3e-78e273be3363
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Score) has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 4-dimensional Gaussian distribution with...

### R325: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 85d734eb-f263-4170-abb3-a29972dd800d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of ADVI (Score) have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 4-dimensional Gaussian distribution with...

### R326: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: eb676011-32a0-43e4-984f-64681709c5a5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 4-dimensional Gaussian distribution with...

### R327: 10 seeded runs using ADVI (Score) to estimate...
- **Rubric ID**: 5b1e168f-5cbd-49f2-b286-fdacb2930c36
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Score) to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 4-dimensional Gaussian distribution with...

### R328: The optimal learning rate for using ADVI (Score)...
- **Rubric ID**: 6b84acf9-9d40-4de4-a6fd-4e104107cbb2
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Score) to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2 has been determined using a grid search
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wit...

### R329: ADVI (Score) has been run to estimate the...
- **Rubric ID**: 73118b23-158f-4406-90b7-fbd91b4507aa
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Score) has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wit...

### R330: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 0e43c57d-ccac-486c-a4cc-9723e35cfe76
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of ADVI (Score) have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wit...

### R331: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 9be67ab7-bada-4325-89c2-c241e7c67700
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wit...

### R332: 10 seeded runs using ADVI (Score) to estimate...
- **Rubric ID**: 2d1b1085-2914-467c-9877-c774adb02f36
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Score) to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wit...

### R333: The optimal learning rate for using ADVI (Score)...
- **Rubric ID**: a9dd06c0-2773-4639-a9ad-c0329dc12eaa
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Score) to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2 has been determined using a grid search
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wit...

### R334: ADVI (Score) has been run to estimate the...
- **Rubric ID**: fdc00a0a-08ef-4d77-93cc-609d084a5867
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Score) has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wit...

### R335: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 07e5a293-cf9b-4210-a4b7-dd9516f089fa
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of ADVI (Score) have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wit...

### R336: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: c580b1c5-edc0-4a8d-9e40-b7a81642532c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wit...

### R337: 10 seeded runs using ADVI (Score) to estimate...
- **Rubric ID**: 0828d604-6f55-4ebb-bf43-49a2b275877e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Score) to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wit...

### R338: The optimal learning rate for using ADVI (Score)...
- **Rubric ID**: e307747d-f3a9-4d30-a051-264e819324e5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Score) to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2 has been determined using a grid search
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 256-dimensional Gaussian distribution wi...

### R339: ADVI (Score) has been run to estimate the...
- **Rubric ID**: ac80844b-3a00-4e2f-98f6-4098b808bc8f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Score) has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 256-dimensional Gaussian distribution wi...

### R340: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 897af513-f413-48e0-b1c5-b458a17e3d5b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of ADVI (Score) have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 256-dimensional Gaussian distribution wi...

### R341: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 507ddc64-8014-4d36-b83f-62d3d81bedb3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 256-dimensional Gaussian distribution wi...

### R342: 10 seeded runs using ADVI (Score) to estimate...
- **Rubric ID**: 15fd4d08-50b9-438d-8001-38014b42c00f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Score) to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 256-dimensional Gaussian distribution wi...

### R343: The optimal learning rate for using ADVI (Fisher)...
- **Rubric ID**: 4d1e3198-2915-4ace-a63b-1afc505dbb29
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2 has been determined using a grid search
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 4-dimensional Gaussian distribution wit...

### R344: ADVI (Fisher) has been run to estimate the...
- **Rubric ID**: 962e743b-6ff0-47c0-8bb4-35f08d70dfa2
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Fisher) has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 4-dimensional Gaussian distribution wit...

### R345: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: d6dc1999-d11d-42f2-92a5-9cf0db8d61d4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of ADVI (Fisher) have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 4-dimensional Gaussian distribution wit...

### R346: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: e1b227a5-1560-4096-9502-c3502c9a1f65
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 4-dimensional Gaussian distribution wit...

### R347: 10 seeded runs using ADVI (Fisher) to estimate...
- **Rubric ID**: f2ae8ce6-1680-4a35-8e49-dd3b1e07ff2a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Fisher) to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 4-dimensional Gaussian distribution wit...

### R348: The optimal learning rate for using ADVI (Fisher)...
- **Rubric ID**: 7803ff73-c5c0-4d4f-87bc-0cdaf29ba3fb
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2 has been determined using a grid search
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wi...

### R349: ADVI (Fisher) has been run to estimate the...
- **Rubric ID**: a5e160a8-fc4c-417c-afe6-cd5dbff6f038
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Fisher) has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wi...

### R350: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: fec68668-f94b-4f71-991a-9cdf8bfba989
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of ADVI (Fisher) have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wi...

### R351: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 1c692b2f-0e3f-4f4d-8d3d-0d0327ad0526
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wi...

### R352: 10 seeded runs using ADVI (Fisher) to estimate...
- **Rubric ID**: 93dd4fb8-6840-438b-ba9e-7d9b1bcc5a73
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Fisher) to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wi...

### R353: The optimal learning rate for using ADVI (Fisher)...
- **Rubric ID**: 26001ddb-6ea7-40e2-9a81-50047fa6fd0a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2 has been determined using a grid search
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wi...

### R354: ADVI (Fisher) has been run to estimate the...
- **Rubric ID**: 8fe279f8-7c00-46a4-9f1b-1dec662d7673
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Fisher) has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wi...

### R355: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 01337593-9d01-4b42-88ca-dbeff84a5d35
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of ADVI (Fisher) have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wi...

### R356: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: b757e1cd-d9f1-46e3-9624-c1fc5987bc44
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wi...

### R357: 10 seeded runs using ADVI (Fisher) to estimate...
- **Rubric ID**: 991e718e-1a51-41fa-b7de-e4a7cf41ed66
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Fisher) to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wi...

### R358: The optimal learning rate for using ADVI (Fisher)...
- **Rubric ID**: ea31481d-5fb2-4452-a631-6877f34cf9c4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2 has been determined using a grid search
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 256-dimensional Gaussian distribution w...

### R359: ADVI (Fisher) has been run to estimate the...
- **Rubric ID**: 9fd46c47-2113-464a-8195-78dbc3cb5dd5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Fisher) has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 256-dimensional Gaussian distribution w...

### R360: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 8ae76871-e954-4aa1-a669-fc254def82d0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, at least at least 10E4 iterations of ADVI (Fisher) have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 256-dimensional Gaussian distribution w...

### R361: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 3d432389-30b2-49ea-a068-b1c50feaa665
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 256-dimensional Gaussian distribution w...

### R362: 10 seeded runs using ADVI (Fisher) to estimate...
- **Rubric ID**: 2e7ef85d-b0d6-404b-b4c8-aaef7ad844c5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Fisher) to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2 have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 256-dimensional Gaussian distribution w...

### R363: BaM has been run to estimate the posterior...
- **Rubric ID**: f4f43f48-a6bd-4ee7-a332-5a69f2ac85ab
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R364: When using BaM to estimate the posterior of...
- **Rubric ID**: 4f376ba6-3614-4bb2-8922-61e3535b95ab
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R365: When using BaM to estimate the posterior of...
- **Rubric ID**: d4a0e069-0784-4b46-8fd2-63443ad231d5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R366: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 47bfc7bf-c5ee-4d76-991f-315508529cbe
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R367: BaM has been run to estimate the posterior...
- **Rubric ID**: eb74865f-b922-4889-a903-fdbefc6e18ba
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 10
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R368: When using BaM to estimate the posterior of...
- **Rubric ID**: 7e5101a0-0082-4e82-8367-75e0f83ebf16
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 10, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R369: When using BaM to estimate the posterior of...
- **Rubric ID**: b41fe229-8ade-43c2-ba5c-f81a2fd48c5e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 10, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R370: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 18ddc804-4de1-42ef-8bc6-43294e1c1311
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 10 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R371: BaM has been run to estimate the posterior...
- **Rubric ID**: e5d9582b-095d-41aa-ada7-224e2fd7d8ff
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R372: When using BaM to estimate the posterior of...
- **Rubric ID**: 498d2346-28da-45ed-ba3d-51a361e051f9
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R373: When using BaM to estimate the posterior of...
- **Rubric ID**: e44f2d22-825c-4919-b5f4-b91e1b7bfb67
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R374: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: c1afb007-3a74-4427-9e4c-89697cbf680e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R375: BaM has been run to estimate the posterior...
- **Rubric ID**: 09bf5fc1-0250-49af-b5a1-db72df7acd0c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 10
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R376: When using BaM to estimate the posterior of...
- **Rubric ID**: 6871bc50-9d3c-4fe7-9ce4-42659f017a40
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 10, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R377: When using BaM to estimate the posterior of...
- **Rubric ID**: 45088ef3-4343-4b6a-be23-1a81470f2983
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 10, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R378: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 5f9ef61e-465b-49e1-8c0c-f5f76e0b081a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 10 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R379: BaM has been run to estimate the posterior...
- **Rubric ID**: 99eb13b1-01c5-44c8-bfb5-442331d2996e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R380: When using BaM to estimate the posterior of...
- **Rubric ID**: 9cd74282-ad08-4d05-96c8-233af32246a9
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R381: When using BaM to estimate the posterior of...
- **Rubric ID**: cdced646-7bfd-4b04-a05c-762b757836f6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R382: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: c4c35868-4073-4be0-a26d-3a4a08eb09fc
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R383: BaM has been run to estimate the posterior...
- **Rubric ID**: ae70dc14-becc-45d1-99e0-02e645a8e452
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 10
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R384: When using BaM to estimate the posterior of...
- **Rubric ID**: 9e360075-b9f3-497f-bfb5-677e956ab4e8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 10, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R385: When using BaM to estimate the posterior of...
- **Rubric ID**: f2a93e5f-fe5f-4d27-aa32-f6cf4fcc4745
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 10, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R386: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: ec069e17-1a0e-4099-8df5-cef3a703dbce
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 10 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R387: BaM has been run to estimate the posterior...
- **Rubric ID**: 1c24cf2d-8c7a-4320-91b7-c5fe59cffd81
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R388: When using BaM to estimate the posterior of...
- **Rubric ID**: 9e436be5-3f70-461d-9dc8-84edc22e6041
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R389: When using BaM to estimate the posterior of...
- **Rubric ID**: ef531090-1b64-4947-93da-264147dc41d6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R390: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: eb01b5f5-8c85-4b91-bb50-b14e29f07cbf
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R391: BaM has been run to estimate the posterior...
- **Rubric ID**: a93772cc-bd01-4453-a6d0-1de89926a9c5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 10
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R392: When using BaM to estimate the posterior of...
- **Rubric ID**: 2d372887-5959-4eb3-9b44-58fccdb4a1f4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 10, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R393: When using BaM to estimate the posterior of...
- **Rubric ID**: b113b88e-031e-4b4c-83f9-981dad188663
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 10, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R394: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 21f1c1bf-530f-49d6-b315-b25585ae8168
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 10 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R395: BaM has been run to estimate the posterior...
- **Rubric ID**: 059ead17-f4a3-4f21-9986-3a43d91dcfad
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R396: When using BaM to estimate the posterior of...
- **Rubric ID**: 12b21af6-e802-4ab2-9c31-abed1c0dcb01
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R397: When using BaM to estimate the posterior of...
- **Rubric ID**: 0171bc4d-cfd7-4f56-82f3-9754abb48194
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R398: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: faf72c5b-ad10-4e60-90df-a905771691d5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R399: BaM has been run to estimate the posterior...
- **Rubric ID**: f7bf8721-e952-4b4e-a5db-21f259900695
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 10
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R400: When using BaM to estimate the posterior of...
- **Rubric ID**: 8c6b48ce-5f2e-4461-bba9-7a12cc4e5a1e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 10, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R401: When using BaM to estimate the posterior of...
- **Rubric ID**: 9946d9e0-f4e1-46f5-8627-1e2cef005725
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 10, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R402: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 63057eb0-4d7e-4464-8ff9-b6fc7c123187
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 10 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R403: BaM has been run to estimate the posterior...
- **Rubric ID**: 46b3a74e-1887-48b9-b03b-5650760bc91b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R404: When using BaM to estimate the posterior of...
- **Rubric ID**: 11118af4-1352-43bb-899e-6cba4a40f1de
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R405: When using BaM to estimate the posterior of...
- **Rubric ID**: 0851596e-4168-4bf1-9af5-a8aa750da367
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R406: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: f3cb72b7-da6b-41b3-afb8-6d1b759c0694
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R407: BaM has been run to estimate the posterior...
- **Rubric ID**: 69e6f97f-8ff8-448a-8f2a-0405ea023bce
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 10
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R408: When using BaM to estimate the posterior of...
- **Rubric ID**: c28337af-0f9b-4e48-beb0-0c11c920fe93
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 10, at least at least 10E4 iterations of BaM VI have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R409: When using BaM to estimate the posterior of...
- **Rubric ID**: 884af9f6-37e5-46bc-ad03-127b9890bdb3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 10, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R410: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 5d0326c5-eae4-480a-9cf7-c80c9c834872
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 10 have been run.
- **Parent context**: BaM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R411: GSM has been run to estimate the posterior...
- **Rubric ID**: 391e09ee-fad5-4fb7-a91a-41778fc39bdb
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R412: When using GSM to estimate the posterior of...
- **Rubric ID**: 10d06c80-8846-4230-ae44-61849795680e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, at least at least 10E4 iterations of GSM VI have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R413: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: 76aa7fad-f537-4973-9afa-3b1af9d796fe
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5 have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R414: GSM has been run to estimate the posterior...
- **Rubric ID**: 88b80548-27f7-4039-ba7e-d9338e804eea
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R415: When using GSM to estimate the posterior of...
- **Rubric ID**: c32d9ae7-90b5-45db-ac88-fd742c2cb31b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, at least at least 10E4 iterations of GSM VI have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R416: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: eb8281d1-3b00-48ab-957e-c2a2079e9693
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5 have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R417: GSM has been run to estimate the posterior...
- **Rubric ID**: a98484f2-0c87-4ca1-b229-be8faba6cd8d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R418: When using GSM to estimate the posterior of...
- **Rubric ID**: 0f5315a6-07f7-4949-9595-db791452a0a8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, at least at least 10E4 iterations of GSM VI have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R419: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: 773b436c-49b8-46ed-a113-31c235976a4c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5 have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R420: GSM has been run to estimate the posterior...
- **Rubric ID**: f21bf1b6-cc7d-46b5-833c-ad976a7beef1
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R421: When using GSM to estimate the posterior of...
- **Rubric ID**: d61f280d-cd4c-4afc-8d1e-f631e171d03d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of GSM VI have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R422: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: badd58a6-886d-4fcf-a43c-eb146b6555d1
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R423: GSM has been run to estimate the posterior...
- **Rubric ID**: 541d7b68-13f7-4717-b3f9-b7bc0bed14be
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R424: When using GSM to estimate the posterior of...
- **Rubric ID**: c7c32ea0-d1f2-421e-8062-67ef37c1f156
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of GSM VI have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R425: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: ed1a5670-7c00-4e9a-8216-dcbd4a71ec2f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R426: GSM has been run to estimate the posterior...
- **Rubric ID**: 91b80ba0-edb1-4b3b-8e19-4ca927d750e6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R427: When using GSM to estimate the posterior of...
- **Rubric ID**: cac3207d-1428-4366-a1f4-cb722f2357a8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of GSM VI have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R428: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: e80c7b4a-288d-49c4-8d4e-5ed1eea148c7
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: GSM has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution w...

### R429: The optimal learning rate for using ADVI to...
- **Rubric ID**: 9c42c539-6d17-45c9-bee6-554311b8232d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R430: ADVI has been run to estimate the posterior...
- **Rubric ID**: 8fadf64b-97be-48f5-b343-ea5c8cd6e507
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R431: When using ADVI to estimate the posterior of...
- **Rubric ID**: ee9fdd7b-920c-4301-a7e3-067f543cfc83
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R432: When using ADVI to estimate the posterior of...
- **Rubric ID**: c0dd7770-fc48-4ef0-b698-ab310ec5ce7a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R433: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: c4209adb-20e8-44d9-816e-a25c6c4235df
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R434: The optimal learning rate for using ADVI to...
- **Rubric ID**: ab275e2b-bea3-4774-83d8-e7ed92a6d903
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R435: ADVI has been run to estimate the posterior...
- **Rubric ID**: 7a40a22a-09ea-4564-8625-70f0758586df
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R436: When using ADVI to estimate the posterior of...
- **Rubric ID**: fa87a2ce-59bf-4664-ab05-b4328caa2bbe
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R437: When using ADVI to estimate the posterior of...
- **Rubric ID**: 17bd6e5e-7cb3-49c1-bf41-44dcaa7a7677
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R438: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: 995a6c19-1c2a-42f9-9670-ae02f4bb9564
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R439: The optimal learning rate for using ADVI to...
- **Rubric ID**: aa2adfc0-b415-423e-a454-b41b85f7fa44
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R440: ADVI has been run to estimate the posterior...
- **Rubric ID**: 82227b50-2294-4ba4-becf-0aa69893137f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R441: When using ADVI to estimate the posterior of...
- **Rubric ID**: 620de40f-72ff-4f08-9a16-847bdfca5414
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R442: When using ADVI to estimate the posterior of...
- **Rubric ID**: 8428beb2-d8cb-4ea6-ac2d-b15cb02d9685
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R443: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: 479187ca-2b66-44ec-a47c-0f68951cc8ed
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R444: The optimal learning rate for using ADVI to...
- **Rubric ID**: 10b6a04c-f4f1-4dce-9c9e-dc6afbc2914c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R445: ADVI has been run to estimate the posterior...
- **Rubric ID**: 55fbb62d-7a39-41aa-89c4-ef139586e6e8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R446: When using ADVI to estimate the posterior of...
- **Rubric ID**: 3198c989-66cd-4a62-b619-b1a13b0edb56
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R447: When using ADVI to estimate the posterior of...
- **Rubric ID**: 8ca49c8f-fe52-4e89-9293-4f03677fb360
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R448: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: 9e8b7c88-5bfd-4c50-a133-b56885f297d5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R449: The optimal learning rate for using ADVI to...
- **Rubric ID**: 786b3d65-1854-495e-8eea-1435ef8506f8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R450: ADVI has been run to estimate the posterior...
- **Rubric ID**: b9498352-f7a7-460e-84a0-300155594f95
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R451: When using ADVI to estimate the posterior of...
- **Rubric ID**: f16e3ab3-0b75-4ff0-a4a2-3d319d0eb724
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R452: When using ADVI to estimate the posterior of...
- **Rubric ID**: 5de2f6fd-7d14-4d1b-ad74-21ce94f90799
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R453: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: 8c91d635-40ce-4788-be54-70c0d33c0493
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R454: The optimal learning rate for using ADVI to...
- **Rubric ID**: 7ac7b7be-bcde-46a7-a110-e05c4e0be65d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R455: ADVI has been run to estimate the posterior...
- **Rubric ID**: f2be3969-10db-44a6-95d4-7e5d0846b340
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R456: When using ADVI to estimate the posterior of...
- **Rubric ID**: a77d5683-e2e1-4bd2-b2d7-db9bba29fa5f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R457: When using ADVI to estimate the posterior of...
- **Rubric ID**: 76eff4b4-fc23-4878-9cf0-37b987a7324e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R458: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: e90a6b24-9e3f-4b8b-99ba-5fb01f7880ac
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution ...

### R459: The optimal learning rate for using ADVI (Score)...
- **Rubric ID**: 2c89a14c-85cd-48b6-ada4-f37a9696fb2d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R460: ADVI (Score) has been run to estimate the...
- **Rubric ID**: e105dac4-cea6-4a3f-a466-b46bedc66870
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R461: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: ba0e9c27-c94e-4d25-952d-07acc87d09eb
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, at least at least 10E4 iterations of ADVI (Score) have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R462: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 7d6fec08-a014-4dfe-b1be-b2ecbb02c8d6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R463: 10 seeded runs using ADVI (Score) to estimate...
- **Rubric ID**: 3640f230-829c-4507-9bc2-caa0f9165911
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5 have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R464: The optimal learning rate for using ADVI (Score)...
- **Rubric ID**: 7023c16b-4e75-4170-873e-badcc17b90bd
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R465: ADVI (Score) has been run to estimate the...
- **Rubric ID**: 710cd4de-fdff-4a58-9dda-d515e1a009b2
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R466: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: c8400f7b-e4e3-4bbc-9949-9ad409f81f52
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, at least at least 10E4 iterations of ADVI (Score) have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R467: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: f51f2f96-0d49-404b-9407-69ac5813c5ba
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R468: 10 seeded runs using ADVI (Score) to estimate...
- **Rubric ID**: 5682594b-5225-43c4-aa14-a89ac5f62ee8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5 have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R469: The optimal learning rate for using ADVI (Score)...
- **Rubric ID**: e2985594-8291-4570-adfe-68f27a0c0210
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R470: ADVI (Score) has been run to estimate the...
- **Rubric ID**: 85fc83b7-ddec-442c-ae8b-ad407e4875af
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R471: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: e02c2119-ad2c-4ab6-9f4d-8d9a0a76066d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, at least at least 10E4 iterations of ADVI (Score) have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R472: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 185d2868-050a-4af1-8b1a-c66c7100c4af
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R473: 10 seeded runs using ADVI (Score) to estimate...
- **Rubric ID**: 40843141-48bc-46fb-b71b-431cf03f752e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5 have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R474: The optimal learning rate for using ADVI (Score)...
- **Rubric ID**: c94040db-d8ad-4a9b-89fd-1a764779497c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R475: ADVI (Score) has been run to estimate the...
- **Rubric ID**: afe5de64-88c9-4675-b2ce-6fa02f973758
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R476: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: bd4aeb0d-4654-4bf5-8c25-098103a6f11f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of ADVI (Score) have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R477: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: fa99ff23-fbb4-4f18-bfee-fe46ad1cca1b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R478: 10 seeded runs using ADVI (Score) to estimate...
- **Rubric ID**: abd3ae40-6a82-4e5e-ad95-2c7137380abf
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R479: The optimal learning rate for using ADVI (Score)...
- **Rubric ID**: 58dfa0e0-fb1f-4ab3-b383-d1998a22e1e4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R480: ADVI (Score) has been run to estimate the...
- **Rubric ID**: 117aa215-e381-4514-a9da-9844f4e803d1
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R481: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 6e80278b-3669-46f1-a833-3e6b2e2d6b97
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of ADVI (Score) have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R482: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 6cf5b95b-9399-4c87-a05a-678e1a553023
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R483: 10 seeded runs using ADVI (Score) to estimate...
- **Rubric ID**: 1bd3dded-deb4-437c-8578-361775e79028
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R484: The optimal learning rate for using ADVI (Score)...
- **Rubric ID**: 1450a497-5db6-479a-a9b3-affb7fb07b0f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R485: ADVI (Score) has been run to estimate the...
- **Rubric ID**: 9ebacb36-0c73-448f-bcdf-386a97ea1cca
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R486: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 8f3f1f62-ead4-48b2-b190-ac0c16dc4f0f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of ADVI (Score) have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R487: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 5b9b81bc-aad3-4706-b9bb-6cc2259493d0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R488: 10 seeded runs using ADVI (Score) to estimate...
- **Rubric ID**: 6c442710-6aac-4598-817e-a318b7e4ceb9
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distr...

### R489: The optimal learning rate for using ADVI (Fisher)...
- **Rubric ID**: 0686194b-fadd-48c2-b161-e1ac4b82c88e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R490: ADVI (Fisher) has been run to estimate the...
- **Rubric ID**: 2f9c441c-6e8c-449b-9c5c-e5599f6cd7b0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R491: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: d84dcacd-ad80-4665-8829-a0a7b45c75fd
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, at least at least 10E4 iterations of ADVI (Fisher) have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R492: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: c32b6acb-ba7a-4877-9162-acda5aa0172e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R493: 10 seeded runs using ADVI (Fisher) to estimate...
- **Rubric ID**: db2831ff-e7f9-4012-b5b0-26771eb705eb
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5 have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R494: The optimal learning rate for using ADVI (Fisher)...
- **Rubric ID**: ae2acf11-98eb-4703-b775-b3f7d0621052
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R495: ADVI (Fisher) has been run to estimate the...
- **Rubric ID**: 3a8fed23-2f7a-43c4-a2e6-22f0537a6cff
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R496: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 105ca4e8-5969-46c2-9d76-b26605b303c3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, at least at least 10E4 iterations of ADVI (Fisher) have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R497: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 68104c27-0eaa-4db7-86a6-549a45db223f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R498: 10 seeded runs using ADVI (Fisher) to estimate...
- **Rubric ID**: 512edafa-0acb-43f1-9d00-7173fc24a508
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5 have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R499: The optimal learning rate for using ADVI (Fisher)...
- **Rubric ID**: 46c877fd-1064-477d-bbc7-06e4b726646a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R500: ADVI (Fisher) has been run to estimate the...
- **Rubric ID**: 634f988d-1793-4fcc-99d7-933c6b0fd30b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R501: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 810dc566-e704-464f-9444-397687161ebc
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, at least at least 10E4 iterations of ADVI (Fisher) have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R502: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: b2c519e8-e277-4d7d-990c-0db96feb9b98
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R503: 10 seeded runs using ADVI (Fisher) to estimate...
- **Rubric ID**: 736c7065-57d6-4c25-a436-8213b0604577
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5 have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R504: The optimal learning rate for using ADVI (Fisher)...
- **Rubric ID**: 7d665e7b-d57a-4b9d-965f-0b16f837ece3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R505: ADVI (Fisher) has been run to estimate the...
- **Rubric ID**: 5f69e162-a701-4113-a6dc-2ebd73e0cc3e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R506: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: c6d6049c-8bfd-4c18-bdc0-ffc7860698e7
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of ADVI (Fisher) have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R507: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 1c0dd897-6924-4961-9a79-114eadd52559
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R508: 10 seeded runs using ADVI (Fisher) to estimate...
- **Rubric ID**: bd3e0fcb-c0e1-4a8b-a14b-db01aa349755
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R509: The optimal learning rate for using ADVI (Fisher)...
- **Rubric ID**: 6284c74f-e116-4e52-9c01-cc8ebe044aec
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R510: ADVI (Fisher) has been run to estimate the...
- **Rubric ID**: c710affd-a06b-4652-936e-83fec4a712a2
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R511: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 0ba1c3c1-8276-4b69-b4ae-379ae0178a50
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of ADVI (Fisher) have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R512: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 40cee27c-896d-4af7-ba0f-2b9b08cdf658
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R513: 10 seeded runs using ADVI (Fisher) to estimate...
- **Rubric ID**: 5a4842c3-e3bf-4857-8851-ac0ff2467d46
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R514: The optimal learning rate for using ADVI (Fisher)...
- **Rubric ID**: c69d8b34-4ae0-4fed-a3d6-57eba5ca6178
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R515: ADVI (Fisher) has been run to estimate the...
- **Rubric ID**: 4ec15363-b060-4ba6-b184-dc4078b745d9
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R516: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: c171a7cc-2ce2-4953-a972-101bc8b61ea5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, at least at least 10E4 iterations of ADVI (Fisher) have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R517: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: d93a5fb2-80ca-4813-aa25-34b44ef70e2b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R518: 10 seeded runs using ADVI (Fisher) to estimate...
- **Rubric ID**: c46cde27-4b26-407b-811f-32c43957e22b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5 have been run.
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 10-dimensional sinh-arcsinh normal dist...

### R519: BaM has been run to estimate the posterior...
- **Rubric ID**: f837eff5-b654-4eb4-871c-089a24176c6e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R520: When using BaM to estimate the posterior of...
- **Rubric ID**: b2bff8f9-bce9-41a6-97dd-4c9fb48fd2a3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8, at least at least 10E4 iterations of BaM have been run.
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R521: When using BaM to estimate the posterior of...
- **Rubric ID**: 5c51279d-cd45-4eee-8ec1-b9bfa4ea9d65
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R522: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 24d3f024-2e96-4084-b860-add43b233edd
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8 have been run.
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R523: BaM has been run to estimate the posterior...
- **Rubric ID**: 6c2d7d49-3b1d-467a-8569-fcf6d14f05f1
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R524: When using BaM to estimate the posterior of...
- **Rubric ID**: 1297829c-9d5b-428d-9c54-9e8aaa51175a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32, at least at least 10E4 iterations of BaM have been run.
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R525: When using BaM to estimate the posterior of...
- **Rubric ID**: 62a4fcd4-71ac-4204-b5b3-5477be5e564f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R526: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 7a4bcf41-4085-45d7-b0e3-4dc4361214c2
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32 have been run.
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R527: BaM has been run to estimate the posterior...
- **Rubric ID**: 015bae58-b11f-4f57-a51d-f5cb7ccee7bd
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 8
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R528: When using BaM to estimate the posterior of...
- **Rubric ID**: 4cb0423c-3664-42a0-bb37-359b4a9b6d8f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 8, at least at least 10E4 iterations of BaM have been run.
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R529: When using BaM to estimate the posterior of...
- **Rubric ID**: b85aa210-398d-40ad-a415-41de3b2abc7f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 8, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R530: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 4bbf804d-5234-4361-94ee-6c678ed53bb3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 8 have been run.
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R531: BaM has been run to estimate the posterior...
- **Rubric ID**: 0ca34203-84bb-465e-a4e4-44e632ca4f5c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 32
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R532: When using BaM to estimate the posterior of...
- **Rubric ID**: 82c175b1-9c51-4144-9662-e71111326ba0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 32, at least at least 10E4 iterations of BaM have been run.
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R533: When using BaM to estimate the posterior of...
- **Rubric ID**: 4ce1270e-2a76-4619-adb5-9b9220ee488f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 32, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R534: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 9c6c5973-756b-44ad-ba80-39082fafeb1e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 32 have been run.
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R535: BaM has been run to estimate the posterior...
- **Rubric ID**: e09285cb-7a24-4437-8bdd-e0f1ae0c87c6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R536: When using BaM to estimate the posterior of...
- **Rubric ID**: 8e72a625-6f5e-4e45-9631-eb645a4d56cf
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8, at least at least 10E4 iterations of BaM have been run.
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R537: When using BaM to estimate the posterior of...
- **Rubric ID**: a9b3491d-bd2c-4aa9-8431-75a69a9b63dd
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R538: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 72e544a7-a8da-4073-b0b1-63366384c25a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8 have been run.
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R539: BaM has been run to estimate the posterior...
- **Rubric ID**: e4bafdae-76e6-4bd0-9d40-7daec888b662
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R540: When using BaM to estimate the posterior of...
- **Rubric ID**: 208f4237-219b-4318-a0e6-cd9169a3f686
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32, at least at least 10E4 iterations of BaM have been run.
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R541: When using BaM to estimate the posterior of...
- **Rubric ID**: 9cd1568d-cb5b-43f4-91ee-f6d65a4fd5f0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32, the learning rate was set to $BD/(t+1)$
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R542: 10 seeded runs using BaM to estimate the...
- **Rubric ID**: 3ae7d54c-2461-46cb-b9d0-1956b5565b5a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32 have been run.
- **Parent context**: BaM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R543: GSM has been run to estimate the posterior...
- **Rubric ID**: c25dd614-2367-474d-8b0c-efa5c808d260
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R544: When using GSM to estimate the posterior of...
- **Rubric ID**: 893babad-44c5-4eed-8a40-3ff0c6f40c7c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8, at least at least 10E4 iterations of GSM have been run.
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R545: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: 8cdc984b-e3b3-45ce-aa8d-2c50511150a1
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8 have been run.
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R546: GSM has been run to estimate the posterior...
- **Rubric ID**: 5cb168ee-9db1-4109-b16c-c5c702acf3b4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R547: When using GSM to estimate the posterior of...
- **Rubric ID**: c3a3c836-d238-4aca-bc42-9c31b2285c09
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32, at least at least 10E4 iterations of GSM have been run.
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R548: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: 36f6d2f5-3d36-469d-9478-129b3913470b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32 have been run.
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wi...

### R549: GSM has been run to estimate the posterior...
- **Rubric ID**: 4ff1459a-d66a-4f3f-bc34-db4d586357a8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 8
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R550: When using GSM to estimate the posterior of...
- **Rubric ID**: 9f2f240e-d923-4c72-becc-4b83d6137360
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 8, at least at least 10E4 iterations of GSM have been run.
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R551: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: ea968935-7675-46f4-8b07-4b898bb917ef
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 8 have been run.
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R552: GSM has been run to estimate the posterior...
- **Rubric ID**: dc4b9ae5-0c57-4f55-b798-c545689a97ab
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 32
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R553: When using GSM to estimate the posterior of...
- **Rubric ID**: f1600521-a4f1-4076-ac20-a3a3feb9a66b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 32, at least at least 10E4 iterations of GSM have been run.
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R554: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: b6ca1761-eec4-4575-a09f-4c1983f3fd39
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 32 have been run.
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimensi...

### R555: GSM has been run to estimate the posterior...
- **Rubric ID**: 6a7e611f-545b-4815-8509-e7188c1d63f1
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R556: When using GSM to estimate the posterior of...
- **Rubric ID**: f81e4479-84f4-4c02-92ce-ef6c77afcc9b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8, at least at least 10E4 iterations of GSM have been run.
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R557: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: e303643c-e84b-498c-9a98-5a612dda2a9d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8 have been run.
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R558: GSM has been run to estimate the posterior...
- **Rubric ID**: 4a847921-4402-4684-8973-b7d72a583b12
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R559: When using GSM to estimate the posterior of...
- **Rubric ID**: 143903aa-d529-4a79-b423-63b3a2c3ab4b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32, at least at least 10E4 iterations of GSM have been run.
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R560: 10 seeded runs using GSM to estimate the...
- **Rubric ID**: 6b588e5e-8f49-4798-b1a5-755f860daef6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using GSM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32 have been run.
- **Parent context**: GSM has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, a...

### R561: The optimal learning rate for using ADVI to...
- **Rubric ID**: 49b48f8a-c8b6-4805-811a-fa52816fe397
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, w...

### R562: ADVI has been run to estimate the posterior...
- **Rubric ID**: 09c6f987-d1c2-409d-b310-19a65f53a5f5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, w...

### R563: When using ADVI to estimate the posterior of...
- **Rubric ID**: eef1ece3-dd3f-48f3-be04-17be555c7a02
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, w...

### R564: When using ADVI to estimate the posterior of...
- **Rubric ID**: 170d0eac-3827-498a-96fa-29a251ddf2f0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, w...

### R565: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: 66537c8d-b749-44e8-bbb4-efc5c8ba42a3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, w...

### R566: The optimal learning rate for using ADVI to...
- **Rubric ID**: 0e78618e-bf65-405c-8432-beb0ad087bcc
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, w...

### R567: ADVI has been run to estimate the posterior...
- **Rubric ID**: 0da174d4-dd67-4186-a769-420d985043d6
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, w...

### R568: When using ADVI to estimate the posterior of...
- **Rubric ID**: a25d0c1a-b751-4534-ac49-b06768d8ad97
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, w...

### R569: When using ADVI to estimate the posterior of...
- **Rubric ID**: cadfa2fb-d037-4db7-9346-aeae4a2aead2
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, w...

### R570: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: 59093363-fd86-41d2-8e04-0bcce926794b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, w...

### R571: The optimal learning rate for using ADVI to...
- **Rubric ID**: 52b65034-4ffe-442f-92f8-2f18f43fb3ba
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimensi...

### R572: ADVI has been run to estimate the posterior...
- **Rubric ID**: 2acedc23-f3d7-42e6-aa64-96ae7512af8a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 8
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimensi...

### R573: When using ADVI to estimate the posterior of...
- **Rubric ID**: 197031d1-83c6-44c7-af19-a79ff7015679
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 8, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimensi...

### R574: When using ADVI to estimate the posterior of...
- **Rubric ID**: ad03053b-d208-4411-bb41-fb3c52aefd27
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 8, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimensi...

### R575: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: fa09e183-c72e-4b1b-9949-b68f08da3911
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 8 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimensi...

### R576: The optimal learning rate for using ADVI to...
- **Rubric ID**: 1bf67145-6e2b-4b22-90b1-836b90353a8a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimensi...

### R577: ADVI has been run to estimate the posterior...
- **Rubric ID**: e4be020d-e25e-419c-85d9-88117a4faaee
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 32
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimensi...

### R578: When using ADVI to estimate the posterior of...
- **Rubric ID**: 2b86577b-7f47-45e8-a51b-b48b32e94149
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 32, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimensi...

### R579: When using ADVI to estimate the posterior of...
- **Rubric ID**: 934936f0-6ae6-4c86-81e1-0e1cb8979929
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 32, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimensi...

### R580: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: 7ec676a0-dec0-43f6-9357-54a0ef6aaf9c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 32 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimensi...

### R581: The optimal learning rate for using ADVI to...
- **Rubric ID**: f93c36f8-0c2f-4ffb-ba6c-75793539b9d3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, ...

### R582: ADVI has been run to estimate the posterior...
- **Rubric ID**: 7c4c0ee4-8e9d-482a-901c-ba9c64e4d020
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, ...

### R583: When using ADVI to estimate the posterior of...
- **Rubric ID**: a971509d-f1f9-4c7d-a17f-f0dd33e11d11
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, ...

### R584: When using ADVI to estimate the posterior of...
- **Rubric ID**: 92e2e914-91ff-4b70-993f-2a6edb0a9772
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, ...

### R585: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: 094edda1-f33d-4e73-9422-41423c4f8c06
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, ...

### R586: The optimal learning rate for using ADVI to...
- **Rubric ID**: 1cc7c950-5c47-4d61-8cac-4182ff8bff8f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5 has been determined using a grid search
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, ...

### R587: ADVI has been run to estimate the posterior...
- **Rubric ID**: 7b7fe513-0da6-48eb-9a77-ee93ce87b9b2
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, ...

### R588: When using ADVI to estimate the posterior of...
- **Rubric ID**: 0ff35efe-0a73-4959-b3a5-4785c1c561c8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32, at least at least 10E4 iterations of ADVI have been run.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, ...

### R589: When using ADVI to estimate the posterior of...
- **Rubric ID**: 0965035a-96e1-486a-b551-f0860a211db2
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, ...

### R590: 10 seeded runs using ADVI to estimate the...
- **Rubric ID**: 8629705b-0212-4e69-b492-9f5a8c733d47
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: 10 seeded runs using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32 have been run.
- **Parent context**: ADVI has been run to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, ...

### R591: Code has been executed such that a VAE...
- **Rubric ID**: 479536e1-9e0e-4673-8f51-f3988503c024
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been executed such that a VAE has been trained on the CIFAR 10 image dataset training split following the standard VAE training procedure from Kingma & Welling, 2014 described in Appendix E.6
- **Parent context**: A Variational Autoencoder (VAE) has been pre-trained on the CIFAR 10 image dataset training split

### R592: Code has been executed such that when training...
- **Rubric ID**: 6d8670e2-8f99-48ba-bcef-5cbc1b96edf0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been executed such that when training a VAE on the CIFAR 10 image dataset training split, the VAE was trained for 100 epochs.
- **Parent context**: A Variational Autoencoder (VAE) has been pre-trained on the CIFAR 10 image dataset training split

### R593: Code has been executed such that when training...
- **Rubric ID**: 842cfb0d-e108-4089-a7ba-208d88bcf5a3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been executed such that when training a VAE on the CIFAR 10 image dataset training split, the VAE was trained generally following the training hyperparameters outlined in the addendum
- **Parent context**: A Variational Autoencoder (VAE) has been pre-trained on the CIFAR 10 image dataset training split

### R594: The optimal learning rate for using BaM to...
- **Rubric ID**: 78f2fcf2-a5f1-4f41-92a1-b34e9ab0cd03
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using BaM to estimate the posterior mean needed for reconstructing the sampled test image with batch size 10 has been determined using a grid search
- **Parent context**: BaM has been run at batch size 10 to reconstruct the sampled test image

### R595: BaM has been run at batch size 10...
- **Rubric ID**: 444bc2d7-6615-4d2a-9b6b-f24c03a6881b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run at batch size 10 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: BaM has been run at batch size 10 to reconstruct the sampled test image

### R596: When using BaM to estimate the posterior mean...
- **Rubric ID**: 8f56f69f-35ec-4aea-b112-3a68654c47f0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 10, at least at least 1000 iterations of BaM have been run.
- **Parent context**: BaM has been run at batch size 10 to reconstruct the sampled test image

### R597: When using BaM to estimate the posterior mean...
- **Rubric ID**: 18a8972e-b70d-45b2-bb61-0bae8190c1a0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 10, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: BaM has been run at batch size 10 to reconstruct the sampled test image

### R598: The optimal learning rate for using BaM to...
- **Rubric ID**: ef8e44b8-9ec2-49ee-b5bb-f6e4f9d81a55
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using BaM to estimate the posterior mean needed for reconstructing the sampled test image with batch size 100 has been determined using a grid search
- **Parent context**: BaM has been run at batch size 100 to reconstruct the sampled test image

### R599: BaM has been run at batch size 100...
- **Rubric ID**: b0690065-7dff-45bd-bf6c-4ec1f0e5bc8a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run at batch size 100 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: BaM has been run at batch size 100 to reconstruct the sampled test image

### R600: When using BaM to estimate the posterior mean...
- **Rubric ID**: 9d9748a1-c0ad-4c7d-bbe5-5fb17afbf5d3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 100, at least at least 1000 iterations of BaM have been run.
- **Parent context**: BaM has been run at batch size 100 to reconstruct the sampled test image

### R601: When using BaM to estimate the posterior mean...
- **Rubric ID**: 6ff3d104-79ab-44e8-8fe9-2e927e32b295
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 100, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: BaM has been run at batch size 100 to reconstruct the sampled test image

### R602: The optimal learning rate for using BaM to...
- **Rubric ID**: f3ebd402-acf6-4b4b-b157-c29070429970
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using BaM to estimate the posterior mean needed for reconstructing the sampled test image with batch size 300 has been determined using a grid search
- **Parent context**: BaM has been run at batch size 300 to reconstruct the sampled test image

### R603: BaM has been run at batch size 300...
- **Rubric ID**: 0bd5bc5f-610c-4d6b-8a25-eff36993c3d7
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: BaM has been run at batch size 300 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: BaM has been run at batch size 300 to reconstruct the sampled test image

### R604: When using BaM to estimate the posterior mean...
- **Rubric ID**: 143b6d2d-7745-4a54-9106-0c57610de19d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 300, at least at least 1000 iterations of BaM have been run.
- **Parent context**: BaM has been run at batch size 300 to reconstruct the sampled test image

### R605: When using BaM to estimate the posterior mean...
- **Rubric ID**: 82747cf2-6d84-451f-82dc-a841f36d8e82
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 300, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: BaM has been run at batch size 300 to reconstruct the sampled test image

### R606: The optimal learning rate for using ADVI to...
- **Rubric ID**: ad5f8cea-d7e3-4034-8a1b-57335d91c552
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior mean needed for reconstructing the sampled test image with batch size 10 has been determined using a grid search
- **Parent context**: ADVI has been run at batch size 10 to reconstruct the sampled test image

### R607: ADVI has been run at batch size 10...
- **Rubric ID**: 33b601eb-4850-47f1-aa0a-cb922a950568
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run at batch size 10 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: ADVI has been run at batch size 10 to reconstruct the sampled test image

### R608: When using ADVI to estimate the posterior mean...
- **Rubric ID**: bd7a93a4-6f40-4a90-a230-487327325001
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 10, at least at least 1000 iterations of ADVI have been run.
- **Parent context**: ADVI has been run at batch size 10 to reconstruct the sampled test image

### R609: When using ADVI to estimate the posterior mean...
- **Rubric ID**: 0f945396-fb64-4464-97c5-245fa8a0dba7
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 10, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run at batch size 10 to reconstruct the sampled test image

### R610: The optimal learning rate for using ADVI to...
- **Rubric ID**: 5c34a45f-b8bc-429f-8a35-a75d9d01f427
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior mean needed for reconstructing the sampled test image with batch size 100 has been determined using a grid search
- **Parent context**: ADVI has been run at batch size 100 to reconstruct the sampled test image

### R611: ADVI has been run at batch size 100...
- **Rubric ID**: 1b648575-fd50-4c80-b7c1-80056bdf212b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run at batch size 100 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: ADVI has been run at batch size 100 to reconstruct the sampled test image

### R612: When using ADVI to estimate the posterior mean...
- **Rubric ID**: 105cd5c2-6b31-42fc-9b30-be0fffabff8d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 100, at least at least 1000 iterations of ADVI have been run.
- **Parent context**: ADVI has been run at batch size 100 to reconstruct the sampled test image

### R613: When using ADVI to estimate the posterior mean...
- **Rubric ID**: 6feffede-d52b-41cd-ab1b-81b353524171
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 100, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run at batch size 100 to reconstruct the sampled test image

### R614: The optimal learning rate for using ADVI to...
- **Rubric ID**: 5ddd339b-f32b-40a0-ae02-679f58791615
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The optimal learning rate for using ADVI to estimate the posterior mean needed for reconstructing the sampled test image with batch size 300 has been determined using a grid search
- **Parent context**: ADVI has been run at batch size 300 to reconstruct the sampled test image

### R615: ADVI has been run at batch size 300...
- **Rubric ID**: 01173144-a0f3-41d8-affd-9b1b351ef8fd
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: ADVI has been run at batch size 300 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: ADVI has been run at batch size 300 to reconstruct the sampled test image

### R616: When using ADVI to estimate the posterior mean...
- **Rubric ID**: 4b609e68-998b-4927-ab05-372feafa9b12
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 300, at least at least 1000 iterations of ADVI have been run.
- **Parent context**: ADVI has been run at batch size 300 to reconstruct the sampled test image

### R617: When using ADVI to estimate the posterior mean...
- **Rubric ID**: 34bb1182-bf82-4449-b80c-213530a7fd8b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 300, the learning rate was set to the learning rate determined by the grid search.
- **Parent context**: ADVI has been run at batch size 300 to reconstruct the sampled test image

### R618: GSM has been run at batch size 10...
- **Rubric ID**: 44c8f43d-7e69-4f28-853f-efe0d2f2da29
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run at batch size 10 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: GSM has been run at batch size 10 to reconstruct the sampled test image

### R619: When using GSM to estimate the posterior mean...
- **Rubric ID**: a79c3275-b73a-4f05-a065-8506e1b924a4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 10, at least at least 1000 iterations of GSM have been run.
- **Parent context**: GSM has been run at batch size 10 to reconstruct the sampled test image

### R620: GSM has been run at batch size 100...
- **Rubric ID**: 71ab7d5d-29a2-4fd3-afe5-ff4bb7d3e080
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run at batch size 100 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: GSM has been run at batch size 100 to reconstruct the sampled test image

### R621: When using GSM to estimate the posterior mean...
- **Rubric ID**: a19b55e0-b4f1-4a18-835f-ce9690e3264c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 100, at least at least 1000 iterations of GSM have been run.
- **Parent context**: GSM has been run at batch size 100 to reconstruct the sampled test image

### R622: GSM has been run at batch size 300...
- **Rubric ID**: f602226a-0a14-45d3-a43f-94d6888c0d34
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: GSM has been run at batch size 300 to estimate the posterior mean needed for reconstructing the sampled test image
- **Parent context**: GSM has been run at batch size 300 to reconstruct the sampled test image

### R623: When using GSM to estimate the posterior mean...
- **Rubric ID**: 477df8a0-2843-4307-908c-8abf635d06f7
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 300, at least at least 1000 iterations of GSM have been run.
- **Parent context**: GSM has been run at batch size 300 to reconstruct the sampled test image

## Code Execution — Evaluation & Benchmarking

### R624: When using BaM to estimate the posterior of...
- **Rubric ID**: 4c09eede-b39e-4176-9447-c97837d19d0e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size...

### R625: When using BaM to estimate the posterior of...
- **Rubric ID**: 8f83d494-95a9-4ad0-af53-ab20deed1801
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size...

### R626: When using BaM to estimate the posterior of...
- **Rubric ID**: 723c33ff-c364-4a99-8a72-2ecf33ff0fc3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size...

### R627: When using BaM to estimate the posterior of...
- **Rubric ID**: 927f15c3-23a9-4b8a-b609-c09ecca3b943
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size...

### R628: When using BaM to estimate the posterior of...
- **Rubric ID**: 039d5a5b-c720-4bf7-87af-d3ee4c6e5384
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch siz...

### R629: When using BaM to estimate the posterior of...
- **Rubric ID**: e753e316-198c-4b34-bfd6-c7d6a9a070ad
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch siz...

### R630: When using BaM to estimate the posterior of...
- **Rubric ID**: 6aec384e-ea26-4299-8a0c-72d5ed13c7e8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 15, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch siz...

### R631: When using BaM to estimate the posterior of...
- **Rubric ID**: a002e9a2-c102-4568-bb4d-e1074d7613bf
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 15, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 16-dimensional Gaussian distribution with batch siz...

### R632: When using BaM to estimate the posterior of...
- **Rubric ID**: 45133900-476a-4761-bd13-d305ab5cec73
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch siz...

### R633: When using BaM to estimate the posterior of...
- **Rubric ID**: e0b6bfdd-c621-49ba-8d60-acf649b4b0c0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch siz...

### R634: When using BaM to estimate the posterior of...
- **Rubric ID**: f8305d21-f8b3-4e32-8659-e5b2f0bfbf97
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 40, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch siz...

### R635: When using BaM to estimate the posterior of...
- **Rubric ID**: c223b970-8c42-46e5-94b8-d2bff394e4fe
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 40, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 64-dimensional Gaussian distribution with batch siz...

### R636: When using BaM to estimate the posterior of...
- **Rubric ID**: 86d49309-597f-4d98-8f66-165226007954
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch si...

### R637: When using BaM to estimate the posterior of...
- **Rubric ID**: bea69362-bf5e-4080-8934-6ea319224005
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch si...

### R638: When using BaM to estimate the posterior of...
- **Rubric ID**: 18b6b769-b2a1-4ff4-b92a-585a997adf20
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 150, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch si...

### R639: When using BaM to estimate the posterior of...
- **Rubric ID**: 1893167f-e0d2-42dc-b64e-af5ac0b0d355
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 150, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 256-dimensional Gaussian distribution with batch si...

### R640: When using GSM to estimate the posterior of...
- **Rubric ID**: a32ab529-4f80-4e7b-97c4-5849d2dda725
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: GSM has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch si...

### R641: When using GSM to estimate the posterior of...
- **Rubric ID**: 9cbd1b65-7be1-411c-8748-2fb8cc1eb3cc
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: GSM has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch s...

### R642: When using GSM to estimate the posterior of...
- **Rubric ID**: 7fab2d25-d8fc-4f6d-8008-196ebbac7bbb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: GSM has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch s...

### R643: When using GSM to estimate the posterior of...
- **Rubric ID**: ec099917-3d20-4f05-b8f7-4b20083cbe1b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: GSM has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch ...

### R644: When using ADVI to estimate the posterior of...
- **Rubric ID**: ef371648-4dfb-42fa-99fd-e488c79464ea
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: ADVI has been run to estimate the posterior of a 4-dimensional Gaussian distribution with batch s...

### R645: When using ADVI to estimate the posterior of...
- **Rubric ID**: 9c292bcb-fb54-43f6-8996-d9d98e306c12
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: ADVI has been run to estimate the posterior of a 16-dimensional Gaussian distribution with batch ...

### R646: When using ADVI to estimate the posterior of...
- **Rubric ID**: 66d03db4-4c97-4d2a-bc8f-4a239709f23f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: ADVI has been run to estimate the posterior of a 64-dimensional Gaussian distribution with batch ...

### R647: When using ADVI to estimate the posterior of...
- **Rubric ID**: 4d3228a0-b083-472a-bb91-a5f4b37494f7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: ADVI has been run to estimate the posterior of a 256-dimensional Gaussian distribution with batch...

### R648: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: a26df670-5f91-48fe-9b3e-369465202b14
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 4-dimensional Gaussian distribution with...

### R649: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 85b88c94-1fec-44ca-abfc-05e72f295f24
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wit...

### R650: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 088bc8dd-e3b4-4266-be9a-3e399301aaf1
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wit...

### R651: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 09649bc7-b949-4e3c-b899-6c402c3893b3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: ADVI (Score) has been run to estimate the posterior of a 256-dimensional Gaussian distribution wi...

### R652: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 5105a35f-39ff-4c47-a793-adf8b3b84ccd
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 4-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 4-dimensional Gaussian distribution wit...

### R653: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 8cf46d16-94fa-47b2-bcd8-8cc823783bf5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 16-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 16-dimensional Gaussian distribution wi...

### R654: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 381b1a65-1aaa-4645-9335-a65fa7810448
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 64-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 64-dimensional Gaussian distribution wi...

### R655: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 83a87c65-d622-4c47-bc92-8122d00a4fd9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 256-dimensional Gaussian distribution with batch size 2, the forward and reverse empirical KL divergence between the estimated posterior and the target posterior has been measured at each iteration
- **Parent context**: ADVI (Fisher) has been run to estimate the posterior of a 256-dimensional Gaussian distribution w...

### R656: When using BaM to estimate the posterior of...
- **Rubric ID**: dc0d4cec-272c-4b32-be12-1e924693bb82
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R657: When using BaM to estimate the posterior of...
- **Rubric ID**: f8cd84bd-cc60-4088-bdc3-a38cde84ce64
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R658: When using BaM to estimate the posterior of...
- **Rubric ID**: 1b3a9ebf-1ff6-400f-b1a5-189aa27c7745
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 10, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R659: When using BaM to estimate the posterior of...
- **Rubric ID**: 33be260a-d620-4675-811a-4af45406b48b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 10, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R660: When using BaM to estimate the posterior of...
- **Rubric ID**: e387403d-a8dd-43e7-a9d5-c3c316048b0d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R661: When using BaM to estimate the posterior of...
- **Rubric ID**: 8950a31a-fe23-4a31-8539-25aa8c4b3420
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R662: When using BaM to estimate the posterior of...
- **Rubric ID**: b59e00e1-a992-4270-8c44-845d47488800
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 10, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R663: When using BaM to estimate the posterior of...
- **Rubric ID**: 83d034f9-7098-413e-96c0-8f05e5e4c2e4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 10, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R664: When using BaM to estimate the posterior of...
- **Rubric ID**: 19af0edd-51bf-408a-b44b-05d2b27cc475
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R665: When using BaM to estimate the posterior of...
- **Rubric ID**: 608d2dc3-755d-4109-b356-068c829de421
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R666: When using BaM to estimate the posterior of...
- **Rubric ID**: b9fd0920-bd92-4380-865d-fb12246afed5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 10, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R667: When using BaM to estimate the posterior of...
- **Rubric ID**: ac696ae0-3912-4b2c-a1df-4ac4340b6cd7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 10, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R668: When using BaM to estimate the posterior of...
- **Rubric ID**: cf03d711-6b0a-44eb-8735-f823a61c4c9e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R669: When using BaM to estimate the posterior of...
- **Rubric ID**: 597d878e-e359-4d95-a461-7e1329a665b8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R670: When using BaM to estimate the posterior of...
- **Rubric ID**: b54f0e5e-85a9-4b85-a14c-602e761d2234
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 10, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R671: When using BaM to estimate the posterior of...
- **Rubric ID**: df794af1-8a08-41c2-a7ee-3ebae63c6f9e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 10, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R672: When using BaM to estimate the posterior of...
- **Rubric ID**: 3382bd2b-59d3-4654-b5ea-87605e1205f4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R673: When using BaM to estimate the posterior of...
- **Rubric ID**: 8af7132c-5395-4997-97a0-ace8a2aa605a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R674: When using BaM to estimate the posterior of...
- **Rubric ID**: 18d74aeb-b932-4d4c-b932-d695bfc7973c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 10, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R675: When using BaM to estimate the posterior of...
- **Rubric ID**: 32400d56-455b-4947-bf96-d540619a254e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 10, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R676: When using BaM to estimate the posterior of...
- **Rubric ID**: 1d325a4d-6a99-4f7c-b00d-faa4cc28bd3b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R677: When using BaM to estimate the posterior of...
- **Rubric ID**: 35fb2726-52d6-4108-ae2b-254177bb1cf0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R678: When using BaM to estimate the posterior of...
- **Rubric ID**: ca568913-9d6f-4dcb-82ea-5b6cd7e40ad9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 10, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R679: When using BaM to estimate the posterior of...
- **Rubric ID**: 1c642871-ea7b-42a2-afa9-8b0be504d863
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 10, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using BaM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R680: When using GSM to estimate the posterior of...
- **Rubric ID**: c30beb18-febd-40a3-9d66-de146b17d7a4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R681: When using GSM to estimate the posterior of...
- **Rubric ID**: 3c669aad-ef59-4626-aba0-e3eee4c00e18
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R682: When using GSM to estimate the posterior of...
- **Rubric ID**: 45df03dd-0004-4666-935b-c6d4dd2ce158
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R683: When using GSM to estimate the posterior of...
- **Rubric ID**: 1b38f57b-8611-44ef-81ab-ca3f05376f5c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R684: When using GSM to estimate the posterior of...
- **Rubric ID**: fa911b45-5cb2-4029-9aa4-2e52ef3909d8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R685: When using GSM to estimate the posterior of...
- **Rubric ID**: 4299c0e1-1c75-4acc-b007-9e039946bab6
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R686: When using GSM to estimate the posterior of...
- **Rubric ID**: 7cf84274-03dc-44a8-8dea-1186c08fa537
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R687: When using GSM to estimate the posterior of...
- **Rubric ID**: ed96f466-5758-4cde-bf73-6f6b86901ea5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R688: When using GSM to estimate the posterior of...
- **Rubric ID**: 65b83b7b-92d2-423a-aea3-6f5741ffa0da
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R689: When using GSM to estimate the posterior of...
- **Rubric ID**: ca52c67e-73d6-4270-9f5e-88c2798f564c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R690: When using GSM to estimate the posterior of...
- **Rubric ID**: 8a7a1ce1-c309-421e-ad03-576c26c382c5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R691: When using GSM to estimate the posterior of...
- **Rubric ID**: 787af806-0e72-4ad0-a5d1-0a2fa5dc4bf5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using GSM to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wit...

### R692: When using ADVI to estimate the posterior of...
- **Rubric ID**: d5251688-7eb0-49a0-b1bd-ad350c56231b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wi...

### R693: When using ADVI to estimate the posterior of...
- **Rubric ID**: 8bdbc3d7-f477-4a57-831c-916a46912a25
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wi...

### R694: When using ADVI to estimate the posterior of...
- **Rubric ID**: 60f213cb-90cc-4de6-8121-cc25c3b82fc5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wi...

### R695: When using ADVI to estimate the posterior of...
- **Rubric ID**: ca7a17c3-115d-47a4-a27f-3d16b6b78583
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wi...

### R696: When using ADVI to estimate the posterior of...
- **Rubric ID**: dae93d49-b089-4861-b924-00a5fc491c98
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wi...

### R697: When using ADVI to estimate the posterior of...
- **Rubric ID**: 92ac75f8-7fba-4278-9e4c-f458135ad5a9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wi...

### R698: When using ADVI to estimate the posterior of...
- **Rubric ID**: 01dab2bb-d769-46fd-a771-474fed6b3dab
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wi...

### R699: When using ADVI to estimate the posterior of...
- **Rubric ID**: 15341615-56ea-4234-b16d-522cb9d0289e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wi...

### R700: When using ADVI to estimate the posterior of...
- **Rubric ID**: 0ebd659c-dcb5-4e14-abe9-f86f302b665f
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wi...

### R701: When using ADVI to estimate the posterior of...
- **Rubric ID**: 8e1b4fe8-72a0-4858-9839-0c1e60517486
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wi...

### R702: When using ADVI to estimate the posterior of...
- **Rubric ID**: 44ba6bbe-0486-4a0e-ae82-39fa155e907e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wi...

### R703: When using ADVI to estimate the posterior of...
- **Rubric ID**: 6b15e080-712a-4daa-8cb0-336210ca1c3b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution wi...

### R704: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 90b4fc01-4bcc-429f-8c41-539f38aee7a0
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distrib...

### R705: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 4b889f83-2fb8-4372-90ad-89486204e40c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distrib...

### R706: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 985ef3ed-763b-4f99-9b6b-d1df1c88bb17
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distrib...

### R707: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: a5ff7730-3115-4a2f-8f46-1f3c901a7500
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distrib...

### R708: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 05bb0a28-c2ac-441b-89c0-56a0dc60c15a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distrib...

### R709: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: da75920e-9fbe-4f19-80dc-bfcf888d5395
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distrib...

### R710: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 69f480e4-0e4c-45f6-9291-fac652ba68b3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distrib...

### R711: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 799684df-a31a-4d2c-9882-806c1b7e3c90
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distrib...

### R712: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 2ac2b72f-21c5-4ee1-a5e8-5f0f6cade681
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distrib...

### R713: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 729fdcea-587c-42ed-a49d-80409cdac9e5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distrib...

### R714: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: c2c82662-c683-43dc-a8e1-5aa536ad1c57
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distrib...

### R715: When using ADVI (Score) to estimate the posterior...
- **Rubric ID**: 2c3111ab-0562-4103-8a11-3319b03df61e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Score) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distrib...

### R716: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 888e4dcc-7b3c-41b4-bc09-1dcef6734c05
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distri...

### R717: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: dcb27d2f-df41-45a2-a48f-a0c140462ed3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=0.2$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distri...

### R718: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: bf28bc43-3893-4f55-8a17-8eb8b49d2057
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distri...

### R719: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 493b1aae-a560-4c7b-94f9-39614a6b0f46
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distri...

### R720: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: aeb48001-33ec-48a9-bb57-1db0b6e6b0ef
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distri...

### R721: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 50995dc3-95a1-47e2-bd03-11ab7abbca30
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1$ and skew $s=1.8$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distri...

### R722: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: d826b219-76ee-438e-90b9-c69f42b8bcb4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distri...

### R723: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 5c12fd10-78ac-41d9-bb02-5ea27313411b
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.1$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distri...

### R724: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 7fa8a2bc-d251-421c-8b77-f387d51efc31
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distri...

### R725: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: e1e1940c-ef91-4ca5-95fb-757acc01e7bc
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=0.9$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distri...

### R726: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: d625fc20-611b-4991-9e52-8e5ae6cfaaeb
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, the forward empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distri...

### R727: When using ADVI (Fisher) to estimate the posterior...
- **Rubric ID**: 6677da00-6f0a-4d75-beed-2ac33d6af2a5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distribution with tail $t=1.7$ and skew $s=0$ with batch size 5, the reverse empirical KL divergence has been measured at each iteration.
- **Parent context**: When using ADVI (Fisher) to estimate the posterior of a 10-dimensional sinh-arcsinh normal distri...

### R728: When using BaM to estimate the posterior of...
- **Rubric ID**: 42b6b19f-73e5-481c-8c88-9295630c0ce8
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with...

### R729: When using BaM to estimate the posterior of...
- **Rubric ID**: 56ae77eb-f010-4617-806e-fcbf725f7c91
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with...

### R730: When using BaM to estimate the posterior of...
- **Rubric ID**: beca4aaf-9f77-47eb-b44b-4f0a020bbd66
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with...

### R731: When using BaM to estimate the posterior of...
- **Rubric ID**: 72683ca0-2cd2-4bdd-b201-e6fb7215f0ee
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using BaM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with...

### R732: When using BaM to estimate the posterior of...
- **Rubric ID**: b6ebb53c-665f-4d3d-9014-c7fc55dd1b08
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 8, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension...

### R733: When using BaM to estimate the posterior of...
- **Rubric ID**: b09f5f97-e9ef-43e8-981f-b39a4adb1906
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 8, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension...

### R734: When using BaM to estimate the posterior of...
- **Rubric ID**: d438fa87-9c81-45ca-8c2a-b8bf51883b17
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 32, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension...

### R735: When using BaM to estimate the posterior of...
- **Rubric ID**: dc385833-683f-42d2-8967-622537e96d46
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 32, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using BaM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension...

### R736: When using BaM to estimate the posterior of...
- **Rubric ID**: dab11bf2-03ea-423e-afa5-d28f7a639962
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at ...

### R737: When using BaM to estimate the posterior of...
- **Rubric ID**: 899ea91d-4a63-485d-9320-b4b22eb3c497
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at ...

### R738: When using BaM to estimate the posterior of...
- **Rubric ID**: 2d2dd630-ef7e-4fa2-b378-4a4e2e82947e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at ...

### R739: When using BaM to estimate the posterior of...
- **Rubric ID**: 9eb38c89-e6d0-4f53-8873-f285fd019fda
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using BaM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at ...

### R740: When using GSM to estimate the posterior of...
- **Rubric ID**: b878a678-81e6-4ba1-badf-8585113ab488
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using GSM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with...

### R741: When using GSM to estimate the posterior of...
- **Rubric ID**: b5dde722-d968-4db7-9ebb-37bf2123ce74
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using GSM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with...

### R742: When using GSM to estimate the posterior of...
- **Rubric ID**: 7f33e8fe-280b-4540-9bbc-4e4b40083a77
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using GSM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with...

### R743: When using GSM to estimate the posterior of...
- **Rubric ID**: 8f104ede-2f09-43f3-86fc-a68e68813bbe
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using GSM to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with...

### R744: When using GSM to estimate the posterior of...
- **Rubric ID**: cd3ee5f9-7d44-4821-9aa7-2b5ddbd8f882
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 8, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using GSM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension...

### R745: When using GSM to estimate the posterior of...
- **Rubric ID**: f16d8608-589e-47d9-82c7-864aafcbd05d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 8, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using GSM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension...

### R746: When using GSM to estimate the posterior of...
- **Rubric ID**: 292ff5b5-770b-4400-a3ec-6d6ccb219e60
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 32, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using GSM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension...

### R747: When using GSM to estimate the posterior of...
- **Rubric ID**: 5c64afb7-4255-4bc3-b63f-de1af6752057
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension D=13, with a batch size of 32, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using GSM to estimate the posterior of the PosteriorDB `gp-pois-regrs` problem, at dimension...

### R748: When using GSM to estimate the posterior of...
- **Rubric ID**: 5cc85417-61ae-4a9f-8db0-afa5682fc92a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using GSM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at ...

### R749: When using GSM to estimate the posterior of...
- **Rubric ID**: b313a0e6-7918-46f6-b84d-6542bbde60f7
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using GSM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at ...

### R750: When using GSM to estimate the posterior of...
- **Rubric ID**: 3367cf7b-56a3-4334-9e64-23d82cf9225a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using GSM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at ...

### R751: When using GSM to estimate the posterior of...
- **Rubric ID**: c3b77980-82a8-45fc-be50-25becac3e123
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using GSM to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at ...

### R752: When using ADVI to estimate the posterior of...
- **Rubric ID**: 4eee7a51-69aa-4307-a31e-0f1f581f3fc3
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wit...

### R753: When using ADVI to estimate the posterior of...
- **Rubric ID**: 93c5238b-9cef-4ffc-9d23-e7676654c82c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 8, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wit...

### R754: When using ADVI to estimate the posterior of...
- **Rubric ID**: 51f771f6-2ad2-42ef-b8d0-ba3ef81b63c4
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wit...

### R755: When using ADVI to estimate the posterior of...
- **Rubric ID**: 64fade5e-3fa9-4fe6-883a-cdac48418e50
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, with a batch size of 32, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using ADVI to estimate the posterior of the PosteriorDB `ark` problem, at dimension D=7, wit...

### R756: When using ADVI to estimate the posterior of...
- **Rubric ID**: b4d586e6-c73f-4b4f-803c-d22a59fa1507
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 8, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension...

### R757: When using ADVI to estimate the posterior of...
- **Rubric ID**: 866b5614-ee07-4d9b-9102-44b066eaa229
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 8, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension...

### R758: When using ADVI to estimate the posterior of...
- **Rubric ID**: 7b6128ed-88e5-4da0-9753-e37e4e1a2362
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 32, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension...

### R759: When using ADVI to estimate the posterior of...
- **Rubric ID**: 8468c8b8-6bfd-4bf3-91eb-1dc2f94b3872
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension D=13, with a batch size of 32, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using ADVI to estimate the posterior of the PosteriorDB `gp-pois-regr` problem, at dimension...

### R760: When using ADVI to estimate the posterior of...
- **Rubric ID**: b440b1c2-fdc2-4bfd-9b5e-979c2f544fc9
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at...

### R761: When using ADVI to estimate the posterior of...
- **Rubric ID**: bbbeb0e4-b603-4ec7-ac70-3b2e1e9aa928
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 8, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at...

### R762: When using ADVI to estimate the posterior of...
- **Rubric ID**: c2859754-9e61-4a4c-b42e-82858d1d7eee
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32, the relative mean error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at...

### R763: When using ADVI to estimate the posterior of...
- **Rubric ID**: 38a29fb9-a04c-4d85-9a37-75de0acc335d
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at dimension D=10, with a batch size of 32, the relative standard error between the estimated posterior and the HMC posterior has been measured at each iteration
- **Parent context**: When using ADVI to estimate the posterior of the PosteriorDB `eight-schools-centered` problem, at...

### R764: When using BaM to estimate the posterior mean...
- **Rubric ID**: 293b53bf-0280-401b-984f-31b9a013ca98
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 10, the MSE between the reconstructed image and the sampled test image has been measured at each iteration
- **Parent context**: BaM has been run at batch size 10 to reconstruct the sampled test image

### R765: When using BaM to estimate the posterior mean...
- **Rubric ID**: a991dbb8-4629-4d6c-8398-ef4605e4ddfa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 100, the MSE between the reconstructed image and the sampled test image has been measured at each iteration
- **Parent context**: BaM has been run at batch size 100 to reconstruct the sampled test image

### R766: When using BaM to estimate the posterior mean...
- **Rubric ID**: ad5934b0-78aa-4783-95c0-15e05c702d3a
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using BaM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 300, the MSE between the reconstructed image and the sampled test image has been measured at each iteration
- **Parent context**: BaM has been run at batch size 300 to reconstruct the sampled test image

### R767: When using ADVI to estimate the posterior mean...
- **Rubric ID**: 8d713188-2d8b-4a32-8420-6436c2acc931
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 10, the MSE between the reconstructed image and the sampled test image has been measured at each iteration
- **Parent context**: ADVI has been run at batch size 10 to reconstruct the sampled test image

### R768: When using ADVI to estimate the posterior mean...
- **Rubric ID**: 409a175d-3094-4bda-b67b-a59aef9fefc5
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 100, the MSE between the reconstructed image and the sampled test image has been measured at each iteration
- **Parent context**: ADVI has been run at batch size 100 to reconstruct the sampled test image

### R769: When using ADVI to estimate the posterior mean...
- **Rubric ID**: e535aeb4-eb78-4fa6-950c-48a1933aef50
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using ADVI to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 300, the MSE between the reconstructed image and the sampled test image has been measured at each iteration
- **Parent context**: ADVI has been run at batch size 300 to reconstruct the sampled test image

### R770: When using GSM to estimate the posterior mean...
- **Rubric ID**: b5399414-8376-4669-bcf4-13087a8f75aa
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 10, the MSE between the reconstructed image and the sampled test image has been measured at each iteration
- **Parent context**: GSM has been run at batch size 10 to reconstruct the sampled test image

### R771: When using GSM to estimate the posterior mean...
- **Rubric ID**: 75ee4374-3bcf-4253-be8e-def88934959e
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 100, the MSE between the reconstructed image and the sampled test image has been measured at each iteration
- **Parent context**: GSM has been run at batch size 100 to reconstruct the sampled test image

### R772: When using GSM to estimate the posterior mean...
- **Rubric ID**: 4c2a435c-7588-4d3e-a9de-f2d4fc216649
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using GSM to estimate the posterior mean needed for reconstructing the sampled test image with a batch size of 300, the MSE between the reconstructed image and the sampled test image has been measured at each iteration
- **Parent context**: GSM has been run at batch size 300 to reconstruct the sampled test image

### R773: When using AVI (the trained encoder network) to...
- **Rubric ID**: 9d3ca042-2b68-42b1-9c2b-8d5b75137e12
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: When using AVI (the trained encoder network) to estimate the posterior mean needed for reconstructing the sampled test image, the MSE between the reconstructed image and the sampled test image has been measured
- **Parent context**: AVI (the trained encoder network) has been run to reconstruct the sampled test image, and its per...

## Result Analysis — Evaluation & Benchmarking

### R774: The forward and reverse KL divergence between target...
- **Rubric ID**: afaa90e8-f1f1-46b9-a4d6-0dc0352a4179
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The forward and reverse KL divergence between target and estimated Gaussian distributions measured over VI iterations for BaM and ADVI show that BaM converges orders of magnitude earlier (in terms of number of iterations) than ADVI.
- **Parent context**: The results of Figure 5.1 and Figure E.3 have been replicated

### R775: The forward and reverse KL divergence between target...
- **Rubric ID**: 1fcbbb32-a117-4781-986a-275bda1b82bc
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The forward and reverse KL divergence between target and estimated Gaussian distributions measured over VI iterations for BaM and GSM show the two methods perform similarly for B=2, while BaM at larger batch sizes tends to converge more quickly than GSM at B=2.
- **Parent context**: The results of Figure 5.1 and Figure E.3 have been replicated

### R776: The forward and reverse KL divergence measured between...
- **Rubric ID**: bc5749df-9522-406a-af84-a15956e07e74
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The forward and reverse KL divergence measured between target and estimated Gaussian distributions over VI iterations for the gradient based methods (ADVI, ADVI (Score) and ADVI (Fisher)) show that the three methods perform similarly
- **Parent context**: The results of Figure 5.1 and Figure E.3 have been replicated

### R777: The forward and reverse KL divergence between target...
- **Rubric ID**: 71fd6df1-5b42-4f6d-8933-641ffb8b7ba4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The forward and reverse KL divergence between target and estimated sinh-arcsinh normal distributions with normal tails ($t=1$) and varying skews measured over VI iterations for BaM and ADVI show that BaM converges faster (in terms of number of iterations) than ADVI.
- **Parent context**: The results of Figure 5.2 and of Figure E.4 have been replicated

### R778: The forward and reverse KL divergence between target...
- **Rubric ID**: 9f8f0bec-6419-425f-92d9-8f5d7ef45fcf
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The forward and reverse KL divergence between target and estimated sinh-arcsinh normal distributions with normal tails ($t=1$) and varying skews measured over VI iterations for BaM and ADVI show that, compared to ADVI, BaM converges to a higher value in terms of forward KL divergence and to a similar value in terms of reverse KL divergence
- **Parent context**: The results of Figure 5.2 and of Figure E.4 have been replicated

### R779: The reverse KL divergence between target and estimated...
- **Rubric ID**: bec65857-cc6a-419d-b5e0-1c78f235f062
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The reverse KL divergence between target and estimated sinh-arcsinh normal distributions with no skew ($s=0$) and varying tails measured over VI iterations for BaM, GSM, ADVI, Score and Fisher show that all methods converge to similar values
- **Parent context**: The results of Figure 5.2 and of Figure E.4 have been replicated

### R780: The reverse KL divergence between target and estimated...
- **Rubric ID**: b75c8f95-7b52-4c5b-880c-9ea50b5bb59f
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The reverse KL divergence between target and estimated sinh-arcsinh normal distributions with no skew ($s=0$) and varying tails measured over VI iterations for BaM, GSM and ADVI show that in some cases, BaM and ADVI converge to better values than GSM
- **Parent context**: The results of Figure 5.2 and of Figure E.4 have been replicated

### R781: The forward and reverse KL divergence between target...
- **Rubric ID**: 609c1c97-01bd-4b8b-b117-caf34905f9de
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The forward and reverse KL divergence between target and estimated sinh-arcsinh normal distributions with no skew ($s=0$) and varying tails measured over VI iterations for BaM and ADVI show that BaM typically converges in fewer iterations than ADVI
- **Parent context**: The results of Figure 5.2 and of Figure E.4 have been replicated

### R782: The relative mean error between HMC and estimated...
- **Rubric ID**: b686ecb8-9b9c-405c-bffd-004e4881c42d
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The relative mean error between HMC and estimated PosteriorDB problem posteriors measured over VI iterations for BaM and ADVI show BaM outperforms ADVI, converging earlier (in terms of number of iterations) to lower relative mean errors.
- **Parent context**: The results of Figure 5.3 and of Figure E.6 have been replicated

### R783: The relative mean error between HMC and estimated...
- **Rubric ID**: 791e7650-8d70-4584-a966-ca4bf37bd3b4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The relative mean error between HMC and estimated PosteriorDB problem posteriors measured over VI iterations for BaM and GSM show that GSM can converge faster than BaM for smaller batch sizes.
- **Parent context**: The results of Figure 5.3 and of Figure E.6 have been replicated

### R784: The relative mean error between HMC and estimated...
- **Rubric ID**: 43895a25-8e25-4b18-aee4-728c61a4a9db
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The relative mean error between HMC and estimated PosteriorDB problem posteriors measured over VI iterations for BaM, ADVI and GSM show that in general BaM tends to benefit from larger batch sizes, while ADVI and GSM do not.
- **Parent context**: The results of Figure 5.3 and of Figure E.6 have been replicated

### R785: The relative mean error and relative standard error...
- **Rubric ID**: 5822d5a9-72f1-4730-a255-e40a31415d18
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The relative mean error and relative standard error between HMC and estimated PosteriorDB problem posteriors measured over VI iterations for BaM, ADVI and GSM show that in general the same trends can be observed for relative mean error and relative standard error, with the exception of the "hierarchical" `eight-schools-centered` problem where BaM converges to a higher relative standard error than GSM or ADVI.
- **Parent context**: The results of Figure 5.3 and of Figure E.6 have been replicated

### R786: The MSE between the reconstructed image and the...
- **Rubric ID**: 949cbdd8-617b-4f85-8da4-79bfcb35ab5f
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The MSE between the reconstructed image and the sampled test image measured over the VI iterations for BaM at batch size 10 shows that BaM performs poorly (MSE greater than 0.2) at smaller batch sizes, i.e. at a batch size of 10.
- **Parent context**: The results of Figure 5.4 b) from Section 5.3 have been replicated

### R787: The MSE between the reconstructed image and the...
- **Rubric ID**: 8e0dacf2-f476-4941-9668-7bc455b46d9a
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The MSE between the reconstructed image and the sampled test image measured over the VI iterations for BaM at batch sizes 100 and 300 show that BaM performs competitively (MSE less than 0.05) at larger batch sizes, i.e. at a batch size of 100 and 300.
- **Parent context**: The results of Figure 5.4 b) from Section 5.3 have been replicated

### R788: The MSE between the reconstructed image and the...
- **Rubric ID**: 6e7bf691-0f0c-468e-be72-c16877e89da5
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The MSE between the reconstructed image and the sampled test image measured over the VI iterations for BaM, GSM and ADVI at batch size 300 show that BaM converges an order of magnitude (or more) faster (in terms of taking less iterations to converge) than ADVI and GSM
- **Parent context**: The results of Figure 5.4 b) from Section 5.3 have been replicated

### R789: The MSE between the reconstructed image and the...
- **Rubric ID**: d520be6a-63e5-4dcc-94af-e9cb5e094b1c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The MSE between the reconstructed image and the sampled test image measured over the VI iterations for BaM, ADVI and AVI at batch sizes 10, 100 and 300 show that in general either BaM or ADVI or both achieve a MSE than AVI.
- **Parent context**: The results of Figure 5.4 b) from Section 5.3 have been replicated
