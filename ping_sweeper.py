# ping_sweeper.py — ICMP Ping Sweeper
import subprocess
import platform

def ping_host(ip):
    system = platform.system().lower()
    flag = "-n" if system == "windows" else "-c"
    result = subprocess.run(
        ["ping", flag, "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0  # True = host is alive

if __name__ == "__main__":
    base = input("Enter network base (e.g. 192.168.1): ")
    print(f"\nSweeping {base}.1 - {base}.10 ...\n")
    for i in range(1, 11):
        ip = f"{base}.{i}"
        status = "🟢 ALIVE" if ping_host(ip) else "🔴 dead"
        print(f"  {ip} → {status}")