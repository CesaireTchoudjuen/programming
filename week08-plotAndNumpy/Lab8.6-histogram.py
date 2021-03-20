# Author: Cesaire Tchoudjuen
# Program that plots the function y = x²

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
salaries = np.random.randint(20000,80000,10)

plt.hist(salaries)
plt.show()