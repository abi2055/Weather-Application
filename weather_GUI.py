import tkinter as tk
from tkinter import font
import requests 

h = 700
w = 800
# Window Canvas size

# Function formats the information being pulled from the API
def formattted_response(weather):
    # try block checked to see if there are no errors and everthing is valid 
    try:
        city_name = weather["name"]
        # City name location in json file
        des = weather["weather"][0]["description"]
        # weather description location in json file
        temp = weather["main"]["temp"]
        # temperature location in json file 

        out = "City: %s \nConditions: %s \nTemperature: (°C): %s" % (city_name, des, temp)
        # print statement stored in variable using percent notation 
    except:
        out = "An Error Has occurred!"
        # Error statement 

    return out
    # returns whichever statement 

# Function that gets the weather details from the API after recieving a city name 
def get_weather(city):
    weather_key = "a7d87ec61910c24ff70a323715515f1c"
    # API key from open weather 
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    # default url that will be changed depending on the city inputted 
    parameters = {"APPID": weather_key, "q": city, "units": "metric"}
    response=requests.get(base_url, params=parameters)
    # Getting a response from API using paramters 
    weather = response.json()
    # storing the response json file that is readable 

    label["text"] = formattted_response(weather)
    # adds the text to the label widget in a formatted way 

# The entire GUI is enclosed in the root 
root = tk.Tk()

root.title("Weather Application")
# Title of the program

canvas = tk.Canvas(root, height=h, width=w)
canvas.pack()
# the window canvas size when opened

bg_image = tk.PhotoImage(file="bg image for app.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)
# bg_image = background image, the landscape in the background is placed to cover the entire canvas

frame = tk.Frame(root, bg="#345fa3", bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")
# the first frame placed within the canvas 
# Colour purple using a hex colour code 

entry = tk.Entry(frame, font=("Century", 20))
entry.place(relwidth=0.65, relheight=1)
# This is an entry block where the user can specify the city for weather data 
# using font "century" from the tkinter font library 

button = tk.Button(frame, text="Get Weather", font=("Century", 14), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)
# Button to get weather details
# when pressed the command line uses a lambda function to run the weather details after the button press and not before 

frame2 = tk.Frame(root, bg="#345fa3", bd=10)
frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")
# the second frame is where the weather details will be printed 

label = tk.Label(frame2, font=("Century", 20), anchor="n", bd=50)
label.place(relwidth=1, relheight=1)
# This label is what holds the whether details and it is tethered to the second frame 

root.mainloop()
