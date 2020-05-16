"""
File DSC510_T303 Week 6 Programming Assignment
Name: Kim Gonzalez
Date: 16May2020
Course: DSC510_T303 Intro to Python Programming
Details:
    - This program will create an empty list called 'temperatures'
    -The program will then allow the user to input a series of temperatures along
    with a sentinel value which will stop the user input.
    -The program will evaluate the temperature list and will determine the largest
    and smallest temperature and print both as well as how many temperatures are in
    the list.

**Include appropriate comments throughout program
"""
#first we create an empty list called 'temperatures'

temperatures = []
def main_calculations():
    welcome = int(input("Aloha! Please provide the temperatures you would\nlike to evaluate.\n"
                    "If done entering temperatures, enter 'DONE'\nPlease enter the quantity of temperatures you want evaluated:\n"))
    total = 0
    for x in range(welcome):
        series = input("Enter temperature:\n")
        if series == 'DONE': #sentinel value
            break
        else:
            temperatures.append(series) #this appends my temp list with the user input
    print("The following temperatures were entered:\n", temperatures,"\n"
        "The Max Temperature entered was:", max(temperatures),"\n"
         "The Min Temperature entered was:", min(temperatures),"\n"
        "The total number of temperatures entered was:", len(temperatures),"\n"
        "Thank you!")


main_calculations()
