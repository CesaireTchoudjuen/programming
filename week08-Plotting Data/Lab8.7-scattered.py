# Author Cesaire Tchoudjuen
# Program that makes a list called AGES that has the same number random values as salaries (range 21 to 65)

import matplotlib.pyplot as plt
import numpy as np

ages = np.random.randint(21, 65, 10)
salaries = np.random.randint(20000,80000,10)

np.random.seed(1)
plt.scatter(ages, salaries)
plt.show()
