# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json 
from datetime import datetime

# Enter your API key here 
with open("openweather_api_key.txt") as f:
    api_key = f.read()[0:-1]

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
city_name = "St. Louis"

# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module 
# return response object 
response = requests.get(complete_url)

# json method of response object 
# convert json format data into 
# python format data 
x = response.json() 

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 
    #print(str(x))
    # store the value of "main" 
    # key in variable y 
    y = x["main"] 

    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 
    
    # time data was recorded (NOT retrieved)
    the_time = datetime.fromtimestamp(x["dt"]).strftime('%H:%M')

    # time of sunset
    sunset = datetime.fromtimestamp(x["sys"]["sunset"]).strftime('%H:%M')
    
    # store the value corresponding 
    # to the "description" key at 
    # the 0th index of z 
    weather_description = z[0]["description"] 

    # print following values 
    to_write = ("Time: " + the_time + ".\n" +
                    "Current Temperature: " +
                    str(y["temp"]) +
                    " kelvin." +
                    "\nFeels Like: " +
                    str(y["feels_like"]) +
                    " kelvin." +
                    "\n" +
                    "Currently " + str(weather_description) + "." +
                    "\n" +
                    "Sunset: " + sunset + "\n")
                    
    with open("weather.txt", 'w') as f:
        f.write(to_write)

else: 
    print(" City Not Found ") 
