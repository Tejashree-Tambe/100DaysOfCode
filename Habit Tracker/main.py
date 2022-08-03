import requests
import datetime as dt

USERNAME = "name"
TOKEN = "token"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

today = dt.datetime.now()

print(f"{pixela_endpoint}/{USERNAME}/graphs")
post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
post_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.2",
}

# post_pixel_response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
# print(post_pixel_response.text)

date = today.strftime("%Y%m%d")
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
update_pixel_params = {
    "quantity": "9.24",
}

update_pixel_response = requests.put(url=update_pixel_endpoint, json=post_pixel_params, headers=headers)
print(update_pixel_response.text)

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
# delete_response = requests.delete(url=delete_endpoint, headers=headers)
# print(delete_response.text)
