# Table 2: Action Set of the MalConv Gym Environment
- **Source**: Table 2, Appendix C.2
- **Caption**: "Action set of the MalConv gym environment."
- **Conditions**: 16 possible mutation actions for PE malware files; reward of 10 for successful evasion; maximum 10 steps per episode.

| Action Index | Action Meaning |
|-------------|----------------|
| 0 | "modify machine type" |
| 1 | "pad overlay" |
| 2 | "append benign data overlay" |
| 3 | "append benign binary overlay" |
| 4 | "add bytes to section cave" |
| 5 | "add section strings" |
| 6 | "add section benign data" |
| 7 | "add strings to overlay" |
| 8 | "add imports" |
| 9 | "rename section" |
| 10 | "remove debug" |
| 11 | "modify optional header" |
| 12 | "modify timestamp" |
| 13 | "break optional header checksum" |
| 14 | "upx unpack" |
| 15 | "upx pack" |
