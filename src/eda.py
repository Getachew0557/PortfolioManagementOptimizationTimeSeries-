import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import pandas as pd

def plot_decomposition(tsla_data):
    """
    Decompose Tesla's stock price into trend, seasonal, and residual components.
    """
    decomposition = sm.tsa.seasonal_decompose(tsla_data['Adj Close'], model='multiplicative', period=252)
    decomposition.plot()
    plt.show()

def plot_rolling_metrics(tsla_data):
    """
    Plot the rolling mean and rolling standard deviation of Tesla's stock price.
    """
    tsla_data['Rolling Mean'] = tsla_data['Adj Close'].rolling(window=30).mean()
    tsla_data['Rolling Std'] = tsla_data['Adj Close'].rolling(window=30).std()

    plt.figure(figsize=(10, 6))
    plt.plot(tsla_data['Rolling Mean'], label='30-Day Rolling Mean', color='blue')
    plt.plot(tsla_data['Rolling Std'], label='30-Day Rolling Std', color='orange')
    plt.title('Rolling Mean and Standard Deviation of TSLA Closing Prices')
    plt.legend()
    plt.show()

def calculate_daily_returns(data):
    data['Adj Close'] = pd.to_numeric(data['Adj Close'], errors='coerce')
    data['Daily Return'] = data['Adj Close'].pct_change() * 100
    return data

def calculate_risk_metrics(tsla_data):
    """
    Calculate Value at Risk (VaR) and Sharpe Ratio for Tesla's stock price.
    """
    # Value at Risk (VaR) - 1-day 99% confidence level (using historical simulation)
    VaR = tsla_data['Daily Return'].quantile(0.01)
    print(f"1-day Value at Risk (99% Confidence): {VaR}%")
    
    # Sharpe Ratio (assuming risk-free rate = 0%)
    mean_daily_return = tsla_data['Daily Return'].mean()
    std_daily_return = tsla_data['Daily Return'].std()
    sharpe_ratio = mean_daily_return / std_daily_return
    print(f"Sharpe Ratio: {sharpe_ratio}")

def plot_closing_prices(spy_data, bnd_data, tsla_data):
    plt.figure(figsize=(10, 6))
    plt.plot(spy_data['Date'], spy_data['Adj Close'], label='SPY Close Price', color='blue')
    plt.plot(bnd_data['Date'], bnd_data['Adj Close'], label='BND Close Price', color='green')
    plt.plot(tsla_data['Date'], tsla_data['Adj Close'], label='TSLA Close Price', color='red')
    plt.title('Adj Close Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Adj Close Price')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()


def plot_volatility(spy_data, bnd_data, tsla_data):
    for data in [spy_data, bnd_data, tsla_data]:
        data['Pct Change'] = data['Adj Close'].pct_change() * 100
        data['Rolling Mean'] = data['Pct Change'].rolling(window=21).mean()
        data['Rolling Std'] = data['Pct Change'].rolling(window=21).std()

    plt.figure(figsize=(10, 6))
    # SPY
    plt.plot(spy_data['Date'], spy_data['Pct Change'], label='SPY Daily Change', color='blue')
    plt.plot(spy_data['Date'], spy_data['Rolling Mean'], label='SPY Rolling Mean', color='cyan', linestyle='--')
    plt.plot(spy_data['Date'], spy_data['Rolling Std'], label='SPY Rolling Std', color='blue', linestyle=':')
    # BND
    plt.plot(bnd_data['Date'], bnd_data['Pct Change'], label='BND Daily Change', color='green')
    plt.plot(bnd_data['Date'], bnd_data['Rolling Mean'], label='BND Rolling Mean', color='lime', linestyle='--')
    plt.plot(bnd_data['Date'], bnd_data['Rolling Std'], label='BND Rolling Std', color='green', linestyle=':')
    # TSLA
    plt.plot(tsla_data['Date'], tsla_data['Pct Change'], label='TSLA Daily Change', color='red')
    plt.plot(tsla_data['Date'], tsla_data['Rolling Mean'], label='TSLA Rolling Mean', color='pink', linestyle='--')
    plt.plot(tsla_data['Date'], tsla_data['Rolling Std'], label='TSLA Rolling Std', color='red', linestyle=':')

    plt.title('Daily Percentage Change and Volatility')
    plt.xlabel('Date')
    plt.ylabel('Percentage Change (%)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()
