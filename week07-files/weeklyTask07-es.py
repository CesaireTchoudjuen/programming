# Author: Cesaire Tchoudjuen
# Program that reads in a text file and outputs the number of e's it contains


# Program asks user to enter the file name
# File should be stored in the same directory as the program itsel
file_name = input("Please enter the file name: ")
letter_input = input("Please enter the letter to be counted: ")
count = 0


with open(file_name, 'r') as f: # Opens the designated file in the read mode
    for i in f:
        word = i.split() # split() method splits a string into a list
        for j in word:
            for letter in j:
                if(letter == letter_input):
                    count = count + 1

print("In your selected file, the letter you entered was counted", count, "times.")
        
