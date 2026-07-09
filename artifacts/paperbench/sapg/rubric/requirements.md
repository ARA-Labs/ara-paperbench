# Rubric Requirements — sapg
**Source**: PaperBench expert-authored reproduction rubric
**Total leaf requirements**: 206

## Method Implementation

### R01: The on-policy actor loss has been implemented as described i...
- **Rubric ID**: b3629831-05ac-4af6-8898-ac0684cc0bc8
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The on-policy actor loss has been implemented as described in Equation 2.
- **Parent context**: The actor loss using on-policy and off-policy samples has been implemented as described in Equation ...

### R02: The off-policy actor loss has been implemented as described...
- **Rubric ID**: 71e63922-52ae-417a-834e-8ed01b0dfefc
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The off-policy actor loss has been implemented as described in Equation 3.
- **Parent context**: The actor loss using on-policy and off-policy samples has been implemented as described in Equation ...

### R03: The n-step return for on-policy data has been implemented as...
- **Rubric ID**: 6998b4d4-adf3-4e18-b668-75b94d843106
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The n-step return for on-policy data has been implemented as described in Equation 5.
- **Parent context**: The critic loss using on-policy and off-policy samples has been implemented as described in Equation...

### R04: The one-step return for off-policy data has been implemented...
- **Rubric ID**: 893fdad6-f965-4ea4-ade3-c4ff6208ad00
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The one-step return for off-policy data has been implemented as described in Equation 6.
- **Parent context**: The critic loss using on-policy and off-policy samples has been implemented as described in Equation...

### R05: The on-policy critic loss has been implemented as described...
- **Rubric ID**: 9cec8d88-5eaa-4fbe-ab24-3db082104ec4
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The on-policy critic loss has been implemented as described in Equation 7. 
- **Parent context**: The critic loss using on-policy and off-policy samples has been implemented as described in Equation...

### R06: The off-policy critic loss has been implemented as described...
- **Rubric ID**: 4c79136d-c44e-49cd-8d94-0164ae87bdab
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: The off-policy critic loss has been implemented as described in Equation 8.
- **Parent context**: The critic loss using on-policy and off-policy samples has been implemented as described in Equation...

### R07: Code has been written to collect samples from a number of di...
- **Rubric ID**: 9ab81633-ae84-430b-a239-0638d1e0e527
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to collect samples from a number of different policies (denoted as $M$ in Section 4.2).
- **Parent context**: The data sampling procedure has been implemented as defined in Section 4.2.

### R08: Code has been written to collect $\frac{N}{2}$ samples from...
- **Rubric ID**: 4cbd9e69-4605-4390-b4ff-6ca21c1040b9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to collect $\frac{N}{2}$ samples from policy $i$ for a batch size of $N$ samples used to update policy $i$.
- **Parent context**: The data sampling procedure has been implemented as defined in Section 4.2.

### R09: Code has been written to collect $\frac{N}{2}$ samples from...
- **Rubric ID**: 010f50bd-7813-4da8-bd99-41c3cc6ef89c
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to collect $\frac{N}{2}$ samples from any policy except policy $i$ for a batch size of $N$ samples used to update policy $i$.
- **Parent context**: The data sampling procedure has been implemented as defined in Section 4.2.

### R10: Code has been written to collect $\frac{N}{2}$ samples from...
- **Rubric ID**: c6fdbab5-5537-4b74-9147-d3495c393f9b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to collect $\frac{N}{2}$ samples from the follower policies from a batch size of $N$ samples, to be used to update the leader.
- **Parent context**: The procedure for sampling on-policy data for the leader, and sub-sampling off-policy data from foll...

### R11: Code has been written to collect on-policy samples from each...
- **Rubric ID**: 56005d05-b995-4d2f-93a7-14f287efd4c2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to collect on-policy samples from each follower policy, to be used to update each follower policy.
- **Parent context**: Leader-follower aggregation has been implemented as described in Section 4.3.

### R12: Code has been written to update the leader with PPO using on...
- **Rubric ID**: fefabdd4-f727-47e8-9a2c-941a5231757f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to update the leader with PPO using on-policy and off-policy data. The off-policy data is weighted by importance sampling.
- **Parent context**: Leader-follower aggregation has been implemented as described in Section 4.3.

### R13: Code has been written to share the backbone $B_theta$ betwee...
- **Rubric ID**: efcaae18-b57f-4001-9485-88dcbe3adacb
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to share the backbone $B_theta$ between the actor policies, conditioned on each policy's hanging parameters $phi_j$.
- **Parent context**: Diversity via latent conditioning has been implemented, as described in Section 4.4.

### R14: Code has been written to share the backbone $C_psi$ between...
- **Rubric ID**: dd211514-5e19-4f44-b10a-fd1e4d3688b8
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to share the backbone $C_psi$ between the actor and critic, conditioned on each policy's hanging parameters $phi_j$.
- **Parent context**: Diversity via latent conditioning has been implemented, as described in Section 4.4.

### R15: Code has been written to select one policy to be the leader...
- **Rubric ID**: 98b54a01-428b-470a-aae9-ff5851176bcd
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to select one policy to be the leader policy and the remaining $M-1$ policies to be the follower policies.
- **Parent context**: Leader-follower aggregation has been implemented as described in Section 4.3.

### R16: Code has been written to collect samples using the leader an...
- **Rubric ID**: 9a011b8c-39aa-48a2-846b-9c8f837d29x2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to collect samples using the leader and follower policies. 
- **Parent context**: Code has been written to sample on-policy data from the leader, and sub-sample off-policy data from ...

### R17: Code has been written to collect $\frac{N}{2}$ samples from...
- **Rubric ID**: d4e81d58-cf8b-4c6d-afa4-64f6385d7b19
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to collect $\frac{N}{2}$ samples from the leader policy from a batch size of $N$ samples, to be used to update the leader.
- **Parent context**: Code has been written to sample on-policy data from the leader, and sub-sample off-policy data from ...

### R18: Code has been written to collect $\frac{N}{2}$ samples from...
- **Rubric ID**: c6fdbab5-5537-4b74-9147-d3495c393f8b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to collect $\frac{N}{2}$ samples from the follower policies from a batch size of $N$ samples, to be used to update the leader.
- **Parent context**: Code has been written to sample on-policy data from the leader, and sub-sample off-policy data from ...

### R19: Code has been written to update each follower policy using P...
- **Rubric ID**: 56005d05-b995-4d2f-93a7-14f287efd4d2
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to update each follower policy using PPO with on-policy samples.
- **Parent context**: Leader-follower aggregation has been implemented as described in Section 4.3.

### R20: Code has been written to update the leader with PPO using on...
- **Rubric ID**: 534229ab-463a-49c3-a715-03bd07c86af6
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to update the leader with PPO using on-policy and off-policy data. The off-policy data is weighted by importance sampling.
- **Parent context**: Leader-follower aggregation has been implemented as described in Section 4.3.

### R21: Code has been written to add an entropy term to the loss of...
- **Rubric ID**: 0746e34d-9303-4463-80a9-198fd7b2028f
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to add an entropy term to the loss of each follower with hyper-parameter $\sigma$ as a coefficient.
- **Parent context**: Diversity through entropy regularization has been implemented, as described in Section 4.5.

### R22: Code has been written for the leader's loss, which, unlike t...
- **Rubric ID**: 34bb0d42-a4bc-4068-9029-84ebf09cbf07
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written for the leader's loss, which, unlike the followers, does not have an entropy term.
- **Parent context**: Diversity through entropy regularization has been implemented, as described in Section 4.5.

### R23: Code has been written to define the observation space, which...
- **Rubric ID**: 758a79c6-97bb-4ddb-a219-98d129d4a353
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to define the observation space, which consists of joint angles, joint velocities, object pose, object linear velocity, and object angular velocity.
- **Parent context**: The experimental setup has been replicated, as described in Section 5.

### R24: Code has been written to place an object in a random positio...
- **Rubric ID**: 94e1952d-cb93-4781-8cee-68782aea8b27
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to place an object in a random position on a table at initialization of a task.
- **Parent context**: The Regrasping task has been replicated, using 24576 parallel environments for testing.

### R25: Code has been written to place an object in a random positio...
- **Rubric ID**: 0c4e69ea-cbf4-49d9-ad39-62500fc4bf26
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to place an object in a random position on a table at initialization of a task.
- **Parent context**: The Throw task has been replicated, using 24576 parallel environments for testing.

