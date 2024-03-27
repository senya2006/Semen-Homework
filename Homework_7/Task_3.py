numbers = [1, 2, 3, 4, 5, 6, 2, 7, 8, 9, 11]
unique_numbers = set(numbers)
if len(numbers) == len(set(numbers)):
    print(f"This set: {numbers} are unique")
else:
    print(f"This set: {numbers} have similar numbers")
