# Author: Cesaire Tchoudjuen
# Program that reads in a students percentage mark and prints out corresponding the grade

percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    print("Please enter a valid percentage value between 0 and 100")
elif percentage < 40:
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit 2")
elif percentage < 70:
    print("Merit 1")
else: print ("Distinction")