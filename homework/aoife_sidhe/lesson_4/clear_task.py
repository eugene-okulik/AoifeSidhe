# pylint: disable=R0801

# Leeson 4

# Import necessary libraries
import pprint
import datetime
import os

# Get the current date and time
# noinspection DuplicatedCode
now = datetime.datetime.now()

# Define initial data
shopping_items_list = ['apple', 'banana', 'orange', 'apple', 'mango', 'lemon']
quantities_tuple = (5, 3, 4, 2, 5)  # holds a tuple. =)
additional_items_set = {'mango', 'pineapple', 'banana', 'apple', 'peach'}
prices_dict = {
    'mango': 1.3,
    'apple': 1.5,
    'banana': 0.76,
    'pineapple': 1.2,
    'peach': 2.3,
    'orange': 2.0,
}

# Dictionary with all the data
my_dict = {
    'shopping_items_list': shopping_items_list,
    'quantities_tuple': quantities_tuple,
    'additional_items_set': additional_items_set,
    'prices_dict': prices_dict
}


def main_menu():
    """Displays the main menu and calls the respective function based on user input."""
    options = {
        '1': task_a,
        '2': task_b,
        '3': task_c,
        '4': task_d,
        '5': task_e_way_a,
        '6': task_e_way_b,
        't': tuples_is_hard,
        'f': task_fun,
    }

    while True:
        print("\nMenu:")
        print("1 - Task A")
        print("2 - Task B")
        print("3 - Task C")
        print("4 - Task D")
        print("5 - Task E - Way A")
        print("6 - Task E - Way B")
        print("t - Show me THAT tuple!")
        print("f - Prints the list in reverse order.")
        print("0 - Exit")

        option = input("Choose an option: ").lower()
        if option == '0':
            print("\nYou've exited the program. Have a nice day!")
            break
        elif option in options:
            options[option]()
        else:
            print("Invalid option. Please try again.")


# Task A
# noinspection DuplicatedCode
def task_a():
    """Displays the last element from the quantities tuple."""
    print()
    print("Task A - tuple")
    print("last element of the tuple:")
    print(my_dict['quantities_tuple'][-1])
    print()


# Task B
def task_b():
    """'Demonstrates operations on a list."""
    print()
    print("Task B - list")
    print(f"Current list is {my_dict['shopping_items_list']}")
    current_list_copy = my_dict['shopping_items_list'].copy()
    ITEM_TO_ADD_TO_THE_LIST = "blueberries"
    print(f"Adding a {ITEM_TO_ADD_TO_THE_LIST}")
    my_dict['shopping_items_list'].append(ITEM_TO_ADD_TO_THE_LIST)
    print(f"Current list is {current_list_copy} + {ITEM_TO_ADD_TO_THE_LIST}")
    print(f"Current list is {my_dict['shopping_items_list']}")
    SECOND_ITEM_TO_ADD = my_dict['shopping_items_list'][1]
    print(f"Removing a second item - {SECOND_ITEM_TO_ADD}")
    del my_dict['shopping_items_list'][1]
    print(my_dict['shopping_items_list'])
    print()


# Task C
def display_dict():
    """Prints the key-value pairs from a dictionary."""
    for key_display, value_display in my_dict['prices_dict'].items():
        if isinstance(value_display, tuple):
            print(f"{key_display}: {str(value_display)[1:-1]}")  # Print tuple values without parentheses
        else:
            print(f"{key_display}: {value_display}")


def print_value_and_type(key):
    """Prints the key-value pair and its type from a dictionary."""
    value = my_dict.get(key, None)
    print(f"{key}:", value)

    if isinstance(value, tuple):
        print(f"{key} is a tuple.\n")
    else:
        print(f"{key} is not a tuple, it is a {type(value)}\n")


