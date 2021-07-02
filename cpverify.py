#!/usr/local/bin/python3.9
import socket
import argparse
import urllib.request

#Argparse
parser = argparse.ArgumentParser(
        description="cPanel license IP validation tool", usage="[IP Address]")
parser.add_argument('-ip', required=True, help="IP Address to check", dest="ip")
args = parser.parse_args()
ip_addr = args.ip
url = 'https://verify.cpanel.net/app/verify?ip=' + ip_addr + '&nohtml=1'

def is_ipv4():
    try:
        socket.inet_pton(socket.AF_INET, ip_addr)
        return True
    except:
        socket.error
        print("Not a valid IP address!")
        return False

def main():
    if is_ipv4():
        print("License data for IP address:" + ip_addr + "\n")
        with urllib.request.urlopen(url) as response:
            html = response.read()
            html = str(html.decode('utf-8'))
            print(html)

if __name__ == '__main__':
    main()
