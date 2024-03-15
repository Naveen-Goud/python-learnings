# Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list[0])

# Modifying elements
my_list[2] = 10
print(my_list)

# Adding elements
my_list.append(6)
print(my_list)  # Output: [1, 2, 10, 4, 5, 6]


###################
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])

# Tuple packing and unpacking
a, b, c = my_tuple[0:3]
print(a, b, c)  # Output: 1 2 3

##########################
# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict['name'])

# Modifying values
my_dict['age'] = 35
print(my_dict)

# Adding new key-value pairs
my_dict['gender'] = 'Male'
print(my_dict)


#########################
# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)
print(my_set)
my_set.remove(3)
print(my_set)
