import re
file = open("contacts.txt", "rt")

customer = {}

for n in file.readlines():
    n = n.strip()

    s1 = re.search("\w+", n)
    name = s1.group(0)
    s2 = re.search("\d{10}", n)
    number = s2.group(0)

    customer[name] = number

for (name, number) in sorted(customer.items()):
    print(f"{name:5} - {number:10}")

