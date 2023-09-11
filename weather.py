from tkinter import *
import tkinter as tk
from datetime import *
import requests 
import pytz 
import datetime
import config 

key = str(config.API_KEY)

def getWeather(root):
    city = textField.get()
    api_call = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + key + "&units=metric"
    json_data = requests.get(api_call).json()
    condition = json_data['weather'][0]['main']


    temperature = int(json_data['main']['temp'] ) 
    temperature_fahrenheit = int((temperature * 9/5) + 32) # converting the temperature to fahrenheit

    min_temperature = int(json_data['main']['temp_min'] )
    min_temperature_fahrenheit = int((min_temperature * 9/5) + 32) # converting the minimum temperature to fahrenheit 


    max_temperature = int(json_data['main']['temp_max'] )
    max_temperature_fahrenheit = int((max_temperature * 9/5) + 32) # converting the maximum temperature to fahrenheit 


    feels_like = int(json_data['main']['feels_like'])
    feels_like_fahrenheit = int((feels_like * 9/5) + 32) # converting the feels_like value to fahrenheit


   # pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    #need to convert time to eastern time.
    sunrise_timestamp = json_data['sys']['sunrise'] - 18000
    sunrise_datetime = datetime.datetime.utcfromtimestamp(sunrise_timestamp)
    sunrise = sunrise_datetime.strftime('%I:%M:%S')

    #need to convert time to eastern time. 
    sunset_timestamp = json_data['sys']['sunset'] - 18000
    sunset_datetime = datetime.datetime.utcfromtimestamp(sunset_timestamp)
    eastern = pytz.timezone('US/Eastern')
    sunset_et = sunset_datetime.astimezone(eastern)
    sunset = sunset_et.strftime('%I:%M:%S')
    
    final_info = condition + "\n" + str(temperature_fahrenheit) + "°F"
    final_data = "\n" + "Maximum Temperature: " + str(max_temperature_fahrenheit) + "°F" + "\n" + "Minimum Temperature: " + str(min_temperature_fahrenheit) + "°F" + "\n" + "Feels Like: " + str(feels_like_fahrenheit) +  "°F" + "\n" + "Humidity: " + str(humidity) +  "%" + "\n" + "Wind: " + str(wind) + "\n" + "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset) 
    label1.config(text = final_info)
    label2.config(text = final_data)

    #print(getWeather(final_info(condition)))

# if the final info is (ex. Cloud), we want there to be a cloud image.
def getWeatherImage ():
    print("Is this working?")

root = Tk()
root.title("Iden's Weather App")
root.geometry("600x500")
root.configure(bg="#A1CCA5")
root.resizable(False, False)

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

#this is the search bar, where user input for the city goes!
textField = tk.Entry(root, font = t, bg="#A1CCA5")
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(root, font = t, bg="#A1CCA5")
label1.pack()

label_Image = tk.Label(root, )

label2 = tk.Label(root, font = f, bg="#A1CCA5")
label2.pack()

root.mainloop()


