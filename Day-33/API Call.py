import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)
#response.raise_for_status()

data = response.json()
print(data)

latitude = response.json()["iss_position"]["latitude"]
longitude = response.json()["iss_position"]["longitude"]
iss_position = (latitude, longitude)
print(iss_position)

response2 = requests.get(url="http://api.open-notify.org/is-now.json")
print(response2.status_code)
#response2.raise_for_status()