# Focus on setosa species

import pandas as pd
import matplotlib.pyplot as plt
#import pdb


iris_df = pd.read_csv('iris.csv')
setosa = iris_df[iris_df['species'] == 'setosa'] # Returns only the setosa species from the iris flowers data frame

# Histogram of petal length repartition for Setosa flowers
setosa.petal_length.plot(kind='hist', title='Frequency of Setosa petal length', xlabel='Centimetres(cm)', color='blue')
plt.xlabel('Petal length (cm)')
plt.ylabel('Frequency')
plt.show()
#pdb.set_trace()

# Histogram of petal width repartition for Setosa flowers
setosa.petal_width.plot(kind='hist', title='Frequency of Setosa petal width', xlabel='Centimetres(cm)', color='yellow')
plt.xlabel('Petal width (cm)')
plt.ylabel('Frequency')
plt.show()
#pdb.set_trace()

# Histogram of sepal width repartition for Setosa flowers
setosa.sepal_width.plot(kind='hist', title='Frequency of Setosa sepal width', xlabel='Centimetres(cm)', color='red')
plt.xlabel('Sepal width (cm)')
plt.ylabel('Frequency')
plt.show()
#pdb.set_trace()

# Histogram of sepal width repartition for Setosa flowers
setosa.sepal_length.plot(kind='hist', title='Frequency of Setosa sepal length', xlabel='Centimetres(cm)', color='green')
plt.xlabel('Sepal length (cm)')
plt.ylabel('Frequency')
plt.show()
#pdb.set_trace()
