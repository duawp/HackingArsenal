import asyncio
from subprocess import call
import time
import socket
import sys
import os

print(r"""______            _     _  ______                 _           _ 
 ____  ____  ____  _____    ____  ____  ____  _      _      _____ ____    ____ ___  _   _      ____  _     _____ _  __
/  __\/  _ \/  __\/__ __\  / ___\/   _\/  _ \/ \  /|/ \  /|/  __//  __\  /  _ \\  \//  / \__/|/  _ \/ \   /  __// |/ /
|  \/|| / \||  \/|  / \    |    \|  /  | / \|| |\ ||| |\ |||  \  |  \/|  | | // \  /   | |\/||| / \|| |   |  \  |   / 
|  __/| \_/||    /  | |    \___ ||  \_ | |-||| | \||| | \|||  /_ |    /  | |_\\ / /    | |  ||| |-||| |_/\|  /_ |   \ 
\_/   \____/\_/\_\  \_/    \____/\____/\_/ \|\_/  \|\_/  \|\____\\_/\_\  \____//_/     \_/  \|\_/ \|\____/\____\\_|\_\
                                                                                                                    
                                                                                                                     """)
print("\n****************************************************************")
print("\n* Copyright of Malek, 2024                              *")
print("\n* https://x.com/FrankZane95                                  *")
print("\n* https://www.youtube.com/@duawp                          *")
print("\n****************************************************************")

async def scan_port(ip, port):
    try:
        reader, writer = await asyncio.open_connection(ip, port)
        writer.close()
        await writer.wait_closed()
        return port
    except:
        return None

async def scan_ports(ip, start_port, end_port):
    open_ports = []
    tasks = [scan_port(ip, port) for port in range(start_port, end_port + 1)]
    for result in await asyncio.gather(*tasks):
        if result is not None:
            open_ports.append(result)
    return open_ports

async def main_task():
    target_ip = input("What is your target IP? : ")
    port_range = input("Enter port range (e.g., 1-1024) or press Enter for default: ")
    call(["python", "scanning.py"])
    
    try:
        if port_range:
            start_port, end_port = map(int, port_range.split('-'))
        else:
            start_port, end_port = 1, 1024

        open_ports = await scan_ports(target_ip, start_port, end_port)
        
        if open_ports:
            print(f"Open ports on {target_ip}: {', '.join(map(str, open_ports))}")
        else:
            print(f"No open ports found on {target_ip}.")
    
    except ValueError:
        print("Invalid port range. Please enter in the format 'start-end' (e.g., '20-80').")
    except KeyboardInterrupt:
        print("\nScan interrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_task())
    
    while True:
        usr_input = input("Press 'q' to exit...").strip().lower()
        if usr_input == 'q':
            start_another_program()
            sys.exit

def start_another_program():
    os.system('hell.py')

if __name__ == "__main__":
    main()

print("Press Enter to exit...")
input()

1







