# Author: Cesaire Tchoudjuen
# Program that reads in two numbers and divides the first one by the second and give the integer result and the remainder

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
answer = a // b
remainder = a%b # % will retun the remainder

print("{} divided by {} is {} with remainder {}".format(a, b, answer, remainder))