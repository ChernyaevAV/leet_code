import sys

j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

result = (1 for char in s if char in j)
print(sum(result))