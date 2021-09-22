def table(number, length):
    for n in range(1, length + 1):
        print(f"{number:2} * {n:2} = {number * n:2}")


x = int(input("enter number :"))
y = int(input("enter length :"))

# positional arguments
table(x, y)

# keyword arguments
table(number=2, length=10)
