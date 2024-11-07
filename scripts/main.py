import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))

from load_data import load_data
from preprocessing import preprocess_data

def main():

    # Load data
    tsla_data, bnd_data, spy_data = load_data('../data/tsla_data.csv', '../data/bnd_data.csv', '../data/spy_data.csv')

    # Preprocess data
    tsla_data, bnd_data, spy_data = preprocess_data(tsla_data, bnd_data, spy_data)



if __name__ == "__main__":
    main() 