# Table 1

**Source**: Table 1, paper page 9.

**Caption**: Reported rejection rates for the CIFAR image comparison (paraphrase; original caption remains in the PDF).

**Screenshot**: [table1.png](table1.png)

**Extraction type**: raw_table

| Test | Paper-reported power |
| --- | --- |
| MMD-FUSE | 0.937 |
| MMDAgg | 0.883 |
| MMD-D | 0.744 |
| CTT | 0.711 |
| MMD-Median | 0.678 |
| ACTT | 0.652 |
| ME | 0.588 |
| AutoML | 0.544 |
| C2ST-L | 0.529 |
| C2ST-S | 0.452 |
| MMD-O | 0.316 |
| MMDAggInc | 0.281 |
| SCF | 0.171 |

All printed rows are retained. The paper states an average over 1000 repetitions at level 0.05. The released arrays contain more detailed floating values, including 0.9366196990013123 for MMD-FUSE. The newly inspected generator declares K=10 and N=100, but no raw original outcome vector is available; those source facts do not verify the exact stated rejection count. See [source conflicts](../source_conflicts.md). MMD-O and this repository's MMD-Split are different baselines, not conflicting labels for one measurement.
