import requests

api_key = "a7d87ec61910c24ff70a323715515f1c"
base_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a City Name: ")
request_url = f"{base_url}?appid={api_key}&q={city}"
response = requests.get(request_url)

data = response.json()
print(data)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15, 2)
    temp_feel = round(data["main"]["feels_like"]-273.15, 2)
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    
    print("City Details")
    print("---------------------------------------------")
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature} celsius")
    print(f"Feels like: {temp_feel} celsius")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} m/s")

else:
    print("An Error Occurred!")