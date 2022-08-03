import requests
import datetime as dt

LATITUDE = lat
LONGITUDE = long

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise_hr = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hr = data["results"]["sunset"].split("T")[1].split(":")[0]

now = dt.datetime.now()
print(now.hour)

