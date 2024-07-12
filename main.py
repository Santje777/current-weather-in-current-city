def display_city_and_temperature():
    city = input("Enter a name of a city:")
    temperature = input(f"What is the current temperature of {city}? (in Celsius)")
    if city and temperature:
        temperature = int(temperature)
        if temperature > 20:print(f"It is currently warm in {city} with a temperature of {temperature}ºC!")
        elif temperature >= 10:print(f"It is currently chilly in {city} with a temperature of {temperature}ºC.")
        else: print(f"It is currently cold in {city} with a temperature of {temperature} ºC.")
    else: print("Please try again and enter a city and temperature")

def display_fahrenheit(celsius_temperature):
    """Displays the temperature in fahrenheit"""
    fahrenheit = (float(celsius_temperature) * 9 / 5) + 32
    return fahrenheit

def display_message(city, temperature):
    """Displays the temperature of a city"""
    fahrenheit= display_fahrenheit(temperature)
    print(f"It is currently {temperature}ºC ({round(fahrenheit)}ªF)in {city}")

def enter_a_city():
    """Enter a city and temperature"""
    city = input("Enter the name of the city:")
    celsius_temperature = input(f"Enter the current temperature in celsius in {city}:")
    if city and celsius_temperature:
        display_message(city, celsius_temperature)
    else:
        print("You did not enter a city and/or temperature. Please try again.")
        
weather = {
  "city":"Lisbon",
  "country":"Portugal",
  "temperature": 17.94,
  "humidity":77
}

def display_fahrenheit(celsius_temperature):
  """Displays the temperature in fahrenheit"""
  fahrenheit = (float(celsius_temperature) * 9 / 5) + 32
  return fahrenheit
fahrenheit= display_fahrenheit(weather['temperature'])

print(f"It is {round(weather['temperature'])}ºC ({round(fahrenheit)}ªF) in {weather['city']}, {weather['country']}, the humidity level is {weather['humidity']}%.")

forecast = {
  "city":"Lisbon",
  "country":"Portugal",
  "daily":
    [
      17.76,
      13.08,
      12.14,
      11.25,
      14.29
    ]
}

print(f"The forecast for {forecast['city']}, {forecast['country']} for the next 5 days is:")

index = 0 
for temperature in forecast['daily']:
  print(f"Day {index+1}: {round(temperature)}ºC")
  index = index + 1
  
import requests
from rich import print

city = input("Enter a city:")
api_key = "3734of2cfc5035aca32f96t5a9b478fb"
api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

response = requests.get(api_url)
print(response)

weather = response.json()
print(weather)

country = weather['country']
temperature = weather['temperature']['current']
humidity = weather['temperature']['humidity']
wind_speed = weather['wind']['speed']
print(f"The temperature of {city} in {country} is currently {round(temperature)}ºC and the humidity is {humidity}% and the windspeed is {round(wind_speed)}km/h")
