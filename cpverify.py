#!/usr/local/bin/python3.9
import socket
import sys
import urllib.request

class Vars:
    if len(sys.argv) > 1:
        ip_addr = sys.argv[1]
    else:
        print("Please provide an IP")
        exit()
    url = 'https://verify.cpanel.net/app/verify?ip=' + ip_addr + '&nohtml=1'

def is_ipv4():
    try:
        socket.inet_pton(socket.AF_INET, Vars.ip_addr)
        return True
    except:
        socket.error
        print("Not a valid IP address!")
        return False

def main():
    if is_ipv4():
        print("License data for IP address:", Vars.ip_addr + "\n")
        with urllib.request.urlopen(Vars.url) as response:
            html = response.read()
            html = str(html.decode('utf-8'))
            if html:
                print(html)
                print(Vars.url.split('&')[0])
            else:
                print("No license found")

if __name__ == '__main__':
    main()
