# Author: Cesaire Tchoudjuen
# Program that prompts the user to guess a number
# The program should keep prompting the user to guess the number until the user gets the right one

guess = int(input("Please guess the number: "))
correctguess = 30

while guess != correctguess:
    print("Wrong!")
    guess = int(input("Please guess again: "))
print("Well done! Yes the number was {}.".format(correctguess))