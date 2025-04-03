from typing import Dict, Any
from ...state import AgentState
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY") # Get API key from .env

def get_weather(state: AgentState) -> Dict[str, Any]:
    print("---GETTING WEATHER---")
    destinations = state["destinations"]
    weather_info = {}
    for dest in destinations:
        city_name = dest["name"]
        #  Replace with your API endpoint and key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_API_KEY}&units=metric"  # Use metric units
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()
            weather_info[city_name] = f"{data['weather'][0]['description']}, {data['main']['temp']}°C"
        except requests.exceptions.RequestException as e:
            weather_info[city_name] = f"Could not retrieve weather for {city_name} ({e})"
        except KeyError:
            weather_info[city_name] = f"Could not parse weather data for {city_name}"

    print("Weather Info:", weather_info)
    return {"weather": weather_info}