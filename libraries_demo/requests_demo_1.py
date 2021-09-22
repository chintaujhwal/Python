import requests

link = requests.get("https://api.github.com/users/srikanthpragada")

details = link.json()

for x, y in details.items():
    print(f"{x:20} - {y}")
