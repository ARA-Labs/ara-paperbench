# Heuristics

## H01: Pre-train the critic head before full fine-tuning (NetHack)
- **Rationale**: The pre-trained model π* was trained with behavioral cloning (no critic). Starting APPO fine-tuning with a random critic head destabilizes training because the value function baseline is unreliable. Pre-training the critic head alone for 500M steps (with the rest of the model frozen) gives the critic a good initialization before the actor is updated.
- **Sensitivity**: high
- **Bounds**: 500M environment steps for NetHack; duration may need tuning for other environments
- **Code ref**: [src/execution/knowledge_retention.py]
- **Source**: Section B.1 (Pre-training subsection), Appendix B.1

## H02: Freeze encoders during NetHack fine-tuning
- **Rationale**: The visual and text encoders in the NetHack model have already learned good representations from behavioral cloning on 115B transitions. Allowing encoder gradients during fine-tuning risks destroying these representations. Freezing encoders also significantly reduces the number of trainable parameters, improving stability.
- **Sensitivity**: high
- **Bounds**: Applied throughout fine-tuning; unfreezing may be explored for very long training runs
- **Code ref**: [src/execution/knowledge_retention.py]
- **Source**: Section B.1 (Fine-tuning subsection)

## H03: Disable entropy maximization when using knowledge retention (NetHack)
- **Rationale**: Entropy maximization conflicts with the KL-divergence auxiliary loss used in BC and KS (which pushes the policy toward π*, not toward a high-entropy distribution). Keeping entropy enabled creates competing objectives that destabilize training.
- **Sensitivity**: medium
- **Bounds**: Only disable when using BC, KS, or EWC; vanilla fine-tuning keeps entropy_cost=0.001
- **Code ref**: [src/execution/knowledge_retention.py]
- **Source**: Section B.1 (Fine-tuning subsection); Baker et al. (2022)

## H04: Apply exponential decay to KS auxiliary loss coefficient
- **Rationale**: As training progresses, the fine-tuned policy improves and should be allowed to deviate more from π* to find better solutions. Decaying the KS coefficient prevents over-constraining the policy in the long run.
- **Sensitivity**: medium
- **Bounds**: Initial scale 0.5, decay rate 0.99998 per training step; decayed every train step in NetHack
- **Code ref**: [src/execution/knowledge_retention.py]
- **Source**: Section B.1 (Fine-tuning subsection)

## H05: Use no decay for BC auxiliary loss coefficient (NetHack)
- **Rationale**: BC uses a static buffer of expert data; the loss is always informative regardless of where the online policy is currently visiting. Decaying the BC coefficient would eventually lose the protection on FAR states (e.g., Sokoban levels rarely visited by the online policy). Keeping BC coefficient fixed ensures persistent retention.
- **Sensitivity**: medium
- **Bounds**: BC scale 2.0 for NetHack, no decay; other environments may benefit from tuning
- **Code ref**: [src/execution/knowledge_retention.py]
- **Source**: Section B.1 (Fine-tuning subsection)

## H06: Protect 10% of replay buffer as episodic memory (RoboticSequence)
- **Rationale**: Too little episodic memory reduces the retention effect; too much prevents the policy from learning the new downstream task efficiently. 10% (10K out of 100K samples) provides sufficient retention without dominating the training distribution.
- **Sensitivity**: medium
- **Bounds**: 100 samples (minimum viable, with higher initial performance drop) to 10K samples tested; larger buffer is always better but the gap vanishes at higher sample counts (Figure 26)
- **Code ref**: [src/execution/robotic_sequence.py]
- **Source**: Appendix F (Impact of memory size), Figure 26

## H07: Use separate output heads per stage with stage ID selection (RoboticSequence)
- **Rationale**: Adding the stage ID as an additional input to a shared network was found to work worse than creating separate output heads. Separate heads prevent interference between stage-specific action distributions while sharing the representation.
- **Sensitivity**: medium
- **Bounds**: One output head per stage (4 heads for 4-stage sequence); head selected by stage ID (one-hot encoded)
- **Code ref**: [src/execution/robotic_sequence.py]
- **Source**: Appendix B.3 (SAC subsection)

## H08: Apply layer normalization after first layer only (RoboticSequence MLP)
- **Rationale**: Layer normalization stabilizes training for SAC with continuous action spaces. Applying it only after the first layer (not all layers) was found to work better in the Continual World codebase (Wołczyk et al., 2021) which this work builds on.
- **Sensitivity**: low
- **Bounds**: Single LayerNorm after the first of 4 hidden layers; Leaky-ReLU activations throughout
- **Code ref**: [src/execution/robotic_sequence.py]
- **Source**: Appendix B.3 (SAC subsection)
