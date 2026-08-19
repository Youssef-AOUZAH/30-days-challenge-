# Day 2: Python Port Scanner CLI

A simple command-line interface (CLI) tool built in Python to perform local TCP port scanning. This project was built as part of the 30 Days Challenge.

## Overview

This project provides a basic demonstration of how to use Python's built-in `socket` and `argparse` libraries to probe TCP ports. It includes two scanning modes:
1. Scanning specific user-defined ports.
2. Quickly scanning a predefined list of the top 100 most common TCP ports based on Nmap's dataset.

## Files
* `cli.py`: The main entry point that handles command-line arguments using `argparse`.
* `ping_tcp.py`: The core logic file containing the socket connection handling and the Nmap top 100 TCP ports list.

## Usage

You can run the scanner from your terminal using Python.

### Scan Specific Ports
Pass the target IP address and the specific port(s) you want to test using the `-p` or `--port` flag.

```bash
python cli.py 127.0.0.1 -p 80 443 8080
```

### Scan the Top 100 Ports
Use the `F` (Fast) argument to automatically test the top 100 most common TCP ports against the target IP.

```bash
python cli.py 127.0.0.1 -p F
```

## Safety & Ethics
**Important:** This script is intended for educational purposes and local testing (e.g., scanning `127.0.0.1` or authorized internal devices). Ensure you have explicit permission before running port scanning tools against any network or host.
