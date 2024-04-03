course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}

try:
    key = input("Enter the key: ")
    value = course[key]
    print(f"Value for key '{key}': {value}")
except KeyError:
    print("No such key exists!")