### R26: Code has been written to place an object in a random positio...
- **Rubric ID**: c2ff9000-b2c1-420b-9644-7ec14f5e5a0b
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to place an object in a random position on a table at initialization of a task. 
- **Parent context**: The Reorientation task has been replicated, using 24576 parallel environments for testing.

### R27: Code has been written to use a shadow hand of 24 degrees of...
- **Rubric ID**: 5cb6fc5a-c1ee-4e27-a272-606f26591056
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to use a shadow hand of 24 degrees of freedom for manipulation.
- **Parent context**: The Shadow hand task has been implemented, using 24576 parallel environments for testing.     

### R28: Code has been written to use an Allegro hand of 16 degrees o...
- **Rubric ID**: 5607d2ef-d61e-4d1e-a1cc-18bd0d2e9832
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to use an Allegro hand of 16 degrees of freedom for manipulation.
- **Parent context**: The Allegro hand task has been implemented, using 24576 parallel environments for testing.     

### R29: Code has been written to re-initialize a task if marked as s...
- **Rubric ID**: 58b76d68-8183-4821-a35e-09fd168fc655
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to re-initialize a task if marked as success. 
- **Parent context**: The Allegro hand task has been implemented, using 24576 parallel environments for testing.     

### R30: Code has been written to import the PPO algorithm introduced...
- **Rubric ID**: 6a5b95b5-4593-4829-bf43-5138a4bd3412
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to import the PPO algorithm introduced by Schulman et al., 2017, as a baseline.
- **Parent context**: The baseline methods are available for comparison.

### R31: Code has been written to import the Parallel Q-learning algo...
- **Rubric ID**: cbee4c00-a3b0-42b3-b8e6-ac2091059933
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to import the Parallel Q-learning algorithm introduced by Li et al., 2023, as a baseline.
- **Parent context**: The baseline methods are available for comparison.

### R32: Code has been written to import the DexPBT algorithm introdu...
- **Rubric ID**: 760ed7c6-9a0d-48ac-b162-bae4611a1add
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to import the DexPBT algorithm introduced by Petrenko et al., 2023, as a baseline.
- **Parent context**: The baseline methods are available for comparison.

### R33: Code has been written to use six different policies for SAPG...
- **Rubric ID**: 79a1c008-6b96-4d5f-945b-9baa0e423325
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to use six different policies for SAPG and DexPBT.
- **Parent context**: The experimental setup has been replicated, as described in Section 5.

### R34: Code has been written to use a recurrent policy for AllegroK...
- **Rubric ID**: 5bf9383b-4137-4d28-a4fa-c4ecf78fe993
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to use a recurrent policy for AllegroKuka tasks.
- **Parent context**: The experimental setup has been replicated, as described in Section 5.

### R35: Code has been written to use an MLP policy for Shadow Hand a...
- **Rubric ID**: 61c3894d-d8a6-4b6e-88b6-9990d7ec6bc9
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to use an MLP policy for Shadow Hand and Allegro Hand tasks.
- **Parent context**: The experimental setup has been replicated, as described in Section 5.

### R36: Code has been written to either implement or import a pre-ex...
- **Rubric ID**: 378939a7-a875-4d9f-961d-f3292f16c8aa
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to either implement or import a pre-existing implementation of PCA.
- **Parent context**: Figure 7 has been replicated.

### R37: Code has been written to implement a neural network that rec...
- **Rubric ID**: 33bc9166-c1ec-4412-aa3c-f488ba1a2cdc
- **Category**: Code Development / Method Implementation
- **Weight**: 1
- **Requirement**: Code has been written to implement a neural network that reconstructs the input. The neural network is made up of two layers, and the size of the layers vary from 8 to 64 neurons. The activation function is ReLU, and Adam is used as optimizer. The loss is the L2 reconstruction error of predicted state transitions.
- **Parent context**: Figure 8 has been replicated.

## Experimental Setup

### R38: Code has been written to set the parameter lambda for off-po...
- **Rubric ID**: 67f4ae44-528e-429a-88ff-b8f532909598
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to set the parameter lambda for off-policy updates to 1.
- **Parent context**: Symmetric aggregation has been implemented as described in Section 4.2.

### R39: $M$ different policies are used to collect samples.
- **Rubric ID**: cb7f70fe-ae90-471f-8514-c34edae8f801
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: $M$ different policies are used to collect samples.
- **Parent context**: Leader-follower aggregation has been implemented as described in Section 4.3.

### R40: One policy is selected to be the leader policy and the remai...
- **Rubric ID**: 98b54a01-428b-470a-aae9-ff5851176bfd
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: One policy is selected to be the leader policy and the remaining $M-1$ policies are selected to be the follower policies.
- **Parent context**: Leader-follower aggregation has been implemented as described in Section 4.3.

### R41: Code has been written to collect $\frac{N}{2}$ samples from...
- **Rubric ID**: d4e81d58-cf8b-4c6d-afa4-64f6385d7b18
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to collect $\frac{N}{2}$ samples from the leader policy from a batch size of $N$ samples, to be used to update the leader.
- **Parent context**: The procedure for sampling on-policy data for the leader, and sub-sampling off-policy data from foll...

### R42: Code has been written to set the parameter lambda for off-po...
- **Rubric ID**: cfbaa359-30ff-4059-8399-0d8942a6eb25
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to set the parameter lambda for off-policy updates to 1.
- **Parent context**: Leader-follower aggregation has been implemented as described in Section 4.3.

### R43: Code has been written to set the parameter lambda for off-po...
- **Rubric ID**: cfbaa359-30ff-4059-8399-0d8942a6eb15
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to set the parameter lambda for off-policy updates to 1.
- **Parent context**: Leader-follower aggregation has been implemented as described in Section 4.3.

### R44: Code has been written to select a three dimensional position...
- **Rubric ID**: 88db1925-492d-4e7c-89ed-adcfe588b676
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to select a three dimensional position at random as the goal at initialization of a task.
- **Parent context**: The Regrasping task has been replicated, using 24576 parallel environments for testing.

### R45: Code has been written to re-initialize a task if marked as s...
- **Rubric ID**: 4ddc20c9-92e9-4215-9ad6-27d0e6b66a59
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to re-initialize a task if marked as success.
- **Parent context**: The Regrasping task has been replicated, using 24576 parallel environments for testing.

### R46: Code has been written to re-initialize a task if marked as s...
- **Rubric ID**: 82a09e6b-28f7-4eb2-8dac-301a1b8d31c2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to re-initialize a task if marked as success.
- **Parent context**: The Throw task has been replicated, using 24576 parallel environments for testing.

### R47: Code has been written to select a pose in 7 dimensions at ra...
- **Rubric ID**: 84a8972c-4571-4c4a-9154-52b920cb9246
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to select a pose in 7 dimensions at random as the goal at initialization of a task.
- **Parent context**: The Reorientation task has been replicated, using 24576 parallel environments for testing.

### R48: Code has been written to select a new pose as the goal if th...
- **Rubric ID**: dbea6a1f-ff1b-43b3-af09-daa5e91b1b05
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to select a new pose as the goal if the task is marked as success.
- **Parent context**: The Reorientation task has been replicated, using 24576 parallel environments for testing.

### R49: Code has been written to place a cube on the hand and pick a...
- **Rubric ID**: 7ca105e5-4ba2-42e7-9af3-34d270cad350
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to place a cube on the hand and pick an orientation as random as the goal at initialization of a task.
- **Parent context**: The Shadow hand task has been implemented, using 24576 parallel environments for testing.     

### R50: Code has been written to re-initialize a task if marked as s...
- **Rubric ID**: a7c600b0-d7ab-4635-bde8-8328a193e20d
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to re-initialize a task if marked as success.
- **Parent context**: The Shadow hand task has been implemented, using 24576 parallel environments for testing.     

### R51: Code has been written to place a cube on the hand and pick a...
- **Rubric ID**: 1beb950d-2248-4bed-9e14-f14a69eceba1
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to place a cube on the hand and pick an orientation as random as the goal at initialization of a task. 
- **Parent context**: The Allegro hand task has been implemented, using 24576 parallel environments for testing.     

### R52: Code has been written to run five different seeds for each e...
- **Rubric ID**: e72b38d4-74ae-46b4-b458-2edad4774d27
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to run five different seeds for each experiment.
- **Parent context**: The experimental setup has been replicated, as described in Section 5.

### R53: Code has been written to collect 16 steps of experience per...
- **Rubric ID**: 5aed04e1-078b-4325-a6ac-88959f972298
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to collect 16 steps of experience per instance of the environment before every PPO update.
- **Parent context**: The experimental setup has been replicated, as described in Section 5.

