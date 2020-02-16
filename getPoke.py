import requests
import random



url = "http://10.11.12.84:1993/pokedex"
randomNumber = random.randint(1,564)
querystring = {"pokedex_number":randomNumber}

print(randomNumber)
print()
print()
response = requests.request("GET", url, params=querystring)
data = response.json()
print(response.text)
