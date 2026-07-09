# Algorithm: SEMA Training Loop

## Mathematical Formulation

### Functional Adapter Output (Eq. 1)
$$f_{\phi_k^l}(\mathbf{x}^l) = \text{ReLU}(\mathbf{x}^l \cdot \mathbf{W}^l_{\text{down},k}) \cdot \mathbf{W}^l_{\text{up},k}$$
where $\mathbf{W}^l_{\text{down},k} \in \mathbb{R}^{d \times r}$, $\mathbf{W}^l_{\text{up},k} \in \mathbb{R}^{r \times d}$.

### Representation Descriptor Loss (Eq. 2)
$$\mathcal{L}^l_{\text{RD},k}(\mathbf{x}; \varphi_k^l) = \sum_{\mathbf{x} \in \mathcal{X}_k^l} \|\mathbf{x} - g_{\varphi_k^l}(\mathbf{x})\|_2^2$$

### Mixture Adapter Output (Eq. 3)
$$\mathbf{x}^l_{\text{out}} = \text{MLP}(\mathbf{x}^l) + \sum_{k=1}^{K^l} w_k^l \cdot f_{\phi_k^l}(\mathbf{x}^l)$$
$$\mathbf{w}^l = \text{softmax}(\mathbf{x}^l \cdot \mathbf{W}^l_{\text{mix}})$$

### Overall Objective (Eq. 4)
$$\min_{\{\phi_k^l\}, \{\psi^l\}, \{\varphi_k^l\}} \sum_{t=1}^T \mathbb{E}_{(x,y)\in D^t}\left[\mathcal{L}_{\text{CE}}(F_{\{\phi_k^l\},\{\psi^l\}}(x), y) + \sum_{l=1}^L \sum_{k=1}^{K^l} \mathcal{L}^l_{\text{RD},k}(x; \varphi_k^l)\right]$$

### Z-Score Expansion Signal
$$z_k^l = \frac{r_k^l - \mu_k^l}{\sigma_k^l}, \quad r_k^l = \|\mathbf{x}^l - g_{\varphi_k^l}(\mathbf{x}^l)\|_2^2$$
Expansion triggered at layer $l$ when $z_k^l > \tau \; \forall k = 1, \ldots, K^l$.

## Pseudocode

```python
# SEMA Training Algorithm
# Input: Task sequence (D_1, ..., D_T), PTM with L layers
# Hyperparameters: expansion_layers (default: {10, 11, 12}), threshold τ,
#                  adapter_lr=0.005, rd_lr=0.01, adapter_epochs=5, rd_epochs=20

# Initialize: for each layer l, add first adapter module on Task 1
for l in expansion_layers:
    adapters[l] = [FunctionalAdapter(d, r)]
    rds[l] = [RepresentationDescriptor(d, 128)]
    routers[l] = Router(d, K_l=1)

# Task 1: train first adapters (treat as always expanded)
train_adapters_and_rds(D_1, expansion_layers, epochs=adapter_epochs, rd_epochs=rd_epochs)
freeze_all_modules()

# Tasks 2..T: on-demand expansion
for t in range(2, T+1):
    expanded_any = False
    
    for l in sorted(expansion_layers):  # shallow to deep
        # Scanning phase (no gradient, no training)
        expansion_triggered = False
        with torch.no_grad():
            for batch in D_t:
                x_l = extract_features(batch, layer=l)  # through frozen ViT + existing adapters
                
                # Compute z-scores for all existing RDs at layer l
                z_scores = []
                for k, rd in enumerate(rds[l]):
                    recon_error = ||x_l - rd(x_l)||^2
                    z_k = (recon_error - mu[l][k]) / sigma[l][k]
                    z_scores.append(z_k)
                
                # Expansion signal: ALL z-scores exceed threshold
                if all(z > tau for z in z_scores):
                    expansion_triggered = True
                    break  # stop scanning once signal is found
        
        if expansion_triggered:
            # Add new modular adapter at layer l
            new_adapter = FunctionalAdapter(d, r)
            new_rd = RepresentationDescriptor(d, 128)
            adapters[l].append(new_adapter)  # K_l += 1
            rds[l].append(new_rd)
            
            # Expand router: add new column, freeze old columns
            routers[l].expand()  # adds one trainable column to W_mix
            
            # Train new adapter + RD + new router column
            unfreeze([new_adapter, new_rd, routers[l].new_column])
            for epoch in range(adapter_epochs):
                for batch in D_t:
                    loss_ce = cross_entropy(model(batch.x), batch.y)
                    loss_rd = reconstruction_loss(new_rd, batch.x, layer=l)
                    (loss_ce + loss_rd).backward()
                    optimizer_adapter.step()
            
            # Train RD separately for more epochs
            for epoch in range(rd_epochs):
                for batch in D_t:
                    loss_rd = reconstruction_loss(new_rd, batch.x, layer=l)
                    loss_rd.backward()
                    optimizer_rd.step()
            
            # Update running statistics buffer for new RD
            update_buffer(rds[l][-1], D_t, layer=l, buffer_size=500)
            
            freeze([new_adapter, new_rd])  # freeze after training
            expanded_any = True
    
    if not expanded_any:
        # No expansion: reuse existing adapters, no training for this task
        pass
    
    # Expand classification head for new classes
    expand_classifier(new_classes=D_t.classes)
```

## Step-by-Step Explanation

1. **Initialization (Task 1)**: Add one modular adapter to each eligible layer and train it on Task 1. Initialize running statistics buffers for each RD.

2. **Detection Phase (Tasks 2+)**: For each new task, iterate through eligible layers from shallow to deep. Pass batches through the frozen network and compute z-scores for each RD. Stop scanning when a signal is triggered.

3. **Expansion**: When triggered, instantiate a new functional adapter and RD; expand the router by one trainable column. Freeze all other parameters.

4. **Training**: Optimize the new adapter with $\mathcal{L}_{\text{CE}} + \mathcal{L}_{\text{RD}}$ for 5 epochs (adapters) and 20 epochs (RDs). The RD training is independent and can run in parallel.

5. **Freeze and Continue**: After training, freeze all new modules and scan the next eligible layer.

6. **No Expansion**: If no layer triggers expansion for a task, no training occurs and existing adapters are reused via the router.

## Complexity Analysis
- **Parameter overhead per expansion event**: $2 \cdot d \cdot r$ (functional adapter) + $2 \cdot d \cdot 128$ (RD AE, training only) + $d$ (new router column).
- **Inference overhead**: Only functional adapters and router active; RDs are training-time only.
- **Expansion rate**: Sub-linear w.r.t. number of tasks $T$ (bounded by number of genuinely distinct distributions).
