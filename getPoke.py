import requests
import random




randomNumber = random.randint(1,801)


url = "http://localhost:1993/pokedex/"

url = url + str(randomNumber)


print(randomNumber)
print()
print()
response = requests.request("GET", url)
data = response.json()
print(response.text)
