import requests

def get_weather(city_name, lat, lon):
    """
    Fetches current temperature and wind speed from Open-Meteo API.
    Prints the result to the console.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "wind_speed_10m"],
        "temperature_unit": "celsius"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()

        data = response.json()
        current_temp = data['current']['temperature_2m']
        wind_speed = data['current']['wind_speed_10m']

        print(f"Successfully received weather data for {city_name}")
        print(f"Current Temperature: {current_temp}°C")
        print(f"Wind speed: {wind_speed} km/h\n")

    except requests.exceptions.RequestException as e:
        print(f"Connection Error for {city_name}: {e}")

if __name__ == "__main__":
    get_weather("Istanbul", 41.01, 28.97)
    get_weather("Ankara", 39.9199, 32.8543)