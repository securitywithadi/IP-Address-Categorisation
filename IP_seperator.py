#This code would help in seperating public/private IP

import ipaddress #Import this Python Library before code execution

with open('ips.txt') as f: #ips.txt to be put up on the same folder as this code
    ips = f.readlines()

private_ips = [ip.strip() for ip in ips if ipaddress.ip_address(ip.strip()).is_private]
public_ips = [ip.strip() for ip in ips if not ipaddress.ip_address(ip.strip()).is_private]

result = {"private": private_ips, "public": public_ips}
print(result)
