# Table 2: Capability Comparison Matrix
- **Source**: Table 2, Section 5.2
- **Caption**: "FRE unifies prior methods in capabilities. OPAL does not have zero-shot capabilities and learns via BC rather than Q-learning. GCRL and SF both limit reward function families to goal-reaching or linear functions, respectively. FB can learn to solve any reward function, but requires a linearized value function."

| Capability | FRE | GCRL | SF | FB | OPAL |
|-----------|-----|------|----|----|------|
| Zero-Shot | ✓ | ✓ | ✓ | ✓ | ✗ |
| Any Reward Function | ✓ | ✗ | ✗ | ✓ | ✗ |
| No Linear Constraint | ✓ | ✓ | ✗ | ✗ | ✓ |
| Learns Optimal Policies | ✓ | ✓ | ✓ | ✓ | ✗ |
