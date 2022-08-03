import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351     # Your latitude
MY_LONG = -0.127758    # Your longitude
MY_EMAIL = "pythondeveloper0401@gmail.com"
PASSWORD = "Python123"


def check_if_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(iss_latitude)
    print(iss_longitude)

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_latitude <= (MY_LAT + 5):
        return True

    else:
        return False


def check_if_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    time_now_hr = time_now.hour

    print(time_now_hr)

    if time_now_hr >= sunset or time_now_hr <= sunrise:
        return True

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    time.sleep(60)
    if check_if_near() and check_if_near():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="manesheetal102@gmail.com",
                msg="Subject: The ISS is above you\n\nLook Up"
            )
