file = open("names.txt", 'a')  # wt --> write text

while True:
    name = input("enter name [end to stop]:")
    if name == "end":
        break

    file.write(name + "\n")