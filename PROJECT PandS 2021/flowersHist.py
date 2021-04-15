import pandas as pd
import matplotlib.pyplot as plt
import pdb

iris_df = pd.read_csv('iris.csv') #No need for full path as file is in the same directory

# All specied variable are defined below
setosa = iris_df[iris_df['species'] == 'setosa']
versicolor = iris_df[iris_df['species'] == 'versicolor']
virginica = iris_df[iris_df['species'] == 'virginica']

# Histogram of petal length repartition for the complte dataset
iris_df.petal_length.plot(kind='hist', title='Frequency of petal length', xlabel='Centimetres(cm)', color='blue')
plt.xlabel('Petal length (cm)')
plt.ylabel('Frequency')
plt.show()

# Histogram of petal width repartition for Setosa flowers
iris_df.petal_width.plot(kind='hist', title='Frequency of petal width', xlabel='Centimetres(cm)', color='yellow')
plt.xlabel('Petal width (cm)')
plt.ylabel('Frequency')
plt.show()

# Histogram of sepal width repartition for Setosa flowers
iris_df.sepal_width.plot(kind='hist', title='Frequency of sepal width', xlabel='Centimetres(cm)', color='blue')
plt.xlabel('Sepal width (cm)')
plt.ylabel('Frequency')
plt.show()

# Histogram of sepal width repartition for Setosa flowers
iris_df.sepal_length.plot(kind='hist', title='Frequency of sepal length', color='red', label='Centimetres(cm)')
plt.xlabel('Sepal length (cm)')
plt.ylabel('Frequency')
plt.show()