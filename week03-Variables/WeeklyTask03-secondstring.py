# Author: Cesaire Tchoudjuen
# Program that takes asks a user to input a string and outputs every second letter in reverse order

sentence = input("Please enter a sentence:")

# The format for slice notation is [start:stop:step]
# [::2] is telling Python to step through the string by 2's (which will return every other character)
# To 'slice' the string backwards and return the string in reverse order, we use the negative value '-2' to work our way from the end of the string
a = sentence[::-2] 


print("If we return every second letter in reverse order, this sentence is: {}".format(a))
