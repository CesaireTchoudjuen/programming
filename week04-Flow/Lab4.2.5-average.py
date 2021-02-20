# Author: Cesaire Tchoudjuen
# Program that keeps reading numbers until the user enters a 0
# The program should then print out each of the numbers entered and the average of them

number = int(input("Enter a number (0 to quit): "))
numbers = []

while number != 0:
    numbers.append(number)
    number = int(input("Enter another number (0 to quit): "))

for val in numbers:
    print(val)

average = float(sum(numbers)) / len(numbers)
print("The average is {}.".format(average))
