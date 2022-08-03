import requests

api_key = "2c0f46ee4a72ff2e0da09221e5cbcac1"
lat = 48.856613
lon = 2.352222
part = "hourly,daily"

# response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}")
# response.raise_for_status()
#
# data = response.json()
# print(data)

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": 48.856613,
    "lon": 2.352222,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()

data = response.json()

weather_for_twelve_hrs = data["hourly"][:12]
will_rain = False

for hour_data in weather_for_twelve_hrs:
    weather_predicted = hour_data["weather"]
    weather_code = weather_predicted[0]["id"]

    if weather_code < 700:
        will_rain = True

if will_rain:
    print("Take an umbrella with you")
