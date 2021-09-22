s = []

x = int(input("Enter number of elements : "))

for n in range(0, x):
    num = int(input("enter a number : "))
    s.append(num)

print("\nEVEN")
for n in s:
    if n % 2 == 0:
        print(n, end=" ")

print("\nODD")
for n in s:
    if n % 2 == 1:
        print(n, end=" ")
