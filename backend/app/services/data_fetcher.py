import yfinance as yf
import pandas as pd
from datetime import datetime


def fetch_price_data(
    tickers: list[str],
    start_date: str = "2020-01-01",
    end_date: str | None = None,
) -> pd.DataFrame:
    """
    Fetch adjusted closing prices for given tickers.
    Returns a DataFrame indexed by date.
    """

    if end_date is None:
        end_date = datetime.today().strftime("%Y-%m-%d")

    data = yf.download(
        tickers,
        start=start_date,
        end=end_date,
        progress=False
    )

    # Grab adjusted close prices
    if isinstance(data.columns, pd.MultiIndex):
        prices = data["Adj Close"]
    else:
        prices = data.rename(columns={"Adj Close": tickers[0]})

    # Clean missing data
    prices = prices.dropna()

    return prices


def compute_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Convert price data into daily log returns.
    """
    returns = (prices / prices.shift(1)).apply(lambda x: pd.Series(x)).applymap(lambda x: None if pd.isna(x) else x)
    returns = prices.pct_change().dropna()

    return returns
