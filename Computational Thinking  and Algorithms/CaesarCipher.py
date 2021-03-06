# input: plaintext, offset
# process: apply offset to every character
# output: the ciphertext

def encrypt( plain_text , offset ):
    cipher_text = ""           # defines cypher_text as a string

    for i in plain_text:        # FOR LOOP: for every character in the plain_text 
        numerical_value = ord(i) # ord() function returns the integer that represents the input value >> chr(numerical_value) will revert the numerical value to a string 
        # print( numerical_value ) 
        if (i.isupper()):
            adjusted = (( numerical_value + offset - 65) % 26) + 65   # on soustrait 65 (lettre 'a' majuscule), on prend le remainder de la division par les 26 lettres de l alphabet
            cipher_text += chr(adjusted)  # une fois le changement de numerical value de la ligne above effectue; return the string value for encoded text
        elif numerical_value == 32: # 32 is the numerical value of space character
            cipher_text += i # this means if when encoding the program finds a space, it will return the space without encoding it
        else: 
            adjusted = (( numerical_value + offset - 97) % 26) + 97 # 97 is for 'a' lowercase
            cipher_text += chr(adjusted)
           #  print("is lower")



    return cipher_text

print(encrypt( "My name is Cesaire" , 2 ))