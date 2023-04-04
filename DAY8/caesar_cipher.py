import art
print(art.logo)
def encrypt(text, shift):
    encode_string = ""
           
    for i in text:
        x = alphabet.index(i)
        new_shift = x + shift
        new_letter = alphabet[new_shift]
        encode_string += new_letter        
  
    print(f"Here's the encoded result :{encode_string}")
  

def decrypt(text, shift):
    decode_string = ""
    for i in text:
        x = decode_alphabet.index(i)
        new_shift = x + shift
        new_letter = decode_alphabet[new_shift]
        decode_string += new_letter        
  
    print(f"Here's the decoded result :{decode_string}")

decode_alphabet = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a' , 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
def run():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))      
           
    if direction == 'encode':
        encrypt(text,shift)
    elif direction == 'decode':
        decrypt(text, shift)
    else:
        print("Please type correctly !!!")
        
    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if choice == "yes":
        run()
    else:
        print("Goodbye")
    
run()    

    
