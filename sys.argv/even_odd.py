import sys

n = int(sys.argv[1])

def check(n):
    if n % 2 == 0:
        return print(n, "is even")
    else:
        return print(n, "is odd")


check(n)
