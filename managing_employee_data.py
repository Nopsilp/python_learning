
employee_records = []
def add_employee (employee_records):
    employee_details = {}
    print("Please put the details of the employee.")
    try:
        employee_details["name"] = input("Name:")
        employee_details["age"] = int(input("Age (enter a positive integer):"))
        employee_details["department"] = (input("Depeartment:"))
        employee_details["salary"] = float(input("Salary (enter a positive or non-negative number):"))
        employee_records.append(employee_details)
        print("The employee's details were added successfully!")
    except ValueError:
        print("Error: Please use correct type.")
    


def update_employee (employee_records):
    employee_name = input("Enter the name of the employee to update: ")
    for employee in employee_records:
        if employee_name.lower() == employee["name"].lower():
            employee_key_update = input("Put the detail you'd like to update (name, age, department, salary). Only one at a time:")
            employee_detail_list = ["name", "age", "department", "salary"]
                            
            if employee_key_update.lower() in employee_detail_list:
                if employee_key_update == "name":
                    updated_employee_name = input("Put the updated name:")
                    new_employee_dictionary = {"name": updated_employee_name}
                    employee.update(new_employee_dictionary)
                elif employee_key_update == "age":
                    updated_employee_age = int(input("Put the updated age:"))
                    new_employee_dictionary = {"age": updated_employee_age}
                    employee.update(new_employee_dictionary)
                elif employee_key_update == "department":
                    updated_employee_department = input("Put the updated department:")
                    new_employee_dictionary = {"department": updated_employee_department}
                    employee.update(new_employee_dictionary)
                else:
                    updated_employee_salary = float(input("Put the updated salary:"))
                    new_employee_dictionary = {"salary": updated_employee_salary}
                    employee.update(new_employee_dictionary)
                
                print("Updated successfully!")
                

            else:         
                print("Please put only 1 of these 4: name, age, department, salary")
                break
             
        else:
            print(f"{employee_name} is not found in our database.")
            break

def remove_employee (employee_records):
    employee_name = input("Enter the name of the employee to remove:")
    found_employee = None
    for employee in employee_records:
        if employee_name.lower() == employee["name"].lower():
            found_employee = employee
            break
            
    if found_employee:
        employee_records.remove(found_employee)
        print ("Removed succefully!") 
    else:
        print ("The employee was not found.") 

def display_employee (employee_records):
    employee_name = input("Enter the name of the employee to remove:")

    found_employee = None
    for employee in employee_records:
        if employee_name.lower() == employee["name"].lower():
            found_employee = employee
            break
    
    if found_employee:
        print("Name:", found_employee["name"])
        print("Age:", found_employee["age"])
        print("Department:", found_employee["department"])
        print("Salary:", found_employee["salary"])

    else:
        print ("The employee was not found.")

def display_employee_records (employee_records):
    for employee in employee_records:
        print("\nEmployee Details:")
        for key, value in employee.items():
            print(f"{key}: {value}")

def average_salary (employee_records):
    total_salary = 0
    for employee in employee_records:
        total_salary += employee["salary"]
        average_salary  = total_salary/len(employee_records) 
    print("Average Salary:", average_salary)



while True:
    print(""" 
    
    
    Please select an option:
    
    1. Add new employee details
    2. Update existing employees' details
    3. Remove an employee's details
    4. Display the details of a specific employee
    5. List all employees and their details
    6. Calculate the average salary of all employees
    7. Exit
     """
   
    )

    user_choice = input("Enter your choice (put only the number of your choice):")
    try:
        if user_choice in ["1", "2", "3", "4", "5", "6", "7"]:
            if user_choice == "1":
                add_employee(employee_records)
            elif user_choice == "2":
                update_employee(employee_records)
            elif user_choice == "3":
                remove_employee(employee_records)
            elif user_choice == "4":
                display_employee(employee_records)
            elif user_choice == "5":
                display_employee_records(employee_records)
            elif user_choice == "6":
                average_salary(employee_records)        
            else:
                print("Thank you! We'd love to see you back soon!")
                break
        else:
            raise ValueError("Put only 1 - 7. One number at a time")
            
    except ValueError as e:
        print(str(e))
        print("\n" * 3)


