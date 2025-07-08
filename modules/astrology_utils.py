import pandas as pd

def match_driver(sign):
    try:
        df = pd.read_csv("data/zodiac_mappings.csv")
        match = df[df["Sign"].str.lower() == sign.lower()]
        if not match.empty:
            return match.iloc[0].to_dict()
        else:
            return None
    except Exception as e:
        print("Error matching zodiac:", e)
        return None
