from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import data, optimization

app = FastAPI(title="Portfolio Optimization Lab")


# ----------------------------------------------------
# Enable frontend access
# ----------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # dev mode — open
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ----------------------------------------------------
# Register routers
# ----------------------------------------------------

app.include_router(data.router)
app.include_router(optimization.router)


@app.get("/")
def root():
    return {"message": "Portfolio Optimizer API running"}
