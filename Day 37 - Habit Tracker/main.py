import requests
from datetime import datetime
import my_secrets

USERNAME=my_secrets.PIXELA["username"]
TOKEN=my_secrets.PIXELA["token"]
GRAPH_ID="graph1"
QUANTITY="2"
DATE=datetime.now().strftime("%Y%m%d")

pixela_endpoint = r"https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
update_endpoint=f"{pixel_endpoint}/{DATE}"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#response=requests.post(url=PIXELA_ENDPOINT, json=user_params)

graph_params={
    "id": GRAPH_ID,
    "name": "Python Course Graph", 
    "unit": "Modules",
    "type": "int",
    "color": "ajisai",
}

headers={
    "X-USER-TOKEN":TOKEN,
}

#response=requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)

pixel_params={
    "date": DATE,
    "quantity":QUANTITY
}

#response=requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

update_params={
    "quantity":QUANTITY
}

#response = requests.delete(url=update_endpoint, headers=headers)
#print(response.text)


