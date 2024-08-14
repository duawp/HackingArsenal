import random
import string
import time  # Added time import for delay
from subprocess import call
from pynput import keyboard
import os
import sys

def display_banner():
    print(r"""______            _     _  ______                 _           _ 
 ____  _  _      ____  _     _____   ____  ____  ____  ____    _____ _____ _        ____ ___  _   _      ____  _     _____ _  __
/ ___\/ \/ \__/|/  __\/ \   /  __/  /  __\/  _ \/ ___\/ ___\  /  __//  __// \  /|  /  _ \\  \//  / \__/|/  _ \/ \   /  __// |/ /
|    \| || |\/|||  \/|| |   |  \    |  \/|| / \||    \|    \  | |  _|  \  | |\ ||  | | // \  /   | |\/||| / \|| |   |  \  |   / 
\___ || || |  |||  __/| |_/\|  /_   |  __/| |-||\___ |\___ |  | |_//|  /_ | | \||  | |_\\ / /    | |  ||| |-||| |_/\|  /_ |   \ 
\____/\_/\_/  \|\_/   \____/\____\  \_/   \_/ \|\____/\____/  \____\\____\\_/  \|  \____//_/     \_/  \|\_/ \|\____/\____\\_|\_\
                                                                                                                                """)
    print("\n****************************************************************")
    print("\n* Copyright of Malek, 2024                              *")
    print("\n* https://x.com/FrankZane95                                  *")
    print("\n* https://www.youtube.com/@duawp                          *")
    print("\n****************************************************************")

def get_pass_length():
    passlength1 = int(input("What should your min pass length be? \n"))
    passlength2 = int(input("What should your max pass length be? \n"))
    return passlength1, passlength2

def gen_pass(passlength1, passlength2, use_uppercase=True, use_digits=True, use_symbols=True):
    length = random.randint(passlength1, passlength2)
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password 


def main():
    display_banner()
    passlength1, passlength2 = get_pass_length()

    print("Your generated password is:", gen_pass(passlength1, passlength2))

    while True:
        user_input = input("press 'q' to exit").strip().lower()
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
