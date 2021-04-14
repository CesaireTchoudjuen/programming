import matplotlib.pyplot as plt
import numpy as np


# Linear plot
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label = "xsquared")
plt.plot(xpoints, xpoints, label = "straight", color="blue")
plt.legend()
plt.savefig('lecture1.png')

# Scattered points plot
randompoints = np.random.randint(1, 1000, 100)
plt.scatter(xpoints, randompoints, label="random")

# Histogram plots

normData = np.random.normal(size=1000)
plt.hist(normData)

plt.show()
