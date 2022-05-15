#!/usr/local/bin/python3.9
import socket
import sys
import urllib.request

class Verify:
    def __init__(self, ip):
        self.ip = ip
        self.base_url = "https://verify.cpanel.net/app/verify?ip="
        self.lookup_url = self.base_url + self.ip + "&nohtml=1"

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, ip):
        try:
            socket.inet_pton(socket.AF_INET, ip)
            self._ip = ip
        except:
            socket.error
            print("Not a valid IPv4 address!")
            exit()

    def check(self):
        with urllib.request.urlopen(self.lookup_url) as response:
            page = response.read()
            page = str(page.decode("utf-8"))
            if page:
                print("License data for IP address:", self.ip)
                print(page)
                print(self.lookup_url.split("&")[0])
            else:
                print("No license found for this IP")

def main():
    if len(sys.argv) > 1:
        Verify(sys.argv[1]).check()
    else:
        print("Please provide an IP")
        exit()

if __name__ == '__main__':
    main()
