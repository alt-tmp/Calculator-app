def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function to generate Fibonacci sequence up to n
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Input from the user
num = int(input("Enter a number: "))

# Calculate and print factorial
fact = factorial(num)
print(f"Factorial of {num} is: {fact}")

# Generate and print Fibonacci sequence up to the number
fib_seq = fibonacci(num)
print(f"Fibonacci sequence up to {num}: {fib_seq}")

# Additional text output
print("\n Vedant")