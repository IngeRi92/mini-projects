import requests


def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Kontrolli, kas API tagastas vea
        if data.get("cod") != 200:  # 200 tähendab edukat päringut
            error_msg = data.get("message", "Unknown error")
            print(f"Error: {error_msg}")
            return None

        return data
    except Exception as e:
        print(f"Network error: {e}")
        return None


# Kasutamine
API_KEY = "YOUR_API_KEY"  # Asenda OMA!! OpenWeatherMap API võtmega, ei mina ei jaga tasuta api võtmeid githubis
city = input("Enter city: ")

weather_data = get_weather(city, API_KEY)
if weather_data:
    print(f"Weather in {city}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Conditions: {weather_data['weather'][0]['description']}")
else:
    print("Failed to fetch weather data.")
