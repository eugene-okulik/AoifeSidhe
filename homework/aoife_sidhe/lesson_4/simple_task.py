# pylint: disable=C0206
# Lesson 4 - simple

import random

from pprint import pprint as p

# Creating the dictionary
my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'},
    'my_set': {5, 10, 15, 20, 25}
}

# Actions for elements in the dictionary

print("Homework 4\n")

# For 'tuple':
LAST_ELEMENT_TUPLE = my_dict['tuple'][-1]
print("Last element in 'tuple':", LAST_ELEMENT_TUPLE)

# For 'list':
print(f"\nList was {my_dict['list']}")
my_dict['list'].append(60)  # Adding another element at the end of the list
del my_dict['list'][1]  # Deleting the second element from the list
print(f"List is {my_dict['list']}")

# For 'dict':
print("\n****************************")
print("\nDictionary\n")
random_values = tuple(random.randint(0, 100) for _ in range(6))
# my_dict[('i am a tuple!',)] = 100
values_for_tuple = (100,)
# my_dict[('i am a tuple!',)] = random_values
my_dict['dict'][('i am a tuple!',)] = values_for_tuple

# Removing an arbitrary element from the dictionary, let's remove 'key3'
del my_dict['dict']['key3']

KEY_NAME = ('i am a tuple!',)
# Print the key-value pair
print(f"{KEY_NAME}: {my_dict['dict'][KEY_NAME]}")
if isinstance(my_dict['dict'][KEY_NAME], tuple):
    print(f"{KEY_NAME}: is a tuple.\n")
else:
    print(f"{KEY_NAME}: is not a tuple.\n")

KEY_NAME = "('i am a tuple',)"
my_dict['dict'][KEY_NAME] = 100  # add a new key-value pair
VALUE_TYPE = str(type(my_dict['dict'][KEY_NAME]))[8:-2]
print(f"{KEY_NAME}: {my_dict['dict'][KEY_NAME]}")

if isinstance(my_dict['dict'][KEY_NAME], tuple):
    print(f"{KEY_NAME} : is a tuple.\n")
else:
    print(f"{KEY_NAME} : is not a tuple. It is of type {VALUE_TYPE}.")
    print("Deleting...")
    del my_dict['dict'][KEY_NAME]

# For 'set':
print("\n****************************\n")
print(f"My set was {my_dict['my_set']}")
my_dict['my_set'].add(30)  # Adding a new element to the set
my_dict['my_set'].pop()  # Removing an arbitrary element from the set
print(f"My set is {my_dict['my_set']}\n")

# Print all keys in my_dict
print("\n****************************\n")
print("Print all keys in my_dict...\n")
for key, value in my_dict.items():
    print(f'{key}: {value}')
    if isinstance(my_dict[key], dict):
        print("\t... and its keys:")
        for sub_key, sub_value in my_dict[key].items():
            print(f'{sub_key}: {sub_value}')

# We can also check if the key is a tuple, and if so, print its elements:
print("\nIf key is a tuple, print its elements...")
for key, value in my_dict['dict'].items():
    if isinstance(key, tuple):
        print(f"Key '{key}' is a tuple with elements:")
        for i, tuple_element in enumerate(key):
            print(f"  Element {i}: {tuple_element}")
        print(f"Value associated with tuple key '{key}': {value}")

print("\n****************************\n")


# Print the value of a particular key in my_dict
# particular_key = ('i am a tuple!',)
# print(my_dict['dict'][particular_key])

# Displaying the updated dictionary
print("\nFinal Result:")
p(my_dict)
