import json
import requests

response = requests.get("http://api.weather.gov/gridpoints/OKX/51,69/forecast/")
days = json.loads(response.text)

name = days['properties']['periods'][2]['name']
temp = days['properties']['periods'][2]['temperature']

print(name + ": " + str(temp))
