import calculator_module

user_num1 = input("Enter the first number: ")
user_num2 = input("Enter the second number: ")

try:
    user_num1 = int(user_num1)
    user_num2 = int(user_num2)

    addition_result = calculator_module.addition(user_num1, user_num2)
    multiplication_result = calculator_module.multiplication(user_num1, user_num2)

    print("The result from addition is: {}".format(addition_result))
    print("The result from multiplication is: {}".format(multiplication_result))

except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
except Exception as e:
    print("Error: An unexpected error occurred:", str(e))

