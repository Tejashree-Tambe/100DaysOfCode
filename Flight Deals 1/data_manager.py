import requests

SHEET_ENDPOINT = "https://api.sheety.co/8da3efc1aab14c7b1e55b116d6f5bdc1/flightDetails/sheet1"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_sheet_data(self):
        get_sheet_response = requests.get(url=SHEET_ENDPOINT)
        get_sheet_response.raise_for_status()

        data = get_sheet_response.json()
        self.destination_data = data["sheet1"]
        return self.destination_data

    def update_sheet_data(self):
        for data in self.destination_data:
            body = {
                "sheet1": {
                    "iataCode": data["iataCode"]
                }
            }

            response = requests.put(url=f"{SHEET_ENDPOINT}/{data['id']}", json=body)

