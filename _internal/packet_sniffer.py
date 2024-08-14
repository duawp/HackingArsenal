import socket
from scapy.all import *
from scapy.layers.l2 import Ether
from subprocess import call
import time
import os
import sys

    
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
interface = "eth0"
sniffer.bind((interface, 0))
running = True

def start_sniffing():
    try:
        while running:
            raw_data, addr = sniffer.recvfrom(65535)
            packet = Ether(raw_data)
            print(packet.summary())
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sniffer.close()
        print("Sniffer closed.")

def main():
    start_sniffing()

    while True:
        user_input = input("Press 'q' to exit...").strip().lower()
        if user_input == 'q':
            print("Exiting and going to main menu !")
            call(["python", "goingbackani.py"])
            time.sleep(1.5)
            start_another_program()
            sys.exit()

def start_another_program():
    os.system('hell.py')

if __name__ == "__main__":
    main()
