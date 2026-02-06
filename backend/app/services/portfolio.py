import numpy as np
import pandas as pd


TRADING_DAYS = 252


def portfolio_return(weights: np.ndarray, mean_returns: pd.Series) -> float:
    """
    Annualized expected portfolio return
    """
    return np.sum(mean_returns * weights) * TRADING_DAYS


def portfolio_volatility(
    weights: np.ndarray,
    cov_matrix: pd.DataFrame
) -> float:
    """
    Annualized portfolio volatility (std dev)
    """
    return np.sqrt(
        weights.T @ cov_matrix @ weights
    ) * np.sqrt(TRADING_DAYS)


def sharpe_ratio(
    weights: np.ndarray,
    mean_returns: pd.Series,
    cov_matrix: pd.DataFrame,
    risk_free_rate: float = 0.02
) -> float:
    """
    Portfolio Sharpe Ratio
    """
    ret = portfolio_return(weights, mean_returns)
    vol = portfolio_volatility(weights, cov_matrix)

    return (ret - risk_free_rate) / vol


def portfolio_performance(
    weights: np.ndarray,
    returns: pd.DataFrame
):
    """
    Convenience function returning key metrics together
    """

    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    ret = portfolio_return(weights, mean_returns)
    vol = portfolio_volatility(weights, cov_matrix)
    sharpe = (ret - 0.02) / vol

    return {
        "return": float(ret),
        "volatility": float(vol),
        "sharpe": float(sharpe)
    }
