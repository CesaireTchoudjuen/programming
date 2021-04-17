import pandas as pd
import matplotlib.pyplot as plt
import pdb

iris_df = pd.read_csv('iris.csv') #No need for full path as file is in the same directory
setosa = iris_df[iris_df['species'] == 'setosa']
fig, ax = plt.subplots(figsize=(10, 6))


#x = setosa.petal_length.plot(kind='hist', title='Frequency of Setosa petal length', xlabel='Centimetres(cm)', color='blue')
#y = setosa.petal_width.plot(kind='hist', title='Frequency of Setosa petal width', xlabel='Centimetres(cm)', color='yellow')

ax.scatter(x = iris_df['petal_length'],y=iris_df['petal_width'])
plt.xlabel("petal_length")
plt.ylabel("petal_width")

plt.show()



'''
## Overlapping the repartition of the 3 iris species data in a scatter plot

a = virginica.petal_length.plot(kind='hist', title='Histogram of Petal Length', label='Virginica', color='green')
b = versicolor.petal_length.plot(kind='hist', title='Histogram of Petal Length', label='Versicolor', color='red')
c = setosa.petal_length.plot(kind='hist', title='Histogram of Petal Length', label= 'Setosa', color='blue') # It seems like the histogram title is the title of the last plot added

data = (a, b, c)
colors = ("red", "green", "blue")
groups = (virginica, versicolor, setosa)

for data, color, group in zip(data, colors, groups):
    x, y = data
ax.scatter(x, y,)


plt.legend() # Adds a legend to the histogram
plt.scatter(a, b, c)
plt.show()
'''