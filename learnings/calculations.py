
import math_operations
from my_package import string_operations

# Using functions from the math_operations module
print("Addition:", math_operations.add(5, 3))
print("Subtraction:", math_operations.subtract(5, 3))
print("Multiplication:", math_operations.multiply(5, 3))
print("Division:", math_operations.divide(5, 3))

# Using functions from the string_operations module inside the package
print("Concatenation:", string_operations.concatenate("Hello, ", "world!"))
print("Capitalization:", string_operations.capitalize_first_letter("python modules and packages"))
