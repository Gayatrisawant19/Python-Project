import requests
import json

# Replace 'your_api_key_here' with your actual API key
API_KEY = 'your_api_key_here'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    # Construct the final API call URL
    request_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    
    # Make a GET request to the API
    response = requests.get(request_url)
    
    # Parse the JSON response
    data = response.json()
    
    if data['cod'] == 200:
        # Extract the necessary information
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        feels_like = main['feels_like']
        temp_min = main['temp_min']
        temp_max = main['temp_max']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']
        
        # Display the information
        print(f"Weather in {city_name}:")
        print(f"Description: {description}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Min Temperature: {temp_min}°C")
        print(f"Max Temperature: {temp_max}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
    else:
        # Display an error message if the city is not found
        print(f"City {city_name} not found.")

if __name__ == '__main__':
    # Get city name input from the user
    city_name = input("Enter city name: ")
    get_weather(city_name)
