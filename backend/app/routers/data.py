from fastapi import APIRouter
from app.services.data_fetcher import fetch_price_data, compute_returns
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/data", tags=["Market Data"])


class PriceResponse(BaseModel):
    tickers: List[str]
    rows: int
    data: list[list[float]]


@router.get("/prices", response_model=PriceResponse)
def get_prices(tickers: str, period: str = "1y"):
    """
    Fetch price data for a list of tickers and a given period.
    """
    ticker_list = [t.strip().upper() for t in tickers.split(",")]
    df = fetch_price_data(ticker_list, period)

    return PriceResponse(
        tickers=ticker_list,
        rows=len(df),
        data=df.values.tolist()
    )