### R54: Code has been written to set the entropy coefficient to eith...
- **Rubric ID**: 846e182a-bcbb-4340-a10f-37300c06ae21
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to set the entropy coefficient to either 0.0, 0.003, or 0.005 for SAPG.
- **Parent context**: The experimental setup has been replicated, as described in Section 5.

### R55: Code has been written to set the entropy coefficient to 0 fo...
- **Rubric ID**: dfe1b771-6aee-4cdb-9b9a-0e4d6429ac9c
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to set the entropy coefficient to 0 for SAPG in the tasks ShadowHand, AllegroHand, Regreasping, and Throw.
- **Parent context**: The experimental setup has been replicated, as described in Section 5.

### R56: Code has been written to set the entropy coefficient to 0.00...
- **Rubric ID**: 2a843a97-d82b-470f-91b1-a9d39257ac8e
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to set the entropy coefficient to 0.005 for SAPG in the task Reorientation. 
- **Parent context**: The experimental setup has been replicated, as described in Section 5.

### R57: Code has been written to train PPO for 7 different batch siz...
- **Rubric ID**: 92e9f9ec-a6b6-4fe1-95ba-1886c631f8c2
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train PPO for 7 different batch sizes ranking in the approximate values of $\{1500, 3125, 6250, 12500, 25000, 50000, 100000\}$.
- **Parent context**: The results for the Shadow Hand task have been replicated.

### R58: Code has been written to train PPO for 7 different batch siz...
- **Rubric ID**: d411af2a-536b-44a6-a296-047d05d62b49
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train PPO for 7 different batch sizes ranking in the approximate values of $\{1500, 3125, 6250, 12500, 25000, 50000, 100000\}$.
- **Parent context**: The results for Allegro Kuka Throw task has been replicated.

### R59: Code has been written to train and evaluate PPO in the Alleg...
- **Rubric ID**: 843cca35-7ec5-4cc4-8c80-e56e75f320e6
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train and evaluate PPO in the Allegro Kuka Regrasping task.
- **Parent context**: PPO results were replicated in Allegro Kuka Regrasping.

### R60: Code has been written to train and evaluate PQL in the Alleg...
- **Rubric ID**: 842335e8-8d9f-48dd-bf0f-826e0cf6cd80
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train and evaluate PQL in the Allegro Kuka Regrasping task.
- **Parent context**: PQL results were replicated in Allegro Kuka Regrasping.

### R61: Code has been written to train and evaluate PBT in the Alleg...
- **Rubric ID**: a81b790b-a196-4697-af20-124c77738773
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train and evaluate PBT in the Allegro Kuka Regrasping task.
- **Parent context**: PBT results were replicated in Allegro Kuka Regrasping.

### R62: Code has been written to train and evaluate SAPG in the Alle...
- **Rubric ID**: 3cdd3bb7-802f-4d1f-8b34-058bd2939ca8
- **Category**: Code Development / Experimental Setup
- **Weight**: 1
- **Requirement**: Code has been written to train and evaluate SAPG in the Allegro Kuka Regrasping task.
- **Parent context**: SAPG results were replicated in Allegro Kuka Regrasping.

### R63: PPO has been trained and evaluated in Allegro Kuka Throw tas...
- **Rubric ID**: e8ec7033-7d4f-405d-9536-117cbcd6b5af
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: PPO has been trained and evaluated in Allegro Kuka Throw task.
- **Parent context**: PPO results were replicated in Allegro Kuka Throw.

### R64: PQL has been trained and evaluated in Allegro Kuka Throw tas...
- **Rubric ID**: 4f88f0f3-0aaa-40e0-b1a0-4ed11e1b4755
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: PQL has been trained and evaluated in Allegro Kuka Throw task.
- **Parent context**: PQL results were replicated in Allegro Kuka Throw.

### R65: PBT has been trained and evaluated in Allegro Kuka Throw tas...
- **Rubric ID**: 723628ad-6f81-478e-bf22-275a8bbf5536
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: PBT has been trained and evaluated in Allegro Kuka Throw task.
- **Parent context**: PBT results were replicated in Allegro Kuka Throw.

### R66: SAPG has been trained and evaluated in Allegro Kuka Throw ta...
- **Rubric ID**: 418b0c7b-d273-447d-a193-8f784834650c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated in Allegro Kuka Throw task.
- **Parent context**: SAPG results were replicated in Allegro Kuka Throw.

### R67: PPO has been trained and evaluated in Allegro Kuka Reorienta...
- **Rubric ID**: 9da703e9-7fb2-46c4-a950-52db7ec2ce2a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: PPO has been trained and evaluated in Allegro Kuka Reorientation task.
- **Parent context**: PPO results were replicated in Allegro Kuka Reorientation.

### R68: PQL has been trained and evaluated in Allegro Kuka Reorienta...
- **Rubric ID**: 49b1b68b-25e5-4fd4-ada1-38b6a3ce0509
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: PQL has been trained and evaluated in Allegro Kuka Reorientation task.
- **Parent context**: PQL results were replicated in Allegro Kuka Reorientation. 

### R69: PBT has been trained and evaluated in Allegro Kuka Reorienta...
- **Rubric ID**: e95fa200-58f7-4653-a16b-5f197593fdf5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: PBT has been trained and evaluated in Allegro Kuka Reorientation task.
- **Parent context**: PBT results were replicated in Allegro Kuka Reorientation. 

### R70: SAPG has been trained and evaluated in Allegro Kuka Reorient...
- **Rubric ID**: 4b212195-caad-4dc9-b977-ff9defcb4814
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated in Allegro Kuka Reorientation task.
- **Parent context**: SAPG results were replicated in Allegro Kuka Reorientation. 

### R71: PPO has been trained and evaluated in Allegro Hand task.
- **Rubric ID**: ec31266e-7771-4899-9507-329b405b6e3a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: PPO has been trained and evaluated in Allegro Hand task.
- **Parent context**: PPO results were replicated in Allegro Hand.

### R72: PBT has been trained and evaluated in Allegro Hand task.
- **Rubric ID**: 97958a51-f0ca-48bc-bdf6-83cef65a1683
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: PBT has been trained and evaluated in Allegro Hand task.
- **Parent context**: PBT results were replicated in Allegro Hand.

### R73: SAPG has been trained and evaluated in Allegro Hand task.
- **Rubric ID**: 210a9216-a1e4-4002-9b10-ccc74736409f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated in Allegro Hand task.
- **Parent context**: SAPG results were replicated in Allegro Hand.

### R74: PPO has been trained and evaluated in Shadow Hand task.
- **Rubric ID**: 03340bc7-510c-4ce5-80aa-d4b2f8847885
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: PPO has been trained and evaluated in Shadow Hand task.
- **Parent context**: PPO results were replicated in Shadow Hand. 

### R75: PBT has been trained and evaluated in Shadow Hand task.
- **Rubric ID**: 476e166e-b412-413e-825e-07c57c90300c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: PBT has been trained and evaluated in Shadow Hand task.
- **Parent context**: PBT results were replicated in Shadow Hand. 

### R76: SAPG has been trained and evaluated in Shadow Hand task.
- **Rubric ID**: 4f86c6af-8e3c-4244-91c3-b3aba40a95c3
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated in Shadow Hand task.
- **Parent context**: SAPG results were replicated in Shadow Hand. 

### R77: SAPG has been trained and evaluated without off-policy data...
- **Rubric ID**: e5d82530-a420-4f27-b38f-890b0576e2d4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated without off-policy data in Allegro Kuka Regrasping
- **Parent context**: The results for Allegro Kuka Regrasping task have been replicated.

### R78: SAPG has been trained and evaluated using symmetric off-poli...
- **Rubric ID**: 8c58346a-161b-418d-86e0-30db27cf5a15
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using symmetric off-policy data in Allegro Kuka Regrasping
- **Parent context**: The results for Allegro Kuka Regrasping task have been replicated.

### R79: SAPG has been trained and evaluated using high off-policy da...
- **Rubric ID**: 1dcfdd84-93b6-482c-83b9-8faddb7c55f4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using high off-policy data ratio in Allegro Kuka Regrasping
- **Parent context**: The results for Allegro Kuka Regrasping task have been replicated.

### R80: SAPG has been trained and evaluated using entropy coefficien...
- **Rubric ID**: 12910787-89ca-4548-a6c3-357bd40c296d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using entropy coefficient of 0.003 in Allegro Kuka Regrasping
- **Parent context**: The results for Allegro Kuka Regrasping task have been replicated.

