import hashlib
import time
from subprocess import call
import os
import sys

def display_banner():
    print(r"""______            _     _  ______                 _           _ 
$$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\         $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |
$$ |  $$ |$$ /  $$ |$$ /  \__|$$ /  \__|      $$ /  \__|$$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / 
$$$$$$$  |$$$$$$$$ |\$$$$$$\  \$$$$$$\        $$ |      $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  
$$  ____/ $$  __$$ | \____$$\  \____$$\       $$ |      $$  __$$< $$  __$$ |$$ |      $$  $$<   
$$ |      $$ |  $$ |$$\   $$ |$$\   $$ |      $$ |  $$\ $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  
$$ |      $$ |  $$ |\$$$$$$  |\$$$$$$  |      \$$$$$$  |$$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ 
\__|      \__|  \__| \______/  \______/        \______/ \__|  \__|\__|  \__| \______/ \__|  \__|
                                                                                                """)
    print("\n****************************************************************")
    print("\n* Copyright of Malek, 2024                              *")
    print("\n* https://x.com/FrankZane95                                  *")
    print("\n* https://www.youtube.com/@duawp                          *")
    print("\n****************************************************************")

def convert_text_to_sha1(text):
    digest = hashlib.sha1(text.encode()).hexdigest()
    return digest

def sha1():
    while True:
        user_sha1 = input("Enter SHA1 to crack: \n").strip().lower()
        if len(user_sha1) == 40 and all(c in '0123456789abcdef' for c in user_sha1):
            break
        else:
            print("Please enter a valid SHA1 hash (40 hexadecimal characters) to crack!")
            time.sleep(1)

    with open("./passwords.txt") as f:
        for line in f:
            password = line.strip()
            converted_sha1 = convert_text_to_sha1(password)

            if user_sha1 == converted_sha1:
                print(f"Password found: {password}")
                return

def main():
    display_banner()
    sha1()

    while True:
        user_input = input("Press 'q' to quit: ").strip().lower()
        if user_input == 'q':
            print("Exiting and starting the other program...")
            call(["python", "goingbackani.py"])
            time.sleep(1.5)
            start_another_program()
            sys.exit()
def start_another_program():
    os.system('hell.py')

if __name__ == "__main__":
    main()
