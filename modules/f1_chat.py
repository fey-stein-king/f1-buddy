import requests
import streamlit as st

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = st.secrets.get("OPENROUTER_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_girly_response(user_prompt):
    payload = {
       "model": "mistralai/mistral-small-3.2-24b-instruct:free",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You're an upbeat, girly F1 expert. "
                    "Use emojis, Gen-Z slang, and explain like you're talking to your bestie "
                    "who's new to the sport 💖🏁"
                )
            },
            {"role": "user", "content": user_prompt}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            st.warning(f"API error: {response.status_code} – {response.text}")
            return "Ugh, OpenRouter just red flagged us 🟥 Try again later, queen."

        data = response.json()
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        st.error(f"Technical error: {e}")
        return "Oops! I stalled 😭 Try again later, queen."
