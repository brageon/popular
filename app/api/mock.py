import os, random, requests, json

BASE_URL = "https://api.api-tennis.com/tennis/"
API_KEY = os.getenv("API_TENNIS_KEY")
DATE = "2025-09-18"

def get_fixtures():
    url = f"{BASE_URL}?method=get_fixtures&APIkey={API_KEY}&date_start={DATE}&date_stop={DATE}"
    resp = requests.get(url).json()
    return resp.get("result", [])

def extract_odds(match_data):
    home_away = match_data.get("Home/Away", {})
    if not home_away:
        return {}
    home = home_away.get("Home", {}).get("1xBet")
    away = home_away.get("Away", {}).get("1xBet")
    return {"home": home, "away": away}

def fetch_odds(event_key):
    url = f"{BASE_URL}?method=get_odds&match_key={event_key}&APIkey={API_KEY}"
    resp = requests.get(url).json()

    match_data = resp.get("result", {}).get(str(event_key), {})
    odds = extract_odds(match_data)
    return odds


if __name__ == "__main__":
    fixtures = get_fixtures()
    sample_fixtures = random.sample(fixtures, min(5, len(fixtures)))
    for fx in sample_fixtures:
        match_key = fx.get("event_key")
        if match_key:
            odds = fetch_odds(match_key)
            if odds:
                print({"Home/Away": {"home": odds["home"], "away": odds["away"]}})
