# Program that makes a list , called salaries, that has 10 random numbers (20000 - 80000)
# Each time the program is called the same random number should be pulled by the program
# Author: Cesaire Tchoudjuen

import numpy as np
import random

np.random.seed(88) # Random.seed to have the same value pulled everytime the function is called
# seed() needs to be called before the below random numbers are generated
salaries = np.random.randint(20000,80000,10)
print(salaries)