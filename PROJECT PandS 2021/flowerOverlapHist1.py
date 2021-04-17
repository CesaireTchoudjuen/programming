import pandas as pd
import matplotlib.pyplot as plt
import pdb

iris_df = pd.read_csv('iris.csv') #No need for full path as file is in the same directory

# All specied variable are defined below
setosa = iris_df[iris_df['species'] == 'setosa']
versicolor = iris_df[iris_df['species'] == 'versicolor']
virginica = iris_df[iris_df['species'] == 'virginica']

## Overlapping the repartition of the 3 iris species data

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