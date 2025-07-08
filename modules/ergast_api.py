import requests

def get_top_driver():
    url = "https://ergast.com/api/f1/current/driverStandings.json"
    try:
        response = requests.get(url)
        data = response.json()
        driver_info = data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]
        driver = driver_info["Driver"]
        constructor = driver_info["Constructors"][0]

        return {
            "name": f"{driver['givenName']} {driver['familyName']}",
            "code": driver["code"],
            "dob": driver["dateOfBirth"],
            "nationality": driver["nationality"],
            "constructor": constructor["name"],
            "points": driver_info["points"],
            "position": driver_info["position"]
        }
    except Exception as e:
        print("Error fetching driver:", e)
        return None
