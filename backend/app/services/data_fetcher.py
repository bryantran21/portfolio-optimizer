import yfinance as yf
import pandas as pd
from typing import List

def fetch_price_data(tickers: List[str], period: str = "1y") -> pd.DataFrame:
    """
    Fetch adjusted closing prices for the given tickers using yfinance.
    Returns a DataFrame indexed by date with tickers as columns.
    Handles single or multiple tickers and missing data.
    """
    # Download data from Yahoo Finance
    data = yf.download(
        tickers,
        period=period,
        progress=False,
        group_by="ticker",
        auto_adjust=True
    )

    # Early exit if no data
    if data.empty:
        raise ValueError(f"No data returned for tickers: {tickers}")

    # Detect if the dataframe uses MultiIndex (multi-ticker)
    if isinstance(data.columns, pd.MultiIndex):
        # Try to extract 'Close' column for each ticker safely
        prices_list = []
        valid_tickers = []
        for t in tickers:
            if t in data.columns.levels[0]:
                if 'Close' in data[t].columns:
                    prices_list.append(data[t]['Close'])
                    valid_tickers.append(t)
        if not prices_list:
            raise ValueError(f"No 'Close' data found for tickers: {tickers}")
        prices = pd.concat(prices_list, axis=1)
        prices.columns = valid_tickers
    else:
        # Single ticker flat dataframe
        if 'Close' in data.columns:
            prices = data['Close'].to_frame(name=tickers[0])
        else:
            raise ValueError(f"No 'Close' data found for ticker: {tickers[0]}")

    # Drop rows where all tickers are NaN
    prices = prices.dropna(how='all')

    return prices

def compute_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Convert price data into daily percentage returns.
    """
    returns = prices.pct_change().dropna()
    return returns
