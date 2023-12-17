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
last_element_tuple = my_dict['tuple'][-1]
print("Last element in 'tuple':", last_element_tuple)

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
values_for_tuple = 100,
# my_dict[('i am a tuple!',)] = random_values
my_dict['dict'][('i am a tuple!',)] = values_for_tuple

# Removing an arbitrary element from the dictionary, let's remove 'key3'
del my_dict['dict']['key3']

key_name = ('i am a tuple!',)
# Print the key-value pair
print(f"{key_name}: {my_dict['dict'][key_name]}")
if isinstance(my_dict['dict'][key_name], tuple):
    print(f"{key_name}: is a tuple.\n")
else:
    print(f"{key_name}: is not a tuple.\n")

key_name = "('i am a tuple',)"
my_dict['dict'][key_name] = 100  # add a new key-value pair
value_type = str(type(my_dict['dict'][key_name]))[8:-2]
print(f"{key_name}: {my_dict['dict'][key_name]}")

if isinstance(my_dict['dict'][key_name], tuple):
    print(f"{key_name} : is a tuple.\n")
else:
    print(f"{key_name} : is not a tuple. It is of type {value_type}.")
    print("Deleting...")
    del my_dict['dict'][key_name]

# For 'set':
print("\n****************************\n")
print(f"My set was {my_dict['my_set']}")
my_dict['my_set'].add(30)  # Adding a new element to the set
my_dict['my_set'].pop()  # Removing an arbitrary element from the set
print(f"My set is {my_dict['my_set']}\n")

# Print all keys in my_dict
print("Print all keys in my_dict...")
for key in my_dict.keys():
    print(key)
    if isinstance(my_dict[key], dict):
        print("\t... and its keys:")
        for sub_key in my_dict[key]:
            print("\t", sub_key)

# We can also check if the key is a tuple, and if so, print its elements:
print("\nIf key is a tuple, print its elements...")
for key in my_dict.keys():
    if isinstance(key, tuple):
        print(f"Key '{key}' is a tuple with elements:")
        for i, tuple_element in enumerate(key):
            print(f"  Element {i}: {tuple_element}")

# Print the value of a particular key in my_dict
particular_key = ('i am a tuple!',)
print(my_dict['dict'][particular_key])

# Displaying the updated dictionary
print("\nFinal Result:")
p(my_dict)
