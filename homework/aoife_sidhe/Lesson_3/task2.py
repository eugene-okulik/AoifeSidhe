# lesson2: task2_answer = x - y / (1 + x * y)
# non-interactive
import random


# Here we are declaring a function 'task_solution' which calculates a mathematical result
# based on the random values of x_value and y_value
def task_solution():
    zero_or_not_zero = random.randint(0, 1)

    if zero_or_not_zero == 0:
        x_value = random.randint(-1000, 1000)
        y_value = random.randint(-1000, 1000)
    else:
        x_value = 1
        y_value = -1

    subtraction_result = x_value - y_value
    multiplication_result = 1 + x_value * y_value

    # Check if the multiplication_result is not equal to zero (to avoid division by zero error)
    if multiplication_result != 0:
        calculation_result = subtraction_result / multiplication_result
        display_answer(x_value, y_value, calculation_result)

    # If the multiplication_result is zero, we print a friendly error message to the user
    else:
        print(f"Task2\n\n({subtraction_result}) / ({multiplication_result})")  # Printing the operation
        division_by_zero_error_message = "Save us! It is division by zero!\n"
        print(division_by_zero_error_message)


# This function prints the detailed result of a calculation operation
def display_answer(x_value, y_value, calculation_result):
    # Printing the values, using f-string for formatting
    print(f"Task2")
    print(f"\nX: {x_value}")
    print(f"Y: {y_value}")
    print(f"({x_value} - {y_value}) / (1 + {x_value} * {y_value})")  # Printing the operation
    print(f"\nAnswer: {calculation_result}")  # Printing the result of the operation


# Call the function
task_solution()
