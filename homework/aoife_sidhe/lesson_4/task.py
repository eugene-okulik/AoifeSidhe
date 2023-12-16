# pylint: disable=R0801
# pylint: disable=C0206

# Lesson 4
import pprint
import datetime
import os

# Get the current date
now = datetime.datetime.now()

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


def display_menu():
    print("\nMenu:")
    print("1 - Task A")
    print("2 - Task B")
    print("3 - Task C")
    print("4 - Task D")
    print("5 - Task E - Way A")
    print("6 - Task E - Way B")
    print("t - show me THAT tuple!")
    print("0 - Exit")


def handle_option(option):
    if option == '0':
        print("\nYou've exited the program. Have a nice day!")
        return False
    if option in options:
        options[option]()
    else:
        print("Invalid option. Please try again.")
    return True


def main_menu():
    while True:
        display_menu()
        option = input("Choose an option: ").lower()
        if not handle_option(option):
            break


# Task A
def task_a():
    print()
    print("Task A - tuple")
    print("last element of the tuple:")
    print(my_dict['quantities_tuple'][-1])  # print last element of the tuple
    print()


# Task B
def task_b():
    print()
    print("Task B - list")
    print(f"Current list is {my_dict['shopping_items_list']}")
    # Making a copy of current list (.copy)
    current_list_copy = my_dict['shopping_items_list'].copy()
    item_to_add_to_the_list = "blueberries"
    print(f"Adding a {item_to_add_to_the_list}")
    my_dict['shopping_items_list'].append(item_to_add_to_the_list)  # add item at the end
    print(f"Current list is {current_list_copy} + {item_to_add_to_the_list}")
    print(f"Current list is {my_dict['shopping_items_list']}")
    second_item_to_add = my_dict['shopping_items_list'][1]
    print(f"Removing a second item - {second_item_to_add}")
    del my_dict['shopping_items_list'][1]  # remove second item
    print(my_dict['shopping_items_list'])
    print()


# Task C
# The .items() method returns a view object that displays a list of tuples
# containing the key-value pairs of a dictionary.
def display_dict():
    for key_display, value_display in my_dict['prices_dict'].items():
        if isinstance(value_display, tuple):
            print(f"{key_display}: {str(value_display)[1:-1]}")  # Print tuple values without parentheses
        else:
            print(f"{key_display}: {value_display}")


def add_today_tomorrow_date():
    today_date = (2023, 12, 16)
    tomorrow_date = (2023, 12, 17)

    # my_dict[("i am a tuple!",)] = (2023, 12, 16)
    my_dict[("Am i a tuple?",)] = today_date, tomorrow_date
    my_dict.update({'tomorrow_date': tomorrow_date})


def add_two_tuples():
    for key in [("Am i a tuple?",), 'tomorrow_date']:
        value = my_dict.get(key)
        if value is not None:
            print(f"{key}: {str(value)[1:-1]}")  # prints the tuple value without parentheses
            if isinstance(value, tuple):
                print(f"{key} is a tuple.\n")
            else:
                print(f"{key} is not a tuple, it is a {type(value).__name__}\n")


def add_requested_tuple():
    # Adding a tuple to prices_dict
    print("Add a requested tuple from the task")
    my_dict['prices_dict']["('i am a tuple',)"] = (8, 13, 21, 34, 55)
    for key in ["('i am a tuple',)"]:
        value = my_dict['prices_dict'].get(key)  # Return the value for key if key is in the dictionary, else default.
        if value is not None:
            if isinstance(value, tuple):
                print(f"\n{key}: {str(value)[1:-1]}")  # prints the tuple value without parentheses
                print(f"{key} is a tuple. Wow!\n")
            else:
                print(f"{key}:", value)
                print(f"{key} is not a tuple, it is a {type(value).__name__}\n")
        else:
            print(f"{key} is not found in prices_dict.")


