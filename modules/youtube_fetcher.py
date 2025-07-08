import requests
import streamlit as st

YOUTUBE_API_KEY = st.secrets.get("AIzaSyClo7zKjEcW7l4xXsFjKYOWPSDUQN0rJqs")
SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
VIDEO_URL = "https://www.googleapis.com/youtube/v3/videos"

def get_youtube_videos(query, max_results=5):
    try:
        # Search for videos matching the query
        search_params = {
            "key": YOUTUBE_API_KEY,
            "q": query,
            "part": "snippet",
            "type": "video",
            "maxResults": max_results
        }
        search_response = requests.get(SEARCH_URL, params=search_params).json()
        video_ids = [item["id"]["videoId"] for item in search_response.get("items", [])]

        if not video_ids:
            return []

        # Fetch video details
        video_params = {
            "key": YOUTUBE_API_KEY,
            "id": ",".join(video_ids),
            "part": "snippet,contentDetails,statistics"
        }
        video_response = requests.get(VIDEO_URL, params=video_params).json()

        results = []
        for item in video_response.get("items", []):
            video_id = item["id"]
            snippet = item["snippet"]
            stats = item["statistics"]
            thumbnail = snippet["thumbnails"]["medium"]["url"]
            title = snippet["title"]
            views = stats.get("viewCount", "0")
            duration = item["contentDetails"]["duration"]

            results.append({
                "title": title,
                "link": f"https://www.youtube.com/watch?v={video_id}",
                "thumbnail": thumbnail,
                "views": f"{int(views):,}",
                "duration": duration.replace("PT", "").lower()
            })

        return results

    except Exception as e:
        st.error(f"YouTube API error: {e}")
        return []
