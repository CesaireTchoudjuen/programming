# Author: Cesaire Tchoudjuen
# Program that outputs a summary of each variable to a single text file

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # Seaborn library is used as it makes it easier to add color to the plot. It also allows us to load built-in dataset
import numpy as np
import pdb
iris = sns.load_dataset("iris") 

describe = iris.describe() # Describe() computes a summary of statistical data pertaining to the analysed dataframe
 
describe.to_csv('variables.txt', sep=' ') # Apends the describe table to the text file

with open('variables.txt', 'a') as file: # Introduces the describe() table above
    file.write('\nOn the abovetable, extract from the describe() method, a summary of statistics pertaining to the dataframe Fisher Iris Flowers are displayed\n\n\n')

with open('variables.txt', 'a') as file: # Creates the file variables.txt and appends the below string
    file.write('Below is summary of each variable used in the analysis by analysis.py as well as some initial statistical data pertaining to the Fisher Iris Flowers dataframe. \n\nVariable used for the analysis of the Fisher I''ris flowers dataframe:\n -Petal Length \n -Petal Width \n -Sepal Length \n -Sepal Width \n- Species (Virginica, Setosa, Versicolor)\n\n\n')
