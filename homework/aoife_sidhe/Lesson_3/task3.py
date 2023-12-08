# Lesson 3: arithmetic mean, geometric mean
# non-interactive
import random


# Here we are declaring a function 'task_solution' which calculates a mathematical result
# based on the random values of x_value and y_value
def task_solution():
    x_value, y_value = generate_numbers()
    arithmetic_mean = (x_value + y_value) / 2
    geometric_mean = (x_value * y_value) ** 0.5
    # Call the display_answer function with correct arguments
    display_answer(x_value, y_value, arithmetic_mean, geometric_mean)
    return arithmetic_mean, geometric_mean


# This function prints the detailed result of a calculation operations, using f-string for formatting
def display_answer(x_value, y_value, arithmetic_mean, geometric_mean):
    print(f"Task 3\n")
    print(f"X value: {x_value}")
    print(f"y value: {y_value}\n")
    print(f"Arithmetic mean: {arithmetic_mean}")
    print(f"Geometric mean: {geometric_mean}")


# Function to generate random numbers for calculations.
def generate_numbers():
    x_value = random.randint(0, 1000)
    y_value = random.randint(0, 1000)
    return x_value, y_value


# Call the function
task_solution()
