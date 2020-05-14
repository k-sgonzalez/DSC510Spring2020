"""
File DSC510_T303 Week 5 Programming Assignment
Name: Kim Gonzalez
Date: 13May2020
Course: DSC510_T303 Intro to Python Programming
Details:
    - This program will perform various calculations (addition, subtraction, multiplication, division,
    and average calculation) by using a variety of loops and functions.
    - This program will add, subtract, multiply, and divide two numbers and provide the average of multiple
    numbers that will be input by the user.

    - First define a function named performCalculation which takes one parameter. The parameter will be the
    operations being performed (+,-,*,/). This function will perform the given prompt from the user for the
    two numbers then perform the expected operation depending on the parameter passed into the function. This
    function will then print the calculated value for the end user.

    -Second, define a function named calculateAverage which takes no parameters. This function will ask the user
    how many numbers they wish to input. This function will then use that number of times to run the program within
    a for loop in order to calculate the total and average. This function will then print the calculated average.

    -Lastly, this program will have a main section which contains a while loop. The while loop will be used to allow
    the user to run the program until they enter a value which ends the loop.
        **The main program should prompt the user for the operation they wish to perform.
        **The main program should evaluate the entered data using if statements.
        **The main program should call the necessary function to perform calculations.

*Include appropriate comments throughout program
"""
#first define the function performCalculation which will perform (+,-,*, or /).

def performCalculation(operation_type):
    num_1 = float(input("Please enter your first number:\n")) #this will ask user for input for first number
    num_2 = float(input("Please enter your second number:\n")) #this will ask user for input for second number
    if operation_type == '+':
        print("The sum of the two numbers entered is", num_1 + num_2)
    elif operation_type == '-':
        print("The difference of the two numbers entered is", num_1 - num_2)
    elif operation_type == '*':
        print("The product of the two numbers entered is", num_1 * num_2)
    elif operation_type == '/':
        print("The quotient of the two numbers entered is", num_1 / num_2)

#Next, we define the function calculateAverage

def calculateAverage():
    user_input = int(input("How many numbers would you like to use to calculate an average?\n")) #this asks the user how many numbers to use
    total = 0
    for x in range(user_input): #this creates the for loop
        user_avg_numbers = float(input("Please enter the numbers you would like to be averaged:")) #this asks for the numbers they would like to use
        total = total + user_avg_numbers #this adds the numbers that were input by the user
    total_avg = total/user_input #this calculates the average of the numbers
    print("The average of the numbers entered is", total_avg)

#Now we must define/create the main function of the program that will call on the performCalculation and calculateAverage functions.
#But first, in order to keep it clean and organized, we will create groups of lists that will contain the possible user inputs

math_functions = ['+', '-', '*', '/'] #this is the list of the possible math functions
avg = ['average', 'avg'] # this is the list of the possible spellings of the word "average" that could be input by user
any = ['+', '-', '*', '/','average','avg','none'] #this list will be used as a safety net for possible user input error

#now we move on to creating our main function that will call on those lists above as well as the above functions

def main(): #main function described above
    print("Welcome! What mathematical operation would you like to perform today?")

    while True: #now we begin our while loop and set our conditions for the main function
        user_function = input("Please choose from the following:(+, - , * , /, or average)\n\n If none, type 'none'.\n")
        if user_function in math_functions: #this condition says that if the user input(user_function) is in the list of math functions, see line 69
            performCalculation(user_function) #then it will call on the performCalculation function
        if user_function in avg: #but if the user_input is in the list of avg then it will call on the calculateAverage function, see line 71.
            calculateAverage()
        if user_function not in any: #if the user_input is not in the list of any, then it will prompt user to check for error, see line 73
            print("OOPS! There's an error. Please go back and check your input.")
        if user_function == 'none': #if the user inputs "none" then this will prompt the loop to end, see line 74 for break statement
            break
    print("Thanks for stopping by!")

main() #this calls for the main function and the program to begin
