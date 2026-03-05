# Version 2 - testing staging
# port_scanner.py — Basic Port Scanner
import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0  # True = port is open
    except Exception as e:
        return False

if __name__ == "__main__":
    host = input("Enter host to scan: ")
    print(f"\nScanning {host}...\n")
    for port in [21, 22, 23, 80, 443, 3389]:
        status = "OPEN" if scan_port(host, port) else "closed"
        print(f"  Port {port}: {status}")