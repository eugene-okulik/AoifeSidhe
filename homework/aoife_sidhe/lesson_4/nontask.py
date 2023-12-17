# pylint: disable=R0801

# Nested dictionary example
import pprint
import math

my_dict = {
    'outer_key1': {
        'inner_key1': '10',
        'inner_key2': '20',
        'inner_key3': '30'
    },
    'outer_key2': {
        'inner_key4': '40',
        'inner_key5': '50'
    }
}

# Printing nested dictionary
for formatted_key, dict_value in my_dict.items():
    if isinstance(dict_value, dict):
        print(f'\n{formatted_key}:\n')
        print("--------")
        print(dict_value)
        print("--------")
        print("")
        for sub_key, sub_value in dict_value.items():
            print(f'  {sub_key}: {sub_value}')

print("")
print(f"Dictionary has {len(my_dict)} keys")
print("")
# print("Way A")
# for key in my_dict:
#     print(f'{key.replace("_", " ")}:')
#     for sub_key, sub_value in my_dict[key].items():
#         print(f'  {sub_key}: {sub_value}')
# print()
print("Way A\n")
for outer_key, inner_dict in my_dict.items():
    print(f'{outer_key.replace("_", " ")}:')
    # if isinstance(inner_dict, dict):
    for sub_key, sub_value in inner_dict.items():
        print(f'  {sub_key}: {sub_value}')

print()
print("Way B")
pp = pprint.PrettyPrinter(indent=0)
for key, value in my_dict.items():
    print(f'{key.replace("_", " ")}:')
    pp.pprint(value)
print()


# map - built-in Python function that allows to apply a specific function to every item in an iterable

def square_root(num):
    return int(math.sqrt(num))


numbers = [1, 4, 9, 16]
squared = list(map(square_root, numbers))

print(numbers)
print(squared)  # [1.0, 2.0, 3.0, 4.0]
