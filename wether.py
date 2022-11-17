# code for weather report
import requests
import requests
import os
from datetime import datetime

api_key = '0bec0ef6dace980a66841733f7b96af3'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather Stats for - {} || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc :", weather_desc)
print("Current Humidity :", hmdt, '%')
print("Current wind speed :", wind_spd, 'kmph')

f = open("file.txt", 'a+')
s = "\nWeather stats for "+location+"\nTemperature=" + \
    str(temp_city)+"\nWeather desc="+weather_desc + \
    "\nHumidity="+str(hmdt)+"\nWind speed="+str(wind_spd)
f.write(s)
f.close()


r = requests.get(
    'https://api.openweathermap.org/data/2.5/weather?q=chennai&appid=0bec0ef6dace980a66841733f7b96af3')

with open('weather.txt', 'wb') as f:
    f.write(r.content)
