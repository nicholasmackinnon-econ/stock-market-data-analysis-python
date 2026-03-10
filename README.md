# Stock Market Data Analysis (Python)

## Overview

This project analyzes historical stock market data using Python to compare the performance of major technology companies and the broader market. Using financial time-series data, the analysis calculates returns, measures volatility, and visualizes price trends.

The goal of the project is to demonstrate practical data analysis skills relevant to economics, finance, and data analyst roles.

---

## Tools & Technologies

- Python
- Pandas
- yfinance
- Matplotlib
- Jupyter Notebook

---

## Stocks Analyzed

The analysis focuses on the following assets:

- AAPL — Apple
- MSFT — Microsoft
- NVDA — NVIDIA
- SPY — S&P 500 ETF (market benchmark)

Time period analyzed:

2020 – 2025

---

## Analysis Performed

The project performs several financial data analysis tasks:

- Download historical stock price data using Yahoo Finance
- Extract closing prices for each asset
- Calculate daily returns
- Calculate cumulative returns
- Measure stock volatility
- Generate charts to compare performance

---

## Visualizations

### Stock Price Trends

![Stock Prices](images/stock_prices.png)

### Cumulative Returns

![Cumulative Returns](images/cumulative_returns.png)

### Volatility Comparison

![Volatility](images/volatility.png)

---

## Project Structure

```
stock-market-data-analysis-python
│
├── data
│   └── stock_data.csv
│
├── images
│   ├── stock_prices.png
│   ├── cumulative_returns.png
│   └── volatility.png
│
├── notebook
│   └── stock_market_analysis.ipynb
│
├── src
│   └── analysis.py
│
└── requirements.txt
```

---

## Key Takeaways

Technology stocks experienced strong growth during the selected period but also exhibited higher volatility compared with the broader market benchmark (SPY). This project demonstrates how Python can be used for financial time-series analysis and visualization using publicly available market data.

---

## Skills Demonstrated

- Financial data analysis
- Time-series analysis
- Python data manipulation (pandas)
- Financial return calculations
- Data visualization with matplotlib
- Project organization and reproducible analysis

---

## Requirements

Install required libraries with:

```
pip install -r requirements.txt
```

---

## Author

Nicholas Mackinnon  
Economics Student — Data & Financial Analysis Portfolio
