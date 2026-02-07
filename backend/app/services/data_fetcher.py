import yfinance as yf
import pandas as pd


def fetch_price_data(tickers: list[str], period: str = "1y") -> pd.DataFrame:
    """
    Fetch adjusted closing prices for given tickers using yfinance.
    Returns a DataFrame indexed by date.
    Supports periods like '1y', '6mo', '1mo', etc.
    """

    # Download data
    data = yf.download(
        tickers,
        period=period,
        progress=False,
        group_by="ticker",  # ensures MultiIndex if multiple tickers
        auto_adjust=True    # adjusted close prices
    )

    # Handle single ticker vs multiple tickers
    if len(tickers) == 1:
        prices = data["Close"].to_frame(name=tickers[0])
    else:
        # Multi-ticker: get 'Close' column for each ticker
        prices = pd.concat([data[t]["Close"] for t in tickers], axis=1)
        prices.columns = tickers

    # Drop rows where all tickers are NaN
    prices = prices.dropna(how="all")

    return prices


def compute_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Convert price data into daily percentage returns.
    """
    returns = prices.pct_change().dropna()
    return returns
