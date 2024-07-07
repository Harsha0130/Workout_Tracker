import requests

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
print(response.json())

