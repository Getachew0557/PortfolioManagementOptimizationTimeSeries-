import os
import sys
import unittest
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))
from eda_analysis import plot_decomposition, plot_rolling_metrics, calculate_daily_returns, calculate_risk_metrics
from io import StringIO
import sys

from eda_analysis import plot_decomposition, plot_rolling_metrics, calculate_daily_returns, calculate_risk_metrics

class TestEDA(unittest.TestCase):
    def setUp(self):
        # Sample data to mimic stock price data
        self.sample_data = pd.DataFrame({
            'Date': pd.date_range(start='2022-01-01', periods=10, freq='D'),
            'Open': [10.0 + i*0.1 for i in range(10)],
            'High': [10.5 + i*0.1 for i in range(10)],
            'Low': [9.8 + i*0.1 for i in range(10)],
            'Close': [10.2 + i*0.1 for i in range(10)],
            'Adj Close': [10.1 + i*0.1 for i in range(10)],
            'Volume': [1000 + i*50 for i in range(10)]
        })
        self.sample_data.set_index('Date', inplace=True)
    
    def test_calculate_daily_returns(self):
        # Calculate daily returns and check if column is added
        result_data = calculate_daily_returns(self.sample_data.copy())
        self.assertIn('Daily Return', result_data.columns, "Daily Return column should be calculated and added.")
        self.assertTrue(pd.api.types.is_float_dtype(result_data['Daily Return']), "Daily returns should be of float type.")

    def test_calculate_risk_metrics(self):
        # Capture print output for VaR and Sharpe Ratio
        captured_output = StringIO()
        sys.stdout = captured_output
        calculate_risk_metrics(calculate_daily_returns(self.sample_data.copy()))
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Value at Risk", output, "Risk metrics should calculate Value at Risk.")
        self.assertIn("Sharpe Ratio", output, "Risk metrics should calculate Sharpe Ratio.")

    # def test_plot_decomposition(self):
    #     try:
    #         plot_decomposition(self.sample_data['Adj Close'])
    #         result = True
    #     except Exception as e:
    #         result = False
    #         print(f"Error: {e}")  # Log the error for debugging
    #     self.assertTrue(result, "Decomposition plot should be generated without errors.")


    def test_plot_rolling_metrics(self):
        try:
            plot_rolling_metrics(self.sample_data)
            result = True
        except Exception as e:
            result = False
        self.assertTrue(result, "Rolling metrics plot should be generated without errors.")

if __name__ == '__main__':
    unittest.main()