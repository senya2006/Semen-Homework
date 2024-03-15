str1 = input("Enter the string")

str1 = str1.replace(' ','').lower()
palindrome = str1 == ''.join(reversed(str1))

if palindrome:
    print("string is polendrome")
else:
    print("string is not polendrome")