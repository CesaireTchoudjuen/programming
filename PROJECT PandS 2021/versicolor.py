# Focus on versicolor species

import pandas as pd
import matplotlib.pyplot as plt
import pdb


iris_df = pd.read_csv('iris.csv')
versicolor = iris_df[iris_df['species'] == 'versicolor'] # Returns only the versicolor species from the iris flowers data frame

# Histogram of petal length repartition for versicolor flowers
versicolor.petal_length.plot(kind='hist', title='Frequency of versicolor petal length', xlabel='Centimetres(cm)', color='green')
plt.xlabel('Petal length (cm)')
plt.ylabel('Frequency')
plt.show()

# Histogram of petal width repartition for versicolor flowers
versicolor.petal_width.plot(kind='hist', title='Frequency of versicolor petal width', xlabel='Centimetres(cm)', color='yellow')
plt.xlabel('Petal width (cm)')
plt.ylabel('Frequency')
plt.show()

# Histogram of sepal width repartition for versicolor flowers
versicolor.sepal_width.plot(kind='hist', title='Frequency of versicolor sepal width', xlabel='Centimetres(cm)', color='blue')
plt.xlabel('Sepal width (cm)')
plt.ylabel('Frequency')
plt.show()

# Histogram of sepal width repartition for versicolor flowers
versicolor.sepal_length.plot(kind='hist', title='Frequency of versicolor sepal length', color='red', label='Centimetres(cm)')
plt.xlabel('Sepal length (cm)')
plt.ylabel('Frequency')
plt.show()
