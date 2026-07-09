"""
FRE Training Script — Complete training pipeline for Functional Reward Encodings.

Usage:
    python train_fre.py --env antmaze-large-diverse-v2 --seed 0
    python train_fre.py --env exorl-cheetah-rnd --seed 0
    python train_fre.py --env exorl-walker-rnd --seed 0
    python train_fre.py --env kitchen-complete-v0 --seed 0

Implements:
    Phase 1: Encoder-decoder pre-training (150K steps for AntMaze, 1M for others)
    Phase 2: IQL policy training with frozen encoder (850K / 1M steps)
    Evaluation: K=32 encoding, 20 episodes x 5 seeds

Hyperparameters (Appendix A, Table 3):
    lr=0.0001, batch_size=512, gamma=0.88, tau_expectile=0.8,
    beta_awr=3.0, beta_kl=0.01, target_update=0.001

Reference: Frans et al., "Unsupervised Zero-Shot RL via Functional Reward Encodings"
"""

import argparse
import os
import time
import json
from typing import Dict, Tuple, Optional, Callable

import numpy as np
import jax
import jax.numpy as jnp

from reward_functions import (
    GoalReachingRewardFunction,
    LinearRewardFunction,
    RandomRewardFunction,
    sample_reward_function,
)
from fre_network import (
    FRENetwork,
    FREAgentState,
    create_learner,
    fre_encoder_loss,
    train_fre,
)


# ========== Environment Configurations ==========

ENV_CONFIGS = {
    "antmaze-large-diverse-v2": {
        "obs_dim": 29,
        "action_dim": 8,
        "max_episode_steps": 2000,
        "encoder_steps": 150_000,
        "policy_steps": 850_000,
        "goal_threshold": 2.0,
        "exclude_xy_dims": [0, 1],  # exclude XY from linear rewards
        "env_type": "antmaze",
        "dataset_name": "antmaze-large-diverse-v2",
    },
    "exorl-cheetah-rnd": {
        "obs_dim": 18,
        "action_dim": 6,
        "max_episode_steps": 1000,
        "encoder_steps": 1_000_000,
        "policy_steps": 1_000_000,
        "goal_threshold": 0.08,
        "exclude_xy_dims": None,
        "env_type": "cheetah",
        "dataset_name": "cheetah-rnd",
        # Physics augmentation: append [speed()] for encoder
        "physics_augment_dims": 1,
    },
    "exorl-walker-rnd": {
        "obs_dim": 27,
        "action_dim": 6,
        "max_episode_steps": 1000,
        "encoder_steps": 1_000_000,
        "policy_steps": 1_000_000,
        "goal_threshold": 0.2,
        "exclude_xy_dims": None,
        "env_type": "walker",
        "dataset_name": "walker-rnd",
        # Physics augmentation: append [horizontal_velocity, torso_upright, torso_height]
        "physics_augment_dims": 3,
    },
    "kitchen-complete-v0": {
        "obs_dim": 30,
        "action_dim": 9,
        "max_episode_steps": 280,
        "encoder_steps": 1_000_000,
        "policy_steps": 1_000_000,
        "goal_threshold": 1e-6,
        "exclude_xy_dims": None,
        "env_type": "kitchen",
        "dataset_name": "kitchen-complete-v0",
    },
}


# ========== Dataset Loading ==========

def load_d4rl_dataset(env_name: str) -> Dict[str, np.ndarray]:
    """
    Load offline dataset from D4RL.

    Returns dict with keys:
        observations:      [N, obs_dim]
        actions:           [N, act_dim]
        next_observations: [N, obs_dim]
        rewards:           [N]
        terminals:         [N]
        timeouts:          [N]
    """
    import d4rl
    import gym

    env = gym.make(env_name)
    dataset = env.get_dataset()

    return {
        "observations": dataset["observations"].astype(np.float32),
        "actions": dataset["actions"].astype(np.float32),
        "next_observations": dataset["next_observations"].astype(np.float32),
        "rewards": dataset["rewards"].astype(np.float32),
        "terminals": dataset["terminals"].astype(np.float32),
        "timeouts": dataset.get("timeouts", np.zeros_like(dataset["terminals"])).astype(np.float32),
    }


