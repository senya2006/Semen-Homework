class CustomFunctions:
    def my_max(self, iterable):
        if not iterable:
            raise ValueError("max() num is an empty range")
        max_value = iterable[0]
        for num in iterable:
            if num > max_value:
                max_value = num
        return max_value

    def my_min(self, iterable):
        if not iterable:
            raise ValueError("min() num is an empty range")
        min_value = iterable[0]
        for item in iterable:
            if item < min_value:
                min_value = item
        return min_value


numbers = [12, 56565, -34, 0, 767, -455]
for_check = CustomFunctions()
print(f"My max: {for_check.my_max(numbers)}")
print(f"My min: {for_check.my_min(numbers)}")
