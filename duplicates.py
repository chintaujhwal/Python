l = []
while True:
    x = int(input("enter a number [0 to stop]: "))
    if x == 0:
        break
    elif x not in l:
        l.append(x)

for i in sorted(l):
    print(i, end=" ")