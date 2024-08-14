import time
import sys
from subprocess import call
import re

def display_intro():
    print(r"""______            _     _  ______                 _           _ 
░·▄▄▄▄  ▄• ▄▌ ▄▄▄· ▄▄▌ ▐ ▄▌ ▄▄▄·    • ▌ ▄ ·. ▄▄▄ . ▐ ▄ ▄• ▄▌
██▪ ██ █▪██▌▐█ ▀█ ██· █▌▐█▐█ ▄█    ·██ ▐███▪▀▄.▀·•█▌▐██▪██▌
▐█· ▐█▌█▌▐█▌▄█▀▀█ ██▪▐█▐▐▌ ██▀·    ▐█ ▌▐▌▐█·▐▀▀▪▄▐█▐▐▌█▌▐█▌
██. ██ ▐█▄█▌▐█ ▪▐▌▐█▌██▐█▌▐█▪·•    ██ ██▌▐█▌▐█▄▄▌██▐█▌▐█▄█▌
▀▀▀▀▀•  ▀▀▀  ▀  ▀  ▀▀▀▀ ▀▪.▀       ▀▀  █▪▀▀▀ ▀▀▀ ▀▀ █▪ ▀▀▀                                                                                                                                        """)
    print("\n****************************************************************")
    print("\n* Copyright of Malek, 2024                              *")
    print("\n* https://x.com/FrankZane95                                  *")
    print("\n* https://www.youtube.com/@duawp                          *")
    print("\n PS. A better Menu will be coming soon. Includes additional keylogger and many more hacking tools ;) ")
    print("\n****************************************************************")

def display_help():
    
    print("\n**HELP**")
    print(r"""______            _     _  ______                 _           _ 
 ___  ___  _______   ___       ________        _____ ______   _______   ________   ___  ___     
|\  \|\  \|\  ___ \ |\  \     |\   __  \      |\   _ \  _   \|\  ___ \ |\   ___  \|\  \|\  \    
\ \  \\\  \ \   __/|\ \  \    \ \  \|\  \     \ \  \\\__\ \  \ \   __/|\ \  \\ \  \ \  \\\  \   
 \ \   __  \ \  \_|/_\ \  \    \ \   ____\     \ \  \\|__| \  \ \  \_|/_\ \  \\ \  \ \  \\\  \  
  \ \  \ \  \ \  \_|\ \ \  \____\ \  \___|      \ \  \    \ \  \ \  \_|\ \ \  \\ \  \ \  \\\  \ 
   \ \__\ \__\ \_______\ \_______\ \__\          \ \__\    \ \__\ \_______\ \__\\ \__\ \_______\
    \|__|\|__|\|_______|\|_______|\|__|           \|__|     \|__|\|_______|\|__| \|__|\|_______|
                                                                                                
                                                                                                
                                                                                                   """)
    print("\n****************************************************************")
    print("\n* Copyright of Malek, 2024                              *")
    print("\n* https://x.com/FrankZane95                                  *")
    print("\n* https://www.youtube.com/@duawp                          *")
    print("\n****************************************************************")
    
    file = open('help.txt', 'r')
    f = file.readlines()
    newlist = []

    for line in f:
        if line.endswith('\n'):
            newlist.append(line[:-1])
        else:
            newlist.append(line)

    file.close()

    for line in newlist:
        print(line)

def display_main_menu():
    print()
    print("**MAIN MENU**")
    print("h = Help")
    print("x = Exit")
    print("s = Start")
    print("b = Back")

def display_sub_menu():
    print()
    print("\n**SUB MENU**")
    print("1 - Port Scanner")
    print("2 - Packet Sniffer")
    print("3 - SHA1 Password Cracker")
    print("4 - Password Generator")
    print("5 - Encrypt/decrypt ")
    print("x - Go back to main menu")

def start_tool():
    call(["python", "processinganimation.py"])
    time.sleep(2)
    while True:
        display_sub_menu()
        user_input2 = input("Enter an Option:  \n")
        if user_input2 == "1":
            call(["python", "processinganimation.py"])
            time.sleep(1)
            call(["python", "port_scanner.py"])
        elif user_input2 == "2":
            call(["python", "processinganimation.py"])
            time.sleep(1)
            call(["python", "packet_sniffer.py"])
        elif user_input2 == "3":
            call(["python", "processinganimation.py"])
            time.sleep(1)
            call(["python", "SHA!.py"])
        elif user_input2 == "4":
            call(["python", "processinganimation.py"])
            time.sleep(1)
            call(["python", "passgen.py"])
        elif user_input2 == "5":
            call(["python", "encryption.py"])
        elif user_input2 == "x":
            return
        else:
            time.sleep(1)
            print("**Option not available**")

def main():
    display_intro()
    menu_options = ("h", "x", "s", "b")

    while True:
        display_main_menu()
        user_input = input("Enter an Option:  \n").lower()
        if user_input in menu_options:
            if user_input == "h":
                call(["python", "processinganimation.py"])
                display_help()
            elif user_input == "x":
                print("Exiting...")
                sys.exit()
            elif user_input == "s":
                start_tool()
            elif user_input == "b":
                print("No previous menu to go back to.")
            else:
                print("**Option not available**")
        else:
            time.sleep(1)
            print("**Option not available**")

if __name__ == "__main__":
    main()




     

