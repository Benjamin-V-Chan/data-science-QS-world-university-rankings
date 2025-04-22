import pandas as pd
import os

def load_data(path):
    return pd.read_csv(path, encoding='latin-1')

if __name__ == '__main__':
    raw_path = os.path.join('data', 'raw', 'qs_rankings_2025.csv')
    df = load_data(raw_path)
    os.makedirs(os.path.join('data', 'processed'), exist_ok=True)
    df.to_csv(os.path.join('data', 'processed', 'raw_rankings.csv'), index=False)
