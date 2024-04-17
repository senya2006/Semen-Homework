def my_max(*args):
    if not args:
        raise ValueError("my_max() arg is an empty range")
    max_value = args[0]
    for arg in args[1:]:
        if arg > max_value:
            max_value = arg
    return max_value

def my_min(*args):
    if not args:
        raise ValueError("my_min() arg is an empty range")
    min_value = args[0]
    for arg in args[1:]:
        if arg < min_value:
            min_value = arg
    return min_value

numbers = [12, 56565, -34, 0, 767, -455]
print(f"My max: {my_max(*numbers)}")
print(f"My min: {my_min(*numbers)}")
