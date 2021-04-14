# Author: Cesaire Tchoudjuen
# Program that reads in a string and strips any leading or trailing spaces
# The program should also convert the string to lower case
# The program should also output the length of the input and output strings

rawstring = input("Please enter a sting: ")
normalisedstring = rawstring.strip().lower() # Returns rawstring without the spqces qt the beginning qnd end of the string +  in lower case

lenghtOfrawstring = len(rawstring)
lenghtOfnormalisedstring = len(normalisedstring)

print("That string normalised is {}".format(normalisedstring))
print("We reduced the input string from {} to {} characters".format(lenghtOfrawstring, lenghtOfnormalisedstring))

