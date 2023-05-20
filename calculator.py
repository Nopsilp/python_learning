"""
Exercise: Calculator Functions

The learning objectives of this exercise include:
    Practicing the creation and definition of functions in Python.
    Understanding how to use parameters and return values in functions.
    Implementing mathematical operations using functions.
    Applying basic control flow concepts (if statements, loops) to handle potential errors or edge cases.
    Reinforcing the understanding of basic syntax and data types (numbers, strings) in Python.
    Getting familiar with running Python scripts and observing the output.

Steps:
    Create a Python script called calculator.py.
    Implement four functions in the calculator.py script: add, subtract, multiply, and divide.
    Each function should take two numbers as parameters and perform the respective mathematical operation.
    The add function should return the sum of the two numbers.
    The subtract function should return the difference between the two numbers.
    The multiply function should return the product of the two numbers.
    The divide function should return the result of dividing the first number by the second number.
    Use the functions to perform the following calculations:
        a. Add 5 and 3, and store the result in a variable called result_add.
        b. Subtract 7 from 10, and store the result in a variable called result_subtract.
        c. Multiply 4 and 6, and store the result in a variable called result_multiply.
        d. Divide 15 by 3, and store the result in a variable called result_divide.
    Print the values of result_add, result_subtract, result_multiply, and result_divide.


"""

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 // number_2


result_add = add(5, 3)
result_subtract = subtract(10, 7)
result_multiply = multiply(4, 6)
result_divide = divide(15, 3)

print("The add result is", result_add)
print("The subtract result is", result_subtract)
print("The multiply result is", result_multiply)
print("The divide result is", result_divide)