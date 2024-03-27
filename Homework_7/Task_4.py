elements = [1, 5, 68, 0]
min1 = 0
for element in elements:
    if min1 == 0 or element < min1:
        min1 = element
print(f"The minimum number in this list of elements:{elements} is {min1}")