### R81: SAPG has been trained and evaluated using entropy coefficien...
- **Rubric ID**: 84211932-bb8a-4ca3-a9c0-7fd864da78da
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using entropy coefficient of 0.005 in Allegro Kuka Regrasping
- **Parent context**: The results for Allegro Kuka Regrasping task have been replicated.

### R82: Standard SAPG has been trained and evaluated in Allegro Kuka...
- **Rubric ID**: 07a91966-1c5d-48c0-bb66-79ec371a1879
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Standard SAPG has been trained and evaluated in Allegro Kuka Regrasping
- **Parent context**: The results for Allegro Kuka Regrasping task have been replicated.

### R83: SAPG has been trained and evaluated without off-policy data...
- **Rubric ID**: 128d2bf1-dd3b-4d6d-a1e2-2f79d915ac73
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated without off-policy data in Allegro Kuka Throw
- **Parent context**: The results for the Allegro Kuka Throw task have been replicated.

### R84: SAPG has been trained and evaluated using symmetric off-poli...
- **Rubric ID**: 0edf5ba9-c61d-4074-9ec8-7c78c6c9fbdd
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using symmetric off-policy data in Allegro Kuka Throw
- **Parent context**: The results for the Allegro Kuka Throw task have been replicated.

### R85: SAPG has been trained and evaluated using high off-policy da...
- **Rubric ID**: 3ab7a450-8aef-4ad9-ab8b-25ff06f84858
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using high off-policy data ratio in Allegro Kuka Throw
- **Parent context**: The results for the Allegro Kuka Throw task have been replicated.

### R86: SAPG has been trained and evaluated using entropy coefficien...
- **Rubric ID**: 75d8b372-80d8-4e34-b75c-606bc06b917e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using entropy coefficient of 0.003 in Allegro Kuka Throw
- **Parent context**: The results for the Allegro Kuka Throw task have been replicated.

### R87: SAPG has been trained and evaluated using entropy coefficien...
- **Rubric ID**: 1358faca-0b44-49aa-894f-6c57b199d672
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using entropy coefficient of 0.005 in Allegro Kuka Throw
- **Parent context**: The results for the Allegro Kuka Throw task have been replicated.

### R88: Standard SAPG has been trained and evaluated in Allegro Kuka...
- **Rubric ID**: e87ccb36-20f8-4bbe-bd3f-86a9b8517b40
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Standard SAPG has been trained and evaluated in Allegro Kuka Throw
- **Parent context**: The results for the Allegro Kuka Throw task have been replicated.

### R89: SAPG has been trained and evaluated without off-policy data...
- **Rubric ID**: a64d9d7b-1c5b-4037-a275-9dd37c646acf
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated without off-policy data in Allegro Kuka Reorientation task
- **Parent context**: The results  for the Allegro Kuka Reorientation task have been replicated.

### R90: SAPG has been trained and evaluated using symmetric off-poli...
- **Rubric ID**: cfb5b8b1-bb67-4098-83d2-e7c001741e07
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using symmetric off-policy data in Allegro Kuka Reorientation task.
- **Parent context**: The results  for the Allegro Kuka Reorientation task have been replicated.

### R91: SAPG has been trained and evaluated using high off-policy in...
- **Rubric ID**: 7420e98b-5d3b-482b-aac5-55d5d8df956c
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using high off-policy in Allegro Kuka Reorientation task.
- **Parent context**: The results  for the Allegro Kuka Reorientation task have been replicated.

### R92: SAPG has been trained and evaluated using entropy coefficien...
- **Rubric ID**: 40352f5e-b9fa-41b1-b386-bfd6717b8b0f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using entropy coefficient of 0.003 in Allegro Kuka Reorientation task.
- **Parent context**: The results  for the Allegro Kuka Reorientation task have been replicated.

### R93: SAPG has been trained and evaluated using entropy coefficien...
- **Rubric ID**: 623dfcd6-ae62-4ce6-89b3-4b0051506fda
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using entropy coefficient of 0.005 in Allegro Kuka Reorientation task.
- **Parent context**: The results  for the Allegro Kuka Reorientation task have been replicated.

### R94: Standard SAPG has been trained and evaluated in Allegro Kuka...
- **Rubric ID**: 856460c8-b9b1-484e-aded-ae66e8feed06
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Standard SAPG has been trained and evaluated in Allegro Kuka Reorientation task.
- **Parent context**: The results  for the Allegro Kuka Reorientation task have been replicated.

### R95: SAPG has been trained and evaluated without off-policy data...
- **Rubric ID**: 089e4282-7b03-4139-9bf8-efeb7847b4f4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated without off-policy data in Shadow Hand task.
- **Parent context**: The results for the Allegro Hand task have been replicated.

### R96: SAPG has been trained and evaluated using symmetric off-poli...
- **Rubric ID**: d9092acc-258f-48ef-a0ee-f7fc1806a11a
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using symmetric off-policy data in Shadow Hand task.
- **Parent context**: The results for the Allegro Hand task have been replicated.

### R97: SAPG has been trained and evaluated using high off-policy in...
- **Rubric ID**: 5c21bf63-50ad-4638-a3ef-6af9a675f4c0
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using high off-policy in Shadow Hand task.
- **Parent context**: The results for the Allegro Hand task have been replicated.

### R98: Standard SAPG has been trained and evaluated in Shadow Hand...
- **Rubric ID**: 6d1e068e-afe6-4abc-8373-4d9654a4a4a8
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Standard SAPG has been trained and evaluated in Shadow Hand task.
- **Parent context**: The results for the Allegro Hand task have been replicated.

### R99: SAPG has been trained and evaluated using entropy coefficien...
- **Rubric ID**: 00b99a98-0c98-4b8f-ab39-c30a3c4a5fdb
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using entropy coefficient of 0.003 in Shadow Hand task.
- **Parent context**: The results for the Allegro Hand task have been replicated.

### R100: SAPG has been trained and evaluated using entropy coefficien...
- **Rubric ID**: e14a9452-e4a1-4b27-8701-4937cbaa18eb
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using entropy coefficient of 0.005 in Shadow Hand task.
- **Parent context**: The results for the Allegro Hand task have been replicated.

### R101: SAPG has been trained and evaluated without off-policy data...
- **Rubric ID**: 258af484-b7bb-4d89-8532-ed7feaf93690
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated without off-policy data in Shadow Hand task.
- **Parent context**: The results for the Shadow Hand task have been replicated.

### R102: SAPG has been trained and evaluated using symmetric off-poli...
- **Rubric ID**: 41f1a669-38a4-4e2d-8ea6-f3c0d8aaa6a7
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using symmetric off-policy data in Shadow Hand task.
- **Parent context**: The results for the Shadow Hand task have been replicated.

### R103: SAPG has been trained and evaluated using high off-policy in...
- **Rubric ID**: ada9a9c5-002d-4ead-9290-81551f332ec4
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using high off-policy in Shadow Hand task.
- **Parent context**: The results for the Shadow Hand task have been replicated.

### R104: Standard SAPG has been trained and evaluated in Shadow Hand...
- **Rubric ID**: 9c9b9344-a9fa-4bfb-9cf7-4c60fca6632b
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: Standard SAPG has been trained and evaluated in Shadow Hand task.
- **Parent context**: The results for the Shadow Hand task have been replicated.

### R105: SAPG has been trained and evaluated using entropy coefficien...
- **Rubric ID**: f2fe516f-6c8c-4147-9265-9988be784a6e
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using entropy coefficient of 0.005 in Shadow Hand task.
- **Parent context**: The results for the Shadow Hand task have been replicated.

### R106: SAPG has been trained and evaluated using entropy coefficien...
- **Rubric ID**: 4584f422-849c-4348-be43-7c923362554d
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: SAPG has been trained and evaluated using entropy coefficient of 0.003 in Shadow Hand task.
- **Parent context**: The results for the Shadow Hand task have been replicated.

### R107: The neural network has been trained on state transition from...
- **Rubric ID**: 5bc4d623-5c81-4885-82c5-13b4d602487f
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The neural network has been trained on state transition from SAPG and the reconstruction error caculated.
- **Parent context**: Allegro Kuka Reorientation results have been replicated.

### R108: The neural network has been trained on state transition from...
- **Rubric ID**: cf84c344-b6ee-4410-8d91-e7f5eeb5d947
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The neural network has been trained on state transition from a random policy and the reconstruction error caculated.
- **Parent context**: Allegro Kuka Reorientation results have been replicated.

### R109: The neural network has been trained on state transition from...
- **Rubric ID**: dfe2ed08-7c47-4d46-bc33-2e5bfeb14809
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The neural network has been trained on state transition from SAPG and the reconstruction error caculated.
- **Parent context**: Allegro Kuka Regrasping results have been replicated.

