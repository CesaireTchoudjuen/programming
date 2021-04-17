# Author: Cesaire Tchoudjuen
# Program that outputs a summary of each variable to a single text file

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # Seaborn library is used as it makes it easier to add color to the plot. It also allows us to load built-in dataset
import numpy as np
import pdb
iris = sns.load_dataset("iris") 

describe = iris.describe() # Describe() computes a summary of statistical data pertaining to the analysed dataframe
# Convert the describe table into an array
# pd.DataFrame.to_numpy() 
pd.DataFrame.to_numpy() 
describe.to_csv('variables.txt', sep=' ')
'''
with open('variables.txt', 'a') as file:
    file.write('This file provides a summary of each variable used in the analysis by analysis.py as well as some initial statistical data pertaining to the Fisher Iris Flowers dataframe. \n\nVariable used for the analysis of the Fisher I''ris flowers dataframe:\n -Petal Length \n -Petal Width \n -Sepal Length \n -Sepal Width \n- Species (Virginica, Setosa, Versicolor)\n\n\n')

'''