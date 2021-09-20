import requests
from datetime import datetime
import my_secrets

APP_ID = my_secrets.EXCERSICE["id"]
API_KEY = my_secrets.EXCERSICE["key"]
BEARER_TOKEN = my_secrets.SHEETY["token"]

EXCERSICE_ENDPOINT = r"https://trackapi.nutritionix.com/v2/natural/exercise"

excersice_header={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

excersices=input("Tell me which excersices you did: ")

excersice_params={
    "query": excersices,
    "gender":"male",
    "weight_kg":85,
    "height_cm":182,
    "age":22
}

response1 = requests.post(url=EXCERSICE_ENDPOINT, json=excersice_params, headers=excersice_header)

sheety_header={
    "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAMLheAAAAAAA0%2BuSeid%2BULvsea4JtiGRiSDSJSI%3DEUifiRBkKG5E2XzMDjRfl76ZC9Ub0wnz4XsNiRVBChTYbJcE3F",
}

for excersice in response1.json()["exercises"]:
    sheety_params = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": excersice["name"].title(),
            "duration": str(excersice["duration_min"])+" min",
            "calories": float(excersice["nf_calories"]),
            }
    }
    response2 = requests.post(url=my_secrets.SHEETY["sheet endpoint"], json=sheety_params, headers=sheety_header)