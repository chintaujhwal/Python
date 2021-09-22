x = input("STRING[1] : ")
y = input("STRING[2] : ")

common = set(x) & set(y)  # intersection

print(common)
