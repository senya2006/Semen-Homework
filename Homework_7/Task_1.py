list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

set1 = set(list_1)
set2 = set(list_2)
elements = sorted(list(set1.intersection(set2)))
print(f"Unique elements in both lists are: {elements}")
