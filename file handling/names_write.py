file = open("names.txt", 'wt')  # wt --> write text

# Any of following 2 methods can be used

# 1
while True:
    name = input("enter name [end to stop]:")
    if name == "end":
        break

    file.write(name + "\n")

# 2
names = ["Dustin", "Steve", "Robin"]
for n in names:
    file.write(n + "\n")

file.close()

