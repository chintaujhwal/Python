num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
char = ["A", "a", "B", "b", "C", "c"]
words = ["Mike", "Eleven", "Lucas", "Max"]

for n in filter(lambda v: v % 2 == 0, num):  # to print even numbers from the above list "num"
    print(n)

for n in filter(lambda v: (ord(v) >= 65 and ord(v) <= 90), char):  # to print UPPER CASE from the above list "char"
    print(n)

for n in filter(lambda v: len(v) > 4, words):  # to print words with length > 4 from the above list "words"
    print(n)
