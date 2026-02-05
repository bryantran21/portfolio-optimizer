# Portfolio Optimization Lab
 
A quantitative finance tool for portfolio optimization and analysis. 
 
## Tech Stack 
 
**Backend:** Python, FastAPI, NumPy, Pandas, SciPy 
**Frontend:** React, Vite, Plotly.js 
**Data:** Yahoo Finance (yfinance) 
 
## Local Development 
 
### Backend 
```bash 
cd backend 
python -m venv venv 
venv\Scripts\activate  # On Windows 
pip install -r requirements.txt 
uvicorn app.main:app --reload 
``` 
 
### Frontend 
```bash 
cd frontend 
npm install 
npm run dev 
``` 
 
## Features 
 
- Historical price data fetching 
- Portfolio statistics calculation 
- Mean-variance optimization 
- Efficient frontier generation 
- Interactive visualizations 
