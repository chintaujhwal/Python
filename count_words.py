s = "GitHub is home to over million developers working together to host and review code manage projects and build software together"

words = s.split(sep=" ")

set = set(words)

for n in set:
    print(f"{n:10} - {words.count(n):2}")


