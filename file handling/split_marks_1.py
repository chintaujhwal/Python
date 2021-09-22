student = {}
with open("marks_1.txt", 'rt') as file:

    for n in file.readlines():
        if len(n.strip()) == 0:  # to avoid blank lines
            continue

        parts = n.split(",")
        name = parts[0]
        marks = parts[1:]
        total = sum(map(int, marks))
        student[name] = total

for (name, total) in student.items():
    print(f"{name:10} - {total:3}")
