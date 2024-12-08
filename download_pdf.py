import requests
import json

json_url = "http://api.open-notify.org/astros.json"
json_path = "D:/user/Downloads/astros.json"

response = requests.get(json_url)
json_data = response.json()

with open(json_path, 'w') as file:
    json.dump(json_data, file, indent=4)

print("JSON data saved successfully.")
