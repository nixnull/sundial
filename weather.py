# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json 
from astral.sun import sun
from astral import LocationInfo
from datetime import datetime, timedelta, date

#Load the config file
with open("config.json") as f:
    configs = json.load(f)

lat = configs["lat"]
lng = configs["lng"]

# Most of these details don't actually matter. Just the lat and lng. TODO: Can I do this without setting random details?
city = LocationInfo("A", "A", "America/Chicago", lat, lng)

tomorrow = date.today() + timedelta(days=1)
s = sun(city.observer, date=tomorrow, tzinfo=city.timezone)
sunrise = s['sunrise']
bedtime = sunrise - timedelta(hours=float(configs["sleep_hrs"]))

# weather_base_url variable to store url 
weather_base_url = "http://api.openweathermap.org/data/2.5/weather?"

# complete url address 
weather_url = weather_base_url + "lat=" + lat + "&lon=" + lng + "&appid=" + configs["weather_api_key"]

#print(weather_url)

# get method of requests module 
# return response object 
x = requests.get(weather_url).json()

#print(x)

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
    to_write = ("Time: " + str(the_time) + ".\n" +
                    "Current Temperature: " +
                    str(y["temp"]) +
                    " kelvin." +
                    "\nFeels Like: " +
                    str(y["feels_like"]) +
                    " kelvin." +
                    "\n" +
                    "Currently " + str(weather_description) + "." +
                    "\n" +
                    "Bedtime: " + bedtime.strftime('%H:%M') + "\n")
                    
    with open("weather.txt", 'w') as f:
        f.write(to_write)

else: 
    print(" Location Not Found ")
    print(x)
