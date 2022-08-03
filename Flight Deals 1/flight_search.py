import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "MTsLvk-_8vjH8uzz3suqDXcplkNJ0qau"


class FlightSearch:

    def get_IATA_code(self, city):
        headers = {
            "apikey": TEQUILA_API_KEY,
        }

        params = {
            "term": city
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        code = data["locations"][0]["code"]
        return code

    def search_flights(self, source_city, destination, from_date, to_date):
        headers = {
            "apikey": TEQUILA_API_KEY,
        }

        params = {
            "fly_from": source_city,
            "fly_to": destination,
            "date_from": from_date,
            "date_to": to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD",
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=params, headers=headers)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flight details found for {destination}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        # print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