def load_exorl_dataset(dataset_name: str, data_dir: str = "data/exorl") -> Dict[str, np.ndarray]:
    """
    Load offline dataset from ExORL (Yarats et al., 2022).

    Expects npz files in data_dir/{dataset_name}/ directory.
    """
    import glob

    domain, algo = dataset_name.split("-")
    pattern = os.path.join(data_dir, domain, algo, "*.npz")
    files = sorted(glob.glob(pattern))

    if not files:
        raise FileNotFoundError(
            f"No ExORL data found at {pattern}. "
            f"Download from https://github.com/denisyarats/exorl"
        )

    all_obs, all_acts, all_next_obs, all_terminals = [], [], [], []

    for f in files:
        data = np.load(f)
        obs = data["observation"].astype(np.float32)
        act = data["action"].astype(np.float32)
        # next_obs is obs shifted by 1 within episode
        next_obs = np.roll(obs, -1, axis=0)
        terminal = np.zeros(len(obs), dtype=np.float32)
        terminal[-1] = 1.0  # last step is terminal

        all_obs.append(obs)
        all_acts.append(act)
        all_next_obs.append(next_obs)
        all_terminals.append(terminal)

    return {
        "observations": np.concatenate(all_obs, axis=0),
        "actions": np.concatenate(all_acts, axis=0),
        "next_observations": np.concatenate(all_next_obs, axis=0),
        "rewards": np.zeros(sum(len(o) for o in all_obs), dtype=np.float32),  # unsupervised
        "terminals": np.concatenate(all_terminals, axis=0),
    }


def load_dataset(env_name: str, data_dir: str = "data") -> Dict[str, np.ndarray]:
    """Load dataset based on environment name."""
    if env_name.startswith("exorl-"):
        dataset_name = ENV_CONFIGS[env_name]["dataset_name"]
        return load_exorl_dataset(dataset_name, os.path.join(data_dir, "exorl"))
    else:
        return load_d4rl_dataset(env_name)


# ========== Reward Sampler Factory ==========

def create_reward_sampler(
    env_config: Dict,
    dataset: Dict[str, np.ndarray],
) -> Callable:
    """
    Create a reward sampler that returns a reward function from the FRE prior p(eta).

    Uses uniform 1/3 mixture of goal-reaching, linear, and random MLP rewards.
    """
    obs_dim = env_config["obs_dim"]

    # Compute per-dimension std for ExORL normalization
    state_std = None
    if env_config["env_type"] in ("cheetah", "walker"):
        state_std = np.std(dataset["observations"], axis=0) + 1e-8

    # Initialize reward function instances
    goal_fn = GoalReachingRewardFunction(obs_dim=obs_dim, state_std=state_std)

    linear_fn = LinearRewardFunction(
        obs_dim=obs_dim,
        exclude_dims=env_config.get("exclude_xy_dims"),
    )

    mlp_fn = RandomRewardFunction(
        num_simplex=256,
        obs_len=obs_dim,
    )

    def sampler() -> "RewardFunction":
        return sample_reward_function(
            rew_ratio_goal=1.0 / 3.0,
            rew_ratio_linear=1.0 / 3.0,
            rew_ratio_mlp=1.0 / 3.0,
            goal_fn=goal_fn,
            linear_fn=linear_fn,
            mlp_fn=mlp_fn,
        )

    return sampler


# ========== Evaluation ==========

