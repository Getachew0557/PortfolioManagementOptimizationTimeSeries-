# Time Series Forecasting for Portfolio Management Optimization

This repository provides a solution for time series forecasting of financial assets using ARIMA, SARIMA, and LSTM models. The goal is to predict market trends and optimize portfolio performance for GMF Investments, improving decision-making and risk management.

# Business Need
GMF Investments aims to enhance portfolio management by leveraging predictive analytics, optimizing asset allocations, and minimizing risks through accurate market forecasting.

# Objective
- **Data Preprocessing**: Clean and analyze historical financial data from assets like TSLA, BND, and SPY.
- **Time Series Forecasting**: Implement ARIMA, SARIMA, and LSTM models.
- **Portfolio Optimization**: Use forecasts to adjust portfolio allocations for better returns and risk management.

# Data
Use historical financial data for three key assets: Tesla (TSLA) Historical stock prices (Open, High, Low, Close), volume, and volatility., Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY). The data will be sourced from YFinance and cover the period from January 1, 2015, to December 31, 2024.


# Setup
- Clone this repository:

```bash
git clone https://github.com/Getachew0557/PortfolioManagementOptimizationTimeSeries-.git
```
- Install Dependencies
```bash
pip install -r requirements.txt
```

# Files
- `data/`: Contains raw and processed data for analysis.
- `models/`: Includes the forecasting models (ARIMA, SARIMA, LSTM).
- `notebooks/`: Jupyter notebooks for EDA, model implementation, and optimization results.
- `requirements.txt`: Lists required Python packages.

# License
Apache2 License.