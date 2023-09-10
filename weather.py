from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim 
from tkinter import ttk,messagebox 
from timezonefinder import TimezoneFinder
from datetime import *
import requests 
import pytz 
from PIL import Image, ImageTk

# we are creating a function that allows us to get the weather information from our API
def getWeather():
    city = textField.get
    api = ""
    json_data = requests.get(api).json
    # need to receive additional data about weather conditions from the api

root = Tk()
root.title("Iden's Weather App")
root.geometry("600x500")
root.configure(bg="#A1CCA5")
root.resizable(False, False)

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

#this is the search bar, where user input goes!
textField = tk.Entry(root, font = t)
textField.pack(pady=20)
textField.focus()

label1 = tk.Label(root, font = t)
label1.pack()
label2 = tk.Label(root, font = f)
label2.pack()

root.mainloop()


