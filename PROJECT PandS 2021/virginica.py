# Focus on virginica species

import pandas as pd
import matplotlib.pyplot as plt
import pdb


iris_df = pd.read_csv('iris.csv')
virginica = iris_df[iris_df['species'] == 'virginica'] # Returns only the virginica species from the iris flowers data frame

# Histogram of petal length repartition for virginica flowers
virginica.petal_length.plot(kind='hist', title='Frequency of virginica petal length', xlabel='Centimetres(cm)', color='green')
plt.xlabel('Petal length (cm)')
plt.ylabel('Frequency')
plt.show()

# Histogram of petal width repartition for virginica flowers
virginica.petal_width.plot(kind='hist', title='Frequency of virginica petal width', xlabel='Centimetres(cm)', color='yellow')
plt.xlabel('Petal width (cm)')
plt.ylabel('Frequency')
plt.show()

# Histogram of sepal width repartition for virginica flowers
virginica.sepal_width.plot(kind='hist', title='Frequency of virginica sepal width', xlabel='Centimetres(cm)', color='blue')
plt.xlabel('Sepal width (cm)')
plt.ylabel('Frequency')
plt.show()

# Histogram of sepal width repartition for virginica flowers
virginica.sepal_length.plot(kind='hist', title='Frequency of virginica sepal length', color='red', label='Centimetres(cm)')
plt.xlabel('Sepal length (cm)')
plt.ylabel('Frequency')
plt.show()
