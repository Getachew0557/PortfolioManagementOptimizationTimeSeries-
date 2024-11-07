import pandas as pd

def preprocess_data(tsla_data, bnd_data, spy_data):
    """
    Perform data cleaning and preprocessing for Tesla, Vanguard Total Bond, and S&P 500 data.
    """
    # Preprocess TSLA data
    tsla_data.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    tsla_data = tsla_data.drop([0, 1])  # Drop the first two rows
    tsla_data['Date'] = pd.to_datetime(tsla_data['Date'], errors='coerce')  # Convert 'Date' to datetime
    tsla_data.set_index('Date', inplace=True)
    
    # Preprocess BND data
    bnd_data.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    bnd_data = bnd_data.drop([0, 1])  # Drop the first two rows
    bnd_data['Date'] = pd.to_datetime(bnd_data['Date'], errors='coerce')  # Convert 'Date' to datetime
    bnd_data.set_index('Date', inplace=True)
    
    # Preprocess SPY data
    spy_data.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    spy_data = spy_data.drop([0, 1])  # Drop the first two rows
    spy_data['Date'] = pd.to_datetime(spy_data['Date'], errors='coerce')  # Convert 'Date' to datetime
    spy_data.set_index('Date', inplace=True)

    print("tsla data", tsla_data.head())
    print("bnd data", bnd_data.head())
    print("spy data", spy_data.head())

    return tsla_data, bnd_data, spy_data
