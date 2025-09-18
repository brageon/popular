import os, requests

API_KEY = os.getenv("ACCUWEATHER_KEY")

def get_location_key(city_name):
    """Get AccuWeather location key from city name."""
    url = f"http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {"apikey": API_KEY, "q": city_name}
    r = requests.get(url, params=params)
    if r.status_code != 200:
        print("Error fetching location key:", r.text)
        return None
    data = r.json()
    if not data:
        print("No results for city:", city_name)
        return None
    return data[0]["Key"]

def get_hourly_weather(location_key, hours=4):
    """Get next hourly forecast (default 4h)."""
    url = f"http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{location_key}"
    params = {"apikey": API_KEY, "metric": "true"}
    r = requests.get(url, params=params)
    if r.status_code != 200:
        print("Error fetching weather:", r.text)
        return None
    data = r.json()
    return data[:hours]

def main():
    city = "Waltersdorf"
    loc_key = get_location_key(city)
    if not loc_key:
        return
    forecast = get_hourly_weather(loc_key, hours=4)
    if not forecast:
        return

    print(f"\nNext 4 hours forecast for {city}:\n")
    for f in forecast:
        time = f["DateTime"]
        temp = f["Temperature"]["Value"]
        rain = f["PrecipitationProbability"]
        phrase = f["IconPhrase"]
        print(f"{time} | {temp}°C | Rain: {rain}% | {phrase}")

if __name__ == "__main__":
    main()
