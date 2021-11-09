#use this with the venv by selecting view->command pallette-> Python select interpreter -> then the venv option. it will run in that environment. you may need to bring it out f the folder to access it.

import requests

api_key = "67da29cb91129f1a68c1c06c1be92daa"
city = "Orlando"
url="http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" +api_key + "&units=imperial"

requests = requests.get(url)
json = requests.json()
# print(json)

description = json.get("weather")[0].get("description")
temp_min = json.get("main").get("temp_min")
print("The minimum temperature is", temp_min)
temp_max = json.get("main").get("temp_max")
print("The maximum temperature is", temp_max)