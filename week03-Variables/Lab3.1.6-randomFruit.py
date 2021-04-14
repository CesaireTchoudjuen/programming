# Author: Cesaire Tchoudjuen
# Program that prints out a random fruit

import random

fruits = ["apple", "mango", "banana", "pear", "orange"]

index = random.randint(0,len(fruits)-1) # Not sure I fully understand how we convert this list of fruit into an index with a numeric value to run this program
fruit = fruits[index]
print("A Random Fruit: {}".format(fruit))