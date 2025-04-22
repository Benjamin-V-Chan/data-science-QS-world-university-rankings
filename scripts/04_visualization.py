import pandas as pd
import matplotlib.pyplot as plt
import os

def save_fig(fig, name):
    fig.savefig(os.path.join('outputs','figures', name), bbox_inches='tight')
    plt.close(fig)

if __name__ == '__main__':
    df = pd.read_csv(os.path.join('data', 'processed', 'processed_rankings.csv'))
    os.makedirs(os.path.join('outputs','figures'), exist_ok=True)
    
    # histogram
    fig = plt.figure()
    df['Overall_Score'].hist(bins=30)
    plt.title('Distribution of Overall Score')
    save_fig(fig, 'hist_overall_score.png')
    
    # top 10 bar
    top10 = df.nlargest(10, 'Overall_Score')
    fig = plt.figure()
    plt.barh(top10['Institution_Name'], top10['Overall_Score'])
    plt.gca().invert_yaxis()
    plt.xlabel('Overall Score')
    plt.title('Top 10 Universities by Overall Score')
    save_fig(fig, 'bar_top10.png')
    
    # scatter
    fig = plt.figure()
    plt.scatter(df['Academic_Reputation_Score'], df['Overall_Score'], alpha=0.6)
    plt.xlabel('Academic Reputation Score')
    plt.ylabel('Overall Score')
    plt.title('Overall vs Academic Reputation')
    save_fig(fig, 'scatter_academic_vs_overall.png')
    
    # boxplot (limit to 5 largest regions)
    top_regions = df['Region'].value_counts().nlargest(5).index
    data = [df[df['Region']==r]['Overall_Score'] for r in top_regions]
    fig = plt.figure()
    plt.boxplot(data, labels=top_regions)
    plt.xticks(rotation=45, ha='right')
    plt.title('Overall Score by Region (Top 5)')
    save_fig(fig, 'box_by_region.png')
