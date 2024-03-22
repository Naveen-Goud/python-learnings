
numbers = [1, 2, 3, 4, 5]

#  Use lambda function to double each number in the list
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("Doubled numbers:", doubled_numbers)

# Use lambda function to filter even numbers from the list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

#Use lambda function to sort a list of tuples based on the second element
pairs = [(1, 3), (2, 1), (5, 2), (4, 4)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Sorted pairs by second element:", sorted_pairs)
