import numpy as np
import pandas as pd
from scipy.optimize import minimize

from app.services.portfolio import (
    portfolio_return,
    portfolio_volatility,
    sharpe_ratio
)


# -------------------------------------------------------
# Helper — constraint: weights sum to 1
# -------------------------------------------------------

def weight_constraint(weights):
    return np.sum(weights) - 1


def bounds(num_assets):
    return tuple((0, 1) for _ in range(num_assets))


# -------------------------------------------------------
# Max Sharpe Optimization
# -------------------------------------------------------

def maximize_sharpe(returns: pd.DataFrame):

    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    num_assets = len(mean_returns)

    init_guess = np.ones(num_assets) / num_assets

    constraints = ({'type': 'eq', 'fun': weight_constraint})
    bnds = bounds(num_assets)

    def neg_sharpe(weights):
        return -sharpe_ratio(weights, mean_returns, cov_matrix)

    result = minimize(
        neg_sharpe,
        init_guess,
        method='SLSQP',
        bounds=bnds,
        constraints=constraints
    )

    return result.x


# -------------------------------------------------------
# Minimum Volatility Optimization
# -------------------------------------------------------

def minimize_volatility(returns: pd.DataFrame):

    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    num_assets = len(mean_returns)
    init_guess = np.ones(num_assets) / num_assets

    constraints = ({'type': 'eq', 'fun': weight_constraint})
    bnds = bounds(num_assets)

    def vol(weights):
        return portfolio_volatility(weights, cov_matrix)

    result = minimize(
        vol,
        init_guess,
        method='SLSQP',
        bounds=bnds,
        constraints=constraints
    )

    return result.x


# -------------------------------------------------------
# Efficient Frontier
# -------------------------------------------------------

def efficient_frontier(returns: pd.DataFrame, points: int = 30):

    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    target_returns = np.linspace(
        mean_returns.min(),
        mean_returns.max(),
        points
    )

    num_assets = len(mean_returns)
    frontier = []

    bnds = bounds(num_assets)

    for target in target_returns:

        constraints = (
            {'type': 'eq', 'fun': weight_constraint},
            {
                'type': 'eq',
                'fun': lambda w, target=target:
                    portfolio_return(w, mean_returns) - target
            }
        )

        init_guess = np.ones(num_assets) / num_assets

        result = minimize(
            lambda w: portfolio_volatility(w, cov_matrix),
            init_guess,
            method='SLSQP',
            bounds=bnds,
            constraints=constraints
        )

        if result.success:
            vol = portfolio_volatility(result.x, cov_matrix)

            frontier.append({
                "return": float(target),
                "volatility": float(vol)
            })

    return frontier
