from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/8da3efc1aab14c7b1e55b116d6f5bdc1/flightDetails/sheet1"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/8da3efc1aab14c7b1e55b116d6f5bdc1/flightDetails/sheet2"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["sheet1"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_users_email(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.user_data = data["sheet2"]
        return self.user_data
