import os
from twilio.rest import Client
import requests

api_key = "2c0f46ee4a72ff2e0da09221e5cbcac1"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": 19.075983,
    "lon": 72.877655,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}
account_sid = "AC1abdc7ac82c6feba7a86c37f42d6f192"
auth_token = "71a1122b85cc63c0bc54f63050323cd2"


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
        from_='+15207292541',
        to='+919930049115'
    )

    print(message.status)
    print("Take an umbrella with you")
