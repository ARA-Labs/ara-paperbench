"""
NetHack fine-tuning training script with knowledge retention integration.

Loads a pre-trained 33M LSTM model (Tuyls et al., 2023) and fine-tunes it
with APPO (Sample Factory) on the NetHack Learning Environment (Human Monk).

Supports four training modes:
  - vanilla: standard APPO fine-tuning (entropy_cost=0.001)
  - ewc:     EWC auxiliary loss (lambda=2e6, Fisher from 10K NLD-AA batches)
  - bc:      BC auxiliary loss (scale=2.0, static NLD-AA buffer, no decay)
  - ks:      KS auxiliary loss (initial_scale=0.5, decay=0.99998/step)

Key heuristics applied automatically:
  H01: Pre-train critic head for 500M steps before full fine-tuning
  H02: Freeze all three encoders during fine-tuning
  H03: Disable entropy when using any knowledge retention method

Reference: Wolczyk et al. (2024), "Fine-tuning Reinforcement Learning Models is
Secretly a Forgetting Mitigation Problem", ICML 2024.
Code base: https://github.com/BartekCupial/finetuning-RL-as-CL

Usage:
    python train_nethack.py --method ks --seeds 5 --pretrained_path /path/to/model.pth
    python train_nethack.py --method vanilla --total_steps 2500000000
"""

import argparse
import copy
import logging
import os
import sys
from typing import Dict, Optional

import torch
import torch.nn as nn

# Sample Factory APPO imports
from sample_factory.algorithms.appo.appo import APPO
from sample_factory.algorithms.appo.appo_utils import make_env_func
from sample_factory.algorithms.utils.algo_utils import ExperimentStatus
from sample_factory.envs.env_registry import global_env_registry
from sample_factory.utils.utils import cfg_file

# NetHack Learning Environment
import nle  # noqa: F401 (registers NLE envs)

