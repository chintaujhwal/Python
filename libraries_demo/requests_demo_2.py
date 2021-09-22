import requests

link = requests.get("https://api.github.com/users/srikanthpragada")

if link.status_code == 200:
    details = link.json()  # convert JSON to DICTIONARY
    print(details['name'])
    print(details['company'])
    print(details['location'])
else:
    print("Sorry ! Could not get details")