def type_of_keys():
    print("Types of Keys in my_dict are:")
    type_value_all = {str(key).replace('_', ' '): type(my_dict[key]) for key in my_dict}
    print()
    for key, value in type_value_all.items():
        print(f"{key}: Class is \"{value.__name__}\"")
        # The __name__ attribute in Python is a special attribute of a class or function object.
        # It holds the name of that class or function as a string.


def task_c():
    print("\nTask C - Dictionary\n")
    display_dict()  # default dict
    print()
    print("Adding new key-value pairs for my_dict")
    print()

    add_today_tomorrow_date()
    add_two_tuples()
    add_requested_tuple()

    # print("Am i a tuple?:", my_dict[("Am i a tuple?",)])
    # print("tomorrow date:", my_dict['tomorrow_date'])

    # Check if all the above entries in dictionary are tuples
    # keys_to_check = [("i am a tuple!",), ("Am i a tuple?",), 'tomorrow_date', 'additional_items_set']
    # print("\n Types")
    # type_value_ok = {key: type(my_dict[key]) for key in keys_to_check}
    # print(type_value_ok)

    type_of_keys()

    # display key and value for my_dict prices_dict apple
    print("\nLet's check current value from prices_dict - apple")
    for key in ['apple']:
        value = my_dict['prices_dict'].get(key)  # Return the value for key if key is in the dictionary, else default.
        if value is not None:
            print(f"{key}:", value)
        else:
            print(f"{key} is not found in prices_dict.")
        if isinstance(value, tuple):
            print(f"{key} is a tuple. Damn!\n")
        else:
            print(f"{key} - obviously, it is not a tuple, it is a {type(value).__name__}\n")

    print("Deleting value from prices_dict - apple")
    print()
    # del my_dict['prices_dict']['apple']  # delete an item
    print('Current prices_dict')
    my_dict['prices_dict'].pop('apple', None)  # delete an item safely
    # We use dict.pop() function which removes a key-value pair and returns the value.
    # If the key doesn't exist, it doesn't raise error if we provide a default value.
    display_dict()  # final dict

    # some work with dictionary
    print()
    print("Checks!")
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

    print("Do we have an lemon key-value pair?")
    if 'lemon' in my_dict['prices_dict']:
        lemon_price = my_dict['prices_dict']['lemon']
        print(f"The price of a lemon is: ${lemon_price}")
    else:
        print("Lemon is not found in the prices dictionary.\n")


def task_d():
    print(f"\nTask D\nSet is: {my_dict['additional_items_set']}")
    my_dict['additional_items_set'].add("blueberries")  # add a new item
    if 'lemon' in my_dict['additional_items_set']:
        my_dict['additional_items_set'].remove('lemon')
    print(my_dict['additional_items_set'])
    # my_dict['additional_items_set'].remove('apple')  # remove an item
    my_dict['additional_items_set'].discard('apple')  # remove an item safely
    # .discard - remove an element if it is present in the set, and do nothing if the element is not present.
    print(my_dict['additional_items_set'])
    print()


def task_e_way_a():
    # Save a duplicate file descriptor of the standard output (usually the terminal)
    # File descriptor 1 represents standard output (stdout)
    standard_output = os.dup(1)

    # Redirect the standard output to a null device
    os.close(1)
    os.open(os.devnull, os.O_RDWR)

    try:
        # Run tasks A, B, and C
        task_a()
        task_b()
        task_c()
    finally:
        # Restore the standard output
        os.dup2(standard_output, 1)

    print("\nTask E - Final Dictionary\n")
    print("Way A")
    pp = pprint.PrettyPrinter(indent=0)
    for key, value in my_dict.items():
        # Display ':' for all keys in the dictionary
        if isinstance(key, str):
            print(f'{key.replace("_", " ")}:')
        else:
            # If the key is not a string, convert it to string
            print(f'{key}:')
        pp.pprint(value)
    print()


