def factor(num):
    for n in range(1, num + 1):
        if num % n == 0:
            print(n)


num = int(input("enter a number : "))

factor(num)
