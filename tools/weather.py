import requests

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": "YOUR_OWM_KEY", "units": "metric"}
    data = requests.get(url, params=params).json()
    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }
