num1 = float(input("Enter first digit: "))
num2 = float(input("Enter second digit: "))
operation = input("Enter name of the operation: ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    print("Try again")
print(result)