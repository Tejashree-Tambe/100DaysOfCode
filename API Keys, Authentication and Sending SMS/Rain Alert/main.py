import os
from twilio.rest import Client
import requests

api_key = "your key"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": 19.075983,
    "lon": 72.877655,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}
account_sid = "acc_sid"
auth_token = "auth_token"


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
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Don't forget your umbrella",
        from_='+from',
        to='+to'
    )

    print(message.status)
    print("Take an umbrella with you")
