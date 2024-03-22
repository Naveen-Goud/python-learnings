# Define a generator function to generate Fibonacci numbers
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Create a generator object
fibonacci = fibonacci_generator(10)

print("Fibonacci numbers generated using a generator:")
for num in fibonacci:
    print(num)