def evaluate_policy(
    agent_state: FREAgentState,
    env_name: str,
    env_config: Dict,
    eval_reward_fn: Callable,
    eval_goal_params: Optional[np.ndarray] = None,
    num_episodes: int = 20,
    K_encode: int = 32,
    seed: int = 0,
) -> Dict[str, float]:
    """
    Evaluate trained FRE policy on a specific downstream task.

    Steps:
        1. Sample K=32 states from the environment/dataset
        2. Compute rewards for those states using the eval reward function
        3. Encode (state, reward) pairs -> z_eval via frozen encoder
        4. Execute pi(a | s, z_eval) for num_episodes episodes
        5. Report mean return and success rate

    Args:
        agent_state: trained FREAgentState
        env_name: environment name for gym.make()
        env_config: environment configuration dict
        eval_reward_fn: the downstream reward function to evaluate on
        eval_goal_params: reward function params for encoding
        num_episodes: number of evaluation episodes (default 20)
        K_encode: number of encoder context pairs (default 32)
        seed: random seed

    Returns:
        dict with "mean_return", "success_rate", "episode_returns"
    """
    import gym

    # Create environment
    if env_name.startswith("exorl-"):
        # ExORL uses DMControl suite
        domain = env_config["dataset_name"].split("-")[0]
        from dm_control import suite
        env = suite.load(domain, "run" if domain == "cheetah" else "walk")
    else:
        env = gym.make(env_name)

    fre_net = agent_state.fre_network
    params = agent_state.params
    rng = jax.random.PRNGKey(seed)

    # Sample K random states from dataset for encoding context
    # In practice, we would use states sampled from the environment
    # For offline evaluation, we use dataset states
    rng, enc_rng = jax.random.split(rng)

    episode_returns = []
    successes = []

    for ep in range(num_episodes):
        rng, ep_rng = jax.random.split(rng)

        if env_name.startswith("exorl-"):
            timestep = env.reset()
            obs = np.concatenate([v.flatten() for v in timestep.observation.values()])
        else:
            obs = env.reset()

        # Sample K encoding states from the environment
        # At test time: run random policy briefly to collect K states
        enc_states = np.zeros((1, K_encode, env_config["obs_dim"]), dtype=np.float32)
        enc_states[0, 0] = obs

        # Collect K-1 more states via random actions
        temp_obs = obs.copy()
        for k in range(1, K_encode):
            if env_name.startswith("exorl-"):
                action_spec = env.action_spec()
                rand_act = np.random.uniform(
                    action_spec.minimum, action_spec.maximum,
                    size=action_spec.shape,
                )
                timestep = env.step(rand_act)
                temp_obs = np.concatenate([v.flatten() for v in timestep.observation.values()])
            else:
                rand_act = env.action_space.sample()
                temp_obs, _, done, _ = env.step(rand_act)
                if done:
                    if env_name.startswith("exorl-"):
                        timestep = env.reset()
                        temp_obs = np.concatenate([v.flatten() for v in timestep.observation.values()])
                    else:
                        temp_obs = env.reset()
            enc_states[0, k] = temp_obs

        # Compute rewards for encoding states using eval reward fn
        if eval_goal_params is not None:
            enc_pairs = eval_reward_fn.make_encoder_pairs_testing(
                eval_goal_params[np.newaxis], enc_states
            )
        else:
            # Compute rewards directly
            enc_rewards = np.zeros((1, K_encode), dtype=np.float32)
            for k in range(K_encode):
                enc_rewards[0, k] = eval_reward_fn(enc_states[0, k])
            enc_pairs = np.concatenate(
                [enc_states, enc_rewards[..., np.newaxis]], axis=-1
            )

        # Encode -> z_eval
        enc_pairs_jax = jnp.array(enc_pairs)
        mu_z, _ = fre_net.apply(params, enc_pairs_jax, method="get_transformer_encoding")
        z_eval = mu_z  # use mean (deterministic at eval time)

        # Reset environment for actual evaluation
        if env_name.startswith("exorl-"):
            timestep = env.reset()
            obs = np.concatenate([v.flatten() for v in timestep.observation.values()])
        else:
            obs = env.reset()

        episode_return = 0.0
        success = False

        for t in range(env_config["max_episode_steps"]):
            rng, act_rng = jax.random.split(rng)

            obs_jax = jnp.array(obs[np.newaxis])  # [1, obs_dim]

            # Sample action from policy
            action = fre_net.apply(
                params, z_eval, obs_jax, act_rng,
                temperature=0.0,  # deterministic at eval
                method="sample_action",
            )
            action = np.array(action[0])  # [act_dim]

            # Clip action to valid range
            if not env_name.startswith("exorl-"):
                action = np.clip(action, env.action_space.low, env.action_space.high)

            # Step environment
            if env_name.startswith("exorl-"):
                timestep = env.step(action)
                next_obs = np.concatenate([v.flatten() for v in timestep.observation.values()])
                # Compute reward using eval reward fn
                if callable(eval_reward_fn) and not hasattr(eval_reward_fn, "compute_reward"):
                    reward = eval_reward_fn(next_obs)
                else:
                    reward = eval_reward_fn.compute_reward(
                        next_obs[np.newaxis], eval_goal_params
                    )[0] if eval_goal_params is not None else 0.0
                done = timestep.last()
            else:
                next_obs, reward, done, info = env.step(action)
                # For AntMaze: check if goal is reached
                if "antmaze" in env_name and info.get("success", False):
                    success = True

            episode_return += reward
            obs = next_obs

            if done:
                break

        episode_returns.append(episode_return)
        successes.append(float(success))

    results = {
        "mean_return": float(np.mean(episode_returns)),
        "std_return": float(np.std(episode_returns)),
        "success_rate": float(np.mean(successes)) if successes else 0.0,
        "episode_returns": [float(r) for r in episode_returns],
        "num_episodes": num_episodes,
    }

    return results


# ========== Main ==========

