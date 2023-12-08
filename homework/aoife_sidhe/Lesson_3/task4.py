# Lesson 4 - Given the sides of a right-angled triangle, find its hypotenuse and area
# non-interactive

import random


# Here we are declaring a function 'task_solution' which calculates a mathematical result
# based on the random values of x_value and y_value
def task_solution():
    x_value, y_value = generate_numbers()
    # Hypotenuse can be calculated by using the Pythagorean theorem: c = sqrt(a^2 + b^2)
    hypotenuse = (x_value ** 2 + y_value ** 2) ** 0.5
    # Area of a right-angled triangle is given by the formula:
    # area = 1/2 * base * height, where base and height are the given sides.
    area = 0.5 * x_value * y_value
    # Call the display_answer function with correct arguments
    display_answer(x_value, y_value, hypotenuse, area)
    return hypotenuse, area


# This function prints the detailed result of a calculation operations, using f-string for formatting
def display_answer(x_value, y_value, hypotenuse, area):
    print("Task 4\n")
    print(f"X value: {x_value}\nY value: {y_value}\n")
    print(f"Hypotenuse: {hypotenuse}\nArea: {area}")


# Function to generate random numbers for calculations.
def generate_numbers():
    x_value = random.randint(1, 1000)
    y_value = random.randint(1, 1000)
    return x_value, y_value


task_solution()
