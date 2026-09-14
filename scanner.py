#!/usr/bin/env python3
# TBH-PortScanner - Fast Port Scanner + Banner Grab + CVE Hint
# Tulungagung Black Hat - uchil404 | Educational Only

import socket
import argparse
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

BANNER = """\033[91m╔══════════════════════════════════════╗
\033[91m║ \033[97mTBH-PortScanner \033[91m- Fast & Smart       \033[91m║
\033[91m║ \033[90mTulungagung Black Hat | uchil404   \033[91m║
\033[91m╚══════════════════════════════════════╝\033[0m"""

# Common ports with CVE hints
PORT_INFO = {
    21: "FTP - Check anonymous login, CVE-2020-15782",
    22: "SSH - Brute force, CVE-2018-15473",
    23: "Telnet - Plaintext, disable!",
    25: "SMTP - Open relay check",
    53: "DNS - Zone transfer",
    80: "HTTP - Dir busting, OWASP",
    110: "POP3 - Plain auth",
    135: "RPC - EternalBlue check",
    139: "NetBIOS - SMB enum",
    443: "HTTPS - SSL scan",
    445: "SMB - EternalBlue MS17-010",
    3306: "MySQL - Root brute, CVE-2012-2122",
    3389: "RDP - BlueKeep CVE-2019-0708",
    5432: "PostgreSQL - brute",
    6379: "Redis - Unauthorized CVE-2022-0543",
    8080: "HTTP-Alt - Proxy/Jenkins",
    8443: "HTTPS-Alt - Tomcat",
}

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        result = s.connect_ex((target, port))
        if result == 0:
            banner = ""
            try:
                s.settimeout(2)
                # Try banner grab
                if port in [21,22,25,80,110]:
                    s.send(b"HEAD / HTTP/1.0\r\n\r\n" if port in [80,8080,8443] else b"\r\n")
                    banner = s.recv(1024).decode(errors='ignore').strip().split('\n')[0][:60]
            except:
                pass
            info = PORT_INFO.get(port, "Unknown - manual enum")
            return (port, True, banner, info)
        s.close()
    except:
        pass
    return (port, False, "", "")

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="TBH-PortScanner - Educational Fast Scanner")
    parser.add_argument("-t","--target", required=True, help="Target IP/domain")
    parser.add_argument("-p","--ports", default="1-1000", help="Ports: 80,443 atau 1-1000 atau top100 (default 1-1000)")
    parser.add_argument("--top100", action="store_true", help="Scan top 100 common ports")
    parser.add_argument("-T","--threads", type=int, default=100, help="Threads (default 100)")
    args = parser.parse_args()

    target = args.target
    try:
        ip = socket.gethostbyname(target)
        print(f"\033[96m[*] Target: {target} ({ip}) | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\033[0m")
    except:
        print(f"\033[91m[!] Cannot resolve {target}\033[0m"); sys.exit(1)

    # Parse ports
    ports = []
    if args.top100:
        ports = list(PORT_INFO.keys())
    elif "-" in args.ports:
        a,b = args.ports.split("-")
        ports = list(range(int(a), int(b)+1))
    elif "," in args.ports:
        ports = [int(p.strip()) for p in args.ports.split(",")]
    else:
        ports = [int(args.ports)]

    print(f"\033[93m[*] Scanning {len(ports)} ports with {args.threads} threads...\033[0m")
    print("\033[90m" + "="*65 + "\033[0m")
    open_ports = []
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        results = list(executor.map(lambda p: scan_port(ip, p), ports))
    
    for port, is_open, banner, info in sorted(results):
        if is_open:
            open_ports.append(port)
            banner_str = f" | {banner}" if banner else ""
            print(f"\033[92m[OPEN] {port:5d} \033[97m{info[:40]:40s}\033[90m{banner_str}\033[0m")
    
    print("\033[90m" + "="*65 + "\033[0m")
    if open_ports:
        print(f"\033[92m[✓] Found {len(open_ports)} open ports: {open_ports}\033[0m")
        print(f"\033[93m[!] Next: nmap -sV -p {','.join(map(str,open_ports))} {target} untuk version detection\033[0m")
        print(f"\033[90m[!] Hanya untuk target milik sendiri / bug bounty scope!\033[0m")
    else:
        print(f"\033[90m[-] No open ports in range\033[0m")

if __name__ == "__main__":
    main()
