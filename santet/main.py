#Santet Indonesia DDoS Tools
#Author : XV1N2
import os
import colorama
from methods.udp import UDP
import argparse
import sys
import ipaddress
from urllib.parse import urlparse

version = 1.0
red = colorama.Fore.RED
green = colorama.Fore.GREEN
magenta = colorama.Fore.MAGENTA
reset = colorama.Fore.RESET

os.system("title Santet By XV1N2")

def parse_target(url):
    return urlparse(url).netloc

def main():
    parser = argparse.ArgumentParser(description="Santet Indonesia DDoS Tools.", usage="python3 main.py [-t target] [-m methods type] [-th num threads] [-tm times]")
    parser.add_argument('-t', '--target', help='Ip/Domain Host', metavar='target')
    parser.add_argument('-m', '--methods', help='DDoS methods (Use -lm / --list-methods)', metavar='methods_type')
    parser.add_argument('-th', '--threads', help='Threads for attack (default: 80)', type=int, default=0.1, metavar='num_threads')
    parser.add_argument('-tm', '--timeout', help='Time when connection error (default: 10)', type=int, metavar='times')
    parser.add_argument('-v', '--version', help='Tools version', required=False, action='store_true')
    parser.add_argument('-lm', '--list-methods', help='Showing all tools methods', required=False, action='store_true')

    if len(sys.argv) <= 1:
        parser.parse_args(['-h'])
        sys.exit(0)
    else:
        args = parser.parse_args()
        if args.version:
            print(version)
        if args.target:
            try:
                if args.target.startswith((('http://', 'https://', 'www.'))):
                    types = "website"
                else:
                    ipaddress.ip_address(args.target)
                    types = "ip"
            except:
                print(red + "[!] Target isn`t valid. Try use ip / http:// or https://")
                sys.exit(0)
        

        if args.list_methods:
            print(magenta + "[=] Santet DDoS Methods [=]\n[+] UDP\n[!] To using the methods: -m or --methods\n" + reset)
            sys.exit(0)
        
        if args.methods:
            methods_type = ['UDP']
            if args.methods.upper() not in methods_type:
                print(red + "[!] Unknown methods. use -lm or --list-methods" + reset)

        if args.target is None:
            print(red + '[!]Target can`t be empty. use -t or --target your_target' + reset)
            sys.exit(0)
        if args.methods is None:
            print(red + '[!]Methods can`t be empty. try use -m or --methods\n[!]For list -lm or --list-methods' + reset)
            sys.exit(0)

        if args.methods.upper == "UDP":
            send = UDP(args.target, args.thread, args.timeout)
            send.attack()

if __name__ == "__main__":
    main()