import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

def weather_score(forecast):

    score = 100

    for day in forecast:
        rain = int(day["rain_chance"])

        if rain >= 80:
            score -= 20
        elif rain >= 60:
            score -= 10
        elif rain >= 40:
            score -= 5

    return max(score, 0)


def get_weather(destination):

    url = (
        f"http://api.weatherapi.com/v1/forecast.json"
        f"?key={API_KEY}"
        f"&q={destination}"
        f"&days=3"
    )

    data = requests.get(url).json()

    forecast = []

    for day in data["forecast"]["forecastday"]:
        forecast.append({
            "date": day["date"],
            "avg_temp": day["day"]["avgtemp_c"],
            "condition": day["day"]["condition"]["text"],
            "rain_chance": day["day"]["daily_chance_of_rain"]
        })

    return {
        "destination": destination,
        "weather_score": weather_score(forecast),
        "forecast": forecast
    }