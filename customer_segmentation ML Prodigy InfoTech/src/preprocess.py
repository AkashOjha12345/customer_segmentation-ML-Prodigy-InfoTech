import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def select_features(df):
    # Selecting only important columns
    X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
    return X