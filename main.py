import requests

base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = open("api_key", 'r').read()
city = input("Enter city name:")


def kelvin_to_celsius(k):
    return k - 273.15


url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()

# print(response)

temp_celsius = kelvin_to_celsius(response['main']['temp'])
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']


print(f"General weather in {city}: {description}")
print(f"Temperature in {city}: {temp_celsius:.2f}°C")
print(f"Wind speed in {city}: {wind_speed}m/s")
print(f"Humidity in {city}: {humidity}%")
