import requests
import datetime as dt

USERNAME = "name"
TOKEN = "token"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN,
}

today = dt.datetime.now()

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you cycle today?"),
}

post_pixel_response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
print(post_pixel_response.text)