def main():
    parser = argparse.ArgumentParser(description="FRE Training Script")
    parser.add_argument(
        "--env", type=str, default="antmaze-large-diverse-v2",
        choices=list(ENV_CONFIGS.keys()),
        help="Environment name",
    )
    parser.add_argument("--seed", type=int, default=0, help="Random seed")
    parser.add_argument("--lr", type=float, default=1e-4, help="Learning rate")
    parser.add_argument("--batch_size", type=int, default=512, help="Batch size")
    parser.add_argument("--gamma", type=float, default=0.88, help="Discount factor")
    parser.add_argument("--tau_expectile", type=float, default=0.8, help="IQL expectile")
    parser.add_argument("--beta_awr", type=float, default=3.0, help="AWR temperature")
    parser.add_argument("--beta_kl", type=float, default=0.01, help="KL weight")
    parser.add_argument("--target_update", type=float, default=0.001, help="Target update rate")
    parser.add_argument("--latent_dim", type=int, default=128, help="Latent z dimension")
    parser.add_argument("--K_encode", type=int, default=32, help="Encoder pairs K")
    parser.add_argument("--K_decode", type=int, default=8, help="Decoder pairs K'")
    parser.add_argument("--eval_episodes", type=int, default=20, help="Evaluation episodes")
    parser.add_argument("--eval_seeds", type=int, default=5, help="Number of eval seeds")
    parser.add_argument("--log_interval", type=int, default=1000, help="Logging interval")
    parser.add_argument("--save_dir", type=str, default="results", help="Save directory")
    parser.add_argument("--data_dir", type=str, default="data", help="Dataset directory")
    parser.add_argument(
        "--encoder_steps", type=int, default=None,
        help="Override encoder training steps (default: env-specific)",
    )
    parser.add_argument(
        "--policy_steps", type=int, default=None,
        help="Override policy training steps (default: env-specific)",
    )
    parser.add_argument(
        "--reward_prior", type=str, default="all",
        choices=["all", "goals", "linear", "mlp", "lin-mlp", "goal-mlp", "goal-lin"],
        help="Reward prior distribution variant",
    )

    args = parser.parse_args()

    # Set random seeds
    np.random.seed(args.seed)
    rng = jax.random.PRNGKey(args.seed)

    # Get environment config
    env_config = ENV_CONFIGS[args.env]
    obs_dim = env_config["obs_dim"]
    action_dim = env_config["action_dim"]

    encoder_steps = args.encoder_steps or env_config["encoder_steps"]
    policy_steps = args.policy_steps or env_config["policy_steps"]

    print(f"=" * 60)
    print(f"FRE Training: {args.env}")
    print(f"  Seed: {args.seed}")
    print(f"  Obs dim: {obs_dim}, Action dim: {action_dim}")
    print(f"  Encoder steps: {encoder_steps:,}, Policy steps: {policy_steps:,}")
    print(f"  lr={args.lr}, batch_size={args.batch_size}, gamma={args.gamma}")
    print(f"  tau={args.tau_expectile}, beta_awr={args.beta_awr}, beta_kl={args.beta_kl}")
    print(f"  Latent dim: {args.latent_dim}, K={args.K_encode}, K'={args.K_decode}")
    print(f"  Reward prior: {args.reward_prior}")
    print(f"=" * 60)

    # ── Load dataset ──
    print("\nLoading dataset...")
    t0 = time.time()
    dataset = load_dataset(args.env, args.data_dir)
    N = dataset["observations"].shape[0]
    print(f"  Loaded {N:,} transitions in {time.time() - t0:.1f}s")

    # ── Create reward sampler ──
    print("Creating reward sampler...")

    # Reward prior ratios based on variant
    ratio_map = {
        "all":      (1/3, 1/3, 1/3),
        "goals":    (1.0, 0.0, 0.0),
        "linear":   (0.0, 1.0, 0.0),
        "mlp":      (0.0, 0.0, 1.0),
        "lin-mlp":  (0.0, 0.5, 0.5),
        "goal-mlp": (0.5, 0.0, 0.5),
        "goal-lin": (0.5, 0.5, 0.0),
    }
    r_goal, r_linear, r_mlp = ratio_map[args.reward_prior]

    # Per-dimension std for ExORL normalization
    state_std = None
    if env_config["env_type"] in ("cheetah", "walker"):
        state_std = np.std(dataset["observations"], axis=0) + 1e-8

    goal_fn = GoalReachingRewardFunction(obs_dim=obs_dim, state_std=state_std)
    linear_fn = LinearRewardFunction(
        obs_dim=obs_dim,
        exclude_dims=env_config.get("exclude_xy_dims"),
    )
    mlp_fn = RandomRewardFunction(num_simplex=256, obs_len=obs_dim)

    def reward_sampler():
        return sample_reward_function(
            rew_ratio_goal=r_goal,
            rew_ratio_linear=r_linear,
            rew_ratio_mlp=r_mlp,
            goal_fn=goal_fn,
            linear_fn=linear_fn,
            mlp_fn=mlp_fn,
        )

    # ── Initialize agent ──
    print("Initializing FRE agent...")
    rng, init_rng = jax.random.split(rng)
    agent_state = create_learner(
        obs_dim=obs_dim,
        action_dim=action_dim,
        rng=init_rng,
        lr=args.lr,
        hidden_dims=(512, 512, 512),
        latent_dim=args.latent_dim,
        num_reward_bins=32,
        K_encode=args.K_encode,
        K_decode=args.K_decode,
    )

    # Count parameters
    param_count = sum(x.size for x in jax.tree.leaves(agent_state.params))
    print(f"  Total parameters: {param_count:,}")

    # ── Train ──
    print("\nStarting training...")
    t0 = time.time()

    agent_state = train_fre(
        dataset=dataset,
        reward_sampler=reward_sampler,
        agent_state=agent_state,
        warmup_steps=encoder_steps,
        policy_steps=policy_steps,
        batch_size=args.batch_size,
        reward_pairs_encode=args.K_encode,
        reward_pairs_decode=args.K_decode,
        kl_weight=args.beta_kl,
        discount=args.gamma,
        expectile=args.tau_expectile,
        temperature=args.beta_awr,
        target_update_rate=args.target_update,
        log_interval=args.log_interval,
    )

    train_time = time.time() - t0
    print(f"\nTraining completed in {train_time / 3600:.1f} hours")

    # ── Evaluate ──
    print(f"\nEvaluating across {args.eval_seeds} seeds, {args.eval_episodes} episodes each...")

    all_results = []
    for eval_seed in range(args.eval_seeds):
        print(f"\n  Eval seed {eval_seed}:")

        # Create a goal-reaching eval task (standard for AntMaze)
        if env_config["env_type"] == "antmaze":
            # Standard AntMaze goal: top-right corner
            goal_state = np.zeros(obs_dim, dtype=np.float32)
            goal_state[0] = 33.0  # target X
            goal_state[1] = 24.0  # target Y
            eval_goal_params = goal_state[np.newaxis]  # [1, obs_dim]

            results = evaluate_policy(
                agent_state=agent_state,
                env_name=args.env,
                env_config=env_config,
                eval_reward_fn=goal_fn,
                eval_goal_params=eval_goal_params,
                num_episodes=args.eval_episodes,
                K_encode=args.K_encode,
                seed=args.seed * 100 + eval_seed,
            )
        else:
            # For ExORL / Kitchen: evaluate with environment-provided reward
            results = evaluate_policy(
                agent_state=agent_state,
                env_name=args.env,
                env_config=env_config,
                eval_reward_fn=goal_fn,
                eval_goal_params=None,
                num_episodes=args.eval_episodes,
                K_encode=args.K_encode,
                seed=args.seed * 100 + eval_seed,
            )

        all_results.append(results)
        print(f"    Mean return: {results['mean_return']:.2f} +/- {results['std_return']:.2f}")
        if results["success_rate"] > 0:
            print(f"    Success rate: {results['success_rate']:.2%}")

    # Aggregate results across seeds
    mean_returns = [r["mean_return"] for r in all_results]
    aggregate = {
        "env": args.env,
        "seed": args.seed,
        "reward_prior": args.reward_prior,
        "encoder_steps": encoder_steps,
        "policy_steps": policy_steps,
        "train_time_hours": train_time / 3600,
        "mean_return": float(np.mean(mean_returns)),
        "std_return": float(np.std(mean_returns)),
        "per_seed_results": all_results,
        "hyperparameters": {
            "lr": args.lr,
            "batch_size": args.batch_size,
            "gamma": args.gamma,
            "tau_expectile": args.tau_expectile,
            "beta_awr": args.beta_awr,
            "beta_kl": args.beta_kl,
            "target_update": args.target_update,
            "latent_dim": args.latent_dim,
            "K_encode": args.K_encode,
            "K_decode": args.K_decode,
        },
    }

    # Save results
    os.makedirs(args.save_dir, exist_ok=True)
    results_path = os.path.join(
        args.save_dir,
        f"fre_{args.env}_seed{args.seed}_{args.reward_prior}.json",
    )
    with open(results_path, "w") as f:
        json.dump(aggregate, f, indent=2)

    print(f"\n{'=' * 60}")
    print(f"Final Results: {args.env} (seed={args.seed}, prior={args.reward_prior})")
    print(f"  Mean return: {aggregate['mean_return']:.2f} +/- {aggregate['std_return']:.2f}")
    print(f"  Training time: {train_time / 3600:.1f} hours")
    print(f"  Results saved to: {results_path}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