### R110: The neural network has been trained on state transition from...
- **Rubric ID**: d6d6cff2-2e7d-401e-97bf-48e13e0ab859
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The neural network has been trained on state transition from a random policy and the reconstruction error caculated.
- **Parent context**: Allegro Kuka Regrasping results have been replicated.

### R111: The neural network has been trained on state transition from...
- **Rubric ID**: fcce8750-c793-4292-8d55-4b074035e2e1
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The neural network has been trained on state transition from SAPG and the reconstruction error caculated. 
- **Parent context**: Allegro Kuka Throw results have been replicated.

### R112: The neural network has been trained on state transition from...
- **Rubric ID**: c266b447-dbe9-4435-849f-df677ceefbe5
- **Category**: Code Execution / Experimental Setup
- **Weight**: 1
- **Requirement**: The neural network has been trained on state transition from a random policy and the reconstruction error caculated. 
- **Parent context**: Allegro Kuka Throw results have been replicated.

## Evaluation, Metrics & Benchmarking

### R113: Code has been written to collect samples using $M$ different...
- **Rubric ID**: cb7f70fe-ae90-471f-8514-c34edae8f811
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to collect samples using $M$ different policies.
- **Parent context**: Leader-follower aggregation has been implemented as described in Section 4.3.

### R114: Code has been written to mark a task as success if the arm l...
- **Rubric ID**: 185eb404-5449-4ccc-b4aa-0e9ce4c6a9fc
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to mark a task as success if the arm lifts the object and holds it at the goal position for 30 time-steps.
- **Parent context**: The Regrasping task has been replicated, using 24576 parallel environments for testing.

### R115: Code has been written to mark a task as success if the arm l...
- **Rubric ID**: 2fa8ea31-caca-414b-b778-50fea9ae2283
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to mark a task as success if the arm lifts the object and throws it into the bucket.
- **Parent context**: The Throw task has been replicated, using 24576 parallel environments for testing.

### R116: Code has been written to mark a task as success if the arm i...
- **Rubric ID**: 6adb40f3-9ff7-454c-96e0-ad17354fb498
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to mark a task as success if the arm is able to orient the object in the goal pose.
- **Parent context**: The Reorientation task has been replicated, using 24576 parallel environments for testing.

### R117: Code has been written to mark a task as success when the cub...
- **Rubric ID**: 4aa6c053-2695-4499-8f90-5cb2416f71ce
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to mark a task as success when the cube reaches the goal orientation.
- **Parent context**: The Shadow hand task has been implemented, using 24576 parallel environments for testing.     

### R118: Code has been written to mark a task as success when the cub...
- **Rubric ID**: 34a9649f-f372-4489-a4d6-0b2c79b84faa
- **Category**: Code Development / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: Code has been written to mark a task as success when the cube reaches the goal orientation. 
- **Parent context**: The Allegro hand task has been implemented, using 24576 parallel environments for testing.     

### R119: The performance of PPO for all batch sizes was below 12,000.
- **Rubric ID**: 9ada4389-8b53-4d71-ad56-91399b0f3e02
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The performance of PPO for all batch sizes was below 12,000.
- **Parent context**: The results for the Shadow Hand task have been replicated.

### R120: SAPG performance reaches above 12,000; significantly higher...
- **Rubric ID**: 28229478-e3d1-4bb3-9d6d-481f685316e4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: SAPG performance reaches above 12,000; significantly higher than that of PPO.
- **Parent context**: The results for the Shadow Hand task have been replicated.

### R121: The performance of PPO for all batch sizes was no greater th...
- **Rubric ID**: 7dcfd407-ed9a-41e6-bdec-5d5f44e79a03
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The performance of PPO for all batch sizes was no greater than 20.
- **Parent context**: The results for Allegro Kuka Throw task has been replicated.

### R122: SAPG performance reaches approximately 30. Its performance i...
- **Rubric ID**: d76f0652-8315-4be3-9a22-79c94245b25e
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: SAPG performance reaches approximately 30. Its performance is significantly higher than that of PPO.
- **Parent context**: The results for Allegro Kuka Throw task has been replicated.

### R123: PPO in Allegro Kuka Regrasping task reaches about 10 success...
- **Rubric ID**: 711e25af-b2eb-46b7-b6a0-8cc60c606c48
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: PPO in Allegro Kuka Regrasping task reaches about 10 successes at the beginning of training, and quickly drops to about 0. It is the worst performing method in the test.
- **Parent context**: PPO results were replicated in Allegro Kuka Regrasping.

### R124: PQL in Allegro Kuka Regrasping task reaches a few number of...
- **Rubric ID**: a77aadc7-8925-4217-a7ea-140e852c7ed6
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: PQL in Allegro Kuka Regrasping task reaches a few number of successes at the beginning of training. Except for the beginning of training, it consistently performs better than PPO.
- **Parent context**: PQL results were replicated in Allegro Kuka Regrasping.

### R125: PBT in Allegro Kuka Regrasping task rapidly increases the nu...
- **Rubric ID**: bb6ca8ea-4738-4368-9161-768294785488
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: PBT in Allegro Kuka Regrasping task rapidly increases the number of successes during training. It significantly outperforms both PPO and PQL.
- **Parent context**: PBT results were replicated in Allegro Kuka Regrasping.

### R126: SAPG in Allegro Kuka Regrasping task rapidly increases the n...
- **Rubric ID**: d05489a2-c250-4b36-a6d2-fd96681470f9
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: SAPG in Allegro Kuka Regrasping task rapidly increases the number of successes during training. It outperforms PBT, and it is the best performing method.
- **Parent context**: SAPG results were replicated in Allegro Kuka Regrasping.

### R127: The number of success in PPO in Allegro Kuka Throw task show...
- **Rubric ID**: 674b8bd7-3c08-4526-b277-b491d419f240
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The number of success in PPO in Allegro Kuka Throw task show a rapid increase during training, but drops towards the end of training; it significantly outperforms PQL.
- **Parent context**: PPO results were replicated in Allegro Kuka Throw.

### R128: The number of success in PQL in Allegro Kuka Throw task is s...
- **Rubric ID**: 933b0de9-a09c-4bb7-8e3f-500b38706541
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The number of success in PQL in Allegro Kuka Throw task is slightly above 0 during training; it is the worst performing method.
- **Parent context**: PQL results were replicated in Allegro Kuka Throw.

### R129: The number of success in PBT in Allegro Kuka Throw task incr...
- **Rubric ID**: 833e2a43-ff46-4b25-a28a-4cf895de5ef9
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The number of success in PBT in Allegro Kuka Throw task increase rapidly during training; it outperforms PPO.
- **Parent context**: PBT results were replicated in Allegro Kuka Throw.

### R130: The number of successes in SAPG in Allegro Kuka Throw task i...
- **Rubric ID**: a5aa1216-118b-4cda-a0ef-b1e7667e87de
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The number of successes in SAPG in Allegro Kuka Throw task increase rapidly during training; it's the best performing method.
- **Parent context**: SAPG results were replicated in Allegro Kuka Throw.

### R131: The number of success in PPO in Allegro Kuka Reorientation t...
- **Rubric ID**: 83634e09-f1d3-4945-9f54-b32bcfab1933
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The number of success in PPO in Allegro Kuka Reorientation task is consistently approximately 0.
- **Parent context**: PPO results were replicated in Allegro Kuka Reorientation.

### R132: The number of success in PQL in Allegro Kuka Reorientation t...
- **Rubric ID**: 8bfc8f8e-977e-4183-a077-4232f8966649
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The number of success in PQL in Allegro Kuka Reorientation task is consistently approximately 0.
- **Parent context**: PQL results were replicated in Allegro Kuka Reorientation. 

### R133: The number of success in PBT in Allegro Kuka Reorientation i...
- **Rubric ID**: a304b983-430f-4c04-8db2-ee9e982e79d9
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The number of success in PBT in Allegro Kuka Reorientation increases steadily. It performs better than both PPO and PQL.
- **Parent context**: PBT results were replicated in Allegro Kuka Reorientation. 

### R134: The number of successes of SAPG in Allegro Kuka Reorientatio...
- **Rubric ID**: 8ce095a8-2423-4041-944c-c70dd3e80195
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The number of successes of SAPG in Allegro Kuka Reorientation increases steadily. It is the best performing method.
- **Parent context**: SAPG results were replicated in Allegro Kuka Reorientation. 

