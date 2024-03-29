roles = {
    'admin': ['Vasya', 'Max', 'Misha'],
    'maintainer': ['Petya', 'Kostya', 'Ivan'],
    'manager': ['Sam', 'Eugene', 'Oleg'],
    'developer': ['Natalia', 'Yulia', 'Alisa']}

name = input("Enter the name: ")  # .lower()  Had a mistake when I want to add this, suggest smth...

for role, users in roles.items():
    if name in users:
        print(f'Hello, {role}')
        break
else:
    print("Hello, Guest")
