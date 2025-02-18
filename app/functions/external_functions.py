import requests
from app.config import WEATHER_API_KEY

def get_weather_details(city, country_code):
    """Fetches weather details for a given city and country code."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={WEATHER_API_KEY}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        return {
            "temperature": main["temp"],
            "humidity": main["humidity"],
            "condition": weather["description"]
        }
    else:
        return {"error": "City not found or API error!"}
