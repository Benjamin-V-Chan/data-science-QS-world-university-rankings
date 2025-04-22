import pandas as pd
import os

if __name__ == '__main__':
    df = pd.read_csv(os.path.join('data', 'processed', 'processed_rankings.csv'))
    num_cols = df.select_dtypes(include=['float64','int64']).columns
    os.makedirs(os.path.join('outputs','tables'), exist_ok=True)
    df[num_cols].describe().to_csv(
        os.path.join('outputs','tables','summary_stats.csv')
    )
    corr = df[num_cols].corr()
    corr.to_csv(os.path.join('outputs','tables','correlation_matrix.csv'))
    region_avg = df.groupby('Region')['Overall_Score'].mean().sort_values(ascending=False)
    region_avg.to_csv(os.path.join('outputs','tables','avg_score_by_region.csv'))
    status_avg = df.groupby('STATUS')['Overall_Score'].mean().sort_values(ascending=False)
    status_avg.to_csv(os.path.join('outputs','tables','avg_score_by_status.csv'))
