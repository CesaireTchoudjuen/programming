# Author: Cesaire Tchoudjuen
# Calculates BMI

weight = input("Enter weight:")
height = input("Enter height:")

bmi = int(weight) / int(height ** 2)

print("Your BMI is " + str(bmi))