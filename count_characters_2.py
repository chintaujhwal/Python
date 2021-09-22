str = input("Enter a string : ")

lower = 0
upper = 0
other = 0

for n in str:
    if ord(n) >= 65 and ord(n) <= 90:  # to count UPPER case
        upper += 1
    elif ord(n) >= 97 and ord(n) <= 122:  # to count LOWER case
        lower += 1
    else:
        other += 1

print("Lower Case :", lower)
print("Upper Case :", upper)
print("Other      :", other)

