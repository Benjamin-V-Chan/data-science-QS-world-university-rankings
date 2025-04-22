import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import joblib

if __name__ == '__main__':
    df = pd.read_csv(os.path.join('data','processed','processed_rankings.csv'))
    y = df['Overall_Score']
    X = df.drop(columns=['Overall_Score','Institution_Name','Location'])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    os.makedirs(os.path.join('outputs','models'), exist_ok=True)
    os.makedirs(os.path.join('outputs','tables'), exist_ok=True)

    # Linear Regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    preds_lr = lr.predict(X_test)
    lr_metrics = {
        'model': 'LinearRegression',
        'MAE': metrics.mean_absolute_error(y_test, preds_lr),
        'MSE': metrics.mean_squared_error(y_test, preds_lr),
        'R2': metrics.r2_score(y_test, preds_lr)
    }
    joblib.dump(lr, os.path.join('outputs','models','lr_model.pkl'))

