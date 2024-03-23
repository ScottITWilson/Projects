import requests

API_KEY = '40f52b19086428c837e6c896c3b53ad7'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input("Enter city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json() #convert data to a readable format
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2) #-273.15 to convert from Kelvin to Celcius
    print("The weather for", city, "is:\n", weather, "\n", temperature, "C")

else:
    print("An error occured")
