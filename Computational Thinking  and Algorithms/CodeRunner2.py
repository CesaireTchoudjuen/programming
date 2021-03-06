def decrypt(plain_text, offset):
    decrypted_text = ""

    for i in plain_text:        
        numerical_value = ord(i)

        if (i.isupper()):
            adjusted = (( numerical_value - offset - 65) % 26) + 65  
            decrypted_text += chr(adjusted)  
        elif numerical_value == 32 :
            decrypted_text += i 
        else: 
            adjusted = (( numerical_value - offset - 97) % 26) + 97 
            decrypted_text += chr(adjusted)
           
    return decrypted_text

print(decrypt( "M pszi KQMX", 4))