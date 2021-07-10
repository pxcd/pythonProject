import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "pow"
TOKEN = "fj4209tuehiwgh28thgiohgt2490uwghfasd"
GRAPH = "graph1"

user_params = {
    "token": TOKEN,
    "username": "pow",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

today = datetime.now()
# print(today.strftime("%Y%m%d"))

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "Hours",
#     "type": "int",
#     "color": "ajisai"
# }

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)


# add_pixel_config = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "1"
# }

add_pixel_config = {
    "date": "20210709",
    "quantity": "2"
}

# post_endpoint = requests.post(url=f"{graph_endpoint}/{GRAPH}", json=add_pixel_config, headers=headers)
# print(post_endpoint)

# update_endpoint = requests.put(url=f"{graph_endpoint}/{GRAPH}/20200709", json=add_pixel_config, headers=headers)
# print(update_endpoint.text)

delete_endpoint = requests.delete(url=f"{graph_endpoint}/{GRAPH}/20210710", json=add_pixel_config, headers=headers)
print(delete_endpoint.text)