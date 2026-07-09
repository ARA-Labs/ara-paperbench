# Figure 5: NetHack Per-Level Evaluation (Level 4 and Sokoban)
- **Source**: Figure 5, Section 5
- **Caption**: "The average return throughout the fine-tuning process on two NetHack tasks: level 4 (top), and Sokoban level (bottom). The result is averaged over 200 episodes, each starting from where the expert (AutoAscend) ended up upon first entering level."
- **Axis labels**: X = training steps (×25M steps evaluation frequency); Y = average return (top: score increment from Level 4; bottom: Sokoban pits filled)
- **Conditions**: Human Monk; 200 AutoAscend game saves per level; evaluated every 25M steps; 5 seeds

## Level 4 Performance (approximate, read from Figure 5 top)

| Training Steps | Pre-trained π* | From Scratch | Vanilla FT | FT + EWC | FT + BC | FT + KS |
|----------------|---------------|-------------|-----------|---------|--------|--------|
| 0 | ≈500 | ≈0 | ≈500 | ≈500 | ≈500 | ≈500 |
| 25M | ≈500 | ≈200 | ≈300 | ≈600 | ≈500 | ≈700 |
| 100M | ≈500 | ≈400 | ≈200 | ≈700 | ≈600 | ≈1000 |
| 200M | ≈500 | ≈450 | ≈150 | ≈600 | ≈700 | ≈1200 |
| 300M | ≈500 | ≈480 | ≈150 | ≈500 | ≈800 | ≈1300 |
| 500M | ≈500 | ≈500 | ≈150 | ≈400 | ≈900 | ≈1400 |

## Sokoban Performance (approximate, read from Figure 5 bottom)

| Training Steps | Pre-trained π* | From Scratch | Vanilla FT | FT + EWC | FT + BC | FT + KS |
|----------------|---------------|-------------|-----------|---------|--------|--------|
| 0 | ≈0.5 | ≈0 | ≈0.5 | ≈0.5 | ≈0.5 | ≈0.5 |
| 50M | ≈0.5 | ≈0 | ≈0.1 | ≈0.2 | ≈0.5 | ≈0.2 |
| 100M | ≈0.5 | ≈0 | ≈0.1 | ≈0.1 | ≈0.5 | ≈0.1 |
| 200M | ≈0.5 | ≈0 | ≈0.1 | ≈0.05 | ≈0.5 | ≈0.1 |
| 500M | ≈0.5 | ≈0 | ≈0.1 | ≈0.05 | ≈0.5 | ≈0.1 |

**Key findings**:
- Level 4: KS and BC consistently improve above pre-trained baseline; vanilla FT and scratch fall below
- Sokoban: BC maintains performance equivalent to π*; KS struggles because Sokoban is deep in dungeon and not visited online early; EWC and vanilla FT forget Sokoban behavior
- Sokoban levels are an NP-hard puzzle branch; forgetting them hurts long-term game performance
