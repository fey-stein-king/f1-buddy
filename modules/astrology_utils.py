def match_driver(sign):
    matches = {
        "Aries": {
            "Driver": "Charles Leclerc",
            "Description": "Bold, ambitious, and a total heartthrob 💘 — Charles matches your fearless fire energy 🔥."
        },
        "Taurus": {
            "Driver": "Fernando Alonso",
            "Description": "Loyal, reliable, and lowkey spicy 🌶️ — just like your earthy calm and luxury-loving vibe."
        },
        "Gemini": {
            "Driver": "Lando Norris",
            "Description": "Chatty, charming, meme lord material 😜 — you and Lando are a TikTok power couple waiting to happen."
        },
        "Cancer": {
            "Driver": "Sebastian Vettel",
            "Description": "Deep, emotional, and a softie behind the helmet 🥺 — Seb gets your protective, nurturing heart."
        },
        "Leo": {
            "Driver": "Lewis Hamilton",
            "Description": "All glam, all guts, always the moment ✨ — Leo queens and Lewis literally share the spotlight."
        },
        "Virgo": {
            "Driver": "George Russell",
            "Description": "Polished, precise, and clean cut 📐 — George is your spreadsheet-loving soulmate."
        },
        "Libra": {
            "Driver": "Carlos Sainz",
            "Description": "Flirty, fashionable, and ✨aesthetic✨ — Carlos balances your scales in style."
        },
        "Scorpio": {
            "Driver": "Max Verstappen",
            "Description": "Mysterious, intense, and totally unstoppable 🦂 — you both go full throttle or nothing."
        },
        "Sagittarius": {
            "Driver": "Daniel Ricciardo",
            "Description": "Free-spirited and always laughing 🤪 — Danny Ric is your chaotic good partner in crime."
        },
        "Capricorn": {
            "Driver": "Valtteri Bottas",
            "Description": "Disciplined, determined, and a touch dry 🧊 — Bottas matches your climb-to-the-top energy."
        },
        "Aquarius": {
            "Driver": "Pierre Gasly",
            "Description": "Unique, unpredictable, and lowkey weird in a hot way 🛸 — Pierre keeps your mind racing."
        },
        "Pisces": {
            "Driver": "Yuki Tsunoda",
            "Description": "Emotional but savage, sensitive but screams on team radio 🎙️ — your F1 anime boy fantasy."
        }
    }

    return matches.get(sign, None)
