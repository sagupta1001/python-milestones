import requests
import json

def fetch_current_weather(city_name="Bengaluru"):
    api_key = "e96d74aae5b066b3ba76c6f79e255178"
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric")
    res_content = res.content.decode('utf-8')

    weather_data = json.loads(res_content)["weather"]
    main_data = json.loads(res_content)["main"]

    print(f"\n\nCurrent weather in {city_name} is: {weather_data[0]['description'].title()}. " +
            f"Temperature is {main_data['temp']} with a minimum of {main_data['temp_min']}. " +
            f"Feels like {main_data['feels_like']} with a humidity of {main_data['humidity']}.")

if __name__ == "__main__":
    print("This program will get the current weather of the city you choose")
    city_name = input("Enter the city name ")
    print(f"Fetching current weather for city {city_name} ... ")
    fetch_current_weather(city_name)