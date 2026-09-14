# TBH-PortScanner - Fast Port Scanner + CVE Hint

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Speed-100%20Threads-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Purpose-Bug%20Bounty%20%7C%20Educational-green?style=for-the-badge">
</p>

> **⚠️ EDUCATIONAL ONLY** - Untuk scan target milik sendiri / dalam scope bug bounty yang diizinkan. Jangan scan tanpa izin.

Oleh **uchil404 | Tulungagung Black Hat**

---

### ✨ Features
- ⚡ **100 Threads** - Scan 1-1000 port dalam detik
- 🎯 **CVE Hint** - Tiap port ada hint CVE & teknik enum (ex: 445 EternalBlue, 3389 BlueKeep)
- 📡 **Banner Grab** - Ambil banner FTP/SSH/HTTP
- 🔧 **Fleksibel** - Range `1-1000`, list `80,443`, atau `--top100`
- 📊 **Colored Output** - Mudah dibaca untuk report

### 📦 Install
```bash
git clone https://github.com/TulungagungBlackHat/TBH-PortScanner
cd TBH-PortScanner
python3 scanner.py -t 127.0.0.1 --top100
```

### 🚀 Usage
```bash
# Top 100 common ports (recommended)
python3 scanner.py -t example.com --top100

# Range
python3 scanner.py -t 192.168.1.1 -p 1-1000

# Specific ports
python3 scanner.py -t example.com -p 80,443,8080,8443

# Custom threads
python3 scanner.py -t example.com --top100 -T 200
```

**Contoh:**
```
[*] Target: 127.0.0.1 (127.0.0.1)
[OPEN]    22 SSH - Brute force, CVE-2018-15473
[OPEN]    80 HTTP - Dir busting, OWASP
[OPEN]   443 HTTPS - SSL scan
[✓] Found 3 open ports: [22, 80, 443]
[!] Next: nmap -sV -p 22,80,443 127.0.0.1
```

### 🛡️ Ethical
Hanya untuk:
- ✅ Lab/localhost
- ✅ VPS milik sendiri
- ✅ Bug bounty dengan scope yang mengizinkan port scan

### 👥 Credits
uchil404 - Tulungagung Black Hat

### 📄 License
MIT
