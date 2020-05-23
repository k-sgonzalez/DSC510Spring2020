"""
File DSC510_T303 Week 11 Programming Assignment
Name: Kim Gonzalez
Date: 23May2020
Course: DSC510_T303 Intro to Python Programming
Details:

-Your program must have a welcome message for the user.
-Your program must have one class called CashRegister.
-Your program will have an instance method called addItem which takes one parameter for price.
    The method should also keep track of the number of items in your cart.
-Your program should have two getter methods.
    getTotal – returns totalPrice
    getCount – returns the itemCount of the cart
-Your program must create an instance of the CashRegister class.
-Your program should have a loop which allows the user to continue to add items to the cart
    until they request to quit.
-Your program should print the total number of items in the cart.
-Your program should print the total $ amount of the cart.
-The output should be formatted as currency. Be sure to investigate the locale class.
    You will need to call locale.setlocale and locale.currency.
"""

import locale

print("Aloha! Welcome to the Cart Register!")

class CashRegister: #creates the CashRegister class that will call on additional needed functions
    def __init__(self):
        self.__itemCount = 0
        self.__totalPrice = 0

    def addItem(self, price: float): #addItem function adds items to the register
        self.__totalPrice += price
        self.__itemCount += 1

    def getTotal(self) -> float: #getTotal function produces the total of the items
        return self.__totalPrice

    def getCount(self) -> int: #getCount functions counts the number of items
        return self.__itemCount

def main():
    print("After entering the prices for all of the items in your cart,\nenter 'Done' for the total of your cart.\n")
    register = CashRegister() #creates instance of the CashRegister class
    locale.setlocale(locale.LC_ALL, 'en_US') #this makes sure that the output is in local currency

    while True: #loop that allows user to continue adding items until they break it
        try:
            user_input: str = input("Please enter item cost:\n")
            if user_input == "Done" or user_input == 'done': #allows calling on our sentinel value to stop the loop
                print("Please wait while we total up your costs...")
                break

            price = float(user_input)
            register.addItem(price)

        except ValueError:
            print('OOPS! Something went wrong! Make sure you entered a number for price or Done for the total!')


    total_price: float = register.getTotal()
    total_count: int = register.getCount()
    print('Total items in cart: {}'.format(total_count))
    print('Cart Total: {}'.format(locale.currency(total_price, grouping=True)))


if __name__ == '__main__': #calls on the entire program to run
    main()
