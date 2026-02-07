from fastapi import APIRouter
from app.services.data_fetcher import compute_returns, fetch_price_data
from app.services.optimizer import (
    maximize_sharpe,
    minimize_volatility,
    efficient_frontier
)

router = APIRouter(prefix="/optimize", tags=["Optimization"])


# ----------------------------------------------------
# Max Sharpe Portfolio
# ----------------------------------------------------

@router.get("/max-sharpe")
def max_sharpe(tickers: str, period: str = "1y"):

    ticker_list = [t.strip().upper() for t in tickers.split(",")]

    prices = fetch_price_data(ticker_list, period)
    returns = compute_returns(prices)
    weights = maximize_sharpe(returns)

    return dict(zip(ticker_list, weights.tolist()))


# ----------------------------------------------------
# Minimum Volatility
# ----------------------------------------------------

@router.get("/min-vol")
def min_vol(tickers: str, period: str = "1y"):

    ticker_list = [t.strip().upper() for t in tickers.split(",")]

    prices = fetch_price_data(ticker_list, period)
    returns = compute_returns(prices)
    weights = minimize_volatility(returns)

    return dict(zip(ticker_list, weights.tolist()))


# ----------------------------------------------------
# Efficient Frontier
# ----------------------------------------------------

@router.get("/frontier")
def frontier(tickers: str, period: str = "1y"):

    ticker_list = [t.strip().upper() for t in tickers.split(",")]

    prices = fetch_price_data(ticker_list, period)
    returns = compute_returns(prices)
    frontier_data = efficient_frontier(returns)

    return frontier_data
