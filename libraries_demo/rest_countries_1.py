import requests

link = requests.get("https://restcountries.eu/rest/v2/all")

countries = link.json()

for n in sorted(countries, key=lambda x: x['population'], reverse=True)[:10]:
    print(f"{n['name']:30} {n['population']:30}")
