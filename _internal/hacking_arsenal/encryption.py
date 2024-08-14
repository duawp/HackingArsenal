import random
import string
from subprocess import call
import time
import os 
import sys

def print_banner():
    print(r"""______            _     _  ______                 _           _ 
 _______   __    __   ______   __       __  _______  
|       \ |  \  |  \ /      \ |  \  _  |  \|       \ 
| $$$$$$$\| $$  | $$|  $$$$$$\| $$ / \ | $$| $$$$$$$\
| $$  | $$| $$  | $$| $$__| $$| $$/  $\| $$| $$__/ $$
| $$  | $$| $$  | $$| $$    $$| $$  $$$\ $$| $$    $$
| $$  | $$| $$  | $$| $$$$$$$$| $$ $$\$$\$$| $$$$$$$ 
| $$__/ $$| $$__/ $$| $$  | $$| $$$$  \$$$$| $$      
| $$    $$ \$$    $$| $$  | $$| $$$    \$$$| $$      
 \$$$$$$$   \$$$$$$  \$$   \$$ \$$      \$$ \$$      
                                                   """)
    print("\n****************************************************************")
    print("\n* Copyright of Malek, 2024                              *")
    print("\n* https://x.com/FrankZane95                                  *")
    print("\n* https://www.youtube.com/@duawp                          *")
    print("\n****************************************************************")

def encrypt():
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    
    plain_text = input("Enter a message to encrypt: ")
    cipher_text = ""
    
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print(f"Original message : {plain_text}")
    print(f"Encrypted message: {cipher_text}")
    
    cipher_text = input("Enter a message to decrypt: ")
    plain_text = ""
    
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Encrypted message: {cipher_text}")
    print(f"Original message : {plain_text}") 

def main():
    print_banner()
    while True:
        encrypt()
        user_input = input("Press 'q' to exit...").lower()
        if user_input == 'q':
            print("Exiting program...")
            call(["python", "hell.py"]) 
            sys.exit()

def start_another_program():
    os.system('python hell.py')

if __name__ == "__main__":
    main()
