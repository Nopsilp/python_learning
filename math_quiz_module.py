"""
Learning Objective:

Demonstrate understanding of creating and using modules in Python.
Apply built-in functions and modules to perform specific tasks.
Implement control flow logic using if statements and loops.
Design a program with a user interface and game mechanics.


Requirements:

Create a module named math_quiz that includes the following functions:

addition(): Generates two random numbers between 1 and 100, asks the user for the sum, and returns True if the answer is correct, False otherwise.
subtraction(): Generates two random numbers between 1 and 100, asks the user for the difference, and returns True if the answer is correct, False otherwise.
multiplication(): Generates two random numbers between 1 and 20, asks the user for the product, and returns True if the answer is correct, False otherwise.


Create a Python script named math_quiz_game.py that:

Imports the math_quiz module.
Implements a math quiz game with the following features:
    Presents a menu to the user to choose the type of math operation: addition, subtraction, or multiplication.
    Uses a loop to repeat the game for a specified number of rounds.
    Calls the corresponding function from the math_quiz module to generate a question and check the user's answer.
    Keeps track of the user's score by incrementing it for correct answers.
    Provides feedback to the user, displaying whether their answer is correct or incorrect.
    Displays the correct answer if the user's answer is incorrect.
    At the end of the game, displays the user's final score.
    Test the program by playing the math quiz game and verifying that it functions correctly.

By completing this exercise, you will demonstrate your proficiency in creating and using modules, utilizing built-in functions and modules, implementing control flow logic, and designing a program with a user interface and game mechanics.

"""

import random

def addition():
    random_number1 = [random.randint(1, 100), random.randint(1, 100)]
    input_prompt = "Please enter the sum of these numbers:  {0} + {1} = ?".format(random_number1[0], random_number1[1])
    try:
        sum_result = int(input(input_prompt))
    except TypeError:
        print("Error: the value you put is not integer. Please put integer")
        return None
    except Exception as e:
        print("Error: An unexpected error occurred:", str(e))
    correct_answer = random_number1[0] + random_number1[1]
    if sum_result == correct_answer:
        return sum_result, correct_answer, True
    else:
        return sum_result, correct_answer, False


def subtraction():
    random_number1 = [random.randint(1, 100), random.randint(1, 100)]
    input_prompt = "Please enter the sum of these numbers:  {0} - {1} = ?".format(random_number1[0], random_number1[1])
    try:
        subtract_result = int(input(input_prompt))
    except TypeError:
        print("Error: the value you put is not integer. Please put integer")
        return None
    except Exception as e:
        print("Error: An unexpected error occurred:", str(e))
    correct_answer = random_number1[0] - random_number1[1]
    if subtract_result == correct_answer:
        return subtract_result, correct_answer, True 
    else:
        return subtract_result, correct_answer, False

def multiplication():
    random_number1 = [random.randint(1, 100), random.randint(1, 100)]
    input_prompt = "Please enter the sum of these numbers:  {0} * {1} = ?".format(random_number1[0], random_number1[1])
    try:
        multiplication_result = int(input(input_prompt))
    except TypeError:
        print("Error: the value you put is not integer. Please put integer")
        return None
    except Exception as e:
        print("Error: An unexpected error occurred:", str(e))
    correct_answer = random_number1[0] * random_number1[1]
    if multiplication_result == correct_answer:
        return multiplication_result, correct_answer, True
    else:
        return multiplication_result, correct_answer, False