import requests
import tweepy
import random

CONSUMER_KEY ="jhVRFkFMhYMNJaz8bKW88gNGH"
CONSUMER_SECRET = "utbzKXwJ5mWg2ApGKHfWJZUyEQjbmracL0IxLHVMLJtC1Smt2l"
ACCESS_KEY = "2264506449-8ZbgybLT15t8OmGuF45237vtWpmXcMBQsWnifc3"
ACCESS_SECRET = "DU1lJ393NC6H5IHSbOVmuLIUKsz90BKsruE0H9fmjNLum"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET )
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET )
api = tweepy.API(auth)

url = "https://superhero-search.p.rapidapi.com/"
randomNumber = random.randint(1,564)
querystring = {"id":randomNumber ,"name": "","fullName": "","publisher": ""}

headers = {
    'x-rapidapi-host': "superhero-search.p.rapidapi.com",
    'x-rapidapi-key': "40c393c934mshf71627973474ee7p1ccbcejsn041365356210"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()
response.text

name = data["name"]
fullName = data["biography"]["fullName"]
aliases = data["biography"]["aliases"]
firstAppearance = data["biography"]["firstAppearance"]
publisher = data["biography"]["publisher"]
api.update_status("Random Comicbook Character. Character Name: %s Full Name: %s Aliases: %s First Appearance in a comicbook: %s Publisher: %s" % (name,fullName,aliases,firstAppearance,publisher))
