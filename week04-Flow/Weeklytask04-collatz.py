# Program that asks the user to input any positive integer and outputs the successive values of the following calculation
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one
# Program ends if the current value is one

value = int(input("Please enter a positive integer: "))

while value != 1: # Loop only runs when value is different than 1
    if value % 2 == 0: 
        value = value / 2
        print(int(value))
    else:   
        value = ( value * 3) + 1
        print(int(value))



