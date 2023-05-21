import calculator_module

user_num1 = int(input("Enter 1st number:"))
user_num2 = int(input("Enter 2nd number:"))

addition_result = calculator_module.addition(user_num1, user_num2)
multiplication_result = calculator_module.multiplication(user_num1, user_num2)

print("The result from addition is: {}".format(addition_result))
print("The result from multiplication is: {}".format(multiplication_result))