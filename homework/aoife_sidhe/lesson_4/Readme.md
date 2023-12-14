# TASK README

This is a Python script exploring various basic programming concepts and operations. Below is a breakdown of its
components:

## Data Structures

- **shopping_items_list**: A list.
- **quantities_tuple**: A tuple.
- **additional_items_set**: A sett.
- **prices_dict**: A dictionary.
- **my_dict**: A dictionary to rule them all

## Tasks

### English:
- **For the value stored under the key 'tuple':**
    - Display the last element.

- **For the value stored under the key 'list':**
    - Add one more element to the end of the list.
    - Remove the second element from the list.

- **For the value stored under the key 'dict':**
    - Add an element with the key ('i am a tuple') and any value.
    - Remove any element.

- **For the value stored under the key 'set':**
    - Add a new element to the set.
    - Remove an element from the set.


## Functions

- **display_dict**: This function displays the keys & values of a dictionary.
- **print_beautiful**: This function is used to print a complex data structure in a readable
  format.

## Imports
**The pprint module** stands for "pretty printer". <br>
It is a Python built-in module that provides the capability to print Python data types to the console in a **_prettier_**,
more readable format. <br>
This can be **especially useful** when we are trying to debug or inspect data structures like nested lists or dictionaries.


## Additional File
Feel free to skip it - i created it only for myself.
**notask** - This Python script is a demonstration of handling nested dictionaries and various methods of presenting
nested dictionaries to the user.

_**It begins**_ with creating a nested dictionary named my_dict with two primary keys: outer_key1 and outer_key2. <br>
Each of these keys holds another dictionary containing inner keys and their corresponding values.

In the ***next section,*** the script prints this nested dictionary in a readable format. <br>
For each key-value pair in my_dict, it checks if the value is also a dictionary. <br>
If it is, then the script further prints the inner keys and their respective values.

**_Following that,_** it prints the **total number of outer keys in my_dict.** <br>
`{len(my_dict)} keys")`

Then, the script demonstrates **two ways to print nested dictionaries** with formatted keys. 

* In Way A, it directly iterates over the keys and sub-keys in my_dict and prints them with their associated values.
* In Way B, the script uses the pprint (Pretty Printer) module for the same purpose. <br>
It creates an instance of PrettyPrinter with an indentation level of 0. <br>
It then iterates over the keys and values of my_dict, replacing the underscores in the keys with a space for better readability<br> 
It also uses the PrettyPrinter instance to print each nested dictionary in a more aesthetically pleasing format.

` print(f'{key.replace("_", " ")}:')`

