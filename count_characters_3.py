s1 = input("enter [string 1] :")
s2 = input("enter [string 2] :")

for n in set(s1):
    print(f"{n:2} - {s2.count(n):2}")
