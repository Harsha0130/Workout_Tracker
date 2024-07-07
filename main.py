import requests
from datetime import datetime

API_ID = "92bc5c4e"
API_KEY = "d324f0d03832da0f828634bf2d28d61f"
api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
HEIGHT_CM = 204
WEIGHT_KG = 60
AGE = 20

header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    }

query = input("Enter the query - ")

parameters = {
    "query": query,
    "gender": GENDER,
    "height_cm": HEIGHT_CM,
    "weight_kg": WEIGHT_KG,
    "age": AGE,
}

response = requests.post(url=api_endpoint, headers=header, json=parameters)
result = response.json()

sheety_api_endpoint = "https://api.sheety.co/f72c7dde575b917aa0ceee138a8b92fd/workoutsTracking/workouts"

header2 = {
    "Authorization": "Basic SGFyc2hhOktha2thQDEyMw=="
}

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=sheety_api_endpoint, json=sheet_input, headers=header2)

    print(sheet_response.text)





