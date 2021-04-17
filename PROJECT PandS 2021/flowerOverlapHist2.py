# Program that overlaps the scatter point plots of the 3 species and then outputs an histogram for the repartition of each measured feature:
# i.e. Sepal Length and Width as well as Petal Length and Width
# The plot should provide with insight regarding the repartition of the flowers features according to their species
# Program will compare the petal length vs width before comparing sepal length vs width

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # Seaborn library is used as it makes it easier to add color to the plot. It also allows us to load built-in dataset
import numpy as np

# DEFINE DATA
iris = sns.load_dataset("iris") 

### SCATTER POINTS PLOTS ###

# PETAL SCATTER POINTS PLOT
for n, grp in iris.groupby("species"): # Program loops over the species
    plt.scatter(grp.petal_length, grp.petal_width, label=n) # And returns the data points for petal length and width
plt.xlabel('Petal Length (cm)') # x and y axis label added for visibility 
plt.ylabel('Petal Width (cm)')
plt.legend() # Displays legend (here listing the species)
plt.show()
# SEPAL SCATTER POINTS PLOT
for n, grp in iris.groupby("species"): # Program loops over the species
    plt.scatter(grp.sepal_length, grp.sepal_width, label=n) # And returns the data points for sepal length and width
plt.xlabel('Sepal Length (cm)') # x and y axis label added for visibility 
plt.ylabel('Sepal Width (cm)')
plt.legend() # Displays legend (here listing the species)
plt.show()

### HISTOGRAM PLOTS ###
# HISTOGRAM OF PETAL LENGTH REPARTITION 
iris.petal_length.plot(kind='hist', title='Petal Length', color='blue') #
plt.xlabel('Length (cm)') # x and y axis label added for visibility 
plt.ylabel('Frequency')
plt.show()
# HISTOGRAM OF PETAL WIDTH REPARTITION 
iris.petal_width.plot(kind='hist', title='Petal Width', color='yellow')
plt.xlabel('Width (cm)') # x and y axis label added for visibility 
plt.ylabel('Frequency')
plt.show()
# HISTOGRAM OF SEPAL LENGTH REPARTITION 
iris.sepal_length.plot(kind='hist', title='Sepal Length', color='red')
plt.xlabel('Length (cm)') # x and y axis label added for visibility 
plt.ylabel('Frequency')
plt.show()
# HISTOGRAM OF SEPAL WIDTH REPARTITION 
iris.sepal_width.plot(kind='hist', title='Sepal Width', color='green')
plt.xlabel('Width (cm)') # x and y axis label added for visibility 
plt.ylabel('Frequency')
plt.show()

