# Author: Cesaire Tchoudjuen
# Calculates BMI

# Define weight in kg and height in cm
x = int(input("Enter weight:"))
y = int(input("Enter height:"))

# Calculate BMI
bmi = x / (y * y) * 10000

# Return the BMI with 2 decimals
print("Your BMI is {0:.2f}".format(bmi))