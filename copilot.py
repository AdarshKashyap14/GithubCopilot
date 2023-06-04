import requests
import json

def get_weather(city):
    api_key = "15735fd7fdb96e4058642a0e9455bb66"  # Replace with your OpenWeatherMap API key

    # Make a request to the OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)

    # Check if the API request was successful
    
    if response.status_code == 200:
        data = json.loads(response.text)

        # Extract relevant weather information from the API response
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_description = data['weather'][0]['description']

        # Print the weather information
        print(f"Weather forecast for {city}:")
        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Weather Description: {weather_description}")
    else:
        print("Failed to fetch weather data. Please try again.")

# Prompt the user for the city name
city_name = input("Enter the city name: ")

# Call the function to retrieve and display the weather forecast
get_weather(city_name)
