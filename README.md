Stock Market Data Analysis (Python)
Overview

This project analyzes historical stock market data using Python to compare the performance of major technology companies and the broader market. Using financial time-series data, the analysis calculates returns, measures volatility, and visualizes price trends.

The goal of the project is to demonstrate practical data analysis skills relevant to economics, finance, and data analyst roles.

Tools & Technologies

Python
Pandas (data analysis)
yfinance (financial market data)
Matplotlib (data visualization)
Jupyter Notebook

Stocks Analyzed

The analysis focuses on the following assets:

AAPL — Apple
MSFT — Microsoft
NVDA — NVIDIA
SPY — S&P 500 ETF (market benchmark)

The time period analyzed is:

2020 — 2025

Analysis Performed

The project performs several financial data analysis tasks:

• Download historical stock price data using the Yahoo Finance API
• Extract and store closing prices for each asset
• Calculate daily returns
• Calculate cumulative investment returns
• Measure stock volatility
• Generate visualizations to compare performance

Visualizations
Stock Price Trends

This chart shows how stock prices evolved over time.

Cumulative Returns

This chart compares how a $1 investment in each asset would have grown over the analyzed time period.

Volatility Comparison

Volatility measures the variability of returns and is commonly used as a proxy for investment risk.

Project Structure
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

data — stored financial dataset
images — generated charts and visualizations
notebook — exploratory analysis in Jupyter Notebook
src — Python script version of the analysis

Key Takeaways

The analysis shows how technology stocks have experienced strong growth over the selected time period while also exhibiting higher volatility compared to the broader market benchmark (SPY).

This project demonstrates how Python can be used to perform financial time-series analysis, data transformation, and visualization using publicly available market data.

Skills Demonstrated

Financial data analysis
Time-series analysis
Python data manipulation (pandas)
Financial return calculations
Data visualization with matplotlib
Project organization for reproducible analysis

Requirements

Install required libraries with:

pip install -r requirements.txt
Author

Nicholas Mackinnon
Economics Student — Data & Financial Analysis Portfolio
