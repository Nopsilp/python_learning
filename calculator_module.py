"""
Exercise:
Create a Python module called "calculator" that contains two functions: addition and multiplication. Then, create a separate Python script that imports the "calculator" module and uses these functions to perform calculations.

Requirements:

In the "calculator" module, define a function called addition that takes two parameters num1 and num2. The function should return the sum of num1 and num2.

In the "calculator" module, define a function called multiplication that takes two parameters num1 and num2. The function should return the product of num1 and num2.

Create a new Python script (e.g., main.py) in the same directory as the "calculator" module.

In the main.py script, import the "calculator" module.

Prompt the user to enter two numbers.

Use the addition function from the "calculator" module to calculate and print the sum of the two numbers entered by the user.

Use the multiplication function from the "calculator" module to calculate and print the product of the two numbers entered by the user.

Test your script by running the main.py file and verifying that the calculations are correct.

Note: Remember to consider appropriate data types and handle any potential exceptions (e.g., if the user enters non-numeric values).

Learning Objectives:

Creating and using a custom module in Python.
Defining functions with parameters and return values.
Importing and utilizing functions from a module in another script.
Implementing basic arithmetic calculations.
Feel free to modify the exercise according to you


"""

def addition(num1: int, num2: int):
    try:
        return num1 + num2
    except ZeroDivisionError:
        print("Error: division by zero is not allowed.")
        return None
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return None
    except TypeError as e:
        print("Error: Both inputs must be numeric value", str(e))
        return None
    except Exception as e:
        print("Error: An unexpected error occured:", str(e))
        return None



def multiplication(num1: int, num2: int):
    try:
        return num1 * num2
    except ZeroDivisionError:
        print("Error: division by zero is not allowed.")
        return None
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return None
    except TypeError as e:
        print("Error: Both inputs must be numeric value", str(e))
        return None
    except Exception as e:
        print("Error: An unexpected error occured:", str(e))
        return None