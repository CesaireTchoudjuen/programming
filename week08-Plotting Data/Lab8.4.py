# Program that makes a list , called salaries, that has 10 random numbers (20000 - 80000)
# Increase all salaries by 5%
# Author: Cesaire Tchoudjuen

import numpy as np

salaries = np.random.randint(20000,80000,10)
salariesIncrease = salaries * 1.05

print(salaries)
print(salariesIncrease)