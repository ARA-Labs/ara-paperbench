"""
RoboticSequence SAC training script with knowledge retention integration.

Pre-trains SAC on FAR stages (peg-unplug-side, push-wall), then fine-tunes
on the full 4-stage sequence (hammer -> push -> peg-unplug-side -> push-wall).

Supports five training modes:
  - vanilla:   standard SAC fine-tuning
  - ewc:       EWC auxiliary loss (actor_coeff=100, critic_coeff=0,
               Fisher from 2560 replay samples, clipped at 1e-5)
  - bc:        BC auxiliary loss (actor_coeff=1, critic_coeff=0)
  - em:        Episodic Memory (10K protected samples in replay buffer)
  - scratch:   SAC from scratch (no pre-training, baseline comparison)

Key experimental parameters:
  - 20 seeds, 90% confidence intervals
  - max_steps_per_stage = 200, success_reward_multiplier (beta) = 1.5
  - lr = 1e-3, batch_size = 128, replay_buffer = 100K

Reference: Wolczyk et al. (2024), "Fine-tuning Reinforcement Learning Models is
Secretly a Forgetting Mitigation Problem", ICML 2024.
Based on Continual World codebase (Wolczyk et al., 2021).

Usage:
    python train_robotic_sequence.py --method bc --seeds 20
    python train_robotic_sequence.py --method ewc --seeds 20 --total_steps 3000000
"""

import argparse
import copy
import json
import logging
import os
from typing import Dict, List, Optional, Tuple

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# Meta-World environment
import metaworld

