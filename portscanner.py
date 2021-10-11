import socket
import ipaddress
import re
from colorama import *
print('port scanner')

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535

open_ports = []
while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        print("You entered a valid ip address.")
        break
    except:
        print("You entered an invalid ip address")
    

while True:
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break
for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.001)
            s.connect((ip_add_entered, port))
            open_ports.append(port)

    except:
    	print(Fore.RED)
    	print(f"Port {port} is closed on {ip_add_entered}")

for port in open_ports:
    print(Fore.GREEN + Back.BLUE)
    print(f"Port {port} is open on {ip_add_entered}")