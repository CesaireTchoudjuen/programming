import pandas as pd
import matplotlib.pyplot as plt


def display():
    irisdata = 'iris.csv'
    iris_df = pd.read_csv(irisdata, names= ['sepal_length',	'sepal_width', 'petal_length',	'petal_width'], header = 1)
    iris_df = iris_df.astype(float)
    print(iris_df.head(5))
    iris_df.plot()
    plt.show()
    return
display()
