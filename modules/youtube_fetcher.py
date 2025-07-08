from youtubesearchpython import VideosSearch

def get_youtube_videos(query, limit=5):
    try:
        results = VideosSearch(query + " F1", limit=limit).result()
        videos = []

        for video in results['result']:
            videos.append({
                'title': video['title'],
                'link': video['link'],
                'thumbnail': video['thumbnails'][0]['url'],
                'duration': video.get('duration'),
                'views': video.get('viewCount', {}).get('short'),
            })

        return videos
    except Exception as e:
        print("YouTube search error:", e)
        return []
