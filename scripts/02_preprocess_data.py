# - import pandas, numpy
# - define clean_rank(series):
#     remove non‑digits (e.g. '=') and convert to int, coercing errors
# - define preprocess(df):
#     apply clean_rank to all rank columns
#     convert Overall_Score to float
#     compute rank_change = RANK_2024 - RANK_2025
#     drop rows missing Overall_Score
#     one‑hot encode categorical cols ['Region','SIZE','FOCUS','RES.','STATUS']
#     return processed DataFrame
# - in main:
#     load raw CSV
#     call preprocess
#     save to 'data/processed/processed_rankings.csv'
