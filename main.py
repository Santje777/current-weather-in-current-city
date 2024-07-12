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