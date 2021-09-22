from tabulate import tabulate

num = dict()

r = int(input("enter RANGE :"))

for n in range(1, r):
    num[n] = n**2, n**3

print(tabulate(num, headers="keys"))