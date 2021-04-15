import pandas as pd
import matplotlib.pyplot as plt
import pdb



iris_df = pd.read_csv('iris.csv') #No need for full path as file is in the same directory

# loc function allows us to return records with the iris species we want to focus on
# a variable is created for each species 
'''
setosa = iris_df.loc[iris_df['species'] == 'setosa']
versicolor = iris_df.loc[iris_df['species'] == 'versicolor']
virginica = iris_df.loc[iris_df['species'] == 'virginica']

# count of number of unique value per species
iris_count = iris_df["species"].value_counts()
print('Please find below the count for each species and their data type:\n',iris_count)
# FOCUS ON SETOSA

min_SeSepalLenght = setosa['sepal_lenght'].min()
print(min_SeSepalLenght)
'''

#print(iris_df)

species = iris_df['species']
petal_length = iris_df['petal_length']

iris_df.plot(kind='scatter',x='species',y='petal_length',color='red')
plt.show()