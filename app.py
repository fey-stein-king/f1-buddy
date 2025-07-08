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
        "🗺️ Track Explorer",
        "🏆 Driver of the Week",
        "🔮 F1 Astrology",
    ]
)

# 🌐 Page Content Loader
st.title(page)

if page == "💬 Chat with F1 Buddy":
    try:
        from modules.f1_chat import get_girly_response

        st.subheader("Ask me anything about Formula 1 💬")
        st.markdown("From DRS to Monaco drama, I’ve got you babe 💖")

        prompt = st.text_input("What's confusing you, queen?")
        if prompt:
            with st.spinner("Spilling the tea..."):
                answer = get_girly_response(prompt)
                st.success(answer)
    except Exception as e:
        st.error("There was an issue loading the chat module 😢")

elif page == "📺 Watch & Learn":
    try:
        from modules.youtube_fetcher import get_youtube_videos

        st.subheader("Iconic F1 Moments 🎥")
        st.markdown("Search iconic races, overtakes, crashes, or team radios. F1 drama? We’ve got the receipts 🧃")

        query = st.text_input("What do you want to watch?")
        if query:
            videos = get_youtube_videos(query)
            if videos:
                for video in videos:
                    st.image(video['thumbnail'], width=320)
                    st.markdown(f"**[{video['title']}]({video['link']})**")
                    st.caption(f"⏱ {video['duration']} — 👀 {video['views']}")
                    st.markdown("---")
            else:
                st.error("No videos found. Try something like 'Silverstone 2022'")
    except Exception as e:
        st.error("There was an issue fetching YouTube videos 😔")

elif page == "🗺️ Track Explorer":
    try:
        from modules.track_explorer import load_track_data

        st.subheader("Zoom Through the Circuits 🗺️")
        st.markdown("Pick a track and I’ll spill the tea 🫖 on laps, chaos, and vibes.")

        df = load_track_data()

        if not df.empty:
            track = st.selectbox("Choose a track:", df["Track"].tolist())
            info = df[df["Track"] == track].iloc[0]

            st.markdown(f"""
            ### 🏁 {track} Grand Prix
            - 📍 Country: **{info['Country']}**
            - 🔁 Laps: **{info['Laps']}**
            - 📏 Circuit Length: **{info['Length_km']} km**
            - 💬 Commentary: _{info['Commentary']}_
            """)
        else:
            st.error("Couldn't load track info right now 😢")
    except Exception as e:
        st.error("Error loading track data 🛠️")

elif page == "🏆 Driver of the Week":
    try:
        from modules.ergast_api import get_top_driver
        st.subheader("This Week’s Grid Crush 💘")
        driver = get_top_driver()

        if driver:
            st.markdown(f"""
            ### 🏎️ {driver['name']}  
            - Team: {driver['constructor']}  
            - Nationality: {driver['nationality']}  
            - Current Points: **{driver['points']}**  
            - Position in Standings: {driver['position']}  
            """)
            st.success(f"Totally crushing it right now 😍 {driver['name']} is giving major grid energy!")
        else:
            st.error("Couldn’t fetch the data, boo 😭 Try again later.")
    except Exception as e:
        st.error("Error loading driver stats 🏎️")

elif page == "🔮 F1 Astrology":
    try:
        from modules.astrology_utils import match_driver

        st.subheader("F1 Soulmate Matcher 🔮💖")
        st.markdown("Pick your zodiac and I’ll tell you who on the grid is *literally* your racing soulmate 🏎️✨")

        zodiac = st.selectbox("Choose your sign:", [
            "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
            "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
        ])

        if st.button("Reveal My F1 Soulmate 💘"):
            result = match_driver(zodiac)
            if result:
                st.success(f"💘 Your match: **{result['Driver']}**")
                st.markdown(f"_{result['Description']}_")
            else:
                st.error("Couldn't find a match... the stars are confused 💫")
    except Exception as e:
        st.error("Star maps broken 😭 Astrology module failed.")

st.markdown("---")
st.caption("Built with 💖 by yours lovingly OM")
