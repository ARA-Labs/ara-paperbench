import time

script_start_time = time.time()
import torch
import numpy as np
import os
from tqdm import tqdm
import math
import torch.nn as nn
import torch.nn.functional as F
from restricted_model import FeedForwardMLM, BiasOnlyMLM, MLPMixer, ConvMLM, ConvMLMWithBiBigrams

device = "cuda:6"
device_type = device.split(":")[0]
batch_size = 16
sequence_length = 128
vocab_size = 50257
# vocab_size = 50304
num_steps = 100_000
lr = 3e-4
mask_prob = 0.15
mask_token_id = 50256

num_layers = 6
hidden_dim = 512
hidden_expansion = 32
expansion_factor = 2
save = False

kernel_size = 7
assert kernel_size % 2 == 1

save_file_name = "model.pt"

run_name = "convbigramslearnedmul2"

wandb_log = True
if wandb_log:
    os.environ["WANDB_SILENT"] = "true"
    import wandb

    wandb.init(project="restricted_mlm", name=run_name)

dataset = "openwebtext"

# All of torch is allowed outside forward pass / outside of inference, get_batch doesn't need to follow restrictions
data_dir = os.path.join("data/data", dataset)


def get_batch(split):
    # We recreate np.memmap every batch to avoid a memory leak, as per
    # https://stackoverflow.com/questions/45132940/numpy-memmap-memory-usage-want-to-iterate-once/61472122#61472122
    stime = time.time()
    if split == "train":
        data = np.memmap(os.path.join(data_dir, "train.bin"), dtype=np.uint16, mode="r")
    else:
        data = np.memmap(os.path.join(data_dir, "val.bin"), dtype=np.uint16, mode="r")
    ix = torch.randint(len(data) - sequence_length, (batch_size,))
    raw_tokens = torch.stack(
        [torch.from_numpy((data[i : i + sequence_length]).astype(np.int64)) for i in ix]
    ).to(device)
    # mask x
    mask = torch.rand(raw_tokens.shape, device=device) < mask_prob
    x = torch.where(mask, mask_token_id, raw_tokens)
    mask_nonzero_indices = torch.nonzero(mask.view(-1), as_tuple=True)[0]
    y = raw_tokens.flatten()[mask_nonzero_indices]  # y is flattened, only includes masked tokens
    # print(f'get_batch took {time.time() - stime} seconds')
    return x, y, mask_nonzero_indices


print("initializing model")
# model = BiasOnlyMLM(vocab_size).to(device)
model = ConvMLMWithBiBigrams(
    vocab_size, kernel_size, hidden_dim, num_layers, expansion_factor, mask_token_id
).to(device)

print("creating optimizer")
optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

train_start_time = time.time()
print(f"setup took {train_start_time - script_start_time} seconds")
print("training")
pbar = tqdm(range(num_steps))
with torch.amp.autocast(device_type=device_type, dtype=torch.bfloat16):
    for i in pbar:
        X, Y, masked_indices = get_batch("train")
        logits, scales = model(X)
        loss = torch.nn.functional.cross_entropy(
            logits.view(-1, vocab_size)[masked_indices], Y.view(-1)
        )
        loss.backward()
        # if loss is nan abort
        if torch.isnan(loss):
            print("loss is nan, aborting")
            break
        grad_scales = {}
        for n, p in model.named_parameters():
            if p.grad is not None:
                grad_scales[n] = p.grad.std().item()
        if wandb_log:
            wandb.log(
                {
                    "loss": loss.item(),
                    **scales,
                    **grad_scales,
                    "lr": optimizer.param_groups[0]["lr"],
                }
            )
        pbar.set_description(f"loss: {loss.item()}")
        if i % 100 == 0:
            print("SCALES")
            print(scales)
            print("GRAD SCALES")
            print(grad_scales)

        if i % 2000 == 0 and save:
            # save model
            torch.save(model.state_dict(), save_file_name)
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        optimizer.zero_grad()

        model.update_inverse_stds()

        optimizer.param_groups[0]["lr"] = (
            lr * min(1, i / 100) * math.cos(i / num_steps * math.pi / 4)
        )
print(f"training took {time.time() - train_start_time} seconds")
