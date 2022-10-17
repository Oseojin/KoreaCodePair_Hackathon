import json

import requests

api_key = "61cbc8f01b2d0870e915eb95bd750028"
city_name = "Seoul"
data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
result = json.loads(data.text)
print(result["name"])
print(result["weather"][0]["main"])