### R135: The reward of PPO in Allegro Hand task increases steadily. I...
- **Rubric ID**: 03fbc6dd-9df3-4c43-86ba-72bad1af6bf3
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The reward of PPO in Allegro Hand task increases steadily. It is only outperformed by PBT.
- **Parent context**: PPO results were replicated in Allegro Hand.

### R136: The reward of PBT in Allegro Hand task increases steadily, b...
- **Rubric ID**: d04b34bf-2027-492c-91e7-c2e0e515c275
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The reward of PBT in Allegro Hand task increases steadily, but it is the worst performing method.
- **Parent context**: PBT results were replicated in Allegro Hand.

### R137: PQL has been trained and evaluated in Allegro Hand task.
- **Rubric ID**: 40ef59ab-4063-4311-afbf-568dcd052edd
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: PQL has been trained and evaluated in Allegro Hand task.
- **Parent context**: PQL results were replicated in Allegro Hand.

### R138: The reward of PQL in Allegro Hand task increases steadily th...
- **Rubric ID**: f3d5704c-b9da-40be-95cf-9f87ab295527
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The reward of PQL in Allegro Hand task increases steadily throughout training. It is the best performing method.
- **Parent context**: SAPG results were replicated in Allegro Hand.

### R139: The reward of PPO in Shadow Hand task increases steadily. It...
- **Rubric ID**: d6c1f104-0072-4443-a1f8-ef1147b8daed
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The reward of PPO in Shadow Hand task increases steadily. It performs similarly to PBT.
- **Parent context**: PPO results were replicated in Shadow Hand. 

### R140: The reward of PBT in Shadow Hand task increases steadily. It...
- **Rubric ID**: 5ec68d84-872f-4e66-b9f1-f9532101b72f
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The reward of PBT in Shadow Hand task increases steadily. It performs similarly to PPO.
- **Parent context**: PBT results were replicated in Shadow Hand. 

### R141: PQL has been trained and evaluated in Shadow Hand task.
- **Rubric ID**: 49b4225f-984d-4d28-a9cf-5caa3d8407a2
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: PQL has been trained and evaluated in Shadow Hand task.
- **Parent context**: PQL results were replicated in Shadow Hand. 

### R142: The reward of PQL in Shadow Hand task increases sharply at f...
- **Rubric ID**: 8c1acd48-8b0e-4b5d-8073-de3db0c72873
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The reward of PQL in Shadow Hand task increases sharply at first and then plateaus. It outperforms both PPO. and PBT, and achieves similar performance as SAPG.
- **Parent context**: PQL results were replicated in Shadow Hand. 

### R143: The reward of SAPG in Shadow Hand task increases steadily. I...
- **Rubric ID**: 9b79ceec-714e-4002-8377-11a833db4689
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The reward of SAPG in Shadow Hand task increases steadily. It outperforms both PPO. and PBT, and achieves similar performance as PQL.
- **Parent context**: SAPG results were replicated in Shadow Hand. 

### R144: The average reward for PPO was 1.01e4 with a standard error...
- **Rubric ID**: b63c5ff5-aa82-486c-b7ab-c2cdba010e7a
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average reward for PPO was 1.01e4 with a standard error of 6.31e2 after 2e10 samples.
- **Parent context**: AllegroHand results from table 1 have been replicated.

### R145: The average reward for PBT was 7.28e3 with a standard error...
- **Rubric ID**: 33580075-0b95-45bb-9251-52da4510ee7b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average reward for PBT was 7.28e3 with a standard error of 1.24e3 after 2e10 samples.
- **Parent context**: AllegroHand results from table 1 have been replicated.

### R146: The average reward for PQL was 1.01e4 with a standard error...
- **Rubric ID**: 0c8b9796-2fd8-499c-a49d-a388fcf48400
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average reward for PQL was 1.01e4 with a standard error of 5.28e2 after 2e10 samples.
- **Parent context**: AllegroHand results from table 1 have been replicated.

### R147: The average reward for SAPG with entropy coefficient of 0 wa...
- **Rubric ID**: 9a1f61db-e368-4228-9aae-3f39970e4de2
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average reward for SAPG with entropy coefficient of 0 was 1.23e4 with a standard error of 3.29e2 after 2e10 samples.
- **Parent context**: AllegroHand results from table 1 have been replicated.

### R148: The average reward for SAPG with entropy coefficient of 0.00...
- **Rubric ID**: 8a568508-ec25-46a5-9b24-ab13f2820d91
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average reward for SAPG with entropy coefficient of 0.005 was 9.14e3 with a standard error of 8.38e2 after 2e10 samples.
- **Parent context**: AllegroHand results from table 1 have been replicated.

### R149: The average reward for PPO was 1.07e4 with a standard error...
- **Rubric ID**: 2c2a52f0-aff6-4b5e-b33f-95c5bebf7c5b
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average reward for PPO was 1.07e4 with a standard error of 4.90e2 after 2e10 samples.
- **Parent context**: ShadowHand results from table 1 have been replicated.

### R150: The average reward for PBT was 1.01e4 with a standard error...
- **Rubric ID**: cdca77ff-3541-4044-926c-8100d9272b51
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average reward for PBT was 1.01e4 with a standard error of 1.80e2 after 2e10 samples.
- **Parent context**: ShadowHand results from table 1 have been replicated.

### R151: The average reward for PQL was 1.28e4 with a standard error...
- **Rubric ID**: e919fe9f-7cd1-4b81-b8c0-7a7d4df7d6f0
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average reward for PQL was 1.28e4 with a standard error of 1.25e2 after 2e10 samples.
- **Parent context**: ShadowHand results from table 1 have been replicated.

### R152: The average reward for SAPG with entropy coefficient of 0 wa...
- **Rubric ID**: 86a7d4cc-ee31-41c7-9b88-ba978e6b86b4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average reward for SAPG with entropy coefficient of 0 was 1.17e4 with a standard error of 2.64e2 after 2e10 samples.
- **Parent context**: ShadowHand results from table 1 have been replicated.

### R153: The average reward for SAPG with entropy coefficient of 0.00...
- **Rubric ID**: 8e8575f2-d93e-4447-a7f0-8e40441f0ef4
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average reward for SAPG with entropy coefficient of 0.005 was 1.28e4 with a standard error of 2.80e2 after 2e10 samples.
- **Parent context**: ShadowHand results from table 1 have been replicated.

### R154: The average number of successes for PBT was 31.9 with a stan...
- **Rubric ID**: 8f9f267a-3787-46af-b5b0-0d8361dcdc9e
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average number of successes for PBT was 31.9 with a standard error of 2.26 after 2e10 samples.
- **Parent context**: Regrasping results from table 1 have been replicated.

### R155: The average number of successes for PQL was 2.73 with a stan...
- **Rubric ID**: c7fe1dbb-6064-45b6-826d-0461ce49fa78
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average number of successes for PQL was 2.73 with a standard error of 0.02 after 2e10 samples.
- **Parent context**: Regrasping results from table 1 have been replicated.

### R156: The average number of successes for SAPG with entropy coeffi...
- **Rubric ID**: 6e3a8ad2-1210-47e2-a4e0-0839ae6c4415
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average number of successes for SAPG with entropy coefficient of 0 was 35.7 with a standard error of 1.46 after 2e10 samples.
- **Parent context**: Regrasping results from table 1 have been replicated.

### R157: SAPG with entropy coefficient of 0 is the best performing me...
- **Rubric ID**: 2fa1bea1-4e1b-4eeb-9f12-4f3645f0a2ba
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: SAPG with entropy coefficient of 0 is the best performing method.
- **Parent context**: Regrasping results from table 1 have been replicated.

### R158: The average number of successes for PPO was 16.8 with a stan...
- **Rubric ID**: e55ce7fb-5c79-49dd-83f1-71b2cea1ba5c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average number of successes for PPO was 16.8 with a standard error of 0.48 after 2e10 samples.
- **Parent context**: Throw results from table 1 have been replicated.

### R159: The average number of successes for PBT was 19.2 with a stan...
- **Rubric ID**: a891f6c5-1567-4a4b-b8e6-10f7b9b288d5
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average number of successes for PBT was 19.2 with a standard error of 1.07 after 2e10 samples.
- **Parent context**: Throw results from table 1 have been replicated.

### R160: The average number of successes for PQL was 2.62 with a stan...
- **Rubric ID**: 757a9a3f-aec6-465b-be05-6d5b5b66e624
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average number of successes for PQL was 2.62 with a standard error of 0.08 after 2e10 samples.
- **Parent context**: Throw results from table 1 have been replicated.

