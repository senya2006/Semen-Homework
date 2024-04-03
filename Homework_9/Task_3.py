course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}

try:
    key = input("Enter the key: ")
    value = course[key]
except KeyError:
    print("No such key exists!")
else:
    print(f"Value for key '{key}': {value}")
