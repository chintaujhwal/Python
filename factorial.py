num = int(input("enter a number : "))
fac = 1

for n in range(1, num + 1):
    fac *= n

print("Factorial of %d is %d" % (num, fac))
