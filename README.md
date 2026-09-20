# simple-network-port-scanner
This port scanner is made using pyton checking whether the given ports on a given host are open or closed. This project helps you understand the basics of sockets and networking basics in python.


Features
Scans a list of common ports by default (SSH, HTTP, HTTPS, MySQL, RDP, etc.)
Supports custom port lists via command-line arguments
Simple, dependency-free — pure Python standard library
Requirements
Python 3.x
Usage

Scan default ports on a host:

bash
python scanner.py 127.0.0.1

Scan specific ports:

bash
python scanner.py 127.0.0.1 22 80 443
Example Output
$ python scanner.py 127.0.0.1

Scanning 127.0.0.1...

Port 22    OPEN
Port 80    OPEN
Port 443   OPEN
Port 3306  CLOSED
Disclaimer

Only scan hosts you own or have explicit authorization to test. Unauthorized port scanning may be illegal in your jurisdiction.
