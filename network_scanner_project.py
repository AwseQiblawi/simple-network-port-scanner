import socket
from sys import *
 
defult_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 8080]
 
def scan_port(host, port, timeout=1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((host, port))
        return result == 0
    finally:
        sock.close()
 
def scan_host(host, ports):
    print(f"Scanning {host}... \n")
    for port in ports:
        is_open = scan_port(host, port)
        status = "OPEN" if is_open else "CLOSED"
        print(f"Port {port:<5} {status}")
 
if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python scanner.py <host> [port1 port2 ...]")
        exit(1)
    target_host = argv[1]

    if len(argv) > 2:
        ports_to_scan = [int(p) for p in argv[2:]]
    else:
        ports_to_scan = defult_ports
 
    scan_host(target_host, ports_to_scan)
 