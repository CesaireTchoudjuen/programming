# Program that makes a list , called salaries, that has 10 random numbers (20000 - 80000)
# Add 5000 to each salary
# Author: Cesaire Tchoudjuen

import numpy as np

salaries = np.random.randint(20000,80000,10)

salariesPlus = salaries + 5000

print(salaries)
print(salariesPlus)