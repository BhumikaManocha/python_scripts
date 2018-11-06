#encryption of text
import string

def encrypt(text,shift):
    encrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    
    shifted_alphabet = second_half + first_half
    
    for i,letter in enumerate(text.lower()):
       
        if letter in alphabet:
        
            original_index = alphabet.index(letter)
            new_letter = shifted_alphabet[original_index]
            encrypted_text[i] = new_letter
        
        else:
            encrypted_text[i]=letter
            
    return ''.join(encrypted_text)
    

encrypt('i cant be encrypted',3)    

#decryption
import string

def decrypt(text,shift):
    decrypted_text = list(range(len(text)))
    alphabet = string.ascii_lowercase
    first_half = alphabet[:shift]
    second_half = alphabet[shift:]
    
    shifted_alphabet = second_half + first_half
    
    for i,letter in enumerate(text.lower()):
       
        if letter in alphabet:
            original_index = shifted_alphabet.index(letter)
            original_letter = alphabet[original_index]    
            decrypted_text[i] = original_letter
      
        else:
            decrypted_text[i]=letter
            
    return ''.join(decrypted_text)
 
 #all possible combinations
 def all_combinations(message):
    for n in range(26):
       # print("using shift {}".format(n))
        print(decrypt(message,n))
        print("\n")