### R161: The average number of successes for SAPG with entropy coeffi...
- **Rubric ID**: 8dd86030-c998-47db-a776-55b02bc2ec6e
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average number of successes for SAPG with entropy coefficient of 0 was 23.7 with a standard error of 0.74 after 2e10 samples.
- **Parent context**: Throw results from table 1 have been replicated.

### R162: The average number of successes for SAPG with entropy coeffi...
- **Rubric ID**: 8d3d1a09-93e5-4faf-b7a8-a0085ed609b2
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average number of successes for SAPG with entropy coefficient of 0.005 was 18.7 with a standard error of 0.43 after 2e10 samples.
- **Parent context**: Throw results from table 1 have been replicated.

### R163: SAPG with entropy coefficient of 0 is the best performing me...
- **Rubric ID**: 0d2b3237-5f84-4ab9-bc77-c38f31c4d55a
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: SAPG with entropy coefficient of 0 is the best performing method.
- **Parent context**: Throw results from table 1 have been replicated.

### R164: The average number of successes for PPO was 2.85 with a stan...
- **Rubric ID**: 54a5ed8e-6a0b-428b-b11b-6e25cee63687
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average number of successes for PPO was 2.85 with a standard error of 0.05 after 2e10 samples.
- **Parent context**: Reorientation results from table 1 have been replicated.

### R165: The average number of successes for PBT was 23.2 with a stan...
- **Rubric ID**: ca949fe5-d656-4294-8a34-ba6231f2cbed
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average number of successes for PBT was 23.2 with a standard error of 4.86 after 2e10 samples.
- **Parent context**: Reorientation results from table 1 have been replicated.

### R166: The average number of successes for PQL was 1.66 with a stan...
- **Rubric ID**: 01475549-724a-4565-91cf-7dadde0b7473
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average number of successes for PQL was 1.66 with a standard error of 0.11 after 2e10 samples.
- **Parent context**: Reorientation results from table 1 have been replicated.

### R167: The average number of successes for SAPG with entropy coeffi...
- **Rubric ID**: f7c78019-2fc6-4e79-865a-061beae18526
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average number of successes for SAPG with entropy coefficient of 0 was 33.2 with a standard error of 4.20 after 2e10 samples.
- **Parent context**: Reorientation results from table 1 have been replicated.

### R168: The average number of successes for SAPG with entropy coeffi...
- **Rubric ID**: cae067cb-95bc-4206-83a9-69b6fdfd5266
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The average number of successes for SAPG with entropy coefficient of 0.005 was 38.6 with a standard error of 0.63 after 2e10 samples.
- **Parent context**: Reorientation results from table 1 have been replicated.

### R169: SAPG with entropy coefficient of 0.005 is the best performin...
- **Rubric ID**: 7ec5e1ed-21da-4769-b8eb-77ad0488dcc8
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: SAPG with entropy coefficient of 0.005 is the best performing method.
- **Parent context**: Reorientation results from table 1 have been replicated.

### R170: Training without off-policy data is the worst performing met...
- **Rubric ID**: 193b0859-6f88-4ce1-b596-12fff30772ff
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: Training without off-policy data is the worst performing method. Using symmetric off-policy improves things a bit. The other methods all perform significantly better.
- **Parent context**: The results for Allegro Kuka Regrasping task have been replicated.

### R171: Training without off-policy data is the worst performing met...
- **Rubric ID**: bd416f08-3b17-415b-a140-dbc7ccbde93f
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: Training without off-policy data is the worst performing method. All other methods perform better, and SAPG using entropy coefficient of 0.005 is the best performing method.
- **Parent context**: The results  for the Allegro Kuka Reorientation task have been replicated.

### R172: Training without off-policy data is the worst performing met...
- **Rubric ID**: 253cc3b2-d656-432b-bf8b-6ad4c4a6a66c
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: Training without off-policy data is the worst performing method. Using symmetric off-policy and high off-policy data improves results and perform similarly to each other. The best methods are standard SAPG and using entropy coefficient of 0.003.
- **Parent context**: The results for the Allegro Hand task have been replicated.

### R173: PCA has been computed for the visited states for PPO and the...
- **Rubric ID**: 2651eef0-98ed-44bd-acb9-a692c8c41778
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: PCA has been computed for the visited states for PPO and the reconstruction errors calculated for components 1 to 66.
- **Parent context**: The Allegro Kuka Reorientation plot has been replicated.

### R174: PCA has been computed for the visited states for a random po...
- **Rubric ID**: 1b5177e8-c14b-4d59-a6cc-4113d610c999
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: PCA has been computed for the visited states for a random policy and the reconstruction errors calculated for components 1 to 66.
- **Parent context**: The Allegro Kuka Reorientation plot has been replicated.

### R175: PCA has been computed for the visited states for PPO and the...
- **Rubric ID**: d99ea898-09a5-4681-b654-693764ae9e24
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: PCA has been computed for the visited states for PPO and the reconstruction errors calculated for components 1 to 56.
- **Parent context**: The Allegro Kuka Regrasping plot has been replicated.

### R176: PPO has the smallest reconstruction error for the first numb...
- **Rubric ID**: 21885969-e53c-4f34-b9e6-7d1b8961d12f
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: PPO has the smallest reconstruction error for the first number of components, and the random policy has the highest reconstruction error for the first number of components. SAPG has the highest reconstruction errors  when using more than 6 components. All methods have similar reconstruction errors when using more than 25 components.
- **Parent context**: The Allegro Kuka Regrasping plot has been replicated.

### R177: The random policy has the smallest reconstruction error when...
- **Rubric ID**: 8550d48c-e5e1-45ae-ae46-ea9ddcc5f838
- **Category**: Result Analysis / Evaluation, Metrics & Benchmarking
- **Weight**: 2
- **Requirement**: The random policy has the smallest reconstruction error when using less than 25 components, and SAPG has the highest reconstruction error for most number of components. All methods have similar reconstruction errors when using more than 25 components.
- **Parent context**: The Allegro Kuka Throw plot has been replicated.

### R178: The neural network has been trained on state transition from...
- **Rubric ID**: bf53661b-16f1-4cd5-b41f-ef4702c41e00
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The neural network has been trained on state transition from PPO and the reconstruction error caculated.
- **Parent context**: Allegro Kuka Reorientation results have been replicated.

### R179: The neural network has been trained on state transition from...
- **Rubric ID**: 52327a19-f739-4196-8fa0-cd33cd33052c
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The neural network has been trained on state transition from PPO and the reconstruction error caculated.
- **Parent context**: Allegro Kuka Regrasping results have been replicated.

### R180: The neural network has been trained on state transition from...
- **Rubric ID**: 1468bf1e-2431-45c4-bfee-79f0d972c1ce
- **Category**: Code Execution / Evaluation, Metrics & Benchmarking
- **Weight**: 1
- **Requirement**: The neural network has been trained on state transition from PPO and the reconstruction error caculated. 
- **Parent context**: Allegro Kuka Throw results have been replicated.

## Environment & Infrastructure Setup

### R181: Code has been written to import the Allegro Kuka Regrasping...
- **Rubric ID**: f83017dc-c6c0-4c2c-be6f-6982b2e37aed
- **Category**: Code Development / Environment & Infrastructure Setup
- **Weight**: 1
- **Requirement**: Code has been written to import the Allegro Kuka Regrasping environment from IsaacGymEnvs.
- **Parent context**: The Regrasping task has been replicated, using 24576 parallel environments for testing.

### R182: Code has been written to mount an Allegro Hand of 16 degrees...
- **Rubric ID**: 56a0ccfe-9d55-4d48-9ff1-5af0a7639e1c
- **Category**: Code Development / Environment & Infrastructure Setup
- **Weight**: 1
- **Requirement**: Code has been written to mount an Allegro Hand of 16 degrees of freedom on a Kuka arm of 7 degrees of freedom.
- **Parent context**: The Regrasping task has been replicated, using 24576 parallel environments for testing.

### R183: Code has been written to import the Allegro Kuka Throw envir...
- **Rubric ID**: 632bd411-ceeb-4284-8863-508e746edd7e
- **Category**: Code Development / Environment & Infrastructure Setup
- **Weight**: 1
- **Requirement**: Code has been written to import the Allegro Kuka Throw environment from IsaacGymEnvs.
- **Parent context**: The Throw task has been replicated, using 24576 parallel environments for testing.

### R184: Code has been written to mount an Allegro Hand of 16 degrees...
- **Rubric ID**: a7bdf75d-ab03-4e73-9a7a-59615e6764af
- **Category**: Code Development / Environment & Infrastructure Setup
- **Weight**: 1
- **Requirement**: Code has been written to mount an Allegro Hand of 16 degrees of freedom on a Kuka arm of 7 degrees of freedom.
- **Parent context**: The Throw task has been replicated, using 24576 parallel environments for testing.

