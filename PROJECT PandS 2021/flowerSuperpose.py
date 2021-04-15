import pandas as pd
import matplotlib.pyplot as plt
import pdb

iris_df = pd.read_csv('iris.csv') #No need for full path as file is in the same directory

# All specied variable are defined below
setosa = iris_df[iris_df['species'] == 'setosa']
versicolor = iris_df[iris_df['species'] == 'versicolor']
virginica = iris_df[iris_df['species'] == 'virginica']

# Superposition of petal length of all 3 species
virginica.petal_length.plot(kind='hist', title='Frequency of virginica petal length', xlabel='Centimetres(cm)', color='green')
versicolor.petal_length.plot(kind='hist', title='Frequency of versicolor petal length', xlabel='Centimetres(cm)', color='red')
setosa.petal_length.plot(kind='hist', title='Frequency of Setosa petal length', xlabel='Centimetres(cm)', color='blue')
plt.xlabel('Petal length (cm)')
plt.ylabel('Frequency')
plt.legend() # Adds a legend to the histogram
plt.show()

# I need to write code for remain 3 attributes + find out how I can amend the legend on the graph itself to show the name of each species
