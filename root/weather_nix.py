# (c) 2020 - Akash Sarkar
# weather

import sys
sys.path.insert(0, 'E:/Projects/Python/myAssistant/nixAssistant/root/common/')

import time
import requests, json

import speak_nix as nix
import sr_nix as sr


def weather():
        apiKey = 'f2ad852dc1e89e7dd3da6b3fb2508e1a'
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        nix.speak("Tell me the city name")
        city_name = sr.takeCommand()
        complete_url = base_url + "appid=" + apiKey + "&q=" + city_name 
        response = requests.get(complete_url) 
        x = response.json() 
  
        if x["cod"] != "404":
           y = x["main"] 
           current_temperature = y["temp"] 
           current_pressure = y["pressure"] 
           current_humidiy = y["humidity"] 
           z = x["weather"] 
           weather_description = z[0]["description"] 
  
           print("Temperature (in kelvin unit) = " + str(current_temperature) + 
                 "\nAtmospheric pressure (in hPa unit) = " + str(current_pressure) +
                 "\nHumidity (in percentage) = " + str(current_humidiy) +
                 "\nDescription = " + str(weather_description))
           nix.speak("Weather report for " + str(city_name))
           time.sleep(1)
           nix.speak("Temperature is " + str(current_temperature) + "Kelvin" +
                 "Atmospheric pressure is " +str(current_pressure) + "hPa" +
                 "Humidity is " + str(current_humidiy) + "hPa" +
                 "And the weather status is " + str(weather_description))
        else:
           print(" City not found!")
           nix.speak(" City not found!")
