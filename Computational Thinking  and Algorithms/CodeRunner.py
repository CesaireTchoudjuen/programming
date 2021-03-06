# Write a method which encrypts a string using the Caesar Cipher Algorithm, the algorithm should not change space characters.

def encrypt(plain_text, offset):
    cipher_text = ""

    for i in plain_text:        
        numerical_value = ord(i)

        if (i.isupper()):
            adjusted = (( numerical_value + offset - 65) % 26) + 65  
            cipher_text += chr(adjusted)  
        elif numerical_value == 32 :
            cipher_text += i 
        else: 
            adjusted = (( numerical_value + offset - 97) % 26) + 97 
            cipher_text += chr(adjusted)
           
    return cipher_text

print(encrypt( "This course is great" , 4 ))