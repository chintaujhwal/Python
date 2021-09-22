menu = {"apple":10, "orange":10, "mango":15, "banana":25}
order = []

print("MENU-----------")
for i,j in menu.items():
    print(f"{i:10} - {j}")

print("\nGIVE YOUR ORDER")
while(True):
    x = input("enter item names [n to stop]: ")
    if x == 'n':
        break
    else:
        order.append(x)

print("\nBILL-----------")
total = 0

for i in order:
    total += menu[i]

print(total)