# noinspection DuplicatedCode
def task_c():
    """Performs operations on a dictionary and demonstrates its usage."""
    print("\nTask C - Dictionary\n")
    display_dict()
    print("Adding new key-value pairs for my_dict")
    print()

    today_date = (2023, 12, 16)
    tomorrow_date = (2023, 12, 17)

    my_dict[("Am i a tuple?",)] = today_date, tomorrow_date
    my_dict.update({'tomorrow_date': tomorrow_date})

    for key in [("Am i a tuple?",), 'tomorrow_date']:
        value = my_dict.get(key)
        if value is not None:
            print(f"{key}: {str(value)[1:-1]}")
            if isinstance(value, tuple):
                print(f"{key} is a tuple.\n")
            else:
                print(f"{key} is not a tuple, it is a {type(value).__name__}\n")

    # Adding a tuple to prices_dict
    print("Add a requested tuple from the task")
    my_dict['prices_dict']["('i am a tuple',)"] = (8, 13, 21, 34, 55)
    for key in ["('i am a tuple',)"]:
        value = my_dict['prices_dict'].get(key)
        if value is not None:
            if isinstance(value, tuple):
                print(f"\n{key}: {str(value)[1:-1]}")
                print(f"{key} is a tuple. Wow!\n")
            else:
                print(f"{key}:", value)
                print(f"{key} is not a tuple, it is a {type(value).__name__}\n")
        else:
            print(f"{key} is not found in prices_dict.")

    print("Types of Keys in my_dict are:")
    type_value_all = {str(key).replace('_', ' '): type(my_dict[key]) for key in my_dict}
    print()
    for key, value in type_value_all.items():
        print(f"{key}: Class is \"{value.__name__}\"")

    print("\nLet's check current value from prices_dict - apple")
    for key in ['apple']:
        value = my_dict['prices_dict'].get(key)
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

    print('Current prices_dict')
    my_dict['prices_dict'].pop('apple', None)
    display_dict()

    print()
    print("Checks!")
    print()
    print("Checking if apple was deleted")

    apple_price = my_dict['prices_dict'].get('apple', 'Not available')

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


# noinspection DuplicatedCode
def task_d():
    """Performs operations on a set."""
    print(f"\nTask D\nSet is: {my_dict['additional_items_set']}")
    my_dict['additional_items_set'].add("blueberries")
    if 'lemon' in my_dict['additional_items_set']:
        my_dict['additional_items_set'].remove('lemon')
    print(my_dict['additional_items_set'])
    my_dict['additional_items_set'].discard('apple')
    print(my_dict['additional_items_set'])
    print()


def task_e_way_a():
    """Demonstrates the first way of completing task E - to display a dictionary"""

    standard_output = os.dup(1)

    os.close(1)
    os.open(os.devnull, os.O_RDWR)

    try:
        task_a()
        task_b()
        task_c()
    finally:
        os.dup2(standard_output, 1)

    print("\nTask E - Final Dictionary\n")
    print("Way A")
    pp = pprint.PrettyPrinter(indent=0)
    for key, value in my_dict.items():
        if isinstance(key, str):
            print(f'{key.replace("_", " ")}:')
        else:
            print(f'{key}:')
        pp.pprint(value)
    print()


def task_e_way_b():
    """Demonstrates the second way of completing task E - to display a dictionary"""
    standard_output = os.dup(1)

    os.close(1)
    os.open(os.devnull, os.O_RDWR)

    try:
        task_a()
        task_b()
        task_c()
    finally:
        os.dup2(standard_output, 1)

    print("\nWay B - very complex way for the cool look =)")
    for key_mydict, dict_value in my_dict.items():  # loop
        if isinstance(key_mydict, str):
            formatted_key = key_mydict.replace('_', ' ')
        else:
            formatted_key = str(key_mydict)

        if isinstance(dict_value, tuple):
            formatted_value = ', '.join(map(str, dict_value))
        elif isinstance(dict_value, (set, list)):
            formatted_value = ', '.join(str(item) for item in dict_value)
        elif isinstance(dict_value, dict):
            print(f'{formatted_key}:')
            for sub_key, sub_value in dict_value.items():
                if isinstance(sub_value, tuple):
                    sub_value = ', '.join(map(str, sub_value))
                    print(f'  {sub_key}: {sub_value}')
                continue

        else:
            formatted_value = dict_value

        print(f'{formatted_key}: {formatted_value}')


def tuples_is_hard():
    """Displays the current date and time in a tuple format."""
    print()
    cool_year = f"Current year is {now.year}"
    cool_month = f"Current month is {now.month}"
    cool_day = f"Current day is {now.day}"
    cool_hour = f"Current hour is {now.hour}"
    cool_minute = f"Current minute is {now.minute}"
    current_date_time = (cool_year, cool_month, cool_day, cool_hour, cool_minute)

    my_dict[("('i am a tuple!',)",)] = current_date_time

    for key_tuple, tuple_val in my_dict.items():
        if "i am a tuple" in str(key_tuple):
            if isinstance(key_tuple, tuple) and isinstance(tuple_val, tuple):
                key_str = ', '.join(map(str, key_tuple))
                value_str = ', '.join(str(val) for val in tuple_val)
                print(f"{key_str} : {value_str}")

    if isinstance(my_dict[("('i am a tuple!',)",)], tuple):
        print(f"('i am a tuple!',): is a tuple.\n")
    else:
        print(f"('i am a tuple!',): is not a tuple. =)\n")


def task_fun():
    """Prints the list in reverse order."""
    print("\nTask B - list")
    print(f'Current order: {my_dict["shopping_items_list"]}')
    print("shopping items list in reverse order:")
    print(my_dict['shopping_items_list'][::-1])
    print()


# Start the program
main_menu()
