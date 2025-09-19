import os, requests
from datetime import datetime, time

API_KEY = os.getenv("ACCUWEATHER_KEY")

def get_location_key(city_name):
    url = "http://dataservice.accuweather.com/locations/v1/cities/search"
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

def get_hourly_weather(location_key, hours=12):
    url = f"http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{location_key}"
    params = {"apikey": API_KEY, "metric": "true"}
    r = requests.get(url, params=params)
    if r.status_code != 200:
        print("Error fetching weather:", r.text)
        return None
    return r.json()

def main():
    city = "Waltersdorf"
    loc_key = get_location_key(city)
    if not loc_key:
        return

    forecast = get_hourly_weather(loc_key)
    if not forecast:
        return

    start_time_str = "19:00"   
    start_time = datetime.strptime(start_time_str, "%H:%M").time()

    selected = []
    for f in forecast:
        dt = datetime.fromisoformat(f["DateTime"].replace("Z", "+00:00"))
        if dt.time().hour == start_time.hour and dt.time().minute == start_time.minute:
            idx = forecast.index(f)
            selected = forecast[idx:idx+4]  # next 4 hours
            break

    print(f"\nForecast from {start_time_str} for {city} (4h window):\n")
    for f in selected:
        time_str = datetime.fromisoformat(f["DateTime"].replace("Z", "+00:00")).strftime("%H:%M")
        temp = f["Temperature"]["Value"]
        rain = f["PrecipitationProbability"]
        phrase = f["IconPhrase"]
        print(f"{time_str} | {temp}°C | Rain: {rain}% | {phrase}")

if __name__ == "__main__":
    main()
