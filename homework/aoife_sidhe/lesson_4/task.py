# pylint: disable=R0801

# Leeson 4
import pprint

# List: Represents the shopping items
shopping_items_list = ['apple', 'banana', 'orange', 'apple', 'mango', 'lemon']
# Tuple: Represents the quantities of each item
quantities_tuple = (5, 3, 4, 2, 5)  # holds a tuple. =)
# Set: Represents additional items to consider
additional_items_set = {'mango', 'pineapple', 'banana', 'apple', 'peach'}
# Dictionary: Represents prices of items
prices_dict = {
    'mango': 1.3,
    'apple': 1.5,
    'banana': 0.76,
    'pineapple': 1.2,
    'peach': 2.3,
    'orange': 2.0,
}

my_dict = {
    'shopping_items_list': shopping_items_list,
    'quantities_tuple': quantities_tuple,
    'additional_items_set': additional_items_set,
    'prices_dict': prices_dict
}

# Task A
print()
print("Task A - tuple")
print("last element of the tuple:")
print(my_dict['quantities_tuple'][-1])  # print last element of the tuple
print()

# Task B
print("Task B - list")
print(f"Current list is {my_dict['shopping_items_list']}")
# Making a copy of current list (.copy)
current_list_copy = my_dict['shopping_items_list'].copy()
ITEM_TO_ADD_TO_THE_LIST = "blueberries"
print(f"Adding a {ITEM_TO_ADD_TO_THE_LIST}")
my_dict['shopping_items_list'].append(ITEM_TO_ADD_TO_THE_LIST)  # add item at the end
print(f"Current list is {current_list_copy} + {ITEM_TO_ADD_TO_THE_LIST}")
print(f"Current list is {my_dict['shopping_items_list']}")
SECOND_ITEM_TO_ADD = my_dict['shopping_items_list'][1]
print(f"Removing a second item - {SECOND_ITEM_TO_ADD}")
del my_dict['shopping_items_list'][1]  # remove second item
print(my_dict['shopping_items_list'])
print()


# Task C
# The .items() method returns a view object that displays a list of tuples
# containing the key-value pairs of a dictionary.
def display_dict():
    for key_display, value_display in my_dict['prices_dict'].items():
        print(f"{key_display}: {value_display}")


print("\nTask C - Dictionary\n")
display_dict()  # default dict
print()
print("Adding new key-value pair for prices_dict - i am a tuple")
my_dict['prices_dict']['i am a tuple'] = 100  # add a new item
# display key and value for my_dict prices_dict apple
print("Deleting value from prices_dict - apple")
print()
del my_dict['prices_dict']['apple']  # delete an item
my_dict['prices_dict'].pop('apple', None)  # delete an item safely
# We use dict.pop() function which removes a key-value pair and returns the value.
# If the key doesn't exist, it doesn't raise error if we provide a default value.
display_dict()  # final dict

# some work with dictionary
print()
print("Checking if apple was deleted")
# Retrieving the value of 'apple' from prices_dict in my_dict
apple_price = my_dict['prices_dict'].get('apple', 'Not available')
# .get method will return a default value if the key does not exist in the dictionary.
print(f"The price of an apple is: {apple_price}")
print("Checking if we have a banana")
banana_price = my_dict['prices_dict'].get('banana', 'Not available')
print(f"The price of a banana is: {banana_price}")

try:
    print("Do we have an apple key-value pair?")
    print(my_dict['prices_dict']['apple'])
except KeyError:
    print("Apple was not found in the dictionary")

if 'lemon' in my_dict['prices_dict']:
    lemon_price = my_dict['prices_dict']['lemon']
    print(f"The price of a lemon is: ${lemon_price}")
else:
    print("Lemon is not found in the prices dictionary.")

print(f"\nTask D\nSet is: {my_dict['additional_items_set']}")
my_dict['additional_items_set'].add("blueberries")  # add a new item
if 'lemon' in my_dict['additional_items_set']:
    my_dict['additional_items_set'].remove('lemon')
print(my_dict['additional_items_set'])
my_dict['additional_items_set'].remove('apple')  # remove an item
my_dict['additional_items_set'].discard('apple')  # remove an item safely
# .discard - remove an element if it is present in the set, and do nothing if the element is not present.
print(my_dict['additional_items_set'])
print()

print("Task E - Final Dictionary\n")
print("Way A")
pp = pprint.PrettyPrinter(indent=0)
for key, value in my_dict.items():
    print(f'{key.replace("_", " ")}:')
    pp.pprint(value)
print()


def print_beautiful():
    print("Way B - very complex way for the cool look =)")
    for key_mydict, dict_value in my_dict.items():  # loop
        formatted_key = key_mydict.replace('_', ' ')  # Replaces underscores in the keys with spaces.
        # Checks if the value is a set, list, or tuple.
        # If so, it converts each item to a string, joins them with commas, and prints the formatted key and value.
        if isinstance(dict_value, (set, list, tuple)):
            # isinstance() is a built-in Python function used to determine if an object is an instance of
            # a specified class or data type.
            # This part iterates through each item in dict_value.
            # str(item) converts each item to a string representation.
            # ', '.join(...) joins these string representations together using ', ' as a separator.
            formatted_value = ', '.join(str(item) for item in dict_value)
            print(f'{formatted_key}: {formatted_value}')
        # same but with the new line for dict
        # dict_value is value from my_dict
        elif isinstance(dict_value, dict):
            print(f'{formatted_key}:')
            for sub_key, sub_value in value.items():
                print(f'  {sub_key}: {sub_value}')


print_beautiful()
