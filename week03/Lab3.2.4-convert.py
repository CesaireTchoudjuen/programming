# Author: Cesaire Tchoudjuen
# Program that converts a float amount of dollars, and returns that absolute mount in cent

amount = float(input("Please enter an amount: "))

amountincent = abs(int(amount * 100))

print("The amount in cent is {}".format(amountincent))