# Local modules
from knowledge_retention import (
    compute_bc_loss,
    compute_ewc_loss,
    compute_fisher_diagonal_robotic,
    setup_episodic_memory_buffer,
)
from robotic_sequence import (
    MultiHeadMLP,
    RoboticSequence,
    compute_forward_transfer,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Stage definitions
# ---------------------------------------------------------------------------
STAGE_NAMES = ["hammer", "push", "peg-unplug-side", "push-wall"]
FAR_STAGES = ["peg-unplug-side", "push-wall"]  # pre-trained stages
CLOSE_STAGES = ["hammer", "push"]  # new downstream stages

# ---------------------------------------------------------------------------
# Default hyperparameters (Table 3, Appendix B.3)
# ---------------------------------------------------------------------------
DEFAULT_HPARAMS = {
    # SAC optimizer
    "lr": 1e-3,
    "batch_size": 128,
    # Replay buffer
    "replay_buffer_size": 100_000,
    "episodic_memory_size": 10_000,  # 10% of replay buffer
    # Environment
    "max_steps_per_stage": 200,
    "success_reward_multiplier": 1.5,
    # Model architecture
    "hidden_dim": 256,
    "n_layers": 4,
    # Knowledge retention (Table 3)
    "ewc_actor_coeff": 100,
    "ewc_critic_coeff": 0,
    "ewc_fisher_samples": 2560,
    "ewc_fisher_clip": 1e-5,
    "bc_actor_coeff": 1,
    "bc_critic_coeff": 0,
    # Training
    "total_steps": 3_000_000,
    "pretrain_steps": 1_000_000,
    "eval_interval": 50_000,
    "n_seeds": 20,
    # SAC-specific
    "gamma": 0.99,
    "tau": 0.005,
    "alpha_auto_tune": True,
    "initial_alpha": 0.2,
    "target_update_interval": 1,
}


# ---------------------------------------------------------------------------
# Replay Buffer with Episodic Memory Protection
# ---------------------------------------------------------------------------

class ReplayBuffer:
    """
    SAC replay buffer with optional protected episodic memory region.

    The first `em_size` entries are protected from overwriting when
    episodic memory (EM) is used. New transitions are inserted into the
    non-protected region via FIFO.

    Args:
        capacity: Total buffer size (paper: 100,000).
        em_size: Number of protected episodic memory entries (paper: 10,000).
    """

    def __init__(self, capacity: int = 100_000, em_size: int = 0):
        self.capacity = capacity
        self.em_size = em_size
        self.buffer: List[Tuple[np.ndarray, np.ndarray, float, np.ndarray, bool]] = []
        self.write_idx = em_size  # start writing after protected region

    def add_episodic_memory(
        self,
        memory: List[Tuple[torch.Tensor, torch.Tensor, torch.Tensor]],
    ) -> None:
        """
        Load protected episodic memory samples into the buffer.

        These occupy the first em_size slots and are never overwritten.

        Args:
            memory: List of (state, action, reward) tuples from pre-training.
        """
        assert len(memory) <= self.em_size, (
            f"Episodic memory ({len(memory)}) exceeds protected region ({self.em_size})"
        )
        for state, action, reward in memory:
            self.buffer.append((
                state.numpy(),
                action.numpy(),
                reward.item(),
                np.zeros_like(state.numpy()),  # placeholder next_state
                False,  # not done
            ))
        logger.info(
            "EM: Loaded %d protected samples (%.1f%% of %d buffer).",
            len(memory),
            100.0 * len(memory) / self.capacity,
            self.capacity,
        )

    def add(
        self,
        state: np.ndarray,
        action: np.ndarray,
        reward: float,
        next_state: np.ndarray,
        done: bool,
    ) -> None:
        """Add a transition, respecting the protected episodic memory region."""
        transition = (state, action, reward, next_state, done)
        if len(self.buffer) < self.capacity:
            self.buffer.append(transition)
        else:
            # Overwrite non-protected region only
            self.buffer[self.write_idx] = transition
        self.write_idx = max(self.em_size, (self.write_idx + 1) % self.capacity)

    def sample(self, batch_size: int) -> Tuple:
        """Sample a random mini-batch from the entire buffer (including EM)."""
        indices = np.random.randint(0, len(self.buffer), size=batch_size)
        states, actions, rewards, next_states, dones = zip(
            *[self.buffer[i] for i in indices]
        )
        return (
            torch.tensor(np.array(states), dtype=torch.float32),
            torch.tensor(np.array(actions), dtype=torch.float32),
            torch.tensor(np.array(rewards), dtype=torch.float32).unsqueeze(1),
            torch.tensor(np.array(next_states), dtype=torch.float32),
            torch.tensor(np.array(dones), dtype=torch.float32).unsqueeze(1),
        )

    def sample_states(self, n: int) -> torch.Tensor:
        """Sample `n` states from the buffer (for Fisher estimation)."""
        indices = np.random.randint(0, len(self.buffer), size=n)
        states = [self.buffer[i][0] for i in indices]
        return torch.tensor(np.array(states), dtype=torch.float32)

    def __len__(self) -> int:
        return len(self.buffer)


# ---------------------------------------------------------------------------
# SAC Actor (Gaussian policy with multi-head MLP)
# ---------------------------------------------------------------------------

class SACGaussianActor(nn.Module):
    """
    SAC Gaussian policy built on MultiHeadMLP backbone.

    Outputs mean and log_std for a squashed Gaussian (tanh-Normal)
    per stage. Architecture: 4-layer MLP, 256 hidden, LeakyReLU,
    LayerNorm after first layer, separate output heads per stage.
    """

    LOG_STD_MIN = -20
    LOG_STD_MAX = 2

    def __init__(self, obs_dim: int, action_dim: int, n_stages: int = 4,
                 hidden_dim: int = 256, n_layers: int = 4):
        super().__init__()
        # Output dim is 2 * action_dim (mean + log_std)
        self.backbone = MultiHeadMLP(
            input_dim=obs_dim,
            hidden_dim=hidden_dim,
            output_dim=2 * action_dim,
            n_stages=n_stages,
            n_layers=n_layers,
        )
        self.action_dim = action_dim

    def forward(self, obs: torch.Tensor, stage_id: int = 0):
        """Return (mean, log_std) for the given stage."""
        out = self.backbone(obs, stage_id)
        mean, log_std = out.chunk(2, dim=-1)
        log_std = torch.clamp(log_std, self.LOG_STD_MIN, self.LOG_STD_MAX)
        return mean, log_std

    def sample(self, obs: torch.Tensor, stage_id: int = 0):
        """Sample an action and return (action, log_prob, mean)."""
        mean, log_std = self.forward(obs, stage_id)
        std = log_std.exp()
        normal = torch.distributions.Normal(mean, std)
        z = normal.rsample()
        action = torch.tanh(z)

        # Log prob with tanh squashing correction
        log_prob = normal.log_prob(z) - torch.log(1 - action.pow(2) + 1e-6)
        log_prob = log_prob.sum(dim=-1, keepdim=True)

        return action, log_prob, mean

    def act(self, state: torch.Tensor, stage_id: int = 0) -> torch.Tensor:
        """Deterministic action for evaluation (use mean)."""
        mean, _ = self.forward(state.unsqueeze(0), stage_id)
        return torch.tanh(mean).squeeze(0)

    def get_distribution(self, states: torch.Tensor, stage_id: int = 0):
        """Return action distribution for BC/KS auxiliary losses."""
        mean, log_std = self.forward(states, stage_id)
        return torch.distributions.Normal(mean, log_std.exp())

    def compute_log_prob(self, states, mu, sigma):
        """Compute log probability for Fisher estimation."""
        normal = torch.distributions.Normal(mu, sigma)
        return normal.log_prob(torch.tanh(mu)).sum(dim=-1)


# ---------------------------------------------------------------------------
# SAC Critic (twin Q-networks)
# ---------------------------------------------------------------------------

class SACCritic(nn.Module):
    """Twin Q-networks for SAC, each built on MultiHeadMLP."""

    def __init__(self, obs_dim: int, action_dim: int, n_stages: int = 4,
                 hidden_dim: int = 256, n_layers: int = 4):
        super().__init__()
        self.q1 = MultiHeadMLP(
            input_dim=obs_dim + action_dim,
            hidden_dim=hidden_dim,
            output_dim=1,
            n_stages=n_stages,
            n_layers=n_layers,
        )
        self.q2 = MultiHeadMLP(
            input_dim=obs_dim + action_dim,
            hidden_dim=hidden_dim,
            output_dim=1,
            n_stages=n_stages,
            n_layers=n_layers,
        )

    def forward(self, obs: torch.Tensor, action: torch.Tensor, stage_id: int = 0):
        x = torch.cat([obs, action], dim=-1)
        return self.q1(x, stage_id), self.q2(x, stage_id)


# ---------------------------------------------------------------------------
# Meta-World environment factory
# ---------------------------------------------------------------------------

def create_metaworld_envs(stage_names: List[str], seed: int) -> List:
    """
    Create Meta-World environment instances for the given stages.

    Each stage gets random start/goal positions per Meta-World convention.

    Args:
        stage_names: List of Meta-World task names.
        seed: Random seed.

    Returns:
        List of Meta-World environment instances.
    """
    ml1 = metaworld.ML1
    envs = []
    for name in stage_names:
        env_cls = ml1(name).train_classes[name]
        env = env_cls()
        tasks = [t for t in ml1(name).train_tasks if t.env_name == name]
        env.set_task(tasks[seed % len(tasks)])
        env.seed(seed)
        envs.append(env)
    return envs


# ---------------------------------------------------------------------------
# Pre-training on FAR stages
# ---------------------------------------------------------------------------

def pretrain_on_far_stages(
    actor: SACGaussianActor,
    critic: SACCritic,
    target_critic: SACCritic,
    far_env: RoboticSequence,
    hparams: dict,
    seed: int,
) -> Tuple[SACGaussianActor, SACCritic, ReplayBuffer]:
    """
    Pre-train SAC on FAR stages (peg-unplug-side + push-wall).

    Trains until 100% success rate on both stages or `pretrain_steps` reached.

    Args:
        actor: SAC actor network.
        critic: SAC twin Q-network.
        target_critic: Target Q-network for soft updates.
        far_env: RoboticSequence env with only FAR stages.
        hparams: Hyperparameters.
        seed: Random seed.

    Returns:
        (pre-trained actor, pre-trained critic, filled replay buffer)
    """
    logger.info("Pre-training SAC on FAR stages: %s", FAR_STAGES)

    replay_buffer = ReplayBuffer(capacity=hparams["replay_buffer_size"])

    actor_optimizer = optim.Adam(actor.parameters(), lr=hparams["lr"])
    critic_optimizer = optim.Adam(critic.parameters(), lr=hparams["lr"])

    # Auto-tune entropy coefficient
    if hparams["alpha_auto_tune"]:
        target_entropy = -actor.action_dim
        log_alpha = torch.zeros(1, requires_grad=True)
        alpha_optimizer = optim.Adam([log_alpha], lr=hparams["lr"])
        alpha = log_alpha.exp().item()
    else:
        alpha = hparams["initial_alpha"]

    obs = far_env.reset()
    total_steps = 0

    while total_steps < hparams["pretrain_steps"]:
        obs_tensor = torch.tensor(obs, dtype=torch.float32)
        # Determine current stage for the multi-head forward pass
        stage_id = far_env.current_stage

        with torch.no_grad():
            action, _, _ = actor.sample(obs_tensor.unsqueeze(0), stage_id)
            action = action.squeeze(0).numpy()

        next_obs, reward, done, info = far_env.step(action)
        replay_buffer.add(obs, action, reward, next_obs, done)

        obs = next_obs if not done else far_env.reset()
        total_steps += 1

        # Train SAC after initial exploration
        if len(replay_buffer) > hparams["batch_size"]:
            _sac_update(
                actor, critic, target_critic,
                replay_buffer, actor_optimizer, critic_optimizer,
                alpha, hparams, stage_id,
            )
            # Soft target update
            _soft_update(critic, target_critic, hparams["tau"])

            # Auto-tune alpha
            if hparams["alpha_auto_tune"]:
                alpha_loss, alpha = _update_alpha(
                    actor, obs_tensor.unsqueeze(0), stage_id,
                    log_alpha, alpha_optimizer, target_entropy,
                )

        if total_steps % hparams["eval_interval"] == 0:
            logger.info(
                "Pre-train step %s / %s — buffer size: %d",
                f"{total_steps:,}",
                f"{hparams['pretrain_steps']:,}",
                len(replay_buffer),
            )

    logger.info("Pre-training complete. Buffer size: %d", len(replay_buffer))
    return actor, critic, replay_buffer


# ---------------------------------------------------------------------------
# SAC update step
# ---------------------------------------------------------------------------

def _sac_update(
    actor: SACGaussianActor,
    critic: SACCritic,
    target_critic: SACCritic,
    replay_buffer: ReplayBuffer,
    actor_optimizer: optim.Optimizer,
    critic_optimizer: optim.Optimizer,
    alpha: float,
    hparams: dict,
    stage_id: int,
) -> dict:
    """Perform one SAC gradient step (critic + actor updates)."""
    states, actions, rewards, next_states, dones = replay_buffer.sample(
        hparams["batch_size"]
    )

    # --- Critic update ---
    with torch.no_grad():
        next_actions, next_log_probs, _ = actor.sample(next_states, stage_id)
        q1_next, q2_next = target_critic(next_states, next_actions, stage_id)
        q_next = torch.min(q1_next, q2_next) - alpha * next_log_probs
        q_target = rewards + hparams["gamma"] * (1 - dones) * q_next

    q1, q2 = critic(states, actions, stage_id)
    critic_loss = nn.functional.mse_loss(q1, q_target) + nn.functional.mse_loss(q2, q_target)

    critic_optimizer.zero_grad()
    critic_loss.backward()
    critic_optimizer.step()

    # --- Actor update ---
    new_actions, log_probs, _ = actor.sample(states, stage_id)
    q1_new, q2_new = critic(states, new_actions, stage_id)
    q_new = torch.min(q1_new, q2_new)
    actor_loss = (alpha * log_probs - q_new).mean()

    actor_optimizer.zero_grad()
    actor_loss.backward()
    actor_optimizer.step()

    return {
        "critic_loss": critic_loss.item(),
        "actor_loss": actor_loss.item(),
    }


def _soft_update(source: nn.Module, target: nn.Module, tau: float) -> None:
    """Polyak averaging for target network."""
    for sp, tp in zip(source.parameters(), target.parameters()):
        tp.data.copy_(tau * sp.data + (1 - tau) * tp.data)


def _update_alpha(
    actor, obs, stage_id, log_alpha, alpha_optimizer, target_entropy
):
    """Auto-tune SAC entropy coefficient."""
    with torch.no_grad():
        _, log_prob, _ = actor.sample(obs, stage_id)
    alpha_loss = -(log_alpha * (log_prob + target_entropy).detach()).mean()
    alpha_optimizer.zero_grad()
    alpha_loss.backward()
    alpha_optimizer.step()
    return alpha_loss.item(), log_alpha.exp().item()


# ---------------------------------------------------------------------------
# Fine-tuning with knowledge retention
# ---------------------------------------------------------------------------

def finetune(
    method: str,
    actor: SACGaussianActor,
    critic: SACCritic,
    target_critic: SACCritic,
    pretrained_actor: SACGaussianActor,
    full_env: RoboticSequence,
    replay_buffer: ReplayBuffer,
    hparams: dict,
    seed: int,
) -> Tuple[Dict, List[float], List[float]]:
    """
    Fine-tune SAC on the full 4-stage RoboticSequence with retention.

    Args:
        method: "vanilla", "ewc", "bc", "em", or "scratch".
        actor: SAC actor (initialized from pre-training or random).
        critic: SAC critic (initialized from pre-training or random).
        target_critic: Target Q-network.
        pretrained_actor: Frozen pre-trained actor (for EWC/BC).
        full_env: Full 4-stage RoboticSequence environment.
        replay_buffer: Replay buffer (may contain EM samples).
        hparams: Hyperparameters.
        seed: Random seed.

    Returns:
        (eval_results, success_rate_curve, scratch_success_curve_placeholder)
    """
    logger.info("Fine-tuning with method: %s", method)

    actor_optimizer = optim.Adam(actor.parameters(), lr=hparams["lr"])
    critic_optimizer = optim.Adam(critic.parameters(), lr=hparams["lr"])

    # Auto-tune alpha
    if hparams["alpha_auto_tune"]:
        target_entropy = -actor.action_dim
        log_alpha = torch.zeros(1, requires_grad=True)
        alpha_optimizer = optim.Adam([log_alpha], lr=hparams["lr"])
        alpha = log_alpha.exp().item()
    else:
        alpha = hparams["initial_alpha"]

    # Setup retention prerequisites
    fisher_diagonal = None
    bc_buffer = None

    if method == "ewc":
        logger.info(
            "EWC: Computing Fisher diagonal from %d replay buffer samples...",
            hparams["ewc_fisher_samples"],
        )
        fisher_diagonal = compute_fisher_diagonal_robotic(
            model=actor,
            replay_buffer=replay_buffer,
            n_samples=hparams["ewc_fisher_samples"],
            clip_min=hparams["ewc_fisher_clip"],
        )
        logger.info("EWC: Fisher diagonal computed and clipped at %.1e.", hparams["ewc_fisher_clip"])

    elif method == "bc":
        # BC buffer: states from replay buffer (pre-training data)
        bc_buffer = []
        n_bc = min(len(replay_buffer), hparams["replay_buffer_size"])
        sample_states = replay_buffer.sample_states(n_bc)
        bc_buffer = [sample_states[i] for i in range(sample_states.shape[0])]
        logger.info("BC: Using %d states from replay buffer as BC buffer.", len(bc_buffer))

    # Store pre-trained actor parameters for EWC
    pretrained_params = None
    if method == "ewc":
        pretrained_params = {
            name: param.clone().detach()
            for name, param in pretrained_actor.named_parameters()
        }

    # Training loop
    obs = full_env.reset()
    total_steps = 0
    success_rate_curve = []
    episode_successes = []
    per_stage_successes = {name: [] for name in STAGE_NAMES}

    while total_steps < hparams["total_steps"]:
        obs_tensor = torch.tensor(obs, dtype=torch.float32)
        stage_id = full_env.current_stage

        with torch.no_grad():
            action, _, _ = actor.sample(obs_tensor.unsqueeze(0), stage_id)
            action = action.squeeze(0).numpy()

        next_obs, reward, done, info = full_env.step(action)
        replay_buffer.add(obs, action, reward, next_obs, done)

        obs = next_obs if not done else full_env.reset()

        if done:
            # Track per-episode success (completed all 4 stages)
            all_stages_done = full_env.current_stage >= full_env.n_stages - 1
            episode_successes.append(1.0 if all_stages_done else 0.0)

        total_steps += 1

        # SAC update
        if len(replay_buffer) > hparams["batch_size"]:
            stats = _sac_update(
                actor, critic, target_critic,
                replay_buffer, actor_optimizer, critic_optimizer,
                alpha, hparams, stage_id,
            )
            _soft_update(critic, target_critic, hparams["tau"])

            if hparams["alpha_auto_tune"]:
                _, alpha = _update_alpha(
                    actor, obs_tensor.unsqueeze(0), stage_id,
                    log_alpha, alpha_optimizer, target_entropy,
                )

            # Knowledge retention loss (actor only, BC5)
            if method == "ewc":
                current_params = {
                    name: param
                    for name, param in actor.named_parameters()
                }
                ewc_loss = compute_ewc_loss(
                    current_params=current_params,
                    pretrained_params=pretrained_params,
                    fisher_diagonal=fisher_diagonal,
                    regularization_coeff=hparams["ewc_actor_coeff"],
                )
                actor_optimizer.zero_grad()
                ewc_loss.backward()
                actor_optimizer.step()

            elif method == "bc":
                bc_loss = compute_bc_loss(
                    current_policy=actor,
                    pretrained_policy=pretrained_actor,
                    bc_buffer=bc_buffer,
                    scale=hparams["bc_actor_coeff"],
                )
                actor_optimizer.zero_grad()
                bc_loss.backward()
                actor_optimizer.step()

        # Periodic evaluation
        if total_steps % hparams["eval_interval"] == 0:
            eval_success = _evaluate_success_rate(actor, full_env, n_episodes=50)
            success_rate_curve.append(eval_success["overall"])
            logger.info(
                "Step %s — overall success: %.2f | per-stage: %s",
                f"{total_steps:,}",
                eval_success["overall"],
                {k: f"{v:.2f}" for k, v in eval_success["per_stage"].items()},
            )

    return {
        "final_success_rate": success_rate_curve[-1] if success_rate_curve else 0.0,
        "success_rate_curve": success_rate_curve,
    }, success_rate_curve, []


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

def _evaluate_success_rate(
    actor: SACGaussianActor,
    env: RoboticSequence,
    n_episodes: int = 50,
) -> dict:
    """
    Evaluate overall and per-stage success rates.

    Args:
        actor: SAC actor to evaluate.
        env: RoboticSequence environment.
        n_episodes: Number of evaluation episodes.

    Returns:
        Dict with "overall" success rate and "per_stage" success rates.
    """
    actor.eval()
    stage_successes = {name: 0 for name in env.stage_names}
    overall_successes = 0

    for _ in range(n_episodes):
        obs = env.reset()
        done = False
        stages_completed = set()

        while not done:
            obs_tensor = torch.tensor(obs, dtype=torch.float32).unsqueeze(0)
            stage_id = env.current_stage
            with torch.no_grad():
                action = actor.act(obs_tensor.squeeze(0), stage_id)
            obs, _reward, done, info = env.step(action.numpy())
            if info.get("success", False):
                stages_completed.add(env.stage_names[stage_id])

        for stage_name in stages_completed:
            stage_successes[stage_name] += 1
        if len(stages_completed) == len(env.stage_names):
            overall_successes += 1

    actor.train()
    return {
        "overall": overall_successes / n_episodes,
        "per_stage": {
            name: count / n_episodes for name, count in stage_successes.items()
        },
    }


# ---------------------------------------------------------------------------
# Main single-seed runner
# ---------------------------------------------------------------------------

def run_single_seed(
    seed: int,
    method: str,
    hparams: dict,
    output_dir: str,
) -> dict:
    """
    Run one seed of RoboticSequence training.

    Pipeline:
      1. Create Meta-World environments for all 4 stages
      2. Pre-train SAC on FAR stages (unless method="scratch")
      3. Setup retention prerequisites (Fisher/BC/EM)
      4. Fine-tune on full 4-stage sequence
      5. Compute forward transfer metric

    Args:
        seed: Random seed.
        method: "vanilla", "ewc", "bc", "em", or "scratch".
        hparams: Hyperparameters.
        output_dir: Output directory.

    Returns:
        Results dict with final metrics.
    """
    logger.info("=" * 60)
    logger.info("Seed %d / %d | Method: %s", seed + 1, hparams["n_seeds"], method)
    logger.info("=" * 60)

    torch.manual_seed(seed)
    np.random.seed(seed)

    # ------------------------------------------------------------------
    # Step 1: Create environments
    # ------------------------------------------------------------------
    far_envs = create_metaworld_envs(FAR_STAGES, seed)
    far_seq = RoboticSequence(far_envs, stage_names=FAR_STAGES)

    all_envs = create_metaworld_envs(STAGE_NAMES, seed)
    full_seq = RoboticSequence(all_envs, stage_names=STAGE_NAMES)

    # Determine observation and action dimensions from Meta-World
    sample_obs = all_envs[0].reset()
    obs_dim = sample_obs.shape[0] + len(STAGE_NAMES) + 1  # obs + stage_onehot + norm_t
    action_dim = all_envs[0].action_space.shape[0]
    logger.info("obs_dim=%d, action_dim=%d", obs_dim, action_dim)

    # ------------------------------------------------------------------
    # Step 2: Initialize models
    # ------------------------------------------------------------------
    actor = SACGaussianActor(
        obs_dim=obs_dim,
        action_dim=action_dim,
        n_stages=len(STAGE_NAMES),
        hidden_dim=hparams["hidden_dim"],
        n_layers=hparams["n_layers"],
    )
    critic = SACCritic(
        obs_dim=obs_dim,
        action_dim=action_dim,
        n_stages=len(STAGE_NAMES),
        hidden_dim=hparams["hidden_dim"],
        n_layers=hparams["n_layers"],
    )
    target_critic = copy.deepcopy(critic)
    for p in target_critic.parameters():
        p.requires_grad = False

    # ------------------------------------------------------------------
    # Step 3: Pre-train on FAR stages (skip for "scratch")
    # ------------------------------------------------------------------
    if method != "scratch":
        actor, critic, replay_buffer = pretrain_on_far_stages(
            actor, critic, target_critic, far_seq, hparams, seed,
        )
        # Update target critic after pre-training
        target_critic.load_state_dict(critic.state_dict())
    else:
        replay_buffer = ReplayBuffer(capacity=hparams["replay_buffer_size"])

    # Freeze pre-trained actor for retention losses
    pretrained_actor = copy.deepcopy(actor)
    pretrained_actor.eval()
    for p in pretrained_actor.parameters():
        p.requires_grad = False

    # ------------------------------------------------------------------
    # Step 4: Setup episodic memory (EM)
    # ------------------------------------------------------------------
    if method == "em":
        logger.info(
            "EM: Collecting %d protected samples from FAR stages...",
            hparams["episodic_memory_size"],
        )
        em_samples = setup_episodic_memory_buffer(
            pretrained_policy=pretrained_actor,
            environment=far_seq,
            n_samples=hparams["episodic_memory_size"],
            replay_buffer_size=hparams["replay_buffer_size"],
        )
        # Create new buffer with protected EM region
        em_buffer = ReplayBuffer(
            capacity=hparams["replay_buffer_size"],
            em_size=hparams["episodic_memory_size"],
        )
        em_buffer.add_episodic_memory(em_samples)
        replay_buffer = em_buffer

    # ------------------------------------------------------------------
    # Step 5: Fine-tune on full sequence
    # ------------------------------------------------------------------
    results, success_curve, _ = finetune(
        method=method,
        actor=actor,
        critic=critic,
        target_critic=target_critic,
        pretrained_actor=pretrained_actor,
        full_env=full_seq,
        replay_buffer=replay_buffer,
        hparams=hparams,
        seed=seed,
    )

    # ------------------------------------------------------------------
    # Step 6: Final evaluation
    # ------------------------------------------------------------------
    final_eval = _evaluate_success_rate(actor, full_seq, n_episodes=100)
    results["final_eval"] = final_eval

    logger.info("Final overall success rate: %.2f", final_eval["overall"])
    for stage, rate in final_eval["per_stage"].items():
        logger.info("  %s: %.2f", stage, rate)

    # ------------------------------------------------------------------
    # Step 7: Save results
    # ------------------------------------------------------------------
    seed_dir = os.path.join(output_dir, f"seed_{seed}")
    os.makedirs(seed_dir, exist_ok=True)
    results_path = os.path.join(seed_dir, "results.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    logger.info("Results saved to: %s", results_path)

    return results


# ---------------------------------------------------------------------------
# Aggregate results across seeds
# ---------------------------------------------------------------------------

def aggregate_results(
    all_results: Dict[str, dict],
    method: str,
    hparams: dict,
    output_dir: str,
) -> None:
    """
    Aggregate results across seeds and compute forward transfer.

    Reports 90% confidence intervals (20 seeds minimum per paper).

    Args:
        all_results: Dict of seed -> results.
        method: Training method name.
        hparams: Hyperparameters.
        output_dir: Output directory.
    """
    n = len(all_results)
    logger.info("=" * 60)
    logger.info("AGGREGATE RESULTS (%d seeds, %s)", n, method)
    logger.info("=" * 60)

    # Overall success rates
    final_rates = [
        r["final_eval"]["overall"] for r in all_results.values()
    ]
    mean_rate = np.mean(final_rates)
    std_rate = np.std(final_rates)

    # 90% confidence interval (t-distribution for small samples)
    from scipy import stats as sp_stats
    ci_90 = sp_stats.t.interval(
        0.90, df=n - 1, loc=mean_rate, scale=sp_stats.sem(final_rates)
    )

    logger.info("Overall success rate: %.2f +/- %.2f", mean_rate, std_rate)
    logger.info("90%% CI: [%.2f, %.2f]", ci_90[0], ci_90[1])

    # Per-stage success rates
    for stage_name in STAGE_NAMES:
        stage_rates = [
            r["final_eval"]["per_stage"][stage_name]
            for r in all_results.values()
        ]
        s_mean = np.mean(stage_rates)
        s_std = np.std(stage_rates)
        logger.info("  %s: %.2f +/- %.2f", stage_name, s_mean, s_std)

    # Forward transfer (requires scratch baseline data)
    if method != "scratch":
        logger.info(
            "Forward transfer computation requires scratch baseline data. "
            "Run with --method scratch first, then use compute_forward_transfer()."
        )

    # Save aggregate
    agg = {
        "method": method,
        "n_seeds": n,
        "overall_mean": float(mean_rate),
        "overall_std": float(std_rate),
        "ci_90": [float(ci_90[0]), float(ci_90[1])],
        "per_seed": {k: v for k, v in all_results.items()},
    }
    agg_path = os.path.join(output_dir, f"aggregate_{method}.json")
    with open(agg_path, "w") as f:
        json.dump(agg, f, indent=2, default=str)
    logger.info("Aggregate saved to: %s", agg_path)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="RoboticSequence SAC training with knowledge retention (FTRL).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--method",
        type=str,
        choices=["vanilla", "ewc", "bc", "em", "scratch"],
        default="bc",
        help="Knowledge retention method.",
    )
    parser.add_argument(
        "--seeds",
        type=int,
        default=DEFAULT_HPARAMS["n_seeds"],
        help="Number of random seeds (paper: 20).",
    )
    parser.add_argument(
        "--total_steps",
        type=int,
        default=DEFAULT_HPARAMS["total_steps"],
        help="Total environment steps for fine-tuning phase.",
    )
    parser.add_argument(
        "--pretrain_steps",
        type=int,
        default=DEFAULT_HPARAMS["pretrain_steps"],
        help="Environment steps for pre-training on FAR stages.",
    )
    parser.add_argument(
        "--eval_interval",
        type=int,
        default=DEFAULT_HPARAMS["eval_interval"],
        help="Steps between periodic evaluations.",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="results/robotic_sequence",
        help="Output directory for results.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    hparams = dict(DEFAULT_HPARAMS)
    hparams["total_steps"] = args.total_steps
    hparams["pretrain_steps"] = args.pretrain_steps
    hparams["eval_interval"] = args.eval_interval
    hparams["n_seeds"] = args.seeds

    logger.info("Method: %s", args.method)
    logger.info("Seeds: %d", args.seeds)
    logger.info("Total steps: %s", f"{args.total_steps:,}")
    logger.info("Pre-train steps: %s", f"{args.pretrain_steps:,}")
    logger.info("Output: %s", args.output_dir)

    os.makedirs(args.output_dir, exist_ok=True)

    all_results = {}
    for seed in range(args.seeds):
        results = run_single_seed(
            seed=seed,
            method=args.method,
            hparams=hparams,
            output_dir=args.output_dir,
        )
        all_results[f"seed_{seed}"] = results

    aggregate_results(all_results, args.method, hparams, args.output_dir)


if __name__ == "__main__":
    main()
