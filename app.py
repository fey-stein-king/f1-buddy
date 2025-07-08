import streamlit as st

# Page navigation
st.set_page_config(page_title="F1 Buddy", page_icon="🏎️", layout="centered")
st.sidebar.title("💖 F1 Buddy")
page = st.sidebar.radio("Navigate", ["💬 Chat", "📺 Watch & Learn", "🧵 Reddit Trends", "🗺️ Track Explorer", "🏆 Driver of the Week", "🔮 F1 Astrology"])

# Main content router
if page == "💬 Chat":
    st.header("💬 Chat with F1 Buddy")
    st.info("Ask me anything about F1 and I’ll spill the tea 🏁💅")

elif page == "📺 Watch & Learn":
    st.header("📺 Watch Iconic F1 Moments")
    st.warning("Coming soon: auto YouTube fetch for crashes, comebacks & chaos.")

elif page == "🧵 Reddit Trends":
    st.header("🧵 What’s Hot on r/formula1")
    st.warning("Reddit memes and race day drama loading...")

elif page == "🗺️ Track Explorer":
    st.header("🗺️ Explore F1 Circuits")
    st.warning("Track maps and commentary coming next.")

elif page == "🏆 Driver of the Week":
    st.header("🏆 Your Weekly F1 Crush")
    st.warning("Live driver stats via Ergast API soon!")

elif page == "🔮 F1 Astrology":
    st.header("🔮 Who’s Your F1 Soulmate?")
    st.warning("Enter your zodiac sign and get matched with your grid bestie.")

