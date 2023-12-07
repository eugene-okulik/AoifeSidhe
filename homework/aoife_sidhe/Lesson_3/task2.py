# Lesson2: x - y / (1 + x * y)
# non-interactive
import random


# Here we are declaring a function 'task_solution' which calculates a mathematical result
# based on the random values of x_value and y_value
def task_solution():
    zero_or_not_zero, x_value, y_value = generate_numbers()
    multiplication_result = 1 + x_value * y_value
    subtraction_result = x_value - y_value
    # the error message in a variable
    division_by_zero_error_message = "Save us! It is division by zero!"
    # If the multiplication_result is not zero we proceed with calculations
    if multiplication_result != 0:
        calculation_result = subtraction_result / multiplication_result
    else:
        # If the multiplication_result is zero, we assign the error message to calculation_result
        calculation_result = division_by_zero_error_message
    # Call the display_answer function with correct arguments
    display_answer(x_value, y_value, calculation_result, zero_or_not_zero, multiplication_result, subtraction_result)
    return multiplication_result, subtraction_result


# This function prints the detailed result of a calculation operations, using f-string for formatting
def display_answer(x_value, y_value, calculation_result, zero_or_not_zero, multiplication_result, subtraction_result):
    example_l = ""
    if zero_or_not_zero == 1:
        example_l = "VarA"
    if zero_or_not_zero == 0:
        example_l = "Var B"
    print(f"Task2 - {example_l}\nX: {x_value}\nY: {y_value}")
    print(f"\nOperation: (x - y) / (1 + x * y)")  # Print the operation
    print(f"It is: {subtraction_result} / {multiplication_result} ")  # Print the operation with values
    print(f"\nAnswer: {calculation_result}")  # Print the result of the operation


# Hewe we generate random numbers for calculations.
def generate_numbers():
    zero_or_not_zero = random.randint(0, 1)
    x_value, y_value = 1, -1  # Divide by zero case
    if zero_or_not_zero == 1:  # Random numbers for our calculations
        x_value = random.randint(-1000, 1000)
        y_value = random.randint(-1000, 1000)
    return zero_or_not_zero, x_value, y_value


# Call the function
task_solution()
