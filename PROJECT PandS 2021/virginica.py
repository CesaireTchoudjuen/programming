# Author: Cesaire Tchoudjuen
# Program that: outputs an histogram displaying the frequency of each of the 4 measured features of Virginica flowers

######################
## IMPORT LIBRARIES ##
import pandas as pd
import matplotlib.pyplot as plt

##################
## DEFINE DATA ###
iris_df = pd.read_csv('iris.csv')
virginica = iris_df[iris_df['species'] == 'virginica'] # Returns only the virginica species from the iris flowers data frame

############
### PLOT ###

# Histogram of petal length repartition for virginica flowers
virginica.petal_length.plot(kind='hist', title='Frequency of virginica petal length', xlabel='Centimetres(cm)', color='green') # Program will only return data from the petal length serie within the Virginica species
plt.xlabel('Petal length (cm)') # x and y axis labels added for visibility
plt.ylabel('Frequency')
plt.show()
# Histogram of petal width repartition for virginica flowers
virginica.petal_width.plot(kind='hist', title='Frequency of virginica petal width', xlabel='Centimetres(cm)', color='yellow') # Program will only return data from the petal width serie within the Virginica species
plt.xlabel('Petal width (cm)') # x and y axis labels added for visibility
plt.ylabel('Frequency')
plt.show()
# Histogram of sepal width repartition for virginica flowers
virginica.sepal_width.plot(kind='hist', title='Frequency of virginica sepal width', xlabel='Centimetres(cm)', color='blue') # Program will only return data from the sepal width serie within the Virginica species
plt.xlabel('Sepal width (cm)') # x and y axis labels added for visibility
plt.ylabel('Frequency')
plt.show()
# Histogram of sepal width repartition for virginica flowers
virginica.sepal_length.plot(kind='hist', title='Frequency of virginica sepal length', color='red', label='Centimetres(cm)') # Program will only return data from the sepal length serie within the Virginica species
plt.xlabel('Sepal length (cm)') # x and y axis labels added for visibility
plt.ylabel('Frequency')
plt.show()
