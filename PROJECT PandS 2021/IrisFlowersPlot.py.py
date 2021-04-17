# Author: Cesaire Tchoudjuen
# Program that:
# (1) Outputs scatter points plots comparing petal (length/width) and sepal (length/width)
# (2) Outputs individual histograms for the frequency of repartition of petal length, petal width, sepal length and sepal width
# (3) Outputs similar histograms as (2) but differentiating each species 
# The plots should provide with insight regarding the repartition of the flowers features according to their species

# IMPORT USED LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # Seaborn library is used as it makes it easier to add color to the plot. It also allows us to load built-in dataset
import numpy as np

# DEFINE DATA
iris = sns.load_dataset("iris") 

########################################
### OVERLAPPING SCATTER POINTS PLOTS ###

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

##################################
### INDIVIDUAL HISTOGRAM PLOTS ###

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

###################################
### OVERLAPPING HISTOGRAM PLOTS ###

# For this part, I found it easier to read a csv file from local directory in order to define series equal to each species
## Define the data
iris_df = pd.read_csv('iris.csv') #No need for full path as file is in the same directory
# All specied variable are defined below
setosa = iris_df[iris_df['species'] == 'setosa']
versicolor = iris_df[iris_df['species'] == 'versicolor']
virginica = iris_df[iris_df['species'] == 'virginica']
# PETAL LENGTH
virginica.petal_length.plot(kind='hist', title='Histogram of Petal Length', label='Virginica', color='green')
versicolor.petal_length.plot(kind='hist', title='Histogram of Petal Length', label='Versicolor', color='red')
setosa.petal_length.plot(kind='hist', title='Histogram of Petal Length', label= 'Setosa', color='blue') # It seems like the histogram title is the title of the last plot added
plt.xlabel('Petal length (cm)') # Adds legends on the x and y axis
plt.ylabel('Frequency')
plt.legend() # Adds a legend to the histogram
plt.show()
# PETAL WIDTH
virginica.petal_width.plot(kind='hist', title='Histogram of Petal Width',label='Virginica', color='green')
versicolor.petal_width.plot(kind='hist', title='Histogram of Petal Width', label='Versicolor', color='red')
setosa.petal_width.plot(kind='hist', title='Histogram of Petal Width', label= 'Setosa', color='blue') 
plt.xlabel('Petal width (cm)')
plt.ylabel('Frequency')
plt.legend() 
plt.show()
# SEPAL LENGTH
virginica.sepal_length.plot(kind='hist', title='Histogram of Sepal Length',label='Virginica', color='green')
versicolor.sepal_length.plot(kind='hist', title='Histogram of Sepal Length', label='Versicolor', color='red')
setosa.sepal_length.plot(kind='hist', title='Histogram of Sepal Length', label= 'Setosa', color='blue') 
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.legend() 
plt.show()
# SEPAL WIDTH
virginica.sepal_width.plot(kind='hist', title='Histogram of Sepal Width',label='Virginica', color='green')
versicolor.sepal_width.plot(kind='hist', title='Histogram of Sepal Width', label='Versicolor', color='red')
setosa.sepal_width.plot(kind='hist', title='Histogram of Sepal Width', label= 'Setosa', color='blue') 
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.legend() 
plt.show()