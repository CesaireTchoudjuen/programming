# IMPORT USED LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # Seaborn library is used as it makes it easier to add color to the plot. It also allows us to load built-in dataset
import numpy as np

# DEFINE DATA
iris = sns.load_dataset("iris") 

########################################
### OVERLAPPING SCATTER POINTS PLOTS ###

print(iris.describe())









'''
def display():
    irisdata = 'iris.csv'
    iris_df = pd.read_csv(irisdata, names= ['sepal_length',	'sepal_width', 'petal_length',	'petal_width'], header = 1)
    iris_df = iris_df.astype(float)
    print(iris_df.head(5))
    iris_df.plot()
    plt.show()
    return
display()

# BELOW CODE IS WORKING without the xlabel / ylabel
def display():
    irisdata = 'iris.csv'
    iris_df = pd.read_csv(irisdata)
    x = iris_df['sepal_length']
    y = iris_df['sepal_width']
    #xlabel('Sepal length')
    #ylabel('Sepal width')
    plt.scatter(x, y, c=col)
    plt.show()
display()


#BELOW CODE WORKS BUT NO COLOR DIFERENTIATION 
# Define Data
iris = sns.load_dataset("iris") # Loading built-in dataset
#print(iris.head(10))
x = iris['sepal_length']
y = iris['sepal_width']
for name, group in iris.groupby("species"):
    plt.scatter(x, y, label=name)
plt.legend()
plt.show()



# PETAL SCATTER POINTS
# Define Data
iris = sns.load_dataset("iris") 
# Plot
for n, grp in iris.groupby("species"): # Program loops over the species
    plt.scatter(grp.petal_length, grp.petal_width, label=n) # And returns the data points for petal length and width
plt.xlabel('Petal Length (cm)') # x and y axis label added for visibility 
plt.ylabel('Petal Width (cm)')
plt.legend() # Displays legend (here listing the species)
plt.show()

# SEPAL SCATTER POINTS
# Define Data
iris = sns.load_dataset("iris") 
# Plot
for n, grp in iris.groupby("species"): # Program loops over the species
    plt.scatter(grp.sepal_length, grp.sepal_width, label=n) # And returns the data points for petal length and width
plt.xlabel('Sepal Length (cm)') # x and y axis label added for visibility 
plt.ylabel('Sepal Width (cm)')
plt.legend() # Displays legend (here listing the species)
plt.show()
'''


