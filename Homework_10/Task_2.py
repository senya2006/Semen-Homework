def is_prime(num):
    if not 2 <= num <= 1000:
        return False
    for digit in range(2, int(num ** 0.5) + 1):
        if num % digit == 0:
            return False
    return True

num = int(input("Enter the digit that you want to check for prime number from 2 to 1000: "))

if is_prime(num):
    print(f"Number: {num} is prime")
else:
    print(f"Number: {num} is not prime")
