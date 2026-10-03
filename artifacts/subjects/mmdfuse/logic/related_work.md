# Related-work graph

These edges describe how the source paper uses prior work, not independent reviews of those papers. Exact printed citations are retained in [source_bibliography.txt](../evidence/source_bibliography.txt). The bibliography is the complete citation footprint; the blocks below identify the works with specific technical roles.

## RW01: Gretton et al. (2012a): A kernel two-sample test
- **DOI**: 10.5555/2503308.2188410
- **Type**: imports
- **Delta**: The unbiased MMD discrepancy supplies the base kernel test.
- **Claims affected**: C01, C02
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 148–151; exact printed metadata, not independently corrected

## RW02: Sriperumbudur et al. (2011): Universality, characteristic kernels and RKHS embedding of measures
- **DOI**: Not specified in the printed citation
- **Type**: bounds
- **Delta**: Characteristic-kernel conditions delimit distribution identification.
- **Claims affected**: C01
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 357–359; exact printed metadata, not independently corrected

## RW03: Hemerik and Goeman (2018): Exact testing with random permutations
- **DOI**: 10.1007/s11749-017-0571-1
- **Type**: imports
- **Delta**: Exact random-permutation testing supplies calibration context.
- **Claims affected**: C01
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 192–194; exact printed metadata, not independently corrected

## RW04: Donsker and Varadhan (1975): Asymptotic evaluation of certain Markov process expectations for large time, I
- **DOI**: 10.1002/cpa.3160280102
- **Type**: imports
- **Delta**: Variational duality motivates divergence-regularized kernel weighting.
- **Claims affected**: C02
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 96–99; exact printed metadata, not independently corrected

## RW05: Kim et al. (2022): Minimax optimality of permutation tests
- **DOI**: 10.1214/21-AOS2103
- **Type**: imports
- **Delta**: Permutation optimality, coupling and variance analysis feed the power arguments.
- **Claims affected**: C04
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 202–206; exact printed metadata, not independently corrected

## RW06: Rudelson and Vershynin (2013): Hanson-Wright inequality and sub-Gaussian concentration
- **DOI**: 10.1214/ECP.v18-2865
- **Type**: imports
- **Delta**: The paper adapts a chaos bound with explicit constants.
- **Claims affected**: C04
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 323–325; exact printed metadata, not independently corrected

## RW07: Dvoretzky et al. (1956): Asymptotic Minimax Character of the Sample Distribution Function and of the Classical Multinomial Estimator
- **DOI**: 10.1214/aoms/1177728174
- **Type**: imports
- **Delta**: Empirical-CDF control supports the permutation reduction.
- **Claims affected**: C04
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 100–103; exact printed metadata, not independently corrected

## RW08: Massart (1990): The Tight Constant in the Dvoretzky-Kiefer-Wolfowitz Inequality
- **DOI**: 10.1214/aop/1176990746
- **Type**: bounds
- **Delta**: The cited tight-constant result sharpens the empirical-CDF tool.
- **Claims affected**: C04
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 289–291; exact printed metadata, not independently corrected

## RW09: Schrab et al. (2023): MMD aggregated two-sample test
- **DOI**: http://jmlr.org/papers/v24/21-1289.html
- **Type**: extends
- **Delta**: Multiple-test aggregation is the main structural and empirical comparison.
- **Claims affected**: C05, C06, C08, C09
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 335–338; exact printed metadata, not independently corrected

## RW10: Schrab et al. (2022b): Efficient aggregated kernel tests using incomplete U-statistics
- **DOI**: Not specified in the printed citation
- **Type**: baseline
- **Delta**: Incomplete statistics provide a different computation/power tradeoff.
- **Claims affected**: C06, C08
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 330–334; exact printed metadata, not independently corrected

## RW11: Jitkrittum et al. (2016): Interpretable distribution features with maximum testing power
- **DOI**: Not specified in the printed citation
- **Type**: baseline
- **Delta**: Learned interpretable features contextualize split-data selection.
- **Claims affected**: C07, C08
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 197–199; exact printed metadata, not independently corrected

## RW12: Sutherland et al. (2017): Generative models and model criticism via optimized maximum mean discrepancy
- **DOI**: Not specified in the printed citation
- **Type**: baseline
- **Delta**: Optimized kernel selection provides a data-splitting comparison.
- **Claims affected**: C07, C08
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 360–363; exact printed metadata, not independently corrected

## RW13: Gretton et al. (2012b): Optimal kernel choice for large-scale two-sample tests
- **DOI**: Not specified in the printed citation
- **Type**: baseline
- **Delta**: Prior kernel selection work motivates the sample-use tradeoff.
- **Claims affected**: C07
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 152–155; exact printed metadata, not independently corrected

## RW14: Liu et al. (2020): Learning deep kernels for non-parametric two-sample tests
- **DOI**: Not specified in the printed citation
- **Type**: baseline
- **Delta**: Deep-kernel image tests and the attributed CIFAR illustration provide context.
- **Claims affected**: C08, C10
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 264–266; exact printed metadata, not independently corrected

## RW15: Kübler et al. (2022b): AutoML two-sample test
- **DOI**: Not specified in the printed citation
- **Type**: baseline
- **Delta**: AutoML is compared with its source-specific training settings.
- **Claims affected**: C08
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 220–223; exact printed metadata, not independently corrected

## RW16: Domingo-Enrich et al. (2023): Compress then test: Powerful kernel testing in near-linear time
- **DOI**: Not specified in the printed citation
- **Type**: baseline
- **Delta**: Compression/thinning tests provide another computational tradeoff.
- **Claims affected**: C06, C08
- **Adopted elements**: the source-attributed elements above
- **Source citation**: source_bibliography.txt lines 93–95; exact printed metadata, not independently corrected

## Remaining citation footprint

The complete source bibliography also retains background, concentration texts, representation-learning work, data citations and proposed extensions. The source’s Recht citation/title mismatch remains explicitly unresolved; no title or source is silently replaced from memory.
