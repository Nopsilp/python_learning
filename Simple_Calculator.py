print("Simple Calculator")
number_1 = int(input("Enter 1st number here:"))
number_2 = int(input("Enter 1st number here:"))
operator = input("Enter an operator (+, -, *, or /) here:")

def calculator(number_1, number_2, operator):
    if operator == "+":
        result = number_1 + number_2
    elif operator == "-":
        result = number_1 - number_2
    elif operator == "*":
        result = number_1 * number_2
    elif operator == "/":
        result = number_1 / number_2
    else:
        result = "Please enter either +, -, *, or / only.\n It seems like you entered incorrect operator."  
    
    return result

print("The result is:" + str(calculator(number_1, number_2, operator)))