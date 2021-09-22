import sys

def factor(num):
    for n in range(1, num + 1):
        if num % n == 0:
            print(n)


if len(sys.argv) < 2:
    print("Usage : factors.py <number>")
    exit(1)

num = int(sys.argv[1])

factor(num)
