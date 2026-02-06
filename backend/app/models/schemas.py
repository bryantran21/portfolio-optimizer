from pydantic import BaseModel, Field
from typing import List, Optional


# ===============================
# Request Models
# ===============================

class PortfolioRequest(BaseModel):
    tickers: List[str] = Field(..., example=["AAPL", "MSFT", "GOOGL"])
    weights: Optional[List[float]] = Field(
        None,
        example=[0.33, 0.33, 0.34],
        description="Optional portfolio weights"
    )
    start_date: Optional[str] = Field(
        "2020-01-01",
        example="2020-01-01"
    )
    end_date: Optional[str] = Field(
        None,
        example="2024-01-01"
    )


class OptimizationRequest(BaseModel):
    tickers: List[str]
    start_date: Optional[str] = "2020-01-01"
    end_date: Optional[str] = None
    risk_free_rate: Optional[float] = 0.02


# ===============================
# Response Models
# ===============================

class PortfolioStats(BaseModel):
    expected_return: float
    volatility: float
    sharpe_ratio: float


class OptimizationResult(BaseModel):
    optimal_weights: List[float]
    expected_return: float
    volatility: float
    sharpe_ratio: float
