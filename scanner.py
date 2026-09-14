#!/usr/bin/env python3
# TBH-PortScanner v2.0 Pro - JSON + Fast
import socket, argparse, sys, json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

BANNER = """\033[91m╔══════════════════════════════════════╗
\033[91m║ \033[97mTBH-PortScanner v2.0 Pro \033[91m- JSON/Fast \033[91m║
\033[91m║ \033[90mTulungagung Black Hat | uchil404   \033[91m║
\033[91m╚══════════════════════════════════════╝\033[0m"""

PORT_INFO={21:"FTP anon CVE-2020-15782",22:"SSH",80:"HTTP OWASP",443:"HTTPS",445:"SMB MS17-010",3306:"MySQL",3389:"RDP BlueKeep",6379:"Redis",8080:"HTTP-Alt"}

def scan_port(target, port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.settimeout(1)
    try:
        if s.connect_ex((target,port))==0:
            return {"port":port,"open":True,"info":PORT_INFO.get(port,"Unknown")}
        s.close()
    except: pass
    return {"port":port,"open":False}

def main():
    print(BANNER)
    parser=argparse.ArgumentParser(description="v2.0 Pro")
    parser.add_argument("-t","--target",required=True,help="Target")
    parser.add_argument("-p","--ports",default="top100",help="top100 atau 1-1000 atau 80,443")
    parser.add_argument("-T","--threads",type=int,default=100)
    parser.add_argument("--json",help="Save JSON")
    args=parser.parse_args()
    target=args.target
    try: ip=socket.gethostbyname(target)
    except: print("[!] Cannot resolve"); sys.exit(1)
    print(f"[*] {target} ({ip})")
    if args.ports=="top100": ports=list(PORT_INFO.keys())
    elif "-" in args.ports: a,b=args.ports.split("-"); ports=list(range(int(a),int(b)+1))
    elif "," in args.ports: ports=[int(p) for p in args.ports.split(",")]
    else: ports=[int(args.ports)]
    print(f"[*] Scanning {len(ports)} ports with {args.threads} threads")
    with ThreadPoolExecutor(max_workers=args.threads) as ex:
        results=list(ex.map(lambda p: scan_port(ip,p), ports))
    open_ports=[r for r in results if r["open"]]
    for r in open_ports: print(f"[OPEN] {r['port']} {r['info']}")
    print(f"[✓] Found {len(open_ports)} open")
    if args.json:
        open(args.json,'w').write(json.dumps({"target":target,"ip":ip,"open_ports":open_ports,"all":results},indent=2))
        print(f"[✓] JSON saved: {args.json}")

if __name__=="__main__": main()
