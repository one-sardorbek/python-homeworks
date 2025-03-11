import requests
lat = 41.945
lon = 63.9954
api_key = "a7d8b2ddbe600e2171dd7aef50d1bba5"
base_url='https://api.openweathermap.org/data/3.0/onecall'
params = {
    "lat": lat,
    "lon": lon,
    "exclude": "current",  # Adjust exclusions if needed
    "appid": api_key
}
weather=requests.get(base_url,params=params)
all=weather.json()
response=all["hourly"]["weather"]
#print("Weather in Navai: ",weather.json())
print(response)