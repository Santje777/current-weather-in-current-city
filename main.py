city = input("What is your current city?")
temperature = input(f"What is the current temperature in {city}?")
temperature = int(temperature)
if city and temperature:
    print(f"The current temperature is {temperature} city is {city}")
else:
    print("You did not provide a city and/or temperature")