"""
Exercise: Managing Employee Data

Learning Objectives:

    Practice working with various data structures in Python, including lists, dictionaries, and sets.
    Gain familiarity with indexing, slicing, and manipulating data within data structures.
    Learn to use built-in methods and functions to perform operations on data structures.
    Understand the concept of immutability and mutable data structures.

Requirements: Create a program to manage employee data using different data structures.

The program should allow the user to perform the following actions:
    Add a new employee and their details (name, age, department, salary).
    Update the details of an existing employee.
    Remove an employee from the data.
    Display the details of a specific employee.
    List all employees and their details.
    Calculate the average salary of all employees.
    Use appropriate data structures to store employee data. Consider using a list of dictionaries or a dictionary of dictionaries.
    Implement error handling to handle potential exceptions, such as invalid input or non-existent employee records.
    Provide an interactive user interface to easily perform the actions mentioned above.


Hints:

    Use a list of dictionaries to store employee data, where each dictionary represents an employee's details.
    You can create a menu-driven program using loops and conditional statements to allow the user to choose different actions.
    Utilize built-in methods like append(), remove(), and update() to add, remove, and update employee records.
    To calculate the average salary, iterate over the employee data and accumulate the salaries, then divide by the total number of employees.
    Implement input validation to ensure the user enters valid data and handle any potential exceptions using try-except blocks.
    Consider defining functions for each action to make your code modular and easier to maintain.
    Test your program thoroughly with different scenarios to ensure it works as expected.
    Note: The exercise aims to provide a starting point for you to practice working with data structures. Feel free to modify or expand upon the requirements based on your understanding and learning goals.
"""


""""
Algorithm 

1.	Create an empty list to store the employee records.
2.	Define a function add_employee that takes the list of employees as a parameter:
    a.	Inside the function, create an empty dictionary to store the employee details.
    b.	Prompt the user to enter the employee's details (name, age, department, salary).
    c.	Append the employee details dictionary to the list of employees using the append() method.
    d.	Print a success message.
3.	Define a function update_employee that takes the list of employees as a parameter:
    a.	Prompt the user to enter the name of the employee to update.
    b.	Use a loop to search for the employee in the list of employees.
    c.	If the employee is found:
        i.	Prompt the user to enter the detail (name, age, department, salary) to update.
        ii.	If the detail is valid, prompt the user to enter the updated value.
        iii.	Use the update() method to update the employee's detail in the dictionary.
        iv.	Print a success message.
        v.	Exit the loop.
    d.	If the employee is not found, print a message indicating that the employee was not found.
4.	Define a function remove_employee that takes the list of employees as a parameter:
    a.	Prompt the user to enter the name of the employee to remove.
    b.	Use a loop to search for the employee in the list of employees.
    c.	If the employee is found:
        i.	Use the remove() method to remove the employee from the list.
        ii.	Print a success message.
        iii.	Exit the loop.
    d.	If the employee is not found, print a message indicating that the employee was not found.
5.	Define a function display_employee that takes the list of employees as a parameter:
    a.	Prompt the user to enter the name of the employee to search for.
    b.	Use a loop to search for the employee in the list of employees.
    c.	If the employee is found, print the employee's details (name, age, department, salary).
    d.	If the employee is not found, print a message indicating that the employee was not found.
6.	Define a function list_employees that takes the list of employees as a parameter:
    a.	Use a loop to iterate over the list of employees.
    b.	Print the details of each employee (name, age, department, salary).
7.	Calculate the average salary of all employees:
    a. Initialize a variable called total_salary to 0.
    b. Use a loop to iterate over the list of employees.
    c. For each employee, access their salary from the employee's dictionary and add it to the total_salary variable.
    d. After the loop, calculate the average salary by dividing the total_salary by the number of employees in the list.
    e. Print the average salary.
8.  Start a loop to display the menu options.
8.	Prompt the user to enter their choice.
9.	If the user chooses to add a new employee, call the add_employee function.
10.	If the user chooses to update an existing employee, call the update_employee function.
11.	If the user chooses to remove an employee, call the remove_employee function.
12.	If the user chooses to display the details of a specific employee, call the display_employee function.
13.	If the user chooses to list all employees and their details, call the list_employees function.
14.	If the user chooses to exit the program, break the loop to exit.
15.	If the user enters an invalid choice, display an error message and continue to the next iteration of the loop.

"""


            
    

              








