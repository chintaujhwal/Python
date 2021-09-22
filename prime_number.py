a = int(input("enter a number : "))

for n in range(2, a):
    if a % n != 0:
        print(a, "is a prime")
        break
    else:
        print(a, "is not a prime")
        break
