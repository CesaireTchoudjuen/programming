# Author: Cesaire Tchoudjuen   
# Program that displays a plot of the function f(x)=x, g(x)=x² and h(x)=x³ in the range [0,4] on one set of axes

import matplotlib.pyplot as plt
import numpy as np

x = np.array(range(1,5))
# We define below our 3 functions f(x)=x, g(x)=x² and h(x)=x³
fFunction = x
gFunction = x * x
hFunction = x * x * x


# For each function, we generate a graph to visualize it with x = [0,4]

plt.plot(x, fFunction, label = "f(x) = x")
plt.plot(x, gFunction, label = "g(x) = x²")
plt.plot(x, hFunction, label = "h(x) = x³")
# We add a title to our graph as well as a legend
plt.title("Plot Task: Plot of functions f(x)=x, g(x)=x² and h(x)=x³")
plt.legend()

plt.show()