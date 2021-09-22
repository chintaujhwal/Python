s = "101:99,102:95,103:91,104:87,105:83"

data = s.split(sep=",")

students = {}  # empty dictionary

for n in data:
    rollno, marks = n.split(sep=":")
    students[rollno] = marks  # storing the values in dictionary

print("{ rollno : marks } =", students)

for rollno, marks in students.items():
    print(rollno, marks)
