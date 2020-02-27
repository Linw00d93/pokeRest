import requests

url = "http://localhost:1993/pokedex/pokeNumber/"

url = url + str(25)


print(url)
print()
print()
response = requests.request("GET", url)
data = response.json()
print(response.text)
