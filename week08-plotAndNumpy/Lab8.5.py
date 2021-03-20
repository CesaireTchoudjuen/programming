# Author: Cesaire Tchoudjuen
# Program that plots the function y = x²

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label = "xsquared")
plt.legend()

plt.show()