import pandas as pd

def load_data(tsla_path, bnd_path, spy_path):
    """
    Load the Tesla (TSLA), Vanguard Total Bond (BND), and S&P 500 (SPY) data from CSV files.
    """
    tsla_data = pd.read_csv(tsla_path)
    bnd_data = pd.read_csv(bnd_path)
    spy_data = pd.read_csv(spy_path)
    
    return tsla_data, bnd_data, spy_data
