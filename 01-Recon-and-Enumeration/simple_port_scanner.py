
import requests

# 1. Target host configuration (Localhost or target IP):
target_host = "http://127.0.0.1"

# 🔍 Critical reconnaissance port pool (HTTP, HTTPS, SSH, FTP):
ports = [80, 443, 8080, 8081, 22, 21]

print(f"[*] Reconnaissance started on target: {target_host}...\n")

# 🔄 2. Main automation loop:
for port in ports:
    
    # Dynamically build the target URL structure for each port:
    url = f"{target_host}:{port}"
    
    # 🛡️ Exception handling matrix:
    try:
        # Timeout set to 2 seconds to prevent the script from hanging on closed ports:
        response = requests.get(url, timeout=2)
        
        # If the server responds, the port is open:
        print(f"[+] SUCCESS: Port {port} is OPEN! (Status Code: {response.status_code})")
        
    except requests.exceptions.ConnectionError:
        # Connection refused indicates a closed port:
        print(f"[-] Port {port}: CLOSED (Connection refused).")
        
    except requests.exceptions.Timeout:
        # Timeout indicates a potential network filter or Firewall intervention:
        print(f"[!] Port {port}: FILTERED / SUSPICIOUS (Timeout occurred).")

print("\n[+] PORT SCANNING OPERATION COMPLETED SUCCESSFULLY!")
