import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))

from load_data import load_data
from preprocessing import preprocess_data
from eda import plot_decomposition, plot_rolling_metrics, calculate_daily_returns, calculate_risk_metrics, plot_closing_prices, plot_volatility

def main():

    # Load data
    tsla_data, bnd_data, spy_data = load_data('../data/tsla_data.csv', '../data/bnd_data.csv', '../data/spy_data.csv')

    # Preprocess data
    tsla_data, bnd_data, spy_data = preprocess_data(tsla_data, bnd_data, spy_data)

    # Perform EDA on TSLA data
    plot_decomposition(tsla_data)
    plot_rolling_metrics(tsla_data)
    calculate_daily_returns(tsla_data)
    calculate_risk_metrics(tsla_data)


if __name__ == "__main__":
    main() 