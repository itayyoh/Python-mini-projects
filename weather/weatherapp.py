import requests
import os

# Fetch your api key through Operating System !
# with os.getenv we can fetch an api key we stored locally!
api_key = os.getenv(#your api key!)
 
if not api_key:
    print("Invalid API key!")
else:
    city = input("Enter City: ")
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp'] - 273.15
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp:.2f}°C')
    print(f'Description : {desc}')
else:
    print("Invalid Input!5")


if response.status_code == 200:
    print(f"HTTP Status Code: {response.status_code} :D")
else:
    print(f'HTTP Status Code: {response.status_code} :(')
