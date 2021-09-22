import sys

if len(sys.argv) < 2:
    print("Usage : sum_of_digits.py <number>")
    exit(1)

n = sys.argv[1]
nums = list(map(int, n))

print(f"sum of digits in {n} is {sum(nums)}")
