import requests

def get_top_driver():
    try:
        url = "https://ergast.com/api/f1/current/driverStandings.json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        standings = data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]
        driver = standings["Driver"]
        constructor = standings["Constructors"][0]

        return {
            "name": f"{driver['givenName']} {driver['familyName']}",
            "position": standings["position"],
            "points": standings["points"],
            "nationality": driver["nationality"],
            "constructor": constructor["name"]
        }

    except Exception as e:
        print(f"Error fetching top driver: {e}")
        return None
