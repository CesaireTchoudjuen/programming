# Author: Cesaire Tchoudjuen
# Program that: outputs an histogram displaying the frequency of each of the 4 measured features of Versicolor flowers

######################
## IMPORT LIBRARIES ##
import pandas as pd
import matplotlib.pyplot as plt

##################
## DEFINE DATA ###
iris_df = pd.read_csv('iris.csv')
versicolor = iris_df[iris_df['species'] == 'versicolor'] # Returns only the versicolor species from the iris flowers data frame

############
### PLOT ###

# Histogram of petal length repartition for versicolor flowers
versicolor.petal_length.plot(kind='hist', title='Frequency of versicolor petal length', xlabel='Centimetres(cm)', color='green') # Program will only return data from the petal length serie within the Versicolor species
plt.xlabel('Petal length (cm)') # x and y axis labels added for visibility
plt.ylabel('Frequency')
plt.show()
# Histogram of petal width repartition for versicolor flowers
versicolor.petal_width.plot(kind='hist', title='Frequency of versicolor petal width', xlabel='Centimetres(cm)', color='yellow') # Program will only return data from the petal width serie within the Versicolor species
plt.xlabel('Petal width (cm)') # x and y axis labels added for visibility
plt.ylabel('Frequency')
plt.show()
# Histogram of sepal width repartition for versicolor flowers
versicolor.sepal_width.plot(kind='hist', title='Frequency of versicolor sepal width', xlabel='Centimetres(cm)', color='blue') # Program will only return data from the sepal width serie within the Versicolor species
plt.xlabel('Sepal width (cm)') # x and y axis labels added for visibility
plt.ylabel('Frequency')
plt.show()
# Histogram of sepal width repartition for versicolor flowers
versicolor.sepal_length.plot(kind='hist', title='Frequency of versicolor sepal length', color='red', label='Centimetres(cm)') # Program will only return data from the sepal length serie within the Versicolor species
plt.xlabel('Sepal length (cm)') # x and y axis labels added for visibility
plt.ylabel('Frequency')
plt.show()
