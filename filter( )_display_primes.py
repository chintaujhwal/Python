# program to print prime numbers
nums = [n for n in range(2, 20)]


def isprime(num):
    for i in range(2, num):
        return num % i != 0


for i in filter(isprime, nums):
    print(i)
