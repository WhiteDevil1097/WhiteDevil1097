import socket
import requests
import colorama
from colorama import Fore,Style

# some decorations for giving it a good look and feel.
colorama.init()
print(Fore.YELLOW + Style.BRIGHT)
print()
print(r"        /$$$$$$  ")
print(r"       /$$__  $$  ")
print(r"      | $$  \ $$  /$$$$$$   /$$$$$$  /$$$$$$$   ")
print(r"      | $$  | $$ /$$__  $$ /$$__  $$| $$__  $$  ")
print(r"      | $$  | $$| $$  \ $$| $$$$$$$$| $$  \ $$  ")
print(r"      | $$  | $$| $$  | $$| $$_____/| $$  | $$  ")
print(r"      |  $$$$$$/| $$$$$$$/|  $$$$$$$| $$  | $$  ")
print(r"       \______/ | $$____/  \_______/|__/  |__/  ")
print(r"                | $$                            ")
print(r"                | $$                            ")
print(r"                |__/                            ")
print(r"                                  /$$            ")
print(r"                                 | $$            ")
print(r"   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$   /$$$$$$$ ")
print(r"  /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/  /$$_____/ ")
print(r" | $$  \ $$| $$  \ $$| $$  \__/  | $$   |  $$$$$$  ")
print(r" | $$  | $$| $$  | $$| $$        | $$ /$$\____  $$ ")
print(r" | $$$$$$$/|  $$$$$$/| $$        |  $$$$//$$$$$$$/ ")
print(r" | $$____/  \______/ |__/         \___/ |_______/  ")
print(r" | $$                                              ")
print(r" | $$                                              ")
print(r" |__/                                              ")
print(r"            »»»Devoloper By White_Devil«««         ")
print()
# Function to scan for open ports on the target
def scan_open_ports(target, ports_to_check):
    print(f"Scanning {target} for open ports...")
    open_ports = []
    for port in ports_to_check:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    if open_ports:
        print(f"Open ports on {target}: {open_ports}")
    else:
        print(f"No open ports found on {target}.")

# Function to check HTTP headers for potential security issues
def check_http_headers(url):
    print(f"Checking HTTP headers for {url}...")
    try:
        response = requests.get(url)
        headers = response.headers

        # Print out the headers
        for header, value in headers.items():
            print(f"{header}: {value}")

        # Basic checks for security-related headers
        security_headers = ['X-Content-Type-Options', 'Strict-Transport-Security', 'Content-Security-Policy', 'X-Frame-Options']
        for header in security_headers:
            if header not in headers:
                print(f"Warning: Missing security header -> {header}")
    except Exception as e:
        print(f"Error checking headers: {e}")

if __name__ == "__main__":
    # Target host and URL
    target_host = input("Enter the target host (IP or domain name): ")
    target_url = input("Enter the target URL (e.g., http://example.com): ")

    # List of common ports to check for open ports
    common_ports = [21, 22, 23, 80, 443, 3306, 8080]

    # Scanning for open ports
    scan_open_ports(target_host, common_ports)

    # Checking for HTTP header vulnerabilities
    check_http_headers(target_url)
