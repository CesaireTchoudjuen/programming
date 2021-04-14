# Author: Cesaire Tchoudjuen
# Function that reads in a number from count.txt

fileName = 'count.txt'

def readNumber():
    with open(fileName) as f:
        number = int(f.read())
    return number
    
num = readNumber()
print(num)