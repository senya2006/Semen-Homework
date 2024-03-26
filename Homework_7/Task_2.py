list_1 = [1, 2, 3, 5, 8, 12, 16]
list_2 = [1, 2, 3, 4, 5, 6]

set1 = set(list_1)
set2 = set(list_2)
elements = set1.difference(set2)

print(f"Elements in list_1 that doesn't have in list_2 are: {elements}")