def task_e_way_b():
    # Save a duplicate file descriptor of the standard output (usually the terminal)
    # File descriptor 1 represents standard output (stdout)
    standard_output = os.dup(1)

    # Redirect the standard output to a null device
    os.close(1)
    os.open(os.devnull, os.O_RDWR)

    try:
        # Run tasks A, B, and C
        task_a()
        task_b()
        task_c()
    finally:
        # Restore the standard output
        os.dup2(standard_output, 1)

    print("\nWay B - very complex way for the cool look =)")
    for key_mydict, dict_value in my_dict.items():  # loop
        if isinstance(key_mydict, str):
            formatted_key = key_mydict.replace('_', ' ')
        else:
            formatted_key = str(key_mydict)

        # If the value is a tuple, then convert to string, remove parentheses and strip spaces
        # if isinstance(dict_value, tuple):
        #     formatted_value = str(dict_value)[1:-1].replace(" ", "")

        # If the value is a tuple, then convert to string and remove parentheses
        if isinstance(dict_value, tuple):
            formatted_value = ', '.join(map(str, dict_value))
        # Checks if the value is a other collection, Converts each item to string, joins with commas.
        elif isinstance(dict_value, (set, list)):
            formatted_value = ', '.join(str(item) for item in dict_value)
        # If the value is another dictionary, it prints the sub dictionary in a formatted way.
        elif isinstance(dict_value, dict):
            print(f'{formatted_key}:')
            for sub_key, sub_value in dict_value.items():
                if isinstance(sub_value, tuple):
                    sub_value = ', '.join(map(str, sub_value))
                    print(f'  {sub_key}: {sub_value}')
                continue

        else:
            formatted_value = dict_value
            # if the value is any other data type (such as a string or numeric value),
            # the else clause handles this by directly assigning dict_value to formatted_value.

        print(f'{formatted_key}: {formatted_value}')


def tuples_is_hard():
    print()
    # Creating a tuple with several values
    # my_tuple = (16, 'zebra', 127, 3, 9)
    # current_date_time = (now.year, now.month, now.day, now.hour, now.minute)
    cool_year = f"Current year is {now.year}"
    cool_month = f"Current month is {now.month}"
    cool_day = f"Current day is {now.day}"
    cool_hour = f"Current hour is {now.hour}"
    cool_minute = f"Current minute is {now.minute}"
    current_date_time = (cool_year, cool_month, cool_day, cool_hour, cool_minute)

    # Assigning my_tuple to the key ("i am a tuple!",) in my_dict
    my_dict[("('i am a tuple!',)",)] = current_date_time

    # Printing the key and its value if the key as a string contains "i am a tuple"
    for key_tuple, tuple_val in my_dict.items():
        # It checks if the string representation of the key contains the phrase "i am a tuple"
        # using if "i am a tuple" in str(key).
        if "i am a tuple" in str(key_tuple):
            # Convert tuple values to a comma-separated string without parentheses
            # check if both the key and value are tuples
            # In this case, the if statement doesn't have a corresponding else.
            # This means that if the condition if "i am a tuple" in str(key_tuple): is not met,
            # no action is taken for that particular key-value pair,
            # and the program moves to the next pair in the dictionary.
            if isinstance(key_tuple, tuple) and isinstance(tuple_val, tuple):
                key_str = ', '.join(map(str, key_tuple))
                # map - built-in Python function that allows to apply a specific function to every item in an iterable
                value_str = ', '.join(str(val) for val in tuple_val)  # Corrected here
                # map(str, key) and map(str, value) are used to convert each element in the key tuple and value tuple
                # into strings, respectively

                print(f"{key_str} : {value_str}")

    # Check if the object is a tuple
    if isinstance(my_dict[("('i am a tuple!',)",)], tuple):
        print("('i am a tuple!',): is a tuple.\n")
    else:
        print("('i am a tuple!',): is not a tuple.\n")


# Moved the options dictionary to the global scope
# Dictionary to map options to functions
options = {
    '1': task_a,
    '2': task_b,
    '3': task_c,
    '4': task_d,
    '5': task_e_way_a,
    '6': task_e_way_b,
    't': tuples_is_hard
    # '0': exit  # To exit from the application - not working
    # exit action is now handled separately after this dictionary
}

main_menu()

# print("i am a tuple" in "('i am a tuple!',)")  # This will output: True