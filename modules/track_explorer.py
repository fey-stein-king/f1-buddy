import pandas as pd

def load_track_data():
    try:
        df = pd.read_csv("data/track_metadata.csv")
        return df
    except Exception as e:
        print("Error loading track data:", e)
        return pd.DataFrame()
