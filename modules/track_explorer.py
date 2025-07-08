import pandas as pd
import streamlit as st

@st.cache_data
def load_track_data():
    try:
        df = pd.read_csv("data/track_metadata.csv")
        return df
    except Exception as e:
        print("Error loading track data:", e)
        st.warning("Could not load CSV — using fallback data instead.")

        # Fallback default list
        data = [
            {
                "Track": "Monza",
                "Country": "Italy",
                "Laps": 53,
                "Length_km": 5.793,
                "Commentary": "Monza is all about speed, queen 👑 – it’s the Temple of Speed!"
            },
            {
                "Track": "Silverstone",
                "Country": "UK",
                "Laps": 52,
                "Length_km": 5.891,
                "Commentary": "Silverstone serves history and high drama – classic British baddie 🇬🇧"
            },
            {
                "Track": "Monaco",
                "Country": "Monaco",
                "Laps": 78,
                "Length_km": 3.337,
                "Commentary": "Glamour meets chaos 💅 – overtaking here is like finding a seat at fashion week"
            },
            {
                "Track": "Suzuka",
                "Country": "Japan",
                "Laps": 53,
                "Length_km": 5.807,
                "Commentary": "Technical queen! 🧠 Drivers *love* Suzuka for its flowing S-curves and thrills"
            }
        ]
        return pd.DataFrame(data)
