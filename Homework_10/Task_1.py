def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "You can't divide by zero!"
    else:
        return x / y
def calculator(x, y, operation):
    if operation == '+':
        return add(x, y)
    elif operation == '-':
        return subtract(x, y)
    elif operation == '*':
        return multiply(x, y)
    elif operation == '/':
        return divide(x, y)
    else:
        return "Incorrect operation!"

num1 = float(input("Enter first digit: "))
num2 = float(input("Enter second digit: "))
operation = input("Enter operation (+,-,*,/): ")

result = calculator(num1, num2, operation)
print(f"The result: {result}")
