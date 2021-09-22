student = {}
with open("marks_2.txt", 'rt') as file:

    for n in file.readlines():
        n = n.strip()
        if len(n) == 0:  # to avoid blank lines
            continue

        parts = n.split(",")
        if len(parts) > 0:      # "len(parts) > 0" --> name without marks will be printed
            name = parts[0]     # "len(parts) > 1" --> name without marks wont be printed
            marks = parts[1:]
            try:  # to avoid value error
                total = sum(map(int, marks))
                student[name] = total
            except:
                pass

for (name, total) in student.items():
    print(f"{name:10} - {total:3}")

