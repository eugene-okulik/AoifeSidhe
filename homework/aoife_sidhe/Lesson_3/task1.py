# Lesson 1: x + y, x - y, y - x, x * y
# non-interactive
import random


# Here we are declaring a function 'task_solution' which calculates a mathematical result
# based on the random values of x_value and y_value
def task_solution():
    x_value, y_value = generate_numbers()
    multiplication_result = x_value * y_value
    subtraction_result1 = x_value - y_value
    subtraction_result2 = y_value - x_value
    addition_result = x_value + y_value
    # Call the display_answer function with correct arguments
    display_answer(x_value, y_value, multiplication_result, subtraction_result1, subtraction_result2, addition_result)
    return multiplication_result, subtraction_result1, addition_result, subtraction_result2


# This function prints the detailed result of a calculation operations, using f-string for formatting
def display_answer(x_value, y_value, multiplication_result, subtraction_result1,
                   subtraction_result2, addition_result):
    print(f"Task1\n")
    print(f"x_value: {x_value}")
    print(f"y_value: {y_value}\n")
    print(f"Multiplication result: {multiplication_result}")
    print(f"Subtraction result 1: {subtraction_result1}")
    print(f"Subtraction result 2: {subtraction_result2}")
    print(f"Addition result: {addition_result}")


# Hewe we generate random numbers for calculations.
def generate_numbers():
    x_value = random.randint(-1000, 1000)
    y_value = random.randint(-1000, 1000)
    return x_value, y_value


# Call the function
task_solution()
