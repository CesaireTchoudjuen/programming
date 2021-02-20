# Author: Cesaire Tchoudjuen
# Program that asks the user to enter a number 
# The program wil tell the user if the number is even or odd

number = int(input("Enter a number: "))

if ((number % 2) == 0):
    print("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))
