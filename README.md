# TBH-PortScanner

<p align="center">
  <a href="https://github.com/TulungagungBlackHat/TBH-PortScanner/actions/workflows/ci.yml"><img src="https://github.com/TulungagungBlackHat/TBH-PortScanner/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/license-MIT-red.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/platform-Termux%20%7C%20Linux%20%7C%20Kali-000000.svg" alt="Platform">
</p>

Fast, threaded TCP port scanner with banner grabbing and JSON export. Single file, standard library only — no Nmap required.

Part of the [Tulungagung Black Hat](https://github.com/TulungagungBlackHat) toolset.

## Features

- **100 concurrent threads** — top-100 ports in seconds on a mobile connection
- **Flexible port ranges** — presets (`top100`), ranges (`1-1000`), or explicit lists (`80,443,8080`)
- **Banner grabbing** — service hints from the first response bytes
- **JSON output** — pipe results into reporting or other tooling
- **Standard library only** — works on stock Termux, Kali, or any Linux box

## Install

```bash
git clone https://github.com/TulungagungBlackHat/TBH-PortScanner
cd TBH-PortScanner
python3 scanner.py --help
```

No `pip install` needed — it's pure standard library.

## Usage

```
usage: scanner.py [-h] -t TARGET [-p PORTS] [-T THREADS] [--json JSON]

options:
  -t, --target TARGET   Target (IP or hostname)
  -p, --ports PORTS     top100 | 1-1000 | 80,443,8080
  -T, --threads THREADS Concurrent threads (default: 100)
  --json JSON           Save results as JSON
```

### Examples

Default top-100 ports:

```bash
python3 scanner.py -t 127.0.0.1
```

Custom range, more threads, JSON export:

```bash
python3 scanner.py -t example.com -p 1-1000 -T 150 --json result.json
```

Specific ports:

```bash
python3 scanner.py -t 192.168.1.1 -p 22,80,443,8080
```

## Sample Output

```
[*] example.com (93.184.216.34)
[*] Scanning 100 ports with 100 threads
[✓] Found 3 open
    80    http    HTTP/1.1 200 OK
    443   https   nginx
    8080  http    Apache
[✓] JSON saved: result.json
```

## Authorized Use Only

Scan only hosts you own or are explicitly authorized to test. Port scanning without permission violates most programs' ToS and many national laws. See [SECURITY.md](SECURITY.md).

## Related Tools

- [TBH-Recon](https://github.com/TulungagungBlackHat/TBH-Recon) — full web recon in one pass
- [TBH-AllScan](https://github.com/TulungagungBlackHat/TBH-AllScan) — port scan plus 9 more checks with risk scoring

## License

[MIT](LICENSE) — Tulungagung Black Hat, East Java, Indonesia. Always Smile :)
