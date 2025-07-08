import streamlit as st

# 🏁 Page Configuration
st.set_page_config(page_title="F1 Buddy 🏎️💖", layout="wide")

# 💖 Sidebar Navigation
st.sidebar.title("F1 Buddy")
st.sidebar.markdown("Your girly bestie for all things Formula 1 💅🏁")

page = st.sidebar.radio(
    "Navigate",
    [
        "💬 Chat with F1 Buddy",
        "📺 Watch & Learn",
        "🧵 Reddit Trends",
        "🗺️ Track Explorer",
        "🏆 Driver of the Week",
        "🔮 F1 Astrology",
    ]
)

# 🌐 Page Content Loader
st.title(page)

if page == "💬 Chat with F1 Buddy":
    st.subheader("Ask me anything about Formula 1 💬")
    st.markdown("I'm here to explain things like DRS, constructors, or why everyone is obsessed with Toto 😘")
    user_input = st.text_input("What do you wanna ask, boo?")
    if user_input:
        st.info("LLM response integration coming soon 👩‍💻✨")

elif page == "📺 Watch & Learn":
    st.subheader("Iconic F1 Videos 🎥")
    st.markdown("Coming soon: Search or pick from curated lists like 'Best Team Radios' or 'Monza 2021 Drama'.")

elif page == "🧵 Reddit Trends":
    st.subheader("Hot F1 Threads 🔥")
    st.markdown("We’ll pull memes, race reactions, and spicy takes from Reddit. Just wait till you see race day drama.")

elif page == "🗺️ Track Explorer":
    st.subheader("Zoom through the circuits 🗺️")
    st.markdown("Select any track and get its layout, chaos factor, and commentary. It’s like Tinder but for circuits 💅")

elif page == "🏆 Driver of the Week":
    st.subheader("This Week’s Grid Crush 💘")
    st.markdown("Real stats + fangirl vibes for one iconic driver. Stats will be pulled using the Ergast API soon!")

elif page == "🔮 F1 Astrology":
    st.subheader("Who’s your F1 soulmate? ✨")
    st.markdown("Enter your zodiac sign and I’ll match you with your perfect F1 boy 😍")

# Footer
st.markdown("---")
st.caption("Built with 💖 by your AI pit crew – Powered by Streamlit")
