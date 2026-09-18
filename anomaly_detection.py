import pandas as pd
from sklearn.ensemble import IsolationForest

def run_anomaly_detection(df):
    features = ['Average_Distance', 'Average_Speed', 'Last_Seen_Time']
    model = IsolationForest(contamination=0.05, random_state=42)
    df['Anomaly_Flag'] = model.fit_predict(df[features])
    # -1 indicates an anomalous pattern, 1 indicates normal
    return df