# Key Concepts

## Refined Coreset Selection (RCS)
- **Notation**: $\text{RCS}(\mathcal{D}, \epsilon)$
- **Definition**: Given a dataset $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^n$, RCS seeks a binary mask $\mathbf{m} \in \{0,1\}^n$ that satisfies two objectives in lexicographic priority order: (O1) the model trained on the coreset performs comparably to full-data training; (O2) the coreset size $\|\mathbf{m}\|_0$ is minimized subject to (O1).
- **Boundary conditions**: Applies when no fixed coreset size is specified in advance; requires that a meaningful performance threshold is achievable with a strict subset.
- **Related concepts**: Lexicographic Preference, Bilevel Optimization, Coreset Mask

## Coreset Mask
- **Notation**: $\mathbf{m} \in \{0,1\}^n$, where $m_i = 1$ means sample $i$ is selected
- **Definition**: A binary vector indicating which data points are included in the coreset. The selected coreset is $\{(x_i, y_i) : m_i = 1\}$. The coreset size is $f_2(\mathbf{m}) = \|\mathbf{m}\|_0$.
- **Boundary conditions**: Discrete domain; not amenable to gradient-based optimization directly. Probabilistic relaxation (Bernoulli reparameterization) is used by Zhou et al. (2022) but not by LBCS.
- **Related concepts**: Refined Coreset Selection (RCS), Bilevel Optimization

## Bilevel Optimization for Coreset Selection
- **Notation**: $\min_{\mathbf{m}} f_1(\mathbf{m})$ s.t. $\theta(\mathbf{m}) \in \arg\min_\theta L(\mathbf{m},\theta)$
- **Definition**: A two-level optimization where the outer loop selects the coreset mask $\mathbf{m}$ to minimize validation loss $f_1(\mathbf{m}) = \frac{1}{n}\sum_{i=1}^n \ell(h(x_i;\theta(\mathbf{m})),y_i)$, and the inner loop trains model parameters $\theta(\mathbf{m})$ on the selected coreset loss $L(\mathbf{m},\theta) = \sum_{i=1}^n m_i \ell(h(x_i;\theta),y_i)$.
- **Boundary conditions**: Assumes inner-loop convergence is achievable; the outer objective evaluates on the full dataset (or a validation proxy).
- **Related concepts**: Coreset Mask, Lexicographic Preference, Inner Loop

## Lexicographic Preference
- **Notation**: $\vec{\min}_{\mathbf{m} \in \mathcal{M}} \mathbf{F}(\mathbf{m})$, where $\mathbf{F}(\mathbf{m}) = [f_1(\mathbf{m}), f_2(\mathbf{m})]$
- **Definition**: An ordering over objective vectors where $\mathbf{F}(\mathbf{m}) \vec{\prec} \mathbf{F}(\mathbf{m}')$ iff there exists $i \in [2]$ such that $f_i(\mathbf{m}) < f_i(\mathbf{m}')$ and $f_{i'}(\mathbf{m}) = f_{i'}(\mathbf{m}')$ for all $i' < i$. The first objective $f_1$ has absolute priority; $f_2$ is only minimized after $f_1$ reaches its optimal region $\mathcal{M}^*_1 = \{\mathbf{m} : f_1(\mathbf{m}) \leq f^*_1 \cdot (1+\epsilon)\}$.
- **Boundary conditions**: Cannot be represented by any weighted combination of objectives (Shi et al. 2020); reflexive and transitive relation.
- **Related concepts**: Refined Coreset Selection (RCS), Voluntary Performance Compromise (ε), LexiFlow

## Voluntary Performance Compromise (ε)
- **Notation**: $\epsilon \geq 0$
- **Definition**: A user-specified fraction relaxing the primary objective. The feasible region for $f_1$ is $\mathcal{M}^*_1 = \{\mathbf{m} : f_1(\mathbf{m}) \leq f^*_1 \cdot (1+\epsilon)\}$, where $f^*_1 = \inf_{\mathbf{m} \in \mathcal{M}} f_1(\mathbf{m})$. Larger $\epsilon$ allows smaller coresets at the cost of potentially higher training loss.
- **Boundary conditions**: $\epsilon = 0$ implies exact optimum of $f_1$ must be achieved before minimizing $f_2$. In practice $\epsilon = 0.2$ is used. Remark 2 notes that larger $\epsilon$ can reduce overfitting under noisy labels.
- **Related concepts**: Lexicographic Preference, ε-Convergence, Refined Coreset Selection (RCS)

## LexiFlow (Black-box Lexicographic Optimizer)
- **Notation**: Algorithm 2 in paper; adapted from Zhang et al. (2023b)
- **Definition**: A randomized direct search algorithm that maintains an incumbent mask $\mathbf{m}^*$ and iteratively samples candidate masks by perturbing along random unit-sphere directions. Candidates are accepted if they lexicographically dominate the incumbent (using practical lexicographic relations $\vec{\prec}_{(\mathbf{F}_H)}$). Includes dynamic step-size adjustment and random restarts to avoid local optima.
- **Boundary conditions**: Requires only pairwise comparisons between mask evaluations; no analytic gradients needed. Convergence requires Conditions 1 and 2 to hold.
- **Related concepts**: Lexicographic Preference, Bilevel Optimization for Coreset Selection

## ε-Convergence
- **Notation**: $P_{t\to\infty}[f_2(\mathbf{m}_t) \leq f^*_2] = 1$
- **Definition**: Under Conditions 1 (Progressable) and 2 (Stable Moving), LBCS converges with probability 1 to the minimum coreset size $f^*_2 = \min_{\mathbf{m} \in \mathcal{M}} \{f_2(\mathbf{m}) : f_1(\mathbf{m}) \leq f^*_1 (1+\epsilon)\}$. The proof proceeds in two stages: first $f_1$ enters $\mathcal{M}^*_1$ (probability→1 as $t\to\infty$), then $f_2$ converges to $f^*_2$ within $\mathcal{M}^*_1$.
- **Boundary conditions**: Requires Conditions 1 and 2 as sufficient (not necessary) conditions. The optimal convergence rate is not characterized (stated as a limitation).
- **Related concepts**: Lexicographic Preference, Voluntary Performance Compromise (ε), LexiFlow

## Progressable Condition (Condition 1)
- **Notation**: At any step $t \geq 0$: if $\mathbf{m}_t \notin \mathcal{M}^*_1$ then $f_1(\mathbf{m}_{t+1}) < f_1(\mathbf{m}_t)$; if $\mathbf{m}_t \in \mathcal{M}^*_1$ then $f_2(\mathbf{m}_{t+1}) < f_2(\mathbf{m}_t)$ and $\mathbf{m}_{t+1} \in \mathcal{M}^*_1$.
- **Definition**: The algorithm only updates the incumbent mask when the new mask strictly improves the active objective (f1 if not in optimal region, f2 if in optimal region). This holds by construction of the lexicographic update rule in Algorithm 2.
- **Boundary conditions**: Holds at all time steps for LBCS by the design of the lexicographic comparison function.
- **Related concepts**: ε-Convergence, Stable Moving Condition (Condition 2)

## Stable Moving Condition (Condition 2)
- **Notation**: $\psi_{t+1}[f_1(\mathbf{m}_t) - f_1(\mathbf{m}_{t+1}) > \gamma_1 \text{ or } \mathbf{m}_t \in \mathcal{M}^*_1] \geq \eta_1$ (and analogous for $f_2$)
- **Definition**: At each step, there is a lower-bounded probability $\eta_1 > 0$ that the algorithm makes a progress of at least $\gamma_1 > 0$ on the active objective. This is a standard assumption for local randomized search algorithms (Dolan et al. 2003, Solis & Wets 1981).
- **Boundary conditions**: Applies to both $f_1$ and $f_2$ in their respective optimization stages. Imposes an improvement lower bound ensuring stable progress.
- **Related concepts**: ε-Convergence, Progressable Condition (Condition 1)

## Practical Lexicographic Relations
- **Notation**: $\vec{=}_{(\mathbf{F}_H)}, \vec{\prec}_{(\mathbf{F}_H)}, \vec{\preceq}_{(\mathbf{F}_H)}$
- **Definition**: Approximations of the theoretical lexicographic relations using the running minimum values $\tilde{f}^*_i$ computed from the history set $H$. Two masks are considered equivalent on objective $i$ if both values are below the running threshold $\tilde{f}^*_i = \hat{f}^*_1 \cdot (1+\epsilon)$ (for $i=1$) or $\tilde{f}^*_2 = \hat{f}^*_2$ (for $i=2$). These enable tractable comparisons without knowing the true infimum.
- **Boundary conditions**: Used in Algorithm 2; converges to theoretical relations as the algorithm explores more masks.
- **Related concepts**: LexiFlow (Black-box Lexicographic Optimizer), Voluntary Performance Compromise (ε)
