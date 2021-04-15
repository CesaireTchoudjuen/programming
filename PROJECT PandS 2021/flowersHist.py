import pandas as pd
import matplotlib.pyplot as plt
import pdb

iris_df = pd.read_csv('iris.csv') #No need for full path as file is in the same directory

# All specied variable are defined below
setosa = iris_df[iris_df['species'] == 'setosa']
versicolor = iris_df[iris_df['species'] == 'versicolor']
virginica = iris_df[iris_df['species'] == 'virginica']

# Histogram of petal length repartition for the complte dataset
iris_df.petal_length.plot(kind='hist', title='Petal Length', color='blue')
plt.xlabel('Measurement (cm)')
plt.ylabel('Frequency')
plt.show()

# Histogram of petal width repartition for Setosa flowers
iris_df.petal_width.plot(kind='hist', title='Petal Width', color='yellow')
plt.xlabel('Measurement (cm)')
plt.ylabel('Frequency')
plt.show()

# Histogram of sepal width repartition for Setosa flowers
iris_df.sepal_width.plot(kind='hist', title='Sepal Width', color='green')
plt.xlabel('Measurement (cm)')
plt.ylabel('Frequency')
plt.show()

# Histogram of sepal length repartition for Setosa flowers
iris_df.sepal_length.plot(kind='hist', title='Sepal Length', color='red')
plt.xlabel('Measurement (cm)')
plt.ylabel('Frequency')
plt.show()