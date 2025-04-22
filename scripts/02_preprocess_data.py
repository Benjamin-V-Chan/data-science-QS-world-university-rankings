import pandas as pd
import os

def clean_rank(series):
    return (series
            .astype(str)
            .str.extract(r'(\d+)', expand=False)
            .astype(float)
           )

def preprocess(df):
    rank_cols = [c for c in df.columns if 'Rank' in c or c.startswith('RANK_')]
    for col in rank_cols:
        df[col] = clean_rank(df[col])
    df['Overall_Score'] = pd.to_numeric(df['Overall_Score'], errors='coerce')
    df['RANK_CHANGE'] = df['RANK_2024'] - df['RANK_2025']
    df = df.dropna(subset=['Overall_Score'])
    cat_cols = ['Region', 'SIZE', 'FOCUS', 'RES.', 'STATUS']
    df = pd.get_dummies(df, columns=cat_cols, dummy_na=False)
    return df

if __name__ == '__main__':
    raw = pd.read_csv(os.path.join('data', 'processed', 'raw_rankings.csv'),
                      encoding='latin-1')
    proc = preprocess(raw)
    proc.to_csv(os.path.join('data', 'processed', 'processed_rankings.csv'),
                index=False)
