s = input("enter a string : ")

for n in sorted(set(s)):
    print(f"{n} - {s.count(n)}")