# Local knowledge retention methods
from knowledge_retention import (
    compute_bc_loss,
    compute_ewc_loss,
    compute_fisher_diagonal_nethack,
    compute_ks_loss,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Pre-trained model specification (Tuyls et al., 2023)
# ---------------------------------------------------------------------------
# Architecture: 3 encoders (main screen ResNet + blstats 2-layer MLP +
# message 2-layer MLP) -> concatenate -> LSTM(hidden_dim=1738) ->
# policy head (120 actions) + baseline head
PRETRAINED_URL = (
    "https://drive.google.com/uc?id=1tWxA92qkat7Uee8SKMNsj-BV1K9ENExl"
)
HIDDEN_DIM = 1738
NUM_ACTIONS = 120
TOTAL_PARAMS_MILLIONS = 33

# ---------------------------------------------------------------------------
# Default hyperparameters (Table 1, Appendix B.1)
# ---------------------------------------------------------------------------
DEFAULT_HPARAMS = {
    # Adam optimizer
    "adam_lr": 0.0001,
    "adam_beta1": 0.9,
    "adam_beta2": 0.999,
    "adam_eps": 1e-7,
    "weight_decay": 0.0001,
    # APPO
    "appo_clip_policy": 0.1,
    "appo_clip_baseline": 1.0,
    "baseline_cost": 1.0,
    "discounting": 0.999999,
    "grad_norm_clipping": 4.0,
    "batch_size": 128,
    "unroll_length": 32,
    # Reward
    "reward_clip": 10.0,
    "reward_scale": 1.0,
    "penalty_step": 0.0,
    "penalty_time": 0.0,
    # Entropy: 0.001 for vanilla; 0.0 for KR methods (H03)
    "entropy_cost_vanilla": 0.001,
    "entropy_cost_kr": 0.0,
    # Critic pre-training (H01)
    "critic_pretrain_steps": 500_000_000,
    # Knowledge retention
    "ewc_lambda": 2_000_000,
    "ewc_fisher_batches": 10_000,
    "bc_scale": 2.0,
    "ks_initial_scale": 0.5,
    "ks_decay": 0.99998,
    # Evaluation
    "eval_episodes": 1000,
    # Training
    "total_steps": 2_500_000_000,
    "n_seeds": 5,
}

# ---------------------------------------------------------------------------
# Encoder parameter identification (H02 - freeze encoders)
# ---------------------------------------------------------------------------
ENCODER_PREFIXES = (
    "main_screen_encoder.",
    "blstats_encoder.",
    "message_encoder.",
)


def _is_encoder_param(name: str) -> bool:
    """Check whether a parameter belongs to one of the three frozen encoders."""
    return any(name.startswith(prefix) for prefix in ENCODER_PREFIXES)


def _is_critic_param(name: str) -> bool:
    """Check whether a parameter belongs to the critic (baseline) head."""
    return "baseline" in name or "critic" in name


def _is_actor_param(name: str) -> bool:
    """Check whether a parameter belongs to the actor (policy) head or LSTM."""
    return not _is_encoder_param(name) and not _is_critic_param(name)


# ---------------------------------------------------------------------------
# Phase 1: Critic head pre-training (H01)
# ---------------------------------------------------------------------------

def pretrain_critic_head(
    model: nn.Module,
    env_factory,
    steps: int,
    hparams: dict,
) -> nn.Module:
    """
    Pre-train the critic (baseline) head for `steps` environment steps.

    Freezes all parameters except the critic head, runs APPO training
    to give the value function a useful initialization before actor
    fine-tuning begins.

    H01: The pre-trained model was trained with behavioral cloning (no
    critic). Starting APPO with a random critic head destabilizes training.
    Pre-training the critic alone for 500M steps stabilizes the baseline.

    Args:
        model: Pre-trained LSTM policy with randomly initialized critic head.
        env_factory: Callable that creates a NetHack environment.
        steps: Number of environment steps for critic pre-training (500M).
        hparams: Training hyperparameters dict.

    Returns:
        Model with pre-trained critic head.
    """
    logger.info(
        "H01: Pre-training critic head for %s steps (encoders + actor frozen).",
        f"{steps:,}",
    )

    # Freeze everything except critic head
    for name, param in model.named_parameters():
        param.requires_grad = _is_critic_param(name)

    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    logger.info(
        "Critic pre-training: %s / %s parameters trainable (%.1f%%).",
        f"{trainable:,}",
        f"{total:,}",
        100.0 * trainable / total,
    )

    # Run APPO with only the critic head unfrozen
    cfg = _build_appo_cfg(
        hparams,
        entropy_cost=hparams["entropy_cost_vanilla"],
        total_steps=steps,
        experiment_name="critic_pretrain",
    )
    algo = APPO(cfg)
    algo.init(model, env_factory)
    status = algo.run()
    if status != ExperimentStatus.SUCCESS:
        logger.warning("Critic pre-training ended with status: %s", status)

    return model


# ---------------------------------------------------------------------------
# Phase 2: Full fine-tuning with knowledge retention
# ---------------------------------------------------------------------------

def freeze_encoders(model: nn.Module) -> None:
    """
    H02: Freeze all three encoders during fine-tuning.

    The visual (ResNet) and text (2-layer MLP) encoders learned good
    representations from 115B transitions of behavioral cloning. Allowing
    encoder gradients risks destroying these representations.
    """
    frozen_count = 0
    for name, param in model.named_parameters():
        if _is_encoder_param(name):
            param.requires_grad = False
            frozen_count += param.numel()
    logger.info("H02: Froze %s encoder parameters.", f"{frozen_count:,}")


def get_actor_params(model: nn.Module) -> Dict[str, torch.Tensor]:
    """Extract named parameter dict for actor (non-encoder, non-critic) params."""
    return {
        name: param
        for name, param in model.named_parameters()
        if _is_actor_param(name) and param.requires_grad
    }


def setup_ewc(
    model: nn.Module,
    nld_aa_loader,
    n_batches: int = 10_000,
) -> Dict[str, torch.Tensor]:
    """
    Compute Fisher Information Matrix diagonal for EWC from NLD-AA dataset.

    Fisher estimated over `n_batches` batches from NLD-AA Human Monk subset
    (~8000 games). Applied to actor parameters only.

    Args:
        model: Pre-trained model (before fine-tuning starts).
        nld_aa_loader: DataLoader yielding (states, actions) from NLD-AA.
        n_batches: Number of batches for Fisher estimation (paper: 10,000).

    Returns:
        Fisher diagonal dict for actor parameters.
    """
    logger.info(
        "EWC: Computing Fisher diagonal over %s NLD-AA batches...",
        f"{n_batches:,}",
    )
    fisher = compute_fisher_diagonal_nethack(model, nld_aa_loader, n_batches)
    # Filter to actor parameters only
    actor_fisher = {
        name: val for name, val in fisher.items() if _is_actor_param(name)
    }
    logger.info(
        "EWC: Fisher computed for %d actor parameter groups.", len(actor_fisher)
    )
    return actor_fisher


def setup_bc_buffer(
    pretrained_model: nn.Module,
    nld_aa_loader,
    n_states: int = 10_000,
) -> list:
    """
    Collect a static buffer of NLD-AA states for BC auxiliary loss.

    BC uses a STATIC buffer of expert states from the pre-training
    distribution (NLD-AA, ~8000 Human Monk games). The BC coefficient
    has NO decay (H05).

    Args:
        pretrained_model: Frozen pre-trained policy pi*.
        nld_aa_loader: DataLoader yielding (states, actions) from NLD-AA.
        n_states: Number of states to collect for the BC buffer.

    Returns:
        List of state tensors.
    """
    logger.info("BC: Collecting %s static states from NLD-AA...", f"{n_states:,}")
    bc_buffer = []
    for batch_idx, (states, _actions) in enumerate(nld_aa_loader):
        for state in states:
            bc_buffer.append(state)
            if len(bc_buffer) >= n_states:
                break
        if len(bc_buffer) >= n_states:
            break
    logger.info("BC: Collected %d states for static buffer.", len(bc_buffer))
    return bc_buffer


def compute_retention_loss(
    method: str,
    model: nn.Module,
    pretrained_model: nn.Module,
    step: int,
    hparams: dict,
    fisher_diagonal: Optional[Dict[str, torch.Tensor]] = None,
    bc_buffer: Optional[list] = None,
    online_states: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    """
    Compute the knowledge retention auxiliary loss for the current step.

    This loss is added to the base APPO RL loss and applied to actor
    parameters only (BC5: critic is NOT regularized).

    Args:
        method: One of "ewc", "bc", "ks".
        model: Current fine-tuned model.
        pretrained_model: Frozen pre-trained model pi*.
        step: Current training step (for KS decay).
        hparams: Hyperparameters dict.
        fisher_diagonal: Fisher diagonal for EWC (required if method="ewc").
        bc_buffer: Static BC buffer states (required if method="bc").
        online_states: States from current rollout (required if method="ks").

    Returns:
        Scalar auxiliary loss tensor.
    """
    if method == "ewc":
        current_params = get_actor_params(model)
        pretrained_params = {
            name: param
            for name, param in pretrained_model.named_parameters()
            if _is_actor_param(name)
        }
        return compute_ewc_loss(
            current_params=current_params,
            pretrained_params=pretrained_params,
            fisher_diagonal=fisher_diagonal,
            regularization_coeff=hparams["ewc_lambda"],
        )

    elif method == "bc":
        return compute_bc_loss(
            current_policy=model,
            pretrained_policy=pretrained_model,
            bc_buffer=bc_buffer,
            scale=hparams["bc_scale"],
        )

    elif method == "ks":
        return compute_ks_loss(
            current_policy=model,
            pretrained_policy=pretrained_model,
            online_states=online_states,
            scale=hparams["ks_initial_scale"],
            decay=hparams["ks_decay"],
            step=step,
        )

    else:
        raise ValueError(f"Unknown retention method: {method}")


# ---------------------------------------------------------------------------
# APPO config builder
# ---------------------------------------------------------------------------

def _build_appo_cfg(
    hparams: dict,
    entropy_cost: float,
    total_steps: int,
    experiment_name: str,
) -> dict:
    """
    Build Sample Factory APPO configuration dict from our hyperparameters.

    Maps the paper's hyperparameter names to Sample Factory's expected keys.
    """
    return {
        "algo": "APPO",
        "env": "nethack",
        "experiment": experiment_name,
        # Optimizer
        "learning_rate": hparams["adam_lr"],
        "adam_beta1": hparams["adam_beta1"],
        "adam_beta2": hparams["adam_beta2"],
        "adam_eps": hparams["adam_eps"],
        "weight_decay": hparams["weight_decay"],
        # APPO
        "ppo_clip_ratio": hparams["appo_clip_policy"],
        "ppo_clip_value": hparams["appo_clip_baseline"],
        "value_loss_coeff": hparams["baseline_cost"],
        "gamma": hparams["discounting"],
        "max_grad_norm": hparams["grad_norm_clipping"],
        "batch_size": hparams["batch_size"],
        "rollout": hparams["unroll_length"],
        "entropy_loss_coeff": entropy_cost,
        # Reward
        "reward_clip": hparams["reward_clip"],
        "reward_scale": hparams["reward_scale"],
        # Training duration
        "train_for_env_steps": total_steps,
        # NLE-specific
        "character": "mon-hum-neu-mal",
        "penalty_step": hparams["penalty_step"],
        "penalty_time": hparams["penalty_time"],
    }


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

def evaluate(
    model: nn.Module,
    env_factory,
    n_episodes: int = 1000,
) -> dict:
    """
    Evaluate the fine-tuned model over `n_episodes` episodes.

    Runs the last checkpoint for 1000 episodes (Table 4 protocol) and
    reports: score, turns, steps, dlvl, xplvl, eating, gold, scout,
    sokoban, staircase.

    Args:
        model: Fine-tuned model to evaluate.
        env_factory: Callable creating a NetHack environment.
        n_episodes: Number of evaluation episodes (paper: 1000).

    Returns:
        Dict of metric_name -> (mean, std) aggregated over episodes.
    """
    logger.info("Evaluating over %d episodes...", n_episodes)
    model.eval()

    metrics_accum = {
        "score": [], "turns": [], "steps": [], "dlvl": [],
        "xplvl": [], "eating": [], "gold": [], "scout": [],
        "sokoban": [], "staircase": [],
    }

    for ep in range(n_episodes):
        env = env_factory()
        obs = env.reset()
        done = False
        episode_reward = 0.0
        episode_steps = 0

        # LSTM hidden state
        hidden = None

        while not done:
            obs_tensor = torch.tensor(obs, dtype=torch.float32).unsqueeze(0)
            with torch.no_grad():
                action_dist, _value, hidden = model(obs_tensor, hidden)
                action = action_dist.sample()
            obs, reward, done, info = env.step(action.item())
            episode_reward += reward
            episode_steps += 1

        # Collect NLE task metrics from final info dict
        metrics_accum["score"].append(info.get("episode_return", episode_reward))
        metrics_accum["turns"].append(info.get("turns", 0))
        metrics_accum["steps"].append(episode_steps)
        metrics_accum["dlvl"].append(info.get("dlvl", 0))
        metrics_accum["xplvl"].append(info.get("xplvl", 0))
        metrics_accum["eating"].append(info.get("eating", 0))
        metrics_accum["gold"].append(info.get("gold", 0))
        metrics_accum["scout"].append(info.get("scout", 0))
        metrics_accum["sokoban"].append(info.get("sokoban", 0))
        metrics_accum["staircase"].append(info.get("staircase", 0))

        if (ep + 1) % 100 == 0:
            import numpy as np
            mean_score = np.mean(metrics_accum["score"])
            logger.info(
                "  Episode %d/%d — running mean score: %.1f",
                ep + 1, n_episodes, mean_score,
            )

        env.close()

    import numpy as np
    results = {}
    for key, values in metrics_accum.items():
        arr = np.array(values, dtype=np.float64)
        results[key] = {"mean": float(arr.mean()), "std": float(arr.std())}

    logger.info("=== Evaluation Results (1000 episodes) ===")
    for key, stats in results.items():
        logger.info("  %-12s  %.1f +/- %.1f", key, stats["mean"], stats["std"])

    return results


# ---------------------------------------------------------------------------
# Main training loop
# ---------------------------------------------------------------------------

def run_single_seed(
    seed: int,
    method: str,
    pretrained_path: str,
    nld_aa_path: Optional[str],
    hparams: dict,
    output_dir: str,
) -> dict:
    """
    Run one seed of NetHack fine-tuning with the specified retention method.

    Pipeline:
      1. Load pre-trained 33M LSTM model
      2. Pre-train critic head for 500M steps (H01)
      3. Freeze encoders (H02)
      4. Set entropy_cost=0.0 if using KR method (H03)
      5. Compute retention prerequisites (Fisher / BC buffer)
      6. Fine-tune with APPO + retention loss
      7. Evaluate last checkpoint (1000 episodes)

    Args:
        seed: Random seed.
        method: "vanilla", "ewc", "bc", or "ks".
        pretrained_path: Path to pre-trained model checkpoint.
        nld_aa_path: Path to NLD-AA dataset (required for ewc/bc).
        hparams: Hyperparameters dict.
        output_dir: Directory to save checkpoints and logs.

    Returns:
        Evaluation results dict.
    """
    logger.info("=" * 60)
    logger.info("Seed %d | Method: %s", seed, method)
    logger.info("=" * 60)

    torch.manual_seed(seed)
    import numpy as np
    np.random.seed(seed)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info("Device: %s", device)

    # ------------------------------------------------------------------
    # Step 1: Load pre-trained model
    # ------------------------------------------------------------------
    logger.info("Loading pre-trained model from: %s", pretrained_path)
    checkpoint = torch.load(pretrained_path, map_location=device)
    model = checkpoint["model"] if "model" in checkpoint else checkpoint
    model = model.to(device)

    param_count = sum(p.numel() for p in model.parameters())
    logger.info(
        "Model loaded: %s parameters (expected ~%dM).",
        f"{param_count:,}",
        TOTAL_PARAMS_MILLIONS,
    )

    # Frozen copy for KR auxiliary losses
    pretrained_model = copy.deepcopy(model)
    pretrained_model.eval()
    for p in pretrained_model.parameters():
        p.requires_grad = False

    # ------------------------------------------------------------------
    # Step 2: Pre-train critic head (H01)
    # ------------------------------------------------------------------
    def env_factory():
        """Create NLE Human Monk environment."""
        import nle.env  # noqa: F811
        return nle.env.NLE(
            character="mon-hum-neu-mal",
            max_episode_steps=100_000,
            penalty_step=hparams["penalty_step"],
            penalty_time=hparams["penalty_time"],
        )

    model = pretrain_critic_head(
        model, env_factory, hparams["critic_pretrain_steps"], hparams
    )

    # ------------------------------------------------------------------
    # Step 3: Freeze encoders (H02)
    # ------------------------------------------------------------------
    freeze_encoders(model)

    # Unfreeze actor (LSTM + policy head) and critic for full fine-tuning
    for name, param in model.named_parameters():
        if not _is_encoder_param(name):
            param.requires_grad = True

    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    logger.info("Fine-tuning phase: %s trainable parameters.", f"{trainable:,}")

    # ------------------------------------------------------------------
    # Step 4: Set entropy cost (H03)
    # ------------------------------------------------------------------
    use_kr = method in ("ewc", "bc", "ks")
    entropy_cost = (
        hparams["entropy_cost_kr"] if use_kr
        else hparams["entropy_cost_vanilla"]
    )
    logger.info(
        "H03: entropy_cost = %.4f (%s)",
        entropy_cost,
        "disabled for KR" if use_kr else "vanilla",
    )

    # ------------------------------------------------------------------
    # Step 5: Setup retention method prerequisites
    # ------------------------------------------------------------------
    fisher_diagonal = None
    bc_buffer = None

    if method == "ewc":
        from torch.utils.data import DataLoader
        nld_aa_dataset = _load_nld_aa_dataset(nld_aa_path)
        nld_aa_loader = DataLoader(
            nld_aa_dataset,
            batch_size=hparams["batch_size"],
            shuffle=True,
        )
        fisher_diagonal = setup_ewc(
            model, nld_aa_loader, hparams["ewc_fisher_batches"]
        )

    elif method == "bc":
        from torch.utils.data import DataLoader
        nld_aa_dataset = _load_nld_aa_dataset(nld_aa_path)
        nld_aa_loader = DataLoader(
            nld_aa_dataset,
            batch_size=hparams["batch_size"],
            shuffle=True,
        )
        bc_buffer = setup_bc_buffer(pretrained_model, nld_aa_loader)

    # ------------------------------------------------------------------
    # Step 6: Fine-tune with APPO + retention loss
    # ------------------------------------------------------------------
    logger.info(
        "Starting APPO fine-tuning for %s steps...",
        f"{hparams['total_steps']:,}",
    )

    cfg = _build_appo_cfg(
        hparams,
        entropy_cost=entropy_cost,
        total_steps=hparams["total_steps"],
        experiment_name=f"finetune_{method}_seed{seed}",
    )

    # Hook into APPO's training step to add retention loss
    class RetentionAPPO(APPO):
        """APPO subclass that injects knowledge retention auxiliary loss."""

        def _compute_loss(self, batch, step):
            """Override to add retention loss to the base APPO loss."""
            base_loss, stats = super()._compute_loss(batch, step)

            if method == "vanilla":
                return base_loss, stats

            online_states = batch["obs"] if method == "ks" else None
            retention_loss = compute_retention_loss(
                method=method,
                model=self.model,
                pretrained_model=pretrained_model,
                step=step,
                hparams=hparams,
                fisher_diagonal=fisher_diagonal,
                bc_buffer=bc_buffer,
                online_states=online_states,
            )

            stats[f"{method}_loss"] = retention_loss.item()
            total_loss = base_loss + retention_loss
            return total_loss, stats

    algo = RetentionAPPO(cfg)
    algo.init(model, env_factory)
    status = algo.run()
    logger.info("Fine-tuning completed with status: %s", status)

    # ------------------------------------------------------------------
    # Step 7: Evaluate last checkpoint (1000 episodes)
    # ------------------------------------------------------------------
    results = evaluate(model, env_factory, hparams["eval_episodes"])

    # Save results
    seed_dir = os.path.join(output_dir, f"seed_{seed}")
    os.makedirs(seed_dir, exist_ok=True)
    import json
    results_path = os.path.join(seed_dir, "eval_results.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Results saved to: %s", results_path)

    return results


def _load_nld_aa_dataset(nld_aa_path: Optional[str]):
    """
    Load NLD-AA dataset (Human Monk subset, ~8000 games).

    NLD-AA: NetHack Learning Dataset - AutoAscend (Hambro et al., 2022c).
    Source: https://github.com/dungeonsdatasubmission/dungeonsdata-neurips2022

    Args:
        nld_aa_path: Path to NLD-AA dataset directory.

    Returns:
        PyTorch Dataset yielding (state, action) pairs.
    """
    if nld_aa_path is None:
        raise ValueError(
            "NLD-AA dataset path required for EWC/BC methods. "
            "Download from: https://github.com/dungeonsdatasubmission/"
            "dungeonsdata-neurips2022"
        )
    # NLD-AA dataset loading follows the finetuning-RL-as-CL codebase
    from nle.dataset import TtyrecDataset
    dataset = TtyrecDataset(
        nld_aa_path,
        character="mon-hum-neu-mal",
    )
    logger.info("Loaded NLD-AA dataset: %d episodes.", len(dataset))
    return dataset


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="NetHack fine-tuning with knowledge retention (FTRL).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--method",
        type=str,
        choices=["vanilla", "ewc", "bc", "ks"],
        default="ks",
        help="Knowledge retention method.",
    )
    parser.add_argument(
        "--pretrained_path",
        type=str,
        required=True,
        help="Path to pre-trained 33M LSTM checkpoint.",
    )
    parser.add_argument(
        "--nld_aa_path",
        type=str,
        default=None,
        help="Path to NLD-AA dataset (required for ewc/bc methods).",
    )
    parser.add_argument(
        "--seeds",
        type=int,
        default=DEFAULT_HPARAMS["n_seeds"],
        help="Number of random seeds to run.",
    )
    parser.add_argument(
        "--total_steps",
        type=int,
        default=DEFAULT_HPARAMS["total_steps"],
        help="Total environment steps for fine-tuning.",
    )
    parser.add_argument(
        "--critic_pretrain_steps",
        type=int,
        default=DEFAULT_HPARAMS["critic_pretrain_steps"],
        help="Environment steps for critic head pre-training (H01).",
    )
    parser.add_argument(
        "--eval_episodes",
        type=int,
        default=DEFAULT_HPARAMS["eval_episodes"],
        help="Number of evaluation episodes per seed.",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="results/nethack",
        help="Output directory for checkpoints and logs.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # Merge CLI args into hparams
    hparams = dict(DEFAULT_HPARAMS)
    hparams["total_steps"] = args.total_steps
    hparams["critic_pretrain_steps"] = args.critic_pretrain_steps
    hparams["eval_episodes"] = args.eval_episodes

    logger.info("Method: %s", args.method)
    logger.info("Seeds: %d", args.seeds)
    logger.info("Total steps: %s", f"{args.total_steps:,}")
    logger.info("Output: %s", args.output_dir)

    os.makedirs(args.output_dir, exist_ok=True)

    all_results = {}
    for seed in range(args.seeds):
        results = run_single_seed(
            seed=seed,
            method=args.method,
            pretrained_path=args.pretrained_path,
            nld_aa_path=args.nld_aa_path,
            hparams=hparams,
            output_dir=args.output_dir,
        )
        all_results[f"seed_{seed}"] = results

    # Aggregate across seeds
    import numpy as np
    logger.info("=" * 60)
    logger.info("AGGREGATE RESULTS (%d seeds, %s)", args.seeds, args.method)
    logger.info("=" * 60)

    metric_names = list(next(iter(all_results.values())).keys())
    for metric in metric_names:
        means = [all_results[s][metric]["mean"] for s in all_results]
        agg_mean = np.mean(means)
        agg_std = np.std(means)
        logger.info("  %-12s  %.1f +/- %.1f", metric, agg_mean, agg_std)

    # Save aggregate
    import json
    agg_path = os.path.join(args.output_dir, f"aggregate_{args.method}.json")
    with open(agg_path, "w") as f:
        json.dump(all_results, f, indent=2)
    logger.info("Aggregate results saved to: %s", agg_path)


if __name__ == "__main__":
    main()
