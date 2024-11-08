import os
import sys
import pytest
import unittest
import pandas as pd
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))

from preprocessing import preprocess_data

class TestPreprocessing(unittest.TestCase):
    def setUp(self):
        # Sample data to mimic stock data with missing values
        self.sample_data = pd.DataFrame({
            'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04'],
            'Open': [10.0, 10.5, 10.7, 10.8],
            'High': [10.5, 10.8, 10.7, 10.6],
            'Low': [9.8, 9.7, 10.0, 10.2],
            'Close': [10.2, 10.6, 10.5, 10.4],
            'Adj Close': [10.1, 10.4, 10.3, 10.2],
            'Volume': [1000, 1100, 1111, 1050]
        })
    
    def test_preprocess_data(self):
        # Pass the sample data through preprocessing and check for NaNs removal
        preprocessed_data, _, _ = preprocess_data(self.sample_data, self.sample_data, self.sample_data)
        
        # Check if missing values are removed
        self.assertFalse(preprocessed_data.isnull().values.any(), "NaN values should be removed.")
        
        # Check if 'Date' is in datetime format
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(preprocessed_data.index), "Date should be in datetime format.")

if __name__ == '__main__':
    unittest.main()
