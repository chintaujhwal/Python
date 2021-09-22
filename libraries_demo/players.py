from datetime import datetime

file = open("players.txt", "rt")
players = {}

for n in file.readlines():
    n = n.strip()

    parts = n.split(',')
    name = parts[0]
    dob = datetime.strptime(parts[1], "%d-%m-%Y")

    age = (datetime.now() - dob).days // 365  # to calculate the age using DOB
    players[name] = age

for x, y in players.items():
    print(f"{x:6} - {y} YEARS")
