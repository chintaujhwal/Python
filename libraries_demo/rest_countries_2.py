import requests

link = requests.get("https://restcountries.eu/rest/v2/alpha/col")

countries = link.json()

for x, y in countries['translations'].items():
    print(x, y)


