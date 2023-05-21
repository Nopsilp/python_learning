"""
Exercise: Word Counter

Learning Objectives:
    Function Definition: Define a function in Python with appropriate parameters and return values.
    String Manipulation: Perform operations on strings, such as counting words, splitting strings, and accessing string elements.
    Control Flow: Implement control flow constructs, such as loops and conditional statements, to solve a problem.
    Problem Solving: Analyze the requirements of the task and design a solution algorithm using the available Python language features.
    Testing and Debugging: Verify the correctness of the function by testing it with different inputs and handling potential edge cases.
    Code Readability: Write clean and readable code by following naming conventions, using appropriate indentation, and adding comments where necessary.

Steps:

Write a Python function called `word_counter` that takes a string as input and returns the number of words in the string. Assume that words in the string are separated by a single space.
For example, given the input string "Hello world, how are you?", the function should return the value `5`, as there are five words in the string.
Write the `word_counter` function and test it with different input strings to verify its correctness.

"""

def word_counter(string):
    list_of_word = string.split()
    counter = 0
    for word in list_of_word:
        counter += 1
    return counter

user_string = input("Enter a sentence here:")

result = word_counter(user_string)
print("The number of words: {}".format(result))
