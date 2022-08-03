from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt

API_KEY = "MTsLvk-_8vjH8uzz3suqDXcplkNJ0qau"
ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()

flight_search = FlightSearch()

notification_manager = NotificationManager()

for data in sheet_data:
    if data['iataCode'] == "":
        city = data['city']
        data['iataCode'] = flight_search.get_IATA_code(city)

data_manager.destination_data = sheet_data
data_manager.update_sheet_data()

today = dt.datetime.now()
today_formatted = today.strftime("%d/%m/%Y")

six_months_from_today = dt.datetime.now() + dt.timedelta(days=6 * 30)
six_months_from_today_formatted = six_months_from_today.strftime("%d/%m/%Y")

for data in sheet_data:
    destination = data['iataCode']

    flight_data = flight_search.search_flights(
        ORIGIN_CITY_IATA,
        destination,
        today_formatted,

        six_months_from_today_formatted
    )

    if flight_data is not None and flight_data.price < data["lowestPrice"]:
        message = f"Low Price Alert! Only ${flight_data.price} to fly from {flight_data.origin_city}-" \
                  f"{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}," \
                  f"from {flight_data.out_date} to {flight_data.return_date}"
        notification_manager.send_sms(message)