### R185: Code has been written to place a bucket at a three dimension...
- **Rubric ID**: bf6d3e03-06ff-4e45-956b-f7b51e6faafa
- **Category**: Code Development / Environment & Infrastructure Setup
- **Weight**: 1
- **Requirement**: Code has been written to place a bucket at a three dimensional position that is out of reach of the arm at initialization of a task.
- **Parent context**: The Throw task has been replicated, using 24576 parallel environments for testing.

### R186: Code has been written to import the Allegro Kuka Reorientati...
- **Rubric ID**: d1c6dd90-961a-4945-889b-1f0320ecb02a
- **Category**: Code Development / Environment & Infrastructure Setup
- **Weight**: 1
- **Requirement**: Code has been written to import the Allegro Kuka Reorientation environment from IsaacGymEnvs.
- **Parent context**: The Reorientation task has been replicated, using 24576 parallel environments for testing.

### R187: Code has been written to mount an Allegro Hand of 16 degrees...
- **Rubric ID**: 0b281ca2-a6d3-4f2c-81e2-6c549010af8b
- **Category**: Code Development / Environment & Infrastructure Setup
- **Weight**: 1
- **Requirement**: Code has been written to mount an Allegro Hand of 16 degrees of freedom on a Kuka arm of 7 degrees of freedom. 
- **Parent context**: The Reorientation task has been replicated, using 24576 parallel environments for testing.

### R188: Code has been written to import the Shadow hand environment...
- **Rubric ID**: ef7bba46-13c6-4a75-9efb-986659c917ff
- **Category**: Code Development / Environment & Infrastructure Setup
- **Weight**: 1
- **Requirement**: Code has been written to import the Shadow hand environment from IsaacGymEnvs.
- **Parent context**: The Shadow hand task has been implemented, using 24576 parallel environments for testing.     

### R189: Code has been written to import the Allegro hand environment...
- **Rubric ID**: 98a3a49c-5a65-440c-b0b8-9ba652997297
- **Category**: Code Development / Environment & Infrastructure Setup
- **Weight**: 1
- **Requirement**: Code has been written to import the Allegro hand environment from IsaacGymEnvs.
- **Parent context**: The Allegro hand task has been implemented, using 24576 parallel environments for testing.     

## Logging, Analysis & Presentation

### R190: The reward of PQL in Allegro Hand task increases quickly and...
- **Rubric ID**: 1535c72d-9e09-46bd-871f-3557ba63bff0
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The reward of PQL in Allegro Hand task increases quickly and then plateaus. The performance is similar to that of PPO.
- **Parent context**: PQL results were replicated in Allegro Hand.

### R191: SAPG with entropy coefficient of 0 is the best performing me...
- **Rubric ID**: bb6200f6-75c5-4f32-bcfb-3b931e6d0117
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: SAPG with entropy coefficient of 0 is the best performing method.
- **Parent context**: AllegroHand results from table 1 have been replicated.

### R192: SAPG with entropy coefficient of 0.005 is the best performin...
- **Rubric ID**: 1eb951c5-8a59-492f-a849-47dc910857e8
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: SAPG with entropy coefficient of 0.005 is the best performing method.
- **Parent context**: ShadowHand results from table 1 have been replicated.

### R193: The average number of successes for PPO was 1.25 with a stan...
- **Rubric ID**: 28d1c0ab-4435-444e-a7fa-864198bff33b
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The average number of successes for PPO was 1.25 with a standard error of 1.15 after 2e10 samples.
- **Parent context**: Regrasping results from table 1 have been replicated.

### R194: The average number of successes for SAPG with entropy coeffi...
- **Rubric ID**: 23cc6a37-8f86-429d-a66b-cf9401bf65fb
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: The average number of successes for SAPG with entropy coefficient of 0.005 was 33.4 with a standard error of 2.25 after 2e10 samples.
- **Parent context**: Regrasping results from table 1 have been replicated.

### R195: Training without off-policy data is the worst performing met...
- **Rubric ID**: 74d49bbb-fc77-4f43-890a-eda9c810b440
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: Training without off-policy data is the worst performing method. All other methods perform a bit better, and standard SAPG is the best performing method.
- **Parent context**: The results for the Allegro Kuka Throw task have been replicated.

### R196: Training using symmetric off-policy data is the worst perfor...
- **Rubric ID**: 89ea072a-8a15-4529-b58c-8e0600bd9e88
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: Training using symmetric off-policy data is the worst performing method. All other methods improves the performance, and the best methods are standard SAPG and using entropy coefficient of 0.003 and 0.005.
- **Parent context**: The results for the Shadow Hand task have been replicated.

### R197: PCA has been computed for the visited states for SAPG and th...
- **Rubric ID**: 02bf6a17-192e-4bfc-b061-0abd6a68c992
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: PCA has been computed for the visited states for SAPG and the reconstruction errors calculated for components 1 to 66.
- **Parent context**: The Allegro Kuka Reorientation plot has been replicated.

### R198: The random policy has the smallest reconstruction error for...
- **Rubric ID**: d33b2f75-eb26-42ff-94a0-ff205dc5a38a
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The random policy has the smallest reconstruction error for most number of components, and SAPG has the highest reconstruction error for most number of components. All methods have similar reconstruction errors when using more than 25 components.
- **Parent context**: The Allegro Kuka Reorientation plot has been replicated.

### R199: PCA has been computed for the visited states for a random po...
- **Rubric ID**: e388762a-858d-42a7-b944-3101fefab2da
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: PCA has been computed for the visited states for a random policy and the reconstruction errors calculated for components 1 to 56.
- **Parent context**: The Allegro Kuka Regrasping plot has been replicated.

### R200: PCA has been computed for the visited states for SAPG and th...
- **Rubric ID**: 7651abd5-f7f2-45da-90a5-85ec88292ffb
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: PCA has been computed for the visited states for SAPG and the reconstruction errors calculated for components 1 to 56.
- **Parent context**: The Allegro Kuka Regrasping plot has been replicated.

### R201: PCA has been computed for the visited states for PPO and the...
- **Rubric ID**: a3abcee9-e2c0-443a-b6e5-6eca5ef44269
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: PCA has been computed for the visited states for PPO and the reconstruction errors calculated for components 1 to 56. 
- **Parent context**: The Allegro Kuka Throw plot has been replicated.

### R202: PCA has been computed for the visited states for a random po...
- **Rubric ID**: ec5c9d5e-7db3-40d0-acf1-e69e6f5dad53
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: PCA has been computed for the visited states for a random policy and the reconstruction errors calculated for components 1 to 56. 
- **Parent context**: The Allegro Kuka Throw plot has been replicated.

### R203: PCA has been computed for the visited states for SAPG and th...
- **Rubric ID**: aba141f8-03f6-4c04-b308-342b75516f7d
- **Category**: Code Execution / Logging, Analysis & Presentation
- **Weight**: 1
- **Requirement**: PCA has been computed for the visited states for SAPG and the reconstruction errors calculated for components 1 to 56. 
- **Parent context**: The Allegro Kuka Throw plot has been replicated.

### R204: The reconstruction error from PPO and SAPG is similar to eac...
- **Rubric ID**: 217424a8-1097-4bbf-8b18-2b1d765a48b3
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The reconstruction error from PPO and SAPG is similar to each other, while the error from the random policy is much smaller. The results indicate higher diversity of states visited in SAPG and PPO, than in a random policy.
- **Parent context**: Allegro Kuka Reorientation results have been replicated.

### R205: The reconstruction error from PPO and SAPG is similar to eac...
- **Rubric ID**: ac0d81a5-ef38-4141-800e-451505c7e54c
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The reconstruction error from PPO and SAPG is similar to each other, while the error from the random policy is much smaller. The results indicate higher diversity of states visited in SAPG and PPO, than in a random policy.
- **Parent context**: Allegro Kuka Regrasping results have been replicated.

### R206: The reconstruction error from PPO and SAPG is similar to eac...
- **Rubric ID**: d1050653-f0e1-4d50-85b9-fed1d65eb5e0
- **Category**: Result Analysis / Logging, Analysis & Presentation
- **Weight**: 2
- **Requirement**: The reconstruction error from PPO and SAPG is similar to each other, while the error from the random policy is much smaller. The results indicate higher diversity of states visited in SAPG and PPO, than in a random policy.
- **Parent context**: Allegro Kuka Throw results have been replicated.
