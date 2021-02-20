# Author: Cesaire Tchoudjuen
# Program that prompts the user to guess a number and tells user if number is too high or too low

guess = int(input("Please guess the number: "))
correctguess = 30

while guess != correctguess:
    print("Wrong!")
    if guess < correctguess:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Please guess again: ")) #redefines the value of guess for the next loop

print("Well done! Yes the number was {}.".format(correctguess))