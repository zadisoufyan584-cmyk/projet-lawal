import socket
from concurrent.futures import ThreadPoolExecutor

print("--- Scanner Sari3 V5 ---")
target = input("Achno site bghiti? ")
ports = range(1, 101)

def scan_port(port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((target, port))
        print(f"[+] Port {port} MEHLOUL")
        s.close()
    except:
        pass

print(f"Kan9elleb f {target}...")
with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scan_port, ports)
print("Sala l-scan!")
