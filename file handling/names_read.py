names = []
file = open("names.txt", 'rt')  # rt --> read text

for n in file.readlines():
    names.append(n)

file.close()

for n in sorted(names):
    print(n.strip())
