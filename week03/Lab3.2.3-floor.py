# Author: Cesaire Tchoudjuen
# Program  that takes in a float and outputs an int rounded down

import math
numberTofloor = float(input("Enter a float number:"))
flooredNumber = math.floor(numberTofloor) # The math.floor() method rounds a number DOWN to the nearest integer, if necessary, and returns the result.
print('{} floored is {}'.format(numberTofloor, flooredNumber))