
# Conditional Statement (if-else)
num = 10  # Assignment Statement
if num > 0:
    print("Positive number")
else:
    print("Non-positive number")


# Loop Statement (for loop)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop Statement (while loop)
count = 0
while count < 5:
    print(count)
    count += 1

# Function Definition
def greet(name):
    print("Hello, " + name + "!")

# Return Statement
def add(x, y):
    return x + y


# Class Definition
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(self.name + " says woof!")


# Exception Handling (try-except)
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")

