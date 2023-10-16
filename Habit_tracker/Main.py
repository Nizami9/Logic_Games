import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "nizami"
TOKEN = 'dfjkdfjdfje34o43jf'
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# requests.post(url=graph_endpoint, json=graph_config, headers=headers)


pixel_config = {
    "date": "20231010",
    "quantity": '20',
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

