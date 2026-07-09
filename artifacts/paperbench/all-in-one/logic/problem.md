---
# Problem Specification

## Observations

### O1: Current SBI methods require structured tabular data
- **Statement**: Existing amortized SBI methods operate on fixed-size (θ, x) vector pairs and cannot natively handle irregularly sampled time series, missing values, or observations at variable numbers of time points.
- **Evidence**: Section 1 of the paper; real-world datasets in ecology, climate science, and health sciences naturally produce irregularly sampled time series (citing Shukla & Marlin, 2021).
- **Implication**: Methods like NPE/NLE/NRE are inapplicable to large classes of scientific data without ad-hoc preprocessing or summary statistics.

### O2: Simulators may have function-valued (∞-dimensional) parameters
- **Statement**: Many scientific simulators have parameters that depend on time or space (e.g., time-varying contact rate in epidemiology), making the parameter space infinite-dimensional. Existing amortized methods require discretization to a fixed grid.
- **Evidence**: Section 1; SIRD model example (Section 4.3) where contact rate β(t) is a function of time.
- **Implication**: Existing methods cannot evaluate posteriors at arbitrary time points or handle continuous parameter functions.

### O3: Amortized SBI methods are locked to a single inference task
- **Statement**: Neural network-based SBI methods must commit to either the posterior (NPE) or the likelihood (NLE) at training time; they cannot flexibly switch between inference tasks or estimate arbitrary conditionals post-hoc.
- **Evidence**: Section 1; users "might want to interactively explore both conditional distributions, investigate posteriors conditioned on subsets of data and parameters, or even explore different prior configurations."
- **Implication**: Separate networks must be trained for each inference task, increasing cost and reducing flexibility.

### O4: Existing methods do not exploit known simulator dependency structure
- **Statement**: Standard SBI methods treat the simulator as a black box and cannot incorporate known conditional independence structures, leading to higher simulation requirements.
- **Evidence**: Section 1; "in practice, one has at least partial knowledge (or assumptions) about the structure of the simulator (i.e., its conditional independencies), but common SBI methods cannot exploit such knowledge."
- **Implication**: Methods are less simulation-efficient than they could be given available domain knowledge.

### O5: Sharp performance threshold at 50 reverse SDE evaluation steps
- **Statement**: Simformer performance (C2ST) shows a sharp transition from suboptimal to near-perfect quality when the number of reverse SDE evaluation steps exceeds approximately 50, rather than gradual improvement.
- **Evidence**: Figure A7, Appendix A3.1; "there is a sharp transition from suboptimal to near-perfect performance when the number of evaluations exceeds 50."
- **Implication**: 50 steps is a sufficient budget for inference, making Simformer competitive with faster normalizing flow methods in practice.

## Gaps

### G1: No amortized method jointly models the full joint distribution
- **Statement**: No existing amortized SBI method trains a model on p(θ, x) that can then sample any conditional, including posterior, likelihood, and arbitrary parameter/data conditionals.
- **Caused by**: O3
- **Existing attempts**: NPE targets p(θ|x); NLE targets p(x|θ); JANA (Radev et al., 2023) and Glöckler et al. (2022) train separate networks.
- **Why they fail**: Each network is specialized and cannot answer queries outside its training objective.

### G2: No method handles both finite and infinite-dimensional parameter spaces
- **Statement**: Existing methods either use discrete grids (GATSBI, Chen et al.) for function-valued parameters, limiting evaluation to the training grid, or ignore function-valued parameters entirely.
- **Caused by**: O2
- **Existing attempts**: Chen et al. (2020), Ramesh et al. (2022), Moss et al. (2023) estimated posteriors over function-valued parameters but relied on predefined discretizations.
- **Why they fail**: Fixed-grid discretization precludes evaluation at arbitrary time/space points.

### G3: Missing and unstructured data not handled
- **Statement**: Standard amortized SBI assumes fixed-size, complete observation vectors; missing or variably observed data requires ad-hoc imputation or specialized architectures.
- **Caused by**: O1
- **Existing attempts**: Wang et al. (2023) proposed data augmentation + RNNs for missing data; Dyer et al. (2021) used ABC with path signatures for irregular time series.
- **Why they fail**: Approaches are task-specific and not amortized across observation structures.

### G4: Simulator structure cannot be exploited by standard methods
- **Statement**: Common SBI methods apply the same dense computational graph regardless of known conditional independencies in the simulator.
- **Caused by**: O4
- **Existing attempts**: Weilbach et al. (2023) proposed graphically structured diffusion models for general graphical models; not previously applied to SBI amortization across all conditionals.
- **Why they fail**: Attention mechanisms were not used to encode simulator structure within the SBI amortization framework.

## Key Insight

- **Insight**: By representing every variable (parameter and data) as a token with an identity embedding, a value embedding, and a learnable condition-state embedding, and training a diffusion score model on the joint distribution p(θ, x) with randomly sampled condition masks, a single model learns to estimate the score of any conditional of the joint distribution. The attention mask of the transformer can simultaneously encode known dependency structure of the simulator.
- **Derived from**: O1, O2, O3, O4; combining transformer attention masking (Weilbach et al., 2023) with the all-conditionals training objective.
- **Enables**: A single trained network that can (1) estimate any conditional of p(θ, x), (2) exploit simulator structure for efficiency, (3) handle variable-length and missing observations, (4) handle function-valued parameters via Fourier embeddings, and (5) condition on intervals via guided diffusion.

## Assumptions

- A1: The simulator provides samples from p(θ, x) without requiring likelihood evaluations (black-box simulator).
- A2: The diffusion SDE (VESDE or VPSDE) does not introduce correlations that invalidate the graphical model structure at t=0 (valid for VESDE and VPSDE).
- A3: Sufficient simulation budget is available for training (experiments use 10³–10⁵ simulations).
- A4: The transformer has enough layers to propagate information along the dependency graph (for undirected graphs; directed graphs may need dynamic mask updates per Webb et al., 2018).
- A5: The score model approximation is accurate enough that guided diffusion with sigmoid-based constraint functions produces well-calibrated samples within specified intervals.
