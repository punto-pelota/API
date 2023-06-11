import requests
import json

params = {
  'access_key': '28cad8508fb0d46555fe462b2ca05b2d'
}

api_result = requests.get('http://api.aviationstack.com/v1/airlines?access_key', params)

with open('json_data.json') as file:
    json_data = file.read()

data = json.loads(json_data)

max_fleet_age = float(0)
selected_airline_name = ''

for entry in data['data']:
    fleet_average_age = float(entry['fleet_average_age'])
    if fleet_average_age < 73 and fleet_average_age > max_fleet_age:
        max_fleet_age = fleet_average_age
        selected_airline_name = entry['airline_name']

if selected_airline_name:
    print("Selected Airline Name:", selected_airline_name)
    print("Max Fleet Average Age:", max_fleet_age)
else:
    print("No matching airline found.")

