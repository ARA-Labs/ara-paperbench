# Figure 3: Toy Example — Three Scheduling Strategies
- **Source**: Figure 3, Section 2.3
- **Caption**: "Toy example showing three resource schedules across multiple CL jobs. Job demands and resource eligibility are shown in the top row. Devices check in at a constant rate. Eligible devices only for Emoji jobs are marked with blue; all devices are eligible for the Keyboard job."
- **Axis labels**: x-axis: Time (devices check-in over time); y-axis: Job assignment (Job 1, Job 2, Job 3)

## Setup
| Job | Training Data | # Devices Required |
|-----|--------------|-------------------|
| Job 1 (Keyboard) | Keyboard | 100% eligible devices |
| Job 2 (Emoji) | Emoji | 50% eligible devices |
| Job 3 (Emoji) | Emoji | 50% eligible devices |

## Average JCT Results

| Strategy | Average JCT |
|----------|-------------|
| Random Matching | 12 (time units) |
| SRSF (Shortest Remaining Service First) | 11 (time units) |
| Optimal | 9.3 (time units) |

**Key Finding**: Random Matching and SRSF inefficiently allocate scarce Emoji-eligible devices to Job 1 (Keyboard), which has ample alternatives. Optimal schedule reserves scarce Emoji devices for Jobs 2 and 3, achieving 23% lower avg JCT than random.
