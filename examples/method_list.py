lst = [1, 2, 4, 5, 7, 3, 55, 333]

for idx, num in enumerate(lst):
    if num < 5:
        lst.remove(num)

print(lst)
