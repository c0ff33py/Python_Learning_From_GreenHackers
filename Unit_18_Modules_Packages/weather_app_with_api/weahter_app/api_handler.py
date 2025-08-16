import requests

def fetch_weeather(city, api_key):
    """Fethc weather data from Openweathermap API"""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    
    else:
        print("❌ Error fetching weather data: ", response.status_code)
        return None
    
        