i = 0

while True:
    try:
        num = int(input("enter a number :"))
        if num == 0:
            break
        i += num

    except:
        print("invalid input")

print("sum is", i)
