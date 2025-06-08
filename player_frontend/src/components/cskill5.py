# Hill Climbing Algorithm to minimize f(x) = x^2

# Define the objective function
def f(x):
    return x ** 2

# Starting point
x = -10
print(f"Starting at: x = {x}, f(x) = {f(x)}")

# Hill climbing loop to minimize the function
while x < 0:
    # Move towards the minimum by incrementing x
    x += 1
    print(f"Move to: x = {x}, f(x) = {f(x)}")

# Final result
print(f"Local minimum found: x = {x}, f(x) = {f(x)}")
print("Vedant")