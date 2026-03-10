import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT", "NVDA", "SPY"]

start_date = "2020-01-01"
end_date = "2025-01-01"

data = yf.download(tickers, start=start_date, end=end_date)

prices = data["Close"]

daily_returns = prices.pct_change().dropna()

cumulative_returns = (1 + daily_returns).cumprod() - 1

print(cumulative_returns.tail())
