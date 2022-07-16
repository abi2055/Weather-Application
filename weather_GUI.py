import tkinter as tk
from tkinter import font
import requests 

h = 700
w = 800

def formattted_response(weather):
    try:
        city_name = weather["name"]
        des = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]

        out = "City: %s \nConditions: %s \nTemperature: (°C): %s" % (city_name, des, temp)
    except:
        out = "An Error Has occurred!"

    return out

def get_weather(city):
    weather_key = "a7d87ec61910c24ff70a323715515f1c"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {"APPID": weather_key, "q": city, "units": "metric"}
    response=requests.get(base_url, params=parameters)
    weather = response.json()

    label["text"] = formattted_response(weather)

root = tk.Tk()

root.title("Weather Application")

canvas = tk.Canvas(root, height=h, width=w)
canvas.pack()

bg_image = tk.PhotoImage(file="bg image for app.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#345fa3", bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=("Century", 20))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=("Century", 14), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

frame2 = tk.Frame(root, bg="#345fa3", bd=10)
frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(frame2, font=("Century", 20), anchor="n", bd=50)
label.place(relwidth=1, relheight=1)

root.mainloop()

