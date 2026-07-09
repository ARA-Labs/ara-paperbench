# Table 4: Efficiency Comparison When Training the Mask Network
- **Source**: Table 4, Appendix C.3
- **Caption**: "Efficiency comparison when training the mask network. We report the number of seconds when training the mask using a fixed number of samples. 'Selfish' represents Selfish Mining. 'Cage' represents Cage Challenge 2. 'Auto' represents Autonomous Driving. 'Malware' represents Malware Mutation."

| Method | Hopper | Walker2d | Reacher | HalfCheetah | Selfish | Cage | Auto | Malware |
|--------|--------|----------|---------|-------------|---------|------|------|---------|
| Num. of samples | 3×10^5 | 3×10^5 | 3×10^5 | 3×10^5 | 1.5×10^6 | 1×10^7 | 2443260 | 32349 |
| StateMask (seconds) | 15393 | 2240 | 8571 | 1579 | 9520 | 79382 | 109802 | 50775 |
| Ours (seconds) | 12426 | 1899 | 7033 | 1317 | 8360 | 65400 | 88761 | 41340 |

**Derived Statistic**: Average time reduction = 16.8% (computed across all 8 environments, reported in §4.3)

**Individual speedups:**
- Hopper: (15393-12426)/15393 = 19.3%
- Walker2d: (2240-1899)/2240 = 15.2%
- Reacher: (8571-7033)/8571 = 17.9%
- HalfCheetah: (1579-1317)/1579 = 16.6%
- Selfish Mining: (9520-8360)/9520 = 12.2%
- Cage Challenge 2: (79382-65400)/79382 = 17.6%
- Auto Driving: (109802-88761)/109802 = 19.2%
- Malware Mutation: (50775-41340)/50775 = 18.6%
