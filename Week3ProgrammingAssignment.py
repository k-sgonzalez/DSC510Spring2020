"""
File: DSC510_T303 Week3 Programming Assignment
Name: Kim Gonzalez
Date: 29MARCH2020
Course: DSC510-T303 Introduction to Programming
Desc: Program calculates quantity and costs of fiber optic cable needed by customer
        to include any qualifying discount, and prints receipt.
In: Company name from user, number of feet of fiber optic cable needed
Out: Receipt for user to include:
        company name
        number of feet of fiber to be installed
        calculated cost in legible format
Include appropriate comments throughout program
"""

print('Welcome to Fiber Optics Emporium!')
companyName = input("Please provide your company name.\n")
customizedGreeting = "Thank you " + companyName + "!"
fibreOpticNeeded = float(input("Please provide the quantity of ft of fiber optic cable to be installed.\n"))
print("Thank you! Please wait while we calculate costs.")
def cost(fibreOpticNeeded):
    if 100<fibreOpticNeeded<=250:
        return fibreOpticNeeded * 0.80
    elif 250<fibreOpticNeeded<=500:
        return fibreOpticNeeded * 0.70
    elif fibreOpticNeeded>500:
        return fibreOpticNeeded * 0.50
    else:
        return fibreOpticNeeded * 0.87
receipt = f"""
    Invoice #23456:
        Thank you {companyName}!
        Num. of ft of Fiber Optic Cable to be installed is {fibreOpticNeeded}.
        Total for installation is ${cost(fibreOpticNeeded)}
        Thank you for contacting Fiber Optics Emporium!
    """
print(receipt)