import os

walk = os.walk(r"c:\users\ujhwal\desktop\python")

for (path, folders, files) in walk:
    for n in files:
        if n.endswith(".py"):
            print(path + "\\" + n)
