"""
Evaluation Metrics for LCA-on-the-Line
Implements R², PEA, KEN, SPE correlation metrics and MAE.
Reference: Section 4, Appendix D.1 of LCA-on-the-Line paper.
"""
import numpy as np
from scipy import stats
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from typing import Tuple


def min_max_scale(x: np.ndarray) -> np.ndarray:
    """
    Apply min-max scaling to array to [0, 1].
    Used for LCA distance preprocessing before correlation/regression.
    
    Args:
        x: Input array (e.g., LCA distances, NOT already in [0,1])
    
    Returns:
        Scaled array in [0, 1]
    """
    x_min, x_max = x.min(), x.max()
    if x_max - x_min < 1e-10:
        return np.zeros_like(x)
    return (x - x_min) / (x_max - x_min)


def compute_r2(x: np.ndarray, y: np.ndarray, apply_scaling: bool = True) -> float:
    """
    Compute R² (coefficient of determination) between x (predictor) and y (target).
    
    R² = 1 - sum(y_i - f(x_i))² / sum(y_i - y_bar)²
    where f is a linear regression fit.
    
    Args:
        x: Predictor variable (ID metric: LCA distance or Top-1 accuracy), shape (n,)
        y: Target variable (OOD Top-1 or Top-5 accuracy), shape (n,)
        apply_scaling: If True, apply min-max scaling to x first
    
    Returns:
        R² value (absolute value taken)
    """
    if apply_scaling:
        x = min_max_scale(x)
    
    # Fit linear regression
    x_reshaped = x.reshape(-1, 1)
    reg = LinearRegression().fit(x_reshaped, y)
    y_pred = reg.predict(x_reshaped)
    
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    
    if ss_tot < 1e-10:
        return 0.0
    
    r2 = 1.0 - ss_res / ss_tot
    return abs(r2)


def compute_pea(x: np.ndarray, y: np.ndarray, apply_scaling: bool = True) -> float:
    """
    Compute Pearson correlation coefficient (PEA).
    
    r = sum((x_i - x_bar)(y_i - y_bar)) / sqrt(sum((x_i-x_bar)²) * sum((y_i-y_bar)²))
    
    Args:
        x: Predictor variable, shape (n,)
        y: Target variable, shape (n,)
        apply_scaling: If True, apply min-max scaling to x first
    
    Returns:
        Absolute Pearson correlation coefficient
    """
    if apply_scaling:
        x = min_max_scale(x)
    
    r, _ = stats.pearsonr(x, y)
    return abs(r)


def compute_ken(x: np.ndarray, y: np.ndarray, apply_scaling: bool = True) -> float:
    """
    Compute Kendall rank correlation coefficient (KEN = Kendall's tau).
    
    tau = (concordant - discordant) / (n*(n-1)/2)
    
    Args:
        x: Predictor variable, shape (n,)
        y: Target variable, shape (n,)
        apply_scaling: If True, apply min-max scaling to x first
    
    Returns:
        Absolute Kendall tau
    """
    if apply_scaling:
        x = min_max_scale(x)
    
    tau, _ = stats.kendalltau(x, y)
    return abs(tau)


def compute_spe(x: np.ndarray, y: np.ndarray, apply_scaling: bool = True) -> float:
    """
    Compute Spearman rank-order correlation coefficient (SPE).
    
    rho = 1 - 6 * sum(d_i²) / (n * (n²-1))
    where d_i is the rank difference between corresponding x_i and y_i.
    
    Args:
        x: Predictor variable, shape (n,)
        y: Target variable, shape (n,)
        apply_scaling: If True, apply min-max scaling to x first
    
    Returns:
        Absolute Spearman rho
    """
    if apply_scaling:
        x = min_max_scale(x)
    
    rho, _ = stats.spearmanr(x, y)
    return abs(rho)


def compute_mae(x: np.ndarray, y: np.ndarray, apply_scaling: bool = True) -> float:
    """
    Compute Mean Absolute Error (MAE) for linear regression prediction.
    
    Fits a linear model from x to y, then computes MAE of predictions.
    Used in Table 3 for OOD accuracy prediction error.
    
    Args:
        x: Predictor variable (ID metric), shape (n,)
        y: Target variable (OOD Top-1 accuracy), shape (n,)
        apply_scaling: If True, apply min-max scaling to x first
    
    Returns:
        MAE of linear regression predictions
    """
    if apply_scaling:
        x = min_max_scale(x)
    
    x_reshaped = x.reshape(-1, 1)
    reg = LinearRegression().fit(x_reshaped, y)
    y_pred = reg.predict(x_reshaped)
    
    return np.mean(np.abs(y - y_pred))


def compute_topk_accuracy(
    predictions: np.ndarray,  # shape: (n_samples, K) logits or probabilities
    targets: np.ndarray,      # shape: (n_samples,) ground truth class indices
    k: int = 1
) -> float:
    """
    Compute Top-K accuracy.
    
    Args:
        predictions: Logits or probabilities, shape (n_samples, K_classes)
        targets: Ground truth indices, shape (n_samples,)
        k: K for top-K accuracy (1 or 5)
    
    Returns:
        Top-K accuracy in [0, 1]
    """
    top_k_preds = np.argsort(predictions, axis=1)[:, -k:]  # (n_samples, k)
    correct = np.any(top_k_preds == targets[:, np.newaxis], axis=1)
    return float(correct.mean())


def compute_average_confidence(
    probs: np.ndarray  # shape: (n_samples, K_classes) softmax probabilities
) -> float:
    """
    Compute Average Confidence (AC) after temperature scaling.
    
    AC = (1/N) * sum_i max_j P(y_j | x_i)
    
    Args:
        probs: Predicted probability distributions, shape (n_samples, K)
    
    Returns:
        Average maximum class probability
    """
    return float(np.mean(np.max(probs, axis=1)))
