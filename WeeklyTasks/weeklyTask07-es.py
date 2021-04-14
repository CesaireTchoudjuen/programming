# Author: Cesaire Tchoudjuen
# Program that reads in a text file and outputs the number of e's it contains


# Program asks user to enter the file name
# File should be stored in the same directory as the program itself. If not, please change directory from the console
file_name = input("Please enter the file name: ")
letter_input = input("Please enter the letter to be counted: ")
count = 0 #We initiate the letter count to 0. Later, the program will increment it as it count the target letter in the selected file


with open(file_name, 'r') as f: # Opens the designated file in the read mode
    for i in f: # The program will scan the entire file
        word = i.split() # split() method splits a string into a list of words
        for j in word: # Now the program will scan each word
            for letter in j: # In each word from the list created above, if the target letetr is found, then our count is increased by 1
                if(letter == letter_input):
                    count = count + 1

print("In your selected file, the letter you entered was counted", count, "times.")
        
