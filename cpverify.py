#!/usr/local/bin/python3.9

import argparse
import urllib.request

#Argparse
parser = argparse.ArgumentParser(
        description="cPanel license IP validation tool")
parser.add_argument('-ip', required=True, help="IP Address to check", dest="ip")
args = parser.parse_args()
ip_addr = args.ip
url = 'https://verify.cpanel.net/app/verify?ip=' + ip_addr + '&nohtml=1'

def main():
    print("License data for IP address:" + ip_addr + "\n")
    with urllib.request.urlopen(url) as response:
        html = response.read()
        html = str(html.decode('utf-8'))
        print(html)

if __name__ == '__main__':
    main()
