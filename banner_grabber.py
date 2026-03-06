# banner_grabber.py — Service Banner Grabber
import socket

def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except:
        return None

if __name__ == "__main__":
    ip = input("Enter target IP: ")
    ports = [21, 22, 80, 8080]
    print(f"\nGrabbing banners from {ip}...\n")
    for port in ports:
        banner = grab_banner(ip, port)
        if banner:
            print(f"  Port {port}: {banner[:50]}")
        else:
            print(f"  Port {port}: no banner")