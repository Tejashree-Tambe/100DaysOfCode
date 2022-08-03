import requests
from datetime import datetime
import os

API_ID = os.getenv("API ID")
API_KEY = os.getenv("API KEY")

GENDER = "female"
WEIGHT_KG = 45
HEIGHT_CM = 230
AGE = 19

# API_ID = "66e0a1f8"
# API_KEY = "80fae14405fab96bbe92470ea0379c5f"
EXERCISE_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
# SHEET_ENDPOINT = "https://api.sheety.co/ae2cead908ac512c1ce11ae26eb8b478/myWorkouts/sheet1"
# BEARER_TOKEN = "wuieriy8uryegeryguin"


SHEET_ENDPOINT = os.getenv("SHEET ENDPOINT")
BEARER_TOKEN = os.getenv("BEARER TOKEN")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

sheet_headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

exercise_text = input("Which exercises have you done?: ")

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url=EXERCISE_API_ENDPOINT, json=params, headers=headers)
data = response.json()
print(response.text)
# I ran 5 miles and walked 3 miles
today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in data["exercises"]:
    body = {
        "sheet1": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_post_response = requests.post(url=SHEET_ENDPOINT, json=body, headers=sheet_headers)
    print(sheet_post_response.text)
