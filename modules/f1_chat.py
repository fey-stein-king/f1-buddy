import requests
import streamlit as st

# ⚠️ Replace with your OpenRouter or HuggingFace endpoint + key
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = st.secrets["OPENROUTER_KEY"]

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_girly_response(user_prompt):
    payload = {
        "model": "nous-hermes-2-mixtral",  # or mixtral-8x7b, llama-3-70b
        "messages": [
            {"role": "system", "content": "You're a fun, girly F1 assistant who uses slang, emojis and explains F1 concepts to total beginners."},
            {"role": "user", "content": user_prompt}
        ]
    }

    try:
        res = requests.post(API_URL, headers=headers, json=payload)
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return "Oops! I stalled 😭 Try again later, queen."
