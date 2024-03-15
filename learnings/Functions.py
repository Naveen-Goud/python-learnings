def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Call the function
num = 17
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")


def reverse_string(input_string):
    return input_string[::-1]

# Call the function
string = "hello world"
reversed_string = reverse_string(string)
print("Original string:", string)
print("Reversed string:", reversed_string)
