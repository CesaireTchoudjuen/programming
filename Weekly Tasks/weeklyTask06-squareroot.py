# Author: Cesaire Tchoudjuen
# Program that takes a positive floating-point number as input and outputs an approximation of its square root

userInput = float(input('Please enter a positive number: ')) # Program asks user to input a floating point number

def sqrt():
# Prompt user to enter a number until a positive floating point number is entered
    while userInput < 0:
        print('This number was negative. ')
        userInput = float(input('Please enter a positive number: '))
    else:
        print('thx')
