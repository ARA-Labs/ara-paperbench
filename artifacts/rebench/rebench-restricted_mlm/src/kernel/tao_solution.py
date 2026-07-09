import torch
import torch.nn as nn
import torch.nn.functional as F


class BiasOnlyMLM(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.vocab_size = vocab_size

        self.output_bias = nn.Parameter(torch.zeros(vocab_size))

    def forward(self, token_indices: torch.Tensor) -> torch.Tensor:
        return self.output_bias[None, None, :].expand(
            token_indices.size(0), token_indices.size(1), self.vocab_size
        )


class UnigramMLM(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.vocab_size = vocab_size

        probabilities = torch.load("unigrams.pt")
        self.logits = nn.Parameter(torch.log(probabilities / (1 - probabilities)))

    def forward(self, token_indices: torch.Tensor) -> torch.Tensor:
        return self.logits[None, None, :].expand(
            token_indices.size(0), token_indices.size(1), self.vocab_size
        )


class BiBigramMLMCheating(nn.Module):
    def __init__(self, vocab_size, mask_token):
        super().__init__()
        self.bigrams_forward = nn.Parameter(torch.load("bigrams_forward.pt", map_location="cpu"))
        self.bigrams_backward = nn.Parameter(torch.load("bigrams_backward.pt", map_location="cpu"))
        self.unigrams = nn.Parameter(torch.load("unigrams.pt", map_location="cpu"))
        self.bigrams_backward.data[mask_token] = self.unigrams.data
        self.bigrams_forward.data[mask_token] = self.unigrams.data

    def forward(self, token_indices: torch.Tensor) -> torch.Tensor:
        forward_probs = self.bigrams_forward[token_indices.roll(1, dims=1)]
        backward_probs = self.bigrams_backward[token_indices.roll(-1, dims=1)]
        prob_average = (forward_probs + backward_probs) / 2
        return torch.log(prob_average / (1 - prob_average))


class BiBigramMLM(nn.Module):
    def __init__(self, vocab_size, mask_token):
        super().__init__()
        unigrams = torch.load("unigrams.pt", map_location="cpu")
        bigrams_forward_probs = torch.load("bigrams_forward.pt", map_location="cpu")
        bigrams_forward_probs[mask_token] = unigrams
        self.register_buffer(
            "bigrams_forward_logits", torch.log(bigrams_forward_probs / (1 - bigrams_forward_probs))
        )
        bigrams_backward_probs = torch.load("bigrams_backward.pt", map_location="cpu")
        bigrams_backward_probs[mask_token] = unigrams
        self.register_buffer(
            "bigrams_backward_logits",
            torch.log(bigrams_backward_probs / (1 - bigrams_backward_probs)),
        )

    def forward(self, token_indices: torch.Tensor) -> torch.Tensor:
        forward_logits = self.bigrams_forward_logits[token_indices.roll(1, dims=1)]
        backward_logits = self.bigrams_backward_logits[token_indices.roll(-1, dims=1)]
        # want to compute log((exp(forward_logits)+exp(backward_logits))/2)
        return (forward_logits + backward_logits) * 0.5


def index_embeddings(embeddings, indices):
    return torch.gather(
        embeddings.unsqueeze(0).expand(indices.size(0), embeddings.size(0), embeddings.size(1)),
        1,
        indices.unsqueeze(-1).expand(indices.size(0), indices.size(1), embeddings.size(1)),
    )


class FeedForwardMLM(nn.Module):
    def __init__(self, vocab_size, sequence_length, hidden_expansion, num_layers):
        super().__init__()
        self.vocab_size = vocab_size
        self.hidden_expansion = hidden_expansion
        hidden_dim = sequence_length * hidden_expansion
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers

        # Embedding weights
        self.embed_weights = nn.Parameter(torch.randn(vocab_size, hidden_expansion))

        # Hidden layer weights and biases
        scale_factor = 1 / (hidden_dim**0.5)  # division allowed bc not forward pass
        self.hidden_weights = nn.Parameter(
            torch.randn(num_layers, hidden_dim, hidden_dim) * scale_factor
        )

        # Output layer weights and bias
        self.output_weights = nn.Parameter(
            torch.randn(vocab_size, hidden_expansion) * vocab_size**-0.5
        )
        self.output_bias = nn.Parameter(torch.zeros(vocab_size))

    def forward(self, token_indices: torch.Tensor) -> torch.Tensor:
        b, s = token_indices.shape
        # Embedding layer
        x = index_embeddings(self.embed_weights, token_indices).reshape(b, self.hidden_dim)
        # Hidden layers
        for i in range(self.num_layers):
            x = torch.einsum("bh,vh->bv", x, self.hidden_weights[i])
            x = torch.nn.functional.relu(x)

        # Output layer
        logits = (
            torch.einsum("bsh,vh->bsv", x.reshape(b, s, self.hidden_expansion), self.output_weights)
            + self.output_bias
        )

        return logits


class MLPMixer(nn.Module):
    def __init__(self, vocab_size, sequence_length, hidden_dim, num_layers, expansion_factor):
        super().__init__()
        self.vocab_size = vocab_size
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        self.expansion_factor = expansion_factor

        # Embedding weights
        self.embed_weights = nn.Parameter(torch.randn(vocab_size, hidden_dim) * 0.01)

        # Hidden layer weights and biases
        scale_factor = hidden_dim**-0.5  # allowed bc not forward pass
        self.per_token_up_weights = nn.Parameter(
            torch.randn(num_layers, hidden_dim * expansion_factor, hidden_dim) * scale_factor
        )
        self.per_token_down_weights = nn.Parameter(
            torch.randn(num_layers, hidden_dim, hidden_dim * expansion_factor)
            * scale_factor
            * expansion_factor**-0.5
        )

        scale_factor_sequence = sequence_length**-0.5
        self.cross_token_up_weights = nn.Parameter(
            torch.randn(num_layers, sequence_length * expansion_factor, sequence_length)
            * scale_factor_sequence
        )
        self.cross_token_down_weights = nn.Parameter(
            torch.randn(num_layers, sequence_length, sequence_length * expansion_factor)
            * scale_factor_sequence
            * expansion_factor**-0.5
        )

        self.register_buffer("inverse_stds", torch.ones(num_layers))

        # Output layer weights and bias
        self.output_weights = nn.Parameter(torch.randn(vocab_size, hidden_dim) * vocab_size**-0.5)
        self.output_bias = nn.Parameter(torch.zeros(vocab_size))

    def forward(self, token_indices: torch.Tensor) -> torch.Tensor:
        b, s = token_indices.shape
        # Embedding layer
        x = (
            index_embeddings(self.embed_weights, token_indices) * 100
        )  # increase gradient towards embeddings
        # Hidden layers
        scales = {"residual": [], "cross_token": [], "per_token": []}
        for i in range(self.num_layers):
            # print("layer", i, "shape", x.shape)
            scales["residual"].append(x.std().item())

            token_expanded = torch.einsum(
                "bsh,zs->bzh", x * self.inverse_stds[i], self.cross_token_up_weights[i]
            )
            scales["cross_token"].append(token_expanded.std().item())
            token_expanded = torch.nn.functional.relu(token_expanded)
            token_compressed = torch.einsum(
                "bzh,sz->bsh", token_expanded, self.cross_token_down_weights[i]
            )
            x = x + token_compressed
            hidden_expanded = torch.einsum(
                "bsh,eh->bse", x * self.inverse_stds[i], self.per_token_up_weights[i]
            )
            scales["per_token"].append(hidden_expanded.std().item())
            hidden_expanded = torch.nn.functional.relu(hidden_expanded)
            hidden_compressed = torch.einsum(
                "bse,he->bsh", hidden_expanded, self.per_token_down_weights[i]
            )
            x = x + hidden_compressed

        self.last_residual_scales = scales["residual"]

        # Output layer
        logits = torch.einsum("bsh,vh->bsv", x, self.output_weights) + self.output_bias
        scales["logits"] = logits.std().item()
        return logits, scales

    def update_inverse_stds(self):
        # this division is allowed as long as it isn't called during inference, eg not called between recieving input and returning output
        self.inverse_stds = self.inverse_stds * 0.99 + 0.01 * (
            1 / torch.tensor(self.last_residual_scales).to(self.inverse_stds.device)
        )


def conv1d_same(input, weight):
    """
    Perform 1D convolution with 'same' padding using einsum and as_strided.

    Args:
    - input (torch.Tensor): Input tensor of shape (batch_size, in_channels, length)
    - weight (torch.Tensor): Convolution kernel of shape (out_channels, in_channels, kernel_size)

    Returns:
    - output (torch.Tensor): Convolved tensor of shape (batch_size, out_channels, length)
    """
    batch_size, in_channels, length = input.shape
    out_channels, _, kernel_size = weight.shape

    # Calculate padding
    pad = (kernel_size - 1) // 2

    # Pad the input
    padded_input = torch.nn.functional.pad(input, (pad, pad))

    # Create a strided version of the input
    stride = padded_input.stride()
    strided_input = padded_input.as_strided(
        size=(batch_size, in_channels, length, kernel_size),
        stride=(stride[0], stride[1], stride[2], 1),
    )

    # Perform convolution using einsum
    output = torch.einsum("bilk,oik->bol", strided_input, weight)

    return output


class ConvMLM(nn.Module):
    def __init__(self, vocab_size, kernel_size, hidden_dim, num_layers, expansion_factor):
        super().__init__()
        self.vocab_size = vocab_size
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        self.expansion_factor = expansion_factor
        self.kernel_size = kernel_size

        # Embedding weights
        self.embed_weights = nn.Parameter(torch.randn(vocab_size, hidden_dim) * 0.01)

        # Hidden layer weights and biases
        scale_factor = (hidden_dim * kernel_size) ** -0.5  # allowed bc not forward pass
        self.up_weights = nn.Parameter(
            torch.randn(num_layers, hidden_dim * expansion_factor, hidden_dim, kernel_size)
            * scale_factor
        )
        self.down_weights = nn.Parameter(
            torch.randn(num_layers, hidden_dim, hidden_dim * expansion_factor, kernel_size)
            * scale_factor
            * expansion_factor**-0.5
        )

        self.register_buffer("inverse_stds", torch.ones(num_layers))

        # Output layer weights and bias
        self.output_weights = nn.Parameter(torch.randn(vocab_size, hidden_dim) * vocab_size**-0.5)
        self.output_bias = nn.Parameter(torch.zeros(vocab_size))

    def forward(self, token_indices: torch.Tensor) -> torch.Tensor:
        x = (
            index_embeddings(self.embed_weights, token_indices).permute(0, 2, 1) * 100
        )  # increase gradient towards embeddings

        # Hidden layers
        scales = {"residual": [], "activations": []}
        for i in range(self.num_layers):
            # print("layer", i, "shape", x.shape)
            scales["residual"].append(x.std().item())

            token_expanded = conv1d_same(x * self.inverse_stds[i], self.up_weights[i])
            scales["activations"].append(token_expanded.std().item())
            token_expanded = torch.nn.functional.relu(token_expanded)
            token_compressed = conv1d_same(token_expanded, self.down_weights[i])
            x = x + token_compressed

        self.last_residual_scales = scales["residual"]

        # Output layer
        logits = torch.einsum("bhs,vh->bsv", x, self.output_weights) + self.output_bias
        scales["logits"] = logits.std().item()
        return logits, scales

    def update_inverse_stds(self):
        # this division is allowed as long as it isn't called during inference, eg not called between recieving input and returning output
        self.inverse_stds = self.inverse_stds * 0.99 + 0.01 * (
            1 / torch.tensor(self.last_residual_scales).to(self.inverse_stds.device)
        )


class ConvMLMWithBiBigrams(nn.Module):
    def __init__(
        self, vocab_size, kernel_size, hidden_dim, num_layers, expansion_factor, mask_token=50256
    ):
        super().__init__()
        self.vocab_size = vocab_size
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        self.expansion_factor = expansion_factor
        self.kernel_size = kernel_size

        # Embedding weights
        self.embed_weights = nn.Parameter(torch.randn(vocab_size, hidden_dim) * 0.01)

        # Hidden layer weights and biases
        scale_factor = (hidden_dim * kernel_size) ** -0.5  # allowed bc not forward pass
        self.up_weights = nn.Parameter(
            torch.randn(num_layers, hidden_dim * expansion_factor, hidden_dim, kernel_size)
            * scale_factor
        )
        self.down_weights = nn.Parameter(
            torch.randn(num_layers, hidden_dim, hidden_dim * expansion_factor, kernel_size)
            * scale_factor
            * expansion_factor**-0.5
        )

        self.register_buffer("inverse_stds", torch.ones(num_layers))

        # Output layer weights and bias
        self.output_weights = nn.Parameter(torch.randn(vocab_size, hidden_dim) * vocab_size**-0.5)
        self.output_bias = nn.Parameter(torch.zeros(vocab_size))

        self.BiBigramMLM = BiBigramMLM(vocab_size, mask_token)
        self.bigram_multiplier = nn.Parameter(torch.tensor(1.0))

    def forward(self, token_indices: torch.Tensor) -> torch.Tensor:
        x = (
            index_embeddings(self.embed_weights, token_indices).permute(0, 2, 1) * 100
        )  # increase gradient towards embeddings

        # Hidden layers
        scales = {"residual": [], "activations": []}
        for i in range(self.num_layers):
            # print("layer", i, "shape", x.shape)
            scales["residual"].append(x.std().item())

            token_expanded = conv1d_same(x * self.inverse_stds[i], self.up_weights[i])
            scales["activations"].append(token_expanded.std().item())
            token_expanded = torch.nn.functional.relu(token_expanded)
            token_compressed = conv1d_same(token_expanded, self.down_weights[i])
            x = x + token_compressed

        self.last_residual_scales = scales["residual"]

        # Output layer
        logits = torch.einsum("bhs,vh->bsv", x, self.output_weights) + self.output_bias
        scales["logits"] = logits.std().item()
        with torch.no_grad():
            bigram_logits = self.BiBigramMLM(token_indices)
        logits = logits + bigram_logits * self.bigram_multiplier
        scales["learned_multiplier"] = self.bigram_multiplier.item()
        return logits, scales

    def update_inverse_stds(self):
        # this division is allowed as long as it isn't called during inference, eg not called between recieving input and returning output
        self.inverse_stds = self.inverse_stds * 0.99 + 0.01 * (
            1 / torch.tensor(self.last_residual_scales).to(self.inverse_stds.device